# 09 — PROOF LIBRARY SYSTEM
**Owner:** Sonnet agent (Phase 9) · **Companion:** `Proof_Library_Inventory.csv` (52 rows) · **Status:** LOCKED structure, [OPEN/VERIFY] content

## Executive Summary

The REI Method has plenty of proof *material* and almost no proof *assets*. The founder journey, the claims bank, and four named client stories exist only as unverified fragments in reel scripts and funnel copy — not one dollar figure has been checked against a record, not one client has signed a consent form, and zero on-site reviews exist despite a live GBP listing. Meanwhile the market-research proof (EDMW, Stacked Homes, ERA) is in the best shape in the library: it was genuinely read and verified on 8 July 2026 and is citable today with a method note.

This file classifies all 52 known proof fragments into 10 types, builds the case-study production system (10-part template, consent/anonymisation rules, schema-eligibility guidance), and generates the forward pipeline: 20 case-study page ideas, 20 review-collection prompts, 10 founder authority angles, and 10 market-research proof pages. It closes with a Compliance-Safe Claims Guide that fixes the entity-name mismatch in the live disclaimer/PDPA copy and sets the verification standard for the two highest-exposure numbers in the business — $160,014,029 collectively invested and 100+ buyers guided.

The single biggest risk in this library: three of the seven proof categories (Strategy Over Comfort, One Stronger Asset Before Two, Exit Before Entry) have **no client story at all** — not even a name. Two of those are the category's own spine (Exit Before Entry is the category law) and its hardest sell (One Stronger Asset Before Two argues against the intuitive "just buy a second one" instinct). Building proof for these two is a higher priority than polishing the four stories that already have names attached.

---

## 1. Proof Inventory

Full inventory of 52 assets is in `Proof_Library_Inventory.csv`. Summary by type:

| Type | Count | Confidence state | Consent required |
|---|---|---|---|
| Founder proof | 7 | Mostly INFERRED (verbal, not record-checked) | Only where a named family co-owner appears |
| Portfolio proof | 6 | INFERRED (reel/funnel copy, no source ledger) | No (aggregate/founder-only figures) |
| Client proof | 4 | UNTESTED (first names only, no figures on file) | Yes, all four |
| Case study | 7 | 4 INFERRED (draftable once client proof is verified), 3 GAP (no client at all) | Yes, all seven |
| Review | 5 (of 20 full list, §4) | UNTESTED (zero collected) | Yes, all |
| Media proof | 3 | 1 INFERRED, 1 UNTESTED, 1 GAP | No |
| Market research proof | 6 | 5 VERIFIED, 1 INFERRED (regulatory figures need re-pull) | No (public data, aggregated) |
| Process proof | 6 | 4 PROVEN (locked artefact formats), 2 INFERRED (unbuilt/unverified) | Yes, wherever a real client file is the source |
| Framework proof | 4 | PROVEN (internal IP decisions, not external claims) | No |
| Authority proof | 4 | 1 BLOCKING UNTESTED (CEA reg. numbers), 2 INFERRED, 1 GAP | No |

**PDPA / consent checklist — apply before publishing any client-identifying asset (client proof, case study, review):**

1. Written consent obtained (signed form or dated email), specifying: what will be published (story, figures, name format, photo/video), where (which pages/funnels/social channels), and for how long.
2. Anonymisation level agreed with the client (first name only / composite pseudonym / full name) — default to first-name-plus-context (e.g., "Edward & Rose, a private-property couple") unless the client explicitly permits more.
3. Dollar figures agreed as exact, rounded, or range-only — a client can consent to the story but decline exact numbers.
4. No property address, block, or unit-stack identifiers that would make the client locatable.
5. Right to withdraw consent and have the asset taken down — state a process and timeframe (recommend 5 business days).
6. Consent is asset-specific and channel-specific — a client agreeing to an on-site case study has not automatically agreed to paid social use of the same story; get both if both are wanted.
7. Store signed consent centrally (recommend a GHL custom field set, e.g. `proof_consent_signed`, `proof_consent_date`, `proof_consent_scope`) so consent status is queryable, not buried in email.
8. DNC/PDPA marketing consent (already on forms) is separate from proof-use consent — do not conflate the two.

None of the four named client stories (Edward & Rose, MoK & Jine, Win/Esther & Family, Lynn) currently has consent on file. Treat all four as **not cleared to publish** until this checklist is run.

