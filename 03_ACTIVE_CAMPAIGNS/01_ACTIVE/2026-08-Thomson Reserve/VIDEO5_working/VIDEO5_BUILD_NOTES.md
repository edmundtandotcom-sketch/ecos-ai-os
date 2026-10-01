# THE LAYOUT COMPARISON — build notes
## State at 23 Sep 2026. Nothing rendered yet.

Scope: **2- and 3-bedroom only.** 4-bed and 5-bed dropped (Edmund, 23 Sep).

## Where everything lives

**Documents and the deck live here, in the campaign folder.** The Remotion
build stays on `E:\REMOTION\` because the renderer needs it there.

| File | What it is |
|---|---|
| `VIDEO5_SCRIPT_v3.md` | **the teleprompter script.** Follows the comparison deck's own 17-slide order, with 13 new slides interleaved. Supersedes v1 and v2 |
| `VIDEO5_teleprompter_v1.pptx` | **30-slide teleprompter deck.** Narration in the speaker notes on every slide. Drag into Drive to convert to Google Slides — notes survive the conversion |
| `VIDEO5_COMPARISON_DATA.md` | PropNex / official figures, every one page-cited |
| `VIDEO5_DECK_AUDIT.md` | audit of the Google Slides comparison deck |
| `VIDEO5_STACK_FACING.md` | block/stack × distance-map cross-reference |
| `VIDEO5_BRIEF.md` | the original 23 Sep brief. **Two claims in it are wrong — see the next section.** Kept for provenance, not for re-import |
| `VIDEO5_ref_comparison_deck_24Sep.pdf` | snapshot of `Thomson Reserve floorplans comparison Sep 2026` as at 24 Sep 2026. The live Google Slides file keeps changing; this is the version the script and the audit were written against |
| `VIDEO5_BUILD_NOTES.md` | this file |

**Still on `E:\REMOTION\` and staying there:**

| Path | Why |
|---|---|
| `work/thomson_compare/` | rasterised PDF pages, extracted artwork, `build_teleprompter.py`, and the superseded `SCRIPT_v1.md` / `SCRIPT_v2.md` |
| `work/thomson_compare/edmund_slides_v2/` | the deck's page renders at 140 and 200 dpi, and the PowerPoint export used to check all 30 frames |
| `public_thomson_reserve/compare/plans/` | **20 named plan assets + MANIFEST.json.** The Remotion composition loads them from here at render time — do not move them |

`build_teleprompter.py` regenerates the deck. If it and `VIDEO5_SCRIPT_v3.md`
ever disagree, **the script wins** and the builder gets regenerated from it.

## Corrections to BRIEF.md — do not re-import from it

1. **The red/green shading on `TF p34–p37` is not a liveable-area measurement.**
   The brief calls it "the single most persuasive frame in the deck" and makes it
   the video's spine. Read across p35 and p36, red covers bedrooms and master
   suites; it is a "compare these rooms" highlight with **no legend anywhere in
   the deck**. It can be shown and talked through. **No percentage can be derived
   from it.** The efficiency spine is now Edmund's own room-by-room + aircon-ledge
   method instead.
2. **The 10 m on `TF p13` is a boundary setback, not a block-to-block gap.**
   It runs from BLK 11 stack 50 east to the site edge. The v1 script line
   "ten metres, that's you and your neighbour's living room" is wrong and must
   not be recorded. Tightest genuine block-to-block on the site is **26 m,
   BLK 9 #41 ↔ BLK 3 #15/16**.
3. Brief says BPS1 is "BLK 1 #03-04". Confirmed correct — the `#02-04` seen on
   the Tri-Force slide is the facade-fin note, not the stack range.

## Assets — what we have

All plan artwork extracted as **clean line art**: the deck's colour shading and
its red room-dimension numbers are vector overlays drawn on top, so the embedded
rasters come out bare. That is what we want — we draw our own dimension callouts
and our own shading with our own reveal timing, over the developer's drawing.

`tr_bps1_full.png` and `tr_cp1_full.png` keep the developer's **numbered callout
pins and the callout list** baked in, so the numbering stays theirs per the
standing rule. Only the reveal timing is ours.

