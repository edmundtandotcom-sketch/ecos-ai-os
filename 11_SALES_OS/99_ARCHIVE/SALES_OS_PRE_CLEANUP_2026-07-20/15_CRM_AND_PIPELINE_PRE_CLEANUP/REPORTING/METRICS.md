# METRICS

Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`..\..\GHL_LIVE_AUDIT_2026-07-11.md` — orchestrator scratchpad, mirrored context) · `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §15 (Sales Performance & Forecasting metric families) · `..\PIPELINE_ARCHITECTURE.md`, `..\CRM_FIELDS.md`, `..\DATA_DICTIONARY.md` (this branch) · `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md`

Every metric below is marked **COMPUTABLE TODAY** (with source) or **BLOCKED** (with the specific gap and which fix unblocks it). Nothing here is a live dashboard — this is the reporting-readiness map.

---

## 1. Lead Family

| Metric | Status | Source / Gap |
|---|---|---|
| Lead count (by period, source, campaign) | **COMPUTABLE TODAY** | Opportunity `source` field (~100% populated) + UTM attribution array; live audit gives exact totals (397 opps, 2025-10-12 → 2026-07-10). |
| Source attribution accuracy | **COMPUTABLE TODAY** | Same — native + UTM capture is the strongest field group in the live schema. |
| Lead quality/grade distribution | **BLOCKED** | Gap: native `contact.score` empty everywhere; no `lead_grade` field exists. Unblocked by: `lead_grade` field (`DATA_DICTIONARY.md` §1). |

## 2. Appointment Family

| Metric | Status | Source / Gap |
|---|---|---|
| Booking rate (New Lead → Booked Call) | **COMPUTABLE TODAY** | Stage snapshot counts from live audit (166 / 56 / 116 / 44 / 11 / 4 by stage). |
| Show rate (Booked Call/Appointment → attended) | **PARTIALLY BLOCKED** | Raw stage-to-stage ratio is computable from snapshot counts, but no-show/cancelled is not a distinct captured status — a stalled Booked Call opportunity is indistinguishable from a genuine no-show. Unblocked by: adding a no-show/cancelled secondary status (mandate §14 lists this as a required secondary status). |

## 3. Consultation Family

| Metric | Status | Source / Gap |
|---|---|---|
| Talk-to-listen ratio | **BLOCKED** | Requires call/recording-level analysis, not a CRM field. Out of this branch's scope — see `21_CONVERSATION_INTELLIGENCE`. |
| Discovery completion | **BLOCKED** | Same — scorecard/consult-record data (mandate §17), not tracked as a CRM field today. |
| Same-day decision rate | **BLOCKED** | Gap: no `consultation_outcome` field and no confirmed stage-transition timestamp access at the field level. Unblocked by: `consultation_outcome` field + stage-exit enforcement (`PIPELINE_ARCHITECTURE.md` §5.2). |
| Consult-to-client conversion | **BLOCKED** | Gap: 0 Won opportunities in the pipeline's entire 9-month history. Unblocked by: Won/Lost stage-exit enforcement (`PIPELINE_ARCHITECTURE.md` §5.3 fix #1). |

## 4. Pipeline Family

| Metric | Status | Source / Gap |
|---|---|---|
| Stage distribution (snapshot) | **COMPUTABLE TODAY** | Live audit §C — exact counts per stage. |
| Staleness / stalled opportunities | **COMPUTABLE TODAY** | Live audit already computed this: 36% of the 220-record sample untouched 30+ days, concentrated in New Lead/Booked Call (282 of 397 opps). |
| Stage conversion rate (cohort/time-based) | **PARTIALLY BLOCKED** | Current snapshot distribution is computable; true cohort conversion (% of a given month's New Leads that reach each later stage) requires confirmed access to stage-entry timestamps per opportunity — not verified available at the field level in this audit. |
| Pipeline value (sum `monetaryValue`) | **BLOCKED** | Gap: 98.6% of opportunities have `monetaryValue = $0` (only 3 non-zero records: $10k, $10k, $100k). Unblocked by: require `monetaryValue` at Close/Won stage entry. |
| Weighted pipeline value | **BLOCKED** | Same gap, plus no stage-based probability weighting scheme exists yet — second gap. |
| Follow-up compliance | **BLOCKED** | Gap: `next_follow_up_date` field does not exist. Unblocked by: `DATA_DICTIONARY.md` §1 field + stale-lead automation. |
| Forecast accuracy | **BLOCKED** | Requires `monetaryValue` + probability + realized-outcome history — none exist yet. |

## 5. Commercial Family

| Metric | Status | Source / Gap |
|---|---|---|
| Revenue per lead / qualified lead / appointment / consult | **BLOCKED** | Gap: 0 Won records, 98.6% `monetaryValue = $0`. Unblocked by: `PIPELINE_ARCHITECTURE.md` §5.3 fix #1. |
| CAC (customer acquisition cost) | **BLOCKED** | Ad spend exists in the dashboard system (`02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md`); revenue side does not. Same gap. |
| ARPC (avg revenue per client) | **BLOCKED** | Same gap. |
| GCI | **BLOCKED** | Same gap. |
| Sales cycle length | **BLOCKED** | Requires Won timestamp vs. lead-created timestamp; 0 Won records to measure from. |
| Repeat client rate | **BLOCKED** | Requires multi-opportunity-per-contact history over time plus a Won baseline; system is only 9 months old and has 0 Won records. |
| Referral rate | **BLOCKED / UNCLEAR** | No referral-source tracking field confirmed distinct from ad-source UTM in this audit — needs confirmation before even scoping the gap. |

## 6. Quality Family

| Metric | Status | Source / Gap |
|---|---|---|
| Fit (lead-to-suitability match) | **BLOCKED** | Gap: no lead grade, no suitability field. |
| Complaints | **BLOCKED / UNKNOWN** | Not a CRM field surfaced in this audit; unclear if tracked anywhere. Flag for confirmation, not assumed absent. |
| Satisfaction / review rate | **BLOCKED** | `19_REVIEWS_TESTIMONIALS_AND_CASE_STUDIES` territory (STUB), not a CRM field today. |
| Completion / cancellation rate | **PARTIALLY BLOCKED** | Same gap as Appointment family — no explicit cancelled/no-show status. |

## 7. Advisor Family

| Metric | Status | Source / Gap |
|---|---|---|
| Contact discipline, quality, conversion, suitability, follow-up, CRM completeness, forecast accuracy, feedback, compliance, coaching progress (all, per advisor) | **ALL BLOCKED** | Gap: every underlying metric above is itself blocked, so per-advisor rollups inherit the same gaps. Additionally, the live audit did not report fill rate on the opportunity `assignedTo`/owner field — confirm this is populated before scoping advisor-level reporting. |

**Mandate rule to carry forward (§15):** never rank advisors by revenue alone — once this family becomes computable, pair any conversion/revenue metric with a quality/compliance metric before it reaches a scorecard.

## 8. Reverse-Engineering Funnel Math (template)

Standard top-down revenue-to-lead math, every input currently UNKNOWN pending outcome tracking:

```
Revenue target                           = UNKNOWN (business input, not a CRM gap)
÷ Avg revenue per client (ARPC)           = UNKNOWN — blocked, §5 (0 Won records)
= Clients needed
÷ Consult-to-client conversion rate       = UNKNOWN — blocked, §3
= Consultations (Strategy Sessions) needed
÷ Show rate (Booked/Appointment → held)   = UNKNOWN — blocked, §2 (no no-show status)
= Appointments/bookings needed
÷ Response rate (New Lead → Responded)    = COMPUTABLE TODAY — 56/397 stage snapshot gives a rough read; true cohort rate needs §4's timestamp caveat
= Contacted leads needed
÷ Lead-to-contact rate                    = COMPUTABLE TODAY — same caveat
= Total leads needed
```

Only the bottom two rows of this chain are usable today. Everything above "Appointments/bookings needed" is a placeholder until Won/Lost tracking exists — do not present this math to Edmund with invented conversion percentages.

## READS FROM
`GHL_LIVE_AUDIT_2026-07-11.md` · `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §15 · `..\PIPELINE_ARCHITECTURE.md` · `..\CRM_FIELDS.md` · `..\DATA_DICTIONARY.md` · `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md`

## FEEDS INTO
`22_SALES_ANALYTICS` (STUB, future deep-build) · `00_COMMAND_CENTER\SALES_OS_STATUS.md`
