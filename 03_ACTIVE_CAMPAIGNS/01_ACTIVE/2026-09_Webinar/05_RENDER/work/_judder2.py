import subprocess, time
import numpy as np
from pathlib import Path

C = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar")
W = C / "05_RENDER" / "work"
SRC = C / "2-Webinar Body.mp4"


def steps(f, ss=0, n=90, vf="scale=270:480,format=gray"):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ss), "-i", str(f), "-frames:v", str(n),
                          "-vf", vf, "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 480, 270).astype(np.float32)
    return np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))


def report(tag, d):
    dups = int((d < 0.35 * np.median(d)).sum())
    print(f"{tag:34} median {np.median(d):5.2f}  p90 {np.percentile(d,90):5.2f}  near-dup steps {dups}/{len(d)}")
    print("   ", " ".join(f"{x:4.1f}" for x in d[:36]))


report("RAW source @60s", steps(SRC, 60))

# 6s excerpt, three treatments, timed
ex = W / "_ex_raw.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "60", "-t", "6", "-i", str(SRC), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", str(ex)], check=True)
tests = {
    "blend 1.15x (current)": "setpts=PTS/1.15,minterpolate=fps=30:mi_mode=blend",
    "mci 1.15x": "setpts=PTS/1.15,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1",
    "decimate+mci 1.15x": "mpdecimate,setpts=PTS/1.15,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1",
}
for tag, vf in tests.items():
    out = W / ("_ex_" + tag.split()[0] + ".mp4")
    t = time.time()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(ex), "-vf", f"scale=1080:1920,{vf}", "-r", "30",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", str(out)], check=True)
    el = time.time() - t
    d = steps(out, 0)
    report(f"{tag} ({el:4.1f}s for 6s)", d)
