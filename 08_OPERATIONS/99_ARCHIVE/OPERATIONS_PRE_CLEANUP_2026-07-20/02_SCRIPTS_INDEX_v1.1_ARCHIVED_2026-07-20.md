# _INDEX — 02_SCRIPTS

Version: v1.1
Status: APPROVED MASTER
Date: 2026-07-13
Supersedes: v1.0 (2026-07-10) — added rescued v9.0 rebuild package (undeployed)
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\01_DASHBOARD_TRACKING_SYSTEM\`

## Purpose
Live automation scripts that pull ad and CRM data into the REI performance dashboard.

## Files

| File | Description |
|---|---|
| `REI_AppsScript_ACTIVE_v8.43.gs` | Google Apps Script — renders the CEO/Overview dashboard web app (leads funnel, Meta/Google/GHL sync, creative tables). **This is the ACTIVE, deployed version.** |
| `REI_GoogleAds_Script_ACTIVE_v8.gs` | Google Ads-native script — pulls campaign performance data into the master sheet the dashboard reads |
| `SCRIPTS_README.md` | What each script does, where it's deployed, dependencies, version notes |
| `REI_PERFORMANCE_OS_V9/` | **RESCUED 2026-07-13, UNDEPLOYED.** Full v9.0 Apps Script rebuild source + deployment package, presented as a supersession of v8.43 above. Never deployed, never reviewed. See `REI_PERFORMANCE_OS_V9/00_RESCUE_NOTE.md` — **PENDING EDMUND DECISION: deploy v9 or stay on v8.43.** |

## READS FROM
- `01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md` (rules these scripts implement)

## FEEDS INTO
- `01_E.C.O.S/07_OPERATIONS_DESK.md` (owns dashboard/script maintenance)
- `01_E.C.O.S/04_MARKETING_ADS_DESK.md` (consumes ad performance data)

## Pending Edmund approval (CANDIDATE)
None — both scripts are ACTIVE/production.

## Note
Not copied: `~$I_AppsScript_v8.35.gs` (Excel/Office lock file artifact in legacy folder, not a real script — excluded).
