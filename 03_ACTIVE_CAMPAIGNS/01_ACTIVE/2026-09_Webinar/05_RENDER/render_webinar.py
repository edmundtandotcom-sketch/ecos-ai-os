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
WORK = HERE / "work"
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
SPEED = FX.HOUSE["speed"]
LOUDNORM_I = -16
MUSIC_VOL = 0.09
PROGRESS_BAR = 12
GRADE = FX.GRADE

# face centre / eye line in the SOURCE frame (haar on a reference frame)
FACE = {"hooks": (524, 734), "body": (468, 783)}
ZOOMS = [1.00, 1.10, 1.22]
CAP_MAX_WORDS = 3

# pause carving
MAX_GAP, PAD_OUT, PAD_IN = 0.38, 0.22, 0.12

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


def tighten(pieces):
    """pieces: [(label, t_lo, t_hi), ...] in edit order.

    Every speech run is encoded on its own (no drift), then stream-copied.
    Word timings are remapped onto the measured durations. Returns the tight
    file, the words on its timeline, and a source map (which take each
    stretch came from - the face position differs per take).
    """
    plan = []
    for label, lo, hi in pieces:
        words = json.loads((WORK / f"words_{label}.json").read_text(encoding="utf-8"))
        for a, b in plan_segments(words, lo, hi):
            plan.append((label, a, b))
    stamp = WORK / "_tight.json"
    dest = WORK / "_tight.mp4"
    segdir = WORK / "_tight"
    segdir.mkdir(parents=True, exist_ok=True)
    if dest.exists() and stamp.exists() and json.loads(stamp.read_text()) == [list(p) for p in plan]:
        durs = [dur_of(q) for q in sorted(segdir.glob("seg*.mp4"))]
        print(f"  tight cut cached ({len(plan)} segments)")
    else:
        for old in segdir.glob("seg*.mp4"):
            old.unlink()
        parts, durs = [], []
        for i, (label, a, b) in enumerate(plan):
            q = segdir / f"seg{i:03d}.mp4"
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(SOURCES[label]),
                 "-vf", f"scale={W}:{H},setsar=1",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
                 "-pix_fmt", "yuv420p", "-r", str(FPS),
                 "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                 "-video_track_timescale", "90000", str(q)])
            parts.append(q)
            durs.append(dur_of(q))
        lst = segdir / "concat.txt"
        lst.write_text("".join(f"file '{q.resolve().as_posix()}'\n" for q in parts), encoding="utf-8")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", str(lst), "-c", "copy", str(dest)])
        stamp.write_text(json.dumps([list(p) for p in plan]), encoding="utf-8")
    out, base, smap = [], 0.0, []
    for (label, a, b), d in zip(plan, durs):
        words = json.loads((WORK / f"words_{label}.json").read_text(encoding="utf-8"))
        for w in words:
            if a - 0.001 <= w["s"] < b:
                out.append(dict(w=w["w"], s=round(base + max(0.0, w["s"] - a), 3),
                                e=round(base + min(d, max(0.0, w["e"] - a)), 3)))
        smap.append(dict(label=label, src0=a, src1=b, out0=round(base, 3), out1=round(base + d, 3)))
        base += d
    raw = sum(hi - lo for _, lo, hi in pieces)
    print(f"  tight: {raw:.1f}s -> {base:.1f}s ({(1 - base / raw) * 100:.0f}% dead air removed)")
    out = fix_tokens(out)
    (WORK / "words_tight.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    (WORK / "words_tight.txt").write_text(
        "\n".join(f"{w['s']:7.2f} {w['w']}" for w in out), encoding="utf-8")
    return dest, out, smap


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
        t0 = max(0.0, cue[0]["s"] - 0.10)
        t1 = min(total, cue[-1]["e"] + 0.12)
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
                          nocap=(dev or {}).get("nocap", False)))
    # continuous audio: each shot runs to the next one's start
    for i in range(len(shots) - 1):
        shots[i]["t1"] = shots[i + 1]["t0"]
    shots[-1]["t1"] = total

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

def compose(spec, tight, words, smap, out_name):
    work = WORK / "build"
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
        if sh.get("nocap") or (sh["dev"] and sh["dev"] not in ("icon_row", "lower_ticker", "split_labels")):
            continue
        cue = [w["w"] for w in sh["cue"]]
        png = capdir / f"c{k:03d}.png"
        y = 0.86 if (sh.get("split") or sh.get("backdrops")) else 0.655
        DV.caption_plate(png, cue, accent=score_accent(sh["cue"]),
                         emoji=DV.pick_emoji(" ".join(cue)), y_frac=y)
        sh["cap"] = str(png)
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
        t0, t1 = owners[0]["out0"], owners[-1]["out1"]
        what = b.get("dev") or b.get("backdrop") or b.get("photo") or b.get("treat") or "shot"
        if not b.get("dev"):
            print(f"  insert  {what:26} {t0:6.2f} -> {t1:6.2f}")
            continue
        d = devdir / f"{bi:02d}_{b['dev']}"
        DEVICES[b["dev"]](d, max(0.8, t1 - t0), **b.get("params", {}))
        dev_overlays.append((d, t0, t1))
        print(f"  device  {what:26} {t0:6.2f} -> {t1:6.2f}")
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
         "-filter_complex_script", "filter.txt", "-map", "[vout]", "-map", "0:a", *ENC, "_body.mp4"],
        cwd=work)

    # ---- final: speed, whooshes, bed, loudness, progress bar ----
    out_d = dur_of(part) / SPEED
    inputs = ["-i", str(part), "-stream_loop", "-1", "-i", str(AUDIO / FX.HOUSE["music"])]
    for _ in segs:
        inputs += ["-i", str(AUDIO / FX.HOUSE["whoosh"])]
    f = []
    mixin = "[0:a]"
    for i, t in enumerate(segs):
        f.append(f"[{2+i}:a]adelay={int(t*1000)}|{int(t*1000)},volume=0.45[wh{i}]")
        mixin += f"[wh{i}]"
    if segs:
        f.append(f"{mixin}amix=inputs={len(segs)+1}:duration=first:dropout_transition=0,"
                 f"volume={len(segs)+1}[mx]")
    else:
        f.append("[0:a]anull[mx]")
    f.append(f"[mx]atempo={SPEED}[sp]")
    f.append(f"[1:a]volume={MUSIC_VOL},afade=t=out:st={out_d-2.0:.2f}:d=2.0[bed]")
    f.append(f"[sp][bed]amix=inputs=2:duration=first:dropout_transition=0,"
             f"loudnorm=I={LOUDNORM_I}:TP=-1.5:LRA=11[a]")
    f.append(f"[0:v]setpts=PTS/{SPEED}[vs]")
    f.extend(FX.progress_bar(out_d, src="vs", dst="vout", thickness=PROGRESS_BAR))
    OUT.mkdir(parents=True, exist_ok=True)
    final = OUT / out_name
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[a]", "-t", f"{out_d:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", str(final)])
    print(f"  OK {final.name}  {dur_of(final):.1f}s, {final.stat().st_size/1e6:.1f} MB")
    return final


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tighten-only", action="store_true")
    a = ap.parse_args()
    sys.path.insert(0, str(HERE))
    from spec_webinar import SPEC, PIECES, OUT_NAME
    WORK.mkdir(parents=True, exist_ok=True)
    print("== TIGHTEN ==")
    tight, words, smap = tighten(PIECES)
    if a.tighten_only:
        return
    print("== COMPOSE ==")
    compose(SPEC, tight, words, smap, OUT_NAME)


if __name__ == "__main__":
    main()
