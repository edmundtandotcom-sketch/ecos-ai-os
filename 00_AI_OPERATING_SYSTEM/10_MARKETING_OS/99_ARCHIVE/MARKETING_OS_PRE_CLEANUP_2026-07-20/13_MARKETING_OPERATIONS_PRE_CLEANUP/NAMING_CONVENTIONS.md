# NAMING CONVENTIONS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (Marketing OS IDs); LL- scheme stays owned by 05_CONTENT_MARKETING_ENGINE/01_CAMPAIGN_LEGACY_LAUNCH
Evidence level: N/A — operating convention, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §8 (13_MARKETING_OPERATIONS); 01_ACTIVE_FOUNDATION/06_LL_VIDEO_SCRIPT_ENGINE_ACTIVE_v1.1.md §15; 01_ACTIVE_FOUNDATION/04_LL_CONCEPT_BATCH_MAP_ACTIVE_v1.0.md §6–8
Next review: when the first non-Legacy-Launch campaign is built (Market Maker validation campaign)

## 1. Marketing OS ID formats (new — this system only)

| Prefix | Object | Format | Example |
|---|---|---|---|
| CMP- | Campaign | `CMP-YYYYMMDD-OFFER-AUDIENCE-SEQ` | `CMP-20260710-LEGACYLAUNCH-OWNERS-001` |
| ANG- | Angle | `ANG-[DOOR/CONCEPT-BATCH]-[ANGLE-SLUG]-SEQ` | `ANG-CB002-IDLEMILLION-01` |
| CR- | Creative asset (registry row) | `CR-YYYYMMDD-[DOOR]-[CONCEPT]-[FORMAT]-SEQ` | `CR-20260710-LL-TBD-VID-001` |
| CP- | Copy variant (headline/body/CTA text) | `CP-[PARENT CR- or CMP-]-[FRAMEWORK CODE]-SEQ` | `CP-CR001-COPYF03-01` |
| FUN- | Funnel | `FUN-YYYYMMDD-[DOOR]-[STAGE]-SEQ` | `FUN-20260710-LEGACYLAUNCH-DIAG-001` |
| EXP- | Experiment | `EXP-YYYYMMDD-[VARIABLE-SLUG]-SEQ` | `EXP-20260711-HOOKANGLE-001` |

SEQ = 3-digit sequence, zero-padded, resets per parent object. Dates = campaign start date where known, else record-creation date.

## 2. Legacy Launch (LL-) scheme — reference only, do not replace

Two LL- formats coexist inside `01_CAMPAIGN_LEGACY_LAUNCH` (read there for full rules):
- **Concept Batch Tracking ID:** `LL-[CB###]-[LLS##]-[TYPE]-[PATTERN]-V##` (TYPE = IMG/VID/WA). Source: `04_LL_CONCEPT_BATCH_MAP_ACTIVE_v1.0.md` §8.
- **Video Modular Asset ID:** Hook `LL-[CB]-[SITUATION]-H-[HOOKTYPE]-H[#]`; Body `LL-[STAGE]-[CB]-[SITUATION]-B-[PATTERN]-[DURATION]-V[#]`; CTA `LL-CTA-[TEMPERATURE]-[#]`; Final `LL-[CB]-[SITUATION]-VID-[BODY_PATTERN]-[DURATION]-V[#]-H[#]-CTA[#]`. Source: `06_LL_VIDEO_SCRIPT_ENGINE_ACTIVE_v1.1.md` §15.

Note: the build brief's shorthand `LL_[STAGE]_[GCODE]_[CONCEPT]_[ANGLE]_[PATTERN]_[DURATION]_V##` is an approximation of the above; the two formats actually in use are documented verbatim here.

## 3. Mapping rule (mandatory)

LL- IDs are the production/editorial IDs and never change. CR- rows in `07_CREATIVE_LIBRARY/CREATIVE_REGISTRY.csv` carry a `LegacyAssetID` field that stores the matching LL- ID(s). CMP- campaign records reference LL- campaign folders by path, not by renaming them. Marketing OS IDs **wrap**; they never rename, move, or replace an LL- asset.

## 4. Rules
- IDs are permanent once assigned. A killed/superseded asset keeps its ID; status changes instead (see CAMPAIGN_LIFECYCLE.md).
- One ID per object. Never reuse a SEQ after a kill.
- Slugs: uppercase, no spaces, hyphen-separated, ≤12 characters.
- Engine is never encoded in the ID string (avoids leaking engine into filenames if shared externally) — engine is a registry field.
