---
name: rei-reels-routine
description: Generate reel/short-form scripts and breakdowns for Coach Edmund Tan / Singapore Real Estate Insider — both paid persona-driven ad reels and organic topical-breakdown reels cut from a long-form. Use when asked to write reels, break a long-form into reels, build hook variations, or produce short-form for a campaign. Same output on desktop and cloud — actual cutting/export happens in SharpCut Studio, not here.
---

# REI Reels Routine — Reel Script Generation

There are **two distinct reel patterns** in use. Pick the right one before generating — they are not interchangeable, and neither should be forced onto the other's use case.

## Pattern A — Persona/Angle Ad Reels (paid, Meta/IG ads)

Source of mechanics: `00_AI_OPERATING_SYSTEM/05_CONTENT_MARKETING_ENGINE/00_PRODUCTION_FOUNDATIONS/LAYER_3A_REEL_SCRIPT_RULEBOOK_v1.4.md`.

**Caveat carried from that document's own index — do not skip:** it was built for the Legacy Launch campaign specifically (its G-codes are Legacy-Launch buyer personas: Idle Millionaire, Fully Paid Settler, Golden Window, etc.) and its own folder index flags that "old segment labels must be reconciled to current Positioning before use." Never copy its G-code personas directly onto a different offer or audience — re-derive segments from that campaign's own buyer research first.

Reusable mechanics regardless of campaign:
- **Hook (0–5s) / body (5s+) independence** — film the body once, swap hooks separately. One body × N hooks = N ad variants from one filming session.
- **Stage-gated content** — PA (problem-aware) / SA (solution-aware) / PA2 (retargeting) each get their own script pattern and CTA intensity.
- **CTA library by stage** — soft (PA) → medium (SA) → strong (PA2). See the rulebook §2E for exact lines.
- **Banned-language list** — never "belief"/"mindset"/"limiting belief"; use "outdated strategy"/"old calculation"/"silent cost" instead. This is REI's advisory tone rule — confirm before applying to a non-advisory brand.
- **Asset naming**: `LL_[STAGE]_[GCODE]_[CONCEPT]_[ANGLE]_[PATTERN]_[DURATION]_V[#]` — adapt the campaign prefix, keep the field structure.
- **Pack Lock gating** — a segment doesn't scale to full production until it proves out (rulebook's threshold: 20 qualified leads + 5 consultations + 1 creative winner). Don't film G2+ before G1 locks.

## Pattern B — Topical Breakdown Reels (organic, cut from a long-form)

Precedent: `03_ACTIVE_CAMPAIGNS/01_ACTIVE/2026-08_New_Launch_Amberwood/` — 14 reels, each isolating one self-contained claim, objection, or data point from the long-form review (e.g. "Zero Small Units," "The Break Even," "Thin Resale Data," "D10 Doesn't Always Climb"). Not persona-driven — fact/angle-driven.

Method:
1. The parent long-form script + its cross-check map must already be locked (via `rei-video-routine`). Do not build these reels before that — flag it if asked to.
2. Scan the locked script for every self-contained claim that could stand alone in 30–90s.
3. One reel per claim. Title = the specific claim, never a generic label ("Reel 3" is wrong; "Quarter of the Precinct" is right).
4. Apply the same locked production rules as the parent long-form (subtitle/number rules, transitions — see `rei-video-routine` §5).
5. Name: `<PROJECT>_REEL_<NN>_<TOPIC>.mp4`. Track every reel in the campaign's `00_INDEX.md` deliverables list as it's produced — don't let the index go stale (the Amberwood precedent's index lagged 14 already-cut reels behind; don't repeat that).

## Which pattern applies

If the task doesn't say, infer from context (paid ad campaign with defined buyer segments → Pattern A; a project review/long-form already exists and needs breaking up → Pattern B) and confirm before generating a full batch.

## Output

This skill produces reel breakdown docs — hook line, angle/claim, body direction, CTA — as markdown. Identical output whether run on desktop or cloud.

## Handoff to actual cutting

This skill does not cut or export video. Once a source recording exists, the cut/caption/crop/export step runs in **SharpCut Studio** (`edmundtandotcom-sketch/sharpcut-studio`) — a browser-only app (silence/filler removal, captions, crop, transitions, MP4 export), deployed on Cloudflare Pages, fully client-side with no backend. It is genuinely portable: the same tool gives the same result whether opened from the desktop machine or any other device with a browser — confirm the live URL against `00_AI_OPERATING_SYSTEM/08_OPERATIONS/06_CODE_REPOSITORY_REGISTRY.md` or ask Edmund rather than assuming a domain. Claude cannot drive its UI directly (it's a browser app, not a CLI), but can hand off the exact cut list and caption text it needs.

For a multi-cam composite build (PIP, data cards, interstitials — not a simple cut-and-caption reel), see `video-produce`.
