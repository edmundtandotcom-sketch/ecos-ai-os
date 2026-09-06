"""Audio offset vs the raw take at each stage after the tight cut, +-2.5s search."""
import json, subprocess
import numpy as np
from pathlib import Path

SPEED = 1.15
WK = Path(r"E:\REMOTION\work\webinar_2026-09")
B = WK / "build_115"
C = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar")
SRC = {"hooks": C / "1-Webinar Hooks.mp4", "body": C / "2-Webinar Body.mp4"}
FINAL = C / "05_RENDER" / "out" / "WEBINAR_THOMSON_RESERVE_9x16_115.mp4"
SR = 16000


def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True).stdout.strip())


def audio(f, ss, t, tempo=None):
    af = ["-af", f"atempo={tempo}"] if tempo else []
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.4f}", "-t", f"{t:.4f}", "-i", str(f), *af,
                          "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def best_lag(ref, sig, max_lag, step=4):
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


plan = json.loads((WK / "_tight_s115m.json").read_text())
segdir = WK / "_tight_s115m"
durs = [dur(segdir / f"seg{i:03d}.mp4") for i in range(len(plan))]
bases = np.concatenate([[0.0], np.cumsum(durs)[:-1]])
shots = json.load(open(B / "shots.json"))


def tight_to_final(t):
    for s in shots:
        if s["t0"] - 1e-3 <= t < s["t1"]:
            return s["out0"] + (t - s["t0"])
    return None


stages = [("_cut", B / "_cut.mp4"), ("_body", B / "_body.mp4"), ("final", FINAL)]
print("seg   final_t   " + "   ".join(f"{n:>14}" for n, _ in stages) + "     (audio offset ms, corr)")
for k in (3, 12, 25, 40, 55, 61):
    label, a, b = plan[k]
    if b - a < 1.6:
        continue
    T = a + 0.9
    E = bases[k] + 0.9 / SPEED
    F = tight_to_final(E)
    if F is None:
        continue
    ref_a = audio(SRC[label], T - 0.3, 0.6, tempo=SPEED)
    row = f"{k:3d}  {F:8.2f}  "
    for name, f in stages:
        sig = audio(f, max(0.0, F - 0.3 / SPEED - 2.5), 0.6 / SPEED + 5.0)
        off, c = best_lag(ref_a, sig, int(2.5 * SR))
        row += f"   {off:+7.0f} ({c:.2f})"
    print(row)
