"""Isolate the final-mix audio drift: run variants of the final graph on a
60s excerpt of _body.mp4 and measure the audio offset at 50s vs _body."""
import subprocess
import numpy as np
from pathlib import Path

B = Path(r"E:\REMOTION\work\webinar_2026-09\build_115")
W = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\work")
AUDIO = Path(r"E:\REMOTION\public\audio")
BED = AUDIO / "bed_powerful_beat_123.mp3"
WH = AUDIO / "whoosh1.mp3"
SR = 16000

ex = W / "_mix_ex.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", "60", "-i", str(B / "_body.mp4"), "-c", "copy", str(ex)], check=True)


def audio(f, ss, t):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.3f}", "-t", f"{t:.3f}", "-i", str(f),
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


ref = audio(ex, 50.0, 0.6)
segs = [10.0, 30.0]
variants = {
    "full (whoosh+bed+loudnorm)": ("full", True, True, True),
    "no loudnorm": ("nol", True, True, False),
    "no bed": ("nobed", True, False, True),
    "no whoosh": ("nowh", False, True, True),
    "plain copy of speech": ("plain", False, False, False),
}
for name, (tag, whoosh, bed, ln) in variants.items():
    inputs = ["-i", str(ex), "-stream_loop", "-1", "-i", str(BED)]
    f = []
    mixin = "[0:a]"
    if whoosh:
        for i, t in enumerate(segs):
            inputs += ["-i", str(WH)]
            f.append(f"[{2+i}:a]adelay={int(t*1000)}|{int(t*1000)},volume=0.45[wh{i}]")
            mixin += f"[wh{i}]"
        f.append(f"{mixin}amix=inputs={len(segs)+1}:duration=first:dropout_transition=0,volume={len(segs)+1}[mx]")
    else:
        f.append("[0:a]anull[mx]")
    f.append("[mx]atempo=1.0[sp]")
    if bed:
        f.append("[1:a]volume=0.10,afade=t=out:st=58:d=2[bed]")
        f.append("[sp][bed]amix=inputs=2:duration=first:dropout_transition=0[m2]")
    else:
        f.append("[sp]anull[m2]")
    if ln:
        f.append("[m2]loudnorm=I=-16:TP=-1.5:LRA=11[a]")
    else:
        f.append("[m2]anull[a]")
    out = W / f"_mix_{tag}.m4a"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(f), "-map", "[a]",
                    "-t", "60", "-c:a", "aac", "-b:a", "192k", str(out)], check=True)
    sr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=sample_rate",
                         "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.strip()
    sig = audio(out, 50.0 - 2.5, 0.6 + 5.0)
    off, c = best_lag(ref, sig, int(2.5 * SR))
    print(f"{name:30} out sr={sr:>6}  audio offset at 50s: {off:+6.0f} ms (corr {c:.2f})")