---

## 2. Case Study Template

### 2.1 The 10-part narrative structure

Every case study, regardless of category, follows this order. This is the story spine, not the page's visual layout — the page can compress parts visually (e.g., situation + hidden risk in one intro block) but must not skip a part.

| # | Part | What it contains | Vocabulary discipline |
|---|---|---|---|
| 1 | **Client situation** | Who they were before: one property, a rough NAV picture, no plan for the next move. Buyer sub-type named (progressing family / DINK couple / single climbing, etc.) | Use "Property Climber," never "homeowner" |
| 2 | **Hidden risk** | The thing they didn't know was a risk: trapped equity, a policy-clock deadline (MOP/SSD/ABSD timing), an exit buyer pool that didn't exist for their target unit type | Name the specific villain (Buy-To-Stay Thinking, The Just-Buy-Second Myth, etc.) where it fits |
| 3 | **Wrong path almost taken** | The default move they were about to make before engaging — usually the intuitive, comfortable, or agent-suggested option | Frame as "the path most buyers take," not as criticism of any named agent/agency |
| 4 | **Framework/Step used** | Which of the 5 Steps did the work — name it explicitly (Position Map / Direction Statement / Move Sequence / Selection Research / Climb Cadence) | Always name the Step and its artefact |
| 5 | **Options rejected** | What alternatives were mapped and why they were rejected (Trade-Up Path vs. Hold-Two Path, a specific project ruled out by Selection Research) | Show the rejection reasoning — this is what proves rigor, not the eventual choice |
| 6 | **Decision made** | The actual Move Sequence chosen and why it fit their age/loan/income/tenure/time position | Tie back to "the order is the product" |
| 7 | **Risk control** | What Exit Before Entry™ specifically de-risked (exit buyer confirmed, downside buffer sized, next-move impact modelled) before they committed | This is the compliance-safe part — frame as risk management, not return prediction |
8 | **Result** | What changed — NAV, options, timeline. State as a range or "individual result" unless a document backs the exact figure (see §7) | Never state as a typical or guaranteed outcome |
9 | **Lesson** | The one-sentence takeaway a reader in the same position should act on | Should double as a pull-quote / meta description candidate |
10 | **CTA** | Single universal CTA: Position Map session | Never a secondary/competing CTA on a proof page |

### 2.2 On-page requirements

- **Anonymisation rules:** default to first name + relationship context (per §1 consent checklist). No addresses, no unit-stack numbers, no employer names, no photos without separate image consent. If a client requests full anonymity, use a composite pseudonym and disclose this in a footnote ("Names changed at the client's request; figures and sequence are unchanged").
- **[VERIFY] gate:** a case study may not go live until (a) written consent is on file, and (b) at least one core figure is corroborated against a document the client or founder can point to (Option to Purchase, valuation report, CPF statement, resale contract). If no document corroboration exists yet, the page must carry rounded ranges only and the phrase "individual results — illustrative" in the result section, never a bare exact figure.
- **Review/FAQ schema eligibility:** case studies are first-party narrative content the business is telling about itself — they are **not eligible for `Review`/`AggregateRating` rich results**, and must not be marked up as such. This matches Google Search Central's Review snippet structured-data guidance: a business narrating its own client outcomes is self-serving content, not a third-party review, regardless of how genuine the underlying story is. Reserve `Review` markup exclusively for genuine third-party testimonials collected under §4. A case study page **may** carry `FAQPage` schema if it contains genuine, on-page Q&A (e.g., "Was this a real client?", "How is this figure verified?", "Does this apply to my situation?") — do not add `FAQPage` markup unless that Q&A content is actually visible on the page (D8: no schema for content that doesn't exist on-page). Recommended schema: `Article` with `about` → the relevant `DefinedTerm` (the Step or category demonstrated) and `mentions` → the category hub.
- **Video version spec:** two cuts per case study, both in the private-wealth-advisory creative direction already established for Legacy Launch V2 (deep navy/charcoal + ivory + champagne gold, serif display headlines, no red urgency bars, editorial pacing):
  - **Short cut (60–90 sec, vertical 9:16):** for Instagram/Facebook Reels — follows the existing 3-level reel-script format (problem/solution/product aware), narrated points 2–3–8–10 only (hidden risk → wrong path → result → CTA), captioned for sound-off viewing.
  - **Long cut (4–6 min, horizontal 16:9):** for YouTube — walks all 10 parts, includes an on-screen Move Sequence or Position Map artefact graphic (redacted), ends on the single CTA.
  - Both cuts require the same consent scope check as the written page (§1, point 6) — video consent is not implied by written-page consent.

