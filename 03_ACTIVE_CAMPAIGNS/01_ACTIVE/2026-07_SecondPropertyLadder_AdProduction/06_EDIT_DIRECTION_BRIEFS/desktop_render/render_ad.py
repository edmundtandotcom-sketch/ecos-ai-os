#!/usr/bin/env python3
"""
REI ad renderer — desktop.

Renders a 9:16 ad from a face-cam body clip + CTA clip, following an Edit
Direction Brief: graded footage, karaoke captions, timed brand-graphic overlays,
end card.

Built for EDB_SP-Benchmark_NL01_v1 (NL01 "Can It Beat the S&P 500?") but the
CONFIG block and BEATS table are the only campaign-specific parts.

Runs entirely locally. Nothing is uploaded.

    python render_ad.py --stage all

Stages: probe · transcribe · frame · graphics · render · qc
Run them individually while iterating, e.g. `--stage frame` to re-check framing.
"""

import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ----------------------------------------------------------------------------
# CONFIG — edit these, not the code below
# ----------------------------------------------------------------------------

# Source clips. Point these at the real files.
BODY_CLIP = r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-07_SecondPropertyLadder_AdProduction\03_RECORDING_OUTPUTS\10-S&P Angle\Raw Assets\S&P-DSLR.mp4"
CTA_CLIP  = r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-07_SecondPropertyLadder_AdProduction\03_RECORDING_OUTPUTS\10-S&P Angle\Raw Assets\S&P CTA-DSLR.mp4"

OUT_DIR = Path("./out")
OUT_NAME = "SP_BENCHMARK_9x16_v1.mp4"

W, H = 1080, 1920           # 9:16 deliverable
FPS = 30

# Framing spec (EDB §3). Auto-framing aims for this; override CROP if needed.
HEAD_PCT_MIN, HEAD_PCT_MAX = 0.12, 0.16   # crown-to-chin as fraction of frame height
EYELINE_PCT = 0.40                         # eye-line, fraction down from top

# Manual crop override. Leave None for auto. Format: (x, y, w, h) in SOURCE pixels.
# Full-bleed 9:16, the way a reel is normally framed - the picture fills the
# canvas, no letterbox. 405x720 is the widest 9:16 window the 1280x720 source
# holds, so this is the most pulled-back a full-frame crop can be; x is centred
# on the speaker (face centre sits at 663 +/- 40 across both takes).
CROP_OVERRIDE = (460, 0, 405, 720)
# If auto-framing makes the head too large, the source is scaled down inside the
# 9:16 canvas over a blurred fill rather than cropping tighter.

# Measured framing override, for sources shot tighter than the head-size target.
# Cropping can only make a head BIGGER, so the only fix is to pull the whole
# picture back and fill the surround with a blurred copy of itself (EDB S3:
# "pull back the crop - add letterbox/blur-fill"). Values are SOURCE pixels,
# read off a real frame. Leave None to use the automatic Haar measurement.
#   head_top    - top of the hair (crown)
#   head_bottom - bottom of the chin
#   eye_y       - pupil centre
# Letterboxed alternative, kept for reference: this is what hits the EDB's
# 12-16% head-size spec, at the cost of a small picture in a navy surround.
# Set CROP_OVERRIDE = None to use it.
FIT_OVERRIDE = None

# Overlay bands, in pixels of the 1080x1920 canvas. With a full-bleed close-up
# there is no empty margin, so these are measured off the speaker rather than
# guessed. He leans in and out across the take, so the band is set by the
# DEEPEST his chin ever gets, not by one reference frame: sampling every 7s
# put the chin at y=1181 worst case in the body and 1192 in the CTA.
LOWER_TOP = 1210
# The caption line starts around y=1560 (64px text bottom-anchored at 85.5%),
# so anything taller than this gap gets scaled down rather than sitting on the
# subtitles. The 340-360px data cards are just over it.
LOWER_MAX_H = 335
# The hook rides at the very top, over hair and background only.
UPPER_Y = 0.005

# Where in the 12-16% band to aim.
TARGET_HEAD_PCT = 0.15
# What surrounds the picture once it is scaled back: "navy" (flat brand navy,
# matching the graphics cards) or "blur" (blurred copy of the frame). Navy reads
# as designed letterbox; blur at this magnification is just a smear of face.
FILL_MODE = "navy"
# Haar's frontal-face box is forehead-to-chin and misses the hair; multiply to
# approximate true crown-to-chin when auto-measuring.
HAAR_TO_HEAD = 1.30

# Palette — Family B, REI Core (EDB §1)
NAVY      = (11, 16, 32)
NAVY_CARD = (20, 27, 51)
BLUE      = (0, 92, 230)
YELLOW    = (255, 232, 0)
WHITE     = (255, 255, 255)

# Whisper model for word timings. Captions are burned from this transcript, so
# mishearings ship on screen - accuracy is worth the extra minutes.
WHISPER_MODEL = "medium"
# Force the language. Auto-detect put the first ~55s of the body take into
# Malay and produced pure gibberish, which also broke every beat anchor in it.
WHISPER_LANG = "en"
# Bias the decoder towards this angle's vocabulary. Without it "S&P 500" comes
# back as "SMP 500", "stamp duty" as "stem beauty", "walkaway price" as "work
# away price".
WHISPER_PROMPT = (
    "Singapore property investment. Terms used: the S&P 500, stamp duty, "
    "ABSD, CPF, mortgage, agent fees, legal fees, return on equity, "
    "walkaway price, entry price, exit price, usable equity, new launch, "
    "the New Launch Ladder, show flat, cooling measures, net asset value."
)

# Voice normalisation target
LOUDNORM_I = -16

# ----------------------------------------------------------------------------
# Beats — overlays are anchored to SPOKEN PHRASES, not hardcoded timestamps, so
# they stay correct whatever the take's actual pacing turned out to be.
#
#   kind:  full   = full-frame cutaway (audio continues under it)
#          lower  = bottom-third overlay, never covers the face
#          upper  = upper-third overlay
#   start/end: ("phrase", offset_seconds). Phrase is fuzzy-matched in the
#          transcript. end may also be ("+", seconds) = start + N seconds.
# ----------------------------------------------------------------------------

