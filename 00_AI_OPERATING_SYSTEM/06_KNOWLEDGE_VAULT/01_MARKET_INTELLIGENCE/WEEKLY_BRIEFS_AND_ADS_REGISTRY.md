Title: Weekly Content Briefs and Weekly Ads Briefs — Registry
Version: v1.0
Status: REGISTRY
Date: 2026-07-10
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Contents\`, `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Ads\`

## What was copied vs. registered

The build spec calls for copying the market intelligence framework plus the 5 most recent weekly briefs, registering the rest. The 5 copied into this folder (all dated 2026-07-06, the most recent batch) are:

1. `[WEEK] REI Weekly Brief — 2026-07-06.md`
2. `[ROLLUP] REI Bi-weekly Insights — 2026-07-06.md`
3. `[LIBRARY] CCR Reversal & Regional Rotation_2026-07-06.md`
4. `[LIBRARY] Condo Dip vs Downturn (Non-Landed -0.1%)_2026-07-06.md`
5. `[LIBRARY] Global Uncertainty & Structured Positioning H2 2026_2026-07-06.md`

**Interpretation note for QA:** "5 most recent" was read as the 5 most recent by date across the whole folder (not just the `[WEEK]` series, of which there are only 3 .md instances total). This pulled in the 2026-07-06 `[ROLLUP]` and two `[LIBRARY]` topic write-ups alongside the dated weekly brief. If Edmund wants a different 5 (e.g. only `[WEEK]` + `[ROLLUP]` series), swap files from the list below.

## Weekly Contents — registered (not copied)

Folder: `03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Contents\`

| File | Date | Type |
|---|---|---|
| `[LIBRARY] HDB K-Shape & MOP Wave 2026_2026-07-06.md` | 2026-07-06 | Library topic write-up |
| `[LIBRARY] Rate Floor & SORA Turn 2026_2026-07-06.md` | 2026-07-06 | Library topic write-up |
| `[EXECUTION LOG] Weekly Brief — 2026-06-29.md` | 2026-06-29 | Execution log |
| `[LIBRARY] 2026 New Precinct Play (Bayshore, Tengah, Dunearn)_2026-06-29.md` | 2026-06-29 | Library topic write-up |
| `[LIBRARY] Accessibility Reset & Market Cooling_2026-06-29.md` | 2026-06-29 | Library topic write-up |
| `[LIBRARY] HDB MOP Wave & Upgrader Timing_2026-06-29.md` | 2026-06-29 | Library topic write-up |
| `[LIBRARY] Mortgage Rate Timing & Refinance ROI Strategy_2026-06-29.md` | 2026-06-29 | Library topic write-up |
| `[LIBRARY] OCR Resale Rebound & Suburban Outperformance_2026-06-29.md` | 2026-06-29 | Library topic write-up |
| `[WEEK] REI Weekly Brief — 2026-06-29.md` | 2026-06-29 | Weekly brief |
| `[WEEK] REI Weekly Brief — 2026-06-20.md` | 2026-06-20 | Weekly brief |
| `[WEEK] REI Weekly Brief — 2026-06-22.gdoc` | 2026-06-22 | Weekly brief (cloud-only, gdoc pointer) |
| `REI_Content_Research_Resources\` (subfolder, 6 items) | — | Supporting research resources for the weekly content brief pipeline |

## Weekly Ads — registered (not copied)

Folder: `03_SHARED_PROPERTY_ASSETS\03_SHARED_RESEARCH\Weekly Ads\`

Mostly Google Doc pointers (cloud-only) plus one live automation reference structure:

| Item | Type |
|---|---|
| `SCHEDULED_TASK_singapore-property-ads-brief_v1.0.md` | Scheduled task definition (references `08_OPERATIONS/03_AUTOMATIONS` skill — see B7) |
| `SCHEDULED_TASK_singapore-property-ads-rollup_v1.0.md` | Scheduled task definition |
| `REI_Ads_Research_Resources\` (subfolder) | Structured reference library: `AdFormats`, `CompetitorIntel`, `BeliefBlockPlaybook`, `EvergreenAngles`, `PsychTriggerPatterns`, `CreatorPatterns`, `CopyPatternLibrary`, `ContentGapMap`, `CaseStudyRegistry`, `SOURCE_REGISTRY`, `ARCHIVE`, plus `INDEX.md` (note: a duplicate `INDEX (1).md` and a newer `INDEX v1.2 — REPLACE OLD INDEX (W02 logged).gdoc` also exist — the "(1)" duplicate is exactly the naming-confusion pattern the AI OS rebuild is meant to eliminate; QA should resolve which INDEX is authoritative before this subfolder is ever promoted) |
| `Rollup Summaries\` (4 gdocs) | Weekly ads rollup/digest, all cloud-only |
| `2026-06-22 REI Ads Brief`, `[2026-06-20] REI Ads Brief — Week of 20 June 2026` (folders) | Dated weekly ads brief working folders |
| `[2026-06-21]`, `[2026-06-22]`, `[2026-07-06]` REI Ads Brief/Library gdocs | Cloud-only weekly ads briefs and source registry updates |

## Why registered, not copied

Global build rule 1 (md-only) rules out the .gdoc pointers — they are not real files, just cloud stubs. The `REI_Ads_Research_Resources` subfolder is a live, actively-maintained reference library in its own right (11 categories) — copying it wholesale would exceed this build's scope (the spec calls for registering "the rest" of weekly briefs/ads, not migrating a second knowledge system). It is flagged here for a future dedicated migration pass, likely owned by the same desk that runs `singapore-property-ads-brief` (see `08_OPERATIONS/03_AUTOMATIONS`, Builder B7).

## Migration recommendation

1. Weekly Contents/Ads folders should get a rolling "copy latest N, archive older" rule going forward rather than a one-time migration — recommend this become a line item in `00_COMMAND_CENTER/09_AUDIT_AND_MAINTENANCE.md`.
2. `REI_Ads_Research_Resources` deserves its own future evaluation: either promote into `06_KNOWLEDGE_VAULT` as a fifth subfolder, or keep it as a specialized ads-desk working library outside the AI OS. Do not migrate piecemeal.
3. Resolve the `INDEX.md` / `INDEX (1).md` / `INDEX v1.2 (gdoc)` triplicate before any future copy.

## Status

REGISTRY — no physical move performed by this build.

## Sync check — 2026-07-13

Compared newest Weekly Contents/Ads files against this folder as part of the workspace rescue pass (see `00_RESCUE_NOTE` context in `08_OPERATIONS`).

**Weekly Contents — gap found and closed.** The 2026-07-13 batch (this week's brief) was not yet in the AI OS. Copied in:
- `[WEEK] REI Weekly Brief — 2026-07-13.md`
- `[ROLLUP] REI Bi-weekly Insights — 2026-07-13.md`
- `[LIBRARY] Decoupling Without the Clawback (SI-05)_2026-07-13.md`
- `[LIBRARY] July Launch Squeeze — Dunearn House & Lentor Gardens_2026-07-13.md`
- `[LIBRARY] Landed Market Pause vs Reversal_2026-07-13.md`
- `[LIBRARY] October BTO Wave & Upgrader Exit Timing_2026-07-13.md`
- `[LIBRARY] SORA Floor & HDB Loan Gap 2026_2026-07-13.md`

Also backfilled 2 items from the 2026-07-06 batch that this registry had previously flagged as registered-but-not-copied (see the original table above — still accurate as a historical record of that decision, now superseded for these 2 files only):
- `[LIBRARY] HDB K-Shape & MOP Wave 2026_2026-07-06.md`
- `[LIBRARY] Rate Floor & SORA Turn 2026_2026-07-06.md`

All 9 files verified copied (byte-identical source folder copy, no transformation).

**Weekly Ads — still nothing to copy.** Checked both July items (`[2026-07-06] REI Ads Brief… (W04)`, `[2026-07-13] REI Ads Brief… (W05)`) — both remain cloud-only `.gdoc` pointer files (same failure mode as any Drive shortcut: `Invalid request code` on read, not real local content). No change to the Weekly Ads section of this registry; still fully cloud-only, still registered-not-copied. If Edmund wants the actual W04/W05 ads brief content in the AI OS, it needs a Google Docs export pass, not a file copy.

**Remaining registered-not-copied 2026-06-29/06-22/06-20 items are unchanged** — this sync pass only addressed the "recent (July 2026)" scope named in the rescue task; older items are still correctly registry-only per the original migration recommendation above.
