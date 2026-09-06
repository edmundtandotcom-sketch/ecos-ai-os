from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def region(start_marker, end_marker, new):
    global s
    a = s.index(start_marker)
    b = s.index(end_marker, a)
    s = s[:a] + new + s[b:]


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:70])
    s = s.replace(old, new)


# ------------------------------------------------------------------ tighten
region("def tighten(pieces, speed=1.0):", "# ============================================================== shots\n", '''def tighten(pieces, speed=1.0):
    """pieces: [(label, t_lo, t_hi), ...] in edit order.

    SYNC BY CONSTRUCTION. Every segment becomes EXACTLY N video frames
    (N = round(len/speed*FPS)) and EXACTLY N/FPS seconds of PCM audio, so the
    concatenated video and the concatenated audio share one timeline to the
    sample. The old per-segment AAC files left a ~30ms timestamp gap at every
    join that a player honoured but the final filter graph packed shut - the
    speech ran 1.8s late by 50s (measured 2026-09-05).

    Returns (tight_video.mp4 [video only], tight_audio.wav, words, smap).
    """
    plan = []
    for label, lo, hi in pieces:
        words = json.loads((WORK / f"words_{label}.json").read_text(encoding="utf-8"))
        for a, b in plan_segments(words, lo, hi):
            plan.append((label, a, b))
    nfs = [int(round((b - a) / speed * FPS)) for _, a, b in plan]
    tag = f"_s{int(round(speed * 100))}x"   # x = exact-length segments, PCM audio
    stamp = WORK / f"_tight{tag}.json"
    vpath = WORK / f"_tight{tag}_v.mp4"
    apath = WORK / f"_tight{tag}_a.wav"
    segdir = WORK / f"_tight{tag}"
    segdir.mkdir(parents=True, exist_ok=True)
    key = json.dumps([list(x) for x in plan])
    if vpath.exists() and apath.exists() and stamp.exists() and stamp.read_text() == key:
        print(f"  tight cut cached ({len(plan)} segments)")
    else:
        for old in list(segdir.glob("seg*.mp4")) + list(segdir.glob("seg*.wav")):
            try:
                old.unlink()
            except PermissionError:
                pass
        vparts, aparts = [], []
        for i, ((label, a, b), N) in enumerate(zip(plan, nfs)):
            qv = segdir / f"seg{i:03d}.mp4"
            qa = segdir / f"seg{i:03d}.wav"
            # --- video: exactly N frames. The phone take drops frames in
            # bursts, so speed changes go through motion-compensated
            # interpolation; it repeats its first/last frames, so interpolate
            # with 2 source frames of context each side and trim to N.
            e = 2.0 / FPS
            a2 = max(0.0, a - e)
            lead = int(round((a - a2) / speed * FPS))
            vf = f"scale={W}:{H},setsar=1"
            if speed != 1.0:
                vf += (f",setpts=PTS/{speed},minterpolate=fps={FPS}:mi_mode=mci:mc_mode=obmc:"
                       f"me_mode=bilat:search_param=16:scd=none")
            vf += (f",tpad=stop_mode=clone:stop_duration=1,trim=start_frame={lead}:end_frame={lead + N},"
                   f"setpts=N/({FPS}*TB)")
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a2:.4f}", "-to", f"{b + e:.4f}", "-i", str(SOURCES[label]),
                 "-vf", vf, "-an", "-frames:v", str(N),
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-bf", "0",
                 "-pix_fmt", "yuv420p", "-r", str(FPS), "-video_track_timescale", "90000", str(qv)])
            # --- audio: exactly N/FPS seconds of PCM from the exact range
            af = f"atempo={speed}," if speed != 1.0 else ""
            af += f"apad,atrim=end={N / FPS:.6f},asetpts=N/SR/TB"
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a:.4f}", "-to", f"{b:.4f}", "-i", str(SOURCES[label]),
                 "-vn", "-af", af, "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", str(qa)])
            got = int(ffprobe(qv, "stream=nb_frames")["streams"][0]["nb_frames"])
            if got != N:
                raise RuntimeError(f"segment {i}: {got} frames, wanted {N}")
            vparts.append(qv)
            aparts.append(qa)
        for parts, dest in ((vparts, vpath), (aparts, apath)):
            lst = segdir / ("concat_" + dest.suffix[1:] + ".txt")
            lst.write_text("".join(f"file '{q.resolve().as_posix()}'\\n" for q in parts), encoding="utf-8")
            run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                 "-i", str(lst), "-c", "copy", str(dest)])
        nv = int(ffprobe(vpath, "stream=nb_frames")["streams"][0]["nb_frames"])
        da = dur_of(apath)
        if nv != sum(nfs) or abs(da - sum(nfs) / FPS) > 0.002:
            raise RuntimeError(f"tight mismatch: video {nv} frames vs {sum(nfs)}, audio {da:.3f}s vs {sum(nfs)/FPS:.3f}")
        stamp.write_text(key, encoding="utf-8")
    durs = [N / FPS for N in nfs]
    out, base, smap = [], 0.0, []
    for (label, a, b), d in zip(plan, durs):
        words = json.loads((WORK / f"words_{label}.json").read_text(encoding="utf-8"))
        for w in words:
            if a - 0.001 <= w["s"] < b:
                out.append(dict(w=w["w"], s=round(base + max(0.0, (w["s"] - a) / speed), 3),
                                e=round(base + min(d, max(0.0, (w["e"] - a) / speed)), 3)))
        smap.append(dict(label=label, src0=a, src1=b, out0=round(base, 3), out1=round(base + d, 3)))
        base += d
    raw = sum(hi - lo for _, lo, hi in pieces)
    print(f"  tight @{speed:.2f}x: {raw:.1f}s -> {base:.1f}s  ({sum(nfs)} frames, audio {dur_of(apath):.3f}s)")
    out = fix_tokens(out)
    (WORK / "words_tight.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    (WORK / "words_tight.txt").write_text(
        "\\n".join(f"{w['s']:7.2f} {w['w']}" for w in out), encoding="utf-8")
    return vpath, apath, out, smap


''')