### Resolution flags

| Asset | Size | Note |
|---|---|---|
| `js_775.png` | 465×497 | **Lowest.** Cannot be improved by re-rasterising — that is the embedded source resolution. Used in scenes 7 and 8. Either source a better JadeScape 775 plan or compose it at reduced size |
| `amo_743.png` | 566×689 | acceptable at half-frame |
| `amo_958.png` | 706×575 | acceptable |
| `amo_1141.png` | 761×583 | acceptable |
| `amo_614.png` | 573×637 | only needed if scene 6 keeps the AMO 614 beat |

### `siteplan_distances.png` — the one real build problem

The red distance arrows and their labels are **baked into the raster**. Scene 12
calls for revealing the block-to-block spans first and the boundary setbacks
second, in two colours. That cannot be done from this image.

Three options, in order of preference:
1. **Use the clean site plan** from `TR_Unit_Mix_Site_Floor_Plans.pdf` and draw
   all arrows ourselves as SVG. Full control, matches the design system, and
   lets us colour-separate block-to-block from boundary. Arrow endpoints are all
   identified in `STACK_FACING.md` §2. **Recommended.**
2. Crop-reveal the baked image region by region. Cheap, but the two kinds of
   distance stay the same colour, which is the exact point of the scene.
3. Show it whole and talk over it. Weakest.

## Frame rules — 16:9, every board

Locked 26 Sep from the approved mock (`E:\REMOTION\work	homson_compare\_mock_board_A2_16x9_pip.png`).

| Zone | Rule |
|---|---|
| Content | stops at **y = 850**. Plan cards 130–600, ledgers 620–780, verdict at 800 |
| Subtitles | own **y 930–1040**, **x 160–1560**. 46 px Barlow Condensed, cream, gold hot words, dark pill. Two lines stack inside the band |
| PiP | bottom-right, **260 px circle** centred (1740, 880), gold ring. Nothing else enters the 300×300 corner |
| PiP crop | **loose** — face in the upper-middle third of the circle with air around it. Not filling the circle. Edmund, 26 Sep |
| Type floor | 22 px minimum; anything carrying a number 26 px or larger; verdict 44 |
| Right ledger | capped at x ≤ 1560 so no transaction line runs under the PiP |
| Plans | competitor plans are **not to scale** with TR's and can't be — both developers print "not drawn to scale". Show a **size bar** under the cards instead (TR vs neighbour, ledge deduction hatched) |

Any board that breaks a zone rule fails the check-board gate before render.

## Script rules the composition enforces

- `[BOARD]` runs never exceed **45 s** without a `[FULL]` or `[BOARD+]` cut — longest in v5 is 22 s
- Micro-CTA gap never over **4 min** in any assembly — all four cuts checked in v5
- Every grid board carries `ESTIMATE — PRICE LIST NOT RELEASED`

## Competitor plans — all clean (26 Sep)

Edmund: build without the PropNex watermark. **Done for all nine.** Files are
`public_thomson_reserve/compare/plans/*_clean.png`; MANIFEST.json records the
method and source for each. **Use the `_clean` file on every board.**

| Plan | Status | How |
|---|---|---|
| amo_614 · 678 · 743 · 958 · 1141 | **CLEAN** | de-watermarked in place: black top-hat k=17 keeps thin features and drops the wide watermark; L<0.72 drops the watermark-toned letter edges. AMO linework is dark, so the tone cut is safe |
| js_1152 | **CLEAN** | same method; its lines are dark enough |
| js_646 · js_775 · js_904 | **CLEAN — re-sourced** | the PropNex pastes could not be cleaned (watermark tone = line tone). Replaced with the developer's own plans from the JadeScape floor-plan brochure at jadescape.propertybook.sg (B1-646, B3-775, C1a-904, 800×600 JPG, no mark), cropped, 2× upsampled, top-hat line art. Source JPGs kept as `js_*_src_propertybook.jpg` |

Also on disk, not used: `work/thomson_compare/js_src/` — the full 31-page
JadeScape brochure PDF and its page extracts (1389 px spreads, 2–4 plans each,
so lower per-plan resolution than the JPGs) plus `C1b-904` (the mirrored 904).

