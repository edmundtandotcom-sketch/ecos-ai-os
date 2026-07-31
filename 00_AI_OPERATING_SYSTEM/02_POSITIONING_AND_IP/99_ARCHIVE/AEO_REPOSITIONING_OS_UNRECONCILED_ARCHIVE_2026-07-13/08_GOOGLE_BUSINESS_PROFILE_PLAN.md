# 08 — GOOGLE BUSINESS PROFILE / LOCAL AUTHORITY PLAN
**Owner:** Sonnet agent (Phase 8) · **Status:** Draft for orchestrator QA · **Depends on:** D1 (entity model), D2 (authority domain), D5 (vocabulary), D7 (compliance)

## Executive Summary

One Google Business Profile (GBP) already exists at `share.google/bpyWTGgjlyNxt8Xiz` with its name, category and review count unverified — the first job is a manual audit, not a rebuild. The entity model (D1) creates a naming problem specific to GBP: Google requires a listing's name to match how the business *already* presents itself in the real world, but "The REI Method" does not yet appear anywhere public (no live site, no social bios use it). Creating a GBP under "The REI Method" today would fail Google's name-matching guideline. The sequencing recommendation is: keep/repair the existing listing under a founder- or currently-verifiable name now, launch `thereimethod.com` and update public bios to match (Phase 2/7 dependency), then migrate or rename the GBP once "The REI Method" is genuinely the public name.

Both founders are CEA salespersons under PropNex, which raises a second structural question: individual practitioner listings vs. one business listing. Google permits a practitioner (its own guidance names doctors, lawyers, and real estate agents) to run a personal listing alongside the parent business listing only if each has genuinely distinct, publicly reachable contact details — Edmund and Cindior currently share one phone (+65 8786 3931) and one email (admin@thereimethod.com), so they do not yet qualify for two separate listings without creating duplicate-listing risk. The address on file (#17-23, Singapore 338520) reads as a home/serviced address, not a client-facing office — recommend Service Area Business (SAB) configuration with the address hidden.

This document delivers the audit checklist, naming and category decision, a full services list and 750-character description (both compliant with the banned-word list), a photo/video plan, a Posts and Q&A programme tied to the 6 content pillars, a PDPA-safe review-generation system with verbatim templates, website/UTM strategy, the canonical NAP block, a citation target list, and a sequenced Local Authority Checklist.

---

## 1. GBP Audit Checklist (existing listing: share.google/bpyWTGgjlyNxt8Xiz)

Run this manually against the live listing before touching anything. Do not edit until every row is filled in — an edit to a listing whose current state is unknown risks tripping Google's re-verification or suspension flags.

| # | Field | What to check | Current value | Target value |
|---|---|---|---|---|
| 1 | Business name | Exact string shown on the listing | [VERIFY] | See §2 Naming Decision |
| 2 | Primary category | Single category shown under the name | [VERIFY] | Real estate consultant (see §3) |
| 3 | Secondary categories | Full list (up to 9 additional) | [VERIFY] | See §3 |
| 4 | Address visibility | Storefront (pin shown) vs. Service Area Business (pin hidden) | [VERIFY] | Service Area Business, address hidden (see §10) |
| 5 | Service area | Which regions/postal areas are set, if SAB | [VERIFY] | Singapore (whole country — advisory serves buyers island-wide) |
| 6 | Hours | Listed opening hours | [VERIFY] | By-appointment hours only; mark "By appointment" if the field supports it, otherwise conservative weekday hours matching booking calendar availability |
| 7 | Phone | Public number shown | [VERIFY] | Must equal +65 8786 3931 (GHL canonical number) |
| 8 | Website link | URL shown, if any | [VERIFY — GHL website field is currently blank] | thereimethod.com once live (see §9) |
| 9 | Appointment/booking link | Whether a "Book" button/link exists | [VERIFY] | Position Map session booking page |
| 10 | Review count and rating | Total reviews, average rating, most recent review date | [VERIFY] | Baseline for velocity target in §8 |
| 11 | Photos present | Count, type (logo, cover, interior, team) | [VERIFY] | Replace/supplement per §6 |
| 12 | Claim/ownership status | Who currently manages the listing (which Google account) | [VERIFY] | Must be transferred to a business-controlled Google Workspace account, not a personal Gmail, before this plan proceeds |
| 13 | Duplicate listings | Search "Coach Edmund Tan," "Cindior Ho," "The REI Method," "Singapore Real Estate Insider" on Google Maps to check for other listings at the same address/phone | [VERIFY] | Zero duplicates representing the same entity (see §2) |
| 14 | Products/Services tab | What is currently populated, if anything | [VERIFY] | Replace with §4 services list |
| 15 | Q&A tab | Any existing public questions (including ones asked by strangers that may contain wrong info) | [VERIFY] | Seed with §7C; correct any wrong public answers immediately — an unanswered wrong answer outranks a correct one over time |

---

## 2. Naming Decision

**Google's rule (Google Business Profile guidelines — "Representing your business on Google," name section):** the name on a Business Profile must match the name the business actually uses in the real world — on signage, stationery, invoices, and other public-facing material. Google explicitly disallows adding marketing taglines, keywords, or descriptors to the name field purely to rank for them.

This creates a direct conflict with D1's business entity ("The REI Method") because that name is not yet used anywhere public. The three names currently in public use are "Coach Edmund Tan" (Facebook), "Property Coach Edmund Tan" (Instagram), and "Singapore Real Estate Insider" (YouTube) — none of which is "The REI Method."

**Recommendation — sequenced, not simultaneous:**

1. **Now (interim):** if the existing listing's current name is already some variant of "Coach Edmund Tan," keep it as an **individual practitioner listing** under that name (with the practitioner-listing caveats in the next section resolved first). If the current name is something else entirely (a stale name, a wrong category, or a name that doesn't match any current public asset), correct it to "Coach Edmund Tan" as the interim, verifiable state.
2. **After Phase 2/7 dependencies land** (thereimethod.com live; Facebook/Instagram bios updated to reference The REI Method per `07_SOCIAL_PROFILE_REPOSITIONING.md`): rename the same listing, or add a second properly-differentiated listing, to **"The REI Method"** as the business-level GBP — at that point the name is real-world-verifiable and the rename request will not read as keyword manipulation to Google's automated name-change review.
3. **Do not create "The REI Method" and "Coach Edmund Tan" as two simultaneous listings at the same address/phone today.** That is the duplicate-listing pattern Google's guidelines prohibit (representing the same entity twice to gain more map real estate). The distinction Google allows is business listing vs. genuinely separate individual practitioner listing — see below.

