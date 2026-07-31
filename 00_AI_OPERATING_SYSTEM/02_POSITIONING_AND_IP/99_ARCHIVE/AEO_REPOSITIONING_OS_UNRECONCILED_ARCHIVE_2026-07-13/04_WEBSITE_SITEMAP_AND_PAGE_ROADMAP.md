# 04 — WEBSITE AUTHORITY ARCHITECTURE & PAGE ROADMAP
**Domain:** `thereimethod.com` (authority domain, per D2) · **Phase:** 4 — Website Authority Architecture
**Owner:** Website Architecture (Opus) · **Date:** 9 July 2026 · **Companion CSV:** `AEO_Page_Roadmap.csv` (90 rows)
**Status:** Built on LOCKED decisions in `_MASTER_CONTEXT_BRIEF.md`. Regulatory content marked [VERIFY] + date-stamp.

---

## EXECUTIVE SUMMARY

This document defines the full website architecture for `thereimethod.com` — the single authority domain that earns every link, citation and entity signal for Coach Edmund Tan, Cindior Ho, and the category **The Second Property Ladder™**. It solves the central tension of this build: **the category vocabulary is not what buyers search.** Nobody types "Second Property Ladder" or "Move Sequence" into Google — they type "sell HDB buy condo", "ABSD second property", "decoupling property Singapore", and "should I sell my HDB after MOP". The architecture answers this with a two-layer system: **demand-capture pages** rank for the phrases buyers actually search, while **category pages** build the brand and the method; **internal links bridge the two** — every demand page links up to the category hub, a relevant calculator, and the Position Map session. We capture the demand and correct the frame in the same visit. The plan sequences 90 pages across three months (entity foundation first, then highest-intent demand capture, then long-tail depth) and continues at a sustainable ~2 pages/week for a full 12-month roadmap. Every page routes to one universal CTA — the **Position Map session** — or the diagnostic that feeds it. No doorway pages, no thin content, no schema for content that is not on the page (D8). Search terms flagged as banned-adjacent — "decoupling" and "sell one buy two" — are captured on-page but reframed through **Exit Before Entry™** and the **Move Sequence** rather than endorsed as slogans.

---

## 1. FULL SITEMAP (TREE WITH SLUGS)

```
thereimethod.com/
│
├── /                                   Homepage — category entry, routes to diagnostic + session
│
├── AUTHORITY / ENTITY LAYER (brand-building)
│   ├── /about                          The REI Method (advisory brand)
│   ├── /edmund-tan                      Founder — Coach Edmund Tan (lead authority face)
│   ├── /cindior-ho                      Founder — Cindior Ho (co-founder authority face)
│   ├── /second-property-ladder          CATEGORY + METHOD HUB (the 5 Steps, Property Climber)
│   │   ├── (child: /guides/what-is-the-second-property-ladder)
│   │   ├── (child: /guides/five-steps-second-property-ladder)
│   │   └── (child: /guides/what-is-a-position-map)
│   └── /exit-before-entry               Category law (Exit Before Entry™)
│
├── OFFER LAYER (conversion)
│   ├── /position-map-session            OFFER PAGE — single universal CTA (45-min session)
│   ├── /case-studies                    Proof hub (7 case-study themes)
│   │   ├── /case-studies/hdb-to-condo-exit-first
│   │   ├── /case-studies/two-name-path-decoupling
│   │   ├── /case-studies/missed-window-warning
│   │   ├── /case-studies/one-stronger-asset-before-two
│   │   ├── /case-studies/strategy-over-comfort
│   │   ├── /case-studies/repositioning-for-growth
│   │   ├── /case-studies/exit-before-entry-in-action
│   │   ├── /case-studies/single-name-climb
│   │   ├── /case-studies/hold-two-path
│   │   ├── /case-studies/trade-up-path
│   │   ├── /case-studies/dink-couple-climb
│   │   └── /case-studies/new-launch-disqualification
│   └── /reviews                         Testimonials + Google reviews (feeds GBP)
│
├── DEMAND-CAPTURE LAYER (SEO/AEO — the phrases buyers search)
│   ├── /tools                           Calculators hub
│   │   ├── /tools/absd-calculator
│   │   ├── /tools/sell-first-or-buy-first-sequencer
│   │   ├── /tools/cpf-accrued-interest-estimator
│   │   ├── /tools/mop-timeline-checker
│   │   ├── /tools/hdb-upgrade-affordability
│   │   ├── /tools/absd-remission-checker
│   │   ├── /tools/sale-proceeds-calculator
│   │   ├── /tools/net-asset-value-tracker
│   │   └── /tools/second-property-budget-planner
│   ├── /guides                          Informational hub
│   │   └── /guides/[topic]              (24 demand + method guides — see CSV)
│   ├── /compare                         Comparison hub
│   │   └── /compare/[x-vs-y]            (11 comparison pages — see CSV)
│   ├── /mistakes                        Buyer-mistake hub
│   │   └── /mistakes/[topic]            (7 mistake pages — see CSV)
│   └── /faq                             Sitewide FAQ (AEO answer surface)
│
├── UTILITY / TRUST
│   └── /contact                         Contact + booking (PDPA-compliant form)
│
└── COMPLIANCE (sitewide footer links + CEA block)
    ├── /privacy
    ├── /disclaimer                       CEA salesperson disclosure + risk/no-guarantee
    └── /pdpa                             PDPA 2012 + DNC consent

CEA COMPLIANCE BLOCK — rendered sitewide in footer on every page:
  Registered names + CEA reg nos (Edmund, Cindior) + PropNex agency name + licence no.
  [VERIFY: all four identifiers before any page goes public — D7]
```

