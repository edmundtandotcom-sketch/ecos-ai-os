# ACTIVE CAMPAIGNS — MARKETING OS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `08_CAMPAIGNS\CAMPAIGN_REGISTRY.csv` (once built). THIS FILE is the Command-Center summary view.
Evidence level: Mixed (per campaign)
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF §8/§9; SOURCE_OF_TRUTH_MAP.md
Next review: weekly, or on any campaign status change

---

Purpose: at-a-glance status of live and imminent campaigns. Full records live in `08_CAMPAIGNS\` (pending build). Every row states its **engine** and **evidence tier**.

## Snapshot
| Campaign ID | Engine | State | Evidence | Points to |
|---|---|---|---|---|
| `CMP-20260710-LEGACYLAUNCH-OWNERS-001` | Engine 1 — Client | ACTIVE (pilot **APPROVED**, Decision 059) | Tier 5 creative; Tier 2 predecessor baseline | `00_AI_OPERATING_SYSTEM\05_CONTENT_MARKETING_ENGINE\01_CAMPAIGN_LEGACY_LAUNCH\` |
| `CMP-2026xxxx-MARKETMAKER-AGENTS-001` | Engine 2 — Agent | PLANNED (validation test) | DRAFT brief; needs real GCI proof (Decision 5) | Agent Edition offer ladder (DRAFT) |
| Historical (Codex aggregates) | Engine 1 — Client | COMPLETED | Tier 2 (through 2026-06-24) | `10_PERFORMANCE\HISTORICAL_BASELINE.md` (pending) |

## Notes
- **Legacy Launch** is the **APPROVED pilot** (Decision 059, 2026-07-11; live, 16 finished ads, diagnostic funnel exists, real predecessor baseline). Audience is decouple-specific SI-05 per Decision 037 (C06 RESOLVED). Remaining launch gates: live diagnostic redeploy + GHL field rename `spl_step_result`→`spl_move_result` (Decision 055 cascade), tracking verification, kill/scale criteria. Baseline to beat: Meta CPL $149.58 (Decision 056).
- **Market Maker validation** is a PLANNED test to validate agent-engine offer economics. Gate the proof asset on real before/after GCI figures — no fabrication.
- **Historical rows** are the archived Codex aggregates (past-30-days paid $13,519 · 88 leads · $153.62 CPL, through 2026-06-24). PII-free aggregates only; no lead→revenue join exists.
- Nothing here is a proven winner. Creative and copy are Tier 5 until live data earns Tier 2.

READS FROM: `08_CAMPAIGNS\` (once built); `SOURCE_OF_TRUTH_MAP.md`; `CONTRADICTION_REGISTER.md`.
FEEDS INTO: weekly marketing review; `SYSTEM_HEALTH.md`.
