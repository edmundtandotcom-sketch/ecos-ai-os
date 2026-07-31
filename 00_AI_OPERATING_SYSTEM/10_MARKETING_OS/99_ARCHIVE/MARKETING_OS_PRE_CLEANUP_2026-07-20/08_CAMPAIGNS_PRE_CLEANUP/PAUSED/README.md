# README — 08_CAMPAIGNS/PAUSED
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A
Supersedes: none
Sources: `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`
Next review: when a campaign is paused

---

## Purpose
Holds campaign records moved out of ACTIVE when paused (spend stopped, not killed, resumable). Empty at build time — no campaign in `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` currently has PAUSED status.

## Next step
When a campaign is paused, move its record file from `ACTIVE/` here, update Status in `CAMPAIGN_REGISTRY.csv`, and note the pause reason + resume trigger in the record.

## READS FROM
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`, `08_CAMPAIGNS/ACTIVE/`

## FEEDS INTO
`00_COMMAND_CENTER/ACTIVE_CAMPAIGNS.md`