---

## 3. 20 Case Study Page Ideas

Items 1–7 map to known raw material or explicit gaps in the 7 proof categories (see CSV rows PL-018 to PL-024). Items 8–20 are sourcing targets — patterns worth finding in the CRM (1-To-1 Pipeline Won-stage contacts; searchable via GHL fields `what_do_you_currently_own`, `next_budget`, `decision_timing`, `family_aligned`, `biggest_worry`) rather than stories that exist yet.

| # | Working title | Category | Step demonstrated | Target cluster/keyword | Status |
|---|---|---|---|---|---|
| 1 | "The Exit That Unlocked Edward & Rose's Next Move" | The Exit That Unlocked the Next Move | Step 4 — Selection Research | Cluster: Exit Before Entry™ pillar | Client proof exists (names only) |
| 2 | "MoK & Jine: Buying in Two Names, Climbing With One Plan" | Two-Name Advantage | Step 2 — Direction Statement | Cluster: Two-Name Advantage / joint ownership | Client proof exists (names only) |
| 3 | "How the Win/Esther Family Repositioned for the Next Generation" | Repositioning for Long-Term Growth | Step 3 — Move Sequence | Cluster: NAV Climb / Family Options | Client proof exists (names only, name TBC) |
| 4 | "Lynn's Walk-Away: The Property She Didn't Buy" | The Missed Window Warning | Step 4 — Selection Research | Cluster: Missed Window / agent-distrust objection | Client proof exists (names only) |
| 5 | "[Proof gap] Choosing the Harder Sequence Over the Comfortable One" | Strategy Over Comfort | Step 2 — Direction Statement | Cluster: One-Property Trap / Buy-To-Stay Thinking | **GAP — no client sourced** |
| 6 | "[Proof gap] One Stronger Asset, Not Two Weaker Ones" | One Stronger Asset Before Two | Step 3 — Move Sequence (Hold-Two Path rejected) | Cluster: NAV Climb vs. door-count | **GAP — highest priority, zero raw material** |
| 7 | "[Proof gap] The Research That Changed Which Property They Bought" | Exit Before Entry | Step 4 — Selection Research | Cluster: Exit Before Entry™ pillar (category law itself) | **GAP — highest visibility, category-law proof** |
| 8 | "From High-Value HDB to Their First Private: the Sequence That Made It Safe" | The Exit That Unlocked the Next Move | Step 1 — Position Map | Cluster: HDB-to-private upgrade | Sourcing target |
| 9 | "The EC Owner Who Waited One Policy Cycle — On Purpose" | Strategy Over Comfort | Step 2 — Direction Statement | Cluster: MOP timing / Policy Clock | Sourcing target |
| 10 | "A DINK Couple's Move Sequence: Two Incomes, One Ladder" | Repositioning for Long-Term Growth | Step 3 — Move Sequence | Cluster: DINK couple upgrade | Sourcing target |
| 11 | "The Single Climber Who Went Private First" | The Exit That Unlocked the Next Move | Step 1 — Position Map | Cluster: single going for first private | Sourcing target |
| 12 | "Why This Family Chose Hold-Two Over Trade-Up (And Why That Was Right For Them)" | One Stronger Asset Before Two (counter-case) | Step 2 — Direction Statement | Cluster: Trade-Up Path vs. Hold-Two Path | Sourcing target — deliberately the counter-argument case |
| 13 | "The Second Name That Changed Their Loan Capacity" | Two-Name Advantage | Step 1 — Position Map | Cluster: Name-Count Advantage | Sourcing target |
| 14 | "Trapped Equity: The Property That Was Quietly Costing Them Options" | The Missed Window Warning | Step 1 — Position Map | Cluster: Trapped Equity / Stuck Asset | Sourcing target |
| 15 | "The Buyer Who Almost Went Agent-Led — and What Changed Their Mind" | Strategy Over Comfort | Step 4 — Selection Research | Cluster: Agent-Led Transaction Thinking villain | Sourcing target |
| 16 | "Rebuilding NAV After a Flat Decade: One Family's Climb Cadence" | Repositioning for Long-Term Growth | Step 5 — Climb Cadence | Cluster: NAV Climb | Sourcing target — needs a client 12+ months post-engagement |
| 17 | "The Exit Buyer Who Didn't Exist: A Selection Research Save" | Exit Before Entry | Step 4 — Selection Research | Cluster: Exit Before Entry™ / rentability research | Sourcing target |
| 18 | "Two Properties, One Family, One Sequence: The Two-Name Path in Practice" | Two-Name Advantage | Step 3 — Move Sequence | Cluster: Two-Name Path | Sourcing target |
| 19 | "The Missed-Window Client Who Moved Just in Time" | The Missed Window Warning | Step 2 — Direction Statement | Cluster: Missed Window | Sourcing target |
| 20 | "One Stronger Asset: The Math Behind Consolidating Two Mortgages Into One Climb" | One Stronger Asset Before Two | Step 3 — Move Sequence | Cluster: NAV Climb vs. door-count | Sourcing target — second attempt at closing the priority-1 gap |