**Practitioner listings for Edmund and Cindior:** Google's guidance (the same "Representing your business on Google" document, section on practitioners) names doctors, lawyers, and real estate agents as the standard example of professionals who may hold an individual listing alongside their parent business's listing — but only where each listing represents a distinct, independently reachable point of contact (own direct phone line and/or own email, and either a shared or individually bookable meeting point). Today, Edmund and Cindior share one phone number and one email in every system of record (GHL). **They do not currently meet the distinctness bar for two separate individual listings.** Two paths forward:

- **Path A (recommended, lower effort):** one business listing only ("Coach Edmund Tan" now → "The REI Method" later), with both founders named and pictured in photos, posts, and the description. No individual GBP listings for either founder.
- **Path B (only if the client wants Cindior to have her own discoverable listing):** issue Cindior a distinct direct number and/or email first, then create a genuinely separate individual practitioner listing for her, cross-linked (not duplicated) to the business listing. This is an [OPEN] decision — do not build Path B until distinct contact details exist, and until Cindior's public-presence appetite is confirmed (open question #4 in the master brief).

**Naming string to use, verbatim, at each stage:**

| Stage | GBP business name field |
|---|---|
| Interim | Coach Edmund Tan |
| Post-launch | The REI Method |
| Individual practitioner (Path B, if pursued) | Cindior Ho |

Do not append descriptors like "— Second Property Ladder Advisory" or "— Property Consultant Singapore" to the name field. That is the keyword-stuffing pattern Google's name guideline exists to catch, and it puts the whole listing at suspension risk.

---

## 3. Category Recommendation

GBP's category list is a fixed, Google-maintained taxonomy — categories cannot be invented, only chosen from what Google offers in the category picker at the time of editing. The names below are the closest real-world matches; confirm exact spelling and availability in the live picker before saving, since Google periodically retires and renames categories.

