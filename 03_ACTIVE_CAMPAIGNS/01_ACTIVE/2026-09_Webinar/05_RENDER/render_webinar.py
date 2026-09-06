#!/usr/bin/env python3
"""
Webinar ad composer - Hook + Body from the 2026-09 outdoor phone takes.

Same architecture as render_ad_v4 (SecondPropertyLadder campaign) but for a
NATIVE 9:16 source: no face crop, the zoom levels are crops around the face
inside the 1080x1920 frame. Includes the tighten stage (pause carving and
re-ordering of takes) so the whole thing runs from the raw files:

    python render_webinar.py                 # tighten -> compose
    python render_webinar.py --tighten-only  # just the cut + words_tight.txt

Foundation: E:\\REMOTION\\ADS_PLAYBOOK.md, ads\\HOUSE_STYLE_ADS.md,
ads\\DEVICE_LIBRARY.md. The ad itself is spec_webinar.py.
"""
import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, r"E:\REMOTION\ads")
import devices as DV                                            # noqa: E402
import devices_house as HD                                      # noqa: E402
import effects as FX                                            # noqa: E402

DEVICES = {**DV.REGISTRY, **HD.REGISTRY}
FULL_FRAME = DV.FULL_FRAME | HD.FULL_FRAME
OVER_SPEAKER = DV.OVER_SPEAKER | HD.OVER_SPEAKER

HERE = Path(__file__).parent
CAMPAIGN = HERE.parent
# Working files live on the LOCAL disk. Drive File Stream locks freshly
# written files while it uploads them (PermissionError on unlink, 2026-09-05)
# and the shot cache is thousands of small encodes. Only out/ stays on Drive.
WORK = Path(r"E:\REMOTION\work\webinar_2026-09")
OUT = HERE / "out"
SOURCES = {"hooks": CAMPAIGN / "1-Webinar Hooks.mp4",
           "body": CAMPAIGN / "2-Webinar Body.mp4"}

BROLL_DIR = Path(r"E:\REMOTION\public\broll\stock")
AUDIO = Path(r"E:\REMOTION\public\audio")
FAMILY = Path(r"E:\REMOTION\public\family")
PROPS = Path(r"E:\REMOTION\public\props")
VFX = Path(r"E:\REMOTION\public\vfx")
SG_BROLL = [p.name for p in sorted(BROLL_DIR.glob("*.mp4"))]
VFX_MANIFEST = json.loads((VFX / "manifest.json").read_text(encoding="utf-8"))

W, H, FPS = 1080, 1920, 30
SPEED = 1.0   # speed is applied in tighten(); the final pass only mixes
LOUDNORM_I = -16
MUSIC_VOL = 0.09
PROGRESS_BAR = 12
WHOOSH_PEAK = 0.89   # seconds into whoosh1.mp3 where the impact sits
GRADE = FX.GRADE

# face centre / eye line in the SOURCE frame (haar on a reference frame)
FACE = {"hooks": (524, 734), "body": (468, 783)}
ZOOMS = [1.00, 1.10, 1.22]
CAP_MAX_WORDS = 3
CAP_Y = 0.80
CAP_SIZE = 82

# pause carving
MAX_GAP, PAD_OUT, PAD_IN = 0.20, 0.10, 0.07

GLUE = [(("$3", ".5"), "$3.5"), (("Park", "Clementis"), "Parc Clematis"),
        (("the", "Triva"), "the Tre Ver"), (("S", "&P"), "S&P"),
        (("1", ",268"), "1,268"), (("1", ",066"), "1,066"), (("2", ",000"), "2,000"),
        (("20", ".86"), "20.86"), (("5", ".87"), "5.87"), (("$2", ",800"), "$2,800"),
        (("$3", ",000"), "$3,000"), (("$3", ".24"), "$3.24"), (("$2", ".7"), "$2.7"),
        (("$2", ".8"), "$2.8"), (("3", "-bedroom"), "3-bedroom"),
        (("Central", "Cashman,"), "Central Catchment,"), (("decision", "-making"), "decision-making"),
        (("top", "-premise"), "top-primary"), (("pressure", "-test"), "pressure-test"),
        (("More", "views"), "Most views")]
FIXES = {"triva": "Tre Ver", "clementis": "Clematis", "aitong": "Ai Tong",
         "temporarily": "temporary", "analysts": "analysis", "tax": "stacks",
         "proving": "proving"}


