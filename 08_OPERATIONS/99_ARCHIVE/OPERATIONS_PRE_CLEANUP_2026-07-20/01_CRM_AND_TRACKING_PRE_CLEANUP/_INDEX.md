# _INDEX — 01_CRM_AND_TRACKING

Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\`

## Purpose
CRM, pipeline, dashboard, reporting, and nurture rules for Client Edition. The measurement and execution-control layer — how leads, bookings, ad performance, follow-up, and database movement are tracked and governed.

## Files

| File | Description |
|---|---|
| `00_OPERATIONS_AND_TRACKING_INDEX_v2.0.md` | Folder map, ownership boundaries (what Operations owns vs. Content Marketing vs. Knowledge Vault vs. Client OS), clean-saving rule |
| `01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` | CRM structure, lead quality scoring, booking status, pipeline stages |
| `02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md` | Dashboard architecture, ad performance tracking, creative intelligence, automation script ownership |
| `03_REPORTING_FOLLOW_UP_AND_HANDOFF_RULES_v2.0.md` | Reporting cadence, follow-up rhythm, campaign-learning handoff rules |
| `04_NURTURE_REACTIVATION_AND_DATABASE_MOVEMENT_SYSTEM_v2.0.md` | Nurture/reactivation logic, timing triggers, database movement without chasing |

All five files are current masters (v2.0, ACTIVE SOURCE FILE status in the legacy folder) — copied as-is with updated version headers. No content rewrite.

## READS FROM
- `00_COMMAND_CENTER` (operating rules, priorities)
- `02_SCRIPTS` (the automation scripts these dashboards run on)

## FEEDS INTO
- `01_E.C.O.S/07_OPERATIONS_DESK.md` (desk that operates this system)
- `04_CONTACT_DATABASE_REGISTRY.md` (contact data quality referenced by CRM rules)

## Pending Edmund approval (CANDIDATE)
None — all files carried APPROVED MASTER status from source.

## Gaps
None found in source folder beyond what's listed. `01_DASHBOARD_TRACKING_SYSTEM` legacy subfolder held only the two `.gs` scripts (now in `02_SCRIPTS`) — no separate dashboard doc existed there.
