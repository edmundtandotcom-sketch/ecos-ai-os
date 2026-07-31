# README — 08_CAMPAIGNS/COMPLETED
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A
Supersedes: none
Sources: `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`
Next review: when a full campaign postmortem is added

---

## Purpose
Holds full campaign postmortem files for COMPLETED campaigns, once written using `12_TEMPLATES/CAMPAIGN_POSTMORTEM.md`. Empty at build time.

## Current state
No postmortem files exist yet. Six COMPLETED rows are seeded in `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` from the only machine-readable historical data on file (archived Codex aggregate, through 2026-06-24, Tier 2, PII-free — see `10_PERFORMANCE/HISTORICAL_BASELINE.md`). Their Decision and Lessons fields read "not captured at close — reconstruct or mark unknown" because no postmortem was written when these campaigns ended.

## Next step
When Edmund/Cindior reconstruct a historical campaign's decision/lessons, or when the active Legacy Launch or Market Maker validation campaigns complete, add a postmortem file here named `<CampaignID>_POSTMORTEM.md` and update the registry row.

## READS FROM
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`

## FEEDS INTO
`11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv`
