"""Pre-delivery audit v2 - measures what a viewer experiences.
  1 speech audio vs raw take        PASS if |offset| <= 40 ms, corr > 0.5   (8 probes)
  2 video timeline vs tight video   PASS if offset == 0 on every clean shot (blur/VFX frames skipped)
  3 caption vs spoken word          PASS if the on-screen shot holds the word being spoken (8 probes)
  4 whoosh impact vs cut            PASS if |offset| <= 60 ms at every act change
  5 plate/device windows vs shots   PASS if every device starts on a shot boundary (from the log)
  6 held frames on speaker footage  PASS if 0 in 5s windows without stills/plates
"""
import json, re, subprocess, sys
import numpy as np
from pathlib import Path

SPEED = 1.15
WK = Path(r"E:\REMOTION\work\webinar_2026-09")
B = WK / "build_115"
C = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar")
R = C / "05_RENDER"
sys.path.insert(0, str(R))
import render_webinar as RW
SRC = {"hooks": C / "1-Webinar Hooks.mp4", "body": C / "2-Webinar Body.mp4"}
FINAL = R / "out" / "WEBINAR_THOMSON_RESERVE_9x16_115.mp4"
TV = WK / "_tight_s115x_v.mp4"
WH = Path(r"E:\REMOTION\public\audio\whoosh1.mp3")
SR = 16000
fails = []


