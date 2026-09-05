import json, sys, time
from pathlib import Path
from faster_whisper import WhisperModel
SRC = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar")
OUT = SRC / "05_RENDER" / "work"
PROMPT = ("Singapore property webinar. Edmund Tan, Legacy Launch, REI Method, second property, "
          "HDB, condo, CPF, ABSD, decoupling, S&P 500, new launch, Thomson Reserve, "
          "Second Property Ladder, one-property trap, know, move, own, webinar, register, link below.")
model = WhisperModel("medium", device="cpu", compute_type="int8")
for label, name in (("hooks", "1-Webinar Hooks.mp4"), ("body", "2-Webinar Body.mp4")):
    t = time.time()
    segs, _ = model.transcribe(str(SRC / name), word_timestamps=True, vad_filter=True,
                               language="en", initial_prompt=PROMPT)
    words = []
    for seg in segs:
        for w in (seg.words or []):
            words.append(dict(w=w.word.strip(), s=round(w.start, 3), e=round(w.end, 3)))
    (OUT / f"words_{label}.json").write_text(json.dumps(words, indent=1), encoding="utf-8")
    print(label, len(words), "words", f"{time.time()-t:.0f}s", flush=True)
print("DONE")
