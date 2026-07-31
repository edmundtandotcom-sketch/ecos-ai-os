# 14_NO_SHOW_LOST_AND_REVIVAL — INDEX
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: OUTCOME_CODES.md (branch 12); Risk Assurance v2.0 §10; CRM SOP 01/03/04

## Purpose
Handles the three end-states that are not a clean win or a clean advisory no-fit: no-shows, lost leads (with controlled reasons), and revival at future triggers. Lost-reason codes align to the branch 12 outcome vocabulary so analysis reconciles across the OS.

## Files
| File | One-liner |
|---|---|
| `LOST_REASON_REGISTRY.csv` | 15 controlled lost-reason codes + outcome mapping + revival eligibility |
| `LOST_REASON_REGISTRY_SPEC.md` | Column definitions + the 15 codes |

## Subfolders (routing files)
| Folder | One-liner |
|---|---|
| `NO_SHOW\` | Reschedule play; recover before writing off |
| `LOST\` | Classify with a controlled reason; feed learning; not over-serve no-fits |
| `REVIVAL\` | Re-engage at a relevant future trigger, never generic re-blasting |

## Rules
`recommended-not-to-transact` / `not-suitable` are advisory outcomes, never counted as losses. No PII in OS lost records.

READS FROM: branch 12 (outcome codes), branch 13 (unclosed gap / no-response ladder), Risk Assurance §10.
FEEDS INTO: branch 07 (re-entry), branch 15 (CRM), branch 21 (loss-pattern learning).
