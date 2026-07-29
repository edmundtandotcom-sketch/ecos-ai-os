# OBJECTION_REGISTRY_SPEC
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: OBJECTION_REGISTRY.csv; OBJECTION_INTELLIGENCE_SYSTEM.md

## Purpose
Indexes objection *categories* (seed rows keyed to the 15 Objection Bank categories / RB blocks). Per-instance objection records follow the full schema in OBJECTION_INTELLIGENCE_SYSTEM.md §2 and are logged operationally (CRM / branch 21), not stored as raw verbatim here (PII stays on E:).

## Columns
| Column | Definition | Controlled values |
|---|---|---|
| `objection_id` | Stable ID | OBJ-CAT-xxx (seed) / OBJ-NNNN (instance) |
| `category` | One of 7 folders | TRUST / TIMING / FINANCIAL / SPOUSE_AND_FAMILY / PROPERTY / PROCESS / DECISION |
| `belief_block` | RB block(s) | RB-01..RB-18 (semicolon-separated) |
| `approx_freq` | Approx count from 376-row table | number / range / NA |
| `resistance_level` | Severity | L1 / L1.5 / L2 / L3 / L4 (ranges allowed) |
| `source_master_path` | Master path | path |
| `evidence_tier` | Backing | T1–T7 (category seeds = T3) |
| `pii_status` | PII exposure | none / PII-raw-Edrive |
| `owner` | Desk | free text |
| `notes` | One-liner | free text |

## Rule
Frequency figures are approximate (multi-tag rows inflate totals) — for prioritisation, not precision (per Objection Bank reliability caveat). Never store attributable client quotes in this OS. `[T3, HARD RULE 5]`
