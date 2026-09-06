from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\work\_final_audit2.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


rep('''for i, s in plain[::max(1, len(plain) // 12)][:12]:''',
    '''for i, s in plain[::max(1, len(plain) // 30)][:30]:''')
rep('''log = (R / "work" / "compose13_115.log").read_text(encoding="utf-8", errors="ignore")''',
    '''log = (R / "work" / "compose14_115.log").read_text(encoding="utf-8", errors="ignore")''')
p.write_text(s, encoding="utf-8")
print("audit widened to 30 shots")

q = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\00_INDEX.md")
t = q.read_text(encoding="utf-8")
a = t.index("## Current deliverables")
b = t.index("## Edit decisions")
new = """## Current deliverables (round 3, 2026-09-05)
| File | Speed | Length | Notes |
|---|---|---|---|
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16_115.mp4` | 1.15x | 2:38 (158.4s) | sync rebuilt from scratch and audited against the raw take (see round 3) |
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16_120.mp4` | 1.20x | 2:32 | round-2 build - NOT rebuilt, carries the round-2 sync defect; do not use |
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16.mp4` | 1.15x | 2:55 | round-1 cut - superseded |

"""
t = t[:a] + new + t[b:]
a = t.index("## Definition of done")
new2 = """**Round 3 (2026-09-05, "nothing is synced")**
- Root cause: audio was assembled from per-shot and per-segment AAC files;
  every AAC seam carries a ~30ms timestamp gap that a player honours but the
  final mix packs shut - speech ran 1.8s late by the 50s mark in every round.
- Rebuilt sync by construction: exact-N-frame video segments + exact-sample
  PCM audio in the tighten stage, video-only shots on the frame grid, one
  continuous speech track in the final mix, assertions at every stage.
- Seek fix: shot seeks are now half a frame early (a 4-decimal seek dropped
  the first frame on one shot in three).
- Whoosh impact (0.89s into the sample) now lands on the cut.
- Audit before delivery (`05_RENDER/work/_final_audit2.py`): speech offset vs
  raw take, video frame offset on clean shots, caption vs spoken word, whoosh
  vs cut, device starts on shot boundaries, held frames.

"""
t = t[:a] + new2 + t[a:]
q.write_text(t, encoding="utf-8")
print("index updated")
