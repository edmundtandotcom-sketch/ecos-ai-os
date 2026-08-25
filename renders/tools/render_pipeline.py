#!/usr/bin/env python3
"""NL01 "Can It Beat the S&P 500?" — 9:16 render pipeline.

Runs the mechanical work of renders/RENDER_TASK.md end to end:
  fetch -> probe -> transcribe -> frame -> captions -> overlays -> encode -> qc

Every stage is resumable: re-running skips work whose output already exists,
so a failed encode does not force a re-transcribe. Stages can also be run
individually:

    python3 render_pipeline.py all            # everything
    python3 render_pipeline.py transcribe     # one stage
    python3 render_pipeline.py frame --head 14

Visual judgement stays with a human (or a Claude session): the `frame` stage
writes test frames and a measurement report to review, and `qc` writes contact
sheets of the finished render. Nothing is auto-approved.
"""
import argparse
import json
import math
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]      # renders/
WORK = ROOT / "work"
SRC = ROOT / "source"
GFX = WORK / "graphics"
OUT = ROOT / "SP_BENCHMARK_9x16_v1.mp4"

W, H = 1080, 1920
BODY_ID = "1fnOeVI0owMziztOtPjZVoeAjPyeZvJnn"
CTA_ID = "1JClBrWVGxtNgtF8gWeOUnUshM8R4c6ld"
BODY_BYTES = 87590396
CTA_BYTES = 18591045

GRADE = ("eq=contrast=1.05:brightness=0.01:saturation=1.06,"
         "colorbalance=rm=0.02:bm=-0.01,unsharp=5:5:0.4")


def run(cmd, **kw):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    return subprocess.run([str(c) for c in cmd], check=True, **kw)


def probe(path, entries):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         entries, "-of", "json", str(path)],
        check=True, capture_output=True, text=True).stdout
    return json.loads(out)


# ---------------------------------------------------------------- fetch ----

def stage_fetch(args):
    SRC.mkdir(parents=True, exist_ok=True)
    for fid, name, want in ((BODY_ID, "body.mp4", BODY_BYTES),
                            (CTA_ID, "cta.mp4", CTA_BYTES)):
        dest = SRC / name
        if dest.exists() and dest.stat().st_size == want:
            print(f"{name}: already present ({want} bytes)")
            continue
        ok = False
        try:
            run(["gdown", fid, "-O", str(dest)])
            ok = dest.exists() and dest.stat().st_size == want
        except subprocess.CalledProcessError:
            ok = False
        if not ok:
            print(f"{name}: gdown failed/short, trying direct download")
            run(["curl", "-fL",
                 f"https://drive.usercontent.google.com/download?id={fid}"
                 "&export=download&confirm=t", "-o", str(dest)])
        got = dest.stat().st_size
        if got != want:
            sys.exit(f"FATAL: {name} is {got} bytes, expected {want}. "
                     "Download was truncated or intercepted — do not render this.")
        print(f"{name}: OK ({got} bytes)")


def stage_probe(args):
    report = {}
    for name in ("body.mp4", "cta.mp4"):
        p = SRC / name
        info = probe(p, "stream=width,height,r_frame_rate,duration:format=duration")
        st = info["streams"][0]
        num, den = (int(x) for x in st["r_frame_rate"].split("/"))
        dur = float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(p)],
            check=True, capture_output=True, text=True).stdout.strip())
        report[name] = {"width": st["width"], "height": st["height"],
                        "fps": round(num / den, 3), "duration_s": round(dur, 3),
                        "bytes": p.stat().st_size}
        print(name, report[name])
    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / "probe.json").write_text(json.dumps(report, indent=2))


# ------------------------------------------------------------ transcribe ----

def stage_transcribe(args):
    WORK.mkdir(parents=True, exist_ok=True)
    from faster_whisper import WhisperModel
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    for name in ("body", "cta"):
        dest = WORK / f"{name}_words.json"
        if dest.exists() and not args.force:
            print(f"{name}: transcript exists, skipping")
            continue
        wav = WORK / f"{name}.wav"
        if not wav.exists():
            run(["ffmpeg", "-v", "error", "-y", "-i", SRC / f"{name}.mp4",
                 "-vn", "-ac", "1", "-ar", "16000", wav])
        segments, _ = model.transcribe(str(wav), word_timestamps=True,
                                       vad_filter=False)
        words = []
        for seg in segments:
            for w in (seg.words or []):
                words.append({"w": w.word.strip(), "s": round(w.start, 3),
                              "e": round(w.end, 3)})
            print(f"  [{seg.start:7.2f}] {seg.text.strip()[:90]}", flush=True)
        dest.write_text(json.dumps(words, indent=1))
        (WORK / f"{name}_text.txt").write_text(" ".join(x["w"] for x in words))
        print(f"{name}: {len(words)} words -> {dest}")


