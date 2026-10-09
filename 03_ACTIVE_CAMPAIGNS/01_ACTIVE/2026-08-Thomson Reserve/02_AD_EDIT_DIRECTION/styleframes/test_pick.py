"""pick_takes on a folder with a subfolder: a combined hook+body take (DSLR-ish 1920x1080), a hook-only
phone take with a CTA tail, and a decoy. Scripts set to the sherpa test transcripts."""
import subprocess, sys, shutil
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import styleframes as SF, render_v1 as RV
T = HERE / "out" / "pick_test"; shutil.rmtree(T, ignore_errors=True); (T / "Longer Ads").mkdir(parents=True); (T / "_render_v1").mkdir()
RV.OUT = T / "work"
wavs = HERE.parent / "asr" / "sherpa-onnx-zipformer-en-2023-06-26" / "test_wavs"
trans = dict(l.split(" ", 1) for l in (wavs / "trans.txt").read_text().strip().splitlines())
RV.SCRIPT_HOOK = trans["0.wav"].capitalize() + "."
RV.SCRIPT_BODY = trans["1.wav"].capitalize() + ". " + trans["8k.wav"].capitalize() + "."
RV.SCRIPT_BODY2_HEAD = "Something else entirely that nobody says in these recordings at all."
plate = T / "plate.png"; SF.plate(1).save(plate)
def mk(path, wav_list, size="1080x1920"):
    lst = T / (path.stem + "_wavs.txt"); lst.write_text("".join(f"file '{w}'\n" for w in wav_list))
    a = T / (path.stem + "_audio.wav")
    subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ar", "16000", "-ac", "1", str(a)], check=True)
    dur = RV.probe(a)["dur"]
    subprocess.run([RV.FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-i", str(plate), "-i", str(a), "-t", f"{dur:.2f}",
                    "-vf", f"scale={size.replace('x', ':')}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(path)], check=True)
mk(T / "Longer Ads" / "Daughter Hook 1-New.mp4", [wavs / "0.wav", wavs / "1.wav", wavs / "8k.wav"], "1920x1080")   # hook + body in one take
mk(T / "Selfie Daughter Hook 1.mp4", [wavs / "0.wav", wavs / "8k.wav"])                                       # hook + a tail
mk(T / "Selfie Body2.mp4", [wavs / "8k.wav", wavs / "8k.wav"])                                                 # decoy
mk(T / "_render_v1" / "ignored.mp4", [wavs / "0.wav"])                                                         # must be skipped
hook, body = RV.pick_takes(T)
assert Path(hook).name == "Daughter Hook 1-New.mp4" and Path(body).name == "Daughter Hook 1-New.mp4", (hook, body)
# now the asr stage on that combined take: hook words must end before body words begin
class A: pass
a = A(); a.hook = hook; a.body = body
RV.stage_audio(a); RV.stage_asr(a)
import json
hw = json.loads((RV.OUT / "words_hook.json").read_text()); bw = json.loads((RV.OUT / "words_body.json").read_text())
print(f"hook span {hw[0]['s']:.2f}–{hw[-1]['e']:.2f}s, body span {bw[0]['s']:.2f}–{bw[-1]['e']:.2f}s")
assert hw[-1]["e"] < bw[0]["s"] + 0.5 and hw[-1]["e"] < 9.0, "hook alignment ran into the body"
print("PICK TEST OK")
