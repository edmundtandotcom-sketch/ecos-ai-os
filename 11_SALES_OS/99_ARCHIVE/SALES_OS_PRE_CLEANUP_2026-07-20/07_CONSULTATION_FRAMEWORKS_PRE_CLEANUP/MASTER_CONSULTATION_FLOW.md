# MASTER_CONSULTATION_FLOW
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources (pointer-first — this file governs the JOIN, not the content):
- Diagnosis Call: `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\01_DIAGNOSIS_CALL_SYSTEM_v2.0.md`
- Strategy Session: `...\03_CONVERSATION_CONVERSION\02_STRATEGY_SESSION_CONVERSATION_SYSTEM_v2.0.md`
- Decision Psychology & Belief Resolution: `...\03_CONVERSATION_CONVERSION\03_DECISION_PSYCHOLOGY_AND_BELIEF_RESOLUTION_v2.1.md`
- Risk Assurance & Next Action: `...\03_CONVERSATION_CONVERSION\04_RISK_ASSURANCE_AND_NEXT_ACTION_SYSTEM_v2.1.md`
- ProDeck Consult Delivery: `...\05_PRODECK\01_PRODECK_CONSULT_DELIVERY_SYSTEM_v2.0.md`
- Trigger Questions: `...\04_TRIGGER_QUESTIONS\01_ADVISORY_TRIGGER_QUESTION_BANK_v2.0.md`, `02_BELIEF_SHIFT_QUESTION_SEQUENCES_v2.0.md`
- MAS Foundation: `...\01_FOUNDATION\01_MAS_ADVISORY_FOUNDATION_v4.0.md`
- Constitution: `00_AI_OPERATING_SYSTEM\CLAUDE.md` (MAS 7-layer stack)

> Evidence tiers used in this OS: **T1** commercial/transaction outcome · **T2** CRM-verified pipeline/behavioural · **T3** verified conversation evidence (coded transcripts, e.g. 376-objection / 166-consult table) · **T4** field-observed single-source · **T5** approved-doctrine assertion · **T6** reasoned inference/analogy · **T7** hypothesis. Nothing is "proven" without a cited tier.

---

## 0. What This File Is

This is the **single governed end-to-end consultation flow**. It does not restate any master — it defines the **order, the joins, the entry/exit gates, and what each phase must produce** so the six approved conversation masters operate as one system instead of six documents. `[T5]`

The consult spine is **REI (Review → Evaluate → Identify)**. Campaign doors create recognition; REI creates diagnosis; ProDeck presents the roadmap. `[T5, per Strategy Session §6]`

**Framework ≠ script (the adaptation rule).** Every phase below is a *required outcome*, not a required sequence of words. The advisor adapts wording, order, and depth to the client's readiness stage and decision style; what may NOT be skipped is the phase *output* (the "Must Produce" line). A phase with no captured output did not happen. `[T5]`

---

## 1. The Flow At A Glance

```
Lead context (CRM grade + segment + readiness)
      │
      ▼
[P1] DIAGNOSIS CALL  ── 6 phases ──►  Diagnosis Record + Tier (1/2/3/Excluded)
      │  gate: Tier 1 only proceeds; Tier 2→nurture; Tier 3→authority nurture; Excluded→close
      ▼
[P2] ADVISOR PREP  ──►  Pre-Session Gate cleared (numbers, decision-makers, fit)
      │  gate: numbers present + decision-makers bookable, else → data-collection loop
      ▼
[P3] STRATEGY SESSION (REI + ProDeck)  ──►  Next-Move Roadmap
      │
      ▼
[P4] DECISION GATE (Risk Assurance)  ──►  Proceed / Prepare / Nurture / No Fit
      │
      ▼
[P5] SANCTIONED OUTCOME  ──►  one of: PROCEED · PREPARE · NURTURE · NO FIT
      │
      ▼
[P6] FOLLOW-UP HANDOFF  ──►  CRM record updated + gap-based follow-up assigned (branch 13)
```

Objection handling (branch 11) and closing (branch 12) are **not a phase** — they are cross-cutting layers invoked inside P3 and P4 whenever resistance or a decision-point surfaces.

---

