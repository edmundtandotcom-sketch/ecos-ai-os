# Campaign Index — The Serra Residences (YouTube video #5, launch review)

Date: 2026-08-24
Status: REVIEW — long-form v3 (20:41) + 11 reels (10:11) re-delivered 2026-09-01 (reel round 4)
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
- **SUPERSEDED** `SERRA_DRAFT_v1_1.15x.mp4` (21:00) + `DELIVERY_QA.jpg` —
  first full cut, 2026-08-29. Reviewed by Edmund; kept for comparison only.
  Note: this render used a bundle three days older than the component fixes
  it needed, so several defects in it were already fixed in source and had
  simply never reached the render.
- **SUPERSEDED** `SERRA_DRAFT_v2_1.15x.mp4` (20:41) — review round 2
  applied; superseded by v3 below.
- **DELIVERED** `SERRA_DRAFT_v3_1.15x.mp4` (20:41, 650 MB) +
  `DELIVERY_QA_v3.jpg`. Review round 3 (Edmund, 2026-08-30):
  - lower third raised clear of the subtitle bar (1:28)
  - ProTrend gap chart now FULL-FRAME with the pip pinned top-right
    ON the image — an explicit `headOver` opt-out from the layout
    rule, declared per plate rather than by weakening the gate (11:36)
  - harmonisation diagram given the whole frame; its three points
    follow as their own plate (13:51)
  - Neu floor-plan card 240px -> 310px, a column row merged to free
    the space (14:16)
  - the $1,865,000 moved BELOW the transaction table, table widened
    (14:29)
  - two right-hand charts held longer: 8.0->11.5s and 7.0->10.5s
  - a full-frame plate now hides the section chip (it was printing
    onto the white diagram)
  - Edmund's tennis-court photo placed at 15:06, shown at native
    682x318 rather than upscaled into softness
  Re-rendered with `work/lib/repatch.py`: the tennis image touched
  1 of 20 parts, so it cost 13 minutes instead of 100.
- v2 detail, retained for the record: +
  `DELIVERY_QA_v2.jpg` (11 frames sampled across the fixes) +
  `subtitles_review.txt` (re-indexed; timecodes are on the v2 file).
  363 clips · 155 displays · 344 subtitle cues. Edmund's full v1 review
  applied:
  - **Layout is solved, not nominated.** `work/lib/layout_gate.py` places the
    head bubble geometrically and FAILS THE BUILD on any overlap. The section
    chip no longer sits under the channel logo; plate copy no longer runs
    under the subtitle bar; the QR no longer covers the CTA card.
  - **The Serra QR was Amberwood's**, byte for byte. Regenerated and
    decode-verified at its 210px display size.
  - **Nine bar/line charts** for the gains and rentals that were caption-only
    — Pavilion 11, The Ansley, Zedge, 8 Bassein, Neu — plus a real x/y psf
    chart for Neu across the period.
  - **Three-ring OCR/RCR/CCR diagram** with the prices counting up.
  - **Six of Edmund's assets placed**: the ProTrend gap chart (held, head
    pinned top-right), the Peck Hay and Vela Bay articles, the GFA
    harmonisation diagram, the Neu floor plan under its compare column, and
    the Neu transaction table with the price animating over it.
  - **Nine subtitle corrections** applied verbatim, plus two more of the same
    phrase found by sweep ("Neu @ Novena" throughout, "within 1KM",
    "being in CCR", "harmonized").
  - **Nine clip removals**, converted from delivered timecodes to source with
    `work/lib/final_to_src.py` — never by eye.
  - **Launch dates corrected on the display**: preview 2 Oct, launch day
    17 Oct, flagged "UPDATED · LATEST DATES" over what the speaker says.
  - **Subscribe/CTA cadence** raised from 3 prompts to 19 across the runtime.
  - All audio is synthesised in-house (`work/enbloc/make_music.py`); no code
    path anywhere still references the track YouTube claimed.
  - CLOSED: tennis-court image — Edmund supplied one 2026-08-30; it is in
    v3 at 15:06.