# ------------------------------------------------------------------ shots on the frame grid
rep('''        t0 = max(0.0, cue[0]["s"] - 0.10)
        t1 = min(total, cue[-1]["e"] + 0.12)
        if t1 - t0 < 0.30:
            continue''',
    '''        # shot boundaries live on the frame grid so the video timeline equals
        # the audio timeline exactly (sum of nf/FPS == t1)
        t0 = round(max(0.0, cue[0]["s"] - 0.10) * FPS) / FPS
        t1 = round(min(total, cue[-1]["e"] + 0.12) * FPS) / FPS
        if t1 - t0 < 0.30:
            continue''')
rep('''    for i in range(len(shots) - 1):
        shots[i]["t1"] = shots[i + 1]["t0"]
    shots[-1]["t1"] = total''',
    '''    for i in range(len(shots) - 1):
        shots[i]["t1"] = shots[i + 1]["t0"]
    shots[-1]["t1"] = round(total * FPS) / FPS''')

# ------------------------------------------------------------------ render_shots: video only
region("def render_shots(", "# ============================================================== captions\n", '''def render_shots(shots, tight, work, endcard=None):
    """Encode every shot from the tight VIDEO, video only, exactly nf frames.
    Audio is never cut per shot - it comes from the continuous tight track.
    The shot's caption plate is burned in here (a single-image overlay on the
    long timeline stops compositing on ffmpeg 8.1.2)."""
    sd = work / "shots"
    sd.mkdir(parents=True, exist_ok=True)
    parts, tl = [], 0.0
    for i, s in enumerate(shots):
        nf = int(round((s["t1"] - s["t0"]) * FPS))
        d = nf / FPS
        src_in = ["-ss", f"{s['t0']:.4f}", "-to", f"{s['t1'] + 0.5 / FPS:.4f}", "-i", str(tight)]
        cap = s.get("cap") if s.get("cap_burn", True) else None
        cap_sig = hashlib.md5(Path(cap).read_bytes()).hexdigest() if cap else None
        key = json.dumps({k: v for k, v in s.items()
                          if k not in ("out0", "out1", "dev_id", "text", "cue", "segment_start", "cap", "cap_burn")}
                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig,
                            "src_file": Path(tight).name, "v": 3}, sort_keys=True)
        p = sd / f"h{hashlib.md5(key.encode()).hexdigest()[:12]}.mp4"
        stamp = p.with_suffix(".json")
        if p.exists() and stamp.exists() and stamp.read_text(encoding="utf-8") == key:
            pass
        else:
            ins, chain = [], ""
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
                chain = f"[0:v]crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,{GRADE}{extra},fps={FPS},{mv}[v0]"
            n_in = len([x for x in ins if x == "-i"]) + 1        # + the tight video
            if cap:
                ins_cap = ["-framerate", str(FPS), "-i", str(cap)]
                chain += f";[{n_in}:v]format=rgba[cp];[v0][cp]overlay=0:0[v1]"
            else:
                ins_cap = []
                chain += ";[v0]null[v1]"
            chain += f";[v1]setpts=N/({FPS}*TB)[v]"
            run(["ffmpeg", "-y", "-loglevel", "error", *ins, *src_in, *ins_cap,
                 "-filter_complex", chain, "-map", "[v]", "-an", "-frames:v", str(nf),
                 "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-bf", "0", "-pix_fmt", "yuv420p",
                 "-r", str(FPS), "-video_track_timescale", "90000", str(p)])
            got = int(ffprobe(p, "stream=nb_frames")["streams"][0]["nb_frames"])
            if got != nf:
                raise RuntimeError(f"shot {i}: {got} frames, wanted {nf} ({s['text']})")
        stamp.write_text(key, encoding="utf-8")
        s["out0"] = round(tl, 3)
        tl += d
        s["out1"] = round(tl, 3)
        if abs(s["out0"] - s["t0"]) > 0.002:
            raise RuntimeError(f"shot {i}: timeline drift {s['out0'] - s['t0']:+.3f}s")
        parts.append(p)
    if endcard:
        p = sd / "s_end.mp4"
        n_end = int(round(endcard["secs"] * FPS))
        run(["ffmpeg", "-y", "-loglevel", "error",
             "-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}:d={n_end / FPS:.4f}",
             "-frames:v", str(n_end), "-an",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-bf", "0", "-pix_fmt", "yuv420p",
             "-r", str(FPS), "-video_track_timescale", "90000", str(p)])
        endcard["out0"] = round(tl, 3)
        tl += n_end / FPS
        endcard["out1"] = round(tl, 3)
        parts.append(p)
    lst = work / "shots.txt"
    lst.write_text("".join(f"file '{q.resolve().as_posix()}'\\n" for q in parts), encoding="utf-8")
    cut = work / "_cut.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(cut)])
    nv = int(ffprobe(cut, "stream=nb_frames")["streams"][0]["nb_frames"])
    if nv != int(round(tl * FPS)):
        raise RuntimeError(f"cut has {nv} frames, timeline says {int(round(tl * FPS))}")
    return cut, tl


''')

