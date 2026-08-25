# EDB — "Can It Beat the S&P 500?" (S&P / Capital Allocation)
Status: DRAFT — awaiting desktop pixel confirmation (§0 flags below)
Date: 2026-08-25
Skill: `/rei-ads-routine` v1 (test run)

## 0. Flags before anything else

1. **Register mismatch.** This script is verbatim NL01 — "THE BENCHMARK" from the New Launch Ladder™ campaign (`00_CONTROL/NewLaunchLadder_Ad_Consolidation_Master_v1.0.md`), and the body itself names "the New Launch Ladder™" at the framework beat. It was recorded and filed under `2026-07_SecondPropertyLadder_AdProduction/03_RECORDING_OUTPUTS/10-S&P Angle/`, a different campaign whose canonical register (A01–A20/B01–B20) explicitly says not to cross-reference IDs with NL01–NL06. I'm proceeding — you confirmed the script and want this produced — but the raw footage and this EDB should probably live in the New Launch Ladder campaign folder, not here. Your call on whether to move it or leave SPL as the production home.
2. **CTA locked: C — and RESOLVED against the real take (2026-08-25, desktop).** The recorded `S&P CTA-DSLR.mp4` does not contain one variant, it contains **all three**, read back to back and each slated aloud "Call to Action 1 / 2 / 3". The renderer finds the slates and cuts out only the one named in `CTA_VARIANT` — currently `"C"` ("…tell me the project you're looking at"). Switching to A or B is now a one-word config change, no re-record and no re-edit.
3. **Timing — the estimates below are superseded by measurement (2026-08-25, desktop).** The raw body take is a teleprompter read with **57% dead air across 31 gaps of up to 12 seconds**; untightened the ad runs about **7.5 minutes**, not the ~180–215s estimated here from word count. The renderer now caps every internal pause (`MAX_GAP = 0.38s`) and drops head/tail silence entirely, then remaps all word timings onto the tightened timeline. The `[EST]` timestamps in §4 remain as the *intended structure and order*; the real times come out of the render and land in `out/beats_resolved.json`. **Do not treat §4's clock values as the edit — treat the sequence as the edit.**
4. **Length call.** 483 words put this in VSL territory (Format 2) rather than the Bible's 120–180s reel spec. Ship it as the primary VSL-length asset; a 30–35s cold-traffic cutdown is separate later work. Note the tightening in flag 3 pulls the finished runtime well below the raw take — final duration comes from the render, not from this estimate.

## 1. Header

