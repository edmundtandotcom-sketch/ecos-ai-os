# FRAMEWORK_SELECTION — 10-Step Selection Engine
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE — reconstructed from the build brief's step list; the underlying "ECOS master prompt" document was not locatable in this workspace (see `_INDEX.md`)
Evidence level: N/A (selection method, not a performance claim)
Supersedes: none
Sources: `MARKETING_OS_BUILD_BRIEF.md` §8 (folder spec); `FRAMEWORK_REGISTRY.csv`
Next review: when the ECOS master prompt is located, or a framework choice is made and worth logging as precedent

---

## Note On Provenance
This 10-step sequence is named directly in the Marketing OS build brief as coming from "the ECOS master prompt." That document could not be found anywhere in this workspace, including `C:\Users\Admin\ecos-ai-os` (a separate software codebase). This file reconstructs the 10 named steps and fills in working content from `FRAMEWORK_REGISTRY.csv` and this OS's own structure. Treat as DRAFT until the original source is located and cross-checked.

## The 10 Steps

1. **Objective** — What is this asset actually for? (lead capture, authority-build, direct booking, nurture, retargeting). State it before picking anything.
2. **Audience** — Which buyer segment (`02_CUSTOMER_INTELLIGENCE\SEGMENT_USAGE_GUIDE.md`) or Agent Edition sub-type is this for? Never write for "everyone."
3. **Awareness** — Where is this audience on both scales in `02_CUSTOMER_INTELLIGENCE\AWARENESS_STAGES.md`: media awareness (PA/SA/PA2) and Ascent Stage (A0–A2 — former A3/A4 retired per Decision 063)? A framework built for PA cold traffic will underperform on PA2 warm traffic and vice versa.
4. **Medium** — What channel and format? Check `FRAMEWORK_REGISTRY.csv` `Channels` column for fit; check `06_CHANNEL_PLAYBOOKS` for platform-specific constraints (all DRAFT — pending platform verification).
5. **Proof** — What evidence tier is actually available for this asset? (`00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md` §5). Do not select a framework whose Proof block assumes Tier 1/2 data (track record, named case study) if only Tier 4/5 material exists — fall back to a warning-story or third-party proof type instead, and label it.
6. **Trust** — What objection or trust gap does this audience carry right now? Cross-check `02_CUSTOMER_INTELLIGENCE\OBJECTIONS_MAP.md` — if Trust (RB-10) or Market Timing (RB-01) is live, the framework must pre-empt it, not just follow its own internal order.
7. **Select** — Pick ONE framework from `FRAMEWORK_REGISTRY.csv` that fits steps 1–6. Do not blend two full frameworks in one asset (e.g. do not run Yes-Ladder and AIDA simultaneously) — pick a spine, then use pieces of others only as supporting technique.
8. **Justify** — Write one sentence: "Using [FrameworkID] because [objective] + [audience] + [awareness stage] + [medium] fit its BestUse and EvidenceTier is acceptable for this asset's risk level."
9. **Reject Alternatives** — Name at least one framework you did NOT pick and why (e.g. "not FR-13 AIDA — too generic for a trust-led cold hook; FR-10 System angle pre-empts the objection AIDA doesn't address").
10. **Adapt** — Adjust for engine (Client vs Agent — never blend), for STALE flags (C05 skeletons need re-verification before language reuse), and for the specific segment's belief block. Log the final choice in the relevant campaign or experiment record (`08_CAMPAIGNS`, `09_EXPERIMENTS`) so the next builder doesn't re-derive it from zero.

## Worked Example
Objective: cold-traffic lead for Legacy Launch → Audience: FCC segment → Awareness: PA / A1 → Medium: Instagram Reel → Proof: Tier 5 only (no launched ads yet) → Trust: Market Timing + Trust objections likely dormant at PA (not yet voiced) → Select: FR-01 Hook-Story-Offer (120s Reel format) + FR-02 G1/PRIVTHOUGHT pattern → Justify: PA-stage, Reel-native, matches G1 "Idle Millionaire" primary priority pack → Reject: FR-08 16-Section Landing Formula (wrong medium, Agent-only, STALE) → Adapt: use Client Advisory language only, no 3C/Market Maker terms, log as `CR-20260710-LL-TBD-VID-001` in `07_CREATIVE_LIBRARY\CREATIVE_REGISTRY.csv`.

## Use Rule
Run this sequence before building any new copy, video, funnel, or email asset. Skipping steps 6 and 9 is the most common failure mode — an asset that "sounds right" but ignores the live objection or never considers a rejected alternative.
