# CRM_QA

Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`GHL_LIVE_AUDIT_2026-07-11.md`) · `PIPELINE_ARCHITECTURE.md`, `CRM_FIELDS.md`, `DATA_DICTIONARY.md` (this branch) · SOP `01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` §1 ("One contact. One record. One journey. One truth.")

Weekly hygiene checklist. Run against the live GHL "1-To-1 Pipeline." Findings feed the weekly review cadence already defined in `03_REPORTING_FOLLOW_UP_AND_HANDOFF_RULES_v2.0.md` §3 — this file adds the CRM-specific checks to that existing rhythm, it does not replace it.

---

## 1. Stage Accuracy

- [ ] Spot-check a sample of opportunities per stage: does the stage reflect reality (e.g., an opportunity sitting in "Strategy Session" that was actually held weeks ago and should have moved)?
- [ ] Any opportunity in Close/Won/Lost/Unqualified/Nurture with `status` still `open` when it shouldn't be? (Baseline defect at build time: 397/397 were `open`, including all 4 in Close — track this number down to zero.)
- [ ] Any opportunity that skipped a stage in a way that looks like a data-entry shortcut rather than a real jump?

## 2. Outcome Completeness

- [ ] Every opportunity in Won: `monetaryValue > 0` and `status = won`?
- [ ] Every opportunity in Lost: `lostReasonId` populated from the controlled list?
- [ ] Every opportunity in Unqualified: reason field populated (pending Decision 2 in `PIPELINE_ARCHITECTURE.md` §6)?
- [ ] Every opportunity that passed through Strategy Session: `consultation_outcome` populated?

## 3. Field Fill Rates

- [ ] `lead_grade` fill rate (target: rising from 0% baseline).
- [ ] `next_follow_up_date` fill rate on all open, non-Nurture opportunities.
- [ ] `source` / UTM fill rate (baseline: ~100% — flag any regression).
- [ ] Duplicate-field cleanup progress: are new records still populating the retired duplicate fields (`CRM_FIELDS.md` §3) instead of the canonical ones? If yes, the intake form/workflow still needs updating.

## 4. One Contact, One Opportunity, One Truth

- [ ] Any contact with more than one *open* opportunity in the same pipeline at the same time (possible duplicate lead, not a legitimate second journey)?
- [ ] Any duplicate contacts (same phone/email, two contact records) — cross-check against the identifier rule in `GHL_REIMPORT_PLAN_v1.1_2026-07-11.md` ("Find existing contacts by Email OR Phone").
- [ ] Any opportunity with no linked contact, or a contact with no linked opportunity that should have one?

## 5. Staleness Review

- [ ] % of open opportunities untouched 30+ days (baseline: 36% of 220 sampled, concentrated in New Lead + Booked Call). Track the trend, not just the snapshot.
- [ ] Of the stale set, how many have a `next_follow_up_date` already scheduled (acceptable — a plan exists) vs. none at all (the real leak)?
- [ ] Any opportunity stale 60+ days with no owner action logged — escalate.

## READS FROM
`GHL_LIVE_AUDIT_2026-07-11.md` · `PIPELINE_ARCHITECTURE.md` · `CRM_FIELDS.md` · `DATA_DICTIONARY.md` · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\03_REPORTING_FOLLOW_UP_AND_HANDOFF_RULES_v2.0.md`

## FEEDS INTO
Weekly review cadence (`03_REPORTING_FOLLOW_UP_AND_HANDOFF_RULES_v2.0.md` §3) · `REPORTING\METRICS.md` (fill-rate/staleness trend inputs) · `00_COMMAND_CENTER\SALES_OS_STATUS.md`
