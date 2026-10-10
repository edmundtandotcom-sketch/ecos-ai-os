"""batch_tr on synthetic takes: a 3-hook take (hooks 1-3 back to back with pauses), two body takes, and the
combined Daughter Hook 1-New take. Checks: each hook is cut from its own stretch of the multi-hook take,
the body cut is reused across jobs, every ad is 1080x1920, the report is written."""
import subprocess, sys, shutil, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import styleframes as SF, render_v1 as RV, tr_scripts as TS, batch_tr as BT
T = HERE / "out" / "batch_test"; shutil.rmtree(T, ignore_errors=True); (T / "Longer Ads").mkdir(parents=True)
wavs = HERE.parent / "asr" / "sherpa-onnx-zipformer-en-2023-06-26" / "test_wavs"
trans = {k: v.capitalize() + "." for k, v in (l.split(" ", 1) for l in (wavs / "trans.txt").read_text().strip().splitlines())}
sil = T / "sil.wav"; subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", "1.2", str(sil)], check=True)
plate = T / "plate.png"; SF.plate(1).save(plate)
def mk(path, wav_list, size="1080x1920"):
    lst = T / (path.stem + "_wavs.txt"); lst.write_text("".join(f"file '{w}'\n" for w in wav_list))
    a = T / (path.stem + "_audio.wav")
    subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ar", "16000", "-ac", "1", str(a)], check=True)
    dur = RV.probe(a)["dur"]
    subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-i", str(plate), "-i", str(a), "-t", f"{dur:.2f}",
                    "-vf", f"scale={size.replace('x', ':')}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(path)], check=True)
LA = T / "Longer Ads"
mk(LA / "Daughter Spin Hook 1-5.mp4", [wavs / "1.wav", sil, wavs / "0.wav", sil, wavs / "8k.wav"])   # hooks 1, 2 and a tail the model cannot hear (8 kHz sample)
mk(LA / "Body-Exit-Short.mp4", [sil, wavs / "1.wav", sil, wavs / "8k.wav"])
mk(LA / "Body-Ballot-Short.mp4", [wavs / "0.wav", sil, wavs / "8k.wav"])
mk(LA / "Daughter Hook 1-New.mp4", [wavs / "0.wav", sil, wavs / "1.wav", sil, wavs / "8k.wav"])      # DH1 + body FULL in one take
mk(T / "Selfie Daughter Hook 1.mp4", [wavs / "0.wav", sil, wavs / "8k.wav"])
# the scripts, swapped for the test transcripts
TS.DAUGHTER_HOOK_1 = trans["0.wav"]
TS.HOOKS = {1: ("HOOK ONE", trans["1.wav"]), 2: ("HOOK TWO", trans["0.wav"]), 3: ("HOOK THREE", "Nobody says this sentence anywhere in these recordings tonight, so the report must flag it.")}
TS.BODIES = {"FULL": trans["1.wav"] + " " + trans["8k.wav"], "EXIT": trans["1.wav"] + " " + trans["8k.wav"], "BALLOT": trans["0.wav"] + " " + trans["8k.wav"]}
report = BT.main(["--folder", str(T), "--work", str(T / "work"), "--photos", str(HERE.parent / "photos"), "--only", "FULL,H01,H02,H03_EXIT"])
notes = {r[0]: r[1] for r in report}
print(notes)
assert len(report) == 6, notes
assert all(n.startswith("OK") and "CHECK" not in n for i, n in notes.items() if "H03" not in i), notes
assert "CHECK" in notes["TR_H03_EXIT"], "a hook that is not in the take must be flagged"      # the wrong-hook guard
# a second run renders nothing new (everything is there already)
again = {r[0]: r[1] for r in BT.main(["--folder", str(T), "--work", str(T / "work"), "--photos", str(HERE.parent / "photos"), "--only", "FULL,H01,H02,H03_EXIT", "--no-cloud"])}
assert all(n == "already rendered" for n in again.values()), again
# hook 2 sits in the middle of the 3-hook take: its words must start after hook 1 (~16 s) and span under 12 s
hw = json.loads((T / "work" / "TR_H02_EXIT" / "words_hook.json").read_text())
print(f"hook 2 in the take: {hw[0]['s']:.1f}–{hw[-1]['e']:.1f}s")
assert hw[0]["s"] > 12 and hw[-1]["e"] - hw[0]["s"] < 12, "hook 2 was not cut from its own stretch of the take"
hw1 = json.loads((T / "work" / "TR_H01_EXIT" / "words_hook.json").read_text())
assert hw1[-1]["e"] < hw[0]["s"], "hook 1 must come before hook 2"
log = (T / "Longer Ads" / "RENDERS" / "batch_log.txt").read_text(encoding="utf-8")
assert log.count("cut reused from an earlier job") >= 3, "body cut cache did not kick in"
for f in sorted((T / "Longer Ads" / "RENDERS").glob("*_1080x1920.mp4")):
    m = RV.probe(f); assert (m["w"], m["h"]) == (1080, 1920), (f.name, m)
    print(f"  {f.name:32s} {m['dur']:5.1f}s  preview {(f.parent / f.name.replace('_1080x1920.mp4', '_preview_small.mp4')).stat().st_size/1e6:.1f} MB")
cloud = sorted((T / "Longer Ads" / "_cloud").glob("*.mp4")); print("cloud copies:", [c.name for c in cloud])
assert all(c.stat().st_size < 5.5e6 for c in cloud) and len(cloud) >= 4
# the EXIT / BALLOT devices drawn once, with the custom items, to be sure they render
from PIL import Image
layer = Image.new("RGBA", (SF.W, SF.H), (0, 0, 0, 0))
SF.dev_checklist(layer, 1.0, y_top=0.40, items=[("2-BED OR 3-BED?", "1f3e2"), ("WHICH STACKS EXIT STRONGER?", "1f4cd"), ("WHAT PRICE LEAVES UPSIDE?", "1f4b0"), ("UNITS I WOULDN'T TOUCH", "1f6ab")])
SF.eyebrow(layer, "THE EXIT", y_frac=0.47, size=58, bg=SF.GOLD, fg=SF.INK)
layer.save(T / "devices_exit.png")
print("BATCH TEST OK")
