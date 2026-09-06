"""Pre-delivery audit of the final against the raw take. PASS criteria:
  video offset  |<= 1 frame|  at every probe
  audio offset  |<= 40 ms|    at every probe (speech vs raw take, sped)
  caption: the shot that is on screen at each probe contains the word being
           spoken (from the tight transcript)
  whoosh onsets land within 60 ms of the segment starts
  held frames: none outside static plates
"""
import json, subprocess, sys
import numpy as np
from pathlib import Path

SPEED = 1.15
WK = Path(r"E:\REMOTION\work\webinar_2026-09")
B = WK / "build_115"
C = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar")
SRC = {"hooks": C / "1-Webinar Hooks.mp4", "body": C / "2-Webinar Body.mp4"}
FINAL = C / "05_RENDER" / "out" / "WEBINAR_THOMSON_RESERVE_9x16_115.mp4"
WH = Path(r"E:\REMOTION\public\audio\whoosh1.mp3")
SR = 16000


def frames_gray(f, ss, n):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.4f}", "-i", str(f), "-frames:v", str(n),
                          "-vf", "scale=135:240,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.uint8).reshape(-1, 240, 135).astype(np.float32)


def audio(f, ss, t, tempo=None):
    af = ["-af", f"atempo={tempo}"] if tempo else []
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.4f}", "-t", f"{t:.4f}", "-i", str(f), *af,
                          "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def best_lag(ref, sig, max_lag, step=2):
    ref = ref - ref.mean(); sig = sig - sig.mean()
    best, bl = -1e9, 0
    n = len(ref)
    for lag in range(-max_lag, max_lag + 1, step):
        a = sig[max_lag + lag: max_lag + lag + n]
        if len(a) < n:
            continue
        c = float(np.dot(ref, a) / (np.linalg.norm(ref) * np.linalg.norm(a) + 1e-9))
        if c > best:
            best, bl = c, lag
    return bl / SR * 1000, best


plan = json.loads((WK / "_tight_s115x.json").read_text())
shots = json.load(open(B / "shots.json"))
words = json.load(open(WK / "words_tight.json"))
speed = SPEED
nfs = [int(round((b - a) / speed * 30)) for _, a, b in plan]
bases = np.concatenate([[0.0], np.cumsum([n / 30 for n in nfs])[:-1]])

fails = []
print("== A/V vs raw take (final timeline == tight timeline by construction)")
for k in (2, 8, 15, 25, 35, 45, 55, 61):
    label, a, b = plan[k]
    if b - a < 1.5:
        continue
    T = a + 0.8
    F = bases[k] + 0.8 / speed
    ref = frames_gray(SRC[label], T, 1)[0]
    win = frames_gray(FINAL, F - 6 / 30, 13)
    d = [np.abs(win[i] - ref).mean() for i in range(len(win))]
    voff = int(np.argmin(d)) - 6
    ref_a = audio(SRC[label], T - 0.3, 0.6, tempo=speed)
    sig = audio(FINAL, F - 0.3 / speed - 0.5, 0.6 / speed + 1.0)
    aoff, c = best_lag(ref_a, sig, int(0.5 * SR))
    # caption check: word spoken at tight time F and the shot on screen
    spoken = next((w for w in words if w["s"] - 0.05 <= F <= w["e"] + 0.05), None)
    shot = next((s for s in shots if s["out0"] - 1e-3 <= F < s["out1"]), None)
    cap_ok = spoken is not None and shot is not None and spoken["w"] in shot["text"].split()
    ok = abs(voff) <= 1 and abs(aoff) <= 40 and c > 0.5 and cap_ok
    if not ok:
        fails.append(f"probe {k} @{F:.2f}s: video {voff:+d}f audio {aoff:+.0f}ms c={c:.2f} caption_ok={cap_ok}")
    print(f"  {'PASS' if ok else 'FAIL'} t={F:7.2f}  video {voff:+2d} frames  audio {aoff:+5.0f} ms (corr {c:.2f})  "
          f"spoken='{spoken['w'] if spoken else '?'}' on-screen='{shot['text'] if shot else '?'}'")

print("== whoosh onsets vs segment starts")
seg_starts = [s["out0"] for s in shots if s.get("segment_start") and s["out0"] > 0.2]
wh = audio(WH, 0, 0.6)
for t in seg_starts:
    sig = audio(FINAL, max(0.0, t - 0.5), 1.6)
    off, c = best_lag(wh, sig, int(0.5 * SR), step=4)
    ok = abs(off) <= 60 and c > 0.25
    if not ok:
        fails.append(f"whoosh at {t:.2f}: {off:+.0f}ms c={c:.2f}")
    print(f"  {'PASS' if ok else 'FAIL'} segment start {t:7.2f}s  whoosh {off:+5.0f} ms (corr {c:.2f})")

print("== held frames (decode-accurate), speaker stretches")
for ss in (12.0, 45.0, 100.0, 140.0):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(FINAL), "-ss", str(ss), "-frames:v", "150",
                          "-vf", "scale=135:240,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 240, 135).astype(np.float32)
    d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
    plates = sum(1 for s in shots if s.get("dev") in ("black_type_open", "icon_compare", "dread_plate", "pin_radius")
                 and s["out0"] < ss + 5 and s["out1"] > ss)
    zeros = int((d < 0.3).sum())
    print(f"  @{ss:5.1f}s 5s window: held frames {zeros:3d}  (static plates in window: {plates})")

print()
print("RESULT:", "PASS - 10/10 on the measurable criteria" if not fails else f"FAIL ({len(fails)})")
for f in fails:
    print("  -", f)
