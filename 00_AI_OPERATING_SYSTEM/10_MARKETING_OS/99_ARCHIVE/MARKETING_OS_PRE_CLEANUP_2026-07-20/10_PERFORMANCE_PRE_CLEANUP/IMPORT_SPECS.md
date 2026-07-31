# IMPORT_SPECS
Version: v1.0
Status: DRAFT — pending platform verification
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (field-mapping spec); platform export formats themselves are owned by Meta/Google/GHL and change without notice
Evidence level: N/A (process spec, not a performance claim)
Supersedes: none
Sources: `08_OPERATIONS/01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md` §3 (minimum dashboard fields); `08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs` (GHL pipeline stage mapping); `10_PERFORMANCE/HISTORICAL_BASELINE.md` (shape of the last real export used)
Next review: before first live import, or on any platform export-format change

---

## Honest starting position
**Nothing is auto-connected today.** No live Meta/Google/GHL feed writes into this Marketing OS. The Apps Script (`08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs`) connects to GHL and writes to the `.gsheet` master sheet, but that sheet is not filesystem-readable from this workspace (see `10_PERFORMANCE/DATA_SOURCES.md`). Minimum viable process today is **weekly CSV export + manual paste** into `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` / `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`.

Meta/Google export field names below are DRAFT — pending platform verification (build brief §2.9). Do not treat any field name as a confirmed current export column without checking the live export first.

---

## Meta Ads export → registry mapping (DRAFT)
| Meta export field (typical) | Registry field | Registry file |
|---|---|---|
| Campaign name | Name / CampaignID (derive ID) | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Ad set name | Audience (partial) | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Ad name | Title (match to CreativeID) | `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv` |
| Amount spent | Spend | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Results / Leads | Leads | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Cost per result | CPL | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| CTR (link click-through rate) | (new field — not in current registry) | n/a |

## Google Ads export → registry mapping (DRAFT)
| Google export field (typical) | Registry field | Registry file |
|---|---|---|
| Campaign | Name / CampaignID | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Cost | Spend | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Conversions (leads) | Leads | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Cost / conv. | CPL | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |

## GHL export → registry mapping (DRAFT)
| GHL field | Registry field | Registry file |
|---|---|---|
| Contact source / campaign tag | CampaignID (match) | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Pipeline stage | Responded / Appointments (derive from stage rank — see `10_PERFORMANCE/KPI_DEFINITIONS.md`) | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| Opportunity status (won/lost) | Decision (partial) | `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` |
| — any name/phone/email field — | **DO NOT IMPORT.** Aggregate/count only, per PII rule. | n/a |

## Minimum viable process (today)
1. Export weekly from Meta Ads Manager, Google Ads, and GHL (pipeline report).
2. Aggregate to campaign level (never paste individual lead rows into the Marketing OS — PII rule, build brief §2.10).
3. Paste aggregate rows into `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`, updating Spend/Leads/Responded/CPL/CostPerResponded/Appointments/CPA.
4. Log the import date and source file path in the campaign's Decision/Lessons or a note field.
5. If a number can't be traced to an export, mark it "unknown" — never estimate silently.

## READS FROM
`08_OPERATIONS/01_CRM_AND_TRACKING/`, `08_OPERATIONS/02_SCRIPTS/`

## FEEDS INTO
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`, `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`, `13_MARKETING_OPERATIONS/DATA_DICTIONARY.md`
