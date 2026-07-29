# _REGISTRY_SPEC — EXPERIMENT_REGISTRY.csv
Version: v0.1
Status: STUB
Date: 2026-07-11
Supersedes: none
Sources: SALES_OS_BUILD_SPEC_v1 mandate §25/§26 (standard outputs); `10_MARKETING_OS\09_EXPERIMENTS\EXPERIMENT_REGISTRY.csv` (sibling column pattern)

---

## Purpose

Column definitions for `EXPERIMENT_REGISTRY.csv`. One row = one sales experiment, from hypothesis through recommendation.

## Columns

| Column | Definition |
|---|---|
| `ExperimentID` | Unique ID, format `EXP-###` |
| `Hypothesis` | The specific, falsifiable claim being tested |
| `Current` | What the sales process currently does (the control) |
| `Variant` | What is being tested instead |
| `ClientType` | Which buyer archetype / readiness stage this experiment targets (or "All") |
| `SampleSize` | Minimum number of consults/leads needed before reading a result |
| `Metric` | The single metric this experiment is judged on |
| `Risk` | What breaks if the variant underperforms; blast radius |
| `StartDate` / `EndDate` | Experiment window |
| `Result` | Outcome once concluded — cite the metric value, not an impression |
| `Confidence` | High / Medium / Low, with one-line reasoning |
| `Recommendation` | Keep / roll back / iterate — the actual call |
| `SystemUpdate` | Which file(s) this experiment's outcome should update, and whether that update has been made |

## Rules

- No row proceeds past `Result` without a `Confidence` rating.
- A `Recommendation` of "Keep" requires the corresponding `SystemUpdate` to name the exact file changed.
- PII rule applies: `ClientType` is an archetype, never a name.

READS FROM: SALES_OS_BUILD_SPEC_v1 mandate.
FEEDS INTO: `EXPERIMENT_REGISTRY.csv`; `27_SALES_LEARNINGS\LEARNING_REGISTRY.csv` on conclusion.