## 2. Phase Definitions, Joins, and Required Outputs

### P1 — Diagnosis Call
- **Governed by (point, do not duplicate):** Diagnosis Call System v2.0 — its 6 phases (Control the Frame → Trigger Discovery → Current Position → Desired Future → Ascent Stage & Property Position → Buyer Segment & Decision Style), Belief Block discovery, Decision-Maker rule, and Tiering. `[T5]`
- **Tools plugged in:** Core Opening + Ascent-Stage questions from Trigger Question Bank §2–§3; archetype read from Buyer Segment Library (branch 08).
- **Must Produce (Diagnosis Record):** trigger · current position · desired future · Ascent Stage (A0–A2 — former A3/A4 retired per Decision 063) · buyer segment · dominant belief block (RB-xx) · decision-maker map · missing information · **Tier (1 / 2 / 3 / Excluded)** · next best action. Written to CRM (branch 15) and DISCOVERY_REGISTRY (branch 08).
- **Exit gate:** Only **Tier 1** advances to P2. Tier 2 → active nurture (branch 13). Tier 3 → authority nurture. Excluded → polite close (do not over-serve). `[T5, Diagnosis §6]`

### P2 — Advisor Prep
- **Governed by:** Strategy Session §2 Pre-Session Gate + ProDeck §3 Pre-Session Gates. `[T5]`
- **Purpose:** convert a booked Tier-1 into a session that can actually produce a strategy. No numbers = no strategy.
- **Must Produce:** confirmed Ascent Stage · Property Position · Strategic Intent · Buyer Segment · Decision-Maker Map · Trigger · Belief Block · numbers required for meaningful advice · pre-empt plan for the top 2–3 likely objections for this segment (branch 11). `[T5]`
- **Exit gate:** numbers present **and** decision-makers can attend → P3. Otherwise the "next step" is **data collection or a second diagnosis conversation**, NOT a Strategy Session. `[T5, Strategy §2]`

### P3 — Strategy Session (REI + ProDeck)
- **Governed by:** Strategy Session Conversation System v2.0 (REI spine + 7-step flow) delivered through ProDeck v2.0 (5 anchors + 60-min flow). `[T5]`
- **REI ↔ ProDeck ↔ RAM join (the critical sequence):**
  - **R — Review Real Position** ↔ ProDeck Anchor 1 (Position Clarity). RAM not used here — facts only. `[T5, RAM §Integration]`
  - **E — Evaluate Market Rewards** ↔ ProDeck Anchor 2 (Market Reward Clarity). **RAM begins here** when a financial concern surfaces.
  - **[Anchor 3 — Risk Assurance]** ↔ deploy the relevant RAM lens/technique (branch 12 + Risk Assurance master). Resolve financial fear *before* the roadmap.
  - **I — Identify Next 2–3 Moves** ↔ ProDeck Anchor 4 (Next-Move Roadmap). Presented only AFTER confidence is restored. `[T5]`
  - **Close** ↔ ProDeck Anchor 5 (Decision Confidence & Next Action) → hands to P4.
- **Objection layer:** any resistance triggers the Decision Psychology resolution sequence (branch 11 routes to RB-01…RB-18). Field rule: never advance on a verbal reframe alone — attach a worked number, comparable, or case. `[T3, Decision Psychology Appendix A]`
- **Must Produce (Next-Move Roadmap):** Current Position · Target Position · Main Risk · Main Opportunity · Pathway Options · Recommended Pathway · Avoid List · Next 2–3 Moves · Immediate Next Action · Follow-Up Trigger. `[T5, Strategy §4 Step 7]`

### P4 — Decision Gate (Risk Assurance)
- **Governed by:** Risk Assurance & Next Action System v2.1 (§6 Proceed/Prepare/Nurture/No Fit + §7 Next Action Menu). `[T5]`
- **Purpose:** convert the roadmap into a decision the client can safely own. Close by clarity, never by pressure.
- **Must Produce:** decision (Proceed/Prepare/Nurture/No Fit) · the concrete, **dated** next step · owner · what info/document/decision-maker is still needed. `[T3 — "lock a dated next step" is a top-5 cross-cutting winner; its absence a top-5 loser]`

