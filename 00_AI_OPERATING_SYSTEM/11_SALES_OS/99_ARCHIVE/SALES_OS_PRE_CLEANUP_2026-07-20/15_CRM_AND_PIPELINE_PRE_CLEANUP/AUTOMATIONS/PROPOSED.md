# PROPOSED (Automations)

Version: v0.1
Status: DRAFT — stub-level, all PROPOSED, none built
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`..\..\GHL_LIVE_AUDIT_2026-07-11.md`) · `..\PIPELINE_ARCHITECTURE.md` §5.2, §5.3 (this branch) · `00_AI_OPERATING_SYSTEM\CLAUDE.md` §11 (Platform Verification Rule)

Every item below is **PROPOSED**, not built, not tested, not scheduled. Building/testing lives with `01_E.C.O.S\07_OPERATIONS_DESK.md` once Edmund approves. All GHL-specific mechanics (workflow triggers, stage-move blocking, required-field enforcement) are **DRAFT — pending platform verification** per constitution §11 — do not assume GHL supports blocking a stage move client-side without confirming current platform behavior.

---

## 1. Stage-Exit Enforcement

**Problem:** 397/397 opportunities are `status: open`; Won and Lost have never held a single record in 9 months. Stages don't currently require anything to exit.

**Proposed rule — Won:** Trigger = opportunity stage changes to Won (`626cf974-a751-4dd4-a854-fd05fde9dda0`). Condition = `monetaryValue > 0` AND native `status` set to `won`. If condition fails: block the move (preferred) or, if GHL cannot block a stage move server-side, fire an immediate notification to the opportunity owner flagging the incomplete Won and auto-revert after a grace window (mechanics TBD, pending platform verification).

**Proposed rule — Lost:** Trigger = opportunity stage changes to Lost (`0829d917-331f-4ee2-a240-ee99d97a6a28`). Condition = `lostReasonId` populated from the controlled list at `12_CLOSING_AND_DECISION\OUTCOME_CODES.md`. Same block-or-notify mechanics as Won.

**Proposed rule — Unqualified:** Same pattern, pending Decision 2 in `PIPELINE_ARCHITECTURE.md` §6 (which reason list governs).

**Owner:** Operations Desk, pending Edmund approval of `PIPELINE_ARCHITECTURE.md` Decision 3 (ship this together with the Apps Script GUID-map patch, not before).

## 2. Stale-Lead Nudge

**Problem:** 36% of the 220-record sample is untouched 30+ days, concentrated in New Lead + Booked Call (282 of 397 opportunities, 71% of the live pipeline).

**Proposed rule:** Trigger = opportunity remains in New Lead or Booked Call with no field update for N days (threshold TBD — recommend 7-day internal nudge, 30-day escalation, matching the audit's own staleness cutoff). Action = notify the opportunity owner; optionally trigger a client-facing nurture touch (WhatsApp/email template, owned by `13_FOLLOW_UP_AND_NURTURE`, WS-B build — pointer only, not duplicated here).

**Owner:** Operations Desk. Depends on: `next_follow_up_date` field existing (`DATA_DICTIONARY.md` §1) so the nudge can distinguish "stale, no plan" from "stale, but a future follow-up is already scheduled."

## 3. Speed-to-Lead Timer

**Problem:** No field or automation currently tracks time-to-first-contact. Industry pattern (not specific to this business, general sales-ops knowledge, T5 hypothesis) is that response speed is one of the strongest predictors of lead conversion — this pipeline has no visibility into it at all today.

**Proposed rule:** Trigger = New Lead opportunity created. Action = start a timer; alert the owner if the lead has no contact-status change within X minutes/hours (threshold not set — recommend Edmund/Cindior set based on team capacity, not assumed). Ties to the SOP's "Contacted" concept (`PIPELINE_ARCHITECTURE.md` §5.1), which is a sub-status, not a live pipeline stage.

**Owner:** Operations Desk.

## READS FROM
`GHL_LIVE_AUDIT_2026-07-11.md` · `..\PIPELINE_ARCHITECTURE.md` §5.2–5.3 · `00_AI_OPERATING_SYSTEM\CLAUDE.md` §11

## FEEDS INTO
`01_E.C.O.S\07_OPERATIONS_DESK.md` (build owner once approved) · `13_FOLLOW_UP_AND_NURTURE` (nurture message content) · `CRM_QA.md` (this branch — weekly check that these, once built, are firing)
