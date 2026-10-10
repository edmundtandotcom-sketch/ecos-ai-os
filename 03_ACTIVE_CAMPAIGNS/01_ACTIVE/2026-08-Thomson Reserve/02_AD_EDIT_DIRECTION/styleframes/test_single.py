"""One-file mode on a synthetic take that carries the hook and then the CTA (pick_test's combined take)."""
import json, sys, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import styleframes as SF, render_v1 as RV
T = HERE / "out" / "single_test"; T.mkdir(parents=True, exist_ok=True); RV.OUT = T
wavs = HERE.parent / "asr" / "sherpa-onnx-zipformer-en-2023-06-26" / "test_wavs"
trans = dict(l.split(" ", 1) for l in (wavs / "trans.txt").read_text().strip().splitlines())
RV.SCRIPT_HOOK = trans["0.wav"].capitalize() + "."
RV.SCRIPT_CTA_SHORT = trans["1.wav"].capitalize() + ". " + trans["8k.wav"].capitalize() + "."
RV.SINGLE = True; RV.PREFIX = "TR_SHORT"; RV.SCRIPT_BODY = RV.SCRIPT_CTA_SHORT
take = HERE / "out" / "pick_test" / "Longer Ads" / "Daughter Hook 1-New.mp4"
class A: pass
a = A(); a.hook = a.body = str(take); a.seed = 3; a.photos = str(HERE.parent / "photos"); SF.load_photos(a.photos)
for st in ("audio", "asr", "tighten", "plan", "render", "qc"):
    print(f"\n== {st.upper()} =="); getattr(RV, f"stage_{st}")(a)
words = json.loads((T / "words.json").read_text())
he = max(w["e"] for w in words if w["clip"] == "hook"); bs = min(w["s"] for w in words if w["clip"] == "body")
print(f"hook ends {he:.2f}s, body starts {bs:.2f}s, total {RV.probe(T / 'TR_V1_Receipt_9x16.mp4')['dur']:.1f}s")
assert bs >= he - 0.05, "body overlaps hook"
print("SINGLE TEST OK")