def load_words(name):
    return json.loads((WORK / f"{name}_words.json").read_text())


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def token_index(words):
    """Flatten words into a normalised token stream.

    One spoken word can normalise to several tokens ("that's" -> that, s;
    "S&P" -> s, p), so matching token-per-word silently fails on exactly the
    phrases this script is full of. Returns (tokens, owner) where owner[i] is
    the index of the word token i came from.
    """
    toks, owner = [], []
    for wi, w in enumerate(words):
        for t in norm(w["w"]).split():
            toks.append(t)
            owner.append(wi)
    return toks, owner


def find_phrase(words, phrase, start_after=0.0, occurrence=1, _idx=None):
    """Locate a spoken phrase; returns (start_s, end_s) or None.

    `phrase` may be a list of alternatives — the first that matches wins, so a
    beat can survive the transcriber writing "$500K" where the script says
    "five hundred K". Matching is on normalised tokens, so punctuation and
    casing in the expected script never block a match against what was said.
    """
    if isinstance(phrase, (list, tuple)):
        for alt in phrase:
            hit = find_phrase(words, alt, start_after, occurrence, _idx)
            if hit:
                return hit
        return None

    want = norm(phrase).split()
    if not want:
        return None
    toks, owner = _idx if _idx else token_index(words)
    hits = 0
    n = len(want)
    for i in range(len(toks) - n + 1):
        if words[owner[i]]["s"] < start_after:
            continue
        if toks[i:i + n] == want:
            hits += 1
            if hits == occurrence:
                return words[owner[i]]["s"], words[owner[i + n - 1]]["e"]
    return None


# --------------------------------------------------------------- framing ----

