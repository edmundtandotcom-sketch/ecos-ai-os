Version: v1.4
Status: APPROVED MASTER
Date: 2026-07-14
Supersedes: v1.3 (2026-07-11) — **Decision 090 cleanup:** the curated media that used to live in this branch (`07_BRAND_PACK\`, `08_PROOF_BANK\`, `06_VIDEO_ADS_MASTER\`) has been relocated to the single home `01_ASSET_LIBRARY\`. This branch is now a **pointer index only** — no binary media.
Sources: `H:\Shared drives\00_E.C.O.S\X-Singapore Real Estate Insider - MAS HQ\05_ASSET_BANK\`, `...\02_CLIENTS\Keep\`, `...\04_CONTENT_ADS_ENGINE\01_CAMPAIGN_LEGACY_LAUNCH\03_Video\`

---

# 07_BRAND_AND_PROOF_BANK — INDEX

> ⚠️ **FILES RELOCATED — 2026-07-14 (Decision 090).** Every real photo, logo, testimonial, and video that this branch used to hold now lives **once**, in **`01_ASSET_LIBRARY\`** (the single home — one file, one place). This folder is now a **pointer/registry index only**: use it to know *what proof/brand assets exist and why they matter*, then open `01_ASSET_LIBRARY\` to get the actual file. The 516 exact duplicates were moved to `_DEL\07_brand_proof_duplicates_2026-07-14\` pending final deletion; 46 curated originals were promoted into the Library.
>
> **Where the files went:** logos & brand specs → `01_ASSET_LIBRARY\03_BRAND_ASSETS\` · founder/team headshots → `01_ASSET_LIBRARY\01_PHOTOS\` · testimonials & proof → `01_ASSET_LIBRARY\02_TESTIMONIALS_PROOF\` · video ads → `01_ASSET_LIBRARY\04_VIDEO_ADS\`.

## Purpose

This branch is now a **pointer index**, not a media store. The `*_REGISTRY.md` files below remain useful as a *catalogue* of what brand/proof material exists (exact counts, date ranges, why it matters) — but the files themselves live in `01_ASSET_LIBRARY\`, per the "one file, one home" rule (Operating Agreement rule 37).

**History:** curated working sets were previously COPIED here (`06_VIDEO_ADS_MASTER\`, `07_BRAND_PACK\`, `08_PROOF_BANK\` — Decisions 034/035/060). The 2026-07-14 spring-clean consolidated those into the Asset Library so nothing is duplicated across two homes.

## Files

| File | Indexes | Files counted | Priority |
|---|---|---|---|
| `01_BRAND_ASSETS_REGISTRY.md` | Design/brand guides + winning marketing assets | 180 | Medium — winning ads high-value, logos need curation |
| `02_PROOF_REGISTRY.md` | Testimonials, case studies, credibility, hot seats, CNY lunch, Full Testimonials video | 523 | Medium — small curated folders high-value, CNY lunch needs culling |
| `03_VIDEO_AD_REGISTRY.md` | Finished Legacy Launch video ads — working master in `06_VIDEO_ADS_MASTER\01_LEGACY_LAUNCH\`, originals intact in MAS HQ | 32 | Resolved 2026-07-11 — two copies exist |
| `04_SALES_DECKS_REGISTRY.md` | Developer project sales decks/kits | 960 | Low — replaceable from developer portals |
| `05_PHOTO_VIDEO_LIBRARY_REGISTRY.md` | Team/event/founder photos + hero/campaign/animated video | 3,563 | Low-Medium — needs curation pass, placeholder dates on two subfolders |
| `07_PROOF_BANK_SHORTLIST.md` | Proof bank curation rationale + category mapping (approved 2026-07-11, Decision 034) | — | Done — reference |
| `06_BRAND_PACK_SHORTLIST.md` | Brand pack curation rationale + exclusion list (approved 2026-07-11, Decision 035) | — | Done — reference |
| `BRAND_PACK_INDEX.md` (pointer) | Catalogue of the curated brand pack: logos, brand-spec PDFs, headshots | files RELOCATED | **→ pull from `01_ASSET_LIBRARY\03_BRAND_ASSETS\` + `01_PHOTOS\`** |
| `PROOF_BANK_INDEX.md` (pointer) | Catalogue of the proof/testimonial bank: 7-category shelves, founder cases, event sets | files RELOCATED | **→ pull from `01_ASSET_LIBRARY\02_TESTIMONIALS_PROOF\`** |

**Total indexed across this branch: 5,258 files, roughly 121 GB** (plus the copied working sets under the approved exceptions: 28-file brand pack + 502-file proof bank).

## GAP — ~~flag for Edmund~~ RESOLVED 2026-07-11 (Decision 035)

~~No centralized, curated logo or headshot pack exists.~~ **Resolved:** `07_BRAND_PACK\` now holds the curated 28-file set — "the" logo and "the" headshots can be handed to any designer or partner with confidence. Remaining sub-gaps (queued): no Second Property Ladder™ mark exists yet; no white/transparent variant of the R.E.I. Method marks (regenerate from `LOGO_SOURCE_VECTOR.ai`); Edmund needs a current solo photoshoot (newest clean asset 2022 vs Cindior's Feb 2025 set).

## Priority order for physical migration (Drive UI, later)

1. ~~`03_VIDEO_AD_REGISTRY.md` — Edited Horizontal/Vertical (32 files)~~ **DONE 2026-07-11 (Decision 060)** — working master in `06_VIDEO_ADS_MASTER\01_LEGACY_LAUNCH\`; MAS HQ originals retained as second copy
2. `01_BRAND_ASSETS_REGISTRY.md` — Winning Marketing Assets (119 files) — proven, high-reuse creative
3. ~~`02_PROOF_REGISTRY.md` — curated proof subfolders~~ **DONE 2026-07-11 as COPY (Decision 034)** — working proof now in `08_PROOF_BANK\`; Hot_Seats ruled a duplicate set (excluded), CTA_Offer stays registered-only (offer clips, not proof)
4. `05_PHOTO_VIDEO_LIBRARY_REGISTRY.md` — `01_EDMUND_CINDIOR\` + `01_HERO_VIDEOS\` (320 files) — smallest, clearest value
5. Everything else — curate before moving (logos, CNY lunch photos, team/events photos, sales decks)

## READS FROM

- `X-Singapore Real Estate Insider - MAS HQ\05_ASSET_BANK\` (all subfolders — read-only)
- `X-Singapore Real Estate Insider - MAS HQ\02_CLIENTS\Keep\` (read-only)
- `X-Singapore Real Estate Insider - MAS HQ\04_CONTENT_ADS_ENGINE\01_CAMPAIGN_LEGACY_LAUNCH\03_Video\00_RAW_FOOTAGE\` (read-only)

## FEEDS INTO

- `02_POSITIONING_AND_IP\` (Case_Study_Bank + Founder_Case_Masters define the proof-category framework this evidence should be organized against)
- `05_CONTENT_MARKETING_ENGINE\` (creative reuse, b-roll, testimonial content)
- `04_AGENT_EDITION_OS\` (brand consistency for agent-facing marketing)
- `01_E.C.O.S\03_CONTENT_STUDIO.md`, `04_MARKETING_ADS_DESK.md` (desks that pull proof/creative for live work)
