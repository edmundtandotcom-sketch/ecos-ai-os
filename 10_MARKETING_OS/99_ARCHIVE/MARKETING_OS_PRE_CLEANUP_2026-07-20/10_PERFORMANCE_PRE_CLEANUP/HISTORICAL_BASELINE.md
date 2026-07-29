# HISTORICAL_BASELINE
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE reproduces figures from the archived Codex snapshot — the xlsx/json originals remain the underlying record (read-only, contains PII, see `10_PERFORMANCE/DATA_SOURCES.md` §3)
Evidence level: 2 (verified behavioural — spend/leads/CPL from a real ad-platform export; no lead→client/revenue join exists, so no Tier 1 claim is made anywhere in this file)
Supersedes: none
Sources: `01_PROPERTY_BUSINESS\01_CLIENT_EDITION\99_ARCHIVE\OLD_OPERATIONS_AND_DASHBOARD_SUPERSEDED_2026-07-04\Codex\lead_summary_cost_batch_payload.json` (and matching `lead_summary_cost_compact_part1.json` / `part2.json`)
Next review: when a newer export is imported (see `10_PERFORMANCE/IMPORT_SPECS.md`)

---

## What this is
The only current performance baseline for the business. One snapshot, "Past 30 Days," date range **2026-05-26 to 2026-06-24** (generated using 2026-06-24 as "today"). Aggregate counts only — no PII. No number in this file has been updated since 2026-06-24.

## Headline totals (Tier 2)
| Metric | Value |
|---|---|
| Total leads | 88 |
| Responded leads | 35 |
| Response rate | 39.8% |
| Total paid spend | $13,519.00 |
| Cost per lead (CPL) | $153.62 |
| Cost per responded lead | $386.26 |

## By channel (Tier 2)
| Channel | Applies to | Spend | Leads | Responded | CPL | Cost/Responded |
|---|---|---|---|---|---|---|
| Meta Ads | Meta Lead Form-Legacy Launch Ladder V.1; Meta LP-Legacy Launch LP | $7,928.00 | 53 | 19 | $149.58 | $417.26 |
| Google Ads | Google LP-Family Legacy Ladder | $5,591.00 | 35 | 16 | $159.74 | $349.44 |
| **Total Paid** | all three tabs | **$13,519.00** | **88** | **35** | **$153.62** | **$386.26** |

## Named campaigns (Tier 2 — lead/response counts only; spend not broken out per campaign in source)
Per-campaign spend was not present in the source payload — only channel-level spend. Per-campaign lead/responded counts are real, direct from source.

| Campaign | Channel | Leads | Responded | Response rate | First–last lead date |
|---|---|---|---|---|---|
| 24 April-Form \| Legacy Launch NL-Videos/Images | Meta (Lead Form) | 35 | 12 | ranges 26.1–100% by ad | 2026-05-26 to 2026-06-24 |
| 14 May-Demand Gen-Hook Vsl1-Financial Shock | Google | 16 | 6 | 40.0% (primary ad) | 2026-05-26 to 2026-06-08 |
| 9 May-Retargeting Video-Why I Do What I Do | Google | 5 | 1 | 20.0% | 2026-05-28 to 2026-06-10 |
| 14 June-Reels-LP-Lentor Gardens | Meta (Landing Page) | 7 | 3 | ranges 0–100% by ad | 2026-06-14 to 2026-06-23 |
| 14 June-Exit First Angle-LP-Lentor Gardens | Meta (Landing Page) | 5 | 1 | 20–25% by ad | 2026-06-14 to 2026-06-22 |
| 15 June-Advisor vs Agent Angle-LP-Lentor Gardens | Meta (Landing Page) | 4 | 1 | 0–33.3% by ad | 2026-06-15 to 2026-06-16 |
| 19 May-Drive Conversions \| Videos | Google | 4 | 4 | 100% (both ads) | 2026-05-30 to 2026-06-04 |
| (unlabelled Google campaign, ID 23849239348, blank name) | Google | 8 | 5 | 50–100% | 2026-06-12 to 2026-06-24 |

Full ad-level breakdown (23 ad rows) is in the source JSON; only campaign-level rollups are reproduced here to keep this file boardroom-usable. The 6 highest-signal campaigns are also seeded as COMPLETED rows in `08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv`.

## What this data does NOT show
- **No appointment, booking, or consult-completion data.** The source is a lead-and-response export only.
- **No cost-per-appointment or CPA.** Cannot be computed without appointment data.
- **No lead → client → revenue join.** This is explicitly why no Tier 1 figure exists anywhere in the Marketing OS (build brief §5). Founder revenue figures ($6.6M→$9M NAV etc., contradiction C10) are separately [VERIFY]-flagged and are not derived from this file.
- **No creative-level performance** (which of the 16 Legacy Launch video ads, if any, are represented in this snapshot — the snapshot predates their 2026-07-10 edit completion date, so none of the 16 finished ads are in this baseline).

## Handling rule
This file is the safe, PII-free extraction. Do not go back to the source xlsx/json for anything beyond what's already aggregated here without re-applying the PII rule in `10_PERFORMANCE/DATA_SOURCES.md` §3.

## READS FROM
Archived Codex folder (read-only, PII rule applies)

## FEEDS INTO
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` (COMPLETED rows), `11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv`, `00_COMMAND_CENTER/SOURCE_OF_TRUTH_MAP.md`