- **PILOT DELIVERED** `REELS/SERRA_REEL_01_THE_NEIGHBOUR_THAT_DIDNT_PAY.mp4`
  (1:01, 1080x1920, -15.0 LUFS / LRA 2.0 LU) + `REELS/REEL01_QA.jpg`.
  Topic list derived from the 337-sentence transcript dump; 12 candidates cut
  to 11 on Edmund's "quality over count" (09 ONLY 13% FREEHOLD folded into 11
  SCARCITY - a statistic, not a teaching point).
  NEW LOOK - skin `serraPrime` in `src/reelSkin.ts`: gold leads, cyan affirms,
  vermilion RESERVED for risk beats; -0.8 counter-tilt, new `ring` card
  treatment and new `bracket` stat mark that echoes the long-form GapBar.
  Pipeline: `work/serra/build_reels.py` (machinery) + `reels_serra.py`
  (specs) + `emit_reels.py` + `render_all_reels.ps1`, rendered from the
  pre-built bundle with `--public-dir=public_serra`.
  Round 2 (Edmund, 2026-08-31): document plates now ZOOM to the sale-price /
  psf columns rather than showing the whole row, cropped SQUARE, and the crop
  is chosen per beat from the words he is saying (`img(..., zooms=[...])`);
  number captions are set larger than the words around them.
  Round 3 (Edmund, 2026-08-31): the b-roll stretch replaced with his three
  market assets (mkt_a/b/c) plus a NEW animated `TrendPlate` - a date-vs-price
  line that draws across the shot, built from the URA Property Price Index
  series MEASURED out of the pixels of his own chart and calibrated against
  its printed axis (extracted endpoint 188.2 vs printed 188.6). Caption fix
  at 0:57 ("and harmonized?").
  CARE: that index rose ~31% over 1Q2018-4Q2022. Edmund's spoken "+52%" is
  NEW-LAUNCH prices, a different series. The chart therefore carries NO
  percentage and the +52% stat was re-anchored one beat earlier so the two
  are never on screen together appearing to label each other.
- **LONG-FORM v5 DELIVERED** (2026-09-04) `SERRA_DRAFT_v5_1.15x.mp4`,
  20:40, 1920x1080 h264/aac, safe outro. Round 5 of Edmund's notes — 22 items,
  14 of them about WHEN something was on screen rather than how it looked.
  All six subtitle corrections VERIFIED in the delivered file by frame grab.
  - Icon slams WITHDRAWN. He flagged three as "came on too early"; they were
    8.2s / 3.7s / 4.7s early because the placement solver allowed drift in
    BOTH directions. Drift is now asymmetric (a label may lag the words,
    never lead them) — but the badges are gone anyway, because every factor
    already had a real display at the right moment.
  - Plate durations are now DERIVED from the speech, not hand-set. Six notes
    said "sync with speaker until we finish explaining".
  - InfoCard bands separated (headline ended y292, content started y296) and
    the PIP went 127px -> 229px by reserving the corner and capping the text
    above it. When the frame is full, the speaker is not what yields.
  - "5:49 medical video cut off" was NOT a cut: the cue dangled on "I" for
    four seconds. Rebalanced.
  - Two schools BOXED in the list panel of his own screenshot rather than
    pinned on the map — the map carries a dozen school glyphs and nothing
    identifies which is which. Accurate beats authoritative-looking.
  ZERO plate-on-plate overlaps (v4 had one).
  RENDER INCIDENT: three parts failed in two different ways — a Google-font
  fetch hitting ERR_NO_BUFFER_SPACE, and ffmpeg killed mid-encode — while
  free RAM read 7-12 GB throughout. Cause: the QA stills harness had leaked
  **24 orphan node processes** across three batches, holding Chrome instances
  and network handles. Cleared; all three parts then succeeded on retry. The
  stills harness now reaps after itself. Playbook rules 78-85.
  STILL OPEN: 5:31 "double mentioned of more foot" — the cue reads "Food,
  community spaces, more foot traffic in the area" ONCE and no duplicate was
  found. Needs Edmund to say where he saw it.