**Resolution after re-sourcing:** js_646 1080×1200, js_775 1116×1200, js_904
1368×1200 (post-upsample). Adequate for a half-frame card at 1080p. The 775 is
no longer the weakest plan we hold.

**On-board credit:** competitor plans carry a one-line source in the footer —
`Floor plan: JadeScape (Qingjian) brochure` / `Floor plan: AMO Residence
brochure via PropNex` — same place the TR boards cite the PDF page. Not a
watermark; a citation, consistent with the "every figure traces" rule.

## Display library (28 Sep)

Nine templates, rendered on real assets in `../VIDEO5_displays/`, keyed to the
script line by line in `../VIDEO5_SHOT_LIST.md`. Generator is
`make_displays.py` (also on E: in `work/thomson_compare/`). It writes:
- `compare/site/siteplan_clean_notext.png` — TriForce p12 with the slide text
  masked in the sampled background colour, cropped to the site outline
- `compare/site/stack_coords.json` — pixel position of every stack in blocks
  1/3/5/7/9/11, read off a gridded render; `P()` maps grid → cropped-image px
- `compare/views/photos/view1..8.png` + `INDEX.json` — the eight developer
  drone photos cropped out of TF p25–28, with direction and level range;
  `keymap_p25..28.png` show where each was shot from

**Stack → face is validated by two developer callouts** (B1 #07 "pool-facing"
= Blk 1 west; DPS1 #22 "GCB/Windsor/MacRitchie" = Blk 5 south, which TF p26–27
place SW). On camera it is still "read off their site plan — confirm at the
gallery."

**Reconfig template (R1–R3)** — `make_reconfig.py`. Element coordinates are read off `plan_p12.png` with a gridded crop (`_dps1_grid.png`); the same approach gives the 1,152's hackable wall in ten minutes.

**Video 2 assets still to stage:** tr_775, tr_1238, tr_1367, tr_1485, tr_1808
(all from FP/TF extracts already rendered), js_1259 and amo_1292 (from the
comparison deck, de-watermark), js_1647 and js_2099 (TF p36/p37). Listed at
the end of the shot list.



## DELIVERED — THOMSON_LAYOUTS_PART1_v1 (28 Sep 2026)

`THOMSON_LAYOUTS_PART1_v1.mp4` in the campaign folder (byte-identical to
`E:\REMOTION\out\THOMSON_LAYOUTS_PART1_v1_1.15x.mp4`), chapters beside it.
25:09 · 1920x1080 · 34.5 fps (30 x 1.15) · 48 kHz · -16.1 LUFS · 481 MB.

**Measured, not assumed:** G0 every anchor matched · G1 caps on the speech clock ·
G2 51,595 master frames = sum of measured segments, A/V +0.000 s · G3 speech at
60/900/1600 s (-17.5 dBFS) · sync +0.000 s at all eight verify points · render took
~7 min (light composition), delivery pass 5 min.

**Freeze verdict — verify_v5's whole-frame freezedetect said FAIL (765 stretches).
That test is meaningless for this show (CH.14 addendum) and it was wrong here too:**
the bubble-crop test flags the curtain on full-frame shots (crop lands beside him),
and a static plan card is identical frames by design. The valid proof, run on three
real full-frame speaker shots picked from SHOTS: per-frame face-region diffs
delivered vs master are identical (2.79/2.77, 4.94/5.00, 5.50/5.43; longest
identical run 1–2 in both). **The render holds no frames.** Test lives in this
session's transcript; worth scripting as `freeze_proof.py` next time.

**What was corrected on screen vs what he said** (captions show his words; boards
carry the audited figure): 28 m not 29 · $2,966 not $2,996 · $1.767 M not $1.75 M ·
$2.196 M at $3,000 not $2.269 M · $2.39 M not $2.239 M · 1,141 not 1,142 · the 1,152
is the same size as JadeScape's, not 97 sqft bigger · Block 1 "no block faces it",
not "40 m".

**Chapters (from SPANS, delivered clock):** 0:00 OPEN · 1:31 SETUP · 1:52 A1 592 ·
6:30 A2 678 · 10:06 A3 732 · 13:54 A4 775 · 14:55 A5 947 · 17:45 A6 1055 ·
20:55 A7 1152 · 24:25 CLOSE.