### P5 — Sanctioned Outcome (exactly one)
The Risk-Assurance gate uses the same canonical labels as the **4 sanctioned closes** (Strategy Session §8 = Risk Assurance §6 — unified by Decision 073, 2026-07-12). No fifth close exists. `[T5]`

| Sanctioned close | Risk-Assurance gate | Meaning | Routes to |
|---|---|---|---|
| **PROCEED** | Proceed | Ready for implementation planning | Branch 12 close → execution / branch 15 |
| **PREPARE** | Prepare | Path valid, missing numbers / docs / decision-maker | Branch 13 (relevant gap) + rebook |
| **NURTURE** | Nurture | Direction valid, timing/belief not ready | Branch 13 gap-based nurture |
| **NO FIT** | No Fit | Not the right strategy now; safer action given | Polite close; branch 14 if lost |

Full outcome vocabulary (11 codes) lives in `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` and refines these four into CRM-recordable states.

### P6 — Follow-Up Handoff
- **Governed by:** Risk Assurance §8 (handoff fields) + CRM SOP 03 follow-up accountability. `[T5]`
- **Must Produce:** CRM record updated with the full handoff field set (latest summary, Ascent Stage, belief block, risk concern, tier, advisory output, next action, next follow-up date, owner, next Ascent trigger) + a **gap-based follow-up** assigned in branch 13 (clarity/trust/financial/spouse/timing/fear/suitability). `[T5]`

---

## 3. Where Each Master Plugs In (single reference table)

| Master (APPROVED, do not duplicate) | Plugs into | Role in the flow |
|---|---|---|
| Diagnosis Call System v2.0 | P1 | Triage, diagnosis, qualification, tiering |
| Trigger Question Bank + Belief-Shift Sequences v2.0 | P1, P3, P4 | Self-realisation questions + objection sequences |
| Buyer Segment / Readiness / Traps (branch 08 pointers) | P1, P2 | Archetype + readiness read |
| Strategy Session Conversation System v2.0 | P3 | REI spine + 7-step conversation |
| ProDeck Consult Delivery v2.0 | P3 | 5 anchors, session control, delivery |
| RAM module (legacy — promotion proposed, branch 11) | P3 Anchor 3 | Financial-fear resolution (5 techniques) |
| Decision Psychology & Belief Resolution v2.1 | P3, P4 (branch 11) | RB-01…RB-18 resolution + field responses |
| Risk Assurance & Next Action v2.1 | P4, P6 | Decision gate + handoff |
| Case Study Bank (7 categories) | P3, P6 (branch 13) | Proof at the point of resistance |

---

## 4. Governance Rules On This Flow

1. **No phase output = phase did not happen.** Registry rows (branch 07/08) and CRM fields (branch 15) are the evidence a phase completed. `[T5]`
2. **No numbers, no strategy.** P2 gate is hard; a Strategy Session run without numbers produces a fake answer (ProDeck §3). `[T5]`
3. **Doctrine beats legacy tactics.** Any Stage-4 historical closing tactic (scarcity, takeaway close) from the 490-transcript blueprint or `00_COACH_EDMUND_BUSINESS_BRAIN_V1.0\07_CONSULT_SALES_LOGIC.md` is **out of scope** here — advisory no-pressure doctrine wins pending Edmund's ruling. Registered as **SC-02**; not silently resolved. `[T5]`
4. **Four closes only.** PROCEED / PREPARE / NURTURE / NO FIT. No artificial urgency or scarcity anywhere in the flow. `[T5]`
5. **Adaptation, not scripting.** See §0 adaptation rule.

---

## 5. Open Contradictions Touching This Flow (register, do not resolve)
- **SC-01** Four pipeline definitions unreconciled → affects where P5 outcomes land in CRM (branch 15 owns the reconciliation).
- **SC-02** Legacy Stage-4 closing tactics vs no-pressure doctrine → doctrine wins pending ruling (Rule §4.3 above).
- **SC-05** MASTER_CONSULT_INDEX "Outcome" column is AI-inferred → usable for sampling, not Tier-1/2 claims.

Full register: `11_SALES_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` (WS-A).
