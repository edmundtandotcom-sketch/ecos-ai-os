# FOLLOW_UP_REGISTRY_SPEC
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: FOLLOW_UP_REGISTRY.csv; FOLLOW_UP_SYSTEM.md §3

## Purpose
Indexes the gap-based follow-up plays (one seed row per gap). Per-client follow-up instances follow the full schema in FOLLOW_UP_SYSTEM.md §3 and are logged in CRM (branch 15), not stored with PII here.

## Columns
| Column | Definition | Controlled values |
|---|---|---|
| `followup_id` | Stable ID | FU-<GAP> (seed) / FU-NNNN (instance) |
| `gap` | One of 7 gaps | CLARITY_GAP / TRUST_GAP / FINANCIAL_GAP / SPOUSE_GAP / TIMING_GAP / FEAR_GAP (+ suitability inside TIMING) |
| `belief_block` | RB block(s) | RB-01..RB-18 |
| `objective` | Single outcome the follow-up must produce | free text |
| `primary_asset` | Asset/case/framework sent (pointer) | free text |
| `channel` | Delivery | email / whatsapp / call / joint-session (platform-verify before send) |
| `timing` | Dated cadence | free text (must be dated, not "later") |
| `exit_condition` | What ends the follow-up | free text |
| `outcome_code` | Links to branch 12 OUTCOME_CODES | one of the 11 codes |
| `evidence_tier` | Backing | T1–T7 |
| `owner` | Accountable | free text |

## Rule
Every follow-up must add value or a decision (BANNED_FOLLOW_UPS.md). Templates carry "DRAFT — pending platform verification" until WhatsApp/email platform rules are verified (constitution §11).
