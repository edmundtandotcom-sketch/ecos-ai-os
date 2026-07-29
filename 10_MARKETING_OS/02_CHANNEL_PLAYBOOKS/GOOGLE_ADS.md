# GOOGLE_ADS
Version: v1.0
Status: DRAFT — pending platform verification
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (playbook) — positioning/platform specs defer to sources below
Evidence level: Mixed — Tier 2 (historical blended aggregate) + N/A (current account) — see Evidence Status
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM/08_OPERATIONS/02_SCRIPTS/REI_GoogleAds_Script_ACTIVE_v8.gs`, `01_E.C.O.S/04_MARKETING_ADS_DESK.md`, `04_AGENT_EDITION_OS/02_MARKETING/MAS_MARKETING_INTELLIGENCE_OS_v1.md` (STALE, C05), build brief §5
Next review: on next Google Ads campaign brief or when Master Sheet access is restored

## Strategic role
Client Advisory: search-intent capture complementing Meta's interrupt-based cold reach; "Hook Vsl1–7" campaign names appear in historical lead data, implying an active VSL-fed search funnel (see VSL.md — source script not located). Agent Edition: no confirmed Google Ads usage in inventory — Market Maker channel mix documented centers on Meta/YouTube; treat Google as unconfirmed for this engine.

## Best use cases
High-intent search queries tied to property-decision moments (Client Advisory); VSL-fed landing traffic where "Hook VslN" naming was historically used. Not yet evidenced for Agent Edition.

## Required inputs
`REI_GoogleAds_Script_ACTIVE_v8.gs` (account-level script; syncs Google_Campaigns_Today/Yesterday/L7D/L14D/L30D/AllTime/Daily, Google_AdGroups, Google_Ads tabs to the Master Sheet daily) as reference for what data structure exists; campaign brief; keyword/search-intent research (none found — gap); currently-verified Google Ads specs (30-char×3 headlines / 90-char×2 descriptions per the STALE MAS skeleton — re-verify, do not assert as current).

## Process
1. Keyword research → ad group structure (none found in workspace; build fresh).
2. Draft responsive search ad copy tied to a named belief block.
3. Ensure landing page matches ad intent (quality score impact).
4. Verify current Google Ads specs before finalising; if unverified, label `DRAFT — pending platform verification`.
5. Launch; the account-level script pushes daily data to the Master Sheet.
6. Weekly read against KPIs; keep/kill/scale.

## Outputs
Campaign brief + ad copy saved to the relevant campaign folder. Script output tabs live in the REI Creative Intelligence Master Sheet — a `.gsheet`, not filesystem-readable from this workspace.

## KPIs
Define: CPL, CPA, quality score, impression share, search term relevance rate. Baseline: same Tier-2 blended paid aggregate as META_ADS.md ($153.62 CPL, Meta+Google blended, brief §5); "Hook Vsl1–7" campaign names appear in the historical lead data but this Marketing OS has **no Google-only CPL breakout** — flag as a gap, not an assumption.

## Common failure modes
Unfiltered search terms wasting spend on irrelevant or agent-recruitment-style queries; landing page mismatch tanking quality score; no negative-keyword discipline; asserting current Google Ads UI/policy from memory.

## Integration with other channels
Script output is the intended data source for 10_PERFORMANCE (currently inaccessible — flagged). FUNNELS_LANDING.md is the conversion destination. Shares creative learnings with META_ADS.md. CRM_NURTURE.md receives resulting leads.

## Evidence status
The script itself is **LIVE code** (exists, functioning per its own header). Its **output** (current spend/CPL) is not verifiable from this workspace — **Tier N/A** for current performance. **Tier 2** only for the one historical archived aggregate. Keyword strategy has **no evidence found** (gap).

## Known gaps
No current campaign structure documented in Marketing OS; no keyword research library found; no read access to the live Google Ads account or Master Sheet in this build; "Hook Vsl1–7" naming's originating brief/script not located — meaning unconfirmed beyond the campaign-name reference in the archived lead data.
