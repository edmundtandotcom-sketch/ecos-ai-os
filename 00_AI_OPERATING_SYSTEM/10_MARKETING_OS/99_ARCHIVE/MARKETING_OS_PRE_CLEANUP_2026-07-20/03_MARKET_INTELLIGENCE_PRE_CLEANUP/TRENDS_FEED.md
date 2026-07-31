# TRENDS_FEED
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `00_AI_OPERATING_SYSTEM\08_OPERATIONS\03_AUTOMATIONS\rei-weekly-content-brief_SKILL.md` + `00_AI_OPERATING_SYSTEM\06_KNOWLEDGE_VAULT\01_MARKET_INTELLIGENCE\`
Evidence level: Tier 3 (live-scraped external signals, not REI performance data)
Supersedes: none
Sources: files above
Next review: next Monday content-brief run

---

## Purpose
State what the live weekly market-signal automation covers, so campaign/content planning knows where fresh trend data actually comes from — thin by design, this is a pointer, not a digest of every past brief.

## Current State — Live
`rei-weekly-content-brief` (APPROVED MASTER, **v2.1 — re-scoped 2026-07-11 per Decision 067: all Family Legacy/Mash-up/SI-06 classification removed**, every Monday 9am) runs a unified weekly + conditional bi-weekly rollup:
- **Tier 1 (live scrape, required):** URA transaction/price data, EdgeProp launches, StackedHomes, 99.co, MoneySmart rates, PropNex news.
- **Tier 2 (creator patterns):** Marcus Luah, JNA, StackedHomes YouTube — format/script pattern study.
- **Tier 3 (sentiment/signals):** Google Trends, Reddit r/singapore, Hardwarezone, Facebook groups, Telegram, LinkedIn, YouTube comments, Instagram/TikTok, Google News alerts.
Output: 8–12 signals filtered through a 6-step angle test (REI Method fit, belief shift, content gap, emotional hook, SI-05/Evergreen-Authority relevance — SI-06/Mash-up removed per Decision 067, provable), ranked 1–5, each producing 3 YouTube script format variations + 3 WhatsApp segment messages. No synthesis fallback — if a source is unreachable it's logged, not guessed.

## Where Output Lives
`01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Contents\` — `[WEEK]` briefs, `[ROLLUP]` bi-weekly syntheses, `[LIBRARY]` topic write-ups (e.g. CCR Reversal & Regional Rotation, Condo Dip vs Downturn, Global Uncertainty & Structured Positioning — all dated 2026-07-06). Most recent batch (5 files) is registered in `06_KNOWLEDGE_VAULT\01_MARKET_INTELLIGENCE\` per `WEEKLY_BRIEFS_AND_ADS_REGISTRY.md`; the rest stays registered-not-copied in the original folder, unmigrated.

## What This File Is Not
Not a live trend feed itself — it does not pull data. For current signals, run the automation or read the latest `[WEEK]` brief directly. This file will go stale the moment a new weekly brief lands; treat the "Current State" section above as structural, not as this week's news.

## Gap
No dedicated trend-velocity dashboard exists — trend data lives as discrete dated Markdown briefs, not a queryable feed. A future `10_PERFORMANCE` or automation upgrade could change this; not attempted here (out of scope for this build).