# ============================================================== helpers

def run(cmd, cwd=None):
    sys.stdout.flush()
    subprocess.run(cmd, check=True, cwd=cwd)


def rel(p, base):
    """Path relative to base when possible - Windows caps a command line at
    32K chars and 114 caption inputs with absolute Drive paths blew it."""
    try:
        return Path(p).resolve().relative_to(Path(base).resolve()).as_posix()
    except ValueError:
        return str(p)


def ffprobe(path, entries="format=duration"):
    return json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries, "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout)


def dur_of(p):
    return float(ffprobe(p)["format"]["duration"])


def broll(name):
    p = BROLL_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"b-roll not found: {name}")
    return p


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def fix_tokens(words):
    out, i = [], 0
    while i < len(words):
        hit = False
        for pair, rep in GLUE:
            n = len(pair)
            if tuple(w["w"] for w in words[i:i + n]) == pair:
                out.append(dict(w=rep, s=words[i]["s"], e=words[i + n - 1]["e"]))
                i += n
                hit = True
                break
        if hit:
            continue
        w = dict(words[i])
        core = w["w"].strip(".,?!")
        key = core.lower()
        if key in FIXES:
            w["w"] = w["w"].replace(core, FIXES[key])
        out.append(w)
        i += 1
    return out


def find_phrase(words, phrase, after=0.0):
    flat, owner = [], []
    for i, w in enumerate(words):
        t = norm(w["w"])
        flat.append(t)
        owner.extend([i] * len(t))
    flat = "".join(flat)
    lo = 0
    while lo < len(owner) and words[owner[lo]]["s"] < after:
        lo += 1
    pos = flat.find(norm(phrase), lo)
    return (words[owner[pos]]["s"], owner[pos]) if pos >= 0 else None


def cue_split(words):
    TRAIL = {"a", "an", "the", "and", "or", "but", "to", "of", "for", "in", "on",
             "at", "is", "are", "was", "your", "my", "i", "we", "you", "it",
             "that", "this", "so", "if", "as", "with"}
    cues, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        gap = (nxt["s"] - w["e"]) if nxt else 99
        joined = " ".join(x["w"] for x in cur)
        hard = w["w"].endswith((".", "?", "!"))
        over = len(cur) > CAP_MAX_WORDS or len(joined) >= 20
        if hard or gap > 0.26 or len(cur) >= CAP_MAX_WORDS or len(joined) >= 17:
            if not hard and nxt is not None and len(cur) < 2:
                continue
            if not hard and nxt is not None and not over and norm(w["w"]) in TRAIL:
                continue
            cues.append(cur)
            cur = []
    if cur:
        cues.append(cur)
    return cues


# ============================================================== tighten
# Carve the dead air out of each take and lay the pieces on ONE timeline in
# the EDIT order (pieces may re-order the take).

def plan_segments(words, t_lo, t_hi):
    ws = [w for w in words if w["e"] > t_lo and w["s"] < t_hi]
    segs = []
    cs = max(t_lo, ws[0]["s"] - PAD_IN)
    prev = ws[0]
    for cur in ws[1:]:
        if cur["s"] - prev["e"] > MAX_GAP:
            segs.append((cs, min(t_hi, prev["e"] + PAD_OUT)))
            cs = max(t_lo, cur["s"] - PAD_IN)
        prev = cur
    segs.append((cs, min(t_hi, prev["e"] + PAD_OUT)))
    return [(math.floor(a * FPS) / FPS, math.ceil(b * FPS) / FPS)
            for a, b in segs if b - a > 1.0 / FPS]


