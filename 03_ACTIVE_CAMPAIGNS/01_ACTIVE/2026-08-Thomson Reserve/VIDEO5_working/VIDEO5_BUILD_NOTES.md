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

## Pipeline — to build, mirroring `work/thomson_layouts/`

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
