"""Rough tempo + loudness for the harvested beds: onset-envelope autocorrelation."""
import subprocess
import numpy as np
from pathlib import Path

H = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\work\_harvest")
SR = 22050
for f in sorted(H.glob("m_*.mp3")):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-t", "60", "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                               capture_output=True, text=True).stdout.strip() or 0)
    hop = 256
    n = len(x) // hop
    env = np.array([np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2)) for i in range(n)])
    onset = np.maximum(0, np.diff(env))
    onset -= onset.mean()
    ac = np.correlate(onset, onset, mode="full")[len(onset) - 1:]
    fps = SR / hop
    lo, hi = int(fps * 60 / 200), int(fps * 60 / 70)      # 70-200 BPM
    lag = lo + int(np.argmax(ac[lo:hi]))
    bpm = 60 * fps / lag
    rms = 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
    print(f"{f.name:26} {dur:6.1f}s  ~{bpm:5.1f} BPM  rms {rms:5.1f} dB")