def tighten(pieces, speed=1.0):
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
        for old in list(segdir.glob("seg*.wav")):
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
            have = (qv.exists() and int(ffprobe(qv, "stream=nb_frames")["streams"][0]["nb_frames"]) == N)
            have or run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a2:.4f}", "-to", f"{b + e:.4f}", "-i", str(SOURCES[label]),
                 "-vf", vf, "-an", "-frames:v", str(N),
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-bf", "0",
                 "-pix_fmt", "yuv420p", "-r", str(FPS), "-video_track_timescale", "90000", str(qv)])
            # --- audio: exactly N/FPS seconds of PCM from the exact range
            af = f"atempo={speed}," if speed != 1.0 else ""
            af += f"apad,atrim=end_sample={N * 48000 // FPS},asetpts=N/SR/TB"
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
            lst.write_text("".join(f"file '{q.resolve().as_posix()}'\n" for q in parts), encoding="utf-8")
            run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                 "-i", str(lst), "-c", "copy", str(dest)])
        nv = int(ffprobe(vpath, "stream=nb_frames")["streams"][0]["nb_frames"])
        da = dur_of(apath)
        if nv != sum(nfs) or abs(da - sum(nfs) / FPS) > 0.001:
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
        "\n".join(f"{w['s']:7.2f} {w['w']}" for w in out), encoding="utf-8")
    return vpath, apath, out, smap


# ============================================================== shots

def source_at(smap, t):
    for m in smap:
        if m["out0"] - 0.001 <= t < m["out1"] + 0.001:
            return m["label"]
    return "body"


def crop_for(z, label):
    cx, ey = FACE[label]
    w = int(round(W / z)) & ~1
    h = int(round(H / z)) & ~1
    x = max(0, min(W - w, int(round(cx - w / 2))))
    y = max(0, min(H - h, int(round(ey - 0.36 * h))))
    return w, h, x, y


def build_shots(spec, words, smap, total):
    beats, used_broll = [], set()
    for b in spec["beats"]:
        hit = find_phrase(words, b["at"], b.get("after", 0.0))
        if not hit:
            print(f"  ! anchor missed: '{b['at']}' ({b.get('dev')})")
            continue
        bd = b.get("backdrop")
        if bd:
            if bd in used_broll:
                alt = next((x for x in SG_BROLL if x not in used_broll
                            and not x.startswith(("rx_", "desk_"))), None)
                print(f"  ! {bd} already used - swapping to {alt}")
                b = {**b, "backdrop": alt}
                bd = alt
            used_broll.add(bd)
        t0 = max(0.0, hit[0] + b.get("lead", 0.0))
        b = {**b, "t0": t0, "t1": min(total, t0 + b["secs"]), "widx": hit[1]}
        # accumulating captions take their word timings from the transcript
        if b.get("dev") == "accum_caption" and "times" not in b.get("params", {}):
            ws = b["params"]["words"]
            times = []
            for k in range(len(ws)):
                wi = hit[1] + k
                times.append(max(0.0, (words[wi]["s"] if wi < len(words) else t0) - t0))
            b["params"] = {**b["params"], "times": times}
        beats.append(b)

    # split cues so a beat starts on its own shot
    cut_points = sorted({b["t0"] for b in beats})
    cues = []
    for cue in cue_split(words):
        cur = cue
        for cp in cut_points:
            if cur[0]["s"] + 0.20 < cp < cur[-1]["e"] - 0.20:
                k = next((i for i, w in enumerate(cur) if w["s"] >= cp - 0.06), None)
                if k:
                    cues.append(cur[:k])
                    cur = cur[k:]
        cues.append(cur)
    shots = []
    for cue in cues:
        # shot boundaries live on the frame grid so the video timeline equals
        # the audio timeline exactly (sum of nf/FPS == t1)
        t0 = round(max(0.0, cue[0]["s"] - 0.10) * FPS) / FPS
        t1 = round(min(total, cue[-1]["e"] + 0.12) * FPS) / FPS
        if t1 - t0 < 0.30:
            continue
        dev = next((x for x in beats if x["t0"] - 0.30 < t0 < x["t1"]), None)
        shots.append(dict(t0=round(t0, 3), t1=round(t1, 3),
                          text=" ".join(x["w"] for x in cue),
                          cue=[dict(w=x["w"], s=x["s"], e=x["e"]) for x in cue],
                          src=source_at(smap, t0),
                          dev=dev.get("dev") if dev else None,
                          dev_id=beats.index(dev) if dev else None,
                          backdrop=(dev or {}).get("backdrop"),
                          split=(dev or {}).get("split", False),
                          backdrops=(dev or {}).get("backdrops"),
                          photo=(dev or {}).get("photo"),
                          prop=(dev or {}).get("prop"),
                          vfx=(dev or {}).get("vfx"),
                          treat=(dev or {}).get("treat"),
                          frame=(dev or {}).get("frame", False),
                          motion=(dev or {}).get("motion"),
                          cap_y=(dev or {}).get("cap_y"),
                          nocap=(dev or {}).get("nocap", False)))
    # continuous audio: each shot runs to the next one's start
    for i in range(len(shots) - 1):
        shots[i]["t1"] = shots[i + 1]["t0"]
    shots[-1]["t1"] = round(total * FPS) / FPS

    seg_times = []
    for ph in spec.get("segments", []):
        hit = find_phrase(words, ph, 0.0)
        if hit:
            seg_times.append(hit[0])
        else:
            print(f"  ! segment anchor missed: '{ph}'")
    prev = -1
    for i, s in enumerate(shots):
        z = (prev + 1 + (i % 2)) % len(ZOOMS)
        s["zoom"] = z
        prev = z
        s["segment_start"] = any(s["t0"] - 0.15 <= t < s["t1"] - 0.15 for t in seg_times)
        if s["motion"]:
            pass
        elif s["segment_start"]:
            s["motion"] = "whip"
        elif re.search(r"[\d$%]", s["text"]):
            s["motion"] = "punch"
        else:
            s["motion"] = FX.HOUSE["move_rotation"][i % len(FX.HOUSE["move_rotation"])]
    return shots, beats


ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
       "-r", str(FPS), "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
       "-video_track_timescale", "90000"]


