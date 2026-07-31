# _INDEX — 08_OPERATIONS

Version: v1.4
Status: APPROVED MASTER
Date: 2026-07-17
Supersedes: v1.3 (2026-07-13) — rescued REI Performance OS v9.0 (undeployed rebuild) into `02_SCRIPTS/REI_PERFORMANCE_OS_V9/` ahead of legacy folder archiving. v1.4 corrects the `06_CONTACT_MASTER/` line below: per Decision 093/095 (2026-07-16 PII migration), that folder no longer lives under this AI OS drive — it relocated to the restricted private drive. Also notes Phase 2 label-by-label sweep (Decisions 096–100, 2026-07-16/17) essentially complete across all discovered vocabulary.
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\`, `H:\Shared drives\00_E.C.O.S\Scheduled\`, `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\Templates\`, `H:\Shared drives\00_E.C.O.S\_MIGRATION_TO_WINDOWS\`, `H:\Shared drives\00_E.C.O.S\X-Singapore Real Estate Insider - MAS HQ\02_CLIENTS\`, `H:\Shared drives\00_E.C.O.S\Artifacts\zoom-summary-generator\`

## Purpose
The measurement, automation, and execution-control layer for the whole business — CRM/pipeline rules, dashboards and their scripts, scheduled automations, and registries for the contact database and Zoom summary tool. This is what `01_E.C.O.S/07_OPERATIONS_DESK.md` runs on.

## Structure

| Item | Description |
|---|---|
| `01_CRM_AND_TRACKING/` | CRM pipeline, lead quality, dashboard/ad tracking, reporting/handoff, and nurture/reactivation rules (5 files, v2.0, all APPROVED MASTER) |
| `02_SCRIPTS/` | The two live scripts (`REI_AppsScript_ACTIVE_v8.43.gs`, `REI_GoogleAds_Script_ACTIVE_v8.gs`) that run the performance dashboard, plus a README — and `REI_PERFORMANCE_OS_V9/`, a rescued but **UNDEPLOYED** v9.0 rebuild package pending Edmund's deploy decision |
| `03_AUTOMATIONS/` | Live scheduled-task skills, the task-template standard, and 5 rescued agent prompts recovered from the pre-Windows-migration Cowork session archive |
| `04_CONTACT_DATABASE_REGISTRY.md` | Registry + urgent status flag for the contact database and its in-flight GHL cleanup/import project |
| `05_ZOOM_SUMMARY_TOOL_REGISTRY.md` | Registry for the live Zoom summary generator Artifact and its supporting (partly duplicated) Google Doc guides |
| `06_CONTACT_MASTER/` | **RELOCATED (Decision 093/095, 2026-07-16) — no longer under this drive.** Now lives at `H:\Shared drives\00_E.C.O.S_CLIENTS_PRIVATE\02_CLIENTS_AND_CONTACTS_PRIVATE\03_MASTER_CONTACT_DATABASE\06_CONTACT_MASTER\` (restricted PII drive). History: consolidated deduplicated contact master — v1.3, 17,663 contacts from 122,433 source rows, names cleaned + labels standardized (Decision 050). GHL import **COMPLETE 2026-07-13**: 7,225/7,314 imported (98.7%), 89 excluded bad-phone (Decision 081), 87 DNC contacts DND-enforced via API (Decision 082). **Phase 2 label-by-label sweep (Decisions 096–100, 2026-07-16/17) essentially complete** — Stacked, Webinar, Ads/VSL/Meta, YT/Referral/App/X, Insider/PWP/PWP Attend/Consult all executed; see `04_CONTACT_DATABASE_REGISTRY.md` for detail and the open next-step (last-name description QA pass, not yet started). |

## READS FROM
- `00_COMMAND_CENTER` (operating rules, priorities — read before any operations work)
- `03_CLIENT_ADVISORY_OS` (the advisory logic that CRM stages and follow-up rules must support)

## FEEDS INTO
- `01_E.C.O.S/07_OPERATIONS_DESK.md` (the desk that owns this entire branch)
- `01_E.C.O.S/04_MARKETING_ADS_DESK.md` (consumes dashboard/ad tracking data and the Friday performance report prompt)
- `01_E.C.O.S/03_CONTENT_STUDIO.md` (consumes the rescued weekly content intelligence prompt and the live `rei-weekly-content-brief` skill)
- `01_E.C.O.S/05_AGENT_RECRUITMENT_DESK.md` (partial — MAS agent coaching automation pointer, currently thin, see `03_AUTOMATIONS/_INDEX.md`)

## Pending Edmund approval (CANDIDATE)
None net-new. All copied CRM/tracking files carried forward their existing APPROVED MASTER status. Rescued prompts are tagged REGISTRY (historical record) — promote to CANDIDATE/APPROVED MASTER only if Edmund chooses to reactivate one as a live scheduled task.

## Flags for QA / Edmund attention
1. **Contact database: GHL import COMPLETE (2026-07-13).** Full import ran 00:24–00:30: 7,225/7,314 success (98.7%), 89 excluded on bad phone (Decision 081, no recovery), zero duplication (Create-and-update mode, dedupe on Contact ID), zero automation fired. 8 custom fields pre-created live; 87 DNC contacts DND-enforced via API (Decision 082, workflow build deferred to manual). Runbook corrected as `06_CONTACT_MASTER/GHL_REIMPORT_PLAN_v1.2_2026-07-13.md` (v1.1 superseded in place). Legacy sources may now be archived only under **separate** Edmund/Cindior approval. See `04_CONTACT_DATABASE_REGISTRY.md`.
2. **Zoom Summary guide duplication** — three of six `.gdoc` guides have an unresolved "_CORRECTED" twin. See `05_ZOOM_SUMMARY_TOOL_REGISTRY.md`.
3. **REI Ads Creative & Reporting Intelligence dashboard prompt not recoverable** — the named session in the migration archive had no real content (`initialMessage` = "its a success..."). See `03_AUTOMATIONS/PROMPT_REI_Ads_Creative_Reporting_Dashboard_RESCUED.md` for the full finding. If a real version of this automation exists, it wasn't in this migration snapshot — ask Edmund/Cindior.
4. **MAS Agent Coaching Programme prompt is thin** — rescued session content is a continuation/status message, not the actual coaching programme build. See file for detail; may need a fresh brief from Edmund/Cindior if this automation is wanted.
5. Legacy `01_DASHBOARD_TRACKING_SYSTEM` folder contained a stray Excel lock file (`~$I_AppsScript_v8.35.gs`) — correctly excluded from the copy, noted here for completeness.
6. **REI Performance OS v9.0 rescued 2026-07-13, UNDEPLOYED.** Full Apps Script rebuild package copied into `02_SCRIPTS/REI_PERFORMANCE_OS_V9/` from the legacy dashboard-tracking folder before it moves to archive. Presents itself as superseding the active v8.43 build but has never been deployed or reviewed. One non-content file (`REI_Performance_OS_MASTER_SHEET_v9.0.gsheet`, a Google Drive shortcut/pointer, not real data) failed to copy due to a Drive-streaming read error — the underlying Google Sheet itself is unaffected. **PENDING EDMUND DECISION: deploy v9 or stay on v8.43** — see `02_SCRIPTS/REI_PERFORMANCE_OS_V9/00_RESCUE_NOTE.md`.
