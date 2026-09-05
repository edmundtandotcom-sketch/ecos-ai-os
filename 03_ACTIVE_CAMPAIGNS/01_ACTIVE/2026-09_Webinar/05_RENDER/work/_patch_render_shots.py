def render_shots(shots, tight, work, endcard=None):
    """Encode every shot. The shot's caption plate (s["cap"]) is burned in
    HERE, on a clip whose timestamps start at zero - a single-image input on
    the long assembled timeline stops compositing a few seconds in on ffmpeg
    8.1.2 no matter how it is held (loop / tpad / stream_loop all failed,
    2026-09-04), while the same overlay on a fresh clip always draws."""
    sd = work / "shots"
    sd.mkdir(parents=True, exist_ok=True)
    parts, tl = [], 0.0
    for i, s in enumerate(shots):
        d = s["t1"] - s["t0"]
        nf = max(2, int(round(d * FPS)))
        aud = ["-ss", f"{s['t0']:.3f}", "-to", f"{s['t1']:.3f}", "-i", str(tight)]
        cap = s.get("cap")
        cap_sig = hashlib.md5(Path(cap).read_bytes()).hexdigest() if cap else None
        key = json.dumps({k: v for k, v in s.items()
                          if k not in ("out0", "out1", "dev_id", "text", "cue", "segment_start", "cap")}
                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig}, sort_keys=True)
        p = sd / f"h{hashlib.md5(key.encode()).hexdigest()[:12]}.mp4"
        stamp = p.with_suffix(".json")
        if p.exists() and stamp.exists() and stamp.read_text(encoding="utf-8") == key:
            pass
        else:
            ins, chain, amap = [], "", "1:a"
            if s.get("photo"):
                src = FAMILY / s["photo"] if (FAMILY / s["photo"]).exists() else PROPS / s["photo"]
                ins = ["-loop", "1", "-framerate", str(FPS), "-t", f"{d:.3f}", "-i", str(src)]
                chain = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                         f"{GRADE},{FX.move('push', nf)}[v0]")
            elif s.get("backdrops"):
                top, bot = s["backdrops"]
                half = H // 2
                ins = ["-stream_loop", "-1", "-t", f"{d:.3f}", "-i", str(broll(top)),
                       "-stream_loop", "-1", "-t", f"{d:.3f}", "-i", str(broll(bot))]
                chain = (f"[0:v]scale={W}:{half}:force_original_aspect_ratio=increase,crop={W}:{half},{GRADE}[t];"
                         f"[1:v]scale={W}:{half}:force_original_aspect_ratio=increase,crop={W}:{half},{GRADE}[b];"
                         f"[t][b]vstack=inputs=2,fps={FPS},setsar=1[v0]")
                amap = "2:a"
            elif s["backdrop"] and s.get("split"):
                top_h = int(H * 0.50) & ~1
                bot_h = H - top_h
                cx, ey = FACE[s["src"]]
                sy = max(0, min(H - bot_h, int(ey - 0.30 * bot_h)))
                ins = ["-stream_loop", "-1", "-t", f"{d:.3f}", "-i", str(broll(s["backdrop"]))]
                chain = (f"[0:v]scale={W}:{top_h}:force_original_aspect_ratio=increase,crop={W}:{top_h},{GRADE}[t];"
                         f"[1:v]crop={W}:{bot_h}:0:{sy},{GRADE}[b];"
                         f"[t][b]vstack=inputs=2,fps={FPS},setsar=1[v0]")
            elif s["backdrop"]:
                src = PROPS / s["backdrop"] if s["backdrop"].startswith("prop_") else broll(s["backdrop"])
                ins = ["-stream_loop", "-1", "-t", f"{d:.3f}", "-i", str(src)]
                chain = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{GRADE},"
                         f"fps={FPS},{FX.move('push', nf)}[v0]")
            else:
                w, h, x, y = crop_for(ZOOMS[s["zoom"]], s["src"])
                extra = f",{FX.speaker_duotone(s['treat'])}" if s.get("treat") else ""
                mv = FX.move(s["motion"], nf)
                if s.get("frame"):
                    mv += f",{FX.cta_frame()}"
                ins = []
                amap = "0:a"
                chain = f"[0:v]crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,{GRADE}{extra},fps={FPS},{mv}[v0]"
            n_in = len([x for x in ins if x == "-i"]) + 1        # + the tight take
            if cap:
                ins_cap = ["-framerate", str(FPS), "-i", str(cap)]
                chain += f";[{n_in}:v]format=rgba[cp];[v0][cp]overlay=0:0[v]"
            else:
                ins_cap = []
                chain += ";[v0]null[v]"
            run(["ffmpeg", "-y", "-loglevel", "error", *ins, *aud, *ins_cap,
                 "-filter_complex", chain, "-map", "[v]", "-map", amap,
                 "-frames:v", str(nf), *ENC, str(p)])
        stamp.write_text(key, encoding="utf-8")
        s["out0"] = round(tl, 3)
        tl += dur_of(p)
        s["out1"] = round(tl, 3)
        parts.append(p)
    if endcard:
        p = sd / "s_end.mp4"
        run(["ffmpeg", "-y", "-loglevel", "error",
             "-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}:d={endcard['secs']:.3f}",
             "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo:d={endcard['secs']:.3f}",
             "-shortest", *ENC, str(p)])
        endcard["out0"] = round(tl, 3)
        tl += dur_of(p)
        endcard["out1"] = round(tl, 3)
        parts.append(p)
    lst = work / "shots.txt"
    lst.write_text("".join(f"file '{q.resolve().as_posix()}'\n" for q in parts), encoding="utf-8")
    cut = work / "_cut.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(cut)])
    return cut, tl


