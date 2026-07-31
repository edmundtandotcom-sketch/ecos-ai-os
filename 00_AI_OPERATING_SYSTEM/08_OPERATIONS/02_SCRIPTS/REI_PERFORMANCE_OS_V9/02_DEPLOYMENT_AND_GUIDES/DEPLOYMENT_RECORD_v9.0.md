# REI Performance OS v9.0 — Deployment Record
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-31
Supersedes: none (new file)
Sources: `DEPLOYMENT_CHECKLIST.md`; live deployment performed 2026-07-31 via clasp as `admin@thereimethod.com`.

**Keep this file.** It holds the identifiers needed to update or roll back v9 without rebuilding anything.

## ⚠️ There were TWO v9 projects on this sheet. Only ONE is canonical.

Discovered 2026-07-31: the sheet already had a container-bound v9 project created 2026-07-13 with its own live web app. A second project was created the same day via clasp before this was known. Both served working web apps simultaneously — the same parallel-deployment trap as the diagnostic app. **Resolved: the July project is canonical; the duplicate was undeployed.**

**Rule: always open the script via the sheet → Extensions → Apps Script.** That is the canonical project. Never create a second bound project for this sheet.

## Live identifiers — CANONICAL

| Item | Value |
|---|---|
| Apps Script project | `(Weekly Ads Dashboard) REI Performance OS v9.0` |
| Script ID | `1KlPAiYWKZ_0xmK9ErqARBjkLDrJ5pXYTCuKdDXYwuTgR8ABr8QKxgq20` |
| Script editor | https://script.google.com/d/1KlPAiYWKZ_0xmK9ErqARBjkLDrJ5pXYTCuKdDXYwuTgR8ABr8QKxgq20/edit |
| Opens from | Sheet → **Extensions → Apps Script** (this is why it is canonical) |
| Bound sheet | `(Weekly Ads Dashboard) REI_Performance_OS_MASTER_SHEET_v9.0` |
| Sheet ID | `167C_gZsN5RtImBFArt5hXcUqMAHlfJFqX52f0rN_pWk` |
| Deployment | `AKfycbzdJ7VILpfty4TL7P76y6drQtkcmw0Dt2_Vai-cUFGZKWeZNia_QnuwiaQd5naerQzF` @3 |
| Web app URL | https://script.google.com/macros/s/AKfycbzdJ7VILpfty4TL7P76y6drQtkcmw0Dt2_Vai-cUFGZKWeZNia_QnuwiaQd5naerQzF/exec |
| Verified | HTTP 200, serving `REI Performance OS v9.0.1` access-key screen, running the fixed code |

## Retired duplicate — do not use

| Item | Value |
|---|---|
| Project | `REI Performance OS v9.0` (no "(Weekly Ads Dashboard)" prefix) |
| Script ID | `1fBoZzks1qaWenl-UU7l9vyipv4VXvUHdkcDQ4bO6ejFpYilkHApyNH_C` |
| Status | **All deployments deleted 2026-07-31 — web app returns HTTP 404.** Inert: no web app, no triggers. |
| Cleanup | Safe to delete the project file from Drive. Retained-but-inert is also acceptable; it cannot run or serve. |

## What was done 2026-07-31 (checklist sections A and C)

- Created the Apps Script project **bound to the v9 sheet** (verified by title before creating — the live v8.43 system was never touched).
- Pushed the fast-path file set per checklist A.5: `REI_AppsScript_v9.0_ALL_IN_ONE.gs` → `Code.gs`, plus `Dashboard.html`, `Styles.html`, `Client.html`. The numbered `00_Config.gs`–`07_Setup.gs` files were deliberately **not** pushed — pushing both would duplicate every function.
- Restored the project manifest to the supplied v9 version. **Note:** project creation overwrites `appsscript.json` with a default (`America/New_York`, no `webapp` block). It was replaced with the correct `Asia/Singapore` + `executeAs: USER_DEPLOYING` + `access: ANYONE_ANONYMOUS` manifest before pushing. Re-check this on any future recreate.
- Created web-app deployment `@1`, described "REI Performance OS v9.0 production".

## Status: LIVE — authorized, setup run, web app serving

- **2026-07-31 14:47 SGT** — `setupV9` completed cleanly (execution log: "REI Performance OS v9 setup complete"). Scopes authorized by `admin@thereimethod.com`.
- **Web app verified: HTTP 200**, title `REI Performance OS v9.0.1`, serving the REI access-key screen (not a Google account chooser) — checklist §C.7 satisfied.
- Still pending: credentials, manual sync, triggers, Google Ads script. **v8.43 remains the system of record.**

## Two source bugs found and fixed during deployment

Both were in the generated `ALL_IN_ONE` bundle and had never surfaced because v9 had never been run.

1. **`ReferenceError: stageRank_ is not defined`** (`rebuildDailyFunnelFact_`). The helper is named `statusRank_`; the modular `02_DataService.gs` calls it correctly, but the bundle used `stageRank_` in the funnel block — a name defined nowhere. 6 occurrences corrected.
2. **`Cannot call SpreadsheetApp.getUi() from this context`** (`setupV9`). `getUi()` is unavailable from the script editor and from time-based triggers. Setup did all its real work then died on a cosmetic completion popup. Added a context-safe `uiAlert_()` helper (falls back to `console.log`) and routed the four alert-only calls through it. This also repaired `runFullSyncFromEditor` and `runHealthCheckFromEditor`, which were named for editor use yet called `getUi()` directly and could never have worked. `onOpen` and `promptProperty_` still use `getUi()` deliberately — they need the sheet UI, so **credential entry must be done from the sheet menu, not the editor.**

**Anyone regenerating `ALL_IN_ONE` from the numbered modular files must re-check both.**

## Remaining steps (owner only)

1. ~~Run `setupV9` and approve permissions~~ — **DONE 2026-07-31.**
2. Refresh the sheet, then use the new **REI Performance OS v9** menu to store: Dashboard access key · Meta access token · GHL private integration key. Must be done from the sheet menu (see bug 2).
3. In **Project Settings → Script Properties**, add: `SHEET_ID` (value above), `META_AD_ACCOUNT_ID` (`act_...`), `META_API_VERSION`, `GHL_LOCATION_ID`, `GHL_PIPELINE_ID`, `GOOGLE_ADS_CUSTOMER_ID`.
4. Run **REI Performance OS v9 → Run full sync now**. Resolve anything appearing in `Error_Log`.
5. Only after a clean manual sync: **Install safe sync triggers**.
6. Re-test the web app URL in an Incognito window — it must show the REI access-key screen, not a Google account chooser.
7. Install `REI_GoogleAds_Script_v9.0.gs` in Google Ads (Tools → Bulk actions → Scripts), schedule daily 06:00 SGT.

## Cutover rule (unchanged)

**v8.43 remains the system of record.** Keep its `/exec` URL active until v9 passes three consecutive clean days of checks (per `DEPLOYMENT_CHECKLIST.md` §F). If v9 fails, continue on v8.43 and inspect `Error_Log`; archived source and the original master sheet are untouched.

## Updating the code later

The clasp staging directory is temporary. To push a new version: create a folder containing the source files plus a `.clasp.json` holding the Script ID and Sheet ID above, then `clasp push`. Source of truth for the code remains `01_SOURCE_CODE/` in this folder.
