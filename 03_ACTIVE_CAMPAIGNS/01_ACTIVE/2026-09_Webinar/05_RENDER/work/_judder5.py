"""Decode-accurate step series on the finals (output seek, no CFR fill artefact)."""
import subprocess
import numpy as np
from pathlib import Path

OUT = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\out")


def steps(f, ss, n=240):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-ss", str(ss), "-frames:v", str(n),
                          "-vf", "scale=135:240,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 240, 135).astype(np.float32)
    return np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))


for name in ("WEBINAR_THOMSON_RESERVE_9x16_115.mp4", "WEBINAR_THOMSON_RESERVE_9x16_120.mp4"):
    for ss in (24.0, 60.0):
        d = steps(OUT / name, ss)
        cuts = int((d > 30).sum())
        zeros = int((d < 0.3).sum())
        print(f"{name[-8:-4]} @{ss:5.1f}s  8s window: cuts {cuts:2d}  held frames {zeros:2d}  median step {np.median(d):4.1f}")
