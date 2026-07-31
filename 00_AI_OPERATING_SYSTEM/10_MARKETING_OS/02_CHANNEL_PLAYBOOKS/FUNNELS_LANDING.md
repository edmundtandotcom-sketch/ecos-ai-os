# FUNNELS_LANDING
Version: v1.0
Status: DRAFT — pending platform verification
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (playbook) — landing formula skeleton defers to source below (STALE)
Evidence level: N/A (live builds exist, untested) / Tier 4 (landing formula, STALE C05)
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM/02_POSITIONING_AND_IP/01_DIAGNOSTIC_APP/`, `04_AGENT_EDITION_OS/02_MARKETING/MAS_AgentCommand_Scorecard_v3.html`, `MAS_Workshop_LandingPage_v2.html`, `MAS_MARKETING_INTELLIGENCE_OS_v1.md` §6 (STALE, C05), `01_CAMPAIGN_LEGACY_LAUNCH/01_ACTIVE_FOUNDATION/01_LL_CAMPAIGN_BRIEF_ACTIVE_v1.0.md`
Next review: on next funnel build, or when C05 landing formula is re-verified against locked positioning

## Strategic role
Client Advisory: the "Which Move Are You On?" gamified diagnostic (renamed per Decision 055) (live `index.html` build) is the lead-gen qualifying tool; the Legacy Launch brief lists a landing page as an output priority (existence/completion of that specific file was not confirmed in this build's search). Agent Edition: Market Maker Scorecard → S$297 Preview → Workshop landing page (`MAS_Workshop_LandingPage_v2.html`) is the full, LOCKED-positioning offer-ladder funnel.

## Best use cases
Diagnostic/scorecard as a top-of-funnel qualifying lead magnet (both engines); long-form landing page for consult/event booking; the 16-section MAS landing formula as a reusable **structural skeleton only** (STALE C05 — verify any copy against locked positioning before reuse).

## Required inputs
The diagnostic's build spec (`Which_Step_Are_You_On_Diagnostic.md`, per the Diagnostic App index); offer/CTA per engine; proof assets; the 16-section skeleton (urgency bar → nav → hero → proof strip → problem → agitation → mechanism → proof → who it's for/not for → offer stack → price+anchor → guarantee → income-gap visual → FAQ → final CTA → sticky bar) as a starting structure only, not verified copy.

## Process
Define the funnel step (magnet → landing → booking) → pull proof/offer per engine → build/adapt page (single-file React/HTML per the diagnostic-app precedent) → verify current hosting/tracking platform specs → deploy → connect pixel/CRM handoff (pixel/tracking setup sits with the Operations Desk, out of this desk's scope) → run a CRO loop (currently absent).

## Outputs
Landing page HTML/build, deploy notes. The diagnostic app and Workshop Landing Page v2 already exist as live builds — this playbook references, does not duplicate them.

## KPIs
Define: funnel completion rate, magnet-to-lead rate, landing page conversion rate, page load time (<2s per the unverified stale skeleton), mobile completion rate. **No live baseline exists in Marketing OS.**

## Common failure modes
Reusing STALE C05 copy without re-verifying against the locked Market Maker Method or Second Property Ladder spine; skipping the "who it's for / not for" filter section; revealing price before value is established; running more than one funnel per campaign (a real learning already flagged in inventory).

## Integration with other channels
Receives traffic from every paid/organic channel; hands off to CRM_NURTURE.md on completion; WEBINAR.md / VSL.md / EVENTS_WORKSHOPS.md sit downstream in the offer ladder; 07_CREATIVE_LIBRARY supplies visual assets.

## Evidence status
Diagnostic app and both HTML landing pages = **live builds** (exist; Tier N/A as unmeasured product). 16-section formula = **Tier 4 at best** (observed pattern, STALE C05, unverified against current platform or positioning). No conversion-rate data of any tier found for any live funnel asset.

## Known gaps
No CRO/testing loop exists; the MAS landing formula is built on retired branding (C05) and needs a re-verified version before Agent Edition reuse; the Client Advisory landing page (the LL brief's `03_LANDING_PAGE` output lane) was not located as a completed file in this build's search.