| Slot | Category | Rationale |
|---|---|---|
| Primary | **Real estate consultant** [VERIFY exact string in picker] | Best match to the advisory positioning — planning/sequencing, not transacting. Distances the profile from the generic "agent who shows property" framing the whole strategy is built to differentiate from. |
| Secondary | **Real estate agency** [VERIFY] | Include only because CEA/PropNex status makes this factually true and Google's category system rewards categories that match actual licensed activity; this is a taxonomy field, not marketing copy, so it does not conflict with the banned-word rule on "agent" in body copy. |
| Secondary | **Real estate agent** [VERIFY — may only be available as an individual-listing category, not business] | Use only on an individual practitioner listing if Path B is built; likely not selectable on the business listing. |
| Secondary | **Financial consultant** [VERIFY] | Reflects the numbers-first, NAV-planning nature of the Position Map / Blueprint work without over-claiming financial-advisory licensing the founders do not hold. |
| Do not use | "Investment company," "Property management company," "Real estate developer" | None of these are factually accurate to what the business does (no managed portfolios, no development activity) — a mismatched category is itself a policy violation and invites suspension on audit. |

---

## 4. Services List (GBP "Services" section)

GBP for a "Real estate consultant" category typically exposes a **Services** section (not a Products section — Products is built for businesses selling discrete physical retail items and is not applicable here; leave it unused rather than force irrelevant entries into it). Each service below is named to LOCKED vocabulary and written under Google's 300-character description limit, with banned words (advice, consultation, unit, agent, investment property, asset progression, good buy, project, Homeowner) avoided.

| Service name | Description (char count noted) |
|---|---|
| Position Map Session | A 45-minute session where we map your defendable property value, CPF position, and loan capacity — so you see your real numbers before you decide on any next move. No pressure, no pitch. Free for qualifying Property Climbers. (225 chars) |
| Which Step Are You On? Diagnostic | A short scored diagnostic that places you on one of the 5 Steps of The Second Property Ladder™, based on your current property, income, and readiness to climb. Takes under 5 minutes, free, no obligation. (203 chars) |
| The Second Property Ladder Blueprint™ | Our paid engagement covering all 5 Steps — Position Map, Direction Statement, Move Sequence, Selection Research, and Climb Cadence — so your next property move is sequenced and exit-ready before you commit. (206 chars) |
| Direction Statement | We help you choose your route — combined purchase versus a two-property path — matched to your age, runway, and risk comfort, with a clear option-value target for where you are heading. (185 chars) |
| Move Sequence | The signature output of Step 3: an ordered list of moves using your age, loan capacity, income, and time — because the order you move in is what protects your net asset value. (175 chars) |
| Selection Research (Exit Before Entry™) | Before you shortlist anything, we research the exit — who buys it after you, at what price, and how deep the buyer pool is — so nothing is chosen without an exit already understood. (181 chars) |
| Climb Cadence / Climb Review | An annual check-in that re-maps your position and confirms whether your next Step is ready to move on, or whether to hold — because the climb is monitored, not a one-time decision. (180 chars) |

---

## 5. Recommended GBP Description (750-character limit)

Verbatim, for the **post-launch ("The REI Method")** stage. Character count confirmed below the block.

> The REI Method helps Singapore Property Climbers turn one strong property into a safely sequenced climb toward higher net asset value. Founders Coach Edmund Tan and Cindior Ho, CEA-registered under PropNex, built The Second Property Ladder™ — five steps: Position Map, Direction Statement, Move Sequence, Selection Research, and Climb Cadence — so your next property move is sequenced before you commit. Every move is researched exit-first under Exit Before Entry™: we look at who buys it after you before we look at what you're buying. Start with a free Position Map session and see your own numbers before you decide anything.

**Character count: 628** (within the 750-character limit; verified by count, not estimate).

For the **interim ("Coach Edmund Tan")** stage, shorten the opening clause to: "Coach Edmund Tan, CEA-registered under PropNex, helps Singapore Property Climbers…" and drop "Founders … built" — keep the rest identical. Re-count before publishing either version, since any future edit to phrasing changes the count.

Do not add CEA registration numbers or the PropNex licence number inside this field — there isn't room within 750 characters to do so without cutting the substantive description, and GBP's description field is not one of CEA's mandated disclosure surfaces. Put the CEA/PropNex disclosure on the linked website page instead (see §9) and in the pinned "About" content on Facebook/Instagram per `07_SOCIAL_PROFILE_REPOSITIONING.md`.

