# NO_SALE_CLOSE — routing
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: CLOSING_FRAMEWORKS.md (No-sale close); Strategy Session v2.0 §8 (No Fit); Risk Assurance v2.0 §6 (No-Fit), §12

## Purpose
Routes the no-sale close — recommending the client *not* transact. A first-class sanctioned outcome (NO FIT), never a failure. Willingness to say no is a core trust-builder (RB-10). `[T5]`

## Two distinct no-sale states (map to different outcome codes)
| State | Meaning | Outcome code |
|---|---|---|
| **Recommended not to transact** | A move is possible but the advisor judges it unwise now | recommended-not-to-transact |
| **Not suitable** | No feasible/safe path for this client | not-suitable |
| **Not qualified** | No advisory fit / poor values fit | not-qualified |

## Rule
State plainly *why* no move is safest + the safer action. Do not over-serve. If the client later becomes viable, route to NURTURE (branch 13), not pressure. `[T5]`

READS FROM: CLOSING_FRAMEWORKS. FEEDS INTO: OUTCOME_CODES, branch 14 (if lost), branch 13 (if nurture-able).
