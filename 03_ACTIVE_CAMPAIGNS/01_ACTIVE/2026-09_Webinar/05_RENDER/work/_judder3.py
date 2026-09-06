import subprocess, time
import numpy as np
from pathlib import Path

W = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\work")
ex = W / "_ex_raw.mp4"


def steps(f, n=90):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-frames:v", str(n),
                          "-vf", "scale=270:480,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 480, 270).astype(np.float32)
    return np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))


tests = {
    "mci_bilat_sp16": "setpts=PTS/1.15,minterpolate=fps=30:mi_mode=mci:mc_mode=obmc:me_mode=bilat:search_param=16:scd=none",
    "mci_bilat_sp8_mb32": "setpts=PTS/1.15,minterpolate=fps=30:mi_mode=mci:mc_mode=obmc:me_mode=bilat:search_param=8:mb_size=32:scd=none",
    "mci_bidir_sp8": "setpts=PTS/1.15,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:search_param=8:scd=none",
}
for tag, vf in tests.items():
    out = W / f"_ex_{tag}.mp4"
    t = time.time()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(ex), "-vf", f"scale=1080:1920,{vf}", "-r", "30",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", str(out)], check=True)
    el = time.time() - t
    d = steps(out)
    print(f"{tag:22} {el:5.1f}s for 6s  median {np.median(d):5.2f} p90 {np.percentile(d,90):5.2f}")
