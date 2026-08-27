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


## ROUND-2 QA (2026-08-27) — found on the finished 36:45 render
The 22:53 render passed all ten gate rules and still shipped four defects that
only frames could show. All four are fixed and now gated (rules 11-12) or
written into `EDITING_PLAYBOOK.md` (rules 16-19):
1. **Gold figure pops landing on displays.** `$190,000` sat across a navy bar
   chart that already read `+$190k`; `570 UNITS` covered two rows of the CDL
   project-information page that already printed "570 residential units";
   `$2,300 PSF` sat on the Sora chart. Text matching could never catch these
   ($190k vs $190,000; a figure printed inside a screenshot). Now geometric:
   a gold pop overlapping a full-frame display in TIME is dropped. 3 removed.
2. **Raw screen recordings.** 17 minutes of iPad stage carried the device
   status bar, the app toolbar, a 238px black pillarbox, and the developer's
   "Strictly private and confidential. Not for circulation and sales purposes."
   banner on every page. `crop_ipad.ps1` crops all four away and sits the page
   on the plate navy. **Edmund: those deck pages are stamped not-for-
   circulation — the banner is now cropped, but the pages themselves are still
   CDL's confidential material. Confirm you are clear to publish them.**
3. **Stills sheared by the Ken Burns push.** `contain` fitted them, then the
   container push scaled the edges off-frame: the URA land-sale table lost its
   entire value column (site area, GFA, highest bid $psf), the Sora panel lost
   its LOWEST/AVERAGE/HIGHEST labels. Stills now push inside a safe inset.
4. **Section chips on document headers.** The top-centre chip parked straight
   on the centred page title it was introducing. Chips moved to the left margin.
Known and accepted: an "Ask Gemini" pill appears for a few seconds inside the
take-6 capture. It overlaps a section bar, so cropping it would cut real
content. Flag if you want that segment re-recorded.

## ROUND-3 REVIEW (2026-08-27) — Edmund's full pass on the 36:45 cut
Seven subtitle corrections, thirteen display/caption fixes, five confirmed
retakes and five new Drive assets. What changed structurally:
- **Retakes are now caught mechanically, before rendering.** `audio_check.py`
  rebuilds the audio the carved timeline will actually ship, transcribes it and
  reports adjacent repeats — ~25 minutes against a 3-hour render. It judges
  what a viewer HEARS, not what the timeline claims. Two traps it exposed:
  ffmpeg's concat demuxer silently ignores inpoint/outpoint on these files (the
  first pass analysed 81 minutes of raw takes and reported 196 phantom
  repeats), and whisper hides a fumble inside ONE stretched token, so a drop
  can land mid-fumble and leave the wrong figure in. Both are now asserted.
- **`headPos` / `headScale` were never wired.** The renderer declared and used
  them but never read them off the overlay, so every bubble placement written
  into a timeline since round 1 was silently discarded. That is why "move the
  speaker bubble" and "make it bigger" kept coming back. Fixed, and gated.
- **Fixed-pitch layout replaced with flow + auto-fit** in NavyBars and
  InfoCard. A label that wrapped used to collide with the row below — the
  "VELA BAY over the Chuan Park bar" and "overlapping of text" notes. Plates
  now scale to the height they have, at any row count or label length.
- **Image plates hug their picture** instead of floating it in a fixed box.
- Point dividers hold 3.2s minimum (two were being clipped to 0.9s), pops take
  the corner away from the head bubble, the subscribe pill sits above the
  bubble rather than over the chart, and the QR prefills the house sentence
  "Hi Coach Edmund, I'd like a Second Property Strategy Session (<Project>)" —
  decode-verified at the 210px it actually renders at.
All of it is written up as rules 20-26 in `E:\REMOTION\EDITING_PLAYBOOK.md`
and enforced by `verify_lucerne.py` (12 checks), which aborts the render.

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
