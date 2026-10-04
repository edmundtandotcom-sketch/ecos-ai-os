#!/usr/bin/env python3
"""
S&P Benchmark ad - rebuilt to ADS_PLAYBOOK v1.0 (E:\\REMOTION\\ADS_PLAYBOOK.md).

v1 (render_ad.py) was built from the DRAFT Edit Direction Brief and missed the
measured norms of the reference set on every axis. This build targets them:

  pace      10-14 cuts/min, ~3.4s shots   (v1 had ZERO cuts in 209s)
  captions  centred at 55% of frame       (v1 anchored them at 85.5%)
  layout    full-bleed, no chrome         (v1 used bottom-third chip cards)
  evidence  full-bleed plates as cutaways (v1 overlaid navy lower-thirds)
  CTA       red frame + boxed line        (v1 used a blue chip)

Grammar B from the playbook: full-bleed speaker, full-bleed plates for
evidence. Head size stays ~51% - outside the reference band and NOT fixable
here; it needs a wider reshoot (playbook S7). Accepted deliberately for this
test build.

Reuses what the v1 run already produced - the tightened cut and the word
timings remapped onto it - so nothing is re-derived.

    python render_ad_v2.py --stage all
"""

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"
GFX = OUT / "graphics"
V2 = OUT / "v2"
OUT_NAME = "SP_BENCHMARK_9x16_v2.mp4"

W, H, FPS = 1080, 1920, 30
LOUDNORM_I = -16

# ---------------------------------------------------------------- framing
# Source 1280x720, speaker's face centre x=663, eyes at y=238 (measured).
# A 9:16 window can only ever magnify, so z=1.00 is the WIDEST available and
# most shots sit there; the punches are for emphasis and shot variation.
FACE_CX, EYE_Y = 663, 238
ZOOMS = [1.00, 1.07, 1.14]
# Which framing each successive shot uses. Cycled; never two the same in a row.
ZOOM_PATTERN = [0, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0, 1]

# Split any shot longer than this, and aim for roughly this per shot.
SHOT_MAX = 6.0
SHOT_TARGET = 4.0

# ---------------------------------------------------------------- captions
# Reference median is 55% of frame. That works because a correctly framed
# medium shot has the chin well above it. Our head is oversized (see module
# docstring), so 55% lands on his mouth - and "nothing covers the face"
# outranks the number. 0.67 keeps the intent (captions ride just under the
# speaker) while clearing the deepest measured chin at y=1192.
CAP_Y_FRAC = 0.67
CAP_SIZE = 84
CAP_FONT = "Impact"      # stand-in; playbook face is Anton / Archivo Black
CAP_MAX_WORDS = 4
ACCENT = "&H0035FFDF&"   # volt-lime-ish in ASS BGR, for the one scored word

# ------------------------------------------------- evidence plates (cutaways)
# Anchored to spoken phrases, matched against the tightened transcript.
PLATES = [
    dict(id="chart", asset="g1_chart.png", at="so the benchmark", lead=-0.3, hold=7.0),
    dict(id="qcard", asset="g3_question.png", at="can this project beat", lead=-0.3, hold=2.8),
    dict(id="dataA", asset="_plate_dataA.png", at="bought at", lead=-0.2, hold=9.0),
    dict(id="dataB", asset="_plate_dataB.png", at="another property", lead=-0.2, hold=9.0),
    dict(id="frame", asset="g4_framework.png", at="new launch ladder", lead=-0.3, hold=8.0),
]

ENDCARD = "g10_endcard.png"
ENDCARD_SECONDS = 2.6
CTA_BORDER = 14          # red CTA frame thickness


def run(cmd):
    sys.stdout.flush()
    return subprocess.run(cmd, check=True)


def ffprobe(path, entries="format=duration"):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries, "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def dur_of(path):
    return float(ffprobe(path)["format"]["duration"])


