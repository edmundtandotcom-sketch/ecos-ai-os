"""A/V sync audit against the raw take.

For a few segments k: pick source time T = a_k + 0.9s. Expected tight time
E = base_k + 0.9/speed. Video offset = which tight frame around E best
matches the source frame at T (image diff). Audio offset = cross-correlation
of the source audio window (sped by atempo) against the tight audio around
E. Then the same for the final using shots.json to map tight -> final.
"""
import json, subprocess
import numpy as np
from pathlib import Path

SPEED = 1.15
WK = Path(r"E:\REMOTION\work\webinar_2026-09")
C = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar")
SRC = {"hooks": C / "1-Webinar Hooks.mp4", "body": C / "2-Webinar Body.mp4"}
TIGHT = WK / "_tight_s115m.mp4"
FINAL = C / "05_RENDER" / "out" / "WEBINAR_THOMSON_RESERVE_9x16_115.mp4"
SR = 16000


def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True).stdout.strip())


def frames_gray(f, ss, n, size="135:240"):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.4f}", "-i", str(f), "-frames:v", str(n),
                          "-vf", f"scale={size},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8)
    h, w = 240, 135
    return a.reshape(-1, h, w).astype(np.float32)


def audio(f, ss, t, tempo=None):
    af = ["-af", f"atempo={tempo}"] if tempo else []
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.4f}", "-t", f"{t:.4f}", "-i", str(f), *af,
                          "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def best_lag(ref, sig, max_lag):
    """lag (samples) of sig relative to ref maximising normalised xcorr."""
    ref = ref - ref.mean(); sig = sig - sig.mean()
    best, bl = -1e9, 0
    n = len(ref)
    for lag in range(-max_lag, max_lag + 1, 8):
        a = sig[max_lag + lag: max_lag + lag + n]
        if len(a) < n:
            continue
        c = float(np.dot(ref, a) / (np.linalg.norm(ref) * np.linalg.norm(a) + 1e-9))
        if c > best:
            best, bl = c, lag
    return bl, best


plan = json.loads((WK / "_tight_s115m.json").read_text())
segdir = WK / "_tight_s115m"
durs = [dur(segdir / f"seg{i:03d}.mp4") for i in range(len(plan))]
bases = np.concatenate([[0.0], np.cumsum(durs)[:-1]])
shots = json.load(open(WK / "build_115" / "shots.json"))


def tight_to_final(t):
    for s in shots:
        if s["t0"] - 1e-3 <= t < s["t1"]:
            return s["out0"] + (t - s["t0"])
    return None


print("seg  src_T    expected_tight  VIDEO(frames) AUDIO(ms)  |  FINAL: VIDEO(frames) AUDIO(ms)")
for k in (3, 12, 25, 40, 55, 61):
    label, a, b = plan[k]
    if b - a < 1.6:
        continue
    T = a + 0.9
    E = bases[k] + 0.9 / SPEED
    # ---- video: source frame at T vs tight frames E-8..E+8
    ref = frames_gray(SRC[label], T, 1)[0]
    win = frames_gray(TIGHT, E - 8 / 30, 17)
    d = [np.abs(win[i] - ref).mean() for i in range(len(win))]
    voff = int(np.argmin(d)) - 8
    # ---- audio: source 0.6s window from T-0.3 sped up, vs tight around E
    ref_a = audio(SRC[label], T - 0.3, 0.6, tempo=SPEED)
    n = len(ref_a)
    sig_a = audio(TIGHT, E - 0.3 / SPEED - 0.4, 0.6 / SPEED + 0.8)
    lag, c = best_lag(ref_a, sig_a, int(0.4 * SR))
    aoff_ms = lag / SR * 1000
    line = f"{k:3d}  {T:7.2f}  {E:9.3f}       {voff:+3d}         {aoff_ms:+6.0f} (c={c:.2f})"
    # ---- final
    F = tight_to_final(E)
    if F is not None:
        winf = frames_gray(FINAL, F - 8 / 30, 17)
        df = [np.abs(winf[i] - ref).mean() for i in range(len(winf))]
        vofff = int(np.argmin(df)) - 8
        sigf = audio(FINAL, F - 0.3 / SPEED - 0.4, 0.6 / SPEED + 0.8)
        lagf, cf = best_lag(ref_a, sigf, int(0.4 * SR))
        line += f"   |  {vofff:+3d}   {lagf / SR * 1000:+6.0f} (c={cf:.2f})   final_t={F:.2f}"
    print(line)
