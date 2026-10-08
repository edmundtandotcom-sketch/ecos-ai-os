#!/usr/bin/env python3
"""End-to-end mechanics test for render_v1.py on synthetic footage:
stand-in plate video + the sherpa test speech, scripts set to those transcripts,
and a beat list injected at fixed times so every device code path runs."""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import styleframes as SF, render_v1 as RV

T = HERE / "out" / "v1_test"; T.mkdir(parents=True, exist_ok=True)
RV.OUT = T
wavs = HERE.parent / "asr" / "sherpa-onnx-zipformer-en-2023-06-26" / "test_wavs"
trans = dict(l.split(" ", 1) for l in (wavs / "trans.txt").read_text().strip().splitlines())
RV.SCRIPT_HOOK = trans["0.wav"].capitalize() + "."
RV.SCRIPT_BODY = trans["1.wav"].capitalize() + ". " + trans["8k.wav"].capitalize() + "."

# synthetic takes: plate + speech (hook 6.6s, body = 1.wav + 8k.wav)
plate = T / "plate.png"; SF.plate(1).save(plate)
def mk(name, wav_list):
    lst = T / f"{name}_wavs.txt"; lst.write_text("".join(f"file '{w}'\n" for w in wav_list))
    a = T / f"{name}_audio.wav"
    subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ar", "16000", "-ac", "1", str(a)], check=True)
    dur = RV.probe(a)["dur"]
    out = T / f"{name}_take.mp4"
    subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-i", str(plate), "-i", str(a), "-t", f"{dur:.2f}",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(out)], check=True)
    return out
hook = mk("hook", [wavs / "0.wav"]); body = mk("body", [wavs / "1.wav", wavs / "8k.wav"])

class A: pass
a = A(); a.hook = str(hook); a.body = str(body); a.seed = 3; a.photos = str(HERE.parent / "photos")
SF.load_photos(a.photos)
for st in ("audio", "asr", "tighten", "plan"):
    print(f"\n== {st.upper()} =="); getattr(RV, f"stage_{st}")(a)

# inject one beat of every kind at fixed times so the render code paths all execute
plan = json.loads((T / "plan.json").read_text()); total = plan["total"]; he = plan["hook_end"]
words = json.loads((T / "words.json").read_text())
def wt(i): return words[min(i, len(words) - 1)]["s"]
plan["beats"] = [
    dict(kind="eyebrow", t0=0.2, t1=he, text="WOULD I BUY THIS FOR MY DAUGHTER?"),
    dict(kind="photo_card", t0=1.2, t1=he - 0.8, photo=0),
    dict(kind="receipt", t0=2.6, t1=he - 0.6),
    dict(kind="underline", t0=he - 1.4, t1=he),
    dict(kind="split", t0=he + 0.5, t1=he + 2.3, src="photo:2", whip=True),
    dict(kind="dotgrid", t0=he + 2.8, t1=he + 5.6, src="deck_p17"),
    dict(kind="bars", t0=he + 6.0, t1=he + 10.0, src="deck_p04", eyebrow="YOU'RE BUYING AFTER THE MRT STORY",
         k_bar1="X", k_bar2="Y", k_pill="Z", whip=True),
    dict(kind="pricegap", t0=he + 10.4, t1=he + 13.6, k_right="X", k_left="Y", k_gap="Z"),
    dict(kind="vs", t0=he + 14.0, t1=he + 16.6, whip=True),
    dict(kind="insert", t0=he + 17.0, t1=he + 19.0, src="photo:4", anchor_x=1.0, pull=True, dip=True),
    dict(kind="checklist", t0=he + 19.3, t1=min(total - 0.5, he + 23.0), items=["A", "B", "C", "D"], ticks=["X", "Y", "Z", "W"]),
]
plan["beats"] = [b for b in plan["beats"] if b["t1"] <= total]
(T / "plan.json").write_text(json.dumps(plan, indent=1))
# find_t falls back to `after` when a phrase misses — fine for the test
for st in ("render", "qc"):
    print(f"\n== {st.upper()} =="); getattr(RV, f"stage_{st}")(a)
