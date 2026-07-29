Title: 00_RESCUE_NOTE — REI Performance OS v9.0 Rebuild
Version: v1.0
Status: REGISTRY
Date: 2026-07-13
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\01_DASHBOARD_TRACKING_SYSTEM\REI_PERFORMANCE_OS_V9_REBUILD\` (read-only, unchanged)

## What this is
Full Apps Script source and deployment package for a v9.0 rebuild of the REI Performance OS dashboard — the same system whose older v8.43 build is the currently ACTIVE, deployed version at `08_OPERATIONS/02_SCRIPTS/` (`REI_AppsScript_ACTIVE_v8.43.gs`, `REI_GoogleAds_Script_ACTIVE_v8.gs`). This v9.0 rebuild existed only in the legacy folder and was never carried into the AI OS — rescued here 2026-07-13 ahead of the legacy folder moving to `_ARCHIVE`.

## Status: UNDEPLOYED
This package has **not been deployed**. The live, production dashboard everyone is running today is still **v8.43** (`08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs`). v9.0 is a complete rebuild sitting ready to ship, not the active system.

## Contents
- `01_SOURCE_CODE/` — full v9.0 Apps Script source (Config, EntryPoints, DataService, MetaSync, GHLSync, Forecast, LogsHealth, Setup, Dashboard/Styles/Client HTML, appsscript.json manifest, plus the Google Ads-side script) and an all-in-one combined script
- `02_DEPLOYMENT_AND_GUIDES/` — README, deployment checklist, Chrome/mobile access notes, migration & QA plan
- `03_ARCHIVE_AND_ROLLBACK/` — copies of the currently-active v8.43 scripts, included by the original package as a rollback safety net
- `REI_Performance_OS_v9.0_SOURCE_PACKAGE.zip` — zipped copy of the source package
- `REI_Performance_OS_MASTER_SHEET_v9.0.gsheet` — **NOT copied.** This is a Google Drive shortcut/pointer file to a live Google Sheet, not real file content; it failed to copy locally (Drive-streaming read error, not a data-loss issue). The underlying Google Sheet is unaffected and still reachable directly in Drive — Edmund/Cindior should re-link it here manually if wanted, or note its Sheet URL in this file.

## Supersedes v8.43 — pending decision
This rebuild is presented by its own README as superseding the active v8.43 build (new source architecture, forecast module, logs/health module, setup module — v8.43 has none of these as separate files). It has not been reviewed or approved for production.

## EDMUND RULING (2026-07-13)
This is an **important working HTML ads-tracking dashboard — KEEP it here in Operations** as a future-improvement asset. Edmund: "we will want to improve this version in future." So there is **no deploy-vs-v8.43 decision to force now** — v9.0 stays filed here as the base we iterate on; the live **v8.43 remains the system of record** until a dedicated future improvement + deployment pass is scheduled. Reference material for that pass: `02_DEPLOYMENT_AND_GUIDES/README_V9_REBUILD.md`, `DEPLOYMENT_CHECKLIST.md`, `MIGRATION_AND_QA_PLAN.md`.