- **LONG-FORM v4 DELIVERED** (2026-09-04) `SERRA_DRAFT_v4_1.15x.mp4`,
  20:40, 1920x1080 h264/aac, safe outro. Identical duration and format
  to v3 — a like-for-like replacement. Render 1h42m, 20 parts, zero
  failures. MEASURED before/after on the same instrumentation:
  | | v3 | v4 |
  |---|---|---|
  | silences @-40dB | 95 | **19** (-80%) |
  | dead plate time | 114s | **32s** (-72%) |
  | cuts/min | 14.4 | 14.1 |
  | LRA | 2.4 | 2.4 |
  | LUFS | -16.0 | -15.9 |
  HONEST LIMIT: the cut rate did NOT fall. Rule 52 says building the
  annotation layer should let it drop, but cuts/min is a property of the
  CLIP list and this pass only added overlays. Bringing 14.1 down toward
  the field's 3-11 needs a re-cut, which is a separate job.
  43% -> 47% CORRECTED AND VERIFIED IN THE DELIVERED FILE at 11:24.
  This had been reported as "fixed in source, awaiting the next render" and
  it was NOT — the source fix only turned whisper's mis-hearing ("only 3%")
  into 43%, never into 47%. It survived four review rounds because TWO
  different 43%-looking numbers sit within 30 seconds of each other: at
  10:51 "RCR the middle ring jumped 43%" is CORRECT (a growth figure), and
  at 11:24 the same 43% is wrong (the CCR-over-RCR premium). Worse, the
  GapBar plate on screen at 11:24 already read "47% apart", so v3 had the
  graphic and the subtitle contradicting each other in the same frame.
  $900 over an RCR of ~$1,900 = 47.4%; his ProTrend sheet says $898/46.82%.
  Fixed in the generator (with the trap named in a comment) and re-rendered
  via a TARGETED repatch: the cue occupies frames 23599-23796, entirely
  inside part 11 of 20, so this cost 5 minutes rather than 1h42m.
  `render_serra.ps1 -RepatchParts 11` — an explicit, logged override of the
  stale-parts gate, not a weakening of it.
  CH.8/CH.9 retrofit detail: v3 was
  built one day before the CH.8 deck-behind-speaker teardown and the CH.9
  ten-channel sweep landed. Measured v3 first with `work/study/analyze.py`
  against that field: **14.4 cuts/min (fastest of the ten), 367s (30%) of
  static plate time, 95 silences at -40dB** against 0-2 for the analytical
  leaders. LRA 2.4 is the best in the field and was left alone.
  Three engine changes, all ADDITIVE:
  - The 20 CH.8/CH.9 devices were built against `ProjectLong`; every video we
    ship renders on `HDBVideo`, so the new grammar was unreachable. Ported
    into HDBVideo namespaced `w*` — four CH.9 names (`timeline`, `article`,
    `agenda`, `social`) already meant something else there and a bare port
    would have silently rebound four working plate kinds.
  - `FactSlate` already staggered its facts — by SIX FRAMES, so the plate
    resolved in a second and then held for seven doing nothing. Optional
    `factTimes` / `sideRowTimes` now spread the reveal across the hold;
    omitted, they fall back to the old stagger, so every delivered timeline
    renders exactly as it shipped.
  - `MUSIC_BASE` 0.07 -> 0.19. On a -17.4 LUFS bed, 0.07 lands near -40 LUFS:
    playing but masking nothing. Measured sweep of added gain vs silences:
    +0.00 -> 25, +0.06 -> 11, +0.10 -> 8, +0.14 -> 4, with integrated
    loudness moving 0.1 LU across the whole range.
  16 devices added, 8 dropped by the placement gate — those moments already
  had a `qcard` or `social` bar treating them, and a second treatment would
  have covered the first. Pass: `work/serra/upgrade_v11.py` (idempotent).
  TWO GATE BUGS FOUND AND FIXED DURING THE BUILD, both worth remembering:
  sampling a candidate moment at ONE INSTANT said 11 of 13 were free, while
  sampling across each device's SPAN said 17 of 24 collided; and a purely
  geometric solve put the 16-year land story at 1:36, half a minute before
  the land is mentioned. Placement is now bounded by a per-kind drift.
  `render_serra.ps1` gained three pre-flight gates: bundle freshness, right
  public dir, and STALE PARTS — the render is resumable, so 20 v3 parts on
  disk would have been silently stitched into a v4 cut.
- **YOUTUBE UPLOAD KIT** (2026-09-04) `YOUTUBE_UPLOAD_KIT.md` - title (3
  options), thumbnail text + art direction (3 options), full description
  with 17 chapters, upload settings and the pinned comment. Every
  timestamp read off the DELIVERED 1.15x file, not the timeline.
  The copy quotes the CCR-RCR gap in DOLLARS ($900 psf then, $487 now)
  and never the percentage, because v3 still carries the 43%/47% defect
  at 11:24 - see OPEN DEFECT below.
