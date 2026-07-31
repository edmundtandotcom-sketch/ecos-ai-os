# CONDITIONAL_COMMITMENTS — routing
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: CLOSING_FRAMEWORKS.md (Conditional close); Risk Assurance v2.0 §6 (Prepare); OUTCOME_CODES.md

## Purpose
Routes the "subject-to" commitment path — a genuine PREPARE outcome where the client commits conditional on a real dependency resolving. `[T5]`

## Valid conditions (each maps to an outcome code)
| Condition | Outcome code |
|---|---|
| Subject to financing / bank check / IPA | subject-to-financing |
| Subject to spouse / decision-maker alignment | subject-to-spouse |
| Subject to sale of current property | subject-to-sale |

## Rule
The condition must be **real** — inventing a condition to soft-pressure is banned (CLOSING_FRAMEWORKS §3). Every conditional commitment carries: the named condition · a date · a fallback if it fails. Resolves to PREPARE; routes to the matching gap in branch 13. `[T5]`

READS FROM: CLOSING_FRAMEWORKS. FEEDS INTO: branch 13 (FINANCIAL_GAP / SPOUSE_GAP / TIMING_GAP), branch 15 CRM.
