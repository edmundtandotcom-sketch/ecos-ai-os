# 03_MARKET_INTELLIGENCE — INDEX
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (pointer hub) — content masters live in `00_AI_OPERATING_SYSTEM\06_KNOWLEDGE_VAULT\` and `08_OPERATIONS\03_AUTOMATIONS\`
Evidence level: N/A (index)
Supersedes: none
Sources: files listed below
Next review: on next weekly brief cycle or automation change

---

## Purpose
Pointer hub for external market, competitor, ad-library, funnel-swipe, and search intelligence. This folder never re-runs or duplicates the live automations — it describes what they produce, where the data lives, and how proven (or not) each source is per the Tier-4 rule: **observed ≠ proven.**

## Files In This Folder

| File | Purpose | Reads From | Feeds Into |
|---|---|---|---|
| `_INDEX.md` | This hub | — | All files below |
| `COMPETITORS.md` | What competitor intel exists — PropertyLimBrothers threat, the weekly ads scraper, the Weekly Ads research library | Business Positioning master, `singapore-property-ads-brief` skill, Weekly Ads library | `05_FRAMEWORK_LIBRARY`, campaign strategy, `00_COMMAND_CENTER` category-window priority |
| `AD_LIBRARY.md` | Purpose + Tier-4 rule for swipe/reference sources; points at 1CC breakdown, guru deep-dives, Peng Joon | `1CC_TOP_PERFORMING_ADS_BREAKDOWN`, `04_MARKETING_REFERENCES` | `05_FRAMEWORK_LIBRARY\CREATIVE_FRAMEWORKS.md`, `07_CREATIVE_LIBRARY` |
| `FUNNEL_LIBRARY.md` | Purpose + Tier-4 rule for funnel/offer-ladder swipe sources | Same as AD_LIBRARY.md, Peng Joon product ladder | `05_FRAMEWORK_LIBRARY\FUNNEL_FRAMEWORKS.md` |
| `TRENDS_FEED.md` | Live weekly-brief automation state; current market signal sources | `rei-weekly-content-brief` skill, Weekly Contents library | Content Studio angle selection |
| `SEARCH_INTELLIGENCE.md` | Current state (no dedicated keyword/search-intent tool found); what's missing | Inventory findings only | SEO/AEO channel playbook gap flag |

## Live Automations (do not duplicate — reference only)
- `00_AI_OPERATING_SYSTEM\08_OPERATIONS\03_AUTOMATIONS\rei-weekly-content-brief_SKILL.md` — Monday 9am, weekly content + bi-weekly rollup, APPROVED MASTER
- `00_AI_OPERATING_SYSTEM\08_OPERATIONS\03_AUTOMATIONS\singapore-property-ads-brief_SKILL.md` — Monday, top-50 ads scraper + rollup, APPROVED MASTER
- `00_AI_OPERATING_SYSTEM\06_KNOWLEDGE_VAULT\01_MARKET_INTELLIGENCE\WEEKLY_BRIEFS_AND_ADS_REGISTRY.md` — registry of what's copied vs. registered from the live libraries

## Tier-4 Rule (applies across this whole folder)
Anything sourced from a competitor ad library, a guru deep-dive, a "winning assets" folder, or an observed-market scrape is **Tier 4 — observed market usage.** It tells us what others are running, not what performs for REI. Never present Tier-4 material as validated. See `00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md` §5 for the full tier definitions.

## Known Gaps
- No keyword/search-intent research tool found anywhere in inventory — see `SEARCH_INTELLIGENCE.md`.
- Live performance dashboards (`REI_Creative_Intelligence_MASTER_SHEET.gsheet`, MAS HQ `01_Ad_Performance\`) are `.gsheet`/`.gdoc` — not readable from the filesystem. Flagged, not solved, by this build.