**Vanity-domain relationship (from D3, governed by Phase 3, not built here):**
`secondpropertyladder.com` hosts the "Which Step Are You On?" diagnostic (funnel steps noindexed; one indexable bridge page canonical to `/second-property-ladder`). `legacylaunch.com.sg` hosts the Legacy Launch V2 funnel (same noindex/bridge rules). Both footer-link to the authority domain and founder pages. `singaporerealestateinsider.com` and `6figurepropertyprofits.com` 301 to `thereimethod.com` (D4). Changi Green is never cross-linked (D1).

---

## 1B. DEMAND-TO-CATEGORY BRIDGE MAP (THE CENTRAL TENSION, RESOLVED)

The category vocabulary is not what buyers search — so each real search phrase gets a demand-capture page, which then bridges to a category concept via internal links and the on-page frame-correction section. This table is the spine of the whole architecture; every builder should keep it open.

| What buyers actually search | Capture page (ranks) | Bridges to (category concept) | Frame correction on-page |
|---|---|---|---|
| "sell HDB buy condo" | `/guides/sell-hdb-buy-condo` | The Move Sequence (Step 3) | The question isn't whether — it's the safe order. |
| "HDB upgrade to condo" | `/guides/hdb-upgrade-to-condo` | The Second Property Ladder (climb) | Upgrading is the first step, not the finish line. |
| "ABSD second property" | `/guides/absd-second-property` + calculator | Exit Before Entry™ | ABSD is a sequence input, not a wall. |
| "decoupling property Singapore" | `/guides/decoupling-property-singapore` | The Two-Name Path / Name-Count Advantage | A structure inside a sequence, never a slogan. |
| "sell one buy two" | `/guides/sell-one-buy-two-singapore` | Hold-Two vs Trade-Up Path | NAV climb, not door-count; order before offer. |
| "CPF accrued interest when selling" | `/guides/cpf-accrued-interest-when-selling` + estimator | Position Map (Step 1, your numbers) | Accrued interest changes your real proceeds. |
| "should I sell my HDB after MOP" | `/guides/should-i-sell-my-hdb-after-mop` | Direction Statement (Step 2) | Post-MOP is a decision point, not a default. |
| "EC upgrade" | `/guides/ec-upgrade-to-condo` | The climb from a private-capable start | Same ladder, different starting rung. |
| "new launch vs resale" | `/compare/new-launch-vs-resale` | Selection Research / exit-readiness | Buy the one you can exit, not the one you can enter. |
| "second property Singapore" | `/guides/second-property-singapore` | The Second Property Ladder (category) | The safe order to a second property. |
| "avoid ABSD legally" | `/guides/avoid-absd-legally` | Exit Before Entry™ + Two-Name Path | Legitimate structures, sequenced — never avoidance. |
| "trade up condo Singapore" | `/guides/trade-up-condo-singapore` | The Trade-Up Path | One route up the ladder, chosen by position. |
| "single buying private property" | `/guides/single-buying-private-property` | Single-Name Climb / Name-Count Advantage | Singles climb too — one name can be an advantage. |

