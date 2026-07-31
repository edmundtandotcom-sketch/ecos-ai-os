# OUTCOME_CODES
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: Strategy Session v2.0 §8 (4 sanctioned closes); Risk Assurance v2.0 §6; CRM Pipeline & Lead Quality System v2.0 (branch 15 reconciliation); CLOSING_FRAMEWORKS.md

## Purpose
The **controlled vocabulary** for consultation outcomes. Every completed consult is stamped with exactly one outcome code. The 4 sanctioned closes are the parent categories; the 11 codes are the CRM-recordable children. No free-text outcomes. `[T5]`

## The 11 Outcome Codes (grouped under the 4 sanctioned closes)
| Code | Parent close | Definition | CRM mapping note (SC-01 open) |
|---|---|---|---|
| `ready-to-proceed` | PROCEED | Decision made; moving to implementation | GHL stage → Won/Closed or Decision Pending→implementation; SOP stage 5→6 |
| `subject-to-financing` | PREPARE | Committed pending bank/IPA/financing | Decision Pending + tag `cond:financing` |
| `subject-to-spouse` | PREPARE | Committed pending decision-maker alignment | Decision Pending + tag `cond:spouse` |
| `subject-to-sale` | PREPARE | Committed pending sale of current property | Decision Pending + tag `cond:sale` |
| `decision-pending` | PREPARE | Genuinely deciding; no single named condition | Decision Pending |
| `long-term-nurture` | NURTURE | Direction valid, timing/belief not ready; dated review set | Nurture + next Ascent trigger |
| `not-qualified` | NO FIT | No advisory fit / poor values fit | Nurture(low-touch) or Exclude; lead grade C/D |
| `not-suitable` | NO FIT | No feasible/safe path for this client | Exclude / closed-no-fit |
| `lost-to-competitor` | NO FIT | Went with another advisor/agent | Lost → branch 14 LOST_REASON |
| `chose-no-action` | NO FIT | Client decided to do nothing | Lost or Nurture per re-engage potential → branch 14/13 |
| `recommended-not-to-transact` | NO FIT | Advisor advised against transacting now | Closed-advised-against; may re-open on trigger |

## Rules
1. **One code per consult.** If a consult produces two candidate codes, pick the *governing* outcome (the one that determines next action). `[T5]`
2. **PREPARE vs NURTURE:** PREPARE = path valid + a near-term dated condition; NURTURE = direction valid but no near-term trigger. `[T5]`
3. **NO FIT is not lost-by-default:** `recommended-not-to-transact` and `not-suitable` are advisory wins that protect trust; only `lost-to-competitor` / `chose-no-action` route to branch 14 lost-reason logging. `[T5]`
4. **CRM mapping is provisional** pending SC-01 pipeline reconciliation (branch 15 owns it). Codes are stable; their GHL-stage mapping may change. `[T5]`

## Cross-refs
- Lost-reason codes (~15): `14_NO_SHOW_LOST_AND_REVIVAL\LOST_REASON_REGISTRY.csv` — aligned to `lost-to-competitor` / `chose-no-action` / NO-FIT states here.
- Follow-up routing by outcome: branch 13.
