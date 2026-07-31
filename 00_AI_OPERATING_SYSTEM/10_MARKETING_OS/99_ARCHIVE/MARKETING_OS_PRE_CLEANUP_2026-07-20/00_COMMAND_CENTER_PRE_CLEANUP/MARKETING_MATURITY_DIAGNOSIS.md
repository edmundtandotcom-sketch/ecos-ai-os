# MARKETING MATURITY DIAGNOSIS — MARKETING OS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (marketing maturity snapshot). Scores are the orchestrator's Phase-2 judgment — reproduced, not re-derived.
Evidence level: Mixed (each row cites its evidence tier / inventory finding)
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF §7; CONTRADICTION_REGISTER.md; SOURCE_OF_TRUTH_MAP.md
Next review: quarterly, or when a scored area materially changes

---

Purpose: an honest, evidence-cited baseline of marketing maturity across 20 areas. Scores are **kept as set by the build brief §7** (do not change). Each area states: maturity /10 · evidence · main weakness · risk · next step. Category window is flagged **AT RISK 10/20** — the standout urgency.

| # | Area | /10 |
|---|---|---|
| 1 | Strategy | 7 |
| 2 | Positioning | 8 |
| 3 | Audience intelligence | 8 |
| 4 | Offer architecture | 7 |
| 5 | Campaign planning | 6 |
| 6 | Copy | 7 |
| 7 | Creative | 7 |
| 8 | Organic content | 6 |
| 9 | Paid media | 4 |
| 10 | Funnels | 5 |
| 11 | CRM / nurture | 5 |
| 12 | Tracking | 4 |
| 13 | Attribution | 3 |
| 14 | CRO | 3 |
| 15 | Sales feedback | 5 |
| 16 | Knowledge management | 8 |
| 17 | Testing discipline | 3 |
| 18 | Market intelligence | 7 |
| 19 | Governance | 8 |
| 20 | Team execution | 5 |

---