def render_shots(shots, tight, work, endcard=None):
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
        src_in = ["-ss", f"{s['t0'] - 0.5 / FPS:.6f}", "-to", f"{s['t1'] + 0.5 / FPS:.6f}", "-i", str(tight)]
        cap = s.get("cap") if s.get("cap_burn", True) else None
        cap_sig = hashlib.md5(Path(cap).read_bytes()).hexdigest() if cap else None
        key = json.dumps({k: v for k, v in s.items()
                          if k not in ("out0", "out1", "dev_id", "text", "cue", "segment_start", "cap", "cap_burn")}
                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig,
                            "src_file": Path(tight).name, "v": 4}, sort_keys=True)
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
    lst.write_text("".join(f"file '{q.resolve().as_posix()}'\n" for q in parts), encoding="utf-8")
    cut = work / "_cut.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(cut)])
    nv = int(ffprobe(cut, "stream=nb_frames")["streams"][0]["nb_frames"])
    if nv != int(round(tl * FPS)):
        raise RuntimeError(f"cut has {nv} frames, timeline says {int(round(tl * FPS))}")
    return cut, tl


# ============================================================== captions

def score_accent(cue):
    STOP = {"a", "an", "the", "and", "or", "but", "to", "of", "for", "in", "on",
            "at", "is", "are", "was", "your", "my", "i", "we", "you", "it",
            "that", "this", "so", "if", "as", "with", "have", "has", "be", "been",
            "im", "ill", "will"}
    best, bi = -1, 0
    for i, w in enumerate(cue):
        t = w["w"]
        s = 10 if re.search(r"[\d$%]", t) else 0
        if norm(t) in STOP:
            s -= 6
        s += min(len(re.sub(r"\W", "", t)), 9) * 0.5
        if s > best:
            best, bi = s, i
    return bi


# ============================================================== compose

def burn_caps_into_device(devdir, t0, t1, shots):
    """Captions are burned into the SHOT, so an opaque plate (dread, icon
    compare, pin map, black type) would hide them. Paste each shot's caption
    plate onto the device frames it overlaps - the band then rides on top of
    every plate, and nothing single-image is ever overlaid on the timeline."""
    from PIL import Image
    frames = sorted(devdir.glob("*.png"))
    if not frames:
        return 0
    n = 0
    caps = [(sh["out0"], sh["out1"], sh["cap"]) for sh in shots
            if sh.get("cap") and sh["out1"] > t0 and sh["out0"] < t1]
    cache = {}
    for i, fpath in enumerate(frames):
        t = t0 + i / FPS
        hit = next((c for a, b, c in caps if a - 0.001 <= t < b), None)
        if not hit:
            continue
        if hit not in cache:
            cache[hit] = Image.open(hit).convert("RGBA")
        im = Image.open(fpath).convert("RGBA")
        im.alpha_composite(cache[hit])
        im.save(fpath)
        n += 1
    return n