---

## 6. Photos/Video Plan

| Asset | What to shoot | Naming convention | Notes |
|---|---|---|---|
| Logo | The REI Method wordmark, square crop, transparent or ivory background | `thereimethod-logo-square.jpg` | Needed before any GBP branding edit — currently no confirmed logo asset exists [VERIFY]. |
| Cover photo | Wide founder shot, both Edmund and Cindior, navy/ivory/gold palette matching the Legacy Launch V2 creative direction | `reimethod-cover-founders.jpg` | Reuse the private-wealth-advisory aesthetic already defined for Legacy Launch V2 so the visual system is consistent site-to-listing. |
| Team photo | Edmund and Cindior together, professional, no property signage or PropNex branding visible in frame (keeps the photo usable regardless of brokerage affiliation changes) | `reimethod-team-edmund-cindior.jpg` | — |
| Session-in-progress | A staged Position Map session: two people at a table, a printed or on-screen Position Map artefact visible but with all numbers replaced by placeholder/sample figures — never a real client's actual financial data | `reimethod-position-map-session.jpg` | PDPA: no real client identifiable info in any photo used publicly. |
| Artefact close-up | Close-up of a sample Position Map or Move Sequence page, anonymised (fictitious name, rounded/sample numbers, watermark "Sample — for illustration") | `reimethod-artefact-position-map-sample.jpg` | Do this for each of the 5 Step artefacts over time — gives Posts and Q&A a rotating visual library. |
| Founder solo shots | Individual professional headshots of Edmund and of Cindior, consistent lighting/background | `reimethod-edmund-headshot.jpg`, `reimethod-cindior-headshot.jpg` | Use for individual practitioner listing if Path B (§2) is pursued, and for author bios on thereimethod.com. |
| Short video | 30–60 second founder-to-camera clip explaining "What is the Second Property Ladder?" — captioned, vertical-safe crop | `reimethod-video-what-is-spl.mp4` | GBP video uploads have a 30-second minimum play weight in local ranking signals; keep it short and looped. |

Do not embed location keywords or spam terms into filenames beyond the plain descriptive name above — Google's guidance on photo metadata warns against keyword-stuffed filenames as a manipulation signal, so keep filenames descriptive, not keyword-loaded.

---

## 7. Products/Services, Posts, and Q&A Programme

### 7A. Products/Services section usage
Leave "Products" unused (not applicable to a consultant/agency category — see §4 rationale). Populate "Services" exactly per the table in §4, ordered with Position Map Session first (it is the single universal CTA) and the Blueprint components following in Step order.

### 7B. Posts — weekly plan tied to the 6 content pillars

Google's standard "Update" posts expire after 7 days, which forces a weekly cadence anyway. Rotate one pillar per week on a 6-week cycle; reuse the rotation continuously.

| Week in cycle | Pillar | Post type | Example angle | CTA button |
|---|---|---|---|---|
| 1 | The One-Property Trap | What's New | "Most Singaporeans stop climbing after one property — here's the trap that stalls net asset value" | Learn more → thereimethod.com/one-property-trap |
| 2 | Exit Before Entry | What's New | "Before you shortlist a launch, ask who buys it after you — Exit Before Entry™ explained" | Learn more |
| 3 | The 5 Steps | What's New | Feature one Step artefact (rotate: Position Map → Direction Statement → Move Sequence → Selection Research → Climb Cadence) | Book (Position Map session) |
| 4 | Founder Proof | What's New | Founder journey milestone, [VERIFY]-flagged figures only after confirmation | Learn more |
| 5 | Buyer Mistakes | What's New | One named buying mistake (e.g., buying before researching the exit) | Book |
| 6 | Case Studies | What's New | One anonymised case-study category (e.g., "The Exit That Unlocked the Next Move") | Learn more |

Use the **Offer** post type instead of "What's New" for any week promoting the Position Map session specifically (Offer posts support a start/end date and a redemption-style CTA), and the **Event** post type when a live seminar or webinar is scheduled. Every post links back to thereimethod.com with the UTM parameters in §9 — never to a bare phone number or unlabelled link.

### 7C. Q&A Seeding — 10 questions, AEO-question-bank style