def load(name):
    return json.loads((OUT / f"words_{name}_tight.json").read_text(encoding="utf-8"))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def find_phrase(words, phrase, after=0):
    flat, owner = [], []
    for i, w in enumerate(words):
        t = norm(w["w"])
        flat.append(t)
        owner.extend([i] * len(t))
    flat = "".join(flat)
    lo = 0
    while lo < len(owner) and owner[lo] < after:
        lo += 1
    pos = flat.find(norm(phrase), lo)
    if pos < 0:
        return None
    i = owner[pos]
    return words[i]["s"], i


# ----------------------------------------------------------------------------
# Stage: plates - full-bleed versions of the two proof cards
# ----------------------------------------------------------------------------

PROOF = [
    dict(dst="_plate_dataA.png", pct="22.9%", unit="/YR",
         lines=["BOUGHT $1.15M", "SOLD $1.525M AFTER 3 YEARS",
                "$321K COMMITTED  \u00b7  NET ~$282K"]),
    dict(dst="_plate_dataB.png", pct="12.9%", unit="/YR",
         lines=["BOUGHT $1.05M", "SOLD $1.28M AFTER 4 YEARS",
                "$292K COMMITTED"]),
]


def _font(size, bold=True):
    from PIL import ImageFont
    for n in ("impact.ttf" if bold else "arialbd.ttf", "arialbd.ttf"):
        f = Path(r"C:\Windows\Fonts") / n
        if f.exists():
            return ImageFont.truetype(str(f), size)
    return ImageFont.load_default()


def stage_plates():
    """Draw the proof plates full-bleed.

    The v1 cards were 1080x340 lower-thirds. Dropping one onto a 1920-tall
    plate leaves a small chip marooned in navy - the number has to be sized
    for the whole frame, not pasted into it.
    """
    print("\n== PLATES ==")
    from PIL import Image, ImageDraw
    NAVY, YELLOW, WHITE = (11, 16, 32), (255, 232, 0), (255, 255, 255)
    MUTED = (176, 186, 214)
    for spec in PROOF:
        im = Image.new("RGB", (W, H), NAVY)
        d = ImageDraw.Draw(im)
        fbig, funit = _font(300), _font(96)
        fline, fsub = _font(62), _font(52)
        x0, y = 92, int(H * 0.34)
        d.text((x0, y), spec["pct"], font=fbig, fill=YELLOW)
        wpct = d.textlength(spec["pct"], font=fbig)
        d.text((x0 + wpct + 20, y + 178), spec["unit"], font=funit, fill=YELLOW)
        y += 330
        d.line([(x0, y), (W - x0, y)], fill=YELLOW, width=4)
        y += 46
        for i, ln in enumerate(spec["lines"]):
            f = fline if i < 2 else fsub
            d.text((x0, y), ln, font=f, fill=WHITE if i < 2 else MUTED)
            y += (86 if i < 2 else 74)
        im.save(GFX / spec["dst"])
        print(f"  {spec['dst']}  {spec['pct']} full-bleed")


# ----------------------------------------------------------------------------
# Stage: shots - re-cut the tightened segments into framed shots
# ----------------------------------------------------------------------------

def plan_shots():
    """Split the tightened speech segments into shots and assign framings."""
    segs = sorted((OUT / "_tight_body").glob("seg*.mp4"))
    words = load("body")
    shots, base = [], 0.0
    for q in segs:
        d = dur_of(q)
        # Split a long segment at its widest internal word gap so the cut
        # lands in a breath, not mid-word.
        n = max(1, min(4, round(d / SHOT_TARGET))) if d > SHOT_MAX else 1
        if n == 1:
            pieces = [(0.0, d)]
        else:
            inner = [w for w in words if base < w["s"] < base + d]
            gaps = sorted(
                ((inner[i + 1]["s"] - inner[i]["e"], (inner[i]["e"] + inner[i + 1]["s"]) / 2 - base)
                 for i in range(len(inner) - 1)), reverse=True)
            cutpts = sorted(g[1] for g in gaps[:n - 1]) if gaps else []
            cutpts = [c for c in cutpts if 0.6 < c < d - 0.6]
            bounds = [0.0] + cutpts + [d]
            pieces = list(zip(bounds, bounds[1:]))
        for a, b in pieces:
            if b - a < 0.35:
                continue
            shots.append(dict(src=str(q), a=round(a, 3), b=round(b, 3),
                              t0=round(base + a, 3), len=round(b - a, 3)))
        base += d
    # framings, never repeating back to back
    prev = None
    for i, s in enumerate(shots):
        z = ZOOM_PATTERN[i % len(ZOOM_PATTERN)]
        if z == prev:
            z = (z + 1) % len(ZOOMS)
        s["zoom"] = z
        prev = z
    return shots, base