---

## 4. 20 Review Snippet Ideas

These are **prompts to ask real clients about**, not scripted or fabricated reviews. Collect via a short post-session or post-engagement review request (Position Map session follow-up email; Climb Cadence annual review follow-up), asking the client to describe the experience in their own words against one of these themes — never handing them pre-written text to approve. State this plainly wherever review collection is described internally and never publish a review the client did not write or explicitly dictate.

| # | Theme to ask about | Objection it neutralises |
|---|---|---|
| 1 | "They told me not to buy something I wanted" | Agent-distrust / sales-pressure fear |
| 2 | "They found the exit problem before I signed anything" | Fear of buying something unsellable later |
| 3 | "I nearly bought the wrong property before this" | Missed-window / regret fear |
| 4 | "It felt like planning, not selling" | "This is just another agent pitch" objection |
| 5 | "The numbers they gave me actually matched reality later" | Distrust of projections/promises |
| 6 | "I understood my own numbers for the first time" | Confusion/overwhelm about own financial position |
| 7 | "They turned me down as a client at first" | Skepticism about the 90% disqualification claim |
| 8 | "My spouse and I finally agreed on a plan" | Couple/family decision-paralysis |
| 9 | "I didn't feel rushed" | Fear of high-pressure sales tactics |
| 10 | "They explained the CPF/ABSD math in a way I could actually follow" | Regulatory confusion / fear of hidden costs |
| 11 | "We compared this to seeing three agents first" | Comparison-shopping objection |
| 12 | "It changed the order I was planning to do things in" | "I already have a plan" objection |
| 13 | "I got a second opinion that didn't just agree with me" | Fear of an echo-chamber sales conversation |
| 14 | "They asked about our exit before asking about our budget" | "Agents only care about closing" objection |
| 15 | "The session was worth it even though it was free" | Skepticism about a free session having real value |
| 16 | "I went in confused about hold-two vs trade-up and left with an actual answer" | Confusion about strategy options |
| 17 | "They flagged a risk our own agent hadn't mentioned" | "My current agent already covers this" objection |
| 18 | "A year later, the plan is still on track" | Doubt that advice holds up over time (Climb Cadence proof) |
| 19 | "I recommended this to my sibling/friend before they made the same mistake I almost made" | Trust-transfer / social-proof objection |
| 20 | "They were upfront that this isn't for everyone" | Skepticism about "by application only" positioning |

---

## 5. 10 Founder Authority Story Angles

All angles below draw only from the verified journey (§ founder proof, CSV PL-001 to PL-007) and existing live-channel footprint (Facebook, Instagram, YouTube, GBP, thereimethod.com). No angle assumes a platform the business doesn't currently use.

