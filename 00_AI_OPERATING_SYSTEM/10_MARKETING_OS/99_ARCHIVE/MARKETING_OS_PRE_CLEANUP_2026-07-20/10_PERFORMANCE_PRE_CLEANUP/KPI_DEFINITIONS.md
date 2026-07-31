# KPI_DEFINITIONS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs` (live pipeline-stage logic) + `08_OPERATIONS/01_CRM_AND_TRACKING/01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` (approved pipeline stage list) — this file restates both for marketing usage, does not override either
Evidence level: N/A (definitions, not performance claims)
Supersedes: none
Sources: as above; `08_OPERATIONS/01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md`
Next review: if the live Apps Script pipeline stage map changes

---

## Funnel stages (matching the live Apps Script / GHL "1-To-1 Pipeline")
Confirmed directly from `REI_AppsScript_ACTIVE_v8.43.gs` (`STAGE_STATUS` map, v8.14 comment: "1-To-1 Pipeline actual stages: New Lead, Responded, Appointment, Strategy Session, Close, Nurture, Unqualified, Won, Lost"). The live script's dashboard status values, in funnel order:

| Stage | Definition |
|---|---|
| New | Lead just entered the pipeline (GHL stages: "New Lead," "New," "Signup"). |
| Contacted | An outbound attempt was made ("Attempting Contact," "Contacted," "Nurture" is also mapped here). |
| Responded | The lead replied. |
| Booked Call | A call/appointment was booked (several GHL stage-name variants map here: "Booked Call," "Booking," "Booked," "Booked Appointment," "Diagnosis Call Booked"). |
| Appointment | Appointment stage reached (distinct from Booked Call in the script's stage-rank logic). |
| Strategy Session | Strategy session booked/held. |
| Appt Qualified | "Implementation Opportunity" / "Attended" / "Appt Qualified" — lead attended and was qualified. |
| Closed | "Close," "Closed," "Won." |
| Lost | "Unqualified," "Lost." |

The build brief's shorthand "Lead → Responded → Booked → Show → Session → Closed" maps onto this real stage list as: New/Contacted → Responded → Booked Call → Appointment/Appt Qualified (the "show") → Strategy Session → Closed/Lost.

## Core metric definitions
- **CPL (Cost per Lead):** Ad spend ÷ total leads for the period/campaign. Confirmed field in `10_PERFORMANCE/HISTORICAL_BASELINE.md`.
- **Cost per Responded Lead:** Ad spend ÷ leads that reached "Responded" or later.
- **CPA (Cost per Appointment/Acquisition):** Not currently computed anywhere in the reviewed source data — no appointment-level cost figure exists in the archived Codex snapshot. **TBD DECISION:** which stage counts as the "A" in CPA for this business — Booked Call, Appointment, or Appt Qualified. Recommend Edmund/Cindior confirm; until then, do not report a CPA number.
- **Qualified lead:** GHL "Appt Qualified" stage ("Implementation Opportunity" / "Attended"). **TBD DECISION:** whether this should be the marketing-facing definition of "qualified," or whether the CRM's separate A/B/C/D lead-quality grade (`08_OPERATIONS/01_CRM_AND_TRACKING/01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` §5) should govern instead. These are two different systems (pipeline stage vs. quality grade) and are not currently reconciled in any source file reviewed.

## Dashboard minimum fields (for reference — do not duplicate the live schema here)
Full field list: `08_OPERATIONS/01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md` §3. Includes date, platform, campaign, ad set, ad/creative, campaign pack, format, awareness stage, buyer profile, hook/angle, spend, impressions, clicks, CTR, leads, CPL, replies, booking link clicks, booked appointments, completed consults, lead quality grade, notes/decision.

## READS FROM
`08_OPERATIONS/01_CRM_AND_TRACKING/`, `08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs`

## FEEDS INTO
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`, `13_MARKETING_OPERATIONS/DATA_DICTIONARY.md`, `12_TEMPLATES/PERFORMANCE_REVIEW.md`