## 1 · Strategy — 7
- **Evidence:** Clear governing positioning + two-engine model in `00_COMMAND_CENTER\01_BUSINESS_POSITIONING.md`.
- **Weakness:** Strategy is documented but not yet expressed as a sequenced marketing plan with owners and dates.
- **Risk:** Direction without a campaign calendar defaults to reactive execution.
- **Next step:** Convert priorities into a dated campaign plan in `08_CAMPAIGNS\`.

## 2 · Positioning — 8 · category window AT RISK 10/20
- **Evidence:** Agent engine LOCKED 2026-07-06; client engine strong but CANDIDATE-churning (Big Idea / Mechanism / CategoryKing).
- **Weakness (resolved 2026-07-11):** Client-side naming locked by Decision 055 (Move everywhere); category window still closing — publish.
- **Risk:** A competitor can occupy the category if publishing stalls on internal naming debates.
- **Next step:** C01/C02 resolved (Decision 055) — ship the pilot to plant the category.

## 3 · Audience intelligence — 8
- **Evidence:** Buyer Segment Library, TRAPS bank, VoC annex (166–376 real consult quotes).
- **Weakness:** Buyer definition drift (C03) and HDB/EC in-or-out (C04) unresolved.
- **Risk:** Targeting and creative eligibility contradict across assets.
- **Next step:** Publish `02_CUSTOMER_INTELLIGENCE\SEGMENT_USAGE_GUIDE.md` once C03/C04 are called.

## 4 · Offer architecture — 7
- **Evidence:** Both offer ladders documented (client free→diagnostic→session→blueprint; agent scorecard→S$297→S$7,000).
- **Weakness:** Session naming conflict (C02); no unit-economics validation of the ladder.
- **Risk:** CTA confusion in-funnel; no proof the price points convert.
- **Next step:** Lock offer names; validate economics via the Market Maker test campaign.

## 5 · Campaign planning — 6
- **Evidence:** Campaigns exist but no registry; door overlap (C06/C11).
- **Weakness:** No single campaign registry or lifecycle discipline before this build.
- **Risk:** Overlapping doors compete for the same audience/budget.
- **Next step:** Adopt `08_CAMPAIGNS\CAMPAIGN_REGISTRY.csv` + lifecycle for every campaign.

## 6 · Copy — 7
- **Evidence:** Trigger Bank, hook/CTA banks, signature lines — rubric-proven only.
- **Weakness:** No copy is market-validated (Tier 5); no A/B history.
- **Risk:** "Winning" copy is asserted, not measured.
- **Next step:** Route top hooks into logged experiments (`09_EXPERIMENTS\`).

## 7 · Creative — 7
- **Evidence:** 16 Legacy Launch video ads finished (×2 orientations), Tier 5.
- **Weakness:** Zero market data; destinations/angle IDs unassigned.
- **Risk:** Finished ≠ effective; treating them as proven is unfounded.
- **Next step:** Seed the creative registry; launch with tracking to earn Tier 2 data.

## 8 · Organic content — 6
- **Evidence:** YouTube Authority Engine + six content pillars defined.
- **Weakness:** Cadence and content-to-funnel wiring not systematised.
- **Risk:** Organic effort not tied to the diagnostic funnel.
- **Next step:** Wire pillars → diagnostic in `06_CHANNEL_PLAYBOOKS\ORGANIC_SOCIAL` / `YOUTUBE`.

## 9 · Paid media — 4
- **Evidence:** Real historical spend archived (Codex: $13,519 · 88 leads · $153.62 CPL, through 2026-06-24, Tier 2); no current in-system structure; specs stale (C05).
- **Weakness:** No live account structure documented in-system; platform specs unverified.
- **Risk:** Relaunching without structure or current specs repeats past inefficiency.
- **Next step:** Build `06_CHANNEL_PLAYBOOKS\META_ADS` / `GOOGLE_ADS` (DRAFT — pending platform verification); re-verify specs.

## 10 · Funnels — 5
- **Evidence:** Diagnostic quiz spec exists; LL landing folder empty; no CRO loop.
- **Weakness:** Landing/funnel assets not built; no conversion measurement loop.
- **Risk:** Traffic lands nowhere optimised; spend leaks.
- **Next step:** Build the LL landing page; define the CRO loop in `10_PERFORMANCE\`.

## 11 · CRM / nurture — 5
- **Evidence:** GHL diagnostic build spec + D5 case routing exist; import NOT executed; nurture folders empty.
- **Weakness:** 7,272 GHL-eligible contacts un-imported; sequences unbuilt.
- **Risk:** Warm audience sits idle; follow-up promises undelivered.
- **Next step:** Execute GHL import (owner decision); build nurture sequences.

## 12 · Tracking — 4
- **Evidence:** Live Apps Script + Google Ads Script; data unreadable from workspace (.gsheet).
- **Weakness:** Performance data inaccessible to the OS.
- **Risk:** Decisions made blind to live numbers.
- **Next step:** Grant read access or export CSVs (owner decision); document in `10_PERFORMANCE\DATA_SOURCES.md`.

## 13 · Attribution — 3
- **Evidence:** No revenue join anywhere in the data (Codex has lead→response, not lead→client).
- **Weakness:** No lead-to-revenue linkage — so no Tier 1 exists.
- **Risk:** Cannot compute true CAC or ROAS; budget decisions unanchored.
- **Next step:** Define the revenue-join spec in `10_PERFORMANCE\IMPORT_SPECS.md`.

## 14 · CRO — 3
- **Evidence:** No experiments logged.
- **Weakness:** No experimentation infrastructure before this build.
- **Risk:** Optimisation is guesswork.
- **Next step:** Stand up `09_EXPERIMENTS\` and run the first logged test.

## 15 · Sales feedback — 5
- **Evidence:** 490 transcripts mined for VoC; no lead-grade feedback loop.
- **Weakness:** Sales insight not fed back to grade lead quality.
- **Risk:** Marketing optimises for volume, not qualified leads.
- **Next step:** Define a lead-grade feedback loop (sales → `11_WINNERS_AND_LEARNINGS\`).

## 16 · Knowledge management — 8
- **Evidence:** Strong AI OS discipline; marketing knowledge previously scattered — this OS consolidates it.
- **Weakness:** Marketing artefacts were fragmented across folders pre-build.
- **Risk:** Drift if the registries are not maintained.
- **Next step:** Enforce `_INDEX.md` + change-control on every new asset.

## 17 · Testing discipline — 3
- **Evidence:** No structured test history.
- **Weakness:** Claims of "what works" rest on rubric scores, not tests.
- **Risk:** Repeated spend on unvalidated assumptions.
- **Next step:** Adopt the experiment brief + kill/scale/iterate statuses (`12_TEMPLATES\EXPERIMENT_BRIEF.md`).

## 18 · Market intelligence — 7
- **Evidence:** Live automations (rei-weekly-content-brief, singapore-property-ads-brief) + unmigrated Weekly Ads/Contents library.
- **Weakness:** Intelligence library unmigrated; not systematised into the OS.
- **Risk:** Insight exists but is not routed into planning.
- **Next step:** Point `03_MARKET_INTELLIGENCE\` at the live feeds; plan migration.

## 19 · Governance — 8
- **Evidence:** Marketing change-control was absent → this build creates it.
- **Weakness:** Root-level placement conflict (C14) unresolved.
- **Risk:** Governance gap at the top (constitution not amended).
- **Next step:** Resolve C14; operate `14_CHANGE_LOG\` for every change.

## 20 · Team execution — 5
- **Evidence:** Effective but single-operator; capacity risk.
- **Weakness:** Execution concentrated on one/two people.
- **Risk:** Bottleneck; single point of failure on delivery.
- **Next step:** Define responsibilities + cadence in `13_MARKETING_OPERATIONS\`.

---

READS FROM: MARKETING_OS_BUILD_BRIEF §7; `SOURCE_OF_TRUTH_MAP.md`; `CONTRADICTION_REGISTER.md`.
FEEDS INTO: `CURRENT_PRIORITIES.md`; `DECISIONS_REQUIRED.md`; `SYSTEM_HEALTH.md`.
