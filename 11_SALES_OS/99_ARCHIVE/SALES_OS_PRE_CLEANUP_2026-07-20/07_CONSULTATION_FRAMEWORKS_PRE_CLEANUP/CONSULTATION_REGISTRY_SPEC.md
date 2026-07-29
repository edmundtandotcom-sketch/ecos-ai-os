# CONSULTATION_REGISTRY_SPEC
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: CONSULTATION_REGISTRY.csv (this branch); FRAMEWORK_LIFECYCLE.md; MASTER_CONSULTATION_FLOW.md

## Purpose
Defines the columns of `CONSULTATION_REGISTRY.csv` — the index of every consultation framework, where its master lives, where it plugs into the flow, and its lifecycle status. The CSV points to masters; it never copies their content.

## Columns
| Column | Definition | Controlled values |
|---|---|---|
| `framework_id` | Stable ID | CF-NN |
| `framework_name` | Human name + version | free text |
| `master_file_path` | Full path to the APPROVED master (blank if none) | path |
| `flow_phase` | Where it plugs into MASTER_CONSULTATION_FLOW | P1 / P2 / P3 / P4 / P5 / P6 / P3-Anchor3 / ranges / `-` |
| `lifecycle_status` | Status per FRAMEWORK_LIFECYCLE §2 | Active / Experimental / Supported / Validated / Context-specific / Superseded / Deprecated / Retired (+ qualifier suffix) |
| `evidence_tier` | Highest evidence tier backing the framework | T1–T7 |
| `owner` | Accountable desk | Advisory Desk / Strategy Office / Operations Desk |
| `last_reviewed` | ISO date | YYYY-MM-DD |
| `notes` | One-liner | free text |

## Update rule
Add a row when a new framework enters the OS; change `lifecycle_status` only via Edmund/Cindior approval, logged in `29_CHANGE_LOG`. Never delete a row — retire it.
