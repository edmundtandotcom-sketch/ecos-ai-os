# DATA_SOURCES
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (honest map of where real performance data lives; not a copy of any dashboard)
Evidence level: N/A (this file is a map, not a data claim)
Supersedes: none
Sources: build brief §4 source-of-truth map row "Live performance dashboards" and "Historical performance data"; `08_OPERATIONS/01_CRM_AND_TRACKING/00_OPERATIONS_AND_TRACKING_INDEX_v2.0.md`; `08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs`; direct filesystem check of `REI_Creative_Intelligence_MASTER_SHEET.gsheet` and MAS HQ `.gsheet`/`.gdoc` paths (2026-07-11)
Next review: when any listed source becomes readable/connected, or the central tracker xlsx is located

---

## Purpose
An honest map. Every number used elsewhere in the Marketing OS must trace back to one of these sources or be marked unknown. Do not trust any unlabelled number — see `11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv` LRN-001.

---

## 1. Live — code exists, connects to GHL/Meta/Google
- **`08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs`** — Google Apps Script. Pulls GHL leads, maps pipeline stages (New Lead → Contacted → Responded → Booked Call → Appointment → Strategy Session → Appt Qualified → Closed/Lost), computes funnel-by-campaign, writes to a dashboard sheet. LIVE code, confirmed present in the AI OS. Whether it is currently scheduled/running and which sheet it writes to was NOT independently re-verified in this build pass.
- **`08_OPERATIONS/02_SCRIPTS/REI_GoogleAds_Script_ACTIVE_v8.gs`** — companion Google Ads script. LIVE code, not independently re-verified running.

## 2. Live but UNREADABLE from this filesystem
- **`REI_Creative_Intelligence_MASTER_SHEET.gsheet`** — path: `01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\01_DASHBOARD_TRACKING_SYSTEM\REI_Creative_Intelligence_MASTER_SHEET.gsheet`. Confirmed to exist at this path (checked 2026-07-11). `.gsheet` is a Google Drive shortcut file, not a data file — its content cannot be read from the filesystem, only from Google Sheets directly. **This is the master performance sheet the Apps Script writes to.** No data from it appears anywhere in this Marketing OS build.
- **MAS HQ Friday reports / dashboard** — `X-Singapore Real Estate Insider - MAS HQ\06_OPERATIONS\01_Ad_Performance\` (per build brief §4). Same problem: `.gsheet`/`.gdoc` shortcuts, Drive-only, not filesystem-readable.

## 3. Archived — the ONLY machine-readable performance history
- **`01_PROPERTY_BUSINESS\01_CLIENT_EDITION\99_ARCHIVE\OLD_OPERATIONS_AND_DASHBOARD_SUPERSEDED_2026-07-04\Codex\`** — contains `lead_list_analysis_source_latest.xlsx` and several `lead_summary_*.json` files. These are Google Sheets API batch-update payloads (paste-data + formatting instructions), not clean tables — but they contain the actual campaign/ad/lead-count/spend rollups reproduced in `10_PERFORMANCE/HISTORICAL_BASELINE.md` and `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`.
- **CONTAINS PII.** `lead_summary_data.json` and the xlsx source contain real lead names/phones/emails (not verified line-by-line, but the file structure and folder purpose indicate individual lead records). **Handling rule: never open these to extract anything beyond channel/campaign-level aggregate counts already surfaced in `HISTORICAL_BASELINE.md`. Never copy a name, phone, or email out of this folder into any Marketing OS file.** The two `lead_summary_cost_*` files used to build `HISTORICAL_BASELINE.md` in this pass are aggregate rollups (campaign name, lead count, spend, response count) with no individual PII fields — this was the only Codex material read for this build.
- Date range covered: 2026-05-26 to 2026-06-24 (the "Past 30 Days" rollup). No data after 2026-06-24 was found.

## 4. Referenced but missing
- **Central tracker xlsx** — referenced in build brief §4 ("central tracker xlsx referenced but missing"). Not located during this build pass.

## 5. Competitor / market intelligence (not our performance, but adjacent)
- `01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Ads\` + `Weekly Contents\` — live, unmigrated, 10-category library, briefs through 2026-07-06. Tier 4 at best (observed market usage, not our data).

## 6. Net position
There is currently **no way to pull live REI ad-performance numbers into this workspace.** Every number in `10_PERFORMANCE/HISTORICAL_BASELINE.md` is from the single archived Codex snapshot dated through 2026-06-24. Closing this loop (read access or CSV export from the live `.gsheet` dashboards) is priority 2 in the marketing view of current priorities (build brief §9) and is `00_COMMAND_CENTER/DECISIONS_REQUIRED.md` item 3.

## READS FROM
`08_OPERATIONS/`, archived Codex folder (read-only), MAS HQ folder (read-only)

## FEEDS INTO
`10_PERFORMANCE/HISTORICAL_BASELINE.md`, `10_PERFORMANCE/IMPORT_SPECS.md`, `00_COMMAND_CENTER/DECISIONS_REQUIRED.md`