BEATS = [
    dict(id="hook",    kind="upper", asset="g6_hook.png",
         start=("is this your", -0.2), end=("here's the question", 0.4)),

    dict(id="chip1",   kind="lower", asset="g5_chip1.png",
         start=("you commit", 0.0), end=("+", 6.0)),
    dict(id="chip2",   kind="lower", asset="g5_chip2.png",
         start=("year mortgage", -0.8), end=("+", 5.0)),
    dict(id="chip3",   kind="lower", asset="g5_chip3.png",
         start=("wait 4 years", -0.3), end=("+", 3.5)),

    dict(id="chart",   kind="full",  asset="g1_chart.png", flash=True,
         start=("so the benchmark", -0.3), end=("beating the s&p", 1.2)),

    dict(id="punch1",  kind="lower", asset="g7_gain.png",
         start=("easy test", -1.5), end=("+", 3.5)),

    dict(id="qcard",   kind="full",  asset="g3_question.png",
         start=("can this project beat", -0.3), end=("+", 2.6)),

    dict(id="dataA",   kind="lower", asset="g2a_card.png",
         start=("bought at", 0.0), end=("+", 12.0)),
    dict(id="dataB",   kind="lower", asset="g2b_card.png",
         start=("another property", 0.0), end=("+", 12.0)),

    dict(id="kin1",    kind="lower", asset="g8_entry.png",
         start=("at the entry price", -0.2), end=("+", 2.0)),
    dict(id="kin2",    kind="lower", asset="g8_unit.png",
         start=("the unit you choose", -0.2), end=("+", 2.0)),
    dict(id="kin3",    kind="lower", asset="g8_buyer.png",
         start=("your future buyer", -0.2), end=("+", 2.0)),
    dict(id="kin4",    kind="lower", asset="g8_exit.png",
         start=("your exit price", -0.2), end=("+", 2.0)),
    dict(id="kin5",    kind="lower", asset="g8_equity.png",
         start=("usable equity", -0.4), end=("+", 2.6)),

    dict(id="frame",   kind="full",  asset="g4_framework.png",
         start=("new launch ladder", -0.3), end=("+", 9.0)),

    dict(id="punch2",  kind="lower", asset="g7_enough.png",
         start=("money is no longer", -0.4), end=("+", 4.0)),
]

# CTA chip runs across the whole CTA clip; end card is appended after.
CTA_CHIP_ASSET = "g9_cta.png"
ENDCARD_ASSET = "g10_endcard.png"
ENDCARD_SECONDS = 3.0

# Pause removal. Both takes are teleprompter reads: 57% of the body clip is
# dead air, in 31 gaps of up to 12s. Untightened the ad runs ~7.5 minutes.
# Every internal pause is capped at PAD_OUT + PAD_IN seconds; head and tail
# dead air goes entirely. Set MAX_GAP = None to keep the raw pacing.
MAX_GAP = 0.38
PAD_OUT = 0.24          # kept after the last word before a cut
PAD_IN = 0.14           # kept before the first word after a cut

# Which CTA to ship. The CTA take contains all three variants read back to
# back, each announced "Call to Action 1 / 2 / 3"; only this one is used.
CTA_VARIANT = "C"

# ----------------------------------------------------------------------------

def run(cmd, **kw):
    """Run a command, streaming output, raising on failure."""
    sys.stdout.flush()
    if isinstance(cmd, str):
        printable = cmd
    else:
        printable = " ".join(str(c) for c in cmd)
    print(f"  $ {printable[:200]}{'…' if len(printable) > 200 else ''}")
    return subprocess.run(cmd, check=True, **kw)


