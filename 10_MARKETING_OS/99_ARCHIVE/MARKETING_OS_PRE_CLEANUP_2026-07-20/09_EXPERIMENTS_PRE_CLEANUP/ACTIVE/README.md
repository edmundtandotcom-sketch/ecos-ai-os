# README — 09_EXPERIMENTS/ACTIVE
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A
Supersedes: none
Sources: `09_EXPERIMENTS/BACKLOG.md`, `09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv`
Next review: when the first backlog item is promoted to active

---

## Purpose
Holds one file per running experiment, once promoted from `09_EXPERIMENTS/BACKLOG.md` and logged as a row in `EXPERIMENT_REGISTRY.csv`. Empty at build time — no experiment is currently running (Legacy Launch has not launched; the Market Maker validation test is PLANNED, not spending).

## Next step
Promote a backlog item (BL-001 through BL-005) when its blocking condition clears — see `09_EXPERIMENTS/BACKLOG.md` for each item's "Blocked by" field.

## READS FROM
`09_EXPERIMENTS/BACKLOG.md`

## FEEDS INTO
`09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv`, `09_EXPERIMENTS/COMPLETED/`
