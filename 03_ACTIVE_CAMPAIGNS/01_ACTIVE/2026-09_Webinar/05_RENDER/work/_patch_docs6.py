from pathlib import Path

p = Path(r"H:\Shared drives\00_E.C.O.S\.claude\skills\rei-ad-build\SKILL.md")
s = p.read_text(encoding="utf-8")
old = "## 6. Growing the library"
new = """- **SYNC BY CONSTRUCTION - the rule that replaces all the seam fixes above.**
  Never build the ad's audio from per-shot or per-segment AAC files. Every
  AAC encode leaves a ~30ms timestamp gap at its seam; a player honours the
  gaps (so stage-by-stage checks pass) but the final filter graph packs the
  samples shut and the speech runs ~33ms late per cut - 1.8s by 50s, on
  EVERY round until 2026-09-05. The tighten stage now makes each segment
  EXACTLY N video frames and EXACTLY N*1600 samples of PCM; shots are cut
  video-only on the frame grid; the final mixes the ONE continuous wav.
  Assertions at each stage (segment frames, shot frames, cut frames vs
  timeline, tight audio vs frames) raise instead of shipping drift.
- **Audit before delivery, against the raw take:** speech offset (<=40ms),
  video offset on clean shots (0 frames), caption vs spoken word, whoosh
  impact on the cut, device starts on shot boundaries, held frames.
  `work/_final_audit2.py` is the template.
- Whoosh: `adelay` the file so its IMPACT (0.89s into whoosh1.mp3) lands on
  the cut, not its silent lead-in.

## 6. Growing the library"""
assert s.count(old) == 1
p.write_text(s.replace(old, new), encoding="utf-8")
print("skill")

p = Path(r"C:\Users\Admin\.claude\projects\H--Shared-drives-00-E-C-O-S\memory\ads-not-reels-playbook.md")
s = p.read_text(encoding="utf-8")
s += """
**THE sync bug, found 2026-09-05 after Edmund's "nothing is synced":** all
rounds built the audio by concatenating per-shot (and per-segment) AAC
files. Each AAC encode leaves a ~30ms timestamp gap at its seam. A player
honours the gaps, so every stage-by-stage check looked fine; the FINAL
filter graph (amix/loudnorm, even a plain re-encode) packs the samples shut
and the speech runs ~33ms late per cut - 1.8s late by 50s. Fix = sync by
construction: tighten makes exact-N-frame video segments + exact-N*1600-
sample PCM audio, shots are video-only on the frame grid, the final mixes
ONE continuous wav; assertions raise on any mismatch. Audit vs the raw take
before delivering (`_final_audit2.py`): speech <=40ms, video 0 frames on
clean shots, caption==spoken word, whoosh impact on the cut. Also: the
frame-match audit is only valid on frames without whip blur or VFX.
"""
p.write_text(s, encoding="utf-8")
print("memory")
