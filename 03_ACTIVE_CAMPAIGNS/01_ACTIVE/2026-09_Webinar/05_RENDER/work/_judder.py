"""Judder check: per-frame mean abs difference over a speaker-only stretch.
Dropped frames from setpts-then-fps show as a periodic spike every ~7 frames;
blended speed-up shows a smooth series."""
import subprocess
import numpy as np
from pathlib import Path

O = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\out")


def series(f, ss, n=90):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ss), "-i", str(f), "-frames:v", str(n),
                          "-vf", "scale=270:480,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 480, 270).astype(np.float32)
    d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
    return d


for name, ss in (("WEBINAR_THOMSON_RESERVE_9x16.mp4", 27.5), ("WEBINAR_THOMSON_RESERVE_9x16_115.mp4", 24.0)):
    d = series(O / name, ss)
    # spikiness: ratio of the 90th percentile step to the median step
    print(f"{name:42} median {np.median(d):5.2f}  p90 {np.percentile(d, 90):5.2f}  "
          f"max {d.max():5.2f}  spike ratio {np.percentile(d, 90) / max(np.median(d), 1e-6):4.2f}")
    print("   first 30 steps:", " ".join(f"{x:4.1f}" for x in d[:30]))