| # | Angle | Platform fit |
|---|---|---|
| 1 | Origin: "We started in a sub-$600K HDB flat" — the founder's own Step 1 Position Map, before there was a method | thereimethod.com founder page (long-form); YouTube long-form |
| 2 | The four-move journey as four chapters: Tre Ver → Parc Clematis → United Square → the east-side 4-bedroom | thereimethod.com founder page (visual timeline); Instagram carousel (one slide per move) |
| 3 | "We built it before we advised it" — why lived experience, not a licence, is the actual credibility test | Instagram/Facebook static post; GBP post |
| 4 | The co-purchase structure: how a multi-name ownership decision inside the founder's own family became the Two-Name Advantage proof point | thereimethod.com founder page; YouTube long-form (once co-owner consent is secured) |
| 5 | "Would we buy our own past property today?" — an honest, self-disqualifying angle that mirrors the 90% disqualification stat applied to the founders' own history | YouTube long-form; Instagram Reel |
| 6 | Why two founders, not one — Edmund and Cindior's complementary roles in the advisory (pending Cindior's confirmed public-presence level, per Master Context Brief D6) | thereimethod.com dual-founder page; Facebook |
| 7 | The shift from "agent" income logic to advisory logic — the founders' own moment of realising project-first thinking was the wrong model (told carefully to avoid contradicting active PropNex-salesperson status) | YouTube long-form; thereimethod.com about page |
| 8 | Family-first motivation: why the climb was always about family options, not door-count | Instagram/Facebook; GBP post |
| 9 | The discipline of writing down real numbers — the founders' own Position Map habit, shown as a screen-recorded (redacted) example | YouTube long-form (screen capture); Instagram Reel |
| 10 | Why the east-side move was the first time the founders applied Selection Research to themselves before advising anyone else on it | thereimethod.com founder page; YouTube long-form |

---

## 6. 10 Market Research Proof Pages

Each is a publishable research asset built only from data that is genuinely collectable — public forum/editorial content already reviewed (VERIFIED), public government data, or the business's own CRM in aggregate/anonymised form. No fabricated statistics. Each page requires the stated method note before publishing (D8: people-first, genuinely answer-complete content).

| # | Page title | Data source | Method note required |
|---|---|---|---|
| 1 | "What Singapore's Upgrade Threads Reveal About Sequencing Regret" | HardwareZone EDMW public threads (already read 8 July 2026) | State thread count, date range read, and that quotes are paraphrased/anonymised, not scraped verbatim without permission |
| 2 | "How Progressing Owners Actually Talk About Their Next Move" | Stacked Homes editorial coverage (already read 8 July 2026) | Cite specific article URLs and publish dates |
| 3 | "The 'Two Properties' Desire: What ERA and PropNex Research Actually Found" | ERA/PropNex published editorial content (already read 8 July 2026) | Cite source URL and date; distinguish industry-body research from The REI Method's own claims |
| 4 | "Private vs. HDB: A Ten-Year Price Index Comparison (2015–2025)" | URA REALIS/URA.gov.sg public price index data | Re-pull directly from URA before publishing (PL-036 is not yet re-verified); state exact index basis and pull date |
| 5 | "Inside the 90% Disqualification Rate: Why Most Buyers Don't Qualify" | The REI Method's own CRM (1-To-1 Pipeline), aggregated and anonymised | State sample size, date range, and that individual client data is never disclosed — this converts the funnel trust-stat into a genuine, sourced page rather than a bare claim |
| 6 | "38,000 Agents, One Sequence: What Buyer Choice Overload Looks Like in Singapore" | CEA public salesperson registry count | Cite CEA source and pull date; use to illustrate market fragmentation, not to disparage any individual agent |
| 7 | "What a Second Property Actually Costs: An ABSD Scenario Breakdown" | IRAS public ABSD rate tables | Date-stamp against current cooling-measure rates; rebuild each time rates change (D7 cadence) |
| 8 | "The Hidden Cost of CPF Accrued Interest When You Hold One Property Too Long" | CPF Board published Ordinary Account interest rate | Date-stamp; show worked example with rate cited |
| 9 | "The Policy Clock: MOP, SSD, and ABSD Timing for Singapore Property Owners" | HDB/IRAS public policy timelines, compiled | Date-stamp every regulatory figure individually, since each has its own review cycle |
| 10 | "Net Asset Value vs. Door Count: What Climbing Actually Looks Like Across [N] Clients" | The REI Method's own CRM, aggregated NAV-growth data | **Gated** — do not publish until sample size (N) is large enough for genuine aggregate reporting without re-identifying individual clients (recommend N ≥ 20 before considering); requires aggregate-use consent language added to future client engagements |

---

## 7. Compliance-Safe Claims Guide

**Portfolio figures (founder or business-level, e.g., Tre Ver/Parc Clematis appreciation, $6.6M→$9M NAV, $160,014,029 invested):**
- Never publish an exact figure without a document it can be checked against (SPA, valuation report, CPF statement, resale contract, or an internal ledger for aggregate business stats).
- Where no document exists yet, publish a rounded range with the word "illustrative," not a bare precise number.
- Date-stamp every portfolio figure ("as at [date]") — property values move, and an undated figure ages into a misleading one.

