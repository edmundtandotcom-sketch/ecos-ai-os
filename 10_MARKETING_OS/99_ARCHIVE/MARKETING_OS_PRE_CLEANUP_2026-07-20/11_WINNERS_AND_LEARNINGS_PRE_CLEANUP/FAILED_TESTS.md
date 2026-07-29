# FAILED_TESTS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A (placeholder — no formal failures on record)
Supersedes: none
Sources: `09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv`, `00_COMMAND_CENTER/MARKETING_MATURITY_DIAGNOSIS.md` (testing discipline scored 3/10)
Next review: when the first experiment or campaign is formally logged as failed/killed

---

## Placeholder
No formally recorded failed test exists in the source material reviewed for this build. This is itself a finding, not a clean bill of health: testing discipline is scored 3/10 in the marketing maturity diagnosis (build brief §7), and `09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv` is currently header-only — no experiment has ever been run and logged in this system.

Historical failures almost certainly occurred (88 leads across multiple campaigns and angles over just one 30-day window implies underperforming variants existed — see `10_PERFORMANCE/HISTORICAL_BASELINE.md` ad-level response-rate spread, 0% to 100% by ad), but none were captured as a "why we killed this" record. This matches `11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv` LRN-004: campaign learning was not captured at close historically.

## Going forward
Log a kill here using `12_TEMPLATES/CAMPAIGN_POSTMORTEM.md` or `12_TEMPLATES/EXPERIMENT_BRIEF.md` decision-rule output whenever a campaign or experiment is formally killed, with: what was tested, KPI, decision rule, result, and root-cause hypothesis. Do not backfill invented failures — mark historical gaps as unknown, not as reconstructed data.

## READS FROM
`09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv`, `10_PERFORMANCE/HISTORICAL_BASELINE.md`

## FEEDS INTO
`11_WINNERS_AND_LEARNINGS/LEARNING_REGISTRY.csv`, `09_EXPERIMENTS/BACKLOG.md`