def capture(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def ffprobe(path, entries):
    out = capture([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", entries, "-of", "json", str(path)
    ])
    return json.loads(out)


# ----------------------------------------------------------------------------
# Stage: probe
# ----------------------------------------------------------------------------

def stage_probe():
    print("\n== PROBE ==")
    missing = [t for t in ("ffmpeg", "ffprobe") if not shutil.which(t)]
    if missing:
        sys.exit(f"ERROR: not on PATH: {', '.join(missing)}\n"
                 f"Install FFmpeg, or add your existing binary's folder to PATH.")
    for label, p in (("BODY", BODY_CLIP), ("CTA", CTA_CLIP)):
        if not Path(p).exists():
            sys.exit(f"ERROR: {label} clip not found:\n  {p}\nFix the path in CONFIG.")
        info = ffprobe(p, "stream=width,height,r_frame_rate,duration")
        s = info["streams"][0]
        dur = float(s.get("duration") or 0)
        print(f"  {label}: {s['width']}x{s['height']}  {s.get('r_frame_rate')}  {dur:.1f}s")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print("  OK")


# ----------------------------------------------------------------------------
# Stage: transcribe  → word-level timings
# ----------------------------------------------------------------------------

def stage_transcribe():
    print("\n== TRANSCRIBE ==")
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("ERROR: pip install faster-whisper")

    model = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")
    for label, clip in (("body", BODY_CLIP), ("cta", CTA_CLIP)):
        dest = OUT_DIR / f"words_{label}.json"
        if dest.exists():
            print(f"  {label}: cached ({dest})")
            continue
        print(f"  {label}: transcribing… (several minutes)")
        segments, _ = model.transcribe(str(clip), word_timestamps=True,
                                       vad_filter=True,
                                       language=WHISPER_LANG,
                                       initial_prompt=WHISPER_PROMPT)
        words = []
        for seg in segments:
            for w in (seg.words or []):
                words.append(dict(w=w.word.strip(), s=round(w.start, 3),
                                  e=round(w.end, 3)))
        dest.write_text(json.dumps(words, indent=1), encoding="utf-8")
        print(f"  {label}: {len(words)} words → {dest}")

    cta = json.loads((OUT_DIR / "words_cta.json").read_text(encoding="utf-8"))
    text = " ".join(w["w"] for w in cta).lower()
    variant = ("C — 'tell me the project'" if "tell me the project" in text
               else "B — 'exactly how my properties'" if "exactly how" in text
               else "A — 'how to find'" if "how to find" in text else "UNRECOGNISED")
    print(f"\n  CTA VARIANT HEARD: {variant}")
    print(f"  (EDB assumes C — check this matches)")


def load_words(label):
    p = OUT_DIR / f"words_{label}.json"
    if not p.exists():
        sys.exit(f"ERROR: {p} missing — run --stage transcribe first")
    return json.loads(p.read_text(encoding="utf-8"))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _flatten(words):
    """Whole transcript as one normalised string + char->word-index map.

    Matching on a spaceless string means "S&P", "S &P" and "S & P" all collapse
    to "sp", so an anchor phrase does not have to guess Whisper's spacing.
    """
    flat, owner = [], []
    for i, w in enumerate(words):
        t = norm(w["w"])
        flat.append(t)
        owner.extend([i] * len(t))
    return "".join(flat), owner


def find_phrase(words, phrase, after_word=0):
    """Find a phrase at or after word index `after_word`.

    Returns (start, end, first_word_index) or None. Searching forward from a
    cursor is what keeps repeated lines - "your future buyer" is said twice -
    anchored to the right occurrence.
    """
    target = norm(phrase)
    if not target:
        return None
    flat, owner = _flatten(words)
    lo = 0
    while lo < len(owner) and owner[lo] < after_word:
        lo += 1
    pos = flat.find(target, lo)
    if pos < 0:
        return None
    i = owner[pos]
    j = owner[min(pos + len(target) - 1, len(owner) - 1)]
    return words[i]["s"], words[j]["e"], i


def resolve_beats(words, offset=0.0):
    """Turn BEATS phrase anchors into concrete (start, end) seconds.

    Anchors resolve in script order: each search starts where the previous
    beat's anchor was found, so a phrase repeated later in the take cannot
    steal an earlier beat (or vice versa).
    """
    resolved, misses = [], []
    cursor = 0
    for b in BEATS:
        ph, off = b["start"]
        hit = find_phrase(words, ph, cursor)
        if not hit:
            misses.append((b["id"], ph))
            continue
        cursor = hit[2]
        start = hit[0] + off + offset
        e = b["end"]
        if e[0] == "+":
            end = start + e[1]
        else:
            hit2 = find_phrase(words, e[0], cursor)
            end = (hit2[1] if hit2 else start + 4.0) + e[1] + offset
        if end <= start:
            end = start + 2.0
        # Clamp to zero: an anchor with a negative lead-in lands before the
        # clip starts, and ffmpeg rejects a negative fade start outright.
        resolved.append({**b, "t0": round(max(0.0, start), 2),
                         "t1": round(end, 2)})

    # Lower-thirds all sit at the same y, so an overrun would draw the next
    # card on top of the previous one with its edges still poking out. Retire
    # each card just before its successor arrives.
    lowers = [b for b in resolved if b["kind"] == "lower"]
    for cur, nxt in zip(lowers, lowers[1:]):
        cur["t1"] = round(min(cur["t1"], nxt["t0"] - 0.08), 2)
    return [b for b in resolved if b["t1"] > b["t0"]], misses


# ----------------------------------------------------------------------------
# Pause removal
# ----------------------------------------------------------------------------

def cta_variant_range(words, variant):
    """(t_lo, t_hi) covering just one CTA variant of a multi-variant take.

    The take reads all three CTAs back to back, each slated "Call to Action N".
    Returns the span after variant N's slate and before the next one.
    """
    want = {"A": "1", "B": "2", "C": "3"}[variant.upper()]
    slates = [(i, norm(words[i + 1]["w"]))
              for i in range(len(words) - 1)
              if norm(words[i]["w"]) == "action" and norm(words[i + 1]["w"]).isdigit()]
    if not slates:
        print("  ! no 'Call to Action N' slates found - using the whole CTA clip")
        return words[0]["s"], words[-1]["e"]
    mine = [k for k, (i, d) in enumerate(slates) if d == want]
    if not mine:
        sys.exit(f"ERROR: CTA variant {variant} (slate '{want}') not in the take")
    k = mine[0]
    t_lo = words[slates[k][0] + 1]["e"] + 0.25
    t_hi = (words[slates[k + 1][0]]["s"] - 0.25 if k + 1 < len(slates)
            else words[-1]["e"])
    print(f"  CTA variant {variant.upper()}: using {t_lo:.2f}-{t_hi:.2f}s "
          f"of {len(slates)} variants in the take")
    return t_lo, t_hi


def plan_segments(words, t_lo, t_hi):
    """Speech runs to keep, with every internal pause capped at MAX_GAP."""
    ws = [w for w in words if w["e"] > t_lo and w["s"] < t_hi]
    if not ws:
        return [(t_lo, t_hi)]
    segs = []
    cs = max(t_lo, ws[0]["s"] - PAD_IN)
    prev = ws[0]
    for cur in ws[1:]:
        if cur["s"] - prev["e"] > MAX_GAP:
            segs.append((cs, min(t_hi, prev["e"] + PAD_OUT)))
            cs = max(t_lo, cur["s"] - PAD_IN)
        prev = cur
    segs.append((cs, min(t_hi, prev["e"] + PAD_OUT)))
    # Snap to whole frames, always outwards - rounding to nearest would shave
    # the leading consonant off a segment's first word (it ate the "Is" of
    # "Is this your...", which then lost the hook overlay its anchor).
    return [(math.floor(a * FPS) / FPS, math.ceil(b * FPS) / FPS)
            for a, b in segs if b - a > 1.0 / FPS]


def tighten_clip(src, segs, dest, work):
    """Cut `segs` out of `src` and join them. Returns the real durations.

    Each piece is encoded on its own so ffmpeg keeps it in sync, then they are
    stream-copied together - no drift accumulates across 30-odd cuts. The
    measured durations come back so word timings can be remapped against what
    was actually written rather than what was requested.
    """
    work.mkdir(parents=True, exist_ok=True)
    for old in work.glob("seg*.mp4"):
        old.unlink()
    parts, durs = [], []
    for i, (a, b) in enumerate(segs):
        q = work / f"seg{i:03d}.mp4"
        run(["ffmpeg", "-y", "-loglevel", "error",
             "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(src),
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
             "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
             "-video_track_timescale", "90000", str(q)])
        parts.append(q)
        durs.append(float(ffprobe(q, "stream=duration")["streams"][0]["duration"]))
    lst = work / "concat.txt"
    lst.write_text("".join(f"file '{q.resolve().as_posix()}'\n" for q in parts),
                   encoding="utf-8")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(dest)])
    return durs


def remap_words(words, segs, durs):
    """Move word timings onto the tightened timeline."""
    out, base = [], 0.0
    for (a, b), d in zip(segs, durs):
        for w in words:
            if a - 0.001 <= w["s"] < b:
                out.append(dict(w=w["w"],
                                s=round(base + max(0.0, w["s"] - a), 3),
                                e=round(base + min(d, max(0.0, w["e"] - a)), 3)))
        base += d
    return out


