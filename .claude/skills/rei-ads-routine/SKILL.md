---
name: rei-ads-routine
description: Art-direct the EDIT of a paid ad reel for REI — given a locked script, raw clips and image assets, produce a timestamped Edit Direction Brief covering visual effects, transitions, graphics, captions, fonts, colors, pacing and overall look, with a variation engine so no two ads present the same way. Use when asked to edit clips into a video ad, design how an ad presents, create ad variations, or invoke /rei-ads-routine. This skill does not write scripts (rei-reels-routine) and does not render (video-produce).
---

# REI Ads Routine — Ad Reel Edit Direction

Scope: the presentation layer ONLY. Script, raw takes, and image assets arrive as inputs. Output is an **Edit Direction Brief (EDB)** precise enough for an editor, SharpCut Studio, or the Remotion pipeline to execute exactly.

## 0. Load first

`00_AI_OPERATING_SYSTEM/05_CONTENT_MARKETING_ENGINE/00_PRODUCTION_FOUNDATIONS/REI_Ad_Reel_Edit_Style_Bible_v1.0.md` — the governing document for this skill. Everything below assumes its contents: two palette families, typography system, locked motion rules, caption preset bank, QC gate, variation engine. If the Bible has a newer approved version, that wins.

Confirm before starting (Ask-First Gate): which campaign/engine (Client Advisory vs Agent Edition — never blend), which palette family that campaign uses, target durations and aspect ratios, and where the raw assets live. If a Variation Register already exists for the campaign, read it.

## 1. Inputs checklist

- Locked script (hook(s) + body + CTA), with emphasis words already marked or inferable
- Raw face-cam takes (note which take, which camera)
- Image assets (project renders, floor plans, data screenshots, brand marks)
- The campaign's Variation Register state (which axis combos are used)

Missing input → name it and stop; never art-direct against imagined footage.

## 2. Spin the variation engine (Bible §8)

1. Read the previous ad's 8-axis combo from the Variation Register.
2. Choose this ad's combo: differ on ≥3 axes, no combo repeat in the campaign, never share Genre+Caption-preset with an ad in the same ad set.
3. State the chosen combo at the top of the EDB and justify the genre choice against the script's tone in one line (a narrative script forced into infographic genre is a mismatch — the axis spin must respect the script, not fight it).

## 3. Write the Edit Direction Brief

Structure (save as `EDB_<CAMPAIGN>_<AD-ID>_v1.md` in the campaign workbench):

```
# EDB — [ad id / hook name]
Engine · Campaign · Palette family · Genre · Duration target · Aspects (master + crops)
Axis combo: [1..8] | Differs from previous ad on: [axes]

## Look
Grade: [S5 clean+bright per Bible §4.7 — state any scene-specific note]
Backdrop: [real room / named studio composite — if composite, the full §4.9 integration chain is implied]
Caption: [preset · font · size% · position · colors from the palette family]

## Timeline
| t | script line (ref) | visual layer | on-screen text (exact, [accent word] marked) | effect/transition in | notes |
```

Timeline rules (all from the Bible — restated here as hard requirements):
- Visual layer changes every ~3s (face-cam → motion graphic → B-roll cycle); audio continuous; boundaries snap to word gaps.
- First caption cue ≤0.5s; hook text on screen within the first second.
- Punchlines: bottom-of-frame designed cards, never touching the face, animated in; one accent-colored word each.
- Every number/price gets an on-screen treatment (gold in Family A, yellow in Family B); number tokens never split across cues.
- Transitions per the chosen flavor axis; zoom-punch reserved for emphasis beats; never the same transition twice consecutively.
- Hook must end on a clean detachable cut so bodies/hooks stay swappable.
- End card: 3s logo card, counted in total duration.

## 4. Graphics to generate

For each motion graphic or still the edit needs but assets don't provide: write a full generation prompt in the house style (see the carousel prompts in `weekly_ads_intelligence_os/production_outputs/2026-07-30_pattern2_daniel_liew.md` for the required prompt quality — palette hexes, composition, style constraints, banned elements, exact overlay text, aspect ratio). Statics-quality bar: the 10 finals in `03_STATIC_CREATIVES_REVIEW`.

## 5. QC gate

Copy the Bible §7 checklist into the EDB verbatim as unchecked boxes. The EDB is not deliverable until every box is checkable by the executor. Add per-aspect caption-safe-zone checks for every crop in the export set.

## 6. Register + handoff

- Append the ad's axis combo to the campaign's Variation Register.
- Update the campaign `00_INDEX.md` deliverables list.
- Route execution via `/video-produce` (SharpCut for cut/caption/export-class work; Remotion/desktop tier for composite-heavy builds). Never claim a render happened here.

## Known reference library (where the DNA came from)

Pixel-verified statics: `01_ASSET_LIBRARY/01_APPROVED_LIBRARY/05_CAMPAIGN_FINALS/80_FINALS_REVIEW/01_LEGACY_LAUNCH/01_GENERIC_AND_POSITIONING/08_LL_CONTENT_SERIES_16_REVIEW/03_STATIC_CREATIVES_REVIEW`. Motion finals: LL hook/body exports, FL Dad-Daughter + Event/Selfie ads (Drive, desktop-readable), and the published Meta finals (80_R1/R2, Hook squares, etc.). Locked motion rules trace to Edmund's VSL v5 review — treat them as review-tested law, not suggestions.
