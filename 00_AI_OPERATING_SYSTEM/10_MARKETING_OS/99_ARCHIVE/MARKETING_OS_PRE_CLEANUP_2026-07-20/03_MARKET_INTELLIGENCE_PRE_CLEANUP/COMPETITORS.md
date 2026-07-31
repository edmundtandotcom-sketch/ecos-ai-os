# COMPETITORS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\01_BUSINESS_POSITIONING.md` (threat assessment) + `08_OPERATIONS\03_AUTOMATIONS\singapore-property-ads-brief_SKILL.md` (live scraper) + `01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Ads\` (research library)
Evidence level: Tier 4 (observed market/competitor activity, not REI performance data)
Supersedes: none
Sources: files above
Next review: next weekly ads brief cycle

---

## The Named Threat
**PropertyLimBrothers (PLB)** is the primary named rival. Per `01_BUSINESS_POSITIONING.md`: sophisticated operator — named frameworks, registered "Disparity Effect®," 12,000+ community, own conventions. Category-creation potential for The Second Property Ladder™ scored 74/100 (June 2026), but **category naming / public ownership scored only 10/20 — AT RISK.** The window to publicly own the Ladder category is shorter than it looks; this is a live strategic priority, not a someday task. Full detail: `00_COMMAND_CENTER\01_BUSINESS_POSITIONING.md`.

## Live Competitor-Intelligence Automation
`singapore-property-ads-brief` (Monday, scheduled, APPROVED MASTER) pulls the real top-50 Singapore property ads weekly from Meta Ads Library + Google Ads + YouTube via Chrome extension — no synthesis fallback. Each ad is scored 0–10 (reach, engagement, creative quality, psych trigger, sustainability) and logged with advertiser, headline, copy, format, psychological trigger, and destination. Output includes a **Competitor Highlights** section (who dominated the top 50, dominant angles, positioning) every run. Source: `08_OPERATIONS\03_AUTOMATIONS\singapore-property-ads-brief_SKILL.md`.

## Weekly Ads Research Library
Location: `01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Ads\REI_Ads_Research_Resources\`. Live, actively-maintained, unmigrated into the AI OS. Actual structure on disk (verified by listing, not skimmed from a description): **11 folders**, not the 10 this build brief described — `AdFormats`, `CompetitorIntel`, `BeliefBlockPlaybook`, `EvergreenAngles`, `PsychTriggerPatterns`, `CreatorPatterns`, `CopyPatternLibrary`, `ContentGapMap`, `CaseStudyRegistry`, `SOURCE_REGISTRY`, `ARCHIVE` — plus a still-unresolved `INDEX.md` / `INDEX (1).md` / cloud-only `INDEX v1.2` triplicate. Weekly briefs run through 2026-07-06. `CompetitorIntel` is the section directly tracking advertiser frequency and positioning shifts week over week.

## Governance Note
This library is flagged in `06_KNOWLEDGE_VAULT\01_MARKET_INTELLIGENCE\WEEKLY_BRIEFS_AND_ADS_REGISTRY.md` as its own future migration — either promoted into `06_KNOWLEDGE_VAULT` or kept as a specialised ads-desk working library. Not migrated by this build; referenced only.

## What This File Does Not Claim
No named competitor besides PLB has a documented threat assessment in the workspace. The weekly scraper surfaces "who dominated the top 50" by ad volume/score, which is a different thing from a competitor's actual market share, CAC, or client outcomes — none of that is available anywhere in this workspace (Tier 1/2 gap, per brief §5).

## Use Rule
Competitor activity is directional signal for angle/format gaps, not proof of what to copy. Cross-reference with `AD_LIBRARY.md` Tier-4 rule before pulling any competitor pattern into a brief.
