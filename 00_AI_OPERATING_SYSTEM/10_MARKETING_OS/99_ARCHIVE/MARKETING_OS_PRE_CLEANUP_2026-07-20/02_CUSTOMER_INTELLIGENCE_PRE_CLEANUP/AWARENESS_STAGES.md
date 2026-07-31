# AWARENESS_STAGES — Reconciliation
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `00_AI_OPERATING_SYSTEM\05_CONTENT_MARKETING_ENGINE\00_FOUNDATIONS\LAYER_3A_REEL_SCRIPT_RULEBOOK_v1.1.md` §2B + `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\01_FOUNDATION\MAS_ASCENT_MODEL_REFERENCE_v2.0.md`
Evidence level: N/A (structural reconciliation, not a data claim)
Supersedes: none
Sources: the two files above
Next review: when either source is revised, or a client-facing asset attempts to show both scales at once

---

## Two Different Systems — Not The Same Axis
The workspace runs two awareness/stage systems that are **not currently mapped to each other**. This file states both, shows the best-available alignment, and flags the gap. Do not treat them as interchangeable.

### System 1 — Media/Content Awareness Stage (PA / SA / PA2)
Source: Reel Script Rulebook v1.1 (Legacy Launch ad production). A classic cold→warm→hot funnel-position label, applied to ad/content variants.
| Stage | Where they are | Ad goal | Tone | CTA |
|---|---|---|---|---|
| PA — Problem Aware | Know something is off; haven't calculated the cost | Name the silent problem | Observational, mirror | Soft — checklist, quiz |
| SA — Solution Aware | Know property can be optimised; hasn't committed to an approach | Show REI Method as the right approach | Logical, slightly urgent | Medium — free session, mini-consult |
| PA2 — Product Aware | Knows Coach Edmund / REI; needs a final push | Social proof, authority, remove last objection | Confident, direct | Strong — book session, limited slots |

### System 2 — Ascent Stage (A0–A2)
Source: Ascent Model Reference v2.0 (carries a Decision 063 supersession banner). The client's journey/readiness spine, independent of any single piece of content.
| Stage | Name | Meaning |
|---|---|---|
| A0 | Activation | Realising current property position may need review |
| A1 | First Climb | Moving from one meaningful property position into a structured next move (Legacy Launch's anchor stage) |
| A2 | Compound | Preparing for exit, redeployment, or the second wealth-building cycle |

> **RETIRED (Decision 063, 2026-07-11):** the former A3 (Legacy) and A4 (Mash-Up) stages are removed from the Ascent Model. Multi-name/family situations are handled inside standard A1/A2 engagements; the Family Legacy and Mash-up marketing doors were retired by Decision 058.

## Best-Available Alignment (approximate — not a confirmed mapping)
| Ascent Stage | Likely PA/SA/PA2 mix | Note |
|---|---|---|
| A0 Activation | Mostly PA | Cold awareness content sits here |
| A1 First Climb | PA → SA → PA2 (full funnel runs inside this one Ascent stage) | This is where almost all current Legacy Launch ad production lives |
| A2 Compound | SA/PA2 (often warmer — past client or referral) | Less top-of-funnel content built for this stage yet |
| ~~A3 Legacy~~ / ~~A4 Mash-Up~~ | — | **RETIRED (Decisions 058/063)** — levels and doors removed; family-audience media planning runs inside the A1/A2 rows above |

## Why These Are Different Dimensions
PA/SA/PA2 measures **awareness of the message/offer** within one piece of content or ad set. Ascent Stage measures **the client's actual position in their property journey**, independent of what content they've seen. A client can be A1 (First Climb) and PA (has never seen REI content) or A1 and PA2 (has watched everything, knows Edmund, still hasn't moved). Collapsing the two into one scale would lose information needed for both media planning (PA/SA/PA2) and advisory diagnosis (Ascent Stage).

## Recommendation
Tag every campaign asset with **both** fields independently: `Ascent Stage` (who this is strategically for) and `Media Awareness Stage` (what this specific asset assumes they already know). `05_FRAMEWORK_LIBRARY\FRAMEWORK_REGISTRY.csv` uses the PA/SA/PA2 vocabulary in its `AwarenessStage` column since that is the field the ad-production system already tracks; Ascent Stage is the campaign-door-level classification (see `SEGMENT_USAGE_GUIDE.md`).

## Open Flag — RESOLVED (Decisions 053 + 063, 2026-07-11)
The Ascent Levels ↔ Ladder Moves relationship is now formally mapped in `00_AI_OPERATING_SYSTEM\02_POSITIONING_AND_IP\Second_Property_Ladder_Mechanism_v1.5.md` §10: they are two different axes (Ascent Level = journey stage; the 5 Moves = advisory method re-run inside any engagement), A0–A2 only. Still do not show Ascent Stage, PA/SA/PA2, and the 5 Moves as one unified ladder in a client-facing asset — they are three different dimensions.
