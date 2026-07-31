# META_ADS
Version: v1.0
Status: DRAFT — pending platform verification
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (playbook) — positioning/platform specs defer to sources below
Evidence level: Mixed — Tier 2 (historical spend/CPL) + Tier 5 (creative) — see Evidence Status
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM/01_E.C.O.S/04_MARKETING_ADS_DESK.md`, `07_BRAND_AND_PROOF_BANK/03_VIDEO_AD_REGISTRY.md`, `05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/`, `04_AGENT_EDITION_OS/02_MARKETING/MAS_Campaign_Brief_MM_ValidationTest_v1.0_DRAFT.md`, build brief §5
Next review: on next Meta campaign brief or platform policy check

## Strategic role
Client Advisory (Second Property Ladder™): primary paid channel for the Legacy Launch campaign door — the only active client-engine door (Family Legacy and Mash-up doors RETIRED per Decisions 058/063). Agent Edition (Market Maker Method): validation-test campaign uses Meta cold + retargeting per the DRAFT MM validation brief. Both engines run on Meta — never blend engine language in one ad set.

## Best use cases
Cold-traffic image/video against a named belief block (e.g. G1 "Idle Million"); retargeting warm viewers of reels/YouTube; custom audiences from scorecard/diagnostic completers (Agent Edition); lookalikes from past leads once GHL import is executed (not yet — see CRM_NURTURE.md).

## Required inputs
Campaign brief (Desk 04 SOP); a belief block from the Trigger Marketing Bank tagged `[LL]`/`[FL]`/`[M]`/`[U]`; a proof asset from Case Study Bank / Proof Registry; creative from the Video Ad Registry (16 finished Legacy Launch ads, Tier 5, status Unlaunched) or Image Prompt Engine; currently-verified Meta specs (not verified in this build).

## Process
1. Read Command Center + positioning spine + Trigger Marketing Bank (Desk 04 SOP).
2. Fix objective, audience, and campaign door.
3. Pull matching proof asset.
4. Draft copy tied to belief block + a Ladder Move (Decision 055: "Move" is the locked public term).
5. Verify current Meta specs before finalising; if unverified, label `DRAFT — pending platform verification`.
6. Launch; track via CRM/Dashboard system (`08_OPERATIONS/01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md`).
7. Review vs KPIs; recommend keep/kill/scale.

## Outputs
Campaign brief, ad copy sets, creative selection — saved to the relevant campaign folder under `05_CONTENT_MARKETING_ENGINE/` (not inside Marketing OS). Marketing OS registries (`08_CAMPAIGNS/`, `07_CREATIVE_LIBRARY/`) reference, never duplicate.

## KPIs
Define: CPL, cost/responded lead, CTR, hook rate, CPA to appointment. **No live KPI baseline exists in Marketing OS.** Only baseline: Tier-2 historical aggregate (brief §5) — past-30-days blended paid **$13,519 spend · 88 leads · 35 responded · $153.62 CPL · $386.26 cost/responded lead**, Meta+Google blended (no Meta-only breakout confirmed), named campaigns incl. "9 May-Retargeting Video-Why I Do What I Do", "24 April-Form | Legacy Launch NL". Source: `lead_list_analysis_source_latest.xlsx` / `lead_summary_*.json`, data through 2026-06-24. No Tier 1 (lead→client/revenue) data exists.

## Common failure modes
Generic property ads not tied to a belief block; blending Client Advisory and Agent Edition language in one ad; asserting Meta specs from memory (violates AI OS Platform Verification Rule); skipping the proof-asset requirement; test design with more than one variable.

## Integration with other channels
Feeds RETARGETING.md (video-view custom audiences), CRM_NURTURE.md (lead handoff via GHL), FUNNELS_LANDING.md (destination), 07_CREATIVE_LIBRARY (asset source). Shares audience/creative learnings with GOOGLE_ADS.md and YOUTUBE.md (cut-down source).

## Evidence status
Creative = **Tier 5** (16 finished Legacy Launch ads, rubric-scored, zero market data, angle mapping pending). Historical spend/CPL = **Tier 2** (archived, aggregate, PII-stripped). **No Tier 1.** Current live Meta account performance is not readable from this workspace — `REI_Creative_Intelligence_MASTER_SHEET.gsheet` and the MAS HQ ad-performance folder are `.gsheet`/`.gdoc`, inaccessible from the filesystem.

## Known gaps
No current in-system Meta campaign structure registry; specs unverified; 16 finished ads not yet launched and not yet Drive-moved off the legacy raw-footage path (URGENT flag in the Video Ad Registry); no Meta-only CPL breakout in the one available aggregate.