Post these as the business, from the business's own Google account, so the answer displayed is authoritative rather than left to a stranger's guess. Written to be genuinely useful (answer-complete, per D8), in locked vocabulary, no banned words.

1. **Q: What is The Second Property Ladder™?**
   A: It's a 5-Step sequence — Position Map, Direction Statement, Move Sequence, Selection Research, and Climb Cadence — that helps Singaporeans who already own a strong first property plan their next move safely, in the right order, instead of buying blind.

2. **Q: What does "Exit Before Entry™" mean?**
   A: It means researching who will buy a property from you, at what price, before you commit to buying it. We research the exit buyer, exit timing, and downside buffer first — entry decisions come second.

3. **Q: Do I need $2.5 million in property value to start?**
   A: Our Position Map session is built for households earning $20k+ a month who can service a property value of roughly $2.5m or more. If you're below that today, our free content still covers all 5 Steps — the paid Blueprint is for households at or near that threshold.

4. **Q: What actually happens in a Position Map session?**
   A: In 45 minutes we map your defendable property value, CPF position (principal plus accrued interest), and loan capacity, so you leave with your real numbers — not a sales pitch for a specific launch.

5. **Q: I currently own an HDB or EC — can I still climb?**
   A: Yes. Many Property Climbers start from a high-value HDB or EC. The first Step, Position Map, is exactly where we work out whether you're ready to move and what your options are from where you stand today.

6. **Q: How is this different from going straight to a new launch showflat?**
   A: A showflat conversation starts with a specific launch. We start with your numbers and your exit — Selection Research happens before any launch is shortlisted, not after you've already fallen for one.

7. **Q: What is the ABSD impact if I already own one property?**
   A: Singapore's Additional Buyer's Stamp Duty applies to a second property for citizens and varies by residency status — figures change with policy updates, so we map your exact ABSD exposure inside the Position Map session rather than quoting a generic rate here. [VERIFY current ABSD rate at time of publishing]

8. **Q: How long does The Second Property Ladder Blueprint™ take?**
   A: It covers all 5 Steps — Position Map, Direction Statement, Move Sequence, Selection Research, and Climb Cadence — and timing depends on how ready your numbers and documents are. We'll give you a specific timeline once your Position Map session is complete.

9. **Q: Are Coach Edmund Tan and Cindior Ho licensed?**
   A: Yes — both are CEA-registered salespersons under PropNex [CEA registration numbers: VERIFY]. We publish our registration details on thereimethod.com in line with CEA's advertising requirements.

10. **Q: Is the Position Map session free, and is there any obligation?**
    A: The Position Map session is free for qualifying Property Climbers and carries no obligation to use any other part of The Second Property Ladder Blueprint™ afterward.

---

## 8. Reviews System

**Velocity target:** ramp from current baseline [VERIFY current count/rating from §1 row 10] to a steady state of **4–6 new reviews per month**, sustained — not a one-time burst. A burst of reviews in a short window is itself a pattern Google's spam systems can flag; steady, session-triggered velocity is safer and more durable.

**PDPA-safe request flow (GHL workflow):**

1. Trigger: contact's pipeline stage in the 1-To-1 Pipeline moves to **"Strategy Session"** completed (i.e., the Position Map session has occurred) or **Blueprint delivered**.
2. Wait 24 hours after the session (same-day requests read as pressured; a day's gap reads as considered).
3. Send via WhatsApp (if the contact has consented to WhatsApp contact — check the PDPA consent field captured at intake) and/or email, using the templates below.
4. The message must: identify the business by name, state the specific purpose (asking for a review), include a direct one-tap review link, and give a clear way to opt out of future requests. This is required both by PDPA (purpose limitation, identified sender) and by Google's own review-solicitation guidance (do not use review-gating — i.e., do not filter who gets asked based on whether they'll leave a positive review).
5. **Never offer an incentive, discount, or entry into a draw in exchange for a review.** This is a direct breach of Google's Business Profile content policy on fake engagement, which prohibits reviews exchanged for money, product, or any other compensation — and it is also the kind of claim that would compound badly with CEA/PropNex advertising scrutiny if ever surfaced. Do not build any workflow branch that varies the ask based on expected sentiment (no gating).