def compose(spec, tight, tight_a, words, smap, out_name):
    work = WORK / ("build_" + Path(out_name).stem[-3:])   # one build dir per speed
    work.mkdir(parents=True, exist_ok=True)
    total = dur_of(tight)
    shots, beats = build_shots(spec, words, smap, total)
    print(f"  {len(shots)} shots, {len(beats)} beats")

    # caption plates are burned into their own shots (see render_shots)
    capdir = work / "caps"
    if capdir.exists():
        shutil.rmtree(capdir)
    capdir.mkdir(parents=True, exist_ok=True)
    n_caps = 0
    for k, sh in enumerate(shots):
        if sh.get("nocap"):
            continue
        cue = [w["w"] for w in sh["cue"]]
        png = capdir / f"c{k:03d}.png"
        # one caption band for the whole ad: low (0.80), on the speaker panel
        # of a split (0.86), or wherever a beat says its plate leaves room
        y = sh.get("cap_y") or (0.86 if (sh.get("split") or sh.get("backdrops")) else CAP_Y)
        DV.caption_plate(png, cue, accent=score_accent(sh["cue"]),
                         emoji=DV.pick_emoji(" ".join(cue)), y_frac=y, size=CAP_SIZE)
        sh["cap"] = str(png)
        sh["cap_burn"] = not sh.get("dev")      # device shots: paste on the plate frames instead
        n_caps += 1
    print(f"  {n_caps} caption plates")

    endcard = dict(spec["endcard"]) if spec.get("endcard") else None
    cut, total_out = render_shots(shots, tight, work, endcard)
    (work / "shots.json").write_text(json.dumps(shots, indent=1), encoding="utf-8")
    lens = sorted(s["out1"] - s["out0"] for s in shots)
    print(f"  cut {total_out:.1f}s  median shot {lens[len(lens)//2]:.2f}s  "
          f"{len(shots)/(total_out/60):.0f} cuts/min")

    flashes, segs = [], []
    for k, sh in enumerate(shots):
        if sh.get("segment_start") and sh["out0"] > 0.2:
            flashes.append(sh["out0"])
            segs.append(sh["out0"])

    devdir = work / "dev"
    if devdir.exists():
        shutil.rmtree(devdir)
    dev_overlays = []
    for bi, b in enumerate(beats):
        owners = [s for s in shots if s["dev_id"] == bi]
        if not owners:
            print(f"  ! beat {bi} '{b['at']}': no shot claimed it")
            continue
        t0 = owners[0]["out0"]
        t1 = owners[-1]["out1"]
        what = b.get("dev") or b.get("backdrop") or b.get("photo") or b.get("treat") or "shot"
        if not b.get("dev"):
            print(f"  insert  {what:26} {t0:6.2f} -> {t1:6.2f}")
            continue
        d = devdir / f"{bi:02d}_{b['dev']}"
        DEVICES[b["dev"]](d, max(0.8, t1 - t0), **b.get("params", {}))
        nb = burn_caps_into_device(d, t0, t1, shots)
        dev_overlays.append((d, t0, t1))
        print(f"  device  {what:26} {t0:6.2f} -> {t1:6.2f}  (+{nb} caption frames)")
    if endcard:
        d = devdir / "99_endcard"
        DEVICES[endcard["dev"]](d, endcard["secs"] + 0.2, **endcard.get("params", {}))
        dev_overlays.append((d, endcard["out0"], endcard["out1"] + 0.5))
        print(f"  endcard {endcard['dev']:26} {endcard['out0']:6.2f} -> {endcard['out1']:6.2f}")

    filt = ["[0:v]null[base]"]
    inputs = ["-i", str(cut)]
    last, idx = "base", 1
    for d, t0, t1 in dev_overlays:
        inputs += ["-framerate", str(FPS), "-i", str(d / "%04d.png")]
        filt.append(f"[{idx}:v]setpts=PTS-STARTPTS+{t0:.3f}/TB,format=rgba[d{idx}]")
        filt.append(f"[{last}][d{idx}]overlay=0:0:enable='between(t,{t0:.3f},{t1:.3f})'[v{idx}]")
        last = f"v{idx}"
        idx += 1
    for bi, b in enumerate(beats):
        if not b.get("prop"):
            continue
        owners = [x for x in shots if x["dev_id"] == bi]
        if not owners:
            continue
        t0, t1 = owners[0]["out0"], owners[-1]["out1"]
        inputs += ["-framerate", str(FPS), "-i", str(PROPS / b["prop"])]
        n = int((t1 - t0) * FPS) + 4
        sc = b.get("prop_scale", 0.8)
        filt.append(f"[{idx}:v]loop=loop={n}:size=1,fps={FPS},setpts=PTS-STARTPTS+{t0:.3f}/TB,"
                    f"format=rgba,scale=iw*{sc}:ih*{sc}[pp{idx}]")
        filt.append(f"[{last}][pp{idx}]overlay=(W-w)/2:(H-h)/2:enable='between(t,{t0:.3f},{t1:.3f})'[v{idx}]")
        last = f"v{idx}"; idx += 1
        print(f"  prop    {b['prop']:26} {t0:6.2f} -> {t1:6.2f}")
    used_vfx = set()
    for bi, b in enumerate(beats):
        if not b.get("vfx"):
            continue
        owners = [x for x in shots if x["dev_id"] == bi]
        if not owners:
            continue
        t0 = owners[0]["out0"]
        t1 = min(owners[-1]["out1"], t0 + b.get("vfx_secs", 1.2))
        kind_files = [VFX / m["file"] for m in VFX_MANIFEST if m.get("kind") == b["vfx"]]
        pool = [f for f in kind_files if f.name not in used_vfx] or kind_files
        if not pool:
            print(f"  ! no vfx for '{b['vfx']}'"); continue
        clip = pool[0]; used_vfx.add(clip.name)
        inputs += ["-stream_loop", "-1", "-t", f"{total_out + 0.5:.3f}", "-i", str(clip)]
        filt.extend(FX.vfx_overlay(idx, t0, t1, src=last, dst=f"v{idx}", opacity=b.get("vfx_gain", 1.0)))
        last = f"v{idx}"; idx += 1
        print(f"  vfx     {clip.name:26} {t0:6.2f} -> {t1:6.2f}")
    for t in flashes:
        filt.append(f"[{last}]{FX.flash(t)}[f{idx}]")
        last = f"f{idx}"; idx += 1
    filt.append(f"[{last}]null[vout]")

    part = work / "_body.mp4"
    (work / "filter.txt").write_text((";" + chr(10)).join(filt), encoding="utf-8")
    inputs = [rel(x, work) if isinstance(x, str) and (x.endswith((".png", ".mp4")) and Path(x).is_absolute()) else x
              for x in inputs]
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex_script", "filter.txt", "-map", "[vout]", "-an",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-bf", "0", "-pix_fmt", "yuv420p",
         "-r", str(FPS), "-video_track_timescale", "90000", "_body.mp4"],
        cwd=work)

    # ---- final: continuous speech track + whooshes + bed, loudness, progress bar ----
    out_d = dur_of(part)
    music = spec.get("music", FX.HOUSE["music"])
    music_p = Path(music) if Path(music).is_absolute() else AUDIO / music
    inputs = ["-i", str(part), "-i", str(tight_a), "-stream_loop", "-1", "-i", str(music_p)]
    for _ in segs:
        inputs += ["-i", str(AUDIO / FX.HOUSE["whoosh"])]
    f = ["[1:a]apad[sp0]"]           # speech: one PCM track, padded through the endcard
    mixin = "[sp0]"
    for i, t in enumerate(segs):
        ms = max(0, int((t - WHOOSH_PEAK) * 1000))
        f.append(f"[{3+i}:a]adelay={ms}|{ms},volume=0.45[wh{i}]")
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
    print(f"  OK {final.name}  {dur_of(final):.1f}s, {final.stat().st_size/1e6:.1f} MB")
    return final


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tighten-only", action="store_true")
    ap.add_argument("--speed", type=float, default=1.15)
    a = ap.parse_args()
    sys.path.insert(0, str(HERE))
    from spec_webinar import SPEC, PIECES, OUT_NAME
    WORK.mkdir(parents=True, exist_ok=True)
    print("== TIGHTEN ==")
    tight_v, tight_a, words, smap = tighten(PIECES, a.speed)
    if a.tighten_only:
        return
    print("== COMPOSE ==")
    name = OUT_NAME.replace(".mp4", f"_{int(round(a.speed * 100))}.mp4")
    compose(SPEC, tight_v, tight_a, words, smap, name)


if __name__ == "__main__":
    main()