# ------------------------------------------------------------------ compose: audio from the tight track
rep("def compose(spec, tight, words, smap, out_name):", "def compose(spec, tight, tight_a, words, smap, out_name):")
rep('''    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex_script", "filter.txt", "-map", "[vout]", "-map", "0:a", *ENC, "_body.mp4"],
        cwd=work)''',
    '''    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex_script", "filter.txt", "-map", "[vout]", "-an",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-bf", "0", "-pix_fmt", "yuv420p",
         "-r", str(FPS), "-video_track_timescale", "90000", "_body.mp4"],
        cwd=work)''')
region('''    # ---- final: speed, whooshes, bed, loudness, progress bar ----''', '''    print(f"  OK {final.name}''', '''    # ---- final: continuous speech track + whooshes + bed, loudness, progress bar ----
    out_d = dur_of(part)
    music = spec.get("music", FX.HOUSE["music"])
    music_p = Path(music) if Path(music).is_absolute() else AUDIO / music
    inputs = ["-i", str(part), "-i", str(tight_a), "-stream_loop", "-1", "-i", str(music_p)]
    for _ in segs:
        inputs += ["-i", str(AUDIO / FX.HOUSE["whoosh"])]
    f = ["[1:a]apad[sp0]"]           # speech: one PCM track, padded through the endcard
    mixin = "[sp0]"
    for i, t in enumerate(segs):
        f.append(f"[{3+i}:a]adelay={int(t*1000)}|{int(t*1000)},volume=0.45[wh{i}]")
        mixin += f"[wh{i}]"
    if segs:
        f.append(f"{mixin}amix=inputs={len(segs)+1}:duration=first:dropout_transition=0,"
                 f"volume={len(segs)+1}[sp]")
    else:
        f.append("[sp0]anull[sp]")
    mvol = spec.get("music_vol", MUSIC_VOL)
    f.append(f"[2:a]volume={mvol},afade=t=out:st={out_d-2.0:.2f}:d=2.0[bed]")
    f.append(f"[sp][bed]amix=inputs=2:duration=first:dropout_transition=0,"
             f"loudnorm=I={LOUDNORM_I}:TP=-1.5:LRA=11,aresample=48000[a]")
    f.append("[0:v]null[vs]")
    f.extend(FX.progress_bar(out_d, src="vs", dst="vout", thickness=PROGRESS_BAR))
    OUT.mkdir(parents=True, exist_ok=True)
    final = OUT / out_name
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[a]", "-t", f"{out_d:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(final)])
''')

# ------------------------------------------------------------------ main
rep('''    tight, words, smap = tighten(PIECES, a.speed)
    if a.tighten_only:
        return
    print("== COMPOSE ==")
    name = OUT_NAME.replace(".mp4", f"_{int(round(a.speed * 100))}.mp4")
    compose(SPEC, tight, words, smap, name)''',
    '''    tight_v, tight_a, words, smap = tighten(PIECES, a.speed)
    if a.tighten_only:
        return
    print("== COMPOSE ==")
    name = OUT_NAME.replace(".mp4", f"_{int(round(a.speed * 100))}.mp4")
    compose(SPEC, tight_v, tight_a, words, smap, name)''')

p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("sync-by-construction patch applied")