**Not in this cut:** the developer-callout pin reveals (L4 shows the pins but does not
animate them) and the outro carries Part 2's REI Method card unchanged. Part 2 (4 & 5
bed, footage `Full Layouts 2a/2b/2c`) is not built; eight plan assets still to extract.

## BUILD — PART 1 (2 & 3 bedroom), recorded 28 Sep, pipeline 28 Sep

**Footage:** `Full Layouts 1a/1b/1c-DSLR.mp4` (18:41 / 7:48 / 5:32, 1280x720p30,
six AAC tracks — **voice is track 0**, the rest silent or secondary). Copied to
`E:\REMOTION\work	homson_compareootage\P11a/b/c.mp4`. 1a = OPEN, set-up,
A1–A4; 1b = A5–A6; 1c = A7 + CLOSE. Edmund read v6 (his own draft + facing).
`Full Layouts 2a/2b/2c` are Part 2 (4 & 5 bed) — not built yet.

**Pipeline** (`E:\REMOTION\work	homson_compare\`, mirrors the Layouts build):

| Step | File | Gate |
|---|---|---|
| transcribe | `transcribe_p1.py` → `P11a/b/c.json` | faster_whisper small int8, beam 5, no conditioning — the Part 2 settings. **Launch with the Bash tool's own background mode, never `nohup &`** (playbook 1851: it silently did not start, again) |
| EDL | `edl.py` | every boundary is an **anchor phrase** resolved against the word JSON; unmatched anchor = exit 1. 18 keep-spans, 8 drops (retakes: second take kept), 30.1 of 32.0 min kept. `python edl.py` prints the resolved table |
| voice EQ | `p1_eq.py` | **fitted**, not Part 2's curve: this DSLR sits 4–8 dB under the Layouts master at 1.3–5 kHz. Loop against the Layouts master, worst band residual **0.7 dB** |
| assemble | `assemble_compare.py` | proven recipe (-t, -frames:v, tpad, apad, pcm); every segment **measured** (frames, audio, level > -50 dBFS) or the build stops; master frame count must equal the sum; words carried across the cut → `compare_map.json` on the master clock |
| shots | `make_shots.py` → `src/timelines/compare_shots.ts` | display plan per block as (anchor phrase, template, params); unmatched anchor = exit 1 (G0). Also exports SITE stack px, PLAN_SIZES, ZONES. Dry-run against the source transcripts before the map exists |
| captions | `gen_caps_compare.py` → `thomson_compare_caps.ts` | Part 2's chunk/FIX/WORDFIX + this project's glossary (the actual mishearings: Concert/Thompson/Homsen Reserve, Jet/JSCAPE/JITScape, Amor/Armors/AMRO, Skyhapydead, Bradhill, Takin, latch…) |
| clock check | `caps_check.py` | first caption per span within 1 s, not in silence, contains the block's key word; drift per 5-min window < 0.35 s (G1) |
| composition | `src/ThomsonCompare.tsx` + `src/CompareBoard.tsx` | bone theme, fixed Ident, zones from the approved mock, PiP loose crop, `<Audio>` mounted, time from `L.fps` |
| check board | `run_board.sh` | G0 → G0b → G1 → proxy (960x540, GOP 15) → clean bundle → CompareBoard at REAL fps → `out/compare_board/_SHEET.png` |
| render | `run_compare.sh` | G0–G2 → bundle → render → **G3 three-point speech level** → 1.15x delivery with bed → verify_v5 → chapters from SPANS. `VER=v1`, name `THOMSON_LAYOUTS_PART1_v1_1.15x.mp4` |

**Spoken slips left in the audio, corrected on the BOARD (never in his mouth):**
"29 metres" (28) · "$2,996" (2,966) · "$1.75M" (1.767) · "$2.269M at $3,000" (2.196)
· "$2.239M" (2.39) · "97 sqft bigger" for the 1,152 (same size) · "1142" (1,141).
Also his ad-lib "Block 1 at least 40 m to the opposite block" — the map has **no**
block-to-block arrow from Block 1; the board says "no block faces it" and shows no
number.


**Check-board round 1 (28 Sep, 143 probes):** pipeline holds end to end - every display
lands on his word, captions on the clock, PiP/subtitle zones clean. Fixes applied before
the full render: (1) ZONES were guessed fractions and ~8 were visibly off -> re-read off
gridded plan sheets (`zone_sheets.py`, `_zones_1/2.png`), all 16 plans; (2) Whisper number
mishearings in captions ("762 bedrooms", "$646M unit", "5,775 square feet") -> glossary;
(3) empty grid showed $0 -> blank; (4) `tighten.py` shortens every pause > 1.0 s to
~0.7 s, source-anchored, 41 pauses / 87 s removed, 59 spans, 28.7 min - master re-cut;
(5) `run_board.sh`/`run_compare.sh` now `set -o pipefail` so a gate piped through `tail`
still stops the chain; the two heredocs that reference $NAME/$VER/$SPEED are unquoted.
`caps_check.py` rewritten to use ffmpeg silencedetect (the hand-rolled envelope read
-180 dB on speech) with a 1.0 s volumedetect window (0.4 s after a seek lands on AAC
priming and reads -91 dB).

**Assets added for the build:** `tr_775.png` (cropped from FP p06 at 300 dpi, pins
kept, sponsor strip trimmed). Still missing for Part 2: tr_1238, tr_1367, tr_1485,
tr_1808, js_1259, amo_1292, js_1647, js_2099.

## Pipeline — original plan (superseded by the table above), mirroring `work/thomson_layouts/`

Reuse the structure, not the files. Do **not** touch `work/thomson_layouts/`,
`out/THOMSON_LAYOUTS_*`, `public_thomson_reserve/layouts/` or
`src/ThomsonLayouts.tsx` — another session is delivering v6.

| To create | Mirrors | Job |
|---|---|---|
| `edl.py` | `thomson_layouts/edl.py` | board list as executable source of truth; prints its own document. **This video is voiceover-led, so the EDL is boards-against-narration, not cuts-against-footage** |
| `make_boards.py` | `make_shots.py` | derive board timings + callout anchors from `compare_map.json`; exit non-zero if any callout has no anchor phrase |
| `gen_caps_compare.py` | `gen_caps_layouts.py` | captions on the speech clock |
| `caps_check.py` | same | verify caption clock against the recorded VO |
| `run_board.sh` | same | **cheap gate — one frame per board, ~6 min.** Run and look at the frames before any full render |
| `run_compare.sh` | `run_layouts.sh` | gated full chain, 1.15× delivery pass with bed + sidechain + loudnorm |
| `src/ThomsonCompare.tsx` | `src/ThomsonLayouts.tsx` | composition |
| design | import `src/LayoutsDesign.tsx` | approved system; do not fork it |

Carry every CH.14–16 gate: G0 regenerate derived data from current masters,
G1 caption clock + sources are the cut ones, G2 master is CFR / matched streams
/ 48 kHz, G3 the native render actually contains speech.

**Version name:** `THOMSON_COMPARE_v1` and up. Distinct on every render.

## Blocking on Edmund

1. `[SIGN-OFF]` JadeScape 775 → $1,900,000 / $2,452 psf (his slide says $1.98M;
   no such row exists). Audit §2A.
2. `[SIGN-OFF]` AMO 1,141 effective → $3.47M (his slide says $3.43M; his own
   printed 3043 psf confirms $3.47M). Audit §2B.
3. Voiceover recording against `SCRIPT_v2.md`.

Boards can be built and the check board rendered before 1–3 land, using
placeholder timing. Nothing goes to a **master** until the two sign-offs do.

---

## v2 — design v2 across the whole of Part 1 (29 Sep 2026)

Built on Edmund's 29 Sep review of v1 and his approval of the 592-block mock.

**Frame rules (every scene)**: logo only; gold punchline in the header band starting clear of the logo;
content band y 180–900 (breathing room under the header); subtitles centred, 52 px; PiP 380 px circle
bottom-right (320 px on FACE scenes, under the fact panel); full-screen speaker on FULL cuts.

**Templates in use**: FULL, MIX (bigger), FLICK, G (matrix, big, TR label), DATE (preview-date asset +
work banner + QR card), L1 (unit-count tag), L2 (dim + box), L3 (plan + context zoom + callout tag),
SIDE (B1 vs B2), S1 (site: plain / lux / classic / stacks with bold block highlights + rings),
FACE (block crop + BLOCK·STACKS / FACING / IN FRONT / FLOORS panel), DIST (developer's p13 drawing
cropped, tag), C1 (TR vs competitor + estimate grid + real transaction), ADJ, L4, CARDS.
Dropped from v1: S2, S3, S4 (drone), NOVIEW, BOTHWAYS — replaced by FACE / S1-stacks / DIST.

**CTAs**: QR card (`cta_card.png`) on every CTA scene (qr / sub / work / DATE); SUBSCRIBE pill + bell
animated; 7 scheduled subscribe pop-ins on FULL cuts (seeded, ~every 3–5 min, never on a CTA shot):
0:30, 3:37, 7:56, 13:02, 18:33, 23:28, 27:21 (master clock, before the 1.15× delivery speed).

**Facings**: re-derived on Edmund's north arrow (north = page-left). Table in VIDEO5_STACK_FACING.md §5.
Two on-camera lines disagree with it (A2/A3 "east facing" → SOUTH on screen; A7 "only south" → WEST).

**Edit**: 15 dead-air drops added to `edl.py` (Edmund's 6 timestamps + 10 more found by silencedetect,
all between sentences): master 1719.8 s → 1686.3 s, 71 spans, 50,589 frames. `spans()` now
overlap-safe (`cur = max(cur, db)`).

**Assets**: `tr_592_b2` cleaned (developer bubbles / disclaimer masked; raw kept as
`tr_592_b2_raw_backup.png`). `plans_tight/` regenerated for it.

**Pipeline**: `run_mock.sh` (block-filtered board for design rounds), `run_board.sh`, `run_compare.sh`
(VER=v2). Bundle copies the 8 GB public dir (~10 min); the render step occasionally dies with a
BrowserRunner timeout on the first attempt — rerun the render alone.

---

## v3 — Edmund's v2 review (29 Sep evening)

- **Project colours** on every label bar and callout tag: Thomson Reserve navy, AMO red (#B3261E), JadeScape green (#1E7F4E), Sky Habitat blue (#1F4E9E).
- **FACE** rebuilt: site crop left (880 px), fact panel 560 px on a blurred site-plan backdrop, bigger text, new TYPE row.
- **His assets** (from his Drive links, 3x Lanczos upscaled — screenshots at 437/634 px): `tr_732_sizes` on the 732 room-by-room scene, `tr_1055_sizes` on the 1,055 first plan + room-by-room, `view_stack05` (his "existing surrounding views" slide) replaces the site plan at "drone view".
- **New displays**: TR 592 vs AMO 678 while he quotes the AMO sale (5:50); AMO 743 storeroom gap (9:13); 947 dining zone + foyer store spotlights (15:33 / 15:54); 904 comparison waits for the second "904 square feet" (nth=2 anchor).
- **Zones corrected**: 947 balcony / dining / foyer; JadeScape 904 bedroom 3; 1,055 back (yard+WC+ST+HS), HS, kitchen countertop; 1,152 wall.
- **Subtitles**: 22 token-level fixes (see gen_caps_compare.py). Rule order matters: an earlier rule can rewrite the tokens a later rule expects.
- **Edit**: 17 clip removals exactly as given (his "12:53.5" read as 13:53.5), plus sliver merge in `spans()` (a keep-span under 0.6 s between two cuts is dropped). Master 1686.3 s → 1630.1 s, 79 spans. The "other side of Bright Hill" display went with its clip; "from 54" anchor became "at level 10".
- caps_check A2 block-start keys updated (the cut removed the old first words).
- Board: `VIDEO5_working/board_v3/`. YouTube pack: `VIDEO5_YOUTUBE_PART1.md`.

---

## v4 — Edmund's v3 review (30 Sep)

- 732 room-by-room scene re-anchored to "liveable" (10:13): his earlier clip cut had removed "Living Hall 23", so the old anchor matched a later "living hall" and the sizes image came in at 11:04.
- L4 rows are now cue-driven: make_shots finds the moment he says each figure (`rowT`, tokens '23' '.5' or a rounded "32"), each row slides in on its cue and the current one is highlighted gold. Rows he never says appear on a fast stagger and are never highlighted. Applies to the 1,055 scene too.
- Caption at 10:14 reads "Living hall 23.5, Master 10.9" (the audio only has ".5" left after his cut).
- Check stills: `board_v4/_room_sizes_cue_check.png`. No EDL change, master unchanged (1630.1 s).

---

## PART 2 — THE 4 & 5 BEDROOMS (build started 30 Sep 2026)

Concept: `VIDEO5_PART2_CONCEPT.md` (THE CLIMB). Pipeline is a fork of Part 1's, in `E:\REMOTION\work	homson_compare2\`:
`edl2.py` (8 blocks, 10 retake drops) → `tighten2.py` → `assemble2.py` (master `public_thomson_reserve/compare2/compare2_master.mp4`,
map `compare2_map.json`) → `make_shots2.py` (91 shots) + `gen_caps2.py` → `run_board2.sh` / `run_mock2.sh` / `run_compare2.sh` (VER=v1, NAME THOMSON_LAYOUTS_PART2).
Composition `src/ThomsonCompare2.tsx` (navy field, PiP square left, ladder strip right, templates HOOK RING LADDER HEIGHT RULER SWIPE CHEQUE FLICK TXQ),
board `src/Compare2Board.tsx`, both registered in Root.

Footage: 2a 8:25 · 2b 5:56 · 2c 4:34 → first master 17.7 min before tightening.
Assets cut this round: TR plans 1,238 / 1,367 / 1,485 / 1,808 (FP PDF p10–13 at 300 dpi, developer pins kept), JadeScape 1,259 / 1,647 / 2,099 (brochure p18/20/21),
views 1–8 (TF p25–28), DP1/E1 kitchen photos (TF p52–55), 4- and 5-bed sale tables (TF p36/37), distance crops from TF p13, the 1,485 reconfiguration frames.

Not on file (scenes show his words as text until they arrive): JadeScape 1,259 sale printout ($3.2–3.3m), AMO 1,292 plan and sale.

---

## PART 2 v2 — Edmund's v1 review (1 Oct)

- **Clip removals**: his ten ranges applied exactly (delivered 1.15x → master → source) in `edl2.py` GAPS; the 10:32 one became
  new block boundaries (2b now ends after "hidden from sight", 2c starts at "a landscape layout"). Master 969.9 → 945.7 s.
  The sliver re-transcription (`check_slivers.py` / `check_master.py`) confirmed the audible result; three captions were then
  re-tokened to match the audio the first-pass Whisper had mis-timed ("350 3-bedrooms", "90 units of 1,238", "So there are no other").
- **Subtitles**: year, Thomson · developer done · the cost for ducted · two entrances · layout lovers like me, · regular shape.
- **Captions**: "the size difference"; the four ladder titles read "1,238 / 1,367 / 1,485 / 1,808 sqft size" (no more "rung").
- **1,238 room highlight**: now bedroom 2, the room beside the master (his "3rd from the right / closest to the master" — flagged).
- **AMO 5:28**: the Thomson Reserve plan removed; the scene is a wide text card until the AMO 1,292 plan arrives.
- **Reconfiguration**: redrawn to his sketch (`make_reconfig2.py`): blue = wall the open side; green = a door in that wall hinged
  on the side opposite the original, and a door through the right wall into the wardrobe. Frames r1/r2/r3, cues "See how" / "voila".
- Known: at 12:54 the "from level 25" restart is still audible after his cut; left as he cut it.

### PART 2 v3 (1 Oct, later)
Reconfiguration corrected to Edmund's red-arrow sketch: no door into the wardrobe. DOOR1 = entrance in the new wall (hinge 1262,1812, swings into the corridor); DOOR2 = the original study door swinging inward (hinge 1590,1812). Red arrows drawn on frames 2 and 3. Punchline: "Enclose the study. Enter from the corridor. Voila." Master unchanged (945.7 s).
