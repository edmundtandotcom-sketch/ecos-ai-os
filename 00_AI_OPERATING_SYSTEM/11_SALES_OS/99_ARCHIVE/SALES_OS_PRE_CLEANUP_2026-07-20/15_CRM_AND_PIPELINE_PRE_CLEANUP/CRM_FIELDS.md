# CRM_FIELDS

Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`GHL_LIVE_AUDIT_2026-07-11.md`, orchestrator scratchpad) — §B, §F; `00_AI_OPERATING_SYSTEM\08_OPERATIONS\06_CONTACT_MASTER\GHL_REIMPORT_PLAN_v1.1_2026-07-11.md` (T1, approved runbook); `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §14; `PIPELINE_ARCHITECTURE.md` (this branch)

Proposal only. No live GHL field is created, renamed, or deleted by this file.

---

## 1. Gap Table (T2, live audit)

### Missing entirely
| Concept | Current state | Proposed home |
|---|---|---|
| Lead grade / score | Native `contact.score` exists but is empty on every contact audited | CONTACT (new custom field, see `DATA_DICTIONARY.md`) |
| Consultation outcome | No field | OPPORTUNITY (new) |
| Structured lost reason | Native `lostReasonId` exists on the opportunity object but is `null` on 220/220 sampled — not a missing field, a missing *practice* | OPPORTUNITY (populate existing native field) |
| DATE-typed next-follow-up | No field | OPPORTUNITY (new) |
| Objection-type picklist | Both existing concern fields are free text, no controlled vocab | OPPORTUNITY (new; allowed values point to `11_OBJECTION_INTELLIGENCE`) |
| Spouse / co-decision-maker flag | Only a generic "are you the decision maker" radio + a CNY-campaign-specific spouse-attendance radio | CONTACT (consolidate the two into one canonical field) |
| HDB MOP (Minimum Occupation Period) status | No field | OPPORTUNITY (new — it's a fact about the specific unit/deal being discussed) |

### Duplicated (live audit §F counts)
| Concept | Overlapping fields (count) | Named instances found in the two 2026 field batches |
|---|---:|---|
| Property situation | 6 | `property situation` (older batch, folder `T86Owp6ZF9LZYd8eaiYw`) + `property_type` (newer batch, folder `T7VXyvtYwxUrZ0W0nwA1`) — the other 4 are not individually named in the audit; a full custom-field export is needed to enumerate them before live consolidation (out of scope here). |
| Timeline / urgency | 4 | `timelines` (older batch) + `timeline` + `decision_timing` (newer batch) — audit flags "2× timeline" as a specific duplicate; 4th instance not named. |
| Concern / objection | 2 | "What is your biggest concern?" (older) vs. "Biggest Worry" / `biggest_worry` (newer) — both free text, no picklist. |
| Financial readiness | scattered, not counted as a single duplicate group | `Cash Buffer`, `CPF Used`, `Loan Left`, `Next Budget`, income select, `Buy Price` (all newer/older batches combined) — not duplicates of each other, but scattered across two field-naming conventions with no single "financial readiness" grouping. |
| Decision-maker | 2 | generic decision-maker radio + CNY-campaign-specific spouse-attendance radio (see "Missing entirely" table — this is the same consolidation). |

**Caveat (evidence discipline):** the audit's aggregate counts (6 property-situation fields, 4 timeline fields) exceed what is individually named in its field-level detail (§F). This file works from what is named; full field-by-field consolidation requires a complete custom-field export, which is not part of this build. Flag as an open action for whoever executes the consolidation.

## 2. Object Placement Rule

Per live audit fix #3: **deal-scoped data goes on the OPPORTUNITY object, not the CONTACT.** Today 0 custom fields exist on OPPORTUNITY — all 56 advisory-relevant fields are jammed onto CONTACT, which only works if each person has exactly one journey ever. That's a narrower claim than the SOP's "One contact, one record, one journey, one truth" principle actually requires: the *contact* record stays singular and canonical (never duplicate a person), but a single contact can rightly have **multiple opportunities over time** (a lead from 2023 who didn't convert, re-engaging in 2026, is one contact with two journeys). Opportunity-level fields are what let that be tracked without contaminating the person's canonical profile with stale, deal-specific data from a dead opportunity.

**Rule of thumb:** if the field's answer could differ between two journeys of the same person, it belongs on OPPORTUNITY. If it describes the person regardless of which deal is live, it belongs on CONTACT.

| Field | Object | Why |
|---|---|---|
| Lead grade | CONTACT | Describes the person's general fit; re-graded per new journey if needed, but starts as a person attribute. |
| Consultation outcome | OPPORTUNITY | Answer is specific to one Strategy Session on one deal. |
| Lost reason | OPPORTUNITY | Specific to why *this* deal died, not the person. |
| Next-follow-up date | OPPORTUNITY | Specific to advancing *this* deal. |
| Objection type | OPPORTUNITY | Objections arise in the context of a specific conversation/deal. |
| Spouse/co-decision-maker flag | CONTACT | Household fact, stable across journeys. |
| MOP status | OPPORTUNITY | Tied to the specific unit under discussion in *this* deal. |
| Property situation, timeline, concern (consolidated) | CONTACT | Pre-consult intake facts about the person's current situation; accepted simplification — revisit only if repeat-client volume (same person, multiple journeys years apart) grows enough to need per-journey history. |

## 3. Consolidation Map

| Concept | Canonical field (proposed) | Fields to retire/merge | Evidence |
|---|---|---|---|
| Property situation | `property_situation` (single picklist, CONTACT) | `property situation` (older batch) + `property_type` (newer batch) + up to 4 unnamed duplicates (pending export) | T2 (named instances); T7 (unnamed count, hypothesis pending export) |
| Timeline / urgency | `timeline` (single field, CONTACT) | `timelines` (older) + `decision_timing` (newer) + 1 unnamed duplicate (pending export) | T2 / T7 |
| Concern / objection (free text) | `biggest_worry` (CONTACT, free text — kept as the qualitative capture) | "What is your biggest concern?" (retire, merge history into `biggest_worry`) | T2 |
| Objection type (NEW, structured) | `objection_type` (OPPORTUNITY, picklist) | n/a — new field, does not replace `biggest_worry`; free text and structured type serve different purposes | T2 (gap) |
| Financial readiness | Group under one section, not one field | `Cash Buffer`, `CPF Used`, `Loan Left`, `Next Budget`, income select, `Buy Price` — keep all, just group and name-normalize (all already OPPORTUNITY-appropriate per §2, currently on CONTACT — recommend migrating to OPPORTUNITY at next field-schema pass) | T2 |
| Decision-maker | `spouse_co_decision_maker` (CONTACT, tri-state: Yes/No/Unknown) | generic decision-maker radio + CNY-specific spouse-attendance radio | T2 |

## 4. Changi Green Co-Mingling (governance issue, not a CRM design issue)

The live audit (§F) confirms the GHL location co-mingles ≥3 businesses on one custom-field schema: ~202 "Changi Green" co-living tenancy fields (`cg_` prefix), ~28 advisory sales fields, 8 UTM attribution fields, ~9 orphaned leftovers (physio-clinic survey, CNY RSVP, coaching-funnel revenue, test junk). This is not a field-design problem this branch can fix — it's a governance/workspace-separation decision: does Changi Green stay in the same GHL location as advisory sales (with folder/naming discipline to keep them apart), or does it need its own location? Flag for Edmund; do not resolve here. Any field-cleanup pass on the advisory 28 fields should explicitly exclude and not touch the `cg_` fields.

## 5. Cross-Reference: `GHL_REIMPORT_PLAN_v1.1_2026-07-11.md`

The reimport plan (T1, approved runbook) creates 7 new custom fields during the pending contact-master import: `Master ID`, `Legacy Name`, `Cohort`, `Lead Source Segment`, `Secondary Email`, `Secondary Phone`, `Do Not Contact` (+ `Do Not Contact Reason`).

**Conflict check: none found.** All 7 are contact-identity/traceability/DNC fields — none overlap conceptually or by name with the gap-table concepts above (lead grade, consultation outcome, lost reason, next-follow-up, objection type, spouse flag, MOP status) or the duplicated concepts (property situation, timeline, concern). No field-name collisions.

**One reconciliation note for `REPORTING\METRICS.md`:** the reimport plan's `Lead Source Segment` (WEBINAR / VSL / ADS / REI-METHOD / STACKED / YT / REFERRAL / APPLICATION / CONCIERGE / LEAD-GENERAL / PWR) is a contact-acquisition-cohort attribute, distinct from the live opportunity's native `source` + UTM attribution array (already ~100% populated, opportunity-level, auto-captured from Meta/Google). These answer different questions — cohort/segment vs. exact ad-level attribution — and should be reported side by side, not merged into one "source" metric.

This branch does **not** instruct executing the reimport — that is a separate pending decision per the build spec.

## READS FROM
`GHL_LIVE_AUDIT_2026-07-11.md` §B, §F · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\06_CONTACT_MASTER\GHL_REIMPORT_PLAN_v1.1_2026-07-11.md` · `PIPELINE_ARCHITECTURE.md`

## FEEDS INTO
`DATA_DICTIONARY.md` · `REPORTING\METRICS.md` · `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` (Changi Green co-mingling, new item)