### Template 1 — Post–Position Map session (WhatsApp)
> Hi [First name], it's [Founder name] from The REI Method. Thanks for coming in for your Position Map session yesterday. If it was useful, would you mind sharing a quick Google review? Here's the direct link: [review link]. Totally fine to skip this — just reply STOP if you'd rather not get these requests again.

### Template 2 — Post-Blueprint delivery (email)
> Subject: A quick favour, [First name]?
>
> Hi [First name],
>
> Now that your Second Property Ladder Blueprint™ is complete, we'd really appreciate it if you shared a short Google review of your experience working with us — it helps other Property Climbers find us.
>
> Direct link: [review link]
>
> This should take under two minutes, and there's no obligation. If you'd prefer not to receive requests like this in future, just reply and let us know and we'll stop.
>
> Thanks,
> [Founder name], The REI Method

### Template 3 — Past-client reactivation (email)
> Subject: Still climbing? A quick ask.
>
> Hi [First name],
>
> It's been a while since we last mapped your position together. We're building out our Google presence and would value a short review of your experience, even if it's been some time — here's the link: [review link].
>
> If anything's changed for you and you'd like a fresh Position Map session to see where you stand today, just reply and we'll set one up.
>
> [Founder name], The REI Method

### Response templates

**Positive review response:**
> Thank you, [First name] — really glad the Position Map session gave you clarity on your numbers. Wishing you a safe climb from here. — [Founder name], The REI Method

**Negative review response:**
> Hi [First name], thank you for the feedback — we take this seriously and would like to understand what happened. Could you reach us directly at admin@thereimethod.com so we can look into this properly? We don't want to get into details here, but we do want to make it right.

Never argue with a negative review in public, never dispute specific facts in the public reply, and never offer compensation in the public reply (move any resolution to a private channel first).

---

## 9. Website Link Strategy

| GBP field | Target |
|---|---|
| Website | thereimethod.com (homepage) once live. Until then, leave blank rather than linking a domain not yet representing "The REI Method" publicly (linking a mismatched domain reinforces the same name-mismatch risk flagged in §2). [OPEN — interim link, if any, pending Phase 4 site launch] |
| Appointment link ("Book online") | Position Map session booking page/calendar — currently the GHL calendar "New Launch/Family Legacy Ladder" (`34KkdVJncaYiuAOjE0FP`) serves a related but differently-branded funnel; a dedicated Position Map session calendar object should be created before this link goes live rather than repurposing a New Launch–branded calendar for the core universal CTA. |
| Services section links | Deep-link each service (§4) to its corresponding page on thereimethod.com once the site's page roadmap (`04_WEBSITE_SITEMAP_AND_PAGE_ROADMAP.md`) is built, rather than all pointing to the homepage. |

**UTM convention** (apply to every outbound GBP link):
`utm_source=google&utm_medium=gbp&utm_campaign=local-authority&utm_content={surface}`

Where `{surface}` is one of: `profile-website-link`, `gbp-post`, `gbp-qa`, `gbp-services`, `gbp-booking-button` — so GA4/Search Console reporting can distinguish which GBP surface drove the click.

---

## 10. Local Citations & NAP Consistency

**Canonical NAP block (recommended, post-launch stage):**

```
Name:    The REI Method
Address: Service Area Business — address not publicly displayed; service area: Singapore
Phone:   +65 8786 3931
Email:   admin@thereimethod.com
Website: thereimethod.com
```

**Address decision [OPEN, recommended default]:** #17-23, Singapore 338520 reads as a residential/home-office unit, not a client-facing storefront. Recommend **Service Area Business** configuration (address hidden, service area set to Singapore) across every citation source below, rather than publishing the literal address. This also sidesteps a real privacy exposure (a founder's home address surfacing on a dozen public directories). If the founders later take a genuine client-facing office, switch every citation source to storefront mode in one coordinated pass — do not let some directories show the address and others hide it, since that inconsistency is itself a negative local-SEO signal.

**Interim NAP (before The REI Method is public-facing):** substitute "Coach Edmund Tan" for the Name field only; Address/Phone/Email/Website rules are identical.

**Citation targets, priority-ordered:**

