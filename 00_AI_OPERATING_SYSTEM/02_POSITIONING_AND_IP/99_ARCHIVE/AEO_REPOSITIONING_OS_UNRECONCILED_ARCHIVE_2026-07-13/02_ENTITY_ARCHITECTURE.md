# 02 — ENTITY ARCHITECTURE
**Phase 2 · AEO Repositioning OS · Singapore property advisory**
**Owner:** Entity Architect (Opus) · **Date:** 9 July 2026 · **Status:** Build-ready; inherits all LOCKED decisions from `_MASTER_CONTEXT_BRIEF.md`
**Authority domain:** `thereimethod.com` (D2) · **Model:** Dual co-founder personal brand behind The REI Method (D1)

---

## Executive Summary

This phase defines the machine-readable identity layer — the set of named things Google's Knowledge Graph and AI answer engines (ChatGPT, Gemini, Perplexity, Google AI Overviews) must recognise, connect, and cite. We define **ten entity classes** anchored on two Person entities (Coach Edmund Tan, Cindior Ho) and one Organization (The REI Method), which owns one Category/Method (The Second Property Ladder™) and one media property (Singapore Real Estate Insider, YouTube only). Every advisory signal converges on `thereimethod.com`; campaign and diagnostic funnels bridge back to it but never fork the graph (D3). **Changi Green is hard-quarantined** — it shares a GHL sub-account but must never appear in any advisory `sameAs`, schema, or internal link. The two live risks this architecture manages: (1) the funnel currently shows three competing names (Legacy Launch / Singapore Real Estate Insider / the founders), which fragments the entity; and (2) "REI" collides with the US retailer REI (Recreational Equipment, Inc.) — mitigated by always writing "The REI Method" in Singapore-property co-occurrence with the founders' names. Schema is scoped strictly to Google-eligible types on real, on-page content (D8). CEA registration numbers and PropNex licence details are the single largest blocker — flagged [VERIFY] throughout and required before any Person/Organization schema publishes.

---

## 1. Entity Register (the ten entities)

### Entity 1 — Person: Edmund Tan ("Coach Edmund Tan")

| Field | Value |
|---|---|
| **Official name** | Edmund Tan |
| **Display / brand name** | Coach Edmund Tan |
| **Aliases / historical tokens** | Property Coach Edmund Tan; "Edmund"; Singapore Real Estate Insider (host attribution — historical, do not use as his personal name); associated with "6 Figure Property Profits" (retire this association per D4) |
| **Canonical description** (reusable verbatim) | "Coach Edmund Tan is a Singapore property advisor and co-founder of The REI Method. He created The Second Property Ladder™, a step-by-step framework that helps Singaporean property owners climb from their first serious property to higher net asset value." |
| **Primary URL** | `thereimethod.com/edmund-tan` |
| **SameAs** | facebook.com/coachedmundtan · instagram.com/propertycoachedmundtan · youtube.com/@singaporerealestateinsider · GBP (share.google/bpyWTGgjlyNxt8Xiz) [VERIFY] · LinkedIn [OPEN — create/confirm] |
| **Supporting pages** | Category hub (`/second-property-ladder`); founder-proof/case-study pages; author byline on all guides |
| **Proof assets** | Portfolio journey (Tre Ver → Parc Clematis → United Square → 4-bed east-side) [VERIFY all figures]; YouTube library (600+ videos [VERIFY]); GBP reviews; CEA registration [VERIFY] |
| **Schema.org type** | `Person` (with `worksFor`, `jobTitle`, `knowsAbout`, `sameAs`, `image`) |
| **Internal link targets** | ← every guide byline; ← category hub "created by"; ← case studies; ↔ Cindior Ho (`colleague`); → The REI Method (`worksFor`) |
| **Priority** | **P0** |

### Entity 2 — Person: Cindior Ho

| Field | Value |
|---|---|
| **Official name** | Cindior Ho |
| **Aliases / historical tokens** | "Cindior"; named GHL account contact ("Coach Edmund & Cindior") |
| **Canonical description** | "Cindior Ho is a Singapore property advisor and co-founder of The REI Method, where she helps progressing Singaporean families plan the safe sequence of their second property move using The Second Property Ladder™." |
| **Primary URL** | `thereimethod.com/cindior-ho` |
| **SameAs** | LinkedIn [OPEN — confirm existence]; Instagram [OPEN — does she have one?]; shares GBP and The REI Method org pages. **Note:** no confirmed personal social profiles exist (D6 flags this gap). |
| **Supporting pages** | Category hub; co-founder proof; "our story" page |
| **Proof assets** | Co-founder journey (shared portfolio); CEA registration [VERIFY] |
| **Schema.org type** | `Person` |
| **Internal link targets** | ↔ Edmund Tan (`colleague`); → The REI Method (`worksFor` / `founder`) |
| **Priority** | **P0** (parity with Edmund per dual-founder decision; content depends on her building public presence — see Concerns) |

