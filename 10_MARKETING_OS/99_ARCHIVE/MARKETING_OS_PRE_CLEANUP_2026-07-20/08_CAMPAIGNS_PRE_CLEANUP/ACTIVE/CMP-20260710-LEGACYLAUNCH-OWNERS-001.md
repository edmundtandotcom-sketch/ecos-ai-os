# CMP-20260710-LEGACYLAUNCH-OWNERS-001 — Legacy Launch (Client Advisory)
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/` (AI OS master — this file is a pointer-first campaign record, not a copy)
Evidence level: 5 (creative — 16 finished ads + 10 reel scripts are rubric-scored, zero market data); registry status fields N/A (not yet launched)
Supersedes: none
Sources: `01_LL_CAMPAIGN_BRIEF_ACTIVE_v1.0.md`, `02_LL_ANGLE_MESSAGE_MATRIX_ACTIVE_v1.0.md`, `_INDEX.md` (campaign folder), `02_REEL_SCRIPTS/_INDEX.md`, `07_BRAND_AND_PROOF_BANK/03_VIDEO_AD_REGISTRY.md`, build brief §9
Next review: on launch, or when tracking/kill-scale criteria are set

---

## Status
ACTIVE. **Pilot APPROVED** (Decision 059, 2026-07-11) — Legacy Launch runs through the full Marketing OS lifecycle as the pilot: intake, tracking verification, launch-readiness gates, pre-registered kill/scale criteria, monitored launch, learning capture. See `00_COMMAND_CENTER/DECISIONS_REQUIRED.md` item 9.

**Remaining launch gates (Decision 059):**
1. Live diagnostic deploy — **DONE 2026-07-12 (live-build session).** Hosted as a Google Apps Script web app on the already-owned `admin@thereimethod.com` account (free, existing stack — no Netlify, no new vendor; honours Decision 074). Live public URL verified serving the full diagnostic HTTP 200 to anonymous visitors: `https://script.google.com/macros/s/AKfycbw_Y4jnm3cfbz0iJ2NRdG-C7Gue_5EXlBjUTW3Lc5o6yMaDPZXnXVUamxyJElAGIhyh/exec`. CONFIG baked in (calendar/booking → the new-launchfamily-legacy-ladder booking widget, GTM-KV7CRWTG, nurture → legacylaunch.com.sg interim). **FLAG:** host deviates from 074's literal "inside GHL funnel page" (GHL's funnel + workflow builders are un-automatable cross-origin iframes); Apps Script host can be iframed into a GHL page if Edmund wants it on the funnel domain — awaiting his ruling. Full state: `00_AI_OPERATING_SYSTEM\02_POSITIONING_AND_IP\01_DIAGNOSTIC_APP\GO_LIVE_RUNBOOK_v1.1.md` §0. Change log CHG-008.
2. GHL field `spl_move_result` + webhook write — **DONE & END-TO-END VERIFIED 2026-07-12.** Field created (Contact/Additional Info; was a CREATE). Webhook = Apps Script `doPost` → GHL `/contacts/upsert`. GHL Private Integration "REI Diagnostic Webhook" (View+Edit Contacts) created by Edmund; token in the `GHL_PIT` script property. **E2E test passed:** a test submission POSTed to the live webhook returned `{ok:true,status:201}` and the GHL contact was confirmed via MCP with `spl_move_result = move_4_climber_in_motion`, source "Which Move Are You On diagnostic", tags `diagnostic-which-move`/`diagnostic-completed`/`diagnostic-grade-a`, phone `+6580000001`. Test contact `HebHsn1lUkHmwJIjhVZy` ("ZZ Diagnostic E2E Test") left for Edmund to delete. Booking CTA renders the new-launchfamily-legacy-ladder widget (Next Move Strategy Session™ calendar). **Gates 1–2 CLOSED.** Change log CHG-008.

**Remaining before spend: gates 3 (tracking) + 4 (kill/scale) below.**
3. Tracking verification — confirm this campaign's UTMs/lead-form/landing-page tracking are wired end-to-end (see Tracking status below).
4. Kill/scale criteria set (see below).

**Baseline to beat:** Meta CPL **$149.58** (Decision 056 official Tier 2 baseline, `10_PERFORMANCE/HISTORICAL_BASELINE.md`).

## Engine
Client Advisory — The Second Property Ladder™. Campaign door: Legacy Launch (layer 6 of the MAS 7-layer stack).

## Objective
Property-position review for Singapore private property owners with one appreciated property and no clear next-move plan. Explicitly not a project-selling campaign (`01_LL_CAMPAIGN_BRIEF_ACTIVE_v1.0.md` §1).

## Audience
G1 — "Idle Million": mature private property owner, one valuable property, no clear plan; comfortable but uncertain whether to hold, sell, restructure, decouple, buy again, or prepare for retirement.

