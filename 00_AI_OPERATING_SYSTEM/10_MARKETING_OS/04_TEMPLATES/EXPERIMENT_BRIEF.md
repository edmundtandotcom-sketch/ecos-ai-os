# EXPERIMENT BRIEF TEMPLATE
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — template, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §2, §8 (12_TEMPLATES, 09_EXPERIMENTS)
Next review: on first live use; then quarterly

Copy into `09_EXPERIMENTS/ACTIVE/` as `<ExperimentID>.md`; register a row in EXPERIMENT_REGISTRY.csv.

## 1. Identity
- Experiment ID (EXP- per NAMING_CONVENTIONS.md): | Campaign ID (if attached): | Engine:

## 2. Variable
- The ONE thing being tested (one variable only — no compound tests):

## 3. Hypothesis
- "If we change [variable], then [metric] will [direction] because [reasoning]."

## 4. Control
- Current/baseline version (asset ID, evidence tier of baseline):

## 5. Variant
- New version being tested (asset ID):

## 6. KPI
- Single success metric: | Direction that counts as a win:

## 7. Evaluation conditions
- Audience/placement/budget conditions that must hold for the result to be valid:

## 8. Minimum useful data
- Sample size / spend / time floor before reading the result (state the rule, not a guess):

## 9. Decision rule
- If KPI clears target with minimum data reached → [scale/adopt variant]
- If KPI misses target with minimum data reached → [kill/revert to control]
- If minimum data not reached by [date] → [extend/kill — state which]

## 10. Status & result
- Status: BACKLOG | ACTIVE | COMPLETED | Start date: | End date:
- Result: | Decision made: kill | keep | iterate | scale
- Learning extracted → LEARNING_REGISTRY.csv row ID:

## 11. Sign-off
- Filed by: | Date: | Reviewed by:
