# WINNING_ASSETS_POLICY
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A (policy, not a performance claim)
Supersedes: none
Sources: build brief §2.8, §5, §13 (13-status asset lifecycle referenced); `00_COMMAND_CENTER/CONTRADICTION_REGISTER.md` C12; `11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv` LRN-002
Next review: on first genuine Tier 1/2 creative-level result

---

## The rule
**Nothing may be labelled "winner" without a Tier 1 or Tier 2 citation attached — a specific source file, date, and number.** A label with no attached evidence is not a fact; it is a guess wearing a fact's clothes.

This rule exists because it was already broken once: MAS HQ's "01_WINNING_MARKETING_ASSETS" and "Top Performing Ads" folders carry the word "winning" with no performance data attached (contradiction C12). Do not repeat this in the Marketing OS.

## What counts as evidence
- **Tier 1** (verified commercial outcome — revenue/clients/CAC): currently NONE exists anywhere in this business (build brief §5). No asset can be called a Tier 1 winner today.
- **Tier 2** (verified behavioural — CTR/CPL/bookings from a real platform export): the only available evidence tier today. See `10_PERFORMANCE/HISTORICAL_BASELINE.md` for the current baseline and `10_PERFORMANCE/IMPORT_SPECS.md` for how new Tier 2 data gets in.
- Tier 3/4/5 (credible external, observed market usage, hypothesis) are never sufficient to call something a "winner" — they can support a hypothesis in `09_EXPERIMENTS/BACKLOG.md`, nothing more.

## Instead of winner/loser: the 13-status asset lifecycle
Per build brief §13 (`13_MARKETING_OPERATIONS/CAMPAIGN_LIFECYCLE.md`, owned by the Operations builder), every creative asset moves through a defined status lifecycle rather than a binary winner/loser label. This file does not restate the 13 statuses (they live in the Operations file) — it establishes that **"winner" is not one of them.** Use the registry's `Status` field (`07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`) for lifecycle state; use a cited note in `Learning` for anything closer to a performance claim.

## Minimum bar to promote an asset informally as "performing well"
1. Reached the clean-read minimum used elsewhere in this business — ≥50 leads/angle (per `04_AGENT_EDITION_OS/02_MARKETING/MAS_Campaign_Brief_MM_ValidationTest_v1.0_DRAFT.md` clean-read rule) or an equivalent stated threshold for the channel.
2. One variable isolated at a time (not a bundle of hook + visual + audience changes at once).
3. Result written into `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv` `Learning` field or `09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv`, with SourcePath cited.
4. Edmund/Cindior sign off before the term "winning" is used in any external-facing planning doc.

## Current state (2026-07-11)
Zero assets in `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv` meet this bar. All 16 Legacy Launch video ads are Tier 5, Status Unlaunched. No asset in this Marketing OS may be called a winner today.

## READS FROM
`00_COMMAND_CENTER/CONTRADICTION_REGISTER.md`, `10_PERFORMANCE/HISTORICAL_BASELINE.md`

## FEEDS INTO
`07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`, `13_MARKETING_OPERATIONS/CAMPAIGN_LIFECYCLE.md`, `11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv`
