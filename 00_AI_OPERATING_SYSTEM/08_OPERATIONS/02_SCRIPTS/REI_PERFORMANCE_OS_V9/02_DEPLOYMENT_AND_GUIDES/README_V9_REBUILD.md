# REI Performance OS v9.0 — Rebuild Package

## What this rebuild changes

- Preserves the existing v8.43 dashboard and source files as rollback copies.
- Uses a new v9 master spreadsheet copied from the existing live data.
- Replaces browser-side `fetch(.../exec?action=...)` polling with `google.script.run`.
- Separates browser display from server-side scheduled data syncing.
- Uses `LockService` to prevent overlapping writes.
- Adds full Meta pagination, retry handling, sync logs, error logs and health checks.
- Adds immutable daily performance and daily funnel fact tables.
- Adds conservative, base and aggressive forecasting.
- Hides phone numbers and email addresses from the mobile dashboard.
- Uses an app access key so the web app can be deployed as “Execute as me / Anyone” without relying on whichever Google account Chrome chooses.

## Main files

**Fastest deployment option:** use `REI_AppsScript_v9.0_ALL_IN_ONE.gs` as the only server-side `.gs` file, plus the three HTML files and manifest. Do not also paste the numbered `.gs` files when using the all-in-one version.

**Modular development option:**

1. `00_Config.gs`
2. `01_EntryPoints.gs`
3. `02_DataService.gs`
4. `03_MetaSync.gs`
5. `04_GHLSync.gs`
6. `05_Forecast.gs`
7. `06_LogsHealth.gs`
8. `07_Setup.gs`
9. `Dashboard.html`
10. `Styles.html`
11. `Client.html`
12. `appsscript.json`
13. `REI_GoogleAds_Script_v9.0.gs`

## New master sheet

`REI_Performance_OS_MASTER_SHEET_v9.0`

The old sheet remains untouched. The new sheet includes all copied historical tabs plus:

- Daily_Performance_Fact
- Daily_Funnel_Fact
- Forecast_Assumptions
- Forecast_Scenarios
- Forecast_Output
- Forecast_vs_Actual
- Stage_Map
- Sync_Log
- Error_Log
- Audit_Log
- Health_Check
- Config_v9

## Important boundary

The files in this folder are complete source and migration assets. A Google Apps Script deployment cannot be activated merely by uploading `.gs` and `.html` files to Drive. The files must be pasted/imported into the Apps Script project bound to the v9 master sheet, authorised, and deployed using the steps in `DEPLOYMENT_CHECKLIST.md`.
