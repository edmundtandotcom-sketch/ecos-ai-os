# 06_CHANNEL_PLAYBOOKS — _INDEX
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A (index)
Supersedes: none
Sources: the 17 playbook files in this folder
Next review: whenever a playbook is added, retired, or materially revised

## Purpose
One operating playbook per marketing channel — strategic role (by engine), best use, required inputs, process, outputs, KPIs, common failure modes, cross-channel integration, evidence status, and known gaps. Every playbook is `DRAFT — pending platform verification` for any platform-specific content and states which of the two engines (Client Advisory / Agent Edition) it serves. These are original operating documents, not pointers — they cite and defer to AI OS masters for positioning, frameworks, and process detail rather than duplicating them.

## Files

| File | One-line purpose | Engine(s) |
|---|---|---|
| `META_ADS.md` | Meta paid: cold + custom-audience campaigns, belief-block-led copy, creative sourcing | Both |
| `GOOGLE_ADS.md` | Google Ads: search-intent capture, account-level reporting script, "Hook Vsl" history | Client Advisory (confirmed); Agent Edition (unconfirmed) |
| `YOUTUBE.md` | Long-form authority production system — the content mother-asset engine | Client Advisory (confirmed); Agent Edition (unconfirmed) |
| `ORGANIC_SOCIAL.md` | Reel production rules, hook-swappable system, TOF script packs | Client Advisory; Agent Edition (event-only Content Studio) |
| `SEO_AEO.md` | Search / AI-answer-engine visibility — no assets found, v1 scope only | Client Advisory (n/a for Agent Edition) |
| `GOOGLE_BUSINESS_PROFILE.md` | Local trust/proof signal — no listing/data found, v1 scope only | Client Advisory (n/a for Agent Edition) |
| `EMAIL.md` | Nurture/reactivation email backbone + campaign email leg | Both |
| `WHATSAPP.md` | Fast-response, keyword-triggered, trigger-based follow-up | Both |
| `SMS.md` | Fallback reminder channel — near-zero evidence, v1 scope only | Both (unconfirmed) |
| `FUNNELS_LANDING.md` | Diagnostic/scorecard + landing pages, the 16-section MAS formula skeleton | Both |
| `VSL.md` | Video sales letter — historical "Hook Vsl1–7" naming, source script not located | Client Advisory (confirmed); Agent Edition (via YouTube engine only) |
| `WEBINAR.md` | Family Legacy webinar format — RETIRED upstream door (Decisions 058/063; C11 resolved-retired), reference only | Client Advisory (n/a for Agent Edition) |
| `RETARGETING.md` | Warm-audience re-engagement across Meta/Google/YouTube | Both |
| `CRM_NURTURE.md` | Readiness-tier follow-up, trigger monitoring, GHL pipeline discipline | Both |
| `REFERRAL.md` | Client-development referral trigger — no program built, v1 scope only | Client Advisory (confirmed reference); Agent Edition (unconfirmed) |
| `PARTNERSHIPS.md` | B2B2C co-marketing — no program found, v1 scope only | Both (unconfirmed) |
| `EVENTS_WORKSHOPS.md` | Market Maker Live 3-Day + S$297 Preview run-of-show | Agent Edition (n/a for Client Advisory) |

## Evidence summary (see build brief §5 for full tier definitions)
Only two channels carry any Tier 1/2 evidence, and only partially: META_ADS.md and GOOGLE_ADS.md share one blended Tier-2 historical aggregate ($153.62 CPL, brief §5) with no per-platform breakout; VSL.md and RETARGETING.md each cite one named historical campaign inside that same blended aggregate with no channel-specific breakout. Every other channel is Tier 4/5 or N/A. **No channel in this folder has Tier 1 (verified commercial outcome) evidence.**

## READS FROM
`01_E.C.O.S/04_MARKETING_ADS_DESK.md` (SOP) · `05_CONTENT_MARKETING_ENGINE/` (campaign briefs, frameworks, Trigger Marketing Bank) · `04_AGENT_EDITION_OS/` (Market Maker positioning, workshop, marketing skeleton) · `08_OPERATIONS/01_CRM_AND_TRACKING/` (CRM/nurture systems) · `07_BRAND_AND_PROOF_BANK/` (creative/proof registries) — all under `00_AI_OPERATING_SYSTEM/`.

## FEEDS INTO
`../08_CAMPAIGNS/` (campaign records cite the relevant playbook per channel used) · `../07_CREATIVE_LIBRARY/` (creative sourcing rules) · `../05_FRAMEWORK_LIBRARY/` (process cross-reference) · `../10_PERFORMANCE/` (KPI definitions) · `../13_MARKETING_OPERATIONS/QA_CHECKLISTS.md` (channel-specific launch gates, when built).

## Known cross-cutting gaps
No channel has a live, filesystem-readable performance dashboard (`REI_Creative_Intelligence_MASTER_SHEET.gsheet` and the MAS HQ ad-performance folder are inaccessible `.gsheet`/`.gdoc`). GHL contact import (17,663 unique / 7,272 eligible) is not executed, blocking CRM_NURTURE.md, EMAIL.md, and WHATSAPP.md from being measured at scale. SEO_AEO, GOOGLE_BUSINESS_PROFILE, SMS, REFERRAL, and PARTNERSHIPS are genuine ground-zero gaps — no assets or evidence found, not just unmigrated content.
