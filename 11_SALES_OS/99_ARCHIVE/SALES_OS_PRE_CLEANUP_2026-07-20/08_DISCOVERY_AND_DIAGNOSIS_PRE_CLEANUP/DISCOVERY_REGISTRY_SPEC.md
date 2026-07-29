# DISCOVERY_REGISTRY_SPEC
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: DISCOVERY_REGISTRY.csv (this branch)

## Purpose
Indexes discovery/diagnosis assets — question sets, diagnostic models, archetype libraries, language vaults — with pointers to their masters. Points; never copies.

## Columns
| Column | Definition | Controlled values |
|---|---|---|
| `asset_id` | Stable ID | DQ-/DM-/AR- prefix |
| `asset_type` | Kind of asset | question-set / model / archetype-library / language-vault |
| `name` | Human name | free text |
| `category_or_model` | 8-category tag or model name | situation/motivation/problem/consequence/financial/decision/suitability/commitment / ascent / readiness / tiering / archetype / voice-of-client |
| `source_master_path` | Full path to master | path |
| `evidence_tier` | Backing tier | T1–T7 |
| `pii_status` | PII exposure | none / PII-raw-Edrive |
| `owner` | Accountable desk | free text |
| `notes` | One-liner | free text |

## Rule
Any asset with `pii_status = PII-raw-Edrive` is referenced in place — never mirrored into 11_SALES_OS (HARD RULE 5).