### Entity 3 — Business: The REI Method

| Field | Value |
|---|---|
| **Official name** | The REI Method |
| **Aliases / historical tokens** | "REI Advisory" (superseded — do not reuse); "The REI Method Advisory Brand"; GHL location "Coach Edmund & Cindior" (internal only). **Never** abbreviate to bare "REI" in public copy (US-retailer collision — see §7) |
| **Canonical description** | "The REI Method is a Singapore property advisory founded by Coach Edmund Tan and Cindior Ho. It advises progressing Singaporean families on The Second Property Ladder™ — the safe, step-by-step way to turn a first property into higher net asset value and more options." |
| **Primary URL** | `thereimethod.com` (homepage = the Organization entity's canonical URL) |
| **SameAs** | facebook.com/coachedmundtan · instagram.com/propertycoachedmundtan · youtube.com/@singaporerealestateinsider · GBP [VERIFY] · LinkedIn company page [OPEN] |
| **Supporting pages** | Category hub; About; both founder pages; Blueprint offer page; guides; FAQ; contact |
| **Proof assets** | Founder portfolio; $160M collectively invested / 100+ buyers guided / 90% disqualification [VERIFY all]; GBP reviews; YouTube channel |
| **Schema.org type** | `Organization` + `ProfessionalService` (multi-type). NOT `LocalBusiness` at org level — see Entity 8 for the GBP local node. Include `founder` ×2, `sameAs`, `areaServed` Singapore, `knowsAbout`, `memberOf` PropNex [VERIFY] |
| **Internal link targets** | Root of the graph; ← every page's publisher/`about`; → founders (`founder`); → category (`owns`/`about`); → media (`subOrganization` or `sameAs`) |
| **Priority** | **P0** |

### Entity 4 — Category / Method: The Second Property Ladder™ (+ Exit Before Entry™)

| Field | Value |
|---|---|
| **Official name** | The Second Property Ladder™ |
| **Sub-concept** | Exit Before Entry™ (the category law, elevated from Step 4) |
| **Aliases / historical tokens** | "Second Property Ladder"; "SPL" (internal only, never public); **New Launch Ladder™** (subordinate campaign mechanism — see Entity 6, NOT an alias of the category) |
| **Canonical description** | "The Second Property Ladder™ is a step-by-step framework for Singaporean property owners to move safely from their first serious property to higher net asset value — mapping the numbers, sequencing the moves, and researching the exit before entry. Created by The REI Method." |
| **Exit Before Entry™ description** | "Exit Before Entry™ is the category law of The Second Property Ladder™: no property move is safe until the exit buyer, exit timing, downside buffer, and next-move impact are understood before committing." |
| **Primary URL** | `thereimethod.com/second-property-ladder` (category hub / pillar) |
| **SameAs** | Not applicable (a proprietary method, not a cross-platform profile). Reinforce via consistent naming + `about`/`mainEntity` references, not `sameAs`. |
| **Supporting pages** | 5-Step cluster pages (Position Map, Direction Statement, Move Sequence, Selection Research, Climb Cadence); Exit Before Entry™ pillar; One-Property Trap pillar; FAQ |
| **Proof assets** | Case studies mapped to the 7 proof categories; founder journey; diagnostic results data |
| **Schema.org type** | No native "Method"/"Framework" type in Schema.org. Represent the hub page as `Article`/`WebPage` with `about` → a `DefinedTerm` (name "The Second Property Ladder™", `inDefinedTermSet` The REI Method glossary) and `FAQPage` for the definitional Q&As. **Do NOT use `HowTo`** — Google retired HowTo rich results (Aug 2023); the markup no longer earns rich display, though a light `HowTo`/step description in body copy still aids entity understanding. Prefer `Article` + `DefinedTerm` + `FAQPage`. |
| **Internal link targets** | ← homepage (`owns`); ← all 6 content pillars; ← diagnostic bridge page (`about`); → founders (`creator`) |
| **Priority** | **P0** |

### Entity 5 — Offers: Position Map session · The Second Property Ladder Blueprint™

| Field | Value |
|---|---|
| **Official names** | Position Map session (free, 45 min, single universal CTA); The Second Property Ladder Blueprint™ (paid advisory) |
| **Aliases / historical tokens** | "Next Move Strategy Session™" / "Strategic Property Clarity Session™" (CategoryKing — superseded by Position Map session); "New Launch Strategy Call" (Legacy Launch funnel — campaign-specific variant, keep scoped to that campaign) |
| **Canonical description (Position Map session)** | "The Position Map session is a free 45-minute session with The REI Method where a Singaporean property owner maps their real numbers — defendable value, nett proceeds, CPF, and loan capacity — the first step of The Second Property Ladder™." |
| **Canonical description (Blueprint™)** | "The Second Property Ladder Blueprint™ is The REI Method's paid advisory engagement delivering a Position Map, Direction Statement, Move Sequence, Selection Research (Exit Before Entry™), and Climb Cadence." |
| **Primary URL** | `thereimethod.com/position-map-session` · `thereimethod.com/blueprint` |
| **SameAs** | N/A |
| **Supporting pages** | Category hub; both offer pages cross-link; FAQ (price/duration once confirmed) |
| **Proof assets** | Session outcome testimonials [collect]; "you leave with your numbers" promise [VERIFY 45-min] |
| **Schema.org type** | `Service` (with `provider` → The REI Method, `areaServed` Singapore, `serviceType`). **No `Offer`/price schema** until price confirmed and shown on-page (D8: no schema for content not on page). Do not use `Event` (not scheduled/dated). |
| **Internal link targets** | ← category hub; ← every guide CTA; ← diagnostic result; → The REI Method (`provider`) |
| **Priority** | **P1** |

### Entity 6 — Campaign entities: Legacy Launch (+ New Launch Ladder™) · Which Step Are You On? diagnostic

| Field | Value |
|---|---|
| **Official names** | Legacy Launch (new-launch campaign line); New Launch Ladder™ (subordinate mechanism = the new-launch application of The Second Property Ladder™, teaching Steps 3–4); Which Step of The Second Property Ladder Are You On? (14-question diagnostic / lead magnet) |
| **Aliases / historical tokens** | "New Launch Ladder™" appears as primary IP across the live funnel + 33 reels (D5 conflict — bridge, do not big-bang rename); "Which Step Are You On?™"; diagnostic CTAs "Start the Climb" / "Reveal My Step!" |
| **Canonical description (Legacy Launch)** | "Legacy Launch is The REI Method's new-launch campaign that applies The Second Property Ladder™ to new-launch buying — sequencing the move and researching the exit before entry, so buyers choose a launch they can actually exit." |
| **Canonical description (diagnostic)** | "'Which Step of The Second Property Ladder Are You On?' is a free 14-question diagnostic from The REI Method that identifies which of the five steps a Singaporean property owner is on and what to do next." |
| **Primary URL** | Diagnostic on `secondpropertyladder.com` (funnel steps noindexed; one indexable bridge page canonical → category hub, D3). Legacy Launch V2 on `legacylaunch.com.sg` (attach domain now; noindex + bridge, D3). |
| **SameAs** | N/A (campaign assets, not profiles) |
| **Supporting pages** | Bridge pages canonical to `thereimethod.com`; footers link authority domain + founder pages |
| **Proof assets** | Funnel trust stats [VERIFY all]; 33 reel library; disqualification checklist (build) |
| **Schema.org type** | Bridge pages: `WebPage` + `FAQPage` where genuine Q&A on page. Diagnostic itself: no rich-result schema (interactive quiz, funnel noindexed). New Launch Ladder™: reference as a `DefinedTerm` subordinate to the category `DefinedTermSet` — reinforces "application of SPL", not a rival category. |
| **Internal link targets** | Bridge pages → category hub (`about`, canonical) + founders; → Position Map session |
| **Priority** | **P1** (Legacy Launch is live-revenue; diagnostic is P1 build) |

### Entity 7 — Media: Singapore Real Estate Insider (YouTube channel)

| Field | Value |
|---|---|
| **Official name** | Singapore Real Estate Insider |
| **Scope** | **Media property ONLY** — the YouTube channel/show. NOT the business name going forward, despite the current funnel © footer (D1). |
| **Aliases / historical tokens** | Current funnel footer "© Singapore Real Estate Insider" (correct as media credit, wrong as legal entity); `singaporerealestateinsider.com` (301 → thereimethod.com, D4) |
| **Canonical description** | "Singapore Real Estate Insider is the YouTube channel of The REI Method, hosted by Coach Edmund Tan and Cindior Ho, publishing Singapore property education built on The Second Property Ladder™." |
| **Primary URL** | youtube.com/@singaporerealestateinsider (canonical home is the channel itself; `singaporerealestateinsider.com` redirects to authority domain) |
| **SameAs** | Links back to The REI Method org + founder pages |
| **Supporting pages** | Individual `VideoObject` embeds on relevant `thereimethod.com` guides; channel "About" must name Edmund, Cindior, The REI Method, The Second Property Ladder™ (D6) |
| **Proof assets** | 600+ videos, 2,000+ subscribers [VERIFY both] |
| **Schema.org type** | `Organization`/`WebPage` for channel reference; `VideoObject` for each embedded video on-page (with `publisher` → The REI Method, `creator` → Edmund Tan). Video schema IS Google-eligible when the video is embedded/on-page. |
| **Internal link targets** | ↔ The REI Method (`sameAs` for the same-named org OR `subOrganization`); embedded videos → guide pages |
| **Priority** | **P1** |

### Entity 8 — Local business (Google Business Profile)

| Field | Value |
|---|---|
| **Official name** | The REI Method (GBP listing name must match — see §7 disambiguation) [VERIFY current listing name] |
| **Aliases / historical tokens** | Current GBP behind share.google/bpyWTGgjlyNxt8Xiz [VERIFY name/category/reviews]; GHL address Singapore 338520 |
| **Canonical description** | Same as Entity 3 canonical, trimmed to GBP's business-description limit; lead with "Singapore property advisory". |
| **Primary URL** | Website field → `thereimethod.com` (currently blank in GHL — set it) |
| **NAP** | Name: The REI Method · Address: [VERIFY — GHL shows #17-23, Singapore 338520] · Phone: +65 8786 3931 · Email: admin@thereimethod.com |
| **SameAs** | GBP is itself a `sameAs` target for the Person and Organization entities; its own profile links to website + social |
| **Proof assets** | Google reviews (Entity 9); posts; photos |
| **Schema.org type** | On the homepage/contact page, `ProfessionalService` (a `LocalBusiness` subtype) with `address` (PostalAddress), `telephone`, `areaServed` Singapore, `sameAs` → GBP. Matches GBP category. |
| **Internal link targets** | Contact page ↔ GBP; homepage `sameAs` |
| **Priority** | **P0** (GBP is the strongest local entity signal Google has; blocked on [VERIFY]) |

### Entity 9 — Review / proof entities

| Field | Value |
|---|---|
| **Official name** | Reviews & testimonials for The REI Method / Coach Edmund Tan |
| **Sources** | Google reviews (via GBP); on-site testimonials; case studies (7 proof categories); founder portfolio proof |
| **Canonical description** | N/A (proof, not a named entity — feeds trust signals into Entities 1–3) |
| **Primary URL** | `thereimethod.com/reviews` or testimonial blocks on offer/category pages |
| **Schema.org type** | `Review` / `AggregateRating` — **only** on first-party content genuinely displayed on-page, attached to the `Organization`/`Service`/`Person` it concerns. Follow **Google Search Central — Review snippet structured data**: self-serving `AggregateRating` (business reviewing itself) is **not eligible** for review rich results; Google reviews live on the GBP, not marked up on your own site. Use `Review` markup only for genuine third-party testimonials you host, with real author names and consent. No fake/incentivised reviews (D8). |
| **Internal link targets** | Testimonials → offer pages, founder pages, category hub |
| **Priority** | **P1** |

### Entity 10 — QUARANTINED: Changi Green

| Field | Value |
|---|---|
| **Official name** | Changi Green |
| **Nature** | Separate business line — co-living / room-rental / tenant management (180+ `cg_*` GHL fields, "Changi Green-Tenant Cycle" pipeline). Shares the GHL sub-account only. |
| **Ruling** | **HARD QUARANTINE.** Changi Green must NEVER appear in the advisory entity graph: not in any `sameAs`, `founder`, `subOrganization`, `owns`, internal link, shared phone/address on a public advisory page, or shared GBP. Recommend a **separate GHL sub-account** and separate domain/GBP if it needs public presence. |
| **Risk if breached** | A shared NAP or cross-link would teach Google that The REI Method = a room-rental operation, diluting the property-advisory entity and confusing AI answers. |
| **Schema.org type** | None within this project. Documented here **only** to define the boundary. |
| **Priority** | **P0 (as a guardrail)** — enforce separation before any public NAP/GBP work goes live. |

---

## 2. Entity Relationship Diagram (text)

Edge labels map directly to Schema.org properties.

```
The REI Method  [Organization + ProfessionalService]  ← ROOT
│
├─(founder)──────────────▶ Edmund Tan (Coach Edmund Tan) [Person]
│                            └─(worksFor)──────▶ The REI Method
│                            └─(colleague)─────▶ Cindior Ho
│                            └─(sameAs)────────▶ FB / IG / YouTube / GBP / LinkedIn
│
├─(founder)──────────────▶ Cindior Ho [Person]
│                            └─(worksFor)──────▶ The REI Method
│                            └─(colleague)─────▶ Edmund Tan
│
├─(owns / about)─────────▶ The Second Property Ladder™ [DefinedTerm / Method]
│                            ├─(hasPart / termCode)▶ Exit Before Entry™ [DefinedTerm — category law]
│                            ├─(creator)───────▶ Edmund Tan + Cindior Ho
│                            └─(hasPart)───────▶ 5 Steps: Position Map · Direction Statement ·
│                                                Move Sequence · Selection Research · Climb Cadence
│
├─(makesOffer / provider)▶ Position Map session [Service, free]
├─(makesOffer / provider)▶ The Second Property Ladder Blueprint™ [Service, paid]
│                            └─(isRelatedTo)───▶ The Second Property Ladder™
│
├─(subOrganization / sameAs)▶ Singapore Real Estate Insider [Media — YouTube channel]
│                            └─(publisher of)──▶ VideoObject ×N  (embedded on thereimethod.com)
│
├─(subjectOf / campaign)─▶ Legacy Launch [Campaign]
│                            └─(about)─────────▶ New Launch Ladder™ [DefinedTerm ⊂ SPL, Steps 3–4]
│
├─(subjectOf)────────────▶ "Which Step Are You On?" diagnostic [Lead magnet]
│                            └─(about)─────────▶ The Second Property Ladder™  (canonical → hub)
│
├─(hasPOS / sameAs)──────▶ Google Business Profile [LocalBusiness node]  ── NAP anchor
│                            └─(review)────────▶ Reviews / AggregateRating [Google-hosted]
│
└─(review / subjectOf)───▶ On-site testimonials & case studies [Review]

╔═══════════════════════════════════════════════════════════╗
║  Changi Green  [SEPARATE ENTITY]  ── NO EDGE TO ANY NODE   ║
║  Shares GHL sub-account only. Zero graph connection.       ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 3. SameAs Link Map

| Entity | Platform | URL | Status |
|---|---|---|---|
| The REI Method / Edmund Tan | Facebook | facebook.com/coachedmundtan | **Live** |
| The REI Method / Edmund Tan | Instagram | instagram.com/propertycoachedmundtan | **Live** — rename-pending → `coachedmundtan` if available (D6) [OPEN] |
| The REI Method / SRE Insider | YouTube | youtube.com/@singaporerealestateinsider | **Live** — About section needs founder + REI Method + SPL naming (D6) |
| The REI Method (local) | Google Business Profile | share.google/bpyWTGgjlyNxt8Xiz | **Live** [VERIFY name/category/reviews] |
| The REI Method | Website (authority) | thereimethod.com | [VERIFY live/has content] |
| The REI Method | LinkedIn company page | — | **Missing** [OPEN — create] |
| Edmund Tan | LinkedIn (personal) | — | **Missing** [OPEN — create/confirm] |
| Cindior Ho | LinkedIn (personal) | — | **Missing** [OPEN — confirm existence] |
| Cindior Ho | Instagram (personal) | — | **Missing / unknown** [OPEN] |
| Singapore Real Estate Insider | Website | singaporerealestateinsider.com | **Live → 301 to thereimethod.com** (D4) |
| — | 6figurepropertyprofits.com | — | **Retire → 301 to thereimethod.com** (D4); never a `sameAs` |
| Changi Green | (any) | — | **QUARANTINED — never listed as sameAs of advisory entities** |

**Rule:** every entity's `sameAs` array must be *reciprocal* — the profile bio/description on each platform links back to `thereimethod.com`. Non-reciprocal `sameAs` are weaker entity signals.

---

## 4. Schema Recommendation Map

| Page | JSON-LD type(s) | Key properties | Notes |
|---|---|---|---|
| `thereimethod.com` (home) | `Organization` + `ProfessionalService` | name, url, logo, description, founder ×2, sameAs, areaServed, telephone, address, memberOf PropNex [VERIFY] | Single org node; `@id` = `#organization` reused site-wide as publisher |
| `/about/edmund-tan` | `Person` | name, alternateName, jobTitle, worksFor(@id org), knowsAbout, sameAs, image | See full block §6 |
| `/about/cindior-ho` | `Person` | mirror of Edmund; sameAs limited until profiles exist | Publish once ≥1 real `sameAs` confirmed |
| `/second-property-ladder` (hub) | `Article` + `DefinedTerm` + `FAQPage` | about → DefinedTerm SPL; author ×2; publisher; FAQ mainEntity | **No `HowTo` rich result** (Google retired it Aug 2023); steps as body + `DefinedTerm` set |
| Each 5-Step page | `Article` + `DefinedTerm` | isPartOf hub; about → step term; author | Step term `inDefinedTermSet` SPL glossary |
| `/position-map-session` | `Service` | provider(@id org), serviceType, areaServed | No `Offer`/price until shown on-page |
| `/blueprint` | `Service` | provider, serviceType, isRelatedTo SPL | Add `Offer` only when price is public |
| `/reviews` + testimonial blocks | `Review` (third-party only) | itemReviewed(@id org/person), author, reviewBody, reviewRating | No self-serving `AggregateRating` rich result (Google Search Central) |
| Guide pages w/ embedded video | `Article` + `VideoObject` | video: name, description, thumbnailUrl, uploadDate, contentUrl/embedUrl, publisher | VideoObject eligible when embedded on-page |
| `secondpropertyladder.com` bridge | `WebPage` + `FAQPage` | canonical → hub; about SPL | Funnel steps `noindex`; bridge indexable (D3) |
| `legacylaunch.com.sg` bridge | `WebPage` + `FAQPage` | canonical → hub; about Legacy Launch / NLL ⊂ SPL | Same noindex/bridge rule; add CEA compliance block |
| Contact page | `ProfessionalService` (LocalBusiness) | address, telephone, openingHours, sameAs GBP | Must match GBP NAP exactly |

**Eligibility discipline (D8 / Google Search Central):** mark up only content visible on the page; `FAQPage` rich results are currently limited by Google to authoritative government/health sites for *display*, but the markup still aids entity/answer understanding — keep it accurate and on-page. `Review`, `VideoObject`, `Organization`, `Person`, `Service` are all supported/understood; `HowTo` display is retired.

---

## 5. Platform Consistency Checklist (NAP + signal alignment)

Every platform must show the **same** name, description root, and back-link so all signals agree.

| Platform | Name / handle | Bio / description line (root) | Website link | Must fix |
|---|---|---|---|---|
| Website (thereimethod.com) | The REI Method | "Singapore property advisory · The Second Property Ladder™ · Coach Edmund Tan & Cindior Ho" | — | Confirm live + content [VERIFY] |
| Facebook | Coach Edmund Tan / @coachedmundtan | "Singapore property advisor · Co-founder, The REI Method · The Second Property Ladder™" | thereimethod.com | Add REI Method + SPL to bio; link site |
| Instagram | Property Coach Edmund Tan / @propertycoachedmundtan → @coachedmundtan [OPEN] | Same root line | thereimethod.com | Rename handle if available; align bio |
| YouTube | Singapore Real Estate Insider / @singaporerealestateinsider | "The YouTube channel of The REI Method · Hosted by Coach Edmund Tan & Cindior Ho · The Second Property Ladder™" | thereimethod.com | Rewrite About; add founder names + SPL (D6) |
| Google Business Profile | The REI Method | "Singapore property advisory. We advise families on The Second Property Ladder™ — the safe way to climb from one property to more options." | thereimethod.com | Set website field; verify name/category = advisory [VERIFY] |
| LinkedIn (company) | The REI Method | Same as GBP root | thereimethod.com | Create [OPEN] |
| LinkedIn (Edmund) | Edmund Tan | "Co-founder, The REI Method · Creator of The Second Property Ladder™ · PropNex [VERIFY]" | thereimethod.com | Create/confirm [OPEN] |
| LinkedIn (Cindior) | Cindior Ho | "Co-founder, The REI Method · The Second Property Ladder™ · PropNex [VERIFY]" | thereimethod.com | Confirm/create [OPEN] |
| GHL sub-account | (internal) "Coach Edmund & Cindior" | — | set website = thereimethod.com | Fix timezone Asia/Kuala_Lumpur → Asia/Singapore; fill blank website field |

**NAP consistency (identical byte-for-byte on every public advisory surface):**
- **Name:** The REI Method
- **Address:** [VERIFY exact registered address — GHL shows "#17-23, Singapore 338520"; confirm this is a public business address before publishing]
- **Phone:** +65 8786 3931
- **Email:** admin@thereimethod.com

Any deviation (e.g. "REI Method" vs "The REI Method", a second phone number, a Changi Green address) weakens the local entity and risks conflation.

---

## 6. Complete JSON-LD Examples

### 6a. Edmund Tan — Person

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://thereimethod.com/edmund-tan#person",
  "name": "Edmund Tan",
  "alternateName": "Coach Edmund Tan",
  "jobTitle": "Co-founder & Property Advisor",
  "description": "Coach Edmund Tan is a Singapore property advisor and co-founder of The REI Method. He created The Second Property Ladder™, a step-by-step framework that helps Singaporean property owners climb from their first serious property to higher net asset value.",
  "url": "https://thereimethod.com/edmund-tan",
  "image": "https://thereimethod.com/img/edmund-tan.jpg",
  "worksFor": { "@id": "https://thereimethod.com/#organization" },
  "colleague": { "@id": "https://thereimethod.com/cindior-ho#person" },
  "knowsAbout": [
    "Singapore property advisory",
    "The Second Property Ladder™",
    "Exit Before Entry™",
    "Net asset value planning",
    "Property upgrading (HDB, EC, private)"
  ],
  "worksFor_note_VERIFY": "CEA registration number and PropNex licence required before publish",
  "sameAs": [
    "https://www.facebook.com/coachedmundtan",
    "https://www.instagram.com/propertycoachedmundtan",
    "https://www.youtube.com/@singaporerealestateinsider"
  ]
}
```
*Add GBP and LinkedIn URLs to `sameAs` once [VERIFY]/[OPEN] resolve. Replace `knowsAbout` credential once CEA no. confirmed — consider adding `hasCredential` (`EducationalOccupationalCredential`) with the CEA registration [VERIFY].*

### 6b. The REI Method — Organization / ProfessionalService

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "ProfessionalService"],
  "@id": "https://thereimethod.com/#organization",
  "name": "The REI Method",
  "description": "The REI Method is a Singapore property advisory founded by Coach Edmund Tan and Cindior Ho. It advises progressing Singaporean families on The Second Property Ladder™ — the safe, step-by-step way to turn a first property into higher net asset value and more options.",
  "url": "https://thereimethod.com",
  "logo": "https://thereimethod.com/img/rei-method-logo.png",
  "founder": [
    { "@id": "https://thereimethod.com/edmund-tan#person" },
    { "@id": "https://thereimethod.com/cindior-ho#person" }
  ],
  "areaServed": { "@type": "Country", "name": "Singapore" },
  "knowsAbout": [
    "The Second Property Ladder™",
    "Exit Before Entry™",
    "Singapore second property planning"
  ],
  "memberOf": {
    "@type": "Organization",
    "name": "PropNex",
    "description": "VERIFY: both founders are CEA-registered salespersons under PropNex; add estate agent licence no."
  },
  "telephone": "+65 8786 3931",
  "email": "admin@thereimethod.com",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "SG",
    "addressLocality": "Singapore",
    "postalCode": "338520",
    "streetAddress": "VERIFY exact registered address"
  },
  "sameAs": [
    "https://www.facebook.com/coachedmundtan",
    "https://www.instagram.com/propertycoachedmundtan",
    "https://www.youtube.com/@singaporerealestateinsider"
  ]
}
```
*`memberOf` PropNex and the CEA registration numbers are [VERIFY] — required on public advertising under CEA guidelines (D7). Do not publish the address unless it is a genuine, public business address (not a residence, and never a Changi Green address).*

---

## 7. Disambiguation Plan

Three conflation risks. Each needs active, repeated signal — Google resolves entities by consistent co-occurrence, not a one-time declaration.

**Risk A — Singapore Real Estate Insider (media) vs The REI Method (business).**
The live funnel footer says "© Singapore Real Estate Insider", which currently *is* the strongest entity token in the copy — teaching machines the business is called that. Mitigations:
1. Every public surface names the business **The REI Method** first; Singapore Real Estate Insider is described only as "the YouTube channel of The REI Method" (never the copyright holder of the advisory).
2. Change funnel footers to "© The REI Method" (schedule with the D5 light-touch bridge pass; do not big-bang).
3. In schema, model the channel as `subOrganization`/`sameAs` of the org, with `publisher` on every `VideoObject` = The REI Method. Same-name reciprocity everywhere.

**Risk B — Legacy Launch / New Launch Ladder™ vs the master category.**
The 33 reels + live funnel make New Launch Ladder™ look like a standalone method. Mitigations:
1. Always frame New Launch Ladder™ as "the new-launch application of The Second Property Ladder™" — a `DefinedTerm` *inside* the SPL `DefinedTermSet`, never its own category page.
2. New assets use SPL vocabulary from day one; Legacy Launch V2 gets a single bridge line (D5). Bridge pages canonical → category hub.
3. Never give New Launch Ladder™ its own `Organization`/`Service` root or its own `sameAs`.

**Risk C — "REI" collides with REI (Recreational Equipment, Inc.), the large US outdoor retailer.**
Bare "REI" will pull the graph toward the American co-op. Mitigations:
1. **Always write "The REI Method" in full.** Ban bare "REI" in all public copy, handles, alt text, and meta. (Internal shorthand only.)
2. **Force Singapore-property co-occurrence:** every canonical description pairs "The REI Method" with "Singapore", "property", and at least one founder name — the disambiguating context Google/AI need.
3. **Anchor on the founders + method:** because the two Person entities and The Second Property Ladder™ are unique tokens with no US-retailer overlap, they pull "The REI Method" firmly into the Singapore-property cluster. Cross-link The REI Method ↔ founders ↔ SPL relentlessly.
4. `areaServed` Singapore + `.com` on a Singapore-advisory site + GBP in Singapore all reinforce geo separation.
5. Never use outdoor/recreation/equipment language anywhere near the brand.

---

## Questions To Clarify

1. **CEA registration numbers + exact registered names** for Edmund and Cindior, and **PropNex licence number** — blocks all Person/Organization schema publish and every public advertising compliance block (D7).
2. **GBP behind share.google/bpyWTGgjlyNxt8Xiz** — exact listing name, primary category, address visibility, review count. Determines whether the local node already says "The REI Method" or something else that needs correcting.
3. **Is `thereimethod.com` live with content?** No schema can ship until the authority domain hosts the pages it describes.
4. **Cindior Ho's public profiles** — does she have any LinkedIn/Instagram today? Entity 2 currently has zero confirmable `sameAs`, which weakens her Person node and stalls dual-founder parity.
5. **Registered business address** — is "#17-23, Singapore 338520" a public business address safe to publish in NAP/schema, and is it shared with Changi Green (quarantine risk)?
6. **LinkedIn** — approval to create company page + two personal pages (largest missing `sameAs` gap).

## Dependencies

- **Blocks / blocked by 03_DOMAIN_ARCHITECTURE.md** — the 301s (singaporerealestateinsider.com, 6figurepropertyprofits.com) and canonical/bridge rules must land before `sameAs` and canonicals are trustworthy.
- **Feeds 04_WEBSITE_SITEMAP** — every Primary URL here must exist as a real page before its schema publishes (D8).
- **Feeds 07_SOCIAL_PROFILE_REPOSITIONING** — the Platform Consistency Checklist (§5) is the source for bio/handle updates.
- **Feeds 08_GOOGLE_BUSINESS_PROFILE_PLAN** — Entity 8 NAP + category are inputs.
- **Feeds 09_PROOF_LIBRARY** — Entity 9 review/testimonial schema depends on collected, consented proof.
- **Gated by CEA [VERIFY]** — Person/Organization schema and any public NAP wait on Q1.

## First 5 Actions

1. **Obtain CEA registration numbers, registered names, and PropNex licence no.** (Q1) — unblocks all identity schema and compliance blocks.
2. **Audit the GBP** (Q2): confirm/rename listing to "The REI Method", set primary category to a property-advisory category, set website field = `thereimethod.com`, and confirm it shares no NAP with Changi Green.
3. **Stand up the two founder pages** (`/about/edmund-tan`, `/about/cindior-ho`) and the category hub on `thereimethod.com`, then attach the §6 JSON-LD (with [VERIFY] placeholders held until Q1).
4. **Fix the entity-fragmentation signals:** change funnel footers toward "© The REI Method", rewrite the YouTube About to name both founders + The REI Method + The Second Property Ladder™ (D6).
5. **Lock the Changi Green quarantine:** confirm a separate GHL sub-account plan and verify no shared public NAP/GBP before any local-entity work goes live.

---

## Concerns (flagged, not silently changed)

- **"This is advisory, not agency."** remains in the live funnel and is a CEA compliance risk while both founders operate as licensed PropNex salespersons (D7). Recommend the brief's replacement — "Advisory-first. We plan the sequence before any transaction." — but this is a PropNex-compliance decision, not an entity-architecture one; flagging for that review.
- **Cindior Ho has no confirmable public presence.** Dual-founder parity (D1) is an entity goal the current asset base cannot yet support. Her Person node will be thin until she has at least one live, reciprocal `sameAs`. If she prefers a low profile (D6 [OPEN]), reconsider whether the schema should present true co-equal founders or Edmund-primary with Cindior as co-founder — a strategy call for the orchestrator.
- **All trust stats and portfolio figures** ($160,014,029; 100+ buyers; 90% disqualification; NAV $6.6M→$9M; Tre Ver / Parc Clematis figures) are [VERIFY] and must not enter any schema `description`, review, or on-page proof until confirmed against records (D7).
- **GHL timezone** is set to Asia/Kuala_Lumpur; should be Asia/Singapore — minor but affects any date-stamped/event signals.