def stage_frame(args):
    """Derive a 9:16 crop/scale that keeps the speaker's head within spec.

    Head crown-to-chin must land at 12-16% of output height (target `--head`),
    eye-line 38-42% from top. A face detector supplies the measurement; the
    result is written as a report plus test frames for a human to confirm.
    """
    import cv2
    import numpy as np

    WORK.mkdir(parents=True, exist_ok=True)
    cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    measurements = []
    for t in (1, 5, 15):
        frame = WORK / f"probe_{t}s.png"
        run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", SRC / "body.mp4",
             "-frames:v", "1", frame])
        img = cv2.imread(str(frame))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.1, 6, minSize=(80, 80))
        if len(faces) == 0:
            print(f"t={t}s: no face detected")
            continue
        x, y, fw, fh = max(faces, key=lambda f: f[2] * f[3])
        # Haar box spans ~brow-to-chin; crown-to-chin is ~1.35x that height,
        # and the crown sits ~0.28*fh above the box top.
        head_h = fh * 1.35
        crown_y = y - 0.28 * fh
        eye_y = y + 0.38 * fh
        measurements.append(dict(t=t, src_h=img.shape[0], src_w=img.shape[1],
                                 face=[int(x), int(y), int(fw), int(fh)],
                                 head_h=head_h, crown_y=crown_y, eye_y=eye_y,
                                 cx=x + fw / 2))
        print(f"t={t}s face={x},{y},{fw},{fh} head_h={head_h:.0f}px")

    if not measurements:
        sys.exit("No face detected in any probe frame — set the crop by hand "
                 "and record the numbers in QC_REPORT.md.")

    m = sorted(measurements, key=lambda d: d["head_h"])[len(measurements) // 2]
    target_head = H * args.head / 100.0
    scale = target_head / m["head_h"]           # <1 shrinks an oversized head
    sw, sh = m["src_w"] * scale, m["src_h"] * scale
    # Place the speaker so the eye-line lands at 40% of output height.
    off_x = W / 2 - m["cx"] * scale
    off_y = H * 0.40 - m["eye_y"] * scale
    off_x, off_y = round(off_x), round(off_y)

    plan = dict(scale=round(scale, 5), scaled_w=round(sw), scaled_h=round(sh),
                offset_x=off_x, offset_y=off_y,
                head_pct=round(target_head / H * 100, 2),
                eyeline_pct=40.0,
                headroom_pct=round((off_y + m["crown_y"] * scale) / H * 100, 2),
                measured_from=m, note="")
    if sw < W or sh < H:
        plan["note"] = "scaled source is smaller than canvas — blurred fill in use"
    (WORK / "framing.json").write_text(json.dumps(plan, indent=2))
    print(json.dumps(plan, indent=2))

    run(["ffmpeg", "-v", "error", "-y", "-ss", 5, "-i", SRC / "body.mp4",
         "-frames:v", "1", "-vf", canvas_filter(plan),
         WORK / "framing_after.png"])
    shutil.copy(WORK / "probe_5s.png", WORK / "framing_before.png")
    print("Review renders/work/framing_before.png vs framing_after.png — "
          f"head should read as {plan['head_pct']}% of frame height.")


def canvas_filter(plan):
    """Speaker scaled onto a 9:16 canvas over a blurred fill of itself."""
    return (
        f"split=2[bg][fg];"
        f"[bg]scale={W}:{H}:force_original_aspect_ratio=increase,"
        f"crop={W}:{H},boxblur=42:2,eq=brightness=-0.06[bgb];"
        f"[fg]scale={plan['scaled_w']}:{plan['scaled_h']}[fgs];"
        f"[bgb][fgs]overlay={plan['offset_x']}:{plan['offset_y']}"
    )


# -------------------------------------------------------------- captions ----

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: {w}
PlayResY: {h}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Low,{font},64,&H0000E8FF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,5,0,2,{ml},{mr},{mvlow},1
Style: High,{font},64,&H0000E8FF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,5,0,2,{ml},{mr},{mvhigh},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

MONEY = re.compile(r"[\$%]|\d")


def ts(t):
    t = max(t, 0)
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def group_cues(words, max_words=4, max_gap=0.7):
    """Group words into <=4-word cues, never splitting a money/number token
    away from the word it belongs to, and breaking on long pauses."""
    cues, cur = [], []
    for i, w in enumerate(words):
        if cur:
            gap = w["s"] - cur[-1]["e"]
            joined = MONEY.search(w["w"]) and MONEY.search(cur[-1]["w"])
            if (len(cur) >= max_words and not joined) or gap > max_gap:
                cues.append(cur)
                cur = []
        cur.append(w)
    if cur:
        cues.append(cur)
    return cues


def build_ass(words, high_windows, path, font="Montserrat"):
    """Karaoke ASS. Cues overlapping a bottom-third card use the raised style."""
    lines = [ASS_HEAD.format(w=W, h=H, font=font,
                             ml=int(W * 0.06), mr=int(W * 0.06),
                             mvlow=int(H * 0.17),    # baseline ~83% height
                             mvhigh=int(H * 0.38))]  # raised ~62% height
    cues = group_cues(words)
    for n, cue in enumerate(cues):
        start, end = cue[0]["s"], cue[-1]["e"] + 0.08
        if n + 1 < len(cues):
            # Two dialogues live at once would stack two caption lines.
            end = min(end, cues[n + 1][0]["s"] - 0.01)
        if end <= start:
            continue
        raised = any(a < end and start < b for a, b in high_windows)
        text = ""
        for w in cue:
            cs = int(round((w["e"] - w["s"]) * 100))
            text += "{\\k%d}%s " % (max(cs, 1), w["w"])
        lines.append(f"Dialogue: 0,{ts(start)},{ts(end)},"
                     f"{'High' if raised else 'Low'},,0,0,0,,{text.strip()}")
    path.write_text("\n".join(lines) + "\n")
    return path


# -------------------------------------------------------------- assemble ----

# (graphic, phrase to anchor on, occurrence, lead-in, hold-after, placement)
# Placement: "full" = full-frame cutaway, "card" = bottom third, "top" = upper
# third, "chipN" = stacked cost chips, "cta" = persistent CTA chip.
# Each phrase is a list of alternatives tried in order, because the
# transcriber may write money and numbers several ways ("$500K", "500K",
# "five hundred K"). Anchors avoid digits where a plain-word anchor exists.
BODY_BEATS = [
    ("G6_hook", ["is this your second"], 1, -0.2, 0.0, "top",
     ["here's the question", "here s the question"]),
    ("G5_chip_capital", ["you commit", "of your own cash"], 1, 0.0, 0.0,
     "chip1", None),
    ("G5_chip_mortgage", ["year mortgage", "you take a 25"], 1, 0.0, 0.0,
     "chip2", None),
    ("G5_chip_wait", ["and you wait four", "you wait four", "wait 4 years"],
     1, 0.0, 0.0, "chip3", None),
    ("G1_chart", ["that same money could be invested", "that same money"],
     1, 0.0, 0.0, "full",
     ["beating the s p 500", "beating the s p five hundred", "beating the"]),
    ("G7a_punch", ["an easy test to pass", "easy test to pass"],
     1, -1.2, 0.6, "card", None),
    ("G3_question", ["can this project beat"], 1, -0.1, 0.4, "full", None),
    ("G2a_card", ["one of my new launches was bought",
                  "new launches was bought"], 1, 0.0, 0.8, "card",
     ["on the capital committed", "a year on the capital"]),
    ("G2b_card", ["another property", "bought at 1 05"], 1, 0.0, 0.8, "card",
     ["roughly 12 9", "roughly twelve point nine", "12 9 percent a year"]),
    ("G8_entry", ["at the entry price", "the entry price"], 1, 0.0, 2.5,
     "kin1", None),
    ("G8_unit", ["the unit you choose"], 1, 0.0, 2.0, "kin2", None),
    ("G8_buyer", ["your future buyer"], 1, 0.0, 1.5, "kin3", None),
    ("G8_exit", ["your exit price"], 1, 0.0, 1.0, "kin4", None),
    ("G8_equity", ["usable equity"], 1, 0.0, 0.8, "kin5", None),
    ("G4_framework", ["that's exactly how we use",
                      "how we use the new launch ladder"], 1, 0.0, 0.0, "full",
     ["before you commit to this one", "next three moves"]),
    ("G7b_punch", ["is no longer good enough", "no longer good enough"],
     1, -1.0, 0.8, "card", None),
]

# Cards occupy the 55-72% band; captions stay anchored at 83% throughout.
# (RENDER_TASK.md offers either this or shifting captions up under a card —
# this is the option chosen, so the two never share vertical space.)
PLACEMENT_XY = {
    "top":   ("(W-w)/2", "H*0.10"),
    "card":  ("(W-w)/2", "H*0.55"),
    "chip1": ("(W-w)/2", "H*0.55"),
    "chip2": ("(W-w)/2", "H*0.55+140"),
    "chip3": ("(W-w)/2", "H*0.55+280"),
    "kin1":  ("(W-w)/2", "H*0.54"),
    "kin2":  ("(W-w)/2", "H*0.54+125"),
    "kin3":  ("(W-w)/2", "H*0.54+250"),
    "kin4":  ("(W-w)/2", "H*0.54+375"),
    "kin5":  ("(W-w)/2", "H*0.54+500"),
    "cta":   ("(W-w)/2", "H*0.62"),
    "full":  ("0", "0"),
}


def resolve_beats(words, beats, offset=0.0):
    """Turn script phrases into real timestamps from the transcript.

    Beats are listed in script order and resolved with a moving cursor, so a
    phrase that recurs (e.g. "your future buyer", said once in the opening and
    again in the kinetic list) binds to the right occurrence instead of the
    first one in the file. Beats sharing a screen band are then de-overlapped
    so two cards never stack on top of each other.
    """
    idx = token_index(words)
    resolved, missed = [], []
    cursor = 0.0
    for name, phrase, occ, lead, hold, place, until in beats:
        hit = find_phrase(words, phrase, start_after=cursor, occurrence=occ,
                          _idx=idx)
        if not hit:
            missed.append((name, phrase))
            continue
        cursor = hit[0] + 0.01
        start = hit[0] + lead
        if until:
            end_hit = find_phrase(words, until, start_after=hit[1], _idx=idx)
            end = (end_hit[1] if end_hit else hit[1] + 3.0) + hold
        else:
            end = hit[1] + hold + (2.5 if place == "full" else 1.2)
        resolved.append(dict(graphic=name, start=round(start + offset, 3),
                             end=round(end + offset, 3), place=place,
                             phrase=phrase, matched=True))

    bands = {}
    for b in sorted(resolved, key=lambda d: d["start"]):
        prev = bands.get(b["place"])
        if prev and b["start"] < prev["end"]:
            prev["end"] = round(max(b["start"] - 0.15, prev["start"] + 0.5), 3)
        bands[b["place"]] = b

    # A full-frame cutaway hides everything under it; retire overlays before
    # it opens rather than leaving them stranded behind the card.
    for full in [b for b in resolved if b["place"] == "full"]:
        for b in resolved:
            if b["place"] == "full" or b["end"] <= full["start"]:
                continue
            if b["start"] < full["start"] < b["end"]:
                b["end"] = round(max(full["start"] - 0.1, b["start"] + 0.4), 3)
    return resolved, missed


def stage_assemble(args):
    plan = json.loads((WORK / "framing.json").read_text())
    bwords, cwords = load_words("body"), load_words("cta")

    # Trim to speech: start a touch before the first word, end after the last.
    b_in = max(bwords[0]["s"] - 0.35, 0.0)
    b_out = bwords[-1]["e"] + 0.45
    c_in = max(cwords[0]["s"] - 0.35, 0.0)
    c_out = cwords[-1]["e"] + 0.55
    body_len = b_out - b_in
    cta_len = c_out - c_in

    bw = [dict(w, s=w["s"] - b_in, e=w["e"] - b_in) for w in bwords]
    cw = [dict(w, s=w["s"] - c_in + body_len, e=w["e"] - c_in + body_len)
          for w in cwords]

    beats, missed = resolve_beats(bw, BODY_BEATS)
    cta_hit = (body_len, body_len + cta_len)
    beats.append(dict(graphic="G9_cta", start=round(cta_hit[0] + 0.3, 3),
                      end=round(cta_hit[1], 3), place="cta",
                      phrase="(whole CTA clip)", matched=True))
    (WORK / "beats.json").write_text(json.dumps(
        dict(body_in=b_in, body_out=b_out, cta_in=c_in, cta_out=c_out,
             body_len=round(body_len, 3), cta_len=round(cta_len, 3),
             beats=beats, unmatched=missed), indent=2))
    if missed:
        print("WARNING — phrases not found in transcript (overlay skipped):")
        for n, p in missed:
            print(f"  {n}: {p!r}")

    # Cards live in the 55-72% band, so captions hold at 83% throughout and
    # the raised style stays unused. Pass windows here to switch strategies.
    ass = build_ass(bw + cw, [], WORK / "captions.ass", font=args.font)

    # --- speaker track: trim, grade, frame, concat body+CTA --------------
    seg_paths = []
    for name, (tin, tout) in (("body", (b_in, b_out)), ("cta", (c_in, c_out))):
        seg = WORK / f"{name}_framed.mp4"
        if not seg.exists() or args.force:
            run(["ffmpeg", "-v", "error", "-stats", "-y", "-ss", f"{tin:.3f}",
                 "-to", f"{tout:.3f}", "-i", SRC / f"{name}.mp4",
                 "-vf", f"{GRADE},{canvas_filter(plan)},fps=30,format=yuv420p",
                 "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                 "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", seg])
        seg_paths.append(seg)

    concat = WORK / "concat.txt"
    concat.write_text("".join(f"file '{p}'\n" for p in seg_paths))
    joined = WORK / "joined.mp4"
    run(["ffmpeg", "-v", "error", "-stats", "-y", "-f", "concat", "-safe", "0",
         "-i", concat, "-c", "copy", joined])

    # --- overlays + burned-in captions ----------------------------------
    inputs = ["-i", str(joined)]
    chain, last = [], "[0:v]"
    for i, b in enumerate(beats, start=1):
        png = GFX / f"{b['graphic']}.png"
        if not png.exists():
            print(f"skip {b['graphic']}: {png} missing")
            continue
        inputs += ["-i", str(png)]
        x, y = PLACEMENT_XY[b["place"]]
        fade = (f"format=rgba,fade=t=in:st={b['start']:.2f}:d=0.25:alpha=1,"
                f"fade=t=out:st={max(b['end'] - 0.25, b['start']):.2f}:d=0.25:alpha=1")
        chain.append(f"[{i}:v]{fade}[g{i}]")
        chain.append(
            f"{last}[g{i}]overlay={x}:{y}:"
            f"enable='between(t,{b['start']:.2f},{b['end']:.2f})'[v{i}]")
        last = f"[v{i}]"

    ass_path = str(ass).replace("\\", "/").replace(":", r"\:")
    chain.append(f"{last}subtitles='{ass_path}'[vout]")
    overlaid = WORK / "overlaid.mp4"
    run(["ffmpeg", "-v", "error", "-stats", "-y", *inputs,
         "-filter_complex", ";".join(chain), "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-c:a", "copy", overlaid])

    # --- 3.0s end card, then loudness normalise -------------------------
    endcard = WORK / "endcard.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", "3.0",
         "-i", GFX / "G10_endcard.png", "-f", "lavfi", "-t", "3.0",
         "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
         "-vf", f"scale={W}:{H},fps=30,format=yuv420p,"
                "fade=t=in:st=0:d=0.4,fade=t=out:st=2.6:d=0.4",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-c:a", "aac", "-b:a", "192k", "-shortest", endcard])

    final_list = WORK / "final_concat.txt"
    final_list.write_text(f"file '{overlaid}'\nfile '{endcard}'\n")
    run(["ffmpeg", "-v", "error", "-stats", "-y", "-f", "concat", "-safe", "0",
         "-i", final_list, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", WORK / "prefinal.mp4"])

    crf = args.crf
    while True:
        run(["ffmpeg", "-v", "error", "-stats", "-y", "-i", WORK / "prefinal.mp4",
             "-c:v", "libx264", "-preset", "slow", "-crf", crf,
             "-pix_fmt", "yuv420p", "-movflags", "+faststart",
             "-c:a", "aac", "-b:a", "160k", OUT])
        mb = OUT.stat().st_size / 1e6
        print(f"encoded {OUT.name}: {mb:.1f} MB at CRF {crf}")
        if mb <= 90 or crf >= 26:
            break
        crf += 3
        print("over 90 MB — re-encoding at higher CRF")

    dur = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(OUT)], check=True, capture_output=True,
        text=True).stdout.strip())
    expected = body_len + cta_len + 3.0
    print(f"duration {dur:.2f}s (expected {expected:.2f}s)")


# -------------------------------------------------------------------- qc ----

def stage_qc(args):
    qc = WORK / "qc"
    if qc.exists():
        shutil.rmtree(qc)
    qc.mkdir(parents=True)
    run(["ffmpeg", "-v", "error", "-i", OUT, "-vf", "fps=1/5,scale=540:-1",
         qc / "f_%04d.png"])
    frames = sorted(qc.glob("f_*.png"))
    print(f"{len(frames)} sample frames (one every 5s)")
    for old in ROOT.glob("contact_sheet_*.jpg"):
        old.unlink()
    run(["ffmpeg", "-v", "error", "-y", "-i", qc / "f_%04d.png",
         "-vf", "tile=4x3:margin=10:padding=10:color=#202020",
         "-q:v", "3", ROOT / "contact_sheet_%02d.jpg"])
    for sheet in sorted(ROOT.glob("contact_sheet_*.jpg")):
        print("wrote", sheet)
    print("Now LOOK at every contact sheet before pushing: overlays clear of "
          "the face, captions unclipped, cards legible, end card present.")


STAGES = {"fetch": stage_fetch, "probe": stage_probe,
          "transcribe": stage_transcribe, "frame": stage_frame,
          "assemble": stage_assemble, "qc": stage_qc}


def stage_graphics(args):
    GFX.mkdir(parents=True, exist_ok=True)
    run([sys.executable, ROOT / "tools" / "graphics.py", GFX])


STAGES["graphics"] = stage_graphics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=list(STAGES) + ["all"])
    ap.add_argument("--model", default="base")
    ap.add_argument("--head", type=float, default=14.0,
                    help="target head height as %% of output height (12-16)")
    ap.add_argument("--crf", type=int, default=21)
    ap.add_argument("--font", default="Montserrat")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    order = ["fetch", "probe", "transcribe", "frame", "graphics", "assemble", "qc"]
    for name in (order if args.stage == "all" else [args.stage]):
        print(f"\n===== {name} =====", flush=True)
        STAGES[name](args)


if __name__ == "__main__":
    main()
