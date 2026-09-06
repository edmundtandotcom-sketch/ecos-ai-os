import subprocess
import numpy as np
from pathlib import Path

D = Path(r"E:\REMOTION\work\webinar_2026-09")


def steps(f, n=400):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-frames:v", str(n),
                          "-vf", "scale=135:240,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 240, 135).astype(np.float32)
    return np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))


for tag in ("_tight_s115m", "_tight_s115n"):
    for name in ("seg001.mp4", "seg002.mp4"):
        f = D / tag / name
        if not f.exists():
            continue
        d = steps(f)
        print(f"{tag}/{name:12} frames {len(d)+1:4d}  head {' '.join(f'{x:4.1f}' for x in d[:4])}   tail {' '.join(f'{x:4.1f}' for x in d[-4:])}   zeros {(d < 0.3).sum()}")