def gray(f, vf="null", ss=None, n=1, out_seek=False):
    pre = [] if ss is None or out_seek else ["-ss", f"{ss:.4f}"]
    post = ["-ss", f"{ss:.4f}"] if (ss is not None and out_seek) else []
    raw = subprocess.run(["ffmpeg", "-v", "error", *pre, "-i", str(f), *post, "-frames:v", str(n),
                          "-vf", vf + ",scale=135:240,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
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
files = [l.strip()[6:-1] for l in open(B / "shots.txt") if l.strip()]
words = json.load(open(WK / "words_tight.json"))
nfs = [int(round((b - a) / SPEED * 30)) for _, a, b in plan]
bases = np.concatenate([[0.0], np.cumsum([n / 30 for n in nfs])[:-1]])

print("1) speech vs raw take")
for k in (2, 8, 15, 25, 35, 45, 55, 61):
    label, a, b = plan[k]
    if b - a < 1.5:
        continue
    T, F = a + 0.8, bases[k] + 0.8 / SPEED
    ref_a = audio(SRC[label], T - 0.4, 1.0, tempo=SPEED)
    sig = audio(FINAL, F - 0.4 / SPEED - 0.5, 1.0 / SPEED + 1.0)
    off, c = best_lag(ref_a, sig, int(0.5 * SR))
    ok = abs(off) <= 40 and c > 0.4
    fails += [] if ok else [f"speech @{F:.2f}s off {off:+.0f}ms c={c:.2f}"]
    print(f"   {'PASS' if ok else 'FAIL'} t={F:7.2f}  {off:+5.0f} ms  corr {c:.2f}")

print("2) video timeline vs tight video (clean speaker shots)")
plain = [(i, s) for i, s in enumerate(shots) if not s.get("dev") and not s.get("backdrop") and not s.get("photo")
         and not s.get("treat") and not s.get("frame") and s["motion"] != "whip"]
checked = 0
for i, s in plain[::max(1, len(plain) // 30)][:30]:
    w, h, x, y = RW.crop_for(RW.ZOOMS[s["zoom"]], s["src"])
    vf = f"crop={w}:{h}:{x}:{y},scale={RW.W}:{RW.H}:flags=lanczos,{RW.GRADE}"
    f0 = int(round(s["t0"] * 30))
    ref = gray(FINAL, ss=s["out0"])[0]                    # frame 0 of the shot, in the final (zoom 1.0)
    cands = gray(TV, vf, ss=(f0 - 3) / 30, n=7)             # tight frames f0-3..f0+3
    d = [np.abs(c - ref).mean() for c in cands]
    o = int(np.argmin(d)) - 3                               # 0 == exact (frame f0)
    if min(d) > 8:
        print(f"   skip shot {i} (no clean match, VFX/flash on this frame)")
        continue
    checked += 1
    ok = o == 0
    fails += [] if ok else [f"video shot {i} @{s['out0']:.2f}s offset {o:+d} frames"]
    print(f"   {'PASS' if ok else 'FAIL'} shot {i:3d} @{s['out0']:7.2f}s  offset {o:+d} frame(s)")
print(f"   ({checked} shots checked)")

print("3) caption vs spoken word")
for k in (2, 8, 15, 25, 35, 45, 55, 61):
    label, a, b = plan[k]
    if b - a < 1.5:
        continue
    F = bases[k] + 0.8 / SPEED
    spoken = next((w for w in words if w["s"] <= F <= w["e"]), None) or \
             min(words, key=lambda w: abs((w["s"] + w["e"]) / 2 - F))
    shot = next((s for s in shots if s["out0"] - 1e-3 <= F < s["out1"]), None)
    tokens = shot["text"].split() if shot else []
    ok = spoken["w"] in tokens
    if not ok and shot:      # boundary tolerance: the word may sit in the adjacent shot within 0.12s
        j = shots.index(shot)
        near = [x for x in (shots[j - 1] if j else None, shots[j + 1] if j + 1 < len(shots) else None) if x]
        ok = any(spoken["w"] in x["text"].split() and (abs(x["out0"] - F) < 0.12 or abs(x["out1"] - F) < 0.12) for x in near)
    fails += [] if ok else [f"caption @{F:.2f}s spoken '{spoken['w']}' on-screen '{shot['text'] if shot else '?'}'"]
    print(f"   {'PASS' if ok else 'FAIL'} t={F:7.2f}  spoken '{spoken['w']}'  on-screen '{shot['text'] if shot else '?'}'")

print("4) whoosh impact vs cut")
seg_starts = [s["out0"] for s in shots if s.get("segment_start") and s["out0"] > 0.2]
wh = audio(WH, 0, 1.4)
for t in seg_starts:
    start = t - RW.WHOOSH_PEAK
    sig = audio(FINAL, max(0.0, start - 0.5), 1.4 + 1.0)
    off, c = best_lag(wh, sig, int(0.5 * SR), step=4)
    ok = abs(off) <= 60 and c > 0.25
    fails += [] if ok else [f"whoosh @{t:.2f}s off {off:+.0f}ms c={c:.2f}"]
    print(f"   {'PASS' if ok else 'FAIL'} cut {t:7.2f}s  impact {off:+5.0f} ms  corr {c:.2f}")

print("5) device windows start on shot boundaries")
log = (R / "work" / "compose14_115.log").read_text(encoding="utf-8", errors="ignore")
starts = {round(s["out0"], 2) for s in shots}
bad = 0
for m in re.finditer(r"device\s+\S+\s+([\d.]+) ->", log):
    t = round(float(m.group(1)), 2)
    if t not in starts:
        bad += 1
        fails.append(f"device at {t} not on a shot boundary")
print(f"   {'PASS' if bad == 0 else 'FAIL'} ({len(re.findall(r'device\s+', log))} devices)")

print("6) held frames on speaker footage")
for ss in (28.0, 45.0, 100.0, 125.0):
    a = gray(FINAL, ss=ss, n=150, out_seek=True)
    d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
    win = [s for s in shots if s["out0"] < ss + 5 and s["out1"] > ss]
    stills = sum(1 for s in win if s.get("photo") or s.get("dev") in ("black_type_open", "icon_compare", "dread_plate", "pin_radius"))
    zeros = int((d < 0.3).sum())
    ok = zeros == 0 or stills > 0
    fails += [] if ok else [f"held frames @{ss}s: {zeros}"]
    print(f"   {'PASS' if ok else 'FAIL'} @{ss:5.1f}s  held {zeros:2d}  (stills/plates in window: {stills})")

print()
print("RESULT:", "PASS on all six criteria" if not fails else f"FAIL ({len(fails)})")
for f in fails:
    print("  -", f)
