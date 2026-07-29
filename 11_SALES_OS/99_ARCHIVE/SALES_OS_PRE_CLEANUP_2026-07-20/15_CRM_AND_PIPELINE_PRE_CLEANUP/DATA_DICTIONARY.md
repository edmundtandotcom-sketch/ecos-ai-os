# DATA_DICTIONARY

Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`GHL_LIVE_AUDIT_2026-07-11.md`) · `CRM_FIELDS.md` (this branch) · `PIPELINE_ARCHITECTURE.md` (this branch) · outcome/lost-reason controlled vocab: `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` (WS-B, referenced by path only, not duplicated here) · `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §14

Proposal only. Fields marked NEW do not exist live. Fields marked EXISTING are live today. No live GHL schema change is executed by this file.

---

## 1. New Fields (from the `CRM_FIELDS.md` gap table)

| Field | Object | Type | Allowed values | Who sets | When | Validation rule |
|---|---|---|---|---|---|---|
| `lead_grade` | Contact | Single-select | A / B / C / D-Exclude (per SOP `01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` §5 — reused, not reinvented) | Advisor or automated scoring rule (TBD) | On qualification (Lead Intake stage) | Required before an opportunity may exit New Lead |
| `consultation_outcome` | Opportunity | Single-select | Points to `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` — the 4 sanctioned closes (Proceed / Prepare / Nurture / No Fit) at minimum; full outcome-classification list (9 values) is mandate §8 Stage 15: ready to proceed; subject to financing/spouse/sale; decision pending; long-term nurture; not qualified; not suitable; lost to competitor; chose no action; recommended not to transact | Advisor | Immediately after the Strategy Session, same day | Required stage-exit condition to leave Strategy Session (`PIPELINE_ARCHITECTURE.md` §5.2) |
| `lost_reason` | Opportunity | Native `lostReasonId` (already exists in GHL schema — this is a populate-the-existing-field task, not a new-field task) | Points to `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` LOST_REASON list (~15 controlled values, WS-B) | Advisor | At the moment the opportunity moves to Lost | Required to complete the move to Lost (currently null on 220/220 sampled) |
| `unqualified_reason` | Opportunity | Single-select | Points to `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` — subtype TBD per Decision 2 in `PIPELINE_ARCHITECTURE.md` §6 | Advisor | At the moment the opportunity moves to Unqualified | Required to complete the move to Unqualified — open pending Decision 2 |
| `next_follow_up_date` | Opportunity | Date | Any future date | Advisor / owner | Set whenever a touch is logged and the opportunity does not change stage | Required whenever an opportunity remains in an open, non-terminal stage after a touch — feeds the stale-lead automation (`AUTOMATIONS\PROPOSED.md`) |
| `objection_type` | Opportunity | Single-select (new; structured) | Points to `11_OBJECTION_INTELLIGENCE` RB-01–18 objection categories (WS-B) | Advisor | Logged during/after Discovery, Diagnosis, or Objection Diagnosis stages | Optional at first touch; recommended before Strategy Session |
| `spouse_co_decision_maker` | Contact | Tri-state select | Yes / No / Unknown | Advisor, from Discovery questions | On qualification or first Discovery conversation | None (informational; consolidates two existing radios per `CRM_FIELDS.md` §3) |
| `mop_status` | Opportunity | Select + optional date | MOP Met / MOP Pending (+ date) / Not Applicable | Advisor | During Diagnosis / Financial & Property Analysis | Required only for HDB-context deals; conditional field |

## 2. Consolidated Fields (replacing named duplicates from `CRM_FIELDS.md` §3)

| Field | Object | Type | Allowed values | Who sets | When | Validation rule |
|---|---|---|---|---|---|---|
| `property_situation` | Contact | Single-select | Controlled list — retains existing option set from the older-batch `property situation` field pending a full picklist review (out of scope here) | Lead (self-report, form/webinar) or advisor (confirm/correct) | Lead intake, confirmed at Discovery | None new — replaces the ~6 overlapping fields once live consolidation is executed (separate approval, not this file) |
| `timeline` | Contact | Single-select | Controlled list — retains existing option set from the newer-batch `timeline`/`decision_timing` fields pending review | Lead or advisor | Lead intake, confirmed at Discovery | Same as above |
| `biggest_worry` | Contact | Free text | n/a (free text; `objection_type` above is the structured companion) | Lead or advisor | Lead intake or Discovery | None |

## 3. Existing Strong Fields (reference only — already live, no change proposed)

| Field | Object | Type | Notes |
|---|---|---|---|
| `source` | Opportunity | Native, system-populated | ~100% populated per audit. |
| UTM attribution array (source/campaign/ad/adset/click ID) | Opportunity | Native, system-populated | Auto-captured from Meta/Google. 8 fields total. |
| "What decision are you considering" | Contact | Picklist | Hold / Sell / Exit / Decouple / Free a name / Buy another / New launch / Help child buy / Compare / Not sure — audit flags this as "a good canonical candidate," kept as-is. |

## READS FROM
`CRM_FIELDS.md` · `PIPELINE_ARCHITECTURE.md` · `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` (pointer, not duplicated — build owned by WS-B) · `11_OBJECTION_INTELLIGENCE\` (pointer, WS-B)

## FEEDS INTO
`REPORTING\METRICS.md` · `AUTOMATIONS\PROPOSED.md` · `CRM_QA.md`
