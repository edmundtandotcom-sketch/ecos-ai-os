# CONTRADICTION REGISTER — SALES OS
Version: v0.2
Status: DRAFT
Date: 2026-07-12
Supersedes: v0.1 (2026-07-11) — SC-03 resolved (Decision 072), SC-07 closed (RAM approved 2026-07-12), SC-08 resolved (Decision 073), SC-09 deferred by Edmund
Sources: SALES_OS_BUILD_SPEC_v1 KNOWN CONTRADICTIONS TO REGISTER; `10_MARKETING_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` (C04/C05/C14 carried where sales-relevant)

---

Purpose: contradictions found in the source material that this OS **registers, not resolves.** Pick neither side silently. Any Sales OS file touching one of these must flag it. Resolution authority: Edmund.

Legend — Status: OPEN (owner call pending) · MANAGED (build rule in place, decision still ideal) · SUPERSEDED (direction set; stop propagating the old form).

---

## SC-01 — Four conflicting pipeline definitions · RULED (Decision 071)
- **Current state (UPDATED after live GHL audit, 2026-07-11):** The live GHL "1-To-1 Pipeline" has **10 stages** (New Lead / Responded / Booked Call / Appointment / Strategy Session / Close / Nurture / Unqualified / Won / Lost). Only stages 0–5 have ever held opportunities; Nurture/Unqualified/Won/Lost have held zero in 9 months. Docs disagree with it and each other: SOP 7-stage (`08_OPERATIONS\01_CRM_AND_TRACKING\01_...v2.0.md`) uses 4 stage names that don't exist live; the sync script (`REI_AppsScript_ACTIVE_v8.43.gs`) maps only 5 stage GUIDs, missing Booked Call (~30% of volume) with a wrong Lost reference; plus a stale Agent-Edition funnel.
- **Conflicting state:** No single document matched live truth until `15_CRM_AND_PIPELINE\PIPELINE_ARCHITECTURE.md` (this build) reconciled them.
- **Evidence:** Tier 2 (live read-only GHL audit, 2026-07-11 — exact per-stage counts).
- **Impact:** CRM reporting, lead-status language, and handoff rules cannot be written with confidence until one architecture is named canonical. Worse: `status` never leaves "open" and no outcome is ever recorded, so conversion/revenue are unmeasurable.
- **Recommendation:** Adopt `15_CRM_AND_PIPELINE\PIPELINE_ARCHITECTURE.md`: keep the live 10 stages, remap the documents onto live names, add stage-exit rules that force outcome capture. Do not rename the live pipeline.
- **Required decision:** RULED 2026-07-11 (Decision 071(1)): remap docs to live names + stage-exit rules force outcome capture; Apps Script fix ships with the exit automation.
- **Status:** RULED — execution pending (doc remap + automation spec)