| Priority | Platform | Type | Notes |
|---|---|---|---|
| 1 | Google Business Profile | Core | Covered above |
| 2 | Bing Places for Business | Core search engine | Free, mirrors GBP data; Bing increasingly feeds AI answer surfaces (Copilot), relevant to the AEO goal |
| 3 | Facebook Page (facebook.com/coachedmundtan) | Social + citation | Update About/NAP fields to match canonical block per `07_SOCIAL_PROFILE_REPOSITIONING.md` |
| 4 | LinkedIn Company Page | Social + citation | Create for The REI Method once launched; individual LinkedIn profiles for Edmund and Cindior are separate from this and covered in Phase 7 |
| 5 | PropNex agent profile pages (Edmund and Cindior individually) | Brokerage-mandated citation | These exist by virtue of CEA/PropNex registration — treat as **sameAs** assets (link targets for structured data on thereimethod.com) even though The REI Method doesn't control their content; keep NAP on them consistent with the canonical block wherever editable |
| 6 | PropertyGuru agent profile | Property-portal citation | High relevance to the category; verify current profile exists and matches NAP [VERIFY] |
| 7 | 99.co agent profile | Property-portal citation | Same treatment as PropertyGuru |
| 8 | EdgeProp agent profile | Property-portal citation | [VERIFY existence] |
| 9 | Yelp Singapore | General citation | Lower relevance for property advisory but a standard, low-effort citation for NAP consistency signal |
| 10 | Hotfrog SG | General directory citation | Low-effort NAP consistency signal |

Do not create citations under "The REI Method" on any platform until the name-sequencing decision in §2 has actually progressed to stage 2 — a citation naming a business that doesn't yet exist publicly is a worse signal than no citation at all.

---

## 11. Compliance Details

- **CEA registration numbers** for Edmund and Cindior, and the **PropNex licence number**, must appear on: thereimethod.com (footer or dedicated compliance page), and ideally in GBP's Q&A answer #9 above once known. They do not fit inside the 750-character GBP description (see §5) — do not compress the description to force them in; use the linked website instead. **[VERIFY both CEA reg. numbers and the PropNex licence number before any public GBP or web copy goes live — this blocks Q&A #9, the compliance footer, and any paid ad creative referencing licensing.]**
- **PDPA** in every review request and reactivation message: identify the sender, state the specific purpose, and provide an opt-out — built into all three templates in §8.
- The line **"This is advisory, not agency"** must not appear on the GBP profile in any form (description, posts, Q&A) per D7 — it is flagged as a compliance risk given both founders are licensed salespersons. Use D7's suggested replacement register instead: "Advisory-first. We plan the sequence before any transaction" if a similar line is ever needed in GBP copy.
- Do not state or imply guaranteed returns, guaranteed exit prices, or guaranteed NAV outcomes anywhere in GBP copy (description, services, posts, Q&A) — every dollar figure carries the [VERIFY] discipline from the master brief until confirmed against records, and none should appear in GBP copy until verified.

---

## 12. Local Authority Checklist (sequenced)

| Week | Action | Owner | Done-criterion |
|---|---|---|---|
| 1 | Complete the full audit in §1 against the live listing | Founders/ops | Every row in §1's table has a real value, no [VERIFY] left blank |
| 1 | Confirm listing ownership sits on a business-controlled Google account, transfer if needed | Founders | Listing manager list shows a business account, not a personal Gmail |
| 1 | Check for duplicate listings (§1 row 13) | Ops | Search confirms zero competing listings for the same entity |
| 2 | Correct name to interim state ("Coach Edmund Tan"), category, and address visibility (SAB) per §2/§3/§10 | Ops | Listing shows corrected name, primary category "Real estate consultant," address hidden, service area = Singapore |
| 2 | Set phone to +65 8786 3931, confirm hours field | Ops | Live listing phone matches GHL canonical number exactly |
| 3 | Shoot/collect photo assets per §6 (logo, cover, team, session, artefact close-ups) | Founders + photographer | At least 6 of the 7 assets in §6's table uploaded |
| 3 | Populate Services section per §4 | Ops | All 7 services live with descriptions under 300 characters each |
| 3 | Publish GBP description (interim wording) per §5 | Ops | Description live, character count re-verified post-edit |
| 4 | Seed Q&A per §7C | Ops | All 10 Q&A pairs posted from the business account |
| 4 | Build the GHL review-request workflow per §8 | GHL admin | Workflow triggers correctly off Position Map session completion in the 1-To-1 Pipeline, sends Template 1, respects PDPA consent field |
| 5 | Confirm CEA reg. numbers and PropNex licence number | Founders | Numbers confirmed and documented for use in §7C Q&A #9 and website footer |
| 5–10 | Run weekly Posts rotation per §7B | Ops/content | One post published every 7 days, pillar rotation followed |
| Ongoing | Monitor and respond to every new review within 48 hours using §8 response templates | Founders | No review older than 48 hours without a reply |
| Dependent on Phase 4/7 | Launch thereimethod.com, update Facebook/Instagram bios to reference The REI Method | Web + social owners | Public bios and live site both show "The REI Method" |
| Dependent on above | Rename/migrate GBP to "The REI Method" (§2 stage 2), relink website field (§9), update all citations (§10) | Ops | Canonical NAP block matches across GBP, website, Facebook, LinkedIn, and all citation targets |

