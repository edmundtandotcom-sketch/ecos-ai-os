"""Exact video-timeline check: for plain speaker shots, frame 0 of the shot
file must equal the tight frame f0 cropped/scaled the same way (the push
move starts at zoom 1.0). Report which tight frame (f0-3..f0+3) matches."""
import json, subprocess, sys
import numpy as np
from pathlib import Path

sys.path.insert(0, r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER")
import render_webinar as R

WK = Path(r"E:\REMOTION\work\webinar_2026-09")
B = WK / "build_115"
TV = WK / "_tight_s115x_v.mp4"
FINAL = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\out\WEBINAR_THOMSON_RESERVE_9x16_115.mp4")
shots = json.load(open(B / "shots.json"))
files = [l.strip()[6:-1] for l in open(B / "shots.txt") if l.strip()]


def gray(f, vf, ss=None, n=1):
    pre = ["-ss", f"{ss:.4f}"] if ss is not None else []
    raw = subprocess.run(["ffmpeg", "-v", "error", *pre, "-i", str(f), "-frames:v", str(n),
                          "-vf", vf + ",scale=135:240,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.uint8).reshape(-1, 240, 135).astype(np.float32)


plain = [(i, s) for i, s in enumerate(shots) if not s.get("dev") and not s.get("backdrop") and not s.get("photo")
         and not s.get("treat") and not s.get("frame")]
picks = plain[::max(1, len(plain) // 10)][:10]
print("shot   t0       shotfile-vs-tight   final-vs-tight   (frame offset; 0 = exact)")
bad = 0
for i, s in picks:
    w, h, x, y = R.crop_for(R.ZOOMS[s["zoom"]], s["src"])
    vf = f"crop={w}:{h}:{x}:{y},scale={R.W}:{R.H}:flags=lanczos,{R.GRADE}"
    f0 = int(round(s["t0"] * 30))
    ref_shot = gray(files[i], "null")[0]
    ref_final = gray(FINAL, "null", ss=s["out0"])[0]
    cands = gray(TV, vf, ss=(f0 - 3) / 30, n=7)
    d1 = [np.abs(c - ref_shot).mean() for c in cands]
    d2 = [np.abs(c - ref_final).mean() for c in cands]
    o1, o2 = int(np.argmin(d1)) - 3, int(np.argmin(d2)) - 3
    bad += (o1 != 0) + (o2 != 0)
    print(f"{i:4d}  {s['t0']:7.3f}        {o1:+d} (min {min(d1):4.1f})            {o2:+d} (min {min(d2):4.1f})")
print("RESULT:", "video timeline exact" if bad == 0 else f"{bad} mismatches")