def tighten(label, clip, words, t_lo, t_hi):
    """Tighten one clip. Returns (path, words on the new timeline)."""
    if MAX_GAP is None:
        return clip, words
    segs = plan_segments(words, t_lo, t_hi)
    dest = OUT_DIR / f"_tight_{label}.mp4"
    work = OUT_DIR / f"_tight_{label}"
    plan = json.dumps(segs)
    stamp = OUT_DIR / f"_tight_{label}.json"
    if dest.exists() and stamp.exists() and stamp.read_text(encoding="utf-8") == plan:
        durs = [float(ffprobe(q, "stream=duration")["streams"][0]["duration"])
                for q in sorted(work.glob("seg*.mp4"))]
        print(f"  {label}: tightened cut cached ({len(segs)} segments)")
    else:
        print(f"  {label}: cutting {len(segs)} speech segments out of "
              f"{t_hi - t_lo:.1f}s")
        durs = tighten_clip(clip, segs, dest, work)
        stamp.write_text(plan, encoding="utf-8")
    kept = sum(durs)
    print(f"  {label}: {t_hi - t_lo:.1f}s -> {kept:.1f}s "
          f"({(1 - kept / (t_hi - t_lo)) * 100:.0f}% dead air removed)")
    return dest, remap_words(words, segs, durs)


# ----------------------------------------------------------------------------
# Stage: frame  → measure the speaker, compute the 9:16 crop
# ----------------------------------------------------------------------------

def stage_frame():
    print("\n== FRAME ==")
    info = ffprobe(BODY_CLIP, "stream=width,height")["streams"][0]
    sw, sh = int(info["width"]), int(info["height"])
    print(f"  source: {sw}x{sh}")

    ref = OUT_DIR / "frame_ref.png"
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "5", "-i", str(BODY_CLIP),
         "-frames:v", "1", str(ref)])

    face = None
    try:
        import cv2
        img = cv2.imread(str(ref))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))
        if len(faces):
            face = max(faces, key=lambda f: f[2] * f[3])
            print(f"  face detected: x={face[0]} y={face[1]} w={face[2]} h={face[3]}")
    except ImportError:
        print("  (opencv not installed — using centred fallback;"
              " pip install opencv-python for auto-framing)")

    if FIT_OVERRIDE:
        fit = compute_fit(sw, sh, **FIT_OVERRIDE)
        geom = {"crop": None, "fit": fit}
        print("  using FIT_OVERRIDE (measured crown/chin)")
        print(f"  picture {fit['vw']}x{fit['vh']} at +{fit['x']}+{fit['y']}"
              f" over {FILL_MODE} fill")
        print(f"  head = {fit['head_pct']*100:.1f}% of frame height "
              f"(target {HEAD_PCT_MIN*100:.0f}-{HEAD_PCT_MAX*100:.0f}%)")
        print(f"  eye-line = {fit['eye_pct']*100:.1f}% "
              f"(target {EYELINE_PCT*100:.0f}%)")
        _write_geom(geom)
        _proof(geom)
        return

    if CROP_OVERRIDE:
        cx, cy, cw, ch = CROP_OVERRIDE
        scale = 1.0
        print(f"  using CROP_OVERRIDE: {cw}x{ch}+{cx}+{cy}")
    elif face is not None:
        fx, fy, fw, fh = face
        # Haar box ≈ forehead→chin, close enough to crown-to-chin for spec work.
        target_head = (HEAD_PCT_MIN + HEAD_PCT_MAX) / 2      # aim mid-band
        # Output frame height that would put this head at the target fraction:
        need_h = fh / target_head
        ch = min(sh, need_h)
        cw = ch * W / H
        if cw > sw:                       # source not wide enough → scale-down path
            cw, ch = sw, sw * H / W
        eye_y = fy + fh * 0.42
        cy = eye_y - ch * EYELINE_PCT
        cx = (fx + fw / 2) - cw / 2
        cx = max(0, min(sw - cw, cx))
        cy = max(0, min(sh - ch, cy))
        cx, cy, cw, ch = int(cx), int(cy), int(cw), int(ch)
        scale = fh / ch
        print(f"  computed crop: {cw}x{ch}+{cx}+{cy}")
        print(f"  head ≈ {scale*100:.1f}% of output height "
              f"(target {HEAD_PCT_MIN*100:.0f}–{HEAD_PCT_MAX*100:.0f}%)")
        if scale > HEAD_PCT_MAX:
            # Cropping cannot make a head smaller - the widest a crop can go is
            # the whole source. Scale the picture back instead and blur-fill.
            print("  ! head too large for any crop - scaling back over blurred fill")
            head = fh * HAAR_TO_HEAD
            fit = compute_fit(sw, sh,
                              head_top=(fy + fh / 2) - head / 2,
                              head_bottom=(fy + fh / 2) + head / 2,
                              eye_y=fy + fh * 0.42)
            geom = {"crop": None, "fit": fit}
            print(f"  head = {fit['head_pct']*100:.1f}% of frame height, "
                  f"eye-line = {fit['eye_pct']*100:.1f}%")
            _write_geom(geom)
            _proof(geom)
            return
    else:
        ch = sh
        cw = int(sh * W / H)
        cx = (sw - cw) // 2
        cy = 0
        print(f"  fallback centre crop: {cw}x{ch}+{cx}+{cy}")

    if cw > sw:
        # Source narrower than 9:16 - pillar it over a blurred fill instead.
        crop = None
        print("  source narrower than 9:16 -> blurred-fill pillarbox")
    else:
        crop = (int(cx), int(cy), int(cw), int(ch))

    geom = {"crop": crop, "fit": None}
    _write_geom(geom)
    _proof(geom)


def _even(n):
    n = int(round(n))
    return n - (n % 2)


def compute_fit(sw, sh, head_top, head_bottom, eye_y):
    """Scale the whole source into the 9:16 canvas so the head hits spec.

    For sources framed tighter than the head-size target. Never upscales and
    never exceeds the canvas width, so the head can only come out at or below
    the target - an over-tight face is the failure mode this exists to prevent.
    """
    head_src = float(head_bottom) - float(head_top)
    s = min((TARGET_HEAD_PCT * H) / head_src, W / sw, 1.0)
    vw, vh = _even(sw * s), _even(sh * s)
    s_eff = vw / sw
    y = int(round(EYELINE_PCT * H - eye_y * s_eff))
    if vh <= H:
        y = max(0, min(H - vh, y))
    else:
        y = 0
    return dict(vw=vw, vh=vh, x=_even((W - vw) / 2), y=y,
                head_pct=head_src * s_eff / H,
                eye_pct=(y + eye_y * s_eff) / H)