## 2. PAGE TEMPLATE STRUCTURES (BY PAGE TYPE)

Every template obeys the **answer-first** rule for AEO: the first on-page block after the H1 is a 40–60 word direct answer a language model can lift verbatim. Every page carries a visible `Last updated: [date]` (`dateModified`) and, on any regulatory claim, a `[VERIFY — figures current as of {date}]` line. Every page ends with the sitewide CEA compliance block. No schema is emitted for content not physically present on the page (D8).

### 2.1 Authority / Founder page (`/edmund-tan`, `/cindior-ho`, `/about`, `/exit-before-entry`)
- **H1 pattern:** "{Name} — {role in plain terms}" e.g. "Coach Edmund Tan — Property Climber, before he guided them." / For law page: "Exit Before Entry™ — Why We Research the Exit Before You Enter."
- **Answer-first block:** who this person/idea is and why they are credible, in 2–3 sentences.
- **Proof block:** portfolio journey since 2019 (Tre Ver → Parc Clematis → United Square → 4-bed east-side) [VERIFY all figures]; PropNex CEA credential line; "We built it before we advised it."
- **Method connection:** how this founder/law maps to the 5 Steps and the category.
- **Author box:** cross-links Edmund ↔ Cindior ↔ The REI Method; sameAs to FB/IG/YouTube (media brand) only — never Changi Green.
- **FAQ block:** 3–5 People-Also-Ask entries.
- **CTA block:** Book a Position Map session (primary); take the diagnostic (secondary).
- **Schema:** `Person` / `AboutPage` / `Organization`, `BreadcrumbList`, `FAQPage`. Video → `VideoObject`.

### 2.2 Guide page (`/guides/[topic]`) — the demand-capture workhorse
- **H1 pattern:** the search phrase, plainly — e.g. "How to Sell Your HDB and Buy a Condo (The Safe Order)".
- **Answer-first summary block (AEO):** the direct answer in 40–60 words, citable, correct, Singapore-specific. This is the block that wins AI Overviews and answer engines.
- **Body:** the honest, complete answer to the query (numbers, steps, regulations), then a **frame-correction section** that reframes the query through the method (e.g. "The real question isn't sell-first-or-buy-first — it's what order your Move Sequence demands"). Bridge, never bait-and-switch.
- **Proof block:** one relevant case study card [VERIFY].
- **Tool link:** the matching calculator (e.g. ABSD calculator, sell-first sequencer).
- **FAQ block:** 3–4 PAA questions with answer-first responses.
- **CTA block:** Position Map session; diagnostic secondary.
- **dateModified display:** yes; regulatory guides carry [VERIFY] + date-stamp and enter the update cadence.
- **Schema:** `Article` (+ `HowTo` where step-based), `FAQPage`, `BreadcrumbList`. Video → `VideoObject`.

### 2.3 Comparison page (`/compare/[x-vs-y]`)
- **H1 pattern:** "{A} vs {B}: {the real decision}" — e.g. "New Launch vs Resale: Which One Can You Actually Exit?".
- **Answer-first block:** the short verdict (with the honest "it depends on your position" caveat that routes to the Position Map).
- **Comparison table:** side-by-side on the criteria buyers care about (cost, ABSD exposure, exit demand, risk) — this table is the AEO asset.
- **Frame-correction section:** re-anchors the choice on **exit-readiness / NAV**, not door-count or hype.
- **Proof + Tool + FAQ + CTA blocks:** as per guide.
- **Schema:** `Article`, `FAQPage`, `BreadcrumbList`.

