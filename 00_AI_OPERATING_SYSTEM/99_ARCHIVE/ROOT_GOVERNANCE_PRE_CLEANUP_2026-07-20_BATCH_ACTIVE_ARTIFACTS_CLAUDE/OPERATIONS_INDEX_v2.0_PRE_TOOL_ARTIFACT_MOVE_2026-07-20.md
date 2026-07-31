# 08_OPERATIONS — _INDEX
Version: v2.0
Status: APPROVED MASTER — LIVE VERIFIED 2026-07-20
Date: 2026-07-20
Supersedes: v1.4 and the pre-cleanup CRM/tracking structure.
Sources: AI OS CLAUDE.md v4.5; Decisions 071 and 107; live Drive audit 2026-07-20.

## Purpose

Operations owns implementation: GHL configuration, fields, workflows, dashboards, tracking, automation, registries and operational QA.

It does not own sales-stage meaning, sales follow-up policy, nurture strategy, consultation methodology, contact PII or software source-of-truth repositories.

## Required orchestration header

> you are the orchestrator, delegated the building to sonnet 5, opus 4.8, and never spawn another fable 5 agent. you plan, you delegate to cheaper model and you do the QA at the end. /compact

## Active map

| Item | Status | Purpose |
|---|---|---|
| `01_CRM_AND_TRACKING/` | APPROVED | CRM implementation boundary, data dictionary, automation requirements, QA and dashboard governance |
| `02_SCRIPTS/` | ACTIVE | Apps Script registry and controlled script assets |
| `03_AUTOMATIONS/` | ACTIVE | Prompt/skill automation registry and operational templates |
| `04_CONTACT_DATABASE_REGISTRY.md` | APPROVED POINTER | Sanitized routing/status pointer; private contact data remains outside the general AI OS |
| `05_ZOOM_SUMMARY_TOOL_REGISTRY.md` | APPROVED POINTER | Tool-purpose and repository routing record |
| `99_ARCHIVE/` | READ ONLY | Pre-cleanup structure and superseded indexes |

## Boundary table

| Question | Owner |
|---|---|
| What does a sales stage mean, and when should a person advance? | `11_SALES_OS/04_PIPELINE_MOVEMENT` |
| How is that stage, rule or outcome implemented in GHL? | Operations |
| How is a Strategy Session diagnosed and delivered? | `03_CLIENT_ADVISORY_OS` |
| Where do named contacts, exports and contact history live? | `00_E.C.O.S_CLIENTS_PRIVATE` |
| Where do live campaign working files live? | `03_ACTIVE_CAMPAIGNS` |
| Where does source code/runtime live? | Local runtime/private Git; Drive only for governed recovery artifacts or registries |

## Change control

1. Read the Sales movement specification before changing pipeline configuration.
2. Confirm live GHL state before quoting stages, counts, fields or workflow status.
3. Record implementation changes and QA evidence.
4. Never copy PII into this branch.
5. Archive replaced documentation before structural changes.
6. Keep the v9 script as a future improvement asset; v8.43 remains the live system of record until separately built, tested and released.

## READS FROM

- AI OS root and Command Center
- `11_SALES_OS/04_PIPELINE_MOVEMENT`
- relevant campaign handoff in `03_ACTIVE_CAMPAIGNS`

## FEEDS INTO

- GHL implementation
- operational dashboards and QA
- Sales and Marketing execution
