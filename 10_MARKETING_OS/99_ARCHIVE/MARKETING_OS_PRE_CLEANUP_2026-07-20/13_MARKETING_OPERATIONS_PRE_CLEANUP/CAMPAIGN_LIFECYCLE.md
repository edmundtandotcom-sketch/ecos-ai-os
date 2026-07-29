# CAMPAIGN LIFECYCLE
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — operating model, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §2, §7 (maturity: Campaign planning 6, Testing discipline 3), §8 (13_MARKETING_OPERATIONS, 08_CAMPAIGNS); QA_CHECKLISTS.md
Next review: after first full campaign cycle (Legacy Launch pilot) completes

## 1. The 13 stages
1. Intake — CAMPAIGN_BRIEF.md filed, ID assigned.
2. Strategy fit check — engine, positioning, priority alignment (Strategy Office if contested).
3. Audience & offer definition — segment, qualified-lead definition, offer ladder position.
4. Framework & angle selection — cite 05_FRAMEWORK_LIBRARY, assign ANG- ID(s).
5. Creative brief & production — CREATIVE_BRIEF.md per asset.
6. Copy draft — CP- variants drafted against chosen frameworks.
7. Funnel/landing build — FUNNEL_BRIEF.md, FUN- ID.
8. QA — cross-channel checklist (QA_CHECKLISTS.md Stage 8).
9. Launch readiness gate — business-level checklist (QA_CHECKLISTS.md Stage 9).
10. Launch / go-live — status → ACTIVE.
11. Monitor & optimize — cadence per REVIEW_CADENCE.md (daily if spending).
12. Performance review — PERFORMANCE_REVIEW.md at weekly/monthly/quarterly cadence.
13. Postmortem & archive — CAMPAIGN_POSTMORTEM.md, learnings to 11_WINNERS_AND_LEARNINGS, status → COMPLETED/PAUSED.

## 2. Diagnosis hierarchy (1–13, tracking → capacity)
When a campaign underperforms, diagnose in this order — fix the lowest-numbered failure first, because higher-numbered diagnoses are unreliable until lower ones are ruled out:
1. Tracking/attribution broken (is the data even accurate?)
2. Platform delivery/spend pacing issue
3. Audience targeting mismatch
4. Offer-audience mismatch
5. Hook/creative attention failure (low hook hold / CTR)
6. Message-belief mismatch (wrong Trigger Bank door)
7. Proof/credibility gap
8. CTA clarity/friction
9. Funnel/landing-page leak
10. Lead quality vs. lead volume tradeoff
11. Follow-up/nurture speed and consistency
12. Sales-conversation/consult conversion
13. Sales capacity (advisor bandwidth to handle volume)

## 3. Kill / Keep / Iterate / Scale
- **Kill:** KPI below floor after minimum useful data reached (see EXPERIMENT_BRIEF.md/CAMPAIGN_BRIEF.md §11) AND no viable iteration hypothesis AND before-kill checklist passed.
- **Keep:** at or near target, no clear scale signal yet — hold and re-review next cadence.
- **Iterate:** below target but diagnosis hierarchy points to a fixable single-variable cause — spin an EXPERIMENT_BRIEF.md.
- **Scale:** at/above target with minimum useful data reached and diagnosis rules out lucky variance — increase budget/reach incrementally, re-review at next cadence.
- Directional-only baseline (not a target): past-30-days aggregate $153.62 CPL / $386.26 cost-per-responded-lead (source: `lead_list_analysis_source_latest.xlsx`, Tier 2, data through 2026-06-24). Do not treat as a hard threshold without Edmund/Cindior sign-off.

### Before-kill checklist
1. Tracking confirmed correct (Stage 1 of diagnosis hierarchy ruled out).
2. Minimum useful data threshold actually reached.
3. At least one iteration already attempted, or iteration hypothesis explicitly rejected with reasoning.
4. Sales-capacity and follow-up-speed ruled out as the real cause (Stages 11–13).
5. Kill decision logged in CAMPAIGN_POSTMORTEM.md or PERFORMANCE_REVIEW.md with evidence.

## 4. 13-status asset lifecycle
Draft → In Production → Ready for QA → QA Passed → QA Failed – Revise → Approved for Launch → Live → Paused → Winning – Scale → Underperforming – Iterate → Kill → Archived → Superseded.

Status lives in the owning registry (CREATIVE_REGISTRY.csv / CAMPAIGN_REGISTRY.csv), not in the filename.
