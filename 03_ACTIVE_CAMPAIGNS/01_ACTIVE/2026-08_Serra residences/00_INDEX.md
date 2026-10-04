# Campaign Index — The Serra Residences (YouTube video #5, launch review)

Date: 2026-08-24
Status: REVISION — v2 rendering 2026-08-29 (Edmund's full v1 review applied)
Deadline: publish before Preview day. DATES REVISED (Edmund, 2026-08-29):
preview 2 Oct, launch day 17 Oct — supersedes the 19 Sep / 3 Oct dates
spoken in the recording, which the on-screen timeline now corrects.

## Objective
Full pre-launch review of The Serra Residences (Far East Organization, D11
Novena, freehold, single 28-storey tower, 133 units). The spine of the video
is the honest question, not the marketing: **Serra's location is obviously
good — so why did Neu at Novena, next door, with almost the same story,
barely move in six years?** Answer arrives as the Price Gap number.

Structure: cold-open (Neu's flat six years) → agenda → quick facts + the
2010 $122m land story → scarcity (7 years / 18 years) → 5 location pillars
(MRT · HealthCity · schools · retail · 2 Moulmein Rd) → what the neighbours
actually paid their owners (Pavilion 11 · Ansley · Zedge vs 8 Bassein · Neu)
→ thin-volume risk → **Price Gap** → harmonisation (livable sf) → 3 buyer
types → risks (ABSD-capped foreign pool · 2.5% yield) → scorecard → CTA.

## Source of record
- **Spoken script (the guide for the entire video):**
  `Raw Assets/Recording-Serra Residences.docx` — this is the teleprompter
  take-by-take record.
- Research script + picture cues: `Raw Assets/Serra Aug 2026 Script.docx`
  (cites Picture 1–46, mapped in `Raw Assets/Supporting Assets/`)
- Evidence images: 46 supporting assets (transaction/rental tables, PropNex
  charts, URA/OneMap maps, floor plan, project renders) → copied to
  `E:\REMOTION\public\serra\pics\p01..p46.png`
- PDFs: factsheet, location map, e-book, ICB deck
- Footage: 8 talking-head scenes, 3 angles each
  - `N.mp4` = front master (1080p, best audio) → `public/footage/serra/N.mp4`
  - `N-Webcam.mp4` = 3/4 side angle → `NB.mp4`
  - `N-DSLR.mp4` = 720p duplicate of the front angle (unused)
  - No iPad/presentation capture this time — the display layer is built,
    not recorded.

## Production (runtime local: E:\REMOTION)
- Composition `SerraReview` · generator `work/serra/`
- **Style Variant F — "Prime Editorial"** (new). Deep ink ground, champagne
  gold rules, electric cyan as the second data colour; reads like a
  financial broadsheet on air. Deliberately different from Amberwood
  (Variant C, Clean White) and Lucerne (Variant D, Cinematic Paper).
- **PrimeKit (component library v9)** — every element ANIMATES ITS CONTENT
  rather than fading a static card in (the "visual effects are still
  lacking" note from Amberwood):
  | Component | Job |
  |---|---|
  | `Odometer` | money/psf/percent that rolls up |
  | `GapBar` | **hero graphic** — two price columns and a bracket that visibly CLOSES from 2019's $900 gap to today's ~$487 |
  | `AgendaBoard` | numbered agenda, rows wipe in behind a travelling rule |
  | `FactSlate` | spec sheet — hairline grid, staggered small-caps rows |
  | `ProportionDots` | 100 dots, 13 light up — "only 13% are freehold" |
  | `DateRail` | preview / booking day markers dropping onto a rail |
  | `SplitCompare` | Neu vs Serra, animated divider, verdict chip |
  | `NumberSlam` | one giant sparse number, chromatic impact |
  | `TickerBug` | persistent editorial section bug |
  | `LightLeak` | anamorphic streak transition |
- QA harness: `PrimeLab` composition (8 slots, one still per element)
- **Speaker grade S5 (locked)** — the raw footage was measurably washed out
  (p99 only 180/255, blacks lifted to ~30, saturation spread 14.6). S5
  recovers the black and white points, warms the skin, neutralises the
  magenta cast on the wall, adds a gentle S-curve, micro-sharpen and a soft
  vignette. Face reads 154/135/109 vs 129/114/104 raw; p99 → 235.
  Chain in `work/serra/grade.sh`.
- **Studio composite** — `work/serra/build_plate.py` + `compose_motion.py`
  (Lucerne v2 chain, extended). Halo control: post-key erosion + gamma-1.25
  alpha hardening (the old gamma-0.72 lift widened the soft edge), despill,
  then wall shadow → contact shadow → directional rim → light wrap sampled
  from the real plate → form shadow → warm key wash → grain → vignette.
  Verified clean on a 3× hair-edge crop: no green fringe, no white halo.

## Locked decisions (Edmund, 2026-08-24)
1. **Speed — 1.15×.**
2. **No studio backdrop.** The composite was rebuilt to fix the halo (direct
   RVM alpha, no green round-trip, edge colour extension, no light wrap or
   rim) and reviewed twice; Edmund's call is that it still doesn't work for
   this video. Ships on the ORIGINAL room. The compositor stays in
   `work/serra/composite_v2.py` for future use.
3. **Grade — N6 "natural".** S5 was rejected as too yellow and too bright:
   it lifted the white point (face 129 → 154) and pushed warmth into the
   highlights. N6 keeps the original exposure exactly (face 129, same as
   untouched), gives only the deep shadows some depth, and raises colour so
   the skin isn't pale (spread 27 → 37). No cast.
4. **Source — the DSLR camera feed, not the program capture.** `N-DSLR.mp4`
   is 720p but carries ~4× the fine detail of the 1080p `N.mp4`
   (laplacian 35.6 vs 8.0, same frame): `N.mp4` is a ~2.6 Mbps re-encode of
   an already-downscaled feed. Masters are `NS.mp4` — DSLR feed upscaled
   ONCE with lanczos, sharpened ONCE, then graded N6. Audio from the same
   file, so nothing needs syncing.
   *Shoot fix for next time:* the ZV-E10's USB streaming is capped at
   720p30 by Sony; capture over micro-HDMI instead and raise the OBS
   recording bitrate.

## Deliverables
- **DELIVERED** `LOOK_TEST/` — five 60s variation clips (ungraded reference ·
  graded original room · three studio composites) + `LOOK_GRID.jpg`,
  `GRADE_BEFORE_AFTER.jpg`, `CUTOUT_EDGE_3x_ZOOM.jpg`, `README.md`
- **DELIVERED** `SERRA_DEMO_2MIN_1.1x.mp4` (1:48) /
  `SERRA_DEMO_2MIN_1.15x.mp4` (1:43) + `DEMO_README.md`.
  Known in this build, already fixed in the source and queued for a
  corrected re-render: the "6 YEARS" slam repeated the spoken line instead
  of adding to it, and "per square foot" printed long in the subtitles
  instead of "psf".
- **DELIVERED** `SERRA_DRAFT_v1_1.15x.mp4` — 21:00, full script, all 8 takes.
  366 clips · 133 displays · 345 subtitle cues. Review against
  `subtitles_review.txt` (indexed, timecodes are on the 1.15x file).
- **IN RENDER** `SERRA_DRAFT_v2_1.15x.mp4` — Edmund's full review of v1
  applied (2026-08-29). 363 clips · 155 displays · 344 subtitle cues,
  ~20:24 at 1.15x. What changed:
  - **Layout is now solved, not nominated.** `work/lib/layout_gate.py` places
    the head bubble geometrically and fails the build on any overlap. The
    section chip no longer sits under the channel logo; plate copy no longer
    runs under the subtitle bar; the QR no longer covers the CTA card.
  - **The Serra QR was Amberwood's**, byte for byte. Regenerated and
    decode-verified at its 210px display size.
  - **Nine bar/line charts added** for the gains and rentals that were
    caption-only — Pavilion 11, The Ansley, Zedge, 8 Bassein and Neu, plus
    a real x/y psf chart for Neu across the period.
  - **Three-ring OCR/RCR/CCR diagram** with the prices counting up.
  - **Six of Edmund's assets placed**: the ProTrend gap chart (held, head
    pinned top-right), the Peck Hay and Vela Bay articles, the GFA
    harmonisation diagram, the Neu floor plan under its compare column, and
    the Neu transaction table with the price animating over it.
  - **Nine subtitle corrections** applied verbatim ("Neu @ Novena" throughout,
    "within 1KM", "being in CCR", "harmonized").
  - **Nine clip removals** converted from delivered timecodes to source with
    `work/lib/final_to_src.py`, never by eye.
  - **Launch dates corrected on the display** — preview 2 Oct, launch day
    17 Oct, flagged "UPDATED · LATEST DATES" over what the speaker says.
  - **Subscribe/CTA cadence** raised from 3 prompts to 19 across the runtime.
  - Outstanding: a tennis-court stock image for 15:28. Nothing suitable
    exists in the deck or the asset library and I will not pull an
    unlicensed web image into a client video — Edmund to supply one.
- Reels batch after long-form approval
- Upload kit on request

## Runtime notes (E:\REMOTION)
- Serra bundles from the slim `public_serra/` (1 GB) rather than the shared
  `public/` (16.8 GB). Render from the pre-built bundle by passing
  `"E:/REMOTION/build"` with FORWARD slashes — backslashes make Remotion
  re-bundle and re-copy the public dir. Both rules are in the playbook.
- Grading of takes 2–8 and transcription of takes 3–8 are running; the
  corrected demo re-render is queued behind them (`work/serra/demo_v2.sh`).

## Decision owner
Edmund. Desk: Content. Pipeline: /video-produce.