def _write_geom(geom):
    (OUT_DIR / "crop.json").write_text(json.dumps(geom), encoding="utf-8")


def _proof(geom):
    """Write the framing proof frame with the spec guides drawn over it."""
    vf = build_geometry_vf(geom) + (
        f",drawbox=y=0:h={int(H*0.10)}:t=fill:color=blue@0.18"
        f",drawbox=y={int(H*0.83)}:h={int(H*0.17)}:t=fill:color=blue@0.18"
        f",drawbox=y={int(H*EYELINE_PCT)}:h=3:t=fill:color=yellow@0.9"
        f",drawbox=y={int(H*0.08)}:h=2:t=fill:color=white@0.5"
    )
    proof = OUT_DIR / "frame_framing_check.png"
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "5", "-i", str(BODY_CLIP),
         "-frames:v", "1", "-vf", vf, str(proof)])
    print(f"\n  -> LOOK AT {proof}")
    print("    Yellow line = eye-line target. Blue bands = keep face clear.")
    print("    Wrong? set FIT_OVERRIDE/CROP_OVERRIDE and re-run --stage frame.")


def build_geometry_vf(geom):
    """Crop/scale/pad the source into the 9:16 canvas."""
    crop = geom.get("crop") if isinstance(geom, dict) else geom
    fit = geom.get("fit") if isinstance(geom, dict) else None
    if crop:
        x, y, w, h = crop
        return (f"crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,setsar=1")
    if fit:
        if FILL_MODE == "navy":
            navy = "0x%02X%02X%02X" % NAVY
            return (f"scale={fit['vw']}:{fit['vh']}:flags=lanczos,"
                    f"pad={W}:{H}:{fit['x']}:{fit['y']}:color={navy},setsar=1")
        return (f"split[a][b];[b]scale={W}:{H}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H},boxblur=40:2[bg];"
                f"[a]scale={fit['vw']}:{fit['vh']}:flags=lanczos[fg];"
                f"[bg][fg]overlay={fit['x']}:{fit['y']},setsar=1")
    # blurred-fill pillarbox
    return (f"split[a][b];[b]scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H},boxblur=40:2[bg];"
            f"[a]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
            f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1")


# ----------------------------------------------------------------------------
# Stage: graphics
# ----------------------------------------------------------------------------

def load_font(size, bold=True, black=False):
    from PIL import ImageFont
    here = Path(__file__).parent / "fonts"
    names = ([ "ArchivoBlack-Regular.ttf", "Anton-Regular.ttf" ] if black else
             [ "Montserrat-Bold.ttf", "Montserrat-SemiBold.ttf" ])
    for n in names:
        p = here / n
        if p.exists():
            return ImageFont.truetype(str(p), size)
    for sysname in (["impact.ttf", "arialbd.ttf"] if black else ["arialbd.ttf", "segoeuib.ttf"]):
        for d in (r"C:\Windows\Fonts", "/usr/share/fonts/truetype/dejavu"):
            p = Path(d) / sysname
            if p.exists():
                return ImageFont.truetype(str(p), size)
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    from PIL import ImageFont as IF
    return IF.load_default()


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_rich(draw, xy, parts, font, line_h, max_w, align="left", stroke=0):
    """Draw text where parts = [(text, colour), …], wrapping across the block.

    `stroke` adds a dark outline — essential for text laid over live footage,
    where the background brightness is unknown.
    """
    x0, y = xy
    line, lines = [], []
    width = 0
    for text, colour in parts:
        for word in text.split(" "):
            if not word:
                continue
            wlen = draw.textlength(word + " ", font=font)
            if width + wlen > max_w and line:
                lines.append(line); line = []; width = 0
            line.append((word, colour)); width += wlen
    if line:
        lines.append(line)
    kw = dict(stroke_width=stroke, stroke_fill=(8, 12, 24, 235)) if stroke else {}
    for ln in lines:
        total = sum(draw.textlength(w + " ", font=font) for w, _ in ln)
        x = x0 if align == "left" else x0 + (max_w - total) / 2
        for word, colour in ln:
            draw.text((x, y), word, font=font, fill=colour, **kw)
            x += draw.textlength(word + " ", font=font)
        y += line_h
    return y


def stage_graphics():
    print("\n== GRAPHICS ==")
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        sys.exit("ERROR: pip install pillow")

    g = OUT_DIR / "graphics"
    g.mkdir(parents=True, exist_ok=True)
    TRANS = (0, 0, 0, 0)

    def new_full():
        return Image.new("RGBA", (W, H), NAVY + (255,))

    def new_trans(h):
        return Image.new("RGBA", (W, h), TRANS)

    # ---- G1 chart interstitial -------------------------------------------
    im = new_full(); d = ImageDraw.Draw(im)
    f = load_font(76, black=True)
    draw_rich(d, (90, 330), [("THE BENCHMARK:", WHITE), (" BEAT", YELLOW),
                             (" THE S&P 500", WHITE)], f, 92, W - 180)
    x0, x1 = 140, W - 140
    ybase, ytop = int(H * 0.76), int(H * 0.47)
    sp = [(x0 + (x1 - x0) * i / 5, ybase - (ybase - ytop) * (0.12 + 0.62 * i / 5))
          for i in range(6)]
    d.line(sp, fill=WHITE, width=7, joint="curve")
    prop = [(x0, ybase), (x0 + (x1 - x0) * .35, ybase),
            (x0 + (x1 - x0) * .60, ybase - (ybase - ytop) * .30),
            (x0 + (x1 - x0) * .82, ybase - (ybase - ytop) * .72),
            (x1, ytop)]
    d.line(prop, fill=YELLOW, width=9, joint="curve")
    fl = load_font(34)
    d.text((x0, ybase + 40), "— S&P 500", font=fl, fill=WHITE)
    d.text((x0, ybase + 92), "— YOUR NEW LAUNCH", font=fl, fill=YELLOW)
    d.text((x0, ybase + 150), "4-year lockup · stamp duty · interest · fees",
           font=load_font(28), fill=(255, 255, 255, 130))
    im.save(g / "g1_chart.png"); print("  g1_chart")

    # ---- G3 question card -------------------------------------------------
    im = new_full(); d = ImageDraw.Draw(im)
    f = load_font(86, black=True)
    lines = _wrap(d, "CAN THIS PROJECT BEAT THE S&P 500?", f, W - 200)
    y = H // 2 - (len(lines) * 100) // 2
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=WHITE)
        y += 100
    d.rounded_rectangle([W // 2 - 44, y + 34, W // 2 + 44, y + 42], 4, fill=YELLOW)
    im.save(g / "g3_question.png"); print("  g3_question")

    # ---- G4 framework card ------------------------------------------------
    im = new_full(); d = ImageDraw.Draw(im)
    f = load_font(60, black=True)
    t = "THE NEW LAUNCH LADDER"
    d.text(((W - d.textlength(t, font=f)) / 2, 250), t, font=f, fill=WHITE)
    d.text((W // 2 + d.textlength(t, font=f) / 2 + 8, 250), "™",
           font=load_font(26), fill=YELLOW)
    rows = [("%", "RETURN ON EQUITY"), ("$", "WALKAWAY PRICE"), ("3", "NEXT 3 MOVES")]
    fb, fl2 = load_font(46, black=True), load_font(44)
    y = int(H * 0.42)
    for badge, label in rows:
        d.ellipse([140, y, 140 + 104, y + 104], outline=YELLOW, width=5)
        d.text((140 + 52 - d.textlength(badge, font=fb) / 2, y + 26),
               badge, font=fb, fill=YELLOW)
        d.text((300, y + 28), label, font=fl2, fill=WHITE)
        y += 190
    im.save(g / "g4_framework.png"); print("  g4_framework")

    # ---- G2a / G2b data cards (transparent, bottom-third) -----------------
    def data_card(num, l1, l2, path):
        card_h = 340
        im = new_trans(card_h); d = ImageDraw.Draw(im)
        d.rounded_rectangle([40, 0, W - 40, card_h - 10], 22,
                            fill=NAVY_CARD + (242,), outline=(255, 255, 255, 28), width=2)
        fn = load_font(104, black=True)
        d.text((84, 34), num, font=fn, fill=YELLOW)
        d.text((84 + d.textlength(num, font=fn) + 12, 92), "/YR",
               font=load_font(40, black=True), fill=YELLOW)
        d.line([84, 176, W - 124, 176], fill=YELLOW + (90,), width=3)
        fs = load_font(38)
        d.text((84, 200), l1, font=fs, fill=WHITE)
        d.text((84, 254), l2, font=fs, fill=(255, 255, 255, 190))
        im.save(path)

    data_card("22.9%", "BOUGHT $1.15M  →  SOLD $1.525M",
              "$321K committed · 3 years · net ~$282K", g / "g2a_card.png")
    data_card("12.9%", "BOUGHT $1.05M  →  SOLD $1.28M",
              "$292K committed · 4 years", g / "g2b_card.png")
    print("  g2a_card, g2b_card")

    # ---- G5 cost chips ----------------------------------------------------
    def chip(text, path, colour=BLUE, fg=WHITE, size=56):
        f = load_font(size, black=False)
        tmp = Image.new("RGBA", (10, 10)); td = ImageDraw.Draw(tmp)
        tw = td.textlength(text, font=f)
        pad_x, pad_y = 46, 26
        cw, ch = int(tw + pad_x * 2), int(size + pad_y * 2)
        im = Image.new("RGBA", (cw, ch), TRANS); d = ImageDraw.Draw(im)
        d.rounded_rectangle([0, 0, cw - 1, ch - 1], 16, fill=colour + (240,))
        d.text((pad_x, pad_y - 6), text, font=f, fill=fg)
        im.save(path)

    for i, txt in enumerate(["$500K–$1M", "25 YEARS", "4 YEARS"], 1):
        chip(txt, g / f"g5_chip{i}.png")
    print("  g5_chip1..3")

    for name, txt in [("g8_entry", "ENTRY PRICE"), ("g8_unit", "THE UNIT"),
                      ("g8_buyer", "FUTURE BUYER"), ("g8_exit", "EXIT PRICE"),
                      ("g8_equity", "EQUITY RELEASED")]:
        chip(txt, g / f"{name}.png")
    print("  g8_* (kinetic list)")

    chip("TELL ME YOUR PROJECT  ›", g / "g9_cta.png", size=58)
    print("  g9_cta")

    # ---- G6 hook headline / G7 punchlines (transparent blocks) ------------
    def headline(parts, path, size=82, block_h=430):
        # Sits over live footage — stroke keeps it readable on any background.
        im = new_trans(block_h); d = ImageDraw.Draw(im)
        f = load_font(size, black=True)
        draw_rich(d, (70, 20), parts, f, size + 22, W - 140,
                  stroke=max(6, size // 12))
        im.save(path)

    headline([("IS THIS YOUR", WHITE), (" 2ND, 3RD OR 4TH", YELLOW),
              (" PROPERTY?", WHITE)], g / "g6_hook.png")
    headline([("ALMOST ANY PROPERTY CAN MAKE", WHITE), (" SOME", YELLOW),
              (" GAIN.", WHITE)], g / "g7_gain.png", size=68, block_h=360)
    headline([("\u201CI MADE MONEY\u201D IS NO LONGER", WHITE), (" ENOUGH.", YELLOW)],
             g / "g7_enough.png", size=72, block_h=360)
    print("  g6_hook, g7_gain, g7_enough")

    # ---- G10 end card -----------------------------------------------------
    im = new_full(); d = ImageDraw.Draw(im)
    box = 190
    d.rounded_rectangle([(W - box) // 2, H // 2 - 190, (W + box) // 2, H // 2 - 190 + box],
                        26, outline=BLUE, width=8)
    f = load_font(96, black=True)
    d.text(((W - d.textlength("R", font=f)) / 2, H // 2 - 158), "R", font=f, fill=BLUE)
    f2 = load_font(40)
    t = "R E I   M E T H O D"
    d.text(((W - d.textlength(t, font=f2)) / 2, H // 2 + 60), t, font=f2,
           fill=(255, 255, 255, 165))
    im.save(g / "g10_endcard.png"); print("  g10_endcard")

    print(f"  → {g}")


# ----------------------------------------------------------------------------
# Captions — karaoke ASS from word timings
# ----------------------------------------------------------------------------

MONEY = re.compile(r"[$%]|\d")

def build_ass(words, path, offset=0.0, max_words=4):
    """Karaoke ASS: white line, active word yellow. Never splits a money token."""
    def cs(t):
        t = max(0, t + offset)
        h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
        return f"{h:d}:{m:02d}:{s:05.2f}"

    cues, cur = [], []
    for w in words:
        cur.append(w)
        long_tok = any(MONEY.search(x["w"]) for x in cur)
        limit = max_words + (1 if long_tok else 0)
        gap = False
        if len(cur) >= limit:
            gap = True
        if gap:
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)

    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Kara,Montserrat,64,&H00FFFFFF,&H0000E8FF,&H00201408,&H96000000,-1,0,0,0,100,100,0,0,1,5,2,2,70,70,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for cue in cues:
        t0, t1 = cue[0]["s"], cue[-1]["e"]
        body = ""
        for w in cue:
            dur = max(4, int(round((w["e"] - w["s"]) * 100)))
            body += "{\\k%d}%s " % (dur, w["w"])
        # anchor at 83% of frame height
        pos = "{\\an2\\pos(%d,%d)}" % (W // 2, int(H * 0.855))
        lines.append(f"Dialogue: 0,{cs(t0)},{cs(t1)},Kara,,0,0,0,,{pos}{body.strip()}")
    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return len(cues)


# ----------------------------------------------------------------------------
# Stage: render
# ----------------------------------------------------------------------------

def overlay_stream(t0, t1, fade_out=True):
    """Turn a still PNG input into a timed, fading overlay stream.

    Two traps here, both silent:

    A PNG decodes to exactly ONE frame at t=0, so fading it directly leaves
    that single frame at alpha 0 - and overlay's default eof_action=repeat
    then holds the transparent frame for the whole beat, compositing every
    graphic completely invisibly. The frame has to be looped first to give
    the fade a real timeline to work against.

    But the loop must be COUNTED, not infinite: overlay ends when all its
    inputs end, so an endless still keeps the graph alive long after the
    footage runs out (a 209s body ran past 302s and climbing). Looping just
    far enough to cover the beat, then shifting the stream to start at t0,
    bounds the graph and keeps the fades on wall-clock time - and means each
    still is only composited over its own beat instead of the whole ad.
    """
    hold = max(0.1, t1 - t0)
    d_in = min(0.22, hold / 3)
    d_out = min(0.20, hold / 3)
    n = int(math.ceil(hold * FPS)) + 4
    chain = (f"loop=loop={n}:size=1,fps={FPS},"
             f"setpts=PTS-STARTPTS+{max(0.0, t0):.3f}/TB,"
             f"fade=t=in:st={max(0.0, t0):.2f}:d={d_in:.2f}:alpha=1")
    if fade_out:
        chain += f",fade=t=out:st={t1 - d_out:.2f}:d={d_out:.2f}:alpha=1"
    return chain


def stage_render():
    print("\n== RENDER ==")
    g = OUT_DIR / "graphics"
    if not (g / "g1_chart.png").exists():
        sys.exit("ERROR: graphics missing — run --stage graphics")
    crop = json.loads((OUT_DIR / "crop.json").read_text(encoding="utf-8"))

    body_words = load_words("body")
    cta_words = load_words("cta")

    body_dur = float(ffprobe(BODY_CLIP, "stream=duration")["streams"][0]["duration"])
    body_clip, body_words = tighten("body", BODY_CLIP, body_words, 0.0, body_dur)
    c_lo, c_hi = cta_variant_range(cta_words, CTA_VARIANT)
    cta_clip, cta_words = tighten("cta", CTA_CLIP, cta_words, c_lo, c_hi)

    beats, misses = resolve_beats(body_words)
    print(f"  beats resolved: {len(beats)}/{len(BEATS)}")
    for bid, ph in misses:
        print(f"  ! MISSED anchor '{ph}' (beat {bid}) - overlay skipped")

    # captions
    n1 = build_ass(body_words, OUT_DIR / "caps_body.ass")
    n2 = build_ass(cta_words, OUT_DIR / "caps_cta.ass")
    print(f"  captions: {n1} body cues, {n2} cta cues")

    grade = ("eq=contrast=1.06:brightness=0.012:saturation=1.07,"
             "unsharp=5:5:0.35:5:5:0.0")

    # ---- pass 1: body ----
    filt = [f"[0:v]{build_geometry_vf(crop)},{grade},fps={FPS}[base]"]
    inputs = ["-i", str(body_clip)]
    idx = 1
    last = "base"
    for b in beats:
        asset = g / b["asset"]
        if not asset.exists():
            print(f"  ! missing asset {asset.name} — skipping {b['id']}")
            continue
        # -framerate matters: loop counts frames at the INPUT rate, and a PNG
        # defaults to 25fps, so a loop sized in 30fps frames came out 20%
        # long and left the CTA holding a frozen frame past its audio.
        inputs += ["-framerate", str(FPS), "-i", str(asset)]
        t0, t1 = b["t0"], b["t1"]
        chain = overlay_stream(t0, t1)
        if b["kind"] == "lower":
            from PIL import Image as _Img
            if _Img.open(asset).height > LOWER_MAX_H:
                chain += f",scale=-2:{LOWER_MAX_H}"
        filt.append(f"[{idx}:v]{chain}[o{idx}]")
        if b["kind"] == "full":
            xy = "0:0"
        elif b["kind"] == "lower":
            xy = f"(W-w)/2:{LOWER_TOP}"
        else:  # upper
            xy = f"(W-w)/2:{int(H * UPPER_Y)}"
        filt.append(f"[{last}][o{idx}]overlay={xy}:"
                    f"enable='between(t,{t0},{t1})'[v{idx}]")
        last = f"v{idx}"
        idx += 1

    ass_body = str(OUT_DIR / "caps_body.ass").replace("\\", "/").replace(":", "\\:")
    fontsdir = str((Path(__file__).parent / "fonts").resolve()).replace("\\", "/").replace(":", "\\:")
    filt.append(f"[{last}]ass='{ass_body}':fontsdir='{fontsdir}'[vout]")

    part_body = OUT_DIR / "_part_body.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", *inputs,
         "-filter_complex", ";".join(filt),
         "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_body)])
    print(f"  body rendered → {part_body.name}")

    # ---- pass 2: cta ----
    cta_chip = g / CTA_CHIP_ASSET
    ass_cta = str(OUT_DIR / "caps_cta.ass").replace("\\", "/").replace(":", "\\:")
    cta_dur = float(ffprobe(cta_clip, "stream=duration")["streams"][0]["duration"])
    cfilt = [f"[0:v]{build_geometry_vf(crop)},{grade},fps={FPS}[base]",
             f"[1:v]{overlay_stream(0.30, cta_dur, fade_out=False)}[chip]",
             f"[base][chip]overlay=(W-w)/2:{LOWER_TOP}[v]",
             f"[v]ass='{ass_cta}':fontsdir='{fontsdir}'[vout]"]
    part_cta = OUT_DIR / "_part_cta.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats",
         "-i", str(cta_clip),
         "-framerate", str(FPS), "-i", str(cta_chip),
         "-filter_complex", ";".join(cfilt),
         "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_cta)])
    print(f"  cta rendered → {part_cta.name}")

    # ---- pass 3: end card ----
    # The still is held with the tpad filter, not "-loop 1". Looping the PNG
    # at the demuxer makes ffmpeg 8.1.2 concatenate the file into itself until
    # the parser overflows ("Failed to reallocate parser buffer to -2147483081")
    # and it eats memory until killed - neither -t nor -frames:v bounds it,
    # because the runaway happens before either applies. Decoding the frame
    # once and cloning it in the filter graph is bounded by construction.
    part_end = OUT_DIR / "_part_end.mp4"
    end_frames = int(round(ENDCARD_SECONDS * FPS))
    run(["ffmpeg", "-y", "-loglevel", "error",
         "-i", str(g / ENDCARD_ASSET),
         "-f", "lavfi", "-i",
         "anullsrc=channel_layout=stereo:sample_rate=48000",
         "-filter_complex",
         f"[0:v]fps={FPS},"
         f"tpad=stop_mode=clone:stop_duration={ENDCARD_SECONDS},"
         f"trim=duration={ENDCARD_SECONDS},setpts=PTS-STARTPTS,"
         f"fade=t=in:st=0:d=0.4,format=yuv420p[v];"
         f"[1:a]atrim=duration={ENDCARD_SECONDS},asetpts=PTS-STARTPTS[a]",
         "-map", "[v]", "-map", "[a]",
         "-frames:v", str(end_frames), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-video_track_timescale", "90000", str(part_end)])

    # ---- join ----
    lst = OUT_DIR / "_concat.txt"
    lst.write_text("".join(f"file '{p.resolve().as_posix()}'\n"
                           for p in (part_body, part_cta, part_end)), encoding="utf-8")
    joined = OUT_DIR / "_joined.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(joined)])

    final = OUT_DIR / OUT_NAME
    run(["ffmpeg", "-y", "-loglevel", "error", "-stats", "-i", str(joined),
         "-af", f"loudnorm=I={LOUDNORM_I}:TP=-1.5:LRA=11",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(final)])

    for q in (part_body, part_cta, part_end):
        d = float(ffprobe(q, "stream=duration")["streams"][0]["duration"])
        print(f"  part {q.stem:12} {d:7.2f}s")
    for q in (joined, lst):
        q.unlink(missing_ok=True)

    dur = float(ffprobe(final, "stream=duration")["streams"][0].get("duration") or 0)
    mb = final.stat().st_size / 1e6
    print(f"\n  ✅ {final}  —  {dur:.1f}s, {mb:.1f} MB")

    (OUT_DIR / "beats_resolved.json").write_text(
        json.dumps(beats, indent=1), encoding="utf-8")


# ----------------------------------------------------------------------------
# Stage: qc
# ----------------------------------------------------------------------------

def stage_qc():
    print("\n== QC ==")
    final = OUT_DIR / OUT_NAME
    if not final.exists():
        sys.exit("ERROR: no render found — run --stage render")
    qc = OUT_DIR / "qc"
    qc.mkdir(exist_ok=True)
    dur = float(ffprobe(final, "stream=duration")["streams"][0].get("duration") or 0)

    # Size the grid to the actual runtime. A fixed 6x5 silently covered only
    # the first 150s, and without -frames:v 1 the muxer refuses the second
    # sheet rather than writing one.
    cols, every = 6, 5.0
    rows = max(1, math.ceil(dur / every / cols))
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(final),
         "-vf", f"fps=1/{every},scale=320:-2,tile={cols}x{rows}",
         "-frames:v", "1", str(qc / "contact_sheet.jpg")])
    print(f"  duration: {dur:.1f}s")
    print(f"  contact sheet: {cols}x{rows} tiles, one every {every:.0f}s")
    print(f"  -> {qc / 'contact_sheet.jpg'}")

    # Full-resolution stills on each beat, where a 320px tile is too small to
    # judge whether a card is clean and its caption legible.
    bp = OUT_DIR / "beats_resolved.json"
    if bp.exists():
        shots = qc / "beats"
        shots.mkdir(exist_ok=True)
        for b in json.loads(bp.read_text(encoding="utf-8")):
            t = (b["t0"] + b["t1"]) / 2
            run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}",
                 "-i", str(final), "-frames:v", "1",
                 str(shots / f"{b['t0']:07.2f}_{b['id']}.png")])
        print(f"  -> {shots} (one full-size still per beat)")
    print("\n  CHECK BY EYE:")
    for line in ("no overlay ever covers the face",
                 "captions legible, inside frame, never clipped",
                 "chips/cards land on the right spoken words",
                 "end card present at the tail",
                 "grade looks natural — skin warm, blacks not lifted",
                 "head size 12–16% of frame height throughout"):
        print(f"    [ ] {line}")


# ----------------------------------------------------------------------------

STAGES = {"probe": stage_probe, "transcribe": stage_transcribe,
          "frame": stage_frame, "graphics": stage_graphics,
          "render": stage_render, "qc": stage_qc}

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", default="all",
                    choices=["all"] + list(STAGES))
    a = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if a.stage == "all":
        for name in ("probe", "transcribe", "frame", "graphics", "render", "qc"):
            STAGES[name]()
    else:
        STAGES[a.stage]()
    print("\nDone.")

if __name__ == "__main__":
    main()