- **REEL BATCH RE-DELIVERED** (2026-09-01) - all 11 reels re-rendered after

  round 4, 10:11 total, in `REELS/` + `REELS_R4_QA.jpg` (22 QA stills, one

  per change). Zero render failures; batch loudness spread **0.2 LU**

  (-15.1 to -14.9), all 1080x1920 h264/aac.

  | # | Reel | Length |

  |---|---|---|

  | 01 | The neighbour that didn't pay | 1:02 |

  | 02 | The price gap | 1:03 |

  | 03 | Volume, not location | 0:31 |

  | 04 | What the old freehold paid | 1:07 |

  | 05 | Smaller on paper, same to live in | 1:06 |

  | 06 | The hospital is the rental story | 0:44 |

  | 07 | Don't buy this for yield | 0:31 |

  | 08 | The foreign money isn't coming | 0:50 |

  | 10 | Three buyers, one should slow down | 1:01 |

  | 11 | Sixteen years on the land | 1:05 |

  | 12 | The honest scorecard | 1:06 |

  Round 4 (Edmund, 2026-09-01): 30 notes across eight reels - 24 caption

  corrections, two clip removals, one held display, one missing figure and

  three plate swaps. Each correction is verified by ASSERTING on the emitted

  cue text (the fix present AND the garble gone), not by eye.

  - "8 Bassein" had been failing silently for three rounds: whisper splits the

    name and puts a CONTINUATION HYPHEN on the back half ("8 -Basin", "both

    -proof"), which `_bare()` never stripped, so the phrase fix matched

    nothing. It is now also ONE caption token, so a line break can no longer

    fall between the 8 and the name (it was doing so in reels 1, 3, 6, 10, 12).

  - "$1,485 sf" was a CLASS, not a one-off: whisper carries the $ from a psf

    figure onto the next number, pricing a floor area. All eight scenes swept;

    three hits, all in reel 04. The cases where $ is correct were left alone.

  - Reel 04's cut-off at 0:41 was measurable - speech ran to 41.94, the cut

    landed at 41.99. `SEG_TAIL` now gives EVERY segment end 0.30s through

    `hold_after()`, which can only extend into measured silence.

  - Fixed beyond the literal notes, same error already ruled on: "both prove"

    in reel 10 as well as 12; "yield is" in reel 07 as well as 12.

  - Two of the three assets Edmund linked were ALREADY in the library,

    byte-identical (Picture 46 = p46, Picture 5 = p05) - referenced, not

    re-imported. Only the pool/tower screenshot was new; it is cropped to its

    bottom-right square because the render's sky is a blown-out WHITE block

    top-left and a square card fills from the top.

  - Spellings used: Tan Tock Seng Hospital, Mount Elizabeth Novena, 8 Bassein.

  CAUGHT BY THE QA STILLS, BEFORE THE RENDER: a re-bundle without

  `--public-dir=public_serra` embedded the shared 16.8 GB public/ (a 64 GB

  bundle). Deck pages exist in both folders and resolved; the new plates and

  EVERY generated crop 404'd. `render_all_reels.ps1` now refuses to start on

  a stale bundle OR a bundle carrying the wrong public dir.

  NOTE for future rounds: composition ids are POSITIONAL (`SerraReel${i+1}`)

  and this campaign has no reel 09, so SerraReel11 is reel 12 and SerraReel12

  does not exist. Derive the id from the manifest, never the reel number.- **REEL BATCH DELIVERED** (2026-08-31) - 11 reels, 9:59 total, in `REELS/`
  + `ALL_REELS_QA.jpg`. All 1080x1920 h264/aac; batch loudness spread
  0.1 LU (-14.9 to -15.0), well inside the 2.5 dB rule:
  | # | Reel | Length |
  |---|---|---|
  | 01 | The neighbour that didn't pay | 1:01 |
  | 02 | The price gap | 1:01 |
  | 03 | Volume, not location | 0:30 |
  | 04 | What the old freehold paid | 1:08 |
  | 05 | Smaller on paper, same to live in | 1:06 |
  | 06 | The hospital is the rental story | 0:42 |
  | 07 | Don't buy this for yield | 0:30 |
  | 08 | The foreign money isn't coming | 0:49 |
  | 10 | Three buyers, one should slow down | 0:59 |
  | 11 | Sixteen years on the land | 1:03 |
  | 12 | The honest scorecard | 1:04 |
  Twelve candidates cut to eleven on "quality over count".
  CORRECTIONS CARRIED IN THE REELS (both from opening the source sheets):
  - Reel 02 caption reads **47%**, not the spoken "3%". His ProTrend sheet
    (p31, on screen in the same shot) reads $898 / 46.82%. The LONG-FORM
    still says 43% at 11:24 - that figure is the RCR growth number, a
    different series - and is fixed in source awaiting its next render.
  - Reel 10 OMITS "only 13% of all condos are freehold". His own slide (p02)
    reads freehold = 49% of condo stock; 13% is freehold AND near an MRT.
    Scarcity rests on the launch drought and the land story instead.
  - p25 was pulled off the "71% Singaporean" beat in reel 08: it is a
    profitable-transactions sheet and carries no buyer data at all.
- **OPEN DEFECT (long-form v3, 11:24):** the subtitle reads "a huge gap, 43%
  more expensive". The correct figure from Edmund's own ProTrend chart (p31,
  on screen at 11:36) is 46.82%, i.e. 47%. Introduced by a correction that
  guessed at a misspoken number. One cue; folded into the next long-form
  render rather than re-rendering 100 minutes for one word.
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
