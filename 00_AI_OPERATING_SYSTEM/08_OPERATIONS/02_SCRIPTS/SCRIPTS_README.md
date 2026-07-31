# SCRIPTS_README — 02_SCRIPTS

Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\01_DASHBOARD_TRACKING_SYSTEM\`

## Purpose
The two live scripts that feed the REI performance dashboard. Both are ACTIVE — do not replace without archiving the prior version first.

## REI_AppsScript_ACTIVE_v8.43.gs

- **What it is:** Google Apps Script powering the REI Creative Intelligence dashboard (web app bound to a Google Sheet).
- **What it does:** Renders the CEO/Overview dashboard — leads funnel (Lead → Responded → Booked Call → Appointment → Strategy Session → Closed), Meta/Google/GHL sync, campaign/ad-set/creative tables, YouTube creative playback, KPI cards, custom date-range picker.
- **Where deployed:** Bound to the master Google Sheet as a Web App (Apps Script editor → Deploy). Runs on `Sync Now` trigger and scheduled refresh.
- **Version history:** 4,329 lines; header comment block logs every change v8.24 → v8.43 (timezone fixes, UI polish, pipeline stage additions, sync-order fixes). Read the header before editing — each fix exists because something broke in production.
- **Dependencies:** Meta Ads API, Google Ads data (written by the companion script below), GHL pipeline data.

## REI_GoogleAds_Script_ACTIVE_v8.gs

- **What it is:** A Google Ads-native script (runs inside Google Ads UI, not Apps Script editor).
- **What it does:** Pulls campaign performance (Today / Yesterday / 7D / 14D / 30D / All Time + full daily history) and writes it into tabs on the same master Google Sheet that `REI_AppsScript_ACTIVE_v8.43.gs` reads from.
- **Where deployed:** Google Ads → Tools & Settings → Bulk Actions → Scripts. Scheduled daily at 6:00 AM SGT.
- **Setup:** One-time — paste script, confirm `MASTER_SHEET_ID` matches the target sheet, authorise Sheets + Ads access, run once for historical backfill, then create the daily schedule.
- **Key config:** `MASTER_SHEET_ID` and `SGD_RATE` (currency conversion for non-SGD accounts) at top of file.
- **Writes:** `Google_Campaigns_*` (Today/Yesterday/L7D/L14D/L30D/AllTime/legacy), `Google_AdGroups`, `Google_Ads`, `Google_Campaigns_Daily` (new in v8 — powers custom date-range picker).

## Operating Note
These two scripts are a matched pair — the Google Ads script writes the sheet tabs the Apps Script dashboard reads. Do not update one without checking the other for tab-name or schema compatibility.