### 2.4 Case study (`/case-studies/[slug]`)
- **H1 pattern:** the outcome, not the client — "The Exit That Unlocked Their Next Move" / theme-led.
- **Answer-first block:** the situation → sequence → outcome in 3 sentences.
- **Structured story:** Starting Position → the One-Property Trap they faced → the Move Sequence → Exit Before Entry applied → result (NAV movement) [VERIFY every figure]. First names only (Edward & Rose, MoK & Jine, Lynn, etc.).
- **Proof block:** verifiable specifics only; confidence flag (PROVEN/VERIFIED/INFERRED/UNTESTED).
- **CTA block:** Position Map session.
- **Author box + video** (which YouTube angle) where available.
- **Schema:** `Article`, `BreadcrumbList`. Video → `VideoObject`. (Do **not** use Review/Testimonial schema on narrative case studies — reserve `Review`/`AggregateRating` for `/reviews`.)

### 2.5 Tool / calculator page (`/tools/[calculator]`)
- **H1 pattern:** the utility phrase — "ABSD Calculator (Singapore, {year})".
- **Answer-first block:** what the tool computes and the one input that matters most.
- **The calculator:** working, on-page, mobile-first; regulatory inputs date-stamped [VERIFY].
- **Explainer:** short prose beneath (feeds the `Article`/FAQ AEO surface) linking to the matching guide.
- **CTA block:** "Your numbers only mean something in sequence — book a Position Map session."
- **Schema:** `SoftwareApplication` / `WebApplication`, `BreadcrumbList`, `FAQPage` where Q&A present.

### 2.6 Hub page (`/second-property-ladder`, `/guides`, `/tools`, `/compare`, `/case-studies`)
- **H1 pattern:** category or cluster name.
- **Answer-first block:** what this hub covers.
- **Curated child grid:** links to every spoke (the internal-linking backbone).
- **CTA block:** diagnostic + Position Map session.
- **Schema:** `CollectionPage` / `ItemList`, `BreadcrumbList`; category hub adds `Service` + `FAQPage`.

### 2.7 Offer page (`/position-map-session`)
- **H1:** "Book a Position Map Session — Leave With Your Numbers." (45 min.)
- **Answer-first block:** what it is, what you leave with, how long — no price hype.
- **Blocks:** outcomes → what a Position Map contains → founder credibility → reviews → FAQ (objections) → PDPA-compliant booking form → CEA block.
- **Schema:** `Service` + `Offer`, `FAQPage`, `BreadcrumbList`.

---

## 3. FIRST 30 PAGES TO BUILD (PRIORITY ORDER + REASONING)

Sequenced so search engines and answer engines first establish **who** (entity), then **what** (category + law + offer), then the **highest-intent demand** that converts fastest. All Month 1.