def crop_for(z):
    zoom = ZOOMS[z]
    w = int(round(W / H * 720 / zoom)) & ~1
    h = int(round(720 / zoom)) & ~1
    x = max(0, min(1280 - w, int(round(FACE_CX - w / 2))))
    y = max(0, min(720 - h, int(round(EYE_Y - 0.30 * h))))
    return w, h, x, y


def stage_shots():
    print("\n== SHOTS ==")
    shots, total = plan_shots()
    lens = sorted(s["len"] for s in shots)
    med = lens[len(lens) // 2]
    print(f"  {len(shots)} shots over {total:.1f}s")
    print(f"  median shot {med:.2f}s  (playbook target ~3.4s)")
    print(f"  cuts/min {len(shots) / (total / 60):.1f}  (playbook target 10-14)")

    work = V2 / "shots"
    work.mkdir(parents=True, exist_ok=True)
    for f in work.glob("*.mp4"):
        f.unlink()
    parts = []
    for i, s in enumerate(shots):
        w, h, x, y = crop_for(s["zoom"])
        p = work / f"s{i:03d}.mp4"
        run(["ffmpeg", "-y", "-loglevel", "error",
             "-ss", f"{s['a']:.3f}", "-to", f"{s['b']:.3f}", "-i", s["src"],
             "-vf", f"crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,setsar=1,"
                    f"eq=contrast=1.06:brightness=0.012:saturation=1.07,"
                    f"unsharp=5:5:0.35:5:5:0.0,fps={FPS}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20",
             "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
             "-video_track_timescale", "90000", str(p)])
        parts.append(p)
    lst = V2 / "shots.txt"
    lst.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in parts),
                   encoding="utf-8")
    dest = V2 / "_body_shots.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(dest)])
    (V2 / "shots.json").write_text(json.dumps(shots, indent=1), encoding="utf-8")
    print(f"  -> {dest.name}  {dur_of(dest):.1f}s")


# ----------------------------------------------------------------------------
# Captions - playbook S5
# ----------------------------------------------------------------------------

def score_accent(cue):
    """The one word that earns the accent colour: numbers first, then length."""
    STOP = {"a", "an", "the", "and", "or", "but", "to", "of", "for", "in",
            "on", "at", "is", "are", "was", "were", "be", "been", "your", "my",
            "i", "we", "you", "it", "that", "this", "so", "if", "as", "with",
            "have", "has", "had", "just", "then", "than", "them", "they"}
    best, bi = -1, 0
    for i, w in enumerate(cue):
        t = w["w"]
        s = 0
        if re.search(r"[\d$%]", t):
            s += 10
        if norm(t) in STOP:
            s -= 6
        s += min(len(re.sub(r"\W", "", t)), 9) * 0.5
        if s > best:
            best, bi = s, i
    return bi