**Client results (case studies, client proof, reviews):**
- Require written consent before any use (§1 checklist).
- Every page carrying a specific client result must carry an "individual results" disclaimer: results reflect a specific client's circumstances and are not typical or guaranteed for any other buyer.
- Prefer ranges over exact figures unless the client has explicitly consented to exact-figure publication.

**Market stats (EDMW/Stacked Homes/ERA findings, URA index, ABSD/CPF worked examples, the "38,000 agents" stat):**
- Every market stat carries a named source and a date. No invented URLs or uncited "industry data."
- Regulatory figures (ABSD rates, CPF interest, MOP/SSD windows) go on a quarterly re-verification cadence per D7 — assign an owner and a recurring check, not a one-time fact-check.

**The $160,014,029 / 100+ buyers verification standard (define before any further reuse):**
1. Define what counts: recommend "total transacted property value of clients who engaged The REI Method's advisory process and completed a purchase," tracked via GHL Won-stage deals using the existing `buy_price` / `current_value` custom fields.
2. Reconcile the running total against the CRM quarterly; assign a named compliance owner (recommend Cindior Ho, given her contact-record role in GHL) to sign off each quarterr's figure before it's used in any new creative.
3. Until step 1–2 is done, treat both stats as INFERRED, not VERIFIED, and avoid introducing them into new pages beyond their current use in the live Legacy Launch V2 funnel (which is not being touched per the do-not-touch/light-touch rules).
4. Once verified, still don't over-state precision: "$160,014,029" reads as suspiciously exact for a marketing stat; consider whether a rounded figure ("$160M+") is both more defensible and more credible once the underlying ledger is confirmed.

**CEA advertising rules:**
- Both founders are PropNex-registered salespersons. Every public page, ad, and piece of proof content that could be read as advertising a property service must carry: the founder's registered name, CEA registration number, and the estate agent (PropNex) name and licence number — per CEA advertising guidelines. This is currently missing everywhere (PL-049, BLOCKING).
- The existing funnel line "This is advisory, not agency" is a compliance risk while the founders operate as licensed salespersons (flagged in the Master Context Brief, D7). Recommended replacement, consistent with LOCKED vocabulary: **"Advisory-first. We plan the sequence before any transaction."**

**Disclaimer and PDPA copy — fix the entity mismatch (D1):**
The current Legacy Launch V2 funnel has three different names doing the job of one entity: the PDPA consent line says clients consent to **"Legacy Launch"** contacting them; the footer copyright says **"© Singapore Real Estate Insider."** Per D1, the correct entity for both is **The REI Method** (Legacy Launch is a campaign sub-brand under it; Singapore Real Estate Insider is the media/YouTube brand only, not the contracting entity). Corrected copy:

- **PDPA consent line (replace "Legacy Launch" with the entity):** "By submitting your details you consent to **The REI Method** contacting you in accordance with Singapore's Personal Data Protection Act (2012)."
- **Footer (replace media-brand copyright with entity):** "© 2026 **The REI Method**. All rights reserved." (Singapore Real Estate Insider may still be credited separately as "as seen on our YouTube channel, Singapore Real Estate Insider" if wanted — but not as the copyright holder.)
- Keep the existing risk disclaimer body copy ("All figures and case studies reflect specific client and portfolio outcomes and are shared for illustration. Property involves risk; past results do not guarantee future performance… Nothing here is financial advice.") — it is compliance-sound as written; only the entity name around it needs fixing.
- Add the CEA registered-name + reg. no. + PropNex licence line to the same footer block once PL-049 is resolved.

**Reviews specifically:**
- No fake or incentivised reviews (D8). No self-serving `AggregateRating`/`Review` schema on first-party content — see §2.2 and the existing ruling in `02_ENTITY_ARCHITECTURE.md` Entity 9 (Google Search Central — Review snippet structured data: a business marking up its own testimonials as reviews is not eligible for review rich results). Genuine third-party reviews collected via §4 may be marked up with `Review` where hosted verbatim, attributed to a real author, with consent.

---

## Concerns