---

## Concerns

- The instruction set assumes a single existing GBP-like listing behind the share.google link; if the audit in §1 reveals it is not actually a Google Business Profile (e.g., a Google Maps saved-place link or a Business Profile still in pending-verification state), the naming/category work in §2–§3 cannot proceed until it is a fully verified, editable listing. Flagging this explicitly since none of the source material confirms verification status.
- Path B (individual practitioner listings for both founders) is written up as an option but not recommended as a default build item — it adds a second listing to maintain, a second NAP surface to keep consistent, and depends on an [OPEN] decision (distinct contact details, Cindior's public-presence appetite) that isn't resolved in the master brief. Treat it as backlog, not part of the first 90 days.

---

## Questions To Clarify

1. What is the exact current name, category, address-visibility setting, and review count on the existing listing at share.google/bpyWTGgjlyNxt8Xiz? (Blocks nearly every section of this plan — see §1.)
2. Which Google account currently manages that listing, and is it a business-controlled account or a personal one?
3. CEA registration numbers for Edmund and Cindior, and the PropNex licence number (needed for §7C Q&A #9, §11, and the website compliance footer).
4. Does Cindior want her own individually discoverable public listing/profile (Path B, §2)? If yes, she needs a direct phone number and/or email distinct from the shared admin@thereimethod.com / +65 8786 3931.
5. Is there a genuine client-facing office anywhere, now or planned, that would change the Service Area Business recommendation in §10 to a storefront listing?
6. Does a Position Map session booking calendar exist yet as its own GHL calendar object, separate from the New Launch–branded "New Launch/Family Legacy Ladder" calendar (`34KkdVJncaYiuAOjE0FP`)?
7. Confirm current existence and NAP accuracy of PropertyGuru, 99.co, and EdgeProp agent profiles for both founders (§10 citation targets).

## Dependencies

- **D1 (entity model)** and **D2 (authority domain)** gate the naming sequencing in §2 — the GBP cannot correctly become "The REI Method" until thereimethod.com is live and social bios (Phase 7) reference the same name.
- **Phase 7 (`07_SOCIAL_PROFILE_REPOSITIONING.md`)** must land the Facebook/Instagram bio and NAP updates before §10's citation pass treats those platforms as consistent sources.
- **Phase 4 (`04_WEBSITE_SITEMAP_AND_PAGE_ROADMAP.md`)** must define the actual page slugs referenced in §7B Posts and §9 Services deep-links.
- **GHL** work: a dedicated Position Map session calendar object (currently absent — question 6 above) and the review-request workflow build in §8 depend on GHL admin access and on the PDPA consent field already existing on intake forms.
- **CEA/PropNex compliance confirmation** (registration numbers, licence number) blocks §7C Q&A #9, §11, and any paid promotion of the GBP profile.

## First 5 Actions

1. Run the full §1 audit against the live listing this week — every other action in this plan depends on knowing its current state.
2. Confirm listing ownership sits on a business-controlled Google account; transfer if it's on a personal Gmail.
3. Correct the interim name/category/address-visibility per §2/§3/§10 (name → "Coach Edmund Tan," primary category → Real estate consultant, address → hidden/Service Area Business).
4. Shoot the founder cover photo, team photo, and one anonymised Position Map artefact close-up (§6) — the minimum photo set needed before the profile looks credible.
5. Build the GHL review-request workflow (§8) so review velocity starts accumulating while the naming/category work above is still in progress — this does not need to wait for the rename sequencing.
