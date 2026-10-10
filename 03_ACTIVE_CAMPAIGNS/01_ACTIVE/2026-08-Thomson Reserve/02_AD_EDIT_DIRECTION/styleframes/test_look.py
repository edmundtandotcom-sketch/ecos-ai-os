"""A looked ad end to end on the synthetic takes from test_batch: the look's headline, captions, proof scene,
body scene, cuts, border and end card must all render; the proof and body devices are anchored to words
that exist in the test transcripts."""
import sys, json, shutil
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import styleframes as SF, render_v1 as RV, tr_scripts as TS, looks as LK, batch_tr as BT
T = HERE / "out" / "batch_test"; assert (T / "Longer Ads" / "Daughter Spin Hook 1-5.mp4").exists(), "run test_batch.py first"
wavs = HERE.parent / "asr" / "sherpa-onnx-zipformer-en-2023-06-26" / "test_wavs"
trans = {k: v.capitalize() + "." for k, v in (l.split(" ", 1) for l in (wavs / "trans.txt").read_text().strip().splitlines())}
ad = sys.argv[1] if len(sys.argv) > 1 else "TR_H02_EXIT"
import re; mm = re.match(r"TR_H(\d+)_(EXIT|BALLOT)", ad); hk, body = int(mm.group(1)), mm.group(2)
TS.HOOKS = {hk: (TS.HOOKS[hk][0], trans["0.wav"])}                                   # the hook = 0.wav, wherever it sits in the take
TS.BODIES = {"FULL": trans["1.wav"], "EXIT": trans["1.wav"] + " " + trans["8k.wav"], "BALLOT": trans["1.wav"] + " " + trans["8k.wav"]}
look = LK.LOOKS[ad]
LK.HOOK_ANCHORS[look["hook_dev"]] = ["yellow lamps", "__question__"]           # inside 0.wav
LK.BODY_ANCHORS[body][look["body_dev"]] = (["lovely child"], "parent", 0) if look["body_dev"] in ("check_white", "check_dark", "ballot") else (["lovely child"], None, 2.8)
for p in (T / "Longer Ads" / "RENDERS").glob(ad + "_*"): p.unlink()
report = BT.main(["--folder", str(T), "--work", str(T / "work"), "--photos", str(HERE.parent / "photos"), "--only", ad, "--no-cloud", "--force"])
note = report[0][1]; print(note); assert note.startswith("OK"), note
plan = json.loads((T / "work" / ad / "plan.json").read_text())
kinds = [b["kind"] for b in plan["beats"]]; print("beats:", [(b["kind"], b.get("dev"), b["t0"], b["t1"]) for b in plan["beats"]])
assert "headline" in kinds and "proof" in kinds and "bodydev" in kinds, kinds
m = RV.probe(T / "Longer Ads" / "RENDERS" / f"{ad}_1080x1920.mp4"); assert (m["w"], m["h"]) == (1080, 1920)
print("LOOK TEST OK", ad)