1. **NAV figure inconsistency:** the Master Context Brief states the founder household NAV moved "$6.6M→$9M potential" (§2, §3 D1 area) while the reel claims bank (Report 3) states "own NAV <$1M→>$5M in <5yrs." These may describe different scopes (one property's NAV vs. household NAV, or different time windows) but as written they read as two different claims about the same thing. Recommend the founders clarify which figure is current and what each one actually measures before either is reused (CSV PL-010/PL-011).
2. **"Win/Esther & Family" name ambiguity:** Report 3's verbatim asset register lists this client as "Win/Esther & Family" with a slash, suggesting the correct first name wasn't confirmed at research time. Do not draft PL-016/PL-020 until this is resolved with the founders.
3. **Three of seven proof categories have zero client material** (Strategy Over Comfort, One Stronger Asset Before Two, Exit Before Entry). Exit Before Entry is especially exposed since it's the category law itself — publishing the category hub without a dedicated client proof point for it is a credibility gap worth closing early, not last.
4. **$160,014,029 precision:** stating a business-wide investment figure to the exact dollar reads as either extremely well-audited or suspiciously fabricated — there is no middle ground with that level of precision. Recommend resolving the verification standard (§7) before this figure appears in any new asset beyond its current, untouched, live-funnel use.

---

## Questions To Clarify

1. Which NAV figure is current and correct — $6.6M→$9M or <$1M→>$5M — and what scope does each measure (see Concern 1)?
2. Is "Win/Esther & Family" one client (Win, or Esther) or a mislabel — confirm the correct name before any case-study drafting.
3. Do Edward & Rose, MoK & Jine, Win/Esther & Family, and Lynn all still have an active/reachable relationship with the founders for a consent conversation?
4. Is there a real client story available for "Strategy Over Comfort," "One Stronger Asset Before Two," or "Exit Before Entry" that simply wasn't captured in the reel-script research, or are these genuine first-time gaps?
5. Who should own the quarterly claims-verification cadence (recommend Cindior Ho, per her GHL contact-record ownership) — confirmed?
6. Does the business have any media/press features, speaking engagements, or awards not reflected in any document reviewed?
7. What is the actual definition the business wants to use for "$160,014,029 collectively invested" — total transacted client value, total AUM-equivalent, or something else?

## Dependencies

- **02_ENTITY_ARCHITECTURE.md** — entity naming (The REI Method vs. Singapore Real Estate Insider vs. Legacy Launch) that the Compliance-Safe Claims Guide (§7) and Entity 9 review-schema ruling both build on.
- **04_WEBSITE_SITEMAP_AND_PAGE_ROADMAP.md** (not yet built) — case-study and proof-page slugs used throughout this file (`/case-studies/*`, `/second-property-ladder`, Step cluster pages) assume this sitemap structure; confirm final slugs once that file exists.
- **06_FUNNEL_ECOSYSTEM_AUDIT.md** (not yet built) — the Legacy Launch V2 disclaimer/PDPA fix in §7 should be applied as part of that funnel's light-touch bridge pass, not as a standalone edit.
- **08_GOOGLE_BUSINESS_PROFILE_PLAN.md** (not yet built) — PL-031 (GBP review count/rating) is blocked on that audit.
- **GHL CRM access** — several verification steps (100+ buyers, 90% disqualification rate, the aggregate NAV research page in §6) require querying the 1-To-1 Pipeline directly.
- **CEA/PropNex compliance sign-off** — PL-049 blocks every public page and ad in this library, not just proof pages.

## First 5 Actions

1. Run the PDPA/consent conversation with all four named clients (Edward & Rose, MoK & Jine, Win/Esther & Family, Lynn) using the checklist in §1 — this unblocks 4 of the 7 case-study categories and 4 client-proof rows in one motion.
2. Start sourcing candidates for the three proof-gap categories (Strategy Over Comfort, One Stronger Asset Before Two, Exit Before Entry) from the 1-To-1 Pipeline Won-stage contacts, prioritising Exit Before Entry and One Stronger Asset Before Two.
3. Obtain CEA registration numbers and PropNex licence numbers for both founders (PL-049) — this is blocking every other public-facing deliverable in the entire repositioning project, not only this one.
4. Fix the Legacy Launch V2 PDPA consent line and footer copyright per §7 (Legacy Launch → The REI Method; Singapore Real Estate Insider → The REI Method) as a light-touch edit, without otherwise disturbing the do-not-touch funnel.
5. Add the post-session review ask (from §4's 20 themes) to the Position Map session follow-up email sequence so genuine review collection starts before any other proof-building work — it is the cheapest, fastest-moving proof type in the entire library and currently sits at zero.
