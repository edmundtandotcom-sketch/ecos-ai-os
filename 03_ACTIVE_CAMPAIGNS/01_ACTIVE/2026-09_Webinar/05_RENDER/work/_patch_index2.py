from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\00_INDEX.md")
s = p.read_text(encoding="utf-8")
a = s.index("## Current deliverables")
b = s.index("## Definition of done")
new = """## Current deliverables (round 2, 2026-09-05)
| File | Speed | Length | Notes |
|---|---|---|---|
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16_115.mp4` | 1.15x | 2:39 (159.0s) | 168 shots, 63 cuts/min, 38 beats, captions on every shot |
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16_120.mp4` | 1.20x | 2:32 (152.4s) | same cut, faster |
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16.mp4` | 1.15x | 2:55 | round-1 cut Edmund reviewed - superseded |

## Edit decisions
**Round 1 (2026-09-04)**
- Hook 1 chosen: number + question in the first 2s. H2/H3 available as variants on request.
- Body re-ordered: likes -> "three things making me think twice" -> dislikes -> CTA.
- Dropped: 144-149s restart, 202.7-212.6s take that trails off, 218s fragment.
- Transcript fixes: Tre Ver, Parc Clematis, Ai Tong, Central Catchment, "stacks" (not tax), "analysis".

**Round 2 (2026-09-05, from Edmund's timestamped notes)**
- Jerking: the phone take drops frames in bursts; speed is now applied with
  motion-compensated interpolation in the tighten stage, not on the final.
- Captions on every shot in one band (0.80), including on plates; orange box
  hugs the word; hook slam moved above the band so the face stays clear.
- Gaps tightened (0.20 / 0.10 / 0.07); 1:57.9-2:01.0 ("So you'll be
  potentially paying more thaaan") cut; graph-paper plate removed.
- Condos only (no HDB) in the LIKE/DISLIKE beat; real forest for Central
  Catchment; a train on a viaduct for the MRT beat; an 800m pin-and-radius
  map for "within 800m of TEL stations".
- Faster bed: 123 BPM future-bass (Pixabay, commercial licence).
- Working files now on E:\\REMOTION\\work\\webinar_2026-09 (Drive locks).

"""
s = s[:a] + new + s[b:]
p.write_text(s, encoding="utf-8")
print("index updated")
