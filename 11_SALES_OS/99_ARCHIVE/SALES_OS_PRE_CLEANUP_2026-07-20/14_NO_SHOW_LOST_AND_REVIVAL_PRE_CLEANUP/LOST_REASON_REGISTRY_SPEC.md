# LOST_REASON_REGISTRY_SPEC
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: LOST_REASON_REGISTRY.csv; OUTCOME_CODES.md (branch 12); CRM SOP 01

## Purpose
Defines the **~15 controlled lost-reason codes** — the only permitted values for classifying why a lead ended. Aligned 1:1 with the branch 12 outcome vocabulary so lost analysis reconciles with consult outcomes. No free-text lost reasons.

## Columns
| Column | Definition | Controlled values |
|---|---|---|
| `lost_reason_code` | Controlled reason | the 15 codes in the CSV |
| `definition` | Plain meaning | free text |
| `maps_to_outcome_code` | Parent outcome (branch 12) | lost-to-competitor / chose-no-action / not-qualified / not-suitable |
| `revival_eligible` | Can this be revived? | yes / limited / no |
| `evidence_tier` | Backing | T1–T7 |
| `notes` | One-liner + belief-block link | free text |

## The 15 codes
price-too-high · lost-to-competitor-advisor · lost-to-other-agent · bought-direct-elsewhere · chose-no-action · spouse-vetoed · financing-fell-through · timing-deferred · went-cold-no-response · not-qualified-disqualified · not-suitable-advised-against · trust-not-established · wanted-transaction-only · life-event-disruption · duplicate-or-invalid

## Rules
1. Exactly one code per lost lead. `[T5]`
2. `not-qualified` / `not-suitable-advised-against` are advisory outcomes, not competitive losses — never counted against conversion. `[T5]`
3. `revival_eligible = yes/limited` routes to REVIVAL with a next Ascent trigger; `no` is a clean exclude. `[T5]`
4. Codes are stable; CRM stage mapping is provisional pending SC-01 (branch 15). `[T5]`
