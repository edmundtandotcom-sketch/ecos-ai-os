# _INDEX — 10_PERFORMANCE
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (folder index)
Evidence level: N/A (index)
Supersedes: none
Sources: files in this folder
Next review: when a live data connection is established

---

## Purpose
Honest map of where real performance data lives (most of it inaccessible), the one usable historical baseline, how to import going forward, and what the funnel metrics actually mean.

## Files

| File | Description |
|---|---|
| `DATA_SOURCES.md` | Live Apps Script (LIVE code) + `.gsheet` master sheet (UNREADABLE from filesystem) + MAS HQ Drive-only reports + archived Codex (ONLY machine-readable history, PII rule) + missing central tracker. |
| `HISTORICAL_BASELINE.md` | The Codex 30-day aggregate (2026-05-26 to 2026-06-24): $13,519 spend, 88 leads, 35 responded, $153.62 CPL, $386.26 cost/responded, by channel and by named campaign. Tier 2. No lead→client/revenue join exists — explicitly no Tier 1 claim. |
| `IMPORT_SPECS.md` | Meta/Google/GHL export → registry field mapping. States plainly nothing is auto-connected; minimum viable process is weekly CSV export + paste. DRAFT — pending platform verification. |
| `KPI_DEFINITIONS.md` | Real funnel stage names from the live Apps Script (New → Contacted → Responded → Booked Call → Appointment → Strategy Session → Appt Qualified → Closed/Lost), CPL/cost-per-responded definitions, CPA and "qualified lead" flagged as TBD DECISION. |

## READS FROM
`08_OPERATIONS/`, archived Codex folder, MAS HQ folder (all read-only)

## FEEDS INTO
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`, `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`, `11_WINNERS_AND_LEARNINGS/`, `00_COMMAND_CENTER/DECISIONS_REQUIRED.md`

## Parent index
`10_MARKETING_OS/_INDEX.md`
