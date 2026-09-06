"""Where does the held frame at a cut come from? Same 3s window through the
pipeline: tight -> a shot file -> _cut.mp4 -> _body.mp4 -> final."""
import json, subprocess
import numpy as np
from pathlib import Path

WK = Path(r"E:\REMOTION\work\webinar_2026-09")
B = WK / "build_115"
OUT = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\out")


def steps(f, ss, n=60):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ss), "-i", str(f), "-frames:v", str(n),
                          "-vf", "scale=270:480,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 480, 270).astype(np.float32)
    return np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))


def show(tag, d):
    z = int((d < 0.5).sum())
    print(f"{tag:12} zero-steps {z:2d}/{len(d)}   " + " ".join(f"{x:4.1f}" for x in d[:40]))


shots = json.load(open(B / "shots.json"))
# a speaker-only stretch: find 3 consecutive plain speaker shots around 24s
i = next(k for k, s in enumerate(shots) if s["out0"] > 24 and not s.get("dev") and not s.get("backdrop") and not s.get("photo"))
s0 = shots[i]
print("shot", i, s0["out0"], s0["out1"], s0["text"], s0["motion"])
files = [l.strip()[6:-1] for l in open(B / "shots.txt") if l.strip()]
show("tight", steps(WK / "_tight_s115m.mp4", s0["t0"]))
show("shotfile", steps(files[i], 0))
show("_cut", steps(B / "_cut.mp4", s0["out0"]))
show("_body", steps(B / "_body.mp4", s0["out0"]))
show("final", steps(OUT / "WEBINAR_THOMSON_RESERVE_9x16_115.mp4", s0["out0"]))
# frame counts of that shot file
info = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
                       "-show_entries", "stream=nb_read_frames,duration", "-of", "csv=p=0", files[i]],
                      capture_output=True, text=True).stdout.strip()
print("shotfile frames,duration:", info, " planned", round(s0["t1"] - s0["t0"], 3))
