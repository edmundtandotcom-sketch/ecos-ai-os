# EDB — "Can It Beat the S&P 500?" (S&P / Capital Allocation)
Status: DRAFT — awaiting desktop pixel confirmation (§0 flags below)
Date: 2026-08-25
Skill: `/rei-ads-routine` v1 (test run)

## 0. Flags before anything else

1. **Register mismatch.** This script is verbatim NL01 — "THE BENCHMARK" from the New Launch Ladder™ campaign (`00_CONTROL/NewLaunchLadder_Ad_Consolidation_Master_v1.0.md`), and the body itself names "the New Launch Ladder™" at the framework beat. It was recorded and filed under `2026-07_SecondPropertyLadder_AdProduction/03_RECORDING_OUTPUTS/10-S&P Angle/`, a different campaign whose canonical register (A01–A20/B01–B20) explicitly says not to cross-reference IDs with NL01–NL06. I'm proceeding — you confirmed the script and want this produced — but the raw footage and this EDB should probably live in the New Launch Ladder campaign folder, not here. Your call on whether to move it or leave SPL as the production home.
2. **CTA locked: C.** Confirmed by Edmund. "…click the link below. Tell me the project you're looking at and I'll show you whether it can beat the S&P 500." §4/§6 below are written to this. If the actual `S&P CTA-DSLR.mp4` take turns out to have spoken A or B instead, only the CTA caption/chip text needs swapping — nothing else changes.
3. **Timing is estimated, not measured.** Cloud cannot open the raw files (all 6 exceed the Drive connector's 10MB cap) — so I cannot verify actual take length, delivery pace, or current framing. Script is 483 words; at a natural direct-response pace (150–190 wpm) that's **~155–195s** for the body, +~15s for CTA-C, **+3s end card ⇒ ~175–215s total**. Timestamps below are built on 170 wpm as the working assumption and are flagged `[EST]`. **A desktop pass must confirm real cut points against the actual take before this locks** — see §9.
4. **Length call.** 483 words is long for the Bible's 120–180s reel spec — it sits in VSL territory (Format 2). **My pick: ship this as the primary VSL-length reel** (the full take that was actually recorded), and separately have a 30–35s cutdown scripted later using the pattern NL01's own master doc already established, for cold-traffic placements. Reason: a full take exists and matches what was filmed; a cutdown from scratch is separate work, not part of this test.

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
- **If source is already tighter than the 12–16% target** (unlikely for a DSLR setup, but possible): do not synthetically zoom out. Flag for a reshoot at wider framing rather than publishing an over-tight ad.
- **Verification gate:** this section is unverified against real pixels. Desktop must confirm actual head-size % before export — see §9.

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

## 9. What desktop needs to confirm before this locks

1. Actual duration and pace of `S&P-DSLR.mp4` + `S&P CTA-DSLR.mp4` — replace every `[EST]` timestamp with measured cuts.
2. Actual head-size % in the DSLR frame against the §3 target — confirm the crop plan works or needs adjusting.
3. Which CTA variant is spoken in `S&P CTA-DSLR.mp4` — confirm or correct §4's CTA-C assumption.
4. Whether this recording/EDB should move to a New Launch Ladder campaign folder (flag 1).