## SC-02 — Historical closing tactics vs no-pressure doctrine · OPEN
- **Current state:** Current advisory doctrine (`03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\02_STRATEGY_SESSION_CONVERSATION_SYSTEM_v2.0.md`) sanctions exactly 4 closes (Proceed / Prepare / Nurture / No Fit), no artificial urgency or scarcity.
- **Conflicting state:** The 490-transcript blueprint and `00_COACH_EDMUND_BUSINESS_BRAIN_V1.0\07_CONSULT_SALES_LOGIC.md` Stage 4 carry historical scarcity / takeaway-close tactics.
- **Evidence:** Tier 5 (legacy practice, not current-doctrine-verified).
- **Impact:** Any build that reuses Stage-4 material wholesale would reintroduce retired pressure tactics into a doctrine that has explicitly moved away from them.
- **Recommendation:** Doctrine wins pending ruling. `07_CONSULTATION_FRAMEWORKS\` and `12_CLOSING_AND_DECISION\` exclude Stage-4 tactics by name.
- **Required decision:** None forced — doctrine already governs. Edmund may formally retire Stage 4 in `04_DECISION_MEMORY.md` to close the loop.
- **Status:** MANAGED

## SC-03 — "Qualified" means two different things · RESOLVED (Decision 072)
- **Current state:** CRM pipeline stage language uses "Qualified" as a stage name.
- **Conflicting state:** Lead grading uses an independent A–D grade also read as "qualified/unqualified." `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md` already flags this split.
- **Evidence:** N/A — definitional collision, not a data conflict.
- **Impact:** "Qualified lead" in a report could mean stage-qualified or grade-qualified — these are not the same population and blending them mis-states conversion rates.
- **Recommendation:** Reconcile as two distinct fields (pipeline stage vs lead grade) rather than one term, when `15_CRM_AND_PIPELINE\CRM_FIELDS.md` is built.
- **Required decision:** RULED 2026-07-12 (Decision 072(2)): two-field model APPROVED — pipeline stage and A–D lead grade are separate GHL fields. Speech-vs-CRM term usage: implement in `15_CRM_AND_PIPELINE\CRM_FIELDS.md` when built ("qualified" in speech = grade A/B; stage names used verbatim in the CRM).
- **Status:** RESOLVED — implementation lands with the `03_LEAD_INTAKE_AND_QUALIFICATION` / CRM_FIELDS build-out

## SC-04 — Historical performance source (Codex) deleted · CLOSED (Decision 071)
- **Current state:** The Codex historical-performance source was deleted 2026-07-11.
- **Conflicting state:** Only an aggregate extract survives, inside `10_MARKETING_OS\`. Drive-trash recovery window closes ~2026-08-10.
- **Evidence:** Tier 2 aggregate only (the raw source is gone).
- **Impact:** Any Sales OS analytics or historical baseline that would have cited raw Codex data cannot — only the marketing-side aggregate is available, and only until the recovery window closes.
- **Recommendation:** If any raw-level historical sales data is needed, recover from Drive trash before 2026-08-10 — after that it is permanently gone.
- **Required decision:** RULED 2026-07-11 (Decision 071(4)): let the window expire; the Marketing OS aggregate extract is the accepted historical baseline.
- **Status:** CLOSED — carried from `10_MARKETING_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`; no restore

## SC-05 — MASTER_CONSULT_INDEX Outcome column is AI-inferred · MANAGED
- **Current state:** `E:\Zoom Consults - Processed\_CONSULT_INTELLIGENCE_OS\02_MASTER_INDEX\MASTER_CONSULT_INDEX.md` carries a 166-row "Outcome" column.
- **Conflicting state:** That column was AI-inferred from transcript content, not verified against the CRM.
- **Evidence:** Tier 4 (observed, not commercially verified) — usable for stratified sampling, not for Tier-1/2 evidence claims.
- **Impact:** Any Sales OS content that cites "X% of consults ended in Proceed" from this index alone would overstate its evidence tier.
- **Build rule:** `21_CONVERSATION_INTELLIGENCE\` PILOT_SAMPLE and any downstream analysis must carry this caveat inline wherever the Outcome column is used.
- **Required decision:** None forced — CRM-verification of outcomes would resolve this if Edmund wants to fund it.
- **Status:** MANAGED

## SC-06 — Founder NAV figures conflict · RESOLVED (Decision 057)
- **Current state:** Figures cited range from $1M→$5M to $6.6M→$9M across different founder-proof documents.
- **Conflicting state:** No single verified figure exists; `10_MARKETING_OS` C10 registers the same conflict on the marketing side.
- **Evidence:** Tier 1 claimed, **none verified.**
- **Impact:** Any case-study or value-communication content in `19_REVIEWS_TESTIMONIALS_AND_CASE_STUDIES\` that cites founder NAV risks publishing an unverifiable public figure.
- **Recommendation:** All founder NAV figures carry `[VERIFY]` and are barred from Sales OS publication until Edmund clears them against portfolio records.
- **Required decision:** RESOLVED — Decision 057 (2026-07-11, parallel session) locked founder NAV proof at **$6.6M → $9M**. Sales OS content uses that figure only.
- **Status:** RESOLVED — mirrors Marketing OS C10

## SC-07 — RAM module version drift · RULED (Decision 071)
- **Current state:** Current masters use Ascent Stages A0–A2 (the former A3/A4 were retired by Decision 063, 2026-07-11), belief blocks RB-01–RB-18, and the R1–R4 Readiness Model / Tier 1-2-3.
- **Conflicting state:** `X-Singapore Real Estate Insider - MAS HQ\01_MAS_OS\02_CONVERSATION_CONVERSION_SYSTEM\MAS_RAM_RISK_ASSESSMENT_MODULE_v1.0.md` — the only structured financial-objection toolkit — still cites old Ascent numbering ("Level 2 = First Climb"), only RB-03/05/08, and a retired "Stage 2 Activated / Tier 2 Warming" taxonomy.
- **Evidence:** Tier 5 (doctrine drift, confirmed by direct read during WS-B build).
- **Impact:** Promoting RAM as-is would reintroduce retired taxonomy into live doctrine; not promoting it leaves the FINANCIAL objection cluster (~30%+ of objections) without a governed master.
- **Recommendation:** Approve the RAM promotion (`11_OBJECTION_INTELLIGENCE\FINANCIAL\_INDEX.md`) WITH a mandatory cross-reference remap to A0–A2 (per Decision 063) / RB-01–18 / R1–R4 before CANDIDATE status.
- **Required decision:** RULED 2026-07-11 (Decision 071(2)): promotion approved with mandatory remap to A0–A2 (Decision 063), RB-01–18, R1–R4, and Move vocabulary (Decision 055). Lands as CANDIDATE pending Edmund content review.
- **Status:** CLOSED — remap complete; RAM v2.0 content APPROVED by Edmund 2026-07-12 (APPROVED MASTER)

## SC-08 — Two label sets for the same four closes · RESOLVED (Decision 073)
- **Current state:** Strategy Session §8 names the 4 sanctioned closes **Proceed / Prepare / Nurture / No Fit**.
- **Conflicting state:** Risk Assurance & Next Action §6 names the same four states **Go / Prepare / Not-Yet / No-Fit**.
- **Evidence:** N/A — naming collision between two APPROVED MASTERS.
- **Impact:** Advisors and CRM outcome codes could log the same result under two names, corrupting outcome reporting.
- **Build rule:** `07_CONSULTATION_FRAMEWORKS\MASTER_CONSULTATION_FLOW.md` §2 and `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` reconcile them 1:1; Sales OS files use Proceed/Prepare/Nurture/No Fit.
- **Required decision:** RULED 2026-07-12 (Decision 073): canonical set = **Proceed / Prepare / Nurture / No Fit**. Risk Assurance & Next Action master conformed same day (→ v2.1, §6 relabelled, v2.0 archived); Sales OS pointers swept (MASTER_CONSULTATION_FLOW, CLOSING/_INDEX, CLOSING_FRAMEWORKS, DECISION_SUPPORT/_INDEX).
- **Status:** RESOLVED — one label set everywhere; CRM outcome codes build on Proceed/Prepare/Nurture/No Fit

## SC-09 — Three businesses co-mingled in one GHL location · DEFERRED (Edmund, 2026-07-12)
- **Current state:** The advisory sales funnel runs in GHL location `cyeYxFVQE1l73kO6S6Lx`.
- **Conflicting state:** The same location carries ~202 Changi Green co-living tenancy fields (of 247 total contact custom fields), a tenant pipeline, plus orphaned fields from unrelated funnels (physio survey, CNY RSVP, coaching revenue) — against One Contact One Opportunity One Truth hygiene.
- **Evidence:** Tier 2 (live field-schema audit, 2026-07-11).
- **Impact:** Field sprawl makes advisory reporting/segmentation noisy, raises mis-automation risk (wrong-audience sends), and complicates every future CRM change.
- **Recommendation:** Governance decision, not urgent surgery: naming/folder convention now; evaluate sub-account separation later. Detail: `15_CRM_AND_PIPELINE\CRM_FIELDS.md` §4.
- **Required decision:** Edmund rules on separation approach (convention now vs sub-account project). **DEFERRED 2026-07-12 (Decision 072.4 — "skip Changi Green"): neither option proceeds until Edmund reopens the item.**
- **Status:** DEFERRED — no action; risk noted (field sprawl + mis-automation) remains live until reopened

## SC-10 — Evidence-tier definitions diverge inside this build · MANAGED (QA finding)
- **Current state:** The mandate (§6, archived in `99_ARCHIVE\`) defines T4 = client experience, T5 = credible external, T6 = observed practice.
- **Conflicting state:** WS-B-built files (07/08/11/12/13/14 branches) inline-define T4 = field-observed single-source, T5 = approved-doctrine, T6 = reasoned inference.
- **Impact:** Tier labels T4–T6 are not comparable across branches until harmonised. T1–T3 and T7 agree everywhere.
- **Build rule:** Mandate definitions are canonical. Harmonise WS-B branch labels at v0.2 (single relabel pass); until then read T4–T6 labels in branches 07–14 per their inline legend.
- **Required decision:** None — orchestrator QA rule stands.
- **Status:** MANAGED

---

## Carried From Marketing OS (sales-relevant only)

- **C04 (HDB/EC audience in or out):** Affects `03_LEAD_INTAKE_AND_QUALIFICATION\` grading criteria if/when built — TRAPS bank keeps qualified HDB/EC in-audience; Consumer Psychology Library retires HDB pathways. See `10_MARKETING_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` C04.
- **C05 (`MAS_MARKETING_INTELLIGENCE_OS_v1.md` stale):** Relevant if `02_MARKETING_TO_SALES_HANDOFF\` ever points to that file — treat as STALE per Marketing OS build rule.
- **C14 (root-level OS placement):** This Sales OS extends the same governance conflict — see `CLAUDE.md` §0 and `DECISIONS_REQUIRED.md` below.

---

READS FROM: SALES_OS_BUILD_SPEC_v1; `10_MARKETING_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`.
FEEDS INTO: `DECISIONS_REQUIRED.md` (rows needing owner calls); every Sales OS file that touches a conflict; `SALES_OS_STATUS.md`.
