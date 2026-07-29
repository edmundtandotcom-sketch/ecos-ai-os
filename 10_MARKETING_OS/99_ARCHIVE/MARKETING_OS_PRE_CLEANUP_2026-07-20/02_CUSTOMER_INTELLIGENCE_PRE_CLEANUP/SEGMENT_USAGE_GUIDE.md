# SEGMENT_USAGE_GUIDE
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\02_CLIENT_INTELLIGENCE\01_BUYER_SEGMENT_LIBRARY_v2.0.md` + `00_AI_OPERATING_SYSTEM\05_CONTENT_MARKETING_ENGINE\00_CAMPAIGN_DOORS_MASTER_v1.0_CANDIDATE.md`
Evidence level: N/A (structural mapping; underlying segments are Tier 3 field-derived psychology profiles, not performance data)
Supersedes: none
Sources: the two files above
Next review: on approval of Campaign Doors Master (Decision 032) or Buyer Segment Library revision

---

## Rule From The Source
A buyer segment is a client psychology profile — **not automatically** a campaign, ad set, funnel, or offer. A segment becomes a campaign only when it's deliberately built one. Diagnose with segments; decide campaigns separately.

## Segment Library (7 Core Segments, Client Advisory Engine only)
| Code | Segment | Ascent Stage | Core Question | Recommended Campaign Direction |
|---|---|---|---|---|
| FCC | First-Climb Existing Owner | A1 | "My property went up. What now?" | Idle Million / One Property Trap / Next 3 Moves |
| DINK | Golden Window DINK | A1 | "Are we wasting our most flexible years?" | Golden Window DINK / One Property Trap |
| FHA | Forever-Home Attached Owner | A1 or A2 | "This is our home. But are we stuck?" | Forever Home Trap / Family Asset Planning |
| DFP | Decoupling / Free-Name Planner | A1 or A2 | "If we free a name, what should we buy?" | Decoupling Is Not The Strategy / Exit-First |
| RM | Ready Mover | A1 or A2 | "Before I sign, is this really the right move?" | Before You Sign The OTP / Showflat Loop |
| HECO-Q | Qualified HDB/EC Upgrade-Window Household | A1 | "When we exit, what should this unlock next?" | HDB/EC Upgrade Window / 1-to-2 Window — **guardrail: qualified only, see C04** |
| FAP | Family Asset Planner | A2 (former A3 retired — Decision 063) | "How should property support our family's next chapter?" | Family Asset Planning (Family Legacy door RETIRED — Decision 058) |

## Campaign Doors (Content Marketing Engine — where segments become campaigns)
| Door | Strategic Intent | Audience | Segments It Draws On |
|---|---|---|---|
| Legacy Launch [LL] | SI-05 | Joint-name condo owners, 30s–50s, equity built, next move unclear (decouple-specific per Decision 037/audience ruling 2026-07-11) | FCC, DFP, RM |
| ~~Family Legacy [FL]~~ **RETIRED (Decision 058)** | SI-06 (historical) | Parents 48–65 with idle capital + working child 23–32 | FAP — now served inside standard A1/A2 engagements |
| ~~Mash-up [M]~~ **RETIRED (Decisions 058/063 — door and A4 level both gone)** | SI-05 + SI-06 (historical) | Joint-name condo owners AND a clean-name working child | FCC + FAP — family-overlap cases handled inside the Legacy Launch / A1–A2 engagement |

## Second Segmentation System — Not Mapped To The Above
The Reel Script Rulebook's ad-production system uses a separate **G-code** behavioural-profile set (G1 Idle Millionaire, G2 Comfortable Compounder, G3 Worried Watcher, G4 Legacy Builder, G5 Retirement Rusher, G8 Spouse Alignment Case) for creative variation — built for Pack 1 of Legacy Launch specifically. G1–G5 roughly parallel FCC/FHA psychology but were built independently and no source document maps G-codes to Buyer Segment Library codes 1:1. Do not assume G1 = FCC exactly; both describe overlapping but not identical profiles. Full detail: `05_FRAMEWORK_LIBRARY\VIDEO_FRAMEWORKS.md`.

## Conflicts — Flag
- **C03 — Buyer definition drift.** Master_Business_Big_Idea (singles included, NAV-based) vs CategoryKing (progressing families) vs Mechanism v1.3 ($20k+/$2.5m+ couples) describe the buyer differently. This segment library is the *psychology* layer and does not itself resolve C03 — it sits downstream of whichever buyer definition wins. Do not lock final targeting parameters (income/quantum thresholds) off this file alone.
- **C06 — Legacy Launch dual audience.** The active, currently-running LL brief targets a broad "mature private owner unsure of next move" (G1 Idle Million), while the Trigger Marketing Bank's [LL] copy and the Family Legacy/Mash-up docs define SI-05 narrowly as decouple-viable joint condo owners. These are not the same targeting brief. Open question for Edmund: is decouple-specific messaging a second lane inside Legacy Launch (not yet built), or has the live brief deliberately broadened past the original SI-05 definition? Full detail: Campaign Doors Master §6.1.
- **HECO-Q guardrail (ties to C04):** do not target broad HDB/EC owners with generic wealth claims — qualify by numbers, timeline, name structure, and advisory readiness first. See `OBJECTIONS_MAP.md` C04 for the deeper HDB/EC in/out-of-audience conflict between the TRAPS Bank and the Consumer Psychology Library v3.1.

## Status Note — RESOLVED (Decisions 058 + 063 + 067, 2026-07-11)
The Family Legacy and Mash-up marketing doors are **RETIRED** (Decision 058 — supersedes Decision 032's "stay live" premise; copy banks kept as reference). Decision 063 additionally retired the A3/A4 ascent levels and the A4 Mash-Up advisory delivery pattern — the Ascent Model is A0–A2; multi-name/family situations run inside standard A1/A2 engagements. **Decision 067 retired SI-06 outright as a Strategic Intent classification** — family/idle-capital situations classify under SI-05 or standard intents; historic SI-06 CRM tags keep their meaning as history. Legacy Launch is the only active client-engine door.

## Usage Rule
Do not turn every segment into a campaign. Use this library to diagnose which segment a piece of content or targeting brief is for; use the Campaign Doors Master to decide whether that segment already has a live door or needs a new one.
