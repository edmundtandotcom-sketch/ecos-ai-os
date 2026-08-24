# Campaign Index — Lucerne Grand (YouTube video #4, launch review)

Date: 2026-08-22
Status: FINAL BUILD — look LOCKED 2026-08-24.

## THE LOOK (FINAL — locked 2026-08-24, do not revisit)
**The ORIGINAL room footage, UNGRADED.** No cutout, no synthetic backdrop,
and no colour enhancement of any kind. What ships is what the camera shot.
Route taken to get here (all evidence kept in the campaign folder):
- 11 one-minute MOTION variations (`LOOK_VARIATIONS/`) — every composite
  lost to the real room, so cutout/backdrop was dropped entirely.
- 8 grade options + tone ladders (`GRADE_OPTIONS/`) — G1 clean, then
  progressively cooler (G1w1-w3), then cooler still (A/B/C). Edmund's final
  call: no enhancement at all, use the original tone.
- `timeline.pregraded = True` stops the renderer applying its own legacy
  contrast/saturate/brightness filter, which is what made the first full cut
  look "too bright / too yellow / fake" despite an approved cool grade.
Heads are the plain encoded takes (`<take>.mp4`); the only processing is the
re-encode + voice chain in `prep.ps1`. iPad captures likewise untouched.
Composition still applies: framing holds per SCENE (1.0/1.06/1.10, capped so
1080p is never upscaled soft) and the head eases aside when a panel is up.
The graded `<take>G.mp4` files and `bake_grade.sh` remain on disk, unused.

## WHY THE COMPOSITES FAILED (keep — stops us repeating it)
Seven look rounds were rejected for a "floating outline" and a washed-out
speaker that were INVISIBLE in still boards. Causes, measured:
1. Light wrap / rim light / warm wash / offset wall shadow all TRACK the
   silhouette — they read as soft integration frozen, and as a glowing
   moving outline in motion. Deleted.
2. eq + form-shadow + vignette were darkening his face a full stop:
   cheek luma 129.7 raw → 113 composited. The clean chain cost only 5.1.
RULES: never grade/overlay the speaker's pixels; judge every look change on
30-60s of MOTION, never on a still.


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
- Composition `LucerneReview` · generator `work/lucerne/build_full.py`
- **Speed: 1.15x** (locked). Branded outro `REI_Method_Outro_v3` concatenated
  at natural speed. Finishing: `work/lucerne/finish_full.ps1`.
- 11 scenes · 616 clips · 127 overlays · 1,322 subtitle cues ·
  **43:07 natural -> 37:29 at 1.15x**
- Style **Variant D - Cinematic Paper** (theme D + PaperKit: torn-paper
  chips, marker-highlight boxes, building tick lists, giant black slates),
  over the graded ORIGINAL footage. Navy VAKit/DynKit plates for data,
  v2 navy-bar subtitles, gold price-only pops, QR bottom-left, nothing
  covers the speaker, original `audio/rei_*` beds only.
- iPad floor-plan scenes: `<take>_ipad.mp4` full-frame, head in the circular
  gold-ring bubble; sync offset +0.130s (cross-correlated, all four).
- Builder notes: the shared restart-detector was deleting real content
  because this script repeats "per square foot" constantly - now capped at
  8s AND requires a 4+ word run with a content word. Phrase anchors match a
  normalised character stream (whisper splits "$250"+",000") and snap to a
  clip start within 0.8s.

## Open items (Edmund)
- Chuan Park figures: audio says "996 of 960"; script + subtitles/displays
  use the verified **696 of 916**. Shipping with the subtitle correction -
  flag if you want that line re-recorded instead.
- The busy CDL marketing map is retired; the clean white connectivity map
  (Picture 28) is used where a map earns its place.

## Deliverables
- `LUCERNE_GRAND_FULL_1.15x_with_outro.mp4` - the full ~37:29 launch review
- `subtitles_review.txt` + `subs_manifest.json` for the REVIEW_STUDIO
  subtitle editor (round-1 review)
- Reels batch after long-form approval
- Superseded (kept for history): LOOK_VARIATIONS/, GRADE_OPTIONS/,
  BACKDROP_OPTIONS/, the LUCERNE_LOOK_DEMO_* and LUCERNE_DEMO_* files

## Decision owner
Edmund. Desk: Content. Pipeline: /video-produce.
