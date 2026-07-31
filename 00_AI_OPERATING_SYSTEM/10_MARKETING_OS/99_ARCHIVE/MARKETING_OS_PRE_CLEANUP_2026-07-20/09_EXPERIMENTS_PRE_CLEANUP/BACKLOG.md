# EXPERIMENTS BACKLOG
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (backlog of open hypotheses; not yet running — see `09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv` for the empty active registry)
Evidence level: 5 (all entries are hypotheses — none have run)
Supersedes: none
Sources: `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`, `05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/`, `05_CONTENT_MARKETING_ENGINE/04_TRIGGER_MARKETING/`, `04_AGENT_EDITION_OS/02_MARKETING/`, `00_COMMAND_CENTER/CONTRADICTION_REGISTER.md` (C06)
Next review: when any entry moves to `09_EXPERIMENTS/ACTIVE/`

---

## Purpose
Real, open hypotheses found in the inventory — not invented test ideas. Each entry states hypothesis, KPI, and what would invalidate it. Nothing here is running; promote to `EXPERIMENT_REGISTRY.csv` + `ACTIVE/` when a campaign is ready to spend against it.

---

## BL-001 — Which of the 16 Legacy Launch ad angles wins
**Hypothesis:** Among the 16 finished Legacy Launch video ads (`07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`, CR-...-VID-001..016), some outperform others on CPL / thumbstop / response rate once launched.
**Status:** Cannot run yet — needs launch. All 16 ads are Tier 5 (rubric-scored, zero market data) and currently unmapped to a confirmed angle (AngleID = "pending" for all 16).
**KPI:** Cost per lead, outbound CTR, cost per responded lead (once tracking is verified — see `10_PERFORMANCE/DATA_SOURCES.md`).
**What would invalidate it:** If spend never reaches the ≥50 leads/angle clean-read threshold used elsewhere in this business (`04_AGENT_EDITION_OS/02_MARKETING/MAS_Campaign_Brief_MM_ValidationTest_v1.0_DRAFT.md` clean-read rule), no angle can be declared a winner — see `11_WINNERS_AND_LEARNINGS/WINNING_ASSETS_POLICY.md`.
**Blocked by:** Legacy Launch campaign launch + kill/scale criteria (TBD — `08_CAMPAIGNS/ACTIVE/CMP-20260710-LEGACYLAUNCH-OWNERS-001.md`).

## BL-002 — Legacy Launch audience: broad mature owner vs decouple-specific (C06) · SUPERSEDED BY RULING (Decision 037, 2026-07-11)
**Hypothesis:** The active Legacy Launch campaign brief's broad "mature private owner, no clear plan" audience and the Trigger Marketing Bank's decouple-specific SI-05 audience (condo owners, late 30s–50s, first/second property) will perform differently — one may out-convert the other, or the mismatch may already be suppressing performance.
**KPI:** CPL and response rate by audience definition, once split-tested.
**What would invalidate it:** If both audiences produce statistically similar CPL/response, the C06 distinction may not matter in practice and the contradiction can be closed as low-priority.
**Status:** SUPERSEDED BY RULING — Edmund ruled Decision 037 (audience is decouple-specific SI-05, reconfirmed by Decisions 059/064); no split test needed. Do not promote to `EXPERIMENT_REGISTRY.csv`.
**Source:** `00_COMMAND_CENTER/CONTRADICTION_REGISTER.md` C06.

## BL-003 — Trigger Marketing Bank hook families, comparative test
**Hypothesis:** Among the Legacy Launch [LL] hooks in `05_CONTENT_MARKETING_ENGINE/04_TRIGGER_MARKETING/MAS_TRIGGER_MARKETING_BANK_v1.0.md` §1 (e.g. "your ABSD headroom" vs "colleagues have two" vs "equity sitting there"), some hook families produce higher engagement/response than others.
**KPI:** Outbound CTR, comment/DM rate on soft-CTA posts, cost per responded lead.
**What would invalidate it:** If all hook families in the bank perform within noise of each other, the bank's internal variety may not matter and effort should shift to angle-level testing (BL-001) instead.
**Note:** None of these hooks are currently marked [PROVEN] per the bank's own maintenance rule (§ Content Bank Maintenance Rules item 3) — this experiment is the mechanism that would earn that label.

## BL-004 — Diagnostic-quiz completion vs direct-booking funnel
**Hypothesis:** Routing Legacy Launch traffic through a diagnostic quiz / Property Position Checklist before offering the 1-Hour Position Review consult produces a different (likely higher-quality, possibly lower-volume) lead than a direct "book now" CTA.
**KPI:** Cost per booked appointment, booking-to-consult-completion rate, lead quality grade (A/B/C/D per `08_OPERATIONS/01_CRM_AND_TRACKING/01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` §5).
**What would invalidate it:** If completion-rate drop-off at the quiz step outweighs any quality gain, the direct-booking path wins on efficiency.
**Blocked by:** Confirmed build status of the diagnostic funnel / landing page for Legacy Launch — not verified as built in this pass (see `08_CAMPAIGNS/ACTIVE/CMP-20260710-LEGACYLAUNCH-OWNERS-001.md`).

## BL-005 — Agent Edition angle test (7 mechanism-led angles)
**Hypothesis:** Among the 7 DRAFT mechanism-led angles in `04_AGENT_EDITION_OS/02_MARKETING/MAS_AdAngle_Master_MarketMaker_v2.0_DRAFT.md` §3 (Agent vs Business, Own Your Market, Own the Conversation, Business in a Box, + 3 more not reviewed in this pass), the flagship Angle 1 ("Agent vs Business") reframe outperforms the mechanism-specific angles for pulling Sub-Type B into the free Scorecard.
**KPI:** Cost per Scorecard lead (primary, per the validation-test brief), outbound CTR (thumbstop), DM/reply rate, cost per completed Scorecard.
**What would invalidate it:** A mechanism-specific angle (e.g. Angle 2 "Own Your Market") outperforming the flagship reframe at the ≥50 leads/angle clean-read threshold.
**Vehicle:** `08_CAMPAIGNS/PLANNED/CMP-20260706-MARKETMAKER-AGENTS-001.md` — this is the campaign designed to answer BL-005 (primary angles for the first test: 3 Vendor Lie, 2 The Ceiling, 5 The Machine, per the DRAFT brief).
**Gap:** Founder before/after GCI proof needed to finalize proof creatives for this angle set — see `00_COMMAND_CENTER/DECISIONS_REQUIRED.md` item 5.

---

## READS FROM
`07_CREATIVE_LIBRARY/`, `08_CAMPAIGNS/`, `05_CONTENT_MARKETING_ENGINE/04_TRIGGER_MARKETING/`, `04_AGENT_EDITION_OS/02_MARKETING/`, `08_OPERATIONS/01_CRM_AND_TRACKING/`

## FEEDS INTO
`09_EXPERIMENTS/EXPERIMENT_REGISTRY.csv` (once promoted to active), `09_EXPERIMENTS/ACTIVE/`, `11_WINNERS_AND_LEARNINGS/`