def build_ass(words, path, blackout=()):
    """ALL CAPS phrase cues, centred at 55%, one accent word per cue."""
    def ts(t):
        h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
        return f"{h:d}:{m:02d}:{s:05.2f}"

    # Phrase cues, playbook S5. Breaking purely on word count strands function
    # words at a cue edge and produces reads like "AT AND I'LL SHOW"; break on
    # punctuation and real pauses first, then never end on a function word.
    TRAIL = {"a", "an", "the", "and", "or", "but", "to", "of", "for", "in",
             "on", "at", "is", "are", "was", "were", "be", "your", "my", "i",
             "we", "you", "it", "that", "this", "so", "if", "as", "with"}
    cues, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        gap = (nxt["s"] - w["e"]) if nxt else 99
        joined = " ".join(x["w"] for x in cur)
        hard = w["w"].endswith((".", "?", "!"))
        soft = w["w"].endswith(",") and len(cur) >= 2
        full = len(cur) >= CAP_MAX_WORDS or len(joined) >= 22
        over = len(cur) > CAP_MAX_WORDS or len(joined) >= 26
        if hard or soft or gap > 0.28 or full:
            if not hard and nxt is not None and len(cur) < 2:
                continue          # a lone word is not a phrase cue
            if (not hard and nxt is not None and not over
                    and norm(w["w"]) in TRAIL):
                continue          # don't strand a function word at the edge
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)

    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Ad,{CAP_FONT},{CAP_SIZE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,7,3,5,95,95,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for cue in cues:
        t0, t1 = cue[0]["s"], cue[-1]["e"]
        # A plate owns the frame; captions would fight its own headline.
        if any(b0 - 0.15 < t0 < b1 for b0, b1 in blackout):
            continue
        t1 = min(t1, min((b0 for b0, b1 in blackout if b0 > t0), default=t1))
        if t1 - t0 < 0.12:
            continue
        ai = score_accent(cue)
        txt = ""
        for i, w in enumerate(cue):
            word = re.sub(r"[,]$", "", w["w"]).upper()
            txt += (f"{{\\c{ACCENT}}}{word}{{\\c&H00FFFFFF&}} " if i == ai
                    else f"{word} ")
        pos = "{\\an5\\pos(%d,%d)}" % (W // 2, int(H * CAP_Y_FRAC))
        lines.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},Ad,,0,0,0,,{pos}{txt.strip()}")
    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


def ass_path(p):
    return str(p).replace("\\", "/").replace(":", "\\:")


def plate_stream(t0, t1):
    hold = max(0.2, t1 - t0)
    n = int(math.ceil(hold * FPS)) + 4
    return (f"loop=loop={n}:size=1,fps={FPS},setpts=PTS-STARTPTS+{t0:.3f}/TB,"
            f"fade=t=in:st={t0:.2f}:d=0.18:alpha=1,"
            f"fade=t=out:st={t1 - 0.18:.2f}:d=0.18:alpha=1")


# ----------------------------------------------------------------------------
# Stage: build
# ----------------------------------------------------------------------------

def stage_build():
    print("\n== BUILD ==")
    body = V2 / "_body_shots.mp4"
    if not body.exists():
        sys.exit("ERROR: run --stage shots first")
    words = load("body")

    # resolve plates against the tightened transcript
    plates, cursor = [], 0
    for p in PLATES:
        hit = find_phrase(words, p["at"], cursor)
        if not hit:
            print(f"  ! MISSED plate anchor '{p['at']}' - skipped")
            continue
        cursor = hit[1]
        t0 = max(0.0, hit[0] + p["lead"])
        plates.append({**p, "t0": round(t0, 2), "t1": round(t0 + p["hold"], 2)})
        print(f"  plate {p['id']:6} {t0:7.2f} -> {t0 + p['hold']:7.2f}")
    black = [(p["t0"], p["t1"]) for p in plates]

    n = build_ass(words, V2 / "caps_body.ass", blackout=black)
    print(f"  captions: {n} cues at {CAP_Y_FRAC*100:.0f}% of frame")

    filt, inputs, idx, last = [], ["-i", str(body)], 1, "0:v"
    for p in plates:
        asset = GFX / p["asset"]
        if not asset.exists():
            print(f"  ! missing {asset.name}")
            continue
        inputs += ["-framerate", str(FPS), "-i", str(asset)]
        filt.append(f"[{idx}:v]scale={W}:{H},{plate_stream(p['t0'], p['t1'])}[p{idx}]")
        filt.append(f"[{last}][p{idx}]overlay=0:0:"
                    f"enable='between(t,{p['t0']},{p['t1']})'[v{idx}]")
        last = f"v{idx}"
        idx += 1
    filt.append(f"[{last}]ass='{ass_path(V2 / 'caps_body.ass')}'[vout]")

    part_body = V2 / "_part_body.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex", ";".join(filt),
         "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_body)])
    print(f"  body -> {part_body.name}  {dur_of(part_body):.1f}s")

    # ---- CTA: full-bleed speaker + red frame, playbook S8 ----
    cta_src = OUT / "_tight_cta.mp4"
    cw, ch, cx, cy = crop_for(0)
    ncap = build_ass(load("cta"), V2 / "caps_cta.ass")
    cta_filt = (
        f"[0:v]crop={cw}:{ch}:{cx}:{cy},scale={W}:{H}:flags=lanczos,setsar=1,"
        f"eq=contrast=1.06:brightness=0.012:saturation=1.07,fps={FPS},"
        f"drawbox=x=0:y=0:w={W}:h={H}:color=red@1.0:t={CTA_BORDER},"
        f"ass='{ass_path(V2 / 'caps_cta.ass')}'[vout]"
    )
    part_cta = V2 / "_part_cta.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", "-i", str(cta_src),
         "-filter_complex", cta_filt, "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_cta)])
    print(f"  cta  -> {part_cta.name}  {dur_of(part_cta):.1f}s  ({ncap} cues, red frame)")

    # ---- end card ----
    part_end = V2 / "_part_end.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(GFX / ENDCARD),
         "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
         "-filter_complex",
         f"[0:v]fps={FPS},tpad=stop_mode=clone:stop_duration={ENDCARD_SECONDS},"
         f"trim=duration={ENDCARD_SECONDS},setpts=PTS-STARTPTS,"
         f"fade=t=in:st=0:d=0.3,format=yuv420p[v];"
         f"[1:a]atrim=duration={ENDCARD_SECONDS},asetpts=PTS-STARTPTS[a]",
         "-map", "[v]", "-map", "[a]",
         "-frames:v", str(int(ENDCARD_SECONDS * FPS)), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_end)])

    lst = V2 / "join.txt"
    lst.write_text("".join(f"file '{p.resolve().as_posix()}'\n"
                           for p in (part_body, part_cta, part_end)), encoding="utf-8")
    joined = V2 / "_joined.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(joined)])

    final = OUT / OUT_NAME
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", "-i", str(joined),
         "-af", f"loudnorm=I={LOUDNORM_I}:TP=-1.5:LRA=11",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(final)])
    joined.unlink(missing_ok=True)
    print(f"\n  OK {final}  {dur_of(final):.1f}s, {final.stat().st_size/1e6:.1f} MB")
    (V2 / "plates_resolved.json").write_text(json.dumps(plates, indent=1), encoding="utf-8")


# ----------------------------------------------------------------------------
# Stage: qc
# ----------------------------------------------------------------------------

def stage_qc():
    print("\n== QC ==")
    final = OUT / OUT_NAME
    d = dur_of(final)
    qc = V2 / "qc"
    qc.mkdir(parents=True, exist_ok=True)
    cols, every = 6, 5.0
    rows = max(1, math.ceil(d / every / cols))
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(final),
         "-vf", f"fps=1/{every},scale=320:-2,tile={cols}x{rows}",
         "-frames:v", "1", str(qc / "contact_sheet.jpg")])
    for t in (1.5, 20, 45, 70, 95, 130, 175, d - 18, d - 6, d - 1.2):
        if 0 < t < d:
            run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}",
                 "-i", str(final), "-frames:v", "1", str(qc / f"t{t:07.2f}.png")])
    print(f"  duration {d:.1f}s -> {qc}")


STAGES = {"plates": stage_plates, "shots": stage_shots,
          "build": stage_build, "qc": stage_qc}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all", choices=["all", *STAGES])
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    V2.mkdir(exist_ok=True)
    for name in (STAGES if a.stage == "all" else [a.stage]):
        STAGES[name]()
    print("\nDone.")


if __name__ == "__main__":
    main()
