# Campaign Index — Lucerne Grand (YouTube video #4, launch review)

Date: 2026-08-22
Status: LOOK DECISION — round-1 feedback applied 2026-08-22 evening.
DECIDED: 1.15x is the speed. REJECTED from demo v1: soft/haloed cutout
(cause: backdrop-CLI fast encode + colour-match 0.45 + punch upscale to
1.28), speaker filling full frame height, study-lamp backdrop, busy CDL
map pins (use the clean white connectivity map — Picture 28 — instead).
NEW LOOK CHAIN (proven on stills in `BACKDROP_OPTIONS/`): native-res RVM
cutout → green → alpha, NO colour-match, erode 4 / feather 1, subject-only
unsharp, quality encode; speaker at 0.82 scale, face on right-third,
soft contact shadow; backdrop cover-cropped + blur 3 + 0.88 brightness.
BACKDROP DECIDED: **J — Brand Studio (angled)**, generated room
(`E:\REMOTION\public\lucerne\plates\bgJ_*.png` = final plate w/ neon
"The REI Method" sign, wrap blur, raw). Realism pass v2 approved chain:
light wrap + grade blend (+13/+9/+6 RGB toward plate) + shared grain +
vignette + key falloff cx 0.60; speaker scale 0.84, face at x=0.60.
Motion compositor: `work/lucerne/compose_motion.py` (ffmpeg filtergraph —
scales to full video, replaces backdrop-CLI whole-frame composites).
LOOK ITERATIONS (2026-08-22/23): v1 rejected (desync = 25fps looped-PNG
bug; hands clipped; too flat). v2 added desk foreground + wall shadow +
rim light + crf16. v3 = the "Suby-grade" low-key recipe after Edmund's
reference frame: plate darkened 0.60 + defocus blur 11 + bloomed
practicals + neon drawn ON TOP (readable) + face key light + stronger
rims. Plate builder: `work/lucerne/build_plate.py <room image>` (use
--no-neon for a room that already carries the sign). Plates archived in
`E:\REMOTION\public\lucerne\plates`.
LOOK APPROVED 2026-08-23: **variant C — 60% neutralised**, speaker-anchored.
GRADE RULE LOCKED: the speaker's footage is the colour anchor; the plate is
white-balanced toward HIM (gray-world 60% + 25% nudge into his cast). The old
direction (subject shifted +13/+9/+6 toward the warm room) is what made him
look yellow — measured: footage R-B = -2.7, raw plate R-B = +46. Also retired:
the defocused desk-edge strip ("bottom screen blur"). 3-point post lighting
kept: warm key wash on the room-lit side, form shadow from the nose line
across his right, narrow cool rim on the shadow side; alpha S-curve solidifies
motion-blurred hands.

FULL BUILD IN PROGRESS (2026-08-23): all 11 scenes authored —
`work/lucerne/build_full.py` → composition `LucerneReview`.
616 clips (240 stage) · 127 overlays · 1,322 subtitle cues ·
**43:07 natural → 37:29 at 1.15x**. tsc clean.
Look pipeline per take: `prep_all.py` (RVM matte → green → compose_motion,
talk = rule-of-thirds, iPad stages = --full native scale so the head bubble
crops correctly). iPad sync +0.130s on all four (cross-correlated).
Builder fixes worth remembering: the shared restart-detector was deleting
real content because this script repeats "per square foot" constantly —
now capped at 8s AND requires a 4+ word run with a content word; phrase
anchors match on a normalised character stream (whisper splits "$250"+",000"
and "two"+"-bedroom") and snap to a clip start within 0.8s.
NEXT: render natural master → `finish_full.ps1` (1.15x + branded outro
REI_Method_Outro_v3) → deliver + REVIEW_STUDIO round 1.
Deadline: publish before preview day (Fri 18 Sep 2026); launch 3 Oct.

## Objective
Full pre-launch review of Lucerne Grand (CDL, D22, 570 units, beside
Lakeside MRT — first launch beside the MRT in 10 years). Structure: hook
(3 districts, 10-year gaps, launch-day results) → overview → P1 lake-condo
proof → P2 breakeven build → P3 comps (Sora/LakeGarden) → P4 older-condo
gains → P5 western corridor → P6 buyers + unit mix + floor plans (iPad) →
buyer types → P7 risk map → scorecard → $2,600 walk-away number →
Strategy Session CTA.

## Source of record
- Script: `Raw Assets/Recording Version.docx` (the spoken cut); long
  version with source tables: `Raw Assets/Lucerne Grand Aug 2026 Script.docx`
- Google Doc guide: docs.google.com/document/d/1it85Z2I5O0lN_eu4f3WYxzOW4LRLoyqwfl8KdOQkmAU
- Footage: `Raw Assets/` — takes 1–8 + 6A/6B/6C, four angles per take
  (N = front master · N-DSLR = front 720p backup · N-Webcam = side ·
  6-series N-ipad = floor-plan walkthrough display layer)
- Supporting assets: `Raw Assets/Supporting Assets/Picture 1–39`
  (map plate, launch articles, unit mix table, JLD plates, at-a-glance)
- Production quality benchmarks: E:\REMOTION\work\study\PRODUCTION_REFS_2026-08-22.md
  (Edmund's four reference long-forms — drives the Variant D upgrades)

## Production (runtime local: E:\REMOTION)
- Composition `LucerneReview` · generator `work/lucerne/build_lucerne.py`
- **Style Variant D — Cinematic Paper** (A=HDB, B=En Bloc, C=Amberwood;
  rotation rule). NEW this video, mirrored from the production-refs study:
  - Backdrop: `podcast-study-lamp` (E:\BACKDROP) — cinematic depth,
    practical lamp; navy shirt separates (led-shelves stays Amberwood's)
  - 3-level punch rotation 1.0/1.14/1.28 + slow push (KenBurnsVideo) —
    every cut lands as an angle change (digital multi-angle)
  - PaperKit (src/components/PaperKit.tsx): torn-paper chips ·
    marker-highlight boxes · building tick lists · giant black slates
  - B&W emphasis flip on drama beats (clip.mono)
  - Theme D: warm paper surfaces, ink text, amber marker accent
- Locked guardrails unchanged: navy plates fullscreen (VAKit/DynKit),
  v2 navy-bar subtitles, gold price-only pops, QR bottom-left, nothing
  covers the speaker, original `audio/rei_*` music beds only
- Composite params (locked round-3): mode max, erode 7, feather 3,
  colour-match 0.45, bg-blur 4, bg-zoom 1.02 (`work/lucerne/compose.py`)

## Open items (Edmund)
- Chuan Park figures: audio says "996 of 960"; script + subtitles/display
  use the verified 696 of 916. OK to ship with subtitle correction, or
  re-record that line?
- Sora/LakeGarden map pins on the CDL map plate are placed approximately
  (both on Yuan Ching Rd) — verify before final.
- Demo decision: 1.1x vs 1.15x.

## Deliverables
- `LUCERNE_DEMO_1.1x.mp4` + `LUCERNE_DEMO_1.15x.mp4` (3-min demo, take 1)
- Full long-form after demo sign-off; reels after long-form approval

## Decision owner
Edmund. Desk: Content. Pipeline: /video-produce.
