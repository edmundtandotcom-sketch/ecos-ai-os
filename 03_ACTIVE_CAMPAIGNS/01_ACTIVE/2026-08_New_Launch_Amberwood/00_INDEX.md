# Campaign Index — Amberwood at Holland (YouTube video #3, launch review)

Date: 2026-08-22
Status: REVIEW — v5 delivered (rounds 3+4 feedback combined; v4 was
superseded mid-render and never delivered)
v5 = v3 grammar + composite quality (erode-7 halo fix, hi-res sharpened
backdrop, colour-match 0.45, ALL head cams composited incl. bubbles) +
VA1 dynamic layer (fullscreen navy question interstitials, navy data
cards, info cards w/ real imagery, URA/Lentor/Peck Hay plates cropped
from the VA reference, TikTok animated captions, money rain, speed-line
shout, white subscribe pill) + price-only gold caption rule + v2 navy-bar
subtitles + horizontal QR + Review Studio v5 (A/B/C/D categories,
subtitle direct-edit loop via subs_manifest/subtitle_overrides, per-comment
asset + effect tags)
Deadline: publish before preview day (Fri 11 Sep 2026); launch 26 Sep

## Objective
Full pre-launch review of Amberwood at Holland (Sim Lian, D10, 212 units,
0% 1-2BR). Structure: hook (Skye 99% vs Dunearn 56%) → Point 1 township bet →
Point 2 launch economics → Point 3 allocation → Point 4 unit-by-unit (C1,
D4P/D5P, Luxe 48/50/52, D6P-vs-D7L) → verdict scorecard → Strategy Session CTA.

## Source of record
- Script: `Script with resources supports-....docx` (cues [CHART]/[TABLE]/
  [SCREEN]/(Picture N) + cross-check map in `cross check resources.md`)
- Footage: 9 multi-cam scenes; scenes 4–8 iPad captures (C files) are the
  LIVE display layer, per round-1 review
- Round-1 review (~70 items) captured via REVIEW_STUDIO 2026-08-20 — all
  applied in v2

## Production (runtime local: E:\REMOTION)
- Composition `AmberwoodReview` · generator `work/amberwood/build_amberwood.py`
- **Style Variant C — Clean White premium** (A=HDB, B=En Bloc; rotation rule)
- **Foundation rules locked by round-1 review (apply to all future videos):**
  - Talk scenes = front camera only (no B-angle alternation)
  - Layout/site-plan showcases = Edmund's recorded iPad presentations (C
    files) full-frame, rendered per-clip so dead-air cuts keep stage+voice
    in sync; head in circular gold-ring PIP bottom-right
  - Every spoken number/price gets an on-screen punchline/display
  - Money/number tokens never split across subtitle cues (glue rule +
    verify check)
  - Transition style rotates per scene (fade/wipe/slide)
  - Subscribe reminders seeded through the mid-stretch
  - Music: original synthesized beds only (`audio/rei_*`) — YouTube-safe,
    not Content-ID-claimable
- Gate: `verify_amberwood.py` — 10 checks, all passing
- v2 cut: 25:24 natural → 22:05 at 1.15x
- Review Studio v3: A/B/C comment categories + paste support, grouped export

## Open items (Edmund)
- Type D6P block number: script says Block 40, cross-check flags 44(?) —
  on-screen graphic currently says Block 40
- CPF OA rate on yield graphic: using 2.5%

## Companion video — "Which unit would I pick?" (2026-08-27)

A SECOND, standalone YouTube video cut from the back half of the review
(site plan + layouts). Both publish; v7 stays live as the full review.

- Composition `AmberwoodLong` (1920x1080) · generator
  `work/amberwood/build_long.py` · render `work/amberwood/render_long.ps1`
- **2ND PROPERTY METHOD brand** (the reels skin taken to 16:9), not the v7 skin
- 12:02 delivered at 1.15x + the house outro = 12:22
- Structure: curiosity cold open (dumbbell tease) -> who-I-am + subscribe ->
  setup -> micro-CTA (comment) -> 01 entry unit -> 02 two generations ->
  micro-CTA (session + QR) -> 03 the 4-bedrooms -> 04 Luxe blocks ->
  05 the dumbbell -> micro-CTA (comment) -> verdict -> CTA + QR
- **Layout showcases run the iPad C recordings FULL FRAME with Edmund carded
  on the right** (round-2 note): 126 of 154 shots. Reuses v7's STAGE_FILES,
  its measured `offsets_c.json` sync, and its BUBBLE_RULES side-swaps so the
  card never covers what he is pointing at. Only 4 static plates remain.
- Audio: per-segment loudness match PLUS a whole-programme EBU R128 flatten
  (I=-14, LRA=7, TP=-1.5) in the render script. The per-segment pass alone
  left a 6 dB spread because level drifts INSIDE a long segment.

### Render-host rules (learned the hard way 2026-08-26)
- Remotion copies ALL of `public/` into a fresh bundle on EVERY invocation.
  `public/` is ~25 GB; this video needs ~1 GB. Always render with
  `--public-dir=E:\REMOTION\public_amberwood`. Without it: ~30 min of
  copying before frame one, and single QA stills cost ~20 min each.
- Never run two Remotion CLI renders at once — a starting render clears
  sibling `%TEMP%\remotion-webpack-bundle-*` dirs and kills the other one.
  Queue with `work/amberwood/render_long_when_free.ps1`.
- QA from the finished MP4 (`work/amberwood/qa_long.ps1`), not from stills.

## Deliverables
- `AMBERWOOD_DRAFT_v1_1.15x.mp4` — reviewed (round 1 done)
- `AMBERWOOD_DRAFT_v2_1.15x.mp4` — rendering
- Reels batch (Reels V2 format) after long-form approval
- `AMBERWOOD_WHICH_UNIT_1080p.mp4` — companion video, round-2 feedback applied
- Upload kit on request

## Decision owner
Edmund. Desk: Content. Pipeline: /video-produce.
