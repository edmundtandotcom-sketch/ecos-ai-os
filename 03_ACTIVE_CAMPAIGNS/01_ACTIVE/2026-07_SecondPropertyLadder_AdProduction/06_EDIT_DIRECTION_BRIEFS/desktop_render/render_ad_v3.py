#!/usr/bin/env python3
"""
S&P Benchmark - 60s TEST cut, built to how the reference ads are actually edited.

v2 was measured against the MEDIAN of the swipe library, which averages in the
lazy ads. The ads that actually hold a scroller cut at 51-57/min with ~1.0s
shots (Freedom Growth Academy, I Quadrant). Watched frame-by-frame at 15fps,
the grammar is:

  * ONE SHOT PER CAPTION PHRASE - the cut lands exactly on the phrase change
  * hard cuts only, no whips or dissolves
  * framing alternates wide / medium / close, never twice in a row
  * a SLOW PUSH inside every shot, so the frame is never still
  * the hook headline BUILDS line by line, payoff word landing in yellow
  * b-roll cutaways carry the abstract lines
  * a number lands as an animated reveal, not a static slide
  * 1.15x on the final render

This builds a 60s slice to judge those mechanics before committing the full cut.

    python render_ad_v3.py --stage all
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
V3 = OUT / "v3"
BROLL = Path(r"E:\REMOTION\public\broll\stock")
AUDIO = Path(r"E:\REMOTION\public\audio")
OUT_NAME = "SP_BENCHMARK_9x16_TEST60.mp4"

W, H, FPS = 1080, 1920, 30
SPEED = 1.15
LOUDNORM_I = -16
MUSIC_VOL = 0.09

FACE_CX, EYE_Y = 663, 238
# wide / medium / close. z=1.00 is the widest the source allows.
ZOOMS = [1.00, 1.10, 1.20]
PUSH = 0.05              # each shot creeps in this much across its own length

# Content blocks for the 60s cut: hook -> cost -> reframe -> benchmark -> proof.
# Times are on the TIGHTENED body timeline (out/words_body_tight.json).
BLOCKS = [
    ("hook",   0.00, 13.60),
    ("cost",  13.60, 24.05),
    ("swap",  24.05, 39.60),
    ("bench", 39.60, 46.60),
    ("proof", 76.30, 86.60),
]

# B-roll cutaways: (block, offset into block, seconds, clip)
# Each one carries an abstract line the face cannot illustrate.
BROLLS = [
    ("cost",  3.0, 1.3, "hdb_apartments.mp4"),   # "$500K to $1 million"
    ("cost",  8.2, 1.3, "heartland_roofs.mp4"),  # "25 year mortgage"
    ("swap",  1.2, 1.6, "sg_skyline2.mp4"),      # "that same money"
    ("swap",  6.0, 1.4, "downtown.mp4"),         # "the S&P 500"
    ("swap", 12.4, 1.4, "couple_talk.mp4"),      # "who your future buyer is"
    ("bench", 3.4, 1.4, "sg_aerial.mp4"),        # "beating the S&P 500"
]

# Captions ride BELOW the chin (deepest measured chin is y=1181). The
# reference sits them mid-frame, but that assumes a medium shot; with a
# full-frame head, mid-frame is his mouth.
CAP_Y = 0.74
PUNCH_Y = 0.72
HOOK_Y = 0.70
# Red perimeter progress bar - traces the frame edge as the ad plays.
PROGRESS_BAR = 12
CAP_SIZE = 84
CAP_FONT = "Impact"
CAP_MAX_WORDS = 4
ACCENT = "&H0035FFDF&"

# The hook is a full-frame typographic hit, not a modest stack. Surveying 28
# reference openings: giant angled outlined caps, one beat at a time, each
# slamming in oversized and settling. Sizes here are 2-3x the narration.
# Each beat is anchored to the WORD he says it on, not a hand-guessed second -
# hardcoded times drifted off the audio ("PROPERTY?" landed before he said it).
HOOK_BEATS = [
    # (anchor phrase, text, size, rotation, colour)
    ("is this your",  "IS THIS YOUR",           108, -3, "white"),
    ("2nd",           "2ND, 3RD\\NOR 4TH",      180,  3, "accent"),
    ("property",      "PROPERTY?",              168, -2, "white"),
]
HOOK_END = 3.30

# Caption treatment rotates every few seconds so the look never settles -
# the reference ads never hold one caption style for more than a few beats.
TREATMENT_BAND = 4.0     # seconds before the treatment changes
ROTATION = ["narr", "punch", "narr", "box", "narr", "build"]

# White frame flash on a slam - 2 frames, the reference cut-flash.
FLASH_FRAMES = 2

# Motion per shot. The reference never holds a still frame, but it also does
# not move everything the same way: narration drifts, punchlines snap.
PUNCH_Z = 0.13           # quick zoom-in on a punchline, lands in ~0.18s
SLAM_Z = 0.20            # segment opener starts oversized and settles
SLAM_SETTLE = 0.28       # seconds for a segment opener to settle
# Key words render BIGGER as well as coloured, so the point carries on its own.
ACCENT_SCALE = 1.34

# Number reveals: dropped. The punch treatment already renders the figure
# oversized and in accent colour on the beat it is spoken, which reads as the
# reveal - a navy band on top of that is two treatments fighting for the same
# moment. Kept as a hook for a future variant that wants a distinct data card.
NUMBERS = []


def run(cmd):
    sys.stdout.flush()
    subprocess.run(cmd, check=True)


def ffprobe(path, entries="format=duration"):
    return json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries, "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout)


def dur_of(p):
    return float(ffprobe(p)["format"]["duration"])


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# Whisper mis-hears and mis-splits a few things every time. Fixed on the WORD
# STREAM before cues are formed - a per-cue fix never sees a phrase that
# straddles a cue boundary, which is how "&P 500" reached the screen.
GLUE = [(("S", "&P"), "S&P")]
FIXES = {"compiles": "compounds", "compile": "compound"}


def fix_tokens(words):
    out, i = [], 0
    while i < len(words):
        merged = False
        for pair, rep in GLUE:
            n = len(pair)
            if tuple(w["w"] for w in words[i:i + n]) == pair:
                out.append(dict(w=rep, s=words[i]["s"], e=words[i + n - 1]["e"]))
                i += n
                merged = True
                break
        if merged:
            continue
        w = dict(words[i])
        key = w["w"].strip(".,?!").lower()
        if key in FIXES:
            w["w"] = w["w"].lower().replace(key, FIXES[key])
        out.append(w)
        i += 1
    return out


def find_phrase(words, phrase, after=0):
    """Locate a phrase in the word stream; returns (start_time, word_index).

    Matches on a spaceless normalised string so "S&P" / "S &P" both hit.
    """
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
    return words[owner[pos]]["s"], owner[pos]


def load_words(name):
    raw = json.loads((OUT / f"words_{name}_tight.json").read_text(encoding="utf-8"))
    return fix_tokens(raw)


def cue_split(words):
    """Phrase cues. One cue == one shot, so this drives the whole cut."""
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
        over = len(cur) > CAP_MAX_WORDS or len(joined) >= 26
        if hard or gap > 0.26 or len(cur) >= CAP_MAX_WORDS or len(joined) >= 22:
            if not hard and nxt is not None and len(cur) < 2:
                continue
            if not hard and nxt is not None and not over and norm(w["w"]) in TRAIL:
                continue
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)
    return cues


def crop_for(z):
    w = int(round(W / H * 720 / z)) & ~1
    h = int(round(720 / z)) & ~1
    x = max(0, min(1280 - w, int(round(FACE_CX - w / 2))))
    y = max(0, min(720 - h, int(round(EYE_Y - 0.30 * h))))
    return w, h, x, y


GRADE = "eq=contrast=1.06:brightness=0.012:saturation=1.07,unsharp=5:5:0.35:5:5:0.0"


def motion_chain(nframes, kind="push"):
    """Per-shot camera move.

    push  - slow drift, the default; the frame is never static
    punch - snaps in over ~0.18s then holds, for a punchline
    slam  - opens oversized and settles, marking a new segment
    """
    n = max(1, nframes - 1)
    if kind == "punch":
        r = max(1, int(0.18 * FPS))
        z = f"1+{PUNCH_Z}*min(1,on/{r})"
    elif kind == "slam":
        r = max(1, int(SLAM_SETTLE * FPS))
        z = f"1+{SLAM_Z}*(1-min(1,on/{r}))"
    else:
        z = f"1+{PUSH}*on/{n}"
    return (f"scale={W*2}:{H*2}:flags=lanczos,"
            f"zoompan=z='{z}':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d=1:s={W}x{H}:fps={FPS},setsar=1")


# ----------------------------------------------------------------------------

def make_numbers():
    """Small animated bands for the spoken figures.

    Cropping the big proof plate for this put an empty navy slab on screen -
    the number needs its own artwork sized for a band, not a reused plate.
    """
    from PIL import Image, ImageDraw, ImageFont

    def font(sz):
        return ImageFont.truetype(r"C:\Windows\Fonts\impact.ttf", sz)

    for pct, dst, sub in (("22.9%", "_num_229.png", "A YEAR ON CAPITAL COMMITTED"),
                          ("12.9%", "_num_129.png", "A YEAR ON CAPITAL COMMITTED")):
        im = Image.new("RGBA", (W, 300), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([40, 0, W - 40, 262], 26, fill=(11, 16, 32, 236))
        fb, fs, fu = font(168), font(46), font(58)
        d.text((88, 22), pct, font=fb, fill=(255, 232, 0, 255))
        wp = d.textlength(pct, font=fb)
        d.text((88 + wp + 18, 118), "/YR", font=fu, fill=(255, 232, 0, 255))
        d.text((92, 196), sub, font=fs, fill=(225, 231, 245, 255))
        im.save(GFX / dst)
    print("  number bands: _num_229.png, _num_129.png")


def build_shotlist():
    words = load_words("body")
    shots = []
    for name, b0, b1 in BLOCKS:
        inner = [w for w in words if w["s"] >= b0 - 0.01 and w["e"] <= b1 + 0.30]
        if not inner:
            continue
        cues = cue_split(inner)
        brolls = [(b[1], b[2], b[3]) for b in BROLLS if b[0] == name]
        for cue in cues:
            t0 = max(b0, cue[0]["s"] - 0.10)
            t1 = min(b1, cue[-1]["e"] + 0.12)
            if t1 - t0 < 0.30:
                continue
            rel = t0 - b0
            bro = next((x for x in brolls if x[0] <= rel < x[0] + x[1]), None)
            shots.append(dict(block=name, t0=round(t0, 3), t1=round(t1, 3),
                              text=" ".join(x["w"] for x in cue),
                              cue=[dict(w=x["w"], s=x["s"], e=x["e"]) for x in cue],
                              broll=bro[2] if bro else None))
    prev = -1
    seen_blocks = set()
    for i, s in enumerate(shots):
        z = (prev + 1 + (i % 2)) % len(ZOOMS)
        s["zoom"] = z
        prev = z
        # first shot of a block opens the segment with a slam
        if s["block"] not in seen_blocks:
            seen_blocks.add(s["block"])
            s["motion"] = "slam"
            s["segment_start"] = True
        elif re.search(r"[\d$%]", s["text"]) and not s["broll"]:
            s["motion"] = "punch"
        else:
            s["motion"] = "push"
    return shots


def stage_shots():
    print("\n== SHOTS (60s test) ==")
    make_numbers()
    shots = build_shotlist()
    body = OUT / "_tight_body.mp4"
    work = V3 / "shots"
    work.mkdir(parents=True, exist_ok=True)
    for f in work.glob("*.mp4"):
        f.unlink()

    total = sum(s["t1"] - s["t0"] for s in shots)
    nb = sum(1 for s in shots if s["broll"])
    print(f"  {len(shots)} shots, {total:.1f}s source -> {total/SPEED:.1f}s at {SPEED}x")
    print(f"  median shot {sorted(s['t1']-s['t0'] for s in shots)[len(shots)//2]:.2f}s"
          f"  ({len(shots)/(total/60):.0f} cuts/min)")
    print(f"  {nb} b-roll cutaways")

    parts, tl = [], 0.0
    for i, s in enumerate(shots):
        d = s["t1"] - s["t0"]
        nf = max(2, int(round(d * FPS)))
        p = work / f"s{i:03d}.mp4"
        if s["broll"]:
            # b-roll carries the picture; the speaker's audio keeps running
            src = BROLL / s["broll"]
            vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
                  f"crop={W}:{H},{GRADE},fps={FPS},{motion_chain(nf, s['motion'])}")
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-stream_loop", "-1", "-t", f"{d:.3f}", "-i", str(src),
                 "-ss", f"{s['t0']:.3f}", "-to", f"{s['t1']:.3f}", "-i", str(body),
                 "-filter_complex", f"[0:v]{vf}[v]",
                 "-map", "[v]", "-map", "1:a",
                 "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                 "-pix_fmt", "yuv420p", "-r", str(FPS),
                 "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                 "-video_track_timescale", "90000", str(p)])
        else:
            w, h, x, y = crop_for(ZOOMS[s["zoom"]])
            vf = f"crop={w}:{h}:{x}:{y},{GRADE},fps={FPS},{motion_chain(nf, s['motion'])}"
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{s['t0']:.3f}", "-to", f"{s['t1']:.3f}", "-i", str(body),
                 "-vf", vf,
                 "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                 "-pix_fmt", "yuv420p", "-r", str(FPS),
                 "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                 "-video_track_timescale", "90000", str(p)])
        s["out0"] = round(tl, 3)
        tl += dur_of(p)
        s["out1"] = round(tl, 3)
        parts.append(p)

    lst = V3 / "shots.txt"
    lst.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in parts),
                   encoding="utf-8")
    dest = V3 / "_cut.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(dest)])
    (V3 / "shots.json").write_text(json.dumps(shots, indent=1), encoding="utf-8")
    print(f"  -> {dest.name}  {dur_of(dest):.1f}s")


# ----------------------------------------------------------------------------

def ass_esc(p):
    return str(p).replace("\\", "/").replace(":", "\\:")


def score_accent(cue):
    STOP = {"a", "an", "the", "and", "or", "but", "to", "of", "for", "in", "on",
            "at", "is", "are", "was", "your", "my", "i", "we", "you", "it",
            "that", "this", "so", "if", "as", "with", "have", "has"}
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


def build_ass(shots, path, hook=True, hook_words=None):
    """One cue per shot, timed to the shot - captions change ON the cut."""
    def ts(t):
        return f"{int(t//3600):d}:{int(t%3600//60):02d}:{t%60:05.2f}"

    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Ad,{CAP_FONT},{CAP_SIZE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,7,3,5,95,95,0,1
Style: Punch,{CAP_FONT},150,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,10,5,5,60,60,0,1
Style: Box,{CAP_FONT},98,&H00FFFFFF,&H00FFFFFF,&H002020E0,&H002020E0,0,0,0,0,100,100,1,0,3,16,0,5,90,90,0,1
Style: Build,{CAP_FONT},124,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,9,4,5,80,80,0,1
Style: Hook,{CAP_FONT},116,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,11,5,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    flashes = []
    # While the hook statement owns the frame, the narration caption is
    # suppressed - drawing both stacks two type sizes on the same spot.
    for k, s in enumerate(shots):
        if hook and s['out0'] < HOOK_END - 0.05:
            continue
        ai = score_accent(s["cue"])
        words = [re.sub(r"[,]$", "", w["w"]).upper() for w in s["cue"]]
        has_num = any(re.search(r"[\d$%]", w) for w in words)

        # treatment: bands of a few seconds, but a figure always punches
        band = int(s["out0"] // TREATMENT_BAND)
        tr = "punch" if has_num else ROTATION[band % len(ROTATION)]
        if tr == "punch" and len(words) > 4:
            tr = "narr"

        if tr == "punch":
            style, y, size_tag = "Punch", PUNCH_Y, ""
            rot = -3 if k % 2 else 3
            # slam: lands oversized and settles in ~110ms
            anim = ("{\\an5\\pos(%d,%d)\\frz%d\\fscx126\\fscy126"
                    "\\t(0,110,\\fscx100\\fscy100)}" % (W // 2, int(H * y), rot))
            flashes.append(s["out0"])
        elif tr == "box":
            style, anim = "Box", ("{\\an5\\pos(%d,%d)\\fad(40,0)}"
                                  % (W // 2, int(H * 0.60)))
        elif tr == "build":
            style, anim = "Build", ("{\\an5\\pos(%d,%d)\\fad(70,0)"
                                    "\\fscx112\\fscy112\\t(0,130,\\fscx100\\fscy100)}"
                                    % (W // 2, int(H * 0.50)))
        else:
            style, anim = "Ad", ("{\\an5\\pos(%d,%d)\\fad(60,0)}"
                                 % (W // 2, int(H * CAP_Y)))

        base_fs = {"Punch": 150, "Box": 98, "Build": 124}.get(style, CAP_SIZE)
        big = int(base_fs * ACCENT_SCALE)
        txt = ""
        for i, word in enumerate(words):
            if i == ai and style != "Box":
                # bigger AND coloured - the point has to carry on its own
                txt += (f"{{\\fs{big}\\c{ACCENT}}}{word}"
                        f"{{\\fs{base_fs}\\c&H00FFFFFF&}} ")
            else:
                txt += f"{word} "
        if s.get("segment_start"):
            flashes.append(s["out0"])
        lines.append(f"Dialogue: 0,{ts(s['out0'])},{ts(s['out1'])},{style},,0,0,0,,"
                     f"{anim}{txt.strip()}")
    Path(str(path) + ".flash").write_text(json.dumps(sorted(set(flashes))),
                                          encoding="utf-8")
    Path(str(path) + ".seg").write_text(
        json.dumps([x["out0"] for x in shots if x.get("segment_start")]),
        encoding="utf-8")

    # hook: each beat is a full-frame slam, replacing the last, not stacking
    if hook:
        beats = []
        for phrase, text, size, rot, col in HOOK_BEATS:
            hit = find_phrase(hook_words, phrase, 0) if hook_words else None
            beats.append((hit[0] if hit else 0.0, text, size, rot, col))
        for k, (at, text, size, rot, col) in enumerate(beats):
            t1 = beats[k + 1][0] if k + 1 < len(beats) else HOOK_END
            colour = ACCENT if col == "accent" else "&H00FFFFFF&"
            tag = ("{\\an5\\pos(%d,%d)\\fs%d\\c%s\\frz%d"
                   "\\fscx122\\fscy122\\t(0,120,\\fscx100\\fscy100)}"
                   % (W // 2, int(H * HOOK_Y), size, colour, rot))
            lines.append(f"Dialogue: 1,{ts(at)},{ts(t1)},Hook,,0,0,0,,{tag}{text}")

    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


def stage_build():
    print("\n== BUILD ==")
    cut = V3 / "_cut.mp4"
    shots = json.loads((V3 / "shots.json").read_text(encoding="utf-8"))
    body_words = load_words("body")
    n = build_ass(shots, V3 / "caps.ass", hook_words=body_words)
    print(f"  {n} caption/hook events")

    filt = [f"[0:v]ass='{ass_esc(V3 / 'caps.ass')}'[base]"]
    inputs = ["-i", str(cut)]
    last, idx = "base", 1
    for token, art in NUMBERS:
        hit = next((s for s in shots if s["block"] == "proof"
                    and token in s["text"]), None)
        if not hit:
            continue
        t0, t1 = hit["out0"], hit["out1"] + 1.3
        inputs += ["-framerate", str(FPS), "-i", str(GFX / art)]
        nf = int((t1 - t0) * FPS) + 4
        filt.append(
            f"[{idx}:v]loop=loop={nf}:size=1,fps={FPS},"
            f"setpts=PTS-STARTPTS+{t0:.3f}/TB,"
            f"fade=t=in:st={t0:.2f}:d=0.12:alpha=1,"
            f"fade=t=out:st={t1-0.22:.2f}:d=0.22:alpha=1[n{idx}]")
        # slides up into place over 0.22s, then holds
        y = int(H * 0.115)
        filt.append(
            f"[{last}][n{idx}]overlay=x=0:"
            f"y='{y}+70*max(0,1-(t-{t0:.3f})/0.22)':"
            f"enable='between(t,{t0:.3f},{t1:.3f})'[v{idx}]")
        last = f"v{idx}"
        idx += 1
        print(f"  number reveal '{token}' at {t0:.2f}s")
    # cut-flash on every slam: two white frames, the reference punctuation
    fl = Path(str(V3 / "caps.ass") + ".flash")
    if fl.exists():
        d = FLASH_FRAMES / FPS
        for t in json.loads(fl.read_text(encoding="utf-8")):
            filt.append(f"[{last}]drawbox=x=0:y=0:w={W}:h={H}:color=white@0.30:"
                        f"t=fill:enable='between(t,{t:.3f},{t + d:.3f})'[f{idx}]")
            last = f"f{idx}"
            idx += 1
    filt.append(f"[{last}]null[vout]")

    part = V3 / "_captioned.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex", ";".join(filt), "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part)])

    # ---- CTA ----
    cta_src = OUT / "_tight_cta.mp4"
    cw, ch, cx, cy = crop_for(ZOOMS[0])
    cwords = load_words("cta")
    ccues = cue_split(cwords)
    cshots = [dict(cue=[dict(w=x["w"], s=x["s"], e=x["e"]) for x in c],
                   out0=c[0]["s"], out1=c[-1]["e"], block="cta",
                   text=" ".join(x["w"] for x in c)) for c in ccues]
    build_ass(cshots, V3 / "caps_cta.ass", hook=False)
    part_cta = V3 / "_part_cta.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", "-i", str(cta_src),
         "-filter_complex",
         # The CTA was being left at the crop size (404x720) instead of scaled to
        # the canvas - which broke the concat and took the audio with it.
        f"[0:v]crop={cw}:{ch}:{cx}:{cy},scale={W}:{H}:flags=lanczos,setsar=1,"
        f"{GRADE},fps={FPS},"
         f"drawbox=x=0:y=0:w={W}:h={H}:color=red@1.0:t=14,"
         f"ass='{ass_esc(V3 / 'caps_cta.ass')}'[vout]",
         "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_cta)])

    lst = V3 / "join.txt"
    lst.write_text("".join(f"file '{p.resolve().as_posix()}'\n"
                           for p in (part, part_cta)), encoding="utf-8")
    joined = V3 / "_joined.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(joined)])

    # ---- final assembly in ONE pass ----
    # The copy-concat was silently dropping the CTA's audio at the seam, so the
    # whole call to action played mute. The concat FILTER re-encodes both
    # streams together and cannot lose one.
    segf = Path(str(V3 / "caps.ass") + ".seg")
    segs = [t for t in (json.loads(segf.read_text(encoding="utf-8"))
                        if segf.exists() else []) if t > 0.2]
    body_d, cta_d = dur_of(part), dur_of(part_cta)
    raw_d = body_d + cta_d
    out_d = raw_d / SPEED

    bed = AUDIO / "rei_bed_pulse.mp3"
    wh = AUDIO / "whoosh1.mp3"
    inputs = ["-i", str(part), "-i", str(part_cta),
              "-stream_loop", "-1", "-i", str(bed)]
    for _ in segs:
        inputs += ["-i", str(wh)]

    f = ["[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[cv][ca]"]
    amix_in = "[ca]"
    for i, t in enumerate(segs):
        f.append(f"[{3+i}:a]adelay={int(t*1000)}|{int(t*1000)},volume=0.45[wh{i}]")
        amix_in += f"[wh{i}]"
    if segs:
        f.append(f"{amix_in}amix=inputs={len(segs)+1}:duration=first:"
                 f"dropout_transition=0,volume={len(segs)+1}[mixed]")
    else:
        f.append("[ca]anull[mixed]")
    f.append(f"[mixed]atempo={SPEED}[sp]")
    f.append(f"[2:a]volume={MUSIC_VOL},afade=t=out:st={out_d-2.0:.2f}:d=2.0[bed]")
    f.append(f"[sp][bed]amix=inputs=2:duration=first:dropout_transition=0,"
             f"loudnorm=I={LOUDNORM_I}:TP=-1.5:LRA=11[a]")
    f.append(f"[cv]setpts=PTS/{SPEED}[vs]")
    f.extend(progress_bar(out_d))

    final = OUT / OUT_NAME
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex", ";".join(f),
         "-map", "[vout]", "-map", "[a]", "-t", f"{out_d:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", str(final)])
    print(f"  whoosh on {len(segs)} segment boundaries")
    print(f"\n  OK {final.name}  {dur_of(final):.1f}s, "
          f"{final.stat().st_size/1e6:.1f} MB")


def progress_bar(total, src="vs", dst="vout"):
    """Red line tracing the frame perimeter, closing exactly as the ad ends.

    Built from four sliding colour bars rather than drawbox: drawbox evaluates
    its w/h expressions once at filter-init, so a time-based size just draws a
    full border for the whole video. overlay DOES re-evaluate x/y per frame, so
    each leg is a full-length bar slid into place from off-frame.
    """
    b, P = PROGRESS_BAR, 2 * (W + H)
    prog = f"({P}*t/{total:.3f})"
    top = f"min({prog},{W})"
    right = f"min(max(0,{prog}-{W}),{H})"
    bottom = f"min(max(0,{prog}-{W + H}),{W})"
    left = f"min(max(0,{prog}-{2 * W + H}),{H})"
    d = f"{total:.3f}"
    return [
        f"color=c=red:s={W}x{b}:d={d}:r={FPS}[pgt]",
        f"color=c=red:s={b}x{H}:d={d}:r={FPS}[pgr]",
        f"color=c=red:s={W}x{b}:d={d}:r={FPS}[pgb]",
        f"color=c=red:s={b}x{H}:d={d}:r={FPS}[pgl]",
        f"[{src}][pgt]overlay=x='{top}-{W}':y=0:shortest=1[pg1]",
        f"[pg1][pgr]overlay=x={W - b}:y='{right}-{H}':shortest=1[pg2]",
        f"[pg2][pgb]overlay=x='{W}-{bottom}':y={H - b}:shortest=1[pg3]",
        f"[pg3][pgl]overlay=x=0:y='{H}-{left}':shortest=1[{dst}]",
    ]


def stage_qc():
    print("\n== QC ==")
    final = OUT / OUT_NAME
    d = dur_of(final)
    qc = V3 / "qc"
    qc.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(final),
         "-vf", f"fps=2,scale=180:-2,tile=12x{math.ceil(d*2/12)}",
         "-frames:v", "1", str(qc / "every_half_second.jpg")])
    print(f"  {d:.1f}s -> {qc/'every_half_second.jpg'}")


STAGES = {"shots": stage_shots, "build": stage_build, "qc": stage_qc}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all", choices=["all", *STAGES])
    a = ap.parse_args()
    V3.mkdir(parents=True, exist_ok=True)
    for k in (STAGES if a.stage == "all" else [a.stage]):
        STAGES[k]()
    print("\nDone.")


if __name__ == "__main__":
    main()