| # | Slug | Type | Priority | Why this, this early |
|---|---|---|---|---|
| 1 | `/` | homepage | P0 | Root of the entity graph; routes all traffic to diagnostic/session. |
| 2 | `/about` | authority | P0 | Establishes The REI Method as the `Organization` entity. |
| 3 | `/edmund-tan` | founder | P0 | Lead authority face; E-E-A-T anchor for every claim on the site. |
| 4 | `/cindior-ho` | founder | P0 | Co-founder; completes the dual-founder brand (D1). |
| 5 | `/second-property-ladder` | hub | P0 | The category hub — top of the hub-and-spoke; every demand page links up here. |
| 6 | `/exit-before-entry` | authority | P0 | The category law and core differentiator; the frame all guides correct toward. |
| 7 | `/position-map-session` | offer | P0 | The single universal CTA; must exist before any page points to it. |
| 8 | `/case-studies` | hub | P0 | Proof hub; conversion depends on visible evidence. |
| 9 | `/reviews` | reviews | P0 | Trust surface; feeds GBP and `AggregateRating`. |
| 10 | `/tools` | hub | P0 | Demand-capture magnet hub; calculators are our fastest-ranking assets. |
| 11 | `/guides` | hub | P0 | Content hub that bridges search demand to the category. |
| 12 | `/faq` | faq | P1 | Sitewide AEO answer surface — high citation value early. |
| 13 | `/contact` | navigational | P1 | Booking + PDPA path; completes the conversion loop. |
| 14 | `/privacy` | compliance | P0 | Required before collecting any form data. |
| 15 | `/disclaimer` | compliance | P0 | CEA salesperson disclosure protects every claims page. |
| 16 | `/pdpa` | compliance | P0 | Governs all forms; must exist before diagnostic/booking go live. |
| 17 | `/tools/absd-calculator` | tool | P0 | "ABSD second property" is top-3 intent; a working calculator ranks fast and earns links. |
| 18 | `/tools/sell-first-or-buy-first-sequencer` | tool | P0 | Directly reframes the #1 buyer panic (order) into the Move Sequence. |
| 19 | `/tools/cpf-accrued-interest-estimator` | tool | P0 | CPF anxiety is universal among upgraders; feeds the numbers-first session. |
| 20 | `/tools/mop-timeline-checker` | tool | P1 | "When can I sell my HDB" — captures MOP-timing demand into Policy Clock. |
| 21 | `/guides/sell-hdb-buy-condo` | guide | P0 | The single highest-volume upgrade query; flagship demand page. |
| 22 | `/guides/hdb-upgrade-to-condo` | guide | P0 | The synonym query; captures the other half of upgrade demand. |
| 23 | `/guides/absd-second-property` | guide | P0 | Top regulatory-intent query; pairs with the ABSD calculator. |
| 24 | `/guides/should-i-sell-my-hdb-after-mop` | guide | P1 | High-intent decision query; the moment a Property Climber is created. |
| 25 | `/guides/second-property-singapore` | guide | P1 | Core category-adjacent query; bridges demand to the brand term. |
| 26 | `/guides/cpf-accrued-interest-when-selling` | guide | P1 | Pairs with the CPF estimator; captures a distinct anxiety cluster. |
| 27 | `/case-studies/hdb-to-condo-exit-first` | case_study | P1 | Proof for the flagship guide (#21); The Exit That Unlocked the Next Move. |
| 28 | `/case-studies/two-name-path-decoupling` | case_study | P1 | Reframes "decoupling" demand with a real Two-Name Path story. |
| 29 | `/case-studies/missed-window-warning` | case_study | P1 | Emotional proof of Exit-Later Buying; supports timing guides. |
| 30 | `/case-studies/one-stronger-asset-before-two` | case_study | P1 | Proves NAV-not-door-count; anchors the reframe pages. |

**Reasoning summary:** Pages 1–16 are the non-negotiable entity + offer + compliance spine — nothing else should rank before the site can prove who is speaking and can legally collect a lead. Pages 17–20 are the calculators, which historically earn backlinks and rank faster than prose. Pages 21–26 are the six highest-intent demand queries, each paired to a tool. Pages 27–30 are the proof that makes the demand pages convert.

---

## 4. FIRST 90 PAGES (GROUPED BY MONTH — DETAIL IN CSV)

Full per-page detail (secondary questions, internal links, proof, video angle, schema) lives in `AEO_Page_Roadmap.csv`. Summary:

### Month 1 — Foundation + highest-intent capture (Pages 1–30)
Entity spine (`/`, `/about`, `/edmund-tan`, `/cindior-ho`), category + law + offer (`/second-property-ladder`, `/exit-before-entry`, `/position-map-session`), all hubs, compliance trio, the four core calculators (ABSD, sell-first sequencer, CPF estimator, MOP checker), the six flagship demand guides, and four proof case studies. This month makes the site rankable, citable, and legally live.

### Month 2 — Demand-capture breadth (Pages 31–60)
The banned-adjacent reframes (`/guides/decoupling-property-singapore`, `/guides/sell-one-buy-two-singapore`), segment guides (EC upgraders, single buyers, trade-up), the comparison cluster (`/compare/new-launch-vs-resale`, `/compare/sell-first-vs-buy-first`, `/compare/hold-two-vs-trade-up`, and three more), the mistake cluster (`/mistakes/hdb-upgraders`, `/mistakes/buying-second-property`, `/mistakes/new-launch-buyers`, `/mistakes/decoupling`), three more calculators, four theme case studies, and the three method-explainer guides (what-is-SPL, five-steps, what-is-a-position-map). This month captures the middle of the demand curve and completes the method's on-page explanation.

### Month 3 — Long-tail depth + regulatory authority (Pages 61–90)
The ABSD/regulatory cluster (`/guides/absd-rates-singapore-2026`, remission, SSD, 15-month wait-out, TDSR — all [VERIFY] + date-stamped and entering the update cadence), the CPF cluster, single-buyer and DINK segment guides, four more comparisons (condo-vs-landed, RCR-vs-OCR, rent-vs-sell, two-vs-one-bigger), three more mistake pages, long-tail timing guides, two more calculators, four path/segment case studies, and the signature Step-3 doctrine page (`/guides/order-before-offer-sequencing`). This month wins the long tail and makes the site the definitive regulatory reference.

---

## 5. 12-MONTH PAGE ROADMAP (THEMES + COUNTS)

Months 1–3 front-load to establish authority (30/month). From Month 4 the cadence drops to a **sustainable ~2 pages/week (≈8/month)** — enough to keep publishing velocity and topical freshness without thin content.

| Month | Theme | New pages | Running total | Notes |
|---|---|---|---|---|
| 1 | Entity foundation + highest-intent capture | 30 | 30 | Spine, hubs, 4 calculators, 6 flagship guides, 4 case studies. |
| 2 | Demand-capture breadth (reframes, comparisons, mistakes) | 30 | 60 | Banned-adjacent reframes, comparison + mistake clusters, method explainers. |
| 3 | Long-tail depth + regulatory authority | 30 | 90 | ABSD/CPF/SSD/TDSR clusters (date-stamped), segment guides, doctrine page. |
| 4 | Segment deep-dives (DINK, singles, private-single climbers) | 8 | 98 | New Property Climber sub-types; new case studies per segment. |
| 5 | Financing & leverage cluster | 8 | 106 | TDSR/LTV depth, bridging loans, cash-buffer/Safe Motion guides + calculators. |
| 6 | Selection Research (Exit Before Entry applied) | 8 | 114 | District/region exit-demand guides, rentability, exit-buyer-pool method pages. |
| 7 | Legacy Launch bridge (new-launch application of SPL) | 8 | 122 | Reframe NLL under SPL; new-launch disqualification guides + case studies. |
| 8 | Refresh + regulatory update pass | 8 | 130 | Re-date-stamp all [VERIFY] pages; refresh Month-1 flagships with new data. |
| 9 | Comparison expansion (vehicle + region matrices) | 8 | 138 | New-vs-old district comparisons, tenure/hold-period comparisons. |
| 10 | Climb Cadence / repeat-buyer content (Step 5) | 8 | 146 | Annual Climb Review content, portfolio-monitoring, second-move planning. |
| 11 | Proof scale-up (case-study library expansion) | 8 | 154 | New verified client stories across all 7 themes; video-led. |
| 12 | Authority consolidation + internal-link audit | 8 | 162 | Pillar refresh, orphan-page fix, schema/entity audit, best-of roundups. |

Regulatory pages (ABSD, SSD, MOP, TDSR, cooling measures) are **re-verified and re-date-stamped every quarter** regardless of the theme month (D7 update cadence). Video production tracks the ~600-video YouTube library: reuse existing footage where the angle fits (Exit-Ready, Missed-Launch Loop, Regret/Hindsight, Math Doesn't Lie, Herd Instinct) before commissioning new.

---

## 6. INTERNAL LINKING MAP (HUB-AND-SPOKE RULES)

The internal-link system is what resolves the vocabulary tension: demand pages rank on search phrases, and their internal links pull authority up to the category and push visitors down to conversion.

**Rule 1 — Every demand page links UP to three fixed targets:**
1. the category hub `/second-property-ladder` (brand signal),
2. the single most relevant calculator under `/tools/*` (utility + dwell time),
3. the offer `/position-map-session` (conversion).
No demand page is a dead end.

**Rule 2 — Category hub is the spider.** `/second-property-ladder` links down to every guide, comparison, mistake, tool and case-study cluster. It is the parent in `BreadcrumbList` for the method pages and the highest-PageRank internal node after the homepage.

**Rule 3 — Founder pages ↔ case studies (bidirectional).** `/edmund-tan` and `/cindior-ho` link to case studies as proof; every case study links back to the founders as the authority behind the outcome. This builds the E-E-A-T loop.

**Rule 4 — Calculators ↔ their guides (bidirectional).** Each tool links to its explainer guide and vice-versa (ABSD calculator ↔ `/guides/absd-second-property`; sell-first sequencer ↔ `/guides/sell-hdb-buy-condo`; CPF estimator ↔ `/guides/cpf-accrued-interest-when-selling`; MOP checker ↔ `/guides/should-i-sell-my-hdb-after-mop`).

**Rule 5 — Comparison and mistake pages link laterally to sibling guides**, then up to the hub and out to the session. Reframe pages ("decoupling", "sell one buy two") always link to `/exit-before-entry` so the correction is one click away.

**Rule 6 — Max 3 clicks from homepage to any page.** Homepage → hub → spoke = 3. Hubs must surface every child; no page may be orphaned (audited in Month 12 and each quarter).

**Rule 7 — Anchor-text discipline (never over-optimised).** Mix **demand phrases** ("sell your HDB and buy a condo", "ABSD on a second property") with **category terms** ("the Move Sequence", "Exit Before Entry", "the Second Property Ladder"). Never repeat the exact-match keyword as anchor across many pages — vary naturally, use branded and descriptive anchors, and keep exact-match to a minority. Banned words never appear in anchors, slugs, or titles (no "homeowner", "investment property", "unit", "good buy").

**Rule 8 — Legacy Launch bridge.** New-launch pages (`/mistakes/new-launch-buyers`, `/compare/new-launch-vs-resale`, `/case-studies/new-launch-disqualification`) link to `/exit-before-entry` and the category hub, positioning the Legacy Launch campaign as Steps 3–4 of SPL applied to new launches (D1) — never as a competing category.

**Illustrative flow (the tension resolved in one journey):**
`/guides/sell-hdb-buy-condo` (ranks for the search) → links up to `/second-property-ladder` (learns the category) → across to `/tools/sell-first-or-buy-first-sequencer` (gets a number) → down to `/position-map-session` (converts). Demand captured; frame corrected; conversion path complete.

---

## 7. COMPLIANCE NOTES (APPLIED ACROSS ALL PAGES)

- **CEA block sitewide (D7):** registered names + CEA reg nos for both founders + PropNex agency name/licence no in the footer of every page. **[VERIFY all four before publish.]**
- **No banned words** in slugs, titles, meta descriptions, anchors, or body — verified per page (no "homeowner", "investment property", "unit", "good buy", "agent"/"advice"/"consultation" as self-description, "asset progression"). "Second property" / "own two properties" phrasing used instead.
- **Regulatory pages** (ABSD, SSD, MOP, TDSR, CPF accrued interest, cooling measures, 15-month wait-out) carry `[VERIFY — figures current as of {date}]` and a visible `dateModified`; they enter a quarterly update cadence.
- **Every $ figure** in case studies and founder proof carries the [VERIFY] discipline until confirmed against records (Master Brief §2 claims bank).
- **PDPA + DNC** consent on `/contact`, the booking form, and the diagnostic; `/pdpa` governs all forms.
- **No schema without on-page content** (D8): `Review`/`AggregateRating` only on `/reviews`; `HowTo` only on genuinely step-based pages; `SoftwareApplication` only on working calculators.
- **"This is advisory, not agency"** is a flagged compliance risk (D7) — do **not** reuse this line on any new page; use "Advisory-first. We plan the sequence before any transaction." pending PropNex compliance review.

---

## QUESTIONS TO CLARIFY

1. Is `thereimethod.com` currently live with any content, and do Search Console / GA4 properties exist? (Determines whether Month 1 is a fresh launch or a migration.)
2. CEA registration numbers + exact registered names for Edmund and Cindior, and PropNex licence number — required in the sitewide footer before any page publishes (D7).
3. Which of the six [VERIFY] portfolio/claim figures are confirmed against records? Case studies 27–30 and all founder proof blocks are blocked until these clear.
4. Are the calculators to be built natively on `thereimethod.com`, or embedded from a tool builder? Affects `SoftwareApplication` schema and page-speed.
5. Does Cindior have public profiles to link as `sameAs` on `/cindior-ho`, and how prominent does she want to be on camera (affects video allocation on founder/case pages)?
6. Confirmation that the diagnostic on `secondpropertyladder.com` and the Position Map booking calendar are ready to receive the traffic Month-1 pages will drive.
7. Preferred CMS/stack for `thereimethod.com` (WordPress vs headless vs GHL sites) — governs how templates in §2 are implemented and schema injected.

## DEPENDENCIES

- **Phase 3 (Domain Architecture)** must confirm `thereimethod.com` DNS/hosting and the 301s/canonicals before Month-1 pages are indexed.
- **Phase 5 (AEO Topic Clusters)** should align its cluster map to the 90 slugs here to avoid keyword overlap/cannibalisation.
- **Phase 9 (Proof Library)** must supply verified case-study figures and confidence flags before case-study pages 27–30 publish.
- **Phase 10 (Content Engine SOP)** owns the ongoing ~2/week cadence from Month 4 and the video-angle assignments.
- **Phase 11 (Technical AEO/SEO)** owns schema implementation, `dateModified` automation, and the internal-link/orphan audit.
- **GHL** must have `spl_*` custom fields created (they do not exist yet) before the diagnostic that feeds these pages can score leads.
- **PropNex compliance** sign-off on the CEA footer block and the replacement advisory line.

## FIRST 5 ACTIONS

1. **Stand up the entity spine (Pages 1–7):** homepage, `/about`, `/edmund-tan`, `/cindior-ho`, `/second-property-ladder`, `/exit-before-entry`, `/position-map-session` — with the CEA footer block wired in (using [VERIFY] placeholders flagged, not invented).
2. **Publish the compliance trio (Pages 14–16)** so forms can legally collect data, then confirm PDPA/DNC consent wiring on `/contact` and the booking form.
3. **Build the four core calculators (Pages 17–20)** — ABSD, sell-first sequencer, CPF estimator, MOP checker — date-stamped, and cross-link each to its guide.
4. **Write the six flagship demand guides (Pages 21–26)** using the guide template, each with the answer-first block and the three fixed up-links (hub, tool, session).
5. **Confirm the four Month-1 case-study figures with the founders** and publish Pages 27–30, closing the proof loop so the demand guides convert.

---

## CONCERNS (flagged, not changed)

- **Calculator accuracy is a compliance surface.** An ABSD/CPF/MOP calculator that returns a wrong figure is a worse liability than no calculator. Recommend each tool ships with a visible "estimate only — verify with the [VERIFY] source" disclaimer and a dated ruleset, owned by Phase 11.
- **Volume vs quality risk (D8).** 30 genuinely answer-complete pages in Month 1 is aggressive for a two-founder operation. If proof/verification cannot keep pace, prioritise the 16-page spine + 4 calculators + 6 guides and let the 4 case studies slip to early Month 2 rather than publish unverified figures.
- **"Decoupling" slug ranking risk.** Ranking for "decoupling" invites buyers whose frame we are correcting; ensure the answer-first block leads with the honest answer before the reframe, or the page reads as bait-and-switch and loses AEO trust.