**C06 RESOLVED by Decision 037 (2026-07-11):** audience is **decouple-specific SI-05 (joint condo owners)** — this matches the approved Trigger Marketing Bank [LL] copy (`05_CONTENT_MARKETING_ENGINE/04_TRIGGER_MARKETING/MAS_TRIGGER_MARKETING_BANK_v1.0.md`). The broad mature-owner framing below (G1 "Idle Million") is **superseded**; the campaign brief carries a ruling banner per Decision 037 pending a full revision pass. Reconfirmed same day by Decisions 059/064 — do not reopen. See `00_COMMAND_CENTER/CONTRADICTION_REGISTER.md` C06.

## Assets
- **16 finished video ads** — `07_BRAND_AND_PROOF_BANK/03_VIDEO_AD_REGISTRY.md`. Edited Horizontal + Edited Vertical, 32 files, ~4.6 GB. Registered as CR-20260710-LL-TBD-VID-001..016 in `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv`, all Status Unlaunched, Tier 5. **URGENT per that registry's flag: these files exist in only one location and are recommended for a Drive-UI move/backup — see Decision 030 / `00_COMMAND_CENTER/DECISIONS_REQUIRED.md` item 7.**
- **10 reel scripts** — `05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/02_REEL_SCRIPTS/LL_TOF_PROBLEM_AWARE_REEL_SCRIPT_PACK_v1.0.md` (+ teleprompter version). Problem-aware TOF pack, DRAFT pending Edmund review before filming. Tier 5 — rubric-scored, zero market data.
- **Diagnostic / clarity funnel** — offer is the 1-Hour Property Position Review / Legacy Launch Clarity Consult (`01_LL_CAMPAIGN_BRIEF_ACTIVE_v1.0.md` §6); soft-CTA entry is "Comment or WhatsApp REVIEW" for a Property Position Checklist. Landing page and WhatsApp/email sequence output locations are specified in the campaign brief §8–9 but production status of those specific assets was not verified in this build pass — confirm before launch.
- **5 active angles** — ANG-001 Idle Million, ANG-002 Appreciation Is Not Progression, ANG-003 Stable Is Not Optimised, ANG-004 Owner vs Strategist, ANG-005 Review Before Options Narrow (`02_LL_ANGLE_MESSAGE_MATRIX_ACTIVE_v1.0.md` §4).

## Tracking status
**NOT verified.** The live Apps Script dashboard (`08_OPERATIONS/02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs`) and GHL pipeline exist and are LIVE code, but no confirmation was made in this build pass that this specific campaign's UTMs/lead-form/landing-page tracking are wired end-to-end. Verify before spend goes live. See `10_PERFORMANCE/DATA_SOURCES.md` and `10_PERFORMANCE/IMPORT_SPECS.md`.

## Kill / scale criteria
**TBD before launch.** No kill/scale thresholds are documented for this campaign in the source files reviewed. Set before spend begins — reference `13_MARKETING_OPERATIONS/CAMPAIGN_LIFECYCLE.md` (kill/keep/iterate/scale model) once approved, and the dashboard decision-output list in `08_OPERATIONS/01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md` §4 (keep monitoring / kill / scale / duplicate-iterate / retest / move learning / update pack).

## Message boundaries
Use: strategy before project, property position review, "appreciation is not progression," "stable is not optimised," "map your next 2–3 moves," "review before options narrow." Avoid: guaranteed profit, sure-win returns, buy-now urgency, fear countdown, blanket sell/decouple advice, project hype. (`01_LL_CAMPAIGN_BRIEF_ACTIVE_v1.0.md` §7)

## Links to AI OS masters
- Campaign brief: `05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/01_ACTIVE_FOUNDATION/01_LL_CAMPAIGN_BRIEF_ACTIVE_v1.0.md`
- Angle/message matrix: `.../02_LL_ANGLE_MESSAGE_MATRIX_ACTIVE_v1.0.md`
- Production brief: `.../03_LL_PRODUCTION_BRIEF_ACTIVE_v1.0.md`
- Video script engine: `.../06_LL_VIDEO_SCRIPT_ENGINE_ACTIVE_v1.1.md`
- YouTube Authority Engine: `.../07_GLOBAL_YOUTUBE_AUTHORITY_ENGINE_ACTIVE_v1.1.md`
- Trigger copy bank: `05_CONTENT_MARKETING_ENGINE/04_TRIGGER_MARKETING/MAS_TRIGGER_MARKETING_BANK_v1.0.md`
- Video ad registry: `07_BRAND_AND_PROOF_BANK/03_VIDEO_AD_REGISTRY.md`

## READS FROM
`05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH/`, `07_BRAND_AND_PROOF_BANK/`, `08_OPERATIONS/01_CRM_AND_TRACKING/`

## FEEDS INTO
`08_CAMPAIGNS/CAMPAIGN_REGISTRY.csv` (row CMP-20260710-LEGACYLAUNCH-OWNERS-001), `09_EXPERIMENTS/BACKLOG.md` (angle-win + C06 audience experiments), `00_COMMAND_CENTER/DECISIONS_REQUIRED.md`