| | |
|---|---|
| Engine | Client Advisory — New Launch Ladder™ (content), filed under Second Property Ladder AdProduction (location — see flag 1) |
| Campaign | `2026-07_SecondPropertyLadder_AdProduction` |
| Angle | NL01 — The Benchmark |
| Palette family | **B — REI Core** (blue/yellow, face-cam direct-response — this is a single-speaker VSL-style ad, not a Legacy Launch metaphor-render piece, so Family A doesn't fit) |
| Genre | Studio hook-to-camera |
| Duration target | ~180–215s [EST], 9:16 |
| Aspects | Master 9:16 (1080×1920) — this test run is 9:16 only per your instruction; 1:1/4:5 crops deferred |
| Raw source | `03_RECORDING_OUTPUTS/10-S&P Angle/Raw Assets/` — https://drive.google.com/drive/folders/1YI01UZ3sKdUsyagB3OOHCEShDyIxdiWk |
| Camera angle used | **DSLR** — `S&P-DSLR.mp4` (body) + `S&P CTA-DSLR.mp4` (CTA), per your instruction |

**Axis combo (Bible §8):** 1-Studio hook-to-camera · 2-Family B · 3-Punch condensed (headline/punchline mode) · 4-karaoke (caption preset) · 5-Real room, S5 grade · 6-Data card + chart/arrow + question interstitial · 7-Zoom-punch-led · 8-Solid blue chip, white text (Family B CTA chip — see §4 note)

**First entry in this campaign's Variation Register — nothing to differ from yet.** Logged in `VARIATION_REGISTER.md` (this folder).

## 2. Look

- **Grade:** S5 clean+bright (Bible §4.7) — real black/white points, warm skin, light S-curve, micro-sharpen. No stylized LUT.
- **Backdrop:** real room, DSLR angle, no compositing (no studio-backdrop assets exist for this batch).
- **Caption:** `karaoke` preset (SharpCut) — Montserrat, active-word highlight in accent yellow **#FFE800** (SharpCut's own default accent, consistent across the engine's presets), white base text, outline on, ALL forced through `applyCase` only where the preset default already uppercases — karaoke's `uppercaseDefault` is false, so sentence case, per engine default. Position: bottom, anchor 83% of frame height (engine default). Font size 100% baseline — recompute per §3 framing once real footage confirms safe zones.
- **Type mode:** Punch condensed (Archivo Black class) for punchline/data-card overlays — matches the VSL-locked Family B world, not the Family A editorial serif.

## 3. Framing spec — answers "speaker not too big" without needing to see the take

Since I can't inspect `S&P-DSLR.mp4`'s current framing, this is a **target the editor hits regardless of what the raw crop currently looks like** — camera-agnostic:

- **Deliverable frame:** 1080×1920 (9:16).
- **Target head size:** crown-to-chin occupies **12–16% of frame height** — a medium shot, not a close-up. Shoulders/upper chest visible.
- **Eye-line:** sits at **38–42% down from top** of frame.
- **Headroom:** ≥8% of frame height above the crown — never crop the top of the head.
- **Reserved bands (do not place face or hands here):** top 10% (safety/eyebrow text), bottom 17% (caption anchor at 83% + karaoke line height per Bible §5 geometry).
- **If the DSLR source is landscape 16:9** (typical interview rig) being center-cropped to 9:16: crop inward evenly around the eye-line, not from a fixed edge. If the resulting crop would exceed the 12–16% head-size target (i.e. speaker reads bigger than that after a straight center crop), **pull back the crop** — add letterbox/blur-fill or reframe wider — rather than accepting an oversized face that fills the frame. That's the direct fix for your framing note.
- **If source is already tighter than the 12–16% target:** ← **this is what the footage actually is.** Measured on the real DSLR frame (2026-08-25): crown at y=55, chin at y=428, pupils at y=238. The head is larger than target, and since cropping can only make a head *bigger*, no crop can fix it. The renderer therefore **scales the whole picture back** inside the 9:16 canvas until the head hits 15%, and fills the surround with **flat brand navy** (`FILL_MODE = "navy"` — a blurred copy at this magnification is just a smear of face). It never upscales and never exceeds canvas width, so the head can only land at or below target. A reshoot at wider framing would still be the better long-term fix.
- **Verification status: MEASURED, not estimated.** The numbers above are read off a real frame. The proof frame (`out/frame_framing_check.png`) still gets a human look before export.

## 4. Timeline [EST — see flag 3]

| t [EST] | Script beat | Visual layer | On-screen text (exact, [accent] marked) | Effect/transition in | Notes |
|---|---|---|---|---|---|
| 0:00–0:08 | HOOK (Call-Out) — "Is this your 2nd, 3rd or 4th investment property? …That's not the question anymore. Here's the question." | Face-cam, DSLR | "IS THIS YOUR **[2ND, 3RD OR 4TH]** PROPERTY?" (punch-condensed, pops in on "Here's the question") | Cold open, no logo first — small eyebrow wordmark only. First caption cue ≤0.5s. | Call-Out hook type per Format 1 — names exactly who it's for. |
| 0:08–0:28 | Setup — "$500K–$1M cash + CPF, 25-yr mortgage, stamp duty, interest, agent fees, four years." | Face-cam → motion graphic (cost stack) at ~0:16 | "$500K–$1M" / "25 YEARS" / "4 YEARS" each punch in as spoken (money tokens never split across a cue) | Zoom-punch on each dollar figure | 3s visual-layer rotation begins here. |
| 0:28–0:42 | Reframe — "That money could be in the S&P 500 at 10%/yr… the benchmark is beating the S&P 500." | **Chart/arrow interstitial** (generate — see §5.1) | "THE BENCHMARK: **[BEAT]** THE S&P 500" (accent word gold→ no, Family B: accent word in **yellow**) | White-flash into graphic, zoom-punch out | This is the belief-shift line — give it the strongest visual beat, full interstitial not just an overlay. |
| 0:42–0:58 | Hard truth — "Most agents only talk about gains… easy test to pass." | Face-cam | "ALMOST ANY PROPERTY CAN MAKE **[SOME]** GAIN." | Straight cut back to face | Contrast beat — pull back from graphic to reestablish the speaker. |
| 0:58–1:10 | Method intro — "Before I invest… I ask one question. Can this project beat the S&P 500?" | Face-cam | **[question interstitial]**: "CAN THIS PROJECT BEAT THE S&P 500?" full-screen navy card, per Amberwood-style vocabulary (Bible §4.8) | Navy question-card wipes in | Direct-address beat — let the question hold ~2s before cutting back. |
| 1:10–1:35 | Proof 1 — Property A: bought $1.15M, $321K committed, sold $1.525M after 3yrs, net $282K, ~22.9%/yr | Face-cam → **data card** (generate — see §5.2) | Data card: "BOUGHT $1.15M → SOLD $1.525M / $321K committed / **[22.9%/YR]**" | Zoom-punch on "22.9%" | Track Record proof type (Format 1 Proof table) — real numbers, gold-standard treatment even in Family B: number gets yellow, not a full palette swap. |
| 1:35–1:58 | Proof 2 — Property B: bought $1.05M, $292K committed, exited 4yrs at $1.28M, ~12.9%/yr | Face-cam → data card variant | "BOUGHT $1.05M → SOLD $1.28M / $292K committed / **[12.9%/YR]**" | Slide-in (varies from Proof 1's zoom-punch — no consecutive repeat, Bible motion rule) | Two proof points back to back — vary the transition between them intentionally. |
| 1:58–2:20 | Reframe 2 — decision factors: entry price, unit, future buyer, exit price, equity release | Face-cam + **5-line kinetic list** overlay, one line per beat | Each factor pops in and holds: "ENTRY PRICE" → "THE UNIT" → "FUTURE BUYER" → "EXIT PRICE" → "EQUITY RELEASED" | Word-by-word style pop (matches `wordPop` caption preset energy, applied to the overlay not the caption track) | Fast rhythm — these are short declarative fragments in the script; let the cutting match that staccato. |
| 2:20–2:50 | Method — "New Launch Ladder™… Return on Equity… walkaway price… next three moves" | Face-cam → **3-icon framework card** (generate — see §5.3) | "THE NEW LAUNCH LADDER™" title card, then 3 icons: Return on Equity / Walkaway Price / Next 3 Moves | Navy card, brand-consistent with the question interstitial from 0:58 (same design system, per Bible reuse rule) | Named-framework beat — this is durable brand IP, treat the card as a reusable asset, not a one-off. |
| 2:50–3:05 | Offer close — "'I made money' is no longer good enough. Your capital needs to work harder." | Face-cam, direct address | "'I MADE MONEY' IS NO LONGER **[ENOUGH]**." | Straight cut, no graphic — let this land as the emotional turn before the CTA | Do not overlay a graphic here; give the line room. |
| 3:05–~3:20 | **CTA-C** (locked) — "…click the link below. Tell me the project you're looking at and I'll show you whether it can beat the S&P 500." | Face-cam → CTA chip animates in | Chip: "TELL ME YOUR PROJECT ›" (solid blue **#005CE6**, white text — Family B equivalent of the Bible's gold chip styles, since Family A's exact chip specs were sampled from Legacy Launch statics; adapt, don't force gold onto Family B) | Chip slides/bounces in | Icon + verb-first label per Bible §3 CTA rule — never "Learn More". |
| ~3:20–3:23 | End card | Logo card | REI wordmark, 3s | Fade | Counted in total duration — QC gate #2. |

## 5. Graphics to generate

### 5.1 — S&P 500 vs Property benchmark chart (interstitial, ~0:28)
> Flat-vector editorial data illustration, deep ink-navy background (#0B1020), two thin 2px line-graphs side by side: left line labeled "S&P 500" rising in a steady, unspectacular slope in white; right line labeled "YOUR NEW LAUNCH" rising steeper but starting later (illustrating the 4-year lockup + costs before the property line even begins), rendered in accent yellow (#FFE800). No axis numbers, no gridlines, generous negative space. Upper third reserved for text overlay: "THE BENCHMARK: BEAT THE S&P 500" in Archivo Black, white with "S&P 500" in yellow. Style: flat matte, no gradients, no 3D, no stock imagery, no currency symbols, no coins. Aspect ratio 1080×1920 (fits full-bleed into the 9:16 timeline).

### 5.2 — Proof data cards (×2, ~1:10 and ~1:35)
> Flat-vector stat card, deep ink-navy background (#0B1020), single accent-yellow (#FFE800) headline number set in Archivo Black at the top ("22.9%/YR" card 1, "12.9%/YR" card 2), with three supporting white grotesque lines below: "Bought $[X]M", "Committed $[Y]K", "Sold $[Z]M after [N] years". Thin yellow hairline rule separates headline from support lines. No photography, no property renders (this is a numbers card, not a project card — no specific project is named in this script). Aspect ratio 1080×1920, designed to sit as a bottom-third overlay over the continuing face-cam, not full-bleed (per Bible §4.3: punchlines never cover the face).

### 5.3 — New Launch Ladder™ framework card (~2:20)
> Flat-vector 3-icon horizontal framework diagram, deep ink-navy background, title "THE NEW LAUNCH LADDER™" in white Archivo Black at top. Three equally spaced icon+label pairs in accent yellow outline icons with white grotesque labels beneath: a calculator/percentage icon → "RETURN ON EQUITY"; a stop-sign/price-tag icon → "WALKAWAY PRICE"; a three-step-staircase icon → "NEXT 3 MOVES". Uniform 2px stroke weight, matte, no gradients, no photography. This card is durable brand IP for this angle — build once, reuse identically in any future NL01 cutdown or carousel. Aspect ratio 1080×1920.

## 6. QC gate (Bible §7 — verbatim, unchecked)

- [ ] No mid-word audio cuts: every cut boundary ≥80ms clear of transcript word end-times
- [ ] End card present: final duration = body + 3s logo card, logo visually confirmed
- [ ] Captions inside safe zones at 9:16 (re-check if 1:1/4:5 crops are produced later)
- [ ] Punchline overlays never intersect the face bounding box at any point
- [ ] 3-second visual-layer rotation verified across the full timeline (no static stretch >4s)
- [ ] Number tokens unsplit; prices/percentages in yellow (Family B)
- [ ] Music at 4%; original/licensed beds only
- [ ] Grade check: skin natural, blacks not lifted, no LUT haze
- [ ] **Added for this ad:** confirmed head-size 12–16% of frame height at every point in the DSLR crop (§3)
- [ ] **Added for this ad:** confirmed which CTA variant (A/B/C) is actually spoken; caption/chip text in §4 matches

## 7. Handoff

Route via `/video-produce`: this is cut/caption/crop/export-class work (no compositing, no multi-cam), so it belongs on **SharpCut Studio** — karaoke preset, 9:16 crop, the three generated graphic assets composited as overlays at the timestamps above. Claude cannot drive SharpCut's UI or render this EDB directly.

## 8. Register + index

- Logged as combo #1 in `VARIATION_REGISTER.md` (this folder).
- Campaign `_INDEX.md` folder map updated to include `06_EDIT_DIRECTION_BRIEFS/`.

## 9. Desktop confirmation — status

Worked through on the desktop 2026-08-25 (`desktop_render/render_ad.py`).

| # | Item | Status |
|---|---|---|
| 1 | Actual duration and pace | **Measured.** Teleprompter read, 57% dead air over 31 gaps (up to 12s); ~7.5 min raw. Renderer tightens it; real beat times land in `out/beats_resolved.json`. |
| 2 | Head-size % against §3 | **Measured.** Source is tighter than target — crown y=55, chin y=428, pupils y=238. Fixed by scaling back over navy fill, not by cropping. See §3. |
| 3 | Which CTA variant is spoken | **Resolved.** The take holds all three, slated aloud. Renderer selects by `CTA_VARIANT`; set to C. |
| 4 | Should this move to a New Launch Ladder folder? | **Still open — Edmund's call** (flag 1). |

Also found and fixed while running it, worth carrying to the next ad:

- **Whisper auto-detect mis-set the language**, transcribing the first ~55s as Malay and producing gibberish — which silently broke every beat anchor inside that stretch. Language is now forced to English, and a domain prompt stops "S&P 500"→"SMP 500", "stamp duty"→"stem beauty", "walkaway price"→"work away price". Model raised to `medium`, since captions burn straight from this transcript.
- **Whisper writes numbers as digits**, so anchors phrased "wait four years" never matched "wait 4 years". Two anchors needed that fix.
- **Anchors now resolve in script order** from a moving cursor, so a phrase said twice (e.g. "your future buyer") attaches to the right occurrence.

## 10. Still to do

- Run the render to completion and QC it by eye (contact sheet + framing proof).
- Decide the campaign-folder question (flag 1).
- Log the finished asset in `VARIATION_REGISTER.md` once it ships.
