# _INDEX — 08_CAMPAIGNS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (folder index)
Evidence level: N/A (index)
Supersedes: none
Sources: files in this folder
Next review: on next campaign added/status change

---

## Purpose
Campaign lifecycle registry + records. One registry row per campaign; one record file per non-historical campaign, filed under its lifecycle subfolder.

## Files / Folders

| Item | Description |
|---|---|
| `CAMPAIGN_REGISTRY.csv` | All campaigns: 1 ACTIVE (Legacy Launch), 1 PLANNED (Market Maker validation test), 6 COMPLETED historical rows from the archived Codex aggregate (Tier 2, PII-free, source-cited). Column list is this build's own design (the ECOS master-prompt §10 field list referenced in the build brief could not be located in this workspace — flagged as a deviation). |
| `ACTIVE/CMP-20260710-LEGACYLAUNCH-OWNERS-001.md` | Full campaign record: objective, audience (incl. C06 conflict flag), assets, tracking status (NOT verified), kill/scale criteria (TBD), links to AI OS masters. |
| `PLANNED/CMP-20260706-MARKETMAKER-AGENTS-001.md` | Thin pointer record to the DRAFT validation-test brief. |
| `COMPLETED/README.md` | Explains empty postmortem folder + why historical rows carry "not captured at close." |
| `PAUSED/README.md` | Explains empty folder (no campaign currently paused). |

## READS FROM
`05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/`, `04_AGENT_EDITION_OS/02_MARKETING/`, archived Codex aggregate (`01_PROPERTY_BUSINESS/01_CLIENT_EDITION/99_ARCHIVE/OLD_OPERATIONS_AND_DASHBOARD_SUPERSEDED_2026-07-04/Codex/`)

## FEEDS INTO
`00_COMMAND_CENTER/ACTIVE_CAMPAIGNS.md`, `09_EXPERIMENTS/`, `10_PERFORMANCE/`, `11_WINNERS_AND_LEARNINGS/`

## Parent index
`10_MARKETING_OS/_INDEX.md`
