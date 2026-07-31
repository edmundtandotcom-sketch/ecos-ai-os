# REI Performance OS v9.0 — Deployment Record
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-31
Supersedes: none (new file)
Sources: `DEPLOYMENT_CHECKLIST.md`; live deployment performed 2026-07-31 via clasp as `admin@thereimethod.com`.

**Keep this file.** It holds the identifiers needed to update or roll back v9 without rebuilding anything.

## Live identifiers

| Item | Value |
|---|---|
| Apps Script project | `REI Performance OS v9.0` |
| Script ID | `1fBoZzks1qaWenl-UU7l9vyipv4VXvUHdkcDQ4bO6ejFpYilkHApyNH_C` |
| Script editor | https://script.google.com/d/1fBoZzks1qaWenl-UU7l9vyipv4VXvUHdkcDQ4bO6ejFpYilkHApyNH_C/edit |
| Bound sheet | `(Weekly Ads Dashboard) REI_Performance_OS_MASTER_SHEET_v9.0` |
| Sheet ID | `167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk` |
| Deployment ID | `AKfycbwPOxtVYkLWxwlmP6PmclOT52UHFEoKr8oQGlxFTfCbQeqj5CEc9YEdlOBsSyJXeSL-BQ` |
| Web app URL | https://script.google.com/macros/s/AKfycbwPOxtVYkLWxwlmP6PmclOT52UHFEoKr8oQGlxFTfCbQeqj5CEc9YEdlOBsSyJXeSL-BQ/exec |
| Deployed by | `admin@thereimethod.com` |

## What was done 2026-07-31 (checklist sections A and C)

- Created the Apps Script project **bound to the v9 sheet** (verified by title before creating — the live v8.43 system was never touched).
- Pushed the fast-path file set per checklist A.5: `REI_AppsScript_v9.0_ALL_IN_ONE.gs` → `Code.gs`, plus `Dashboard.html`, `Styles.html`, `Client.html`. The numbered `00_Config.gs`–`07_Setup.gs` files were deliberately **not** pushed — pushing both would duplicate every function.
- Restored the project manifest to the supplied v9 version. **Note:** project creation overwrites `appsscript.json` with a default (`America/New_York`, no `webapp` block). It was replaced with the correct `Asia/Singapore` + `executeAs: USER_DEPLOYING` + `access: ANYONE_ANONYMOUS` manifest before pushing. Re-check this on any future recreate.
- Created web-app deployment `@1`, described "REI Performance OS v9.0 production".

## Status: DEPLOYED BUT NOT YET AUTHORIZED

The web app currently returns **HTTP 403 Access denied**. This is expected and not a fault: an "Execute as me" web app cannot serve until the owning account has authorized the script's scopes at least once. That authorization is checklist section B and requires a human — it cannot be automated.

## Remaining steps (owner only)

1. Open the script editor (link above) → select `setupV9` in the function dropdown → **Run** → approve the permission prompt. On the "Google hasn't verified this app" screen choose **Advanced → Go to REI Performance OS v9.0**.
2. Refresh the sheet, then use the new **REI Performance OS v9** menu to store: Dashboard access key · Meta access token · GHL private integration key.
3. In **Project Settings → Script Properties**, add: `SHEET_ID` (value above), `META_AD_ACCOUNT_ID` (`act_...`), `META_API_VERSION`, `GHL_LOCATION_ID`, `GHL_PIPELINE_ID`, `GOOGLE_ADS_CUSTOMER_ID`.
4. Run **REI Performance OS v9 → Run full sync now**. Resolve anything appearing in `Error_Log`.
5. Only after a clean manual sync: **Install safe sync triggers**.
6. Re-test the web app URL in an Incognito window — it must show the REI access-key screen, not a Google account chooser.
7. Install `REI_GoogleAds_Script_v9.0.gs` in Google Ads (Tools → Bulk actions → Scripts), schedule daily 06:00 SGT.

## Cutover rule (unchanged)

**v8.43 remains the system of record.** Keep its `/exec` URL active until v9 passes three consecutive clean days of checks (per `DEPLOYMENT_CHECKLIST.md` §F). If v9 fails, continue on v8.43 and inspect `Error_Log`; archived source and the original master sheet are untouched.

## Updating the code later

The clasp staging directory is temporary. To push a new version: create a folder containing the source files plus a `.clasp.json` holding the Script ID and Sheet ID above, then `clasp push`. Source of truth for the code remains `01_SOURCE_CODE/` in this folder.
