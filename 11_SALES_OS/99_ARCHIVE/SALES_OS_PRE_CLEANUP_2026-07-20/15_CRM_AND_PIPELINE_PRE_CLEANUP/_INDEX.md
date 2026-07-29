# _INDEX — 15_CRM_AND_PIPELINE

Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`GHL_LIVE_AUDIT_2026-07-11.md`, orchestrator scratchpad) · `SALES_OS_BUILD_SPEC_v1.md` (Fable, orchestrator) · `11_SALES_OS\CLAUDE.md`

Purpose: CRM & pipeline architecture for the "1-To-1 Pipeline" (GHL, 397 live opportunities) — the reconciled pipeline design, field plan, data dictionary, reporting-readiness map, proposed automations, and weekly QA checklist. This is a **deep-build** branch (Decision 051.4).

This branch does not hold consultation content, objection scripts, or closing frameworks — those live in `07_CONSULTATION_FRAMEWORKS`, `11_OBJECTION_INTELLIGENCE`, `12_CLOSING_AND_DECISION`. This branch holds the CRM mechanics that record and report on that work.

## Files
- `PIPELINE_ARCHITECTURE.md` — resolves SC-01 (four pipeline definitions). Live 10-stage truth + SOP 7-stage intent + Apps Script mismatch → one target architecture: keep the live 10 stages, map SOP names onto them, define stage-entry/exit criteria, force outcome capture at Won/Lost/Unqualified. 3 DECISION REQUIRED items for Edmund.
- `CRM_FIELDS.md` — gap table (missing + duplicated fields), OPPORTUNITY-vs-CONTACT placement rule, consolidation map, Changi Green co-mingling governance flag, cross-reference against `GHL_REIMPORT_PLAN_v1.1` (no conflict found).
- `DATA_DICTIONARY.md` — every proposed/consolidated field: object, type, allowed values (pointing to `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` for outcome/lost-reason codes, not duplicated), who sets it, when, validation rule.
- `CRM_QA.md` — weekly hygiene checklist: stage accuracy, outcome completeness, field fill rates, One Contact One Opportunity One Truth, staleness review.
- `REPORTING\METRICS.md` (+ `_INDEX.md`) — mandate §15 metric families, each marked COMPUTABLE TODAY or BLOCKED with the unblocking fix; reverse-engineering funnel math template (mostly UNKNOWN pending outcome tracking).
- `AUTOMATIONS\PROPOSED.md` (+ `_INDEX.md`) — stub-level, none built: stage-exit enforcement, stale-lead nudge, speed-to-lead timer.

## Headline Findings (T2, live audit 2026-07-11)
397 live opportunities, 9 months of history, `status: open` on 397/397 — Won and Lost have never held a single record. 71% of volume sits in New Lead + Booked Call, 36% stale 30+ days. 0 custom fields on the opportunity object; all deal-scoped data is wrongly parked on the contact object. The core defect is not a missing report — it's that the pipeline has never once been required to record an outcome.

## READS FROM
`GHL_LIVE_AUDIT_2026-07-11.md` · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\` (all 3 SOPs) · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\02_SCRIPTS\REI_AppsScript_ACTIVE_v8.43.gs` · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\06_CONTACT_MASTER\GHL_REIMPORT_PLAN_v1.1_2026-07-11.md` · `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md` · `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` (pointer, WS-B) · `11_OBJECTION_INTELLIGENCE\` (pointer, WS-B)

## FEEDS INTO
`00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` (SC-01 resolution proposal, Changi Green co-mingling) · `00_COMMAND_CENTER\DECISIONS_REQUIRED.md` (3 items from `PIPELINE_ARCHITECTURE.md` §6) · `01_E.C.O.S\07_OPERATIONS_DESK.md` (build owner for any approved automation/script work) · `22_SALES_ANALYTICS` (STUB, future deep-build)
