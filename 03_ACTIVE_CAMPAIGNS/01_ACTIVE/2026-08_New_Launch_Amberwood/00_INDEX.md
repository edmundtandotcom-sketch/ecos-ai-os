# Campaign Index — Amberwood at Holland (YouTube video #3, launch review)

Date: 2026-08-18
Status: BUILD — first QA stills in review; draft render next
Deadline: publish before preview day (Fri 11 Sep 2026); launch 26 Sep

## Objective
Full pre-launch review of Amberwood at Holland (Sim Lian, D10, 212 units,
0% 1-2BR). Structure: hook (Skye 99% vs Dunearn 56%) → Point 1 township bet →
Point 2 launch economics → Point 3 allocation → Point 4 unit-by-unit (C1,
D4P/D5P, Luxe 48/50/52, D6P-vs-D7L) → verdict scorecard → Strategy Session CTA.

## Source of record
- Script: `Script with resources supports-....docx` (cues [CHART]/[TABLE]/
  [SCREEN]/(Picture N) + cross-check map in `cross check resources.md`)
- Footage: 9 multi-cam scenes (masters + B-angles; scenes 4–8 also have the
  raw iPad display captures NC used as timing reference only)
- Displays rebuilt at full quality from `floor plan.pdf` (18 pp), E-Book v2.3,
  Architect Briefing (144 pp), Pictures 1–25

## Production (runtime local: E:\REMOTION)
- Composition `AmberwoodReview` · generator `work/amberwood/build_amberwood.py`
- **Style Variant C — Clean White premium** (A=HDB, B=En Bloc; rotation rule)
- **Multi-cam**: angle blocks ~14s, audio-sync verified (offsets ≤0.07s)
- **New v5 components**: PlanStage (hi-res plan pan/zoom + speech-anchored
  callout rings mirroring Edmund's iPad annotations), PlanVS (floor-plan duel)
- Auto-restart detection with AUDITED whitelist (13 false positives kept as
  real content — presentation speech repeats phrases legitimately)
- Gate: `verify_amberwood.py` — 8 checks, all passing
- Current cut: 26:26 natural → 22:59 at 1.15x (target 18–22, trim in review)

## Open items (Edmund)
- Type D6P block number: script says Block 40, cross-check flags 44(?) —
  on-screen graphic currently says Block 40
- CPF OA rate on yield graphic: using 2.5%

## Deliverables (planned)
- `AMBERWOOD_DRAFT_v1_1.15x.mp4` → review via REVIEW_STUDIO → final + outro
- Reels batch (Reels V2 format) after long-form approval
- Upload kit on request

## Decision owner
Edmund. Desk: Content. Pipeline: /video-produce.
