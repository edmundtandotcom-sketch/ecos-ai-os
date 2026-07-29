# Second Property Ladder — Landing Page Wireframes v1.1 (Phase 1B)

Version: v1.1
Status: APPROVED MASTER — approved by Coach Edmund 2026-07-16
Date: 2026-07-19
Owner: Coach Edmund (Programme Owner)
Supersedes: v1.0 — aligns authority, booked-session naming, Blueprint terminology and current master filenames after the 2026-07-19 Positioning & IP audit.
Sources: `10_MARKETING_FOUNDATION_v1.1.md`; `11_MINIMUM_SELECTION_DOCTRINE_v1.1.md`; `14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md`; `12_DECISION_RECONCILIATION.md`; Edmund's R-1–R-7 rulings.
Related: `10_MARKETING_FOUNDATION_v1.1.md` · `11_MINIMUM_SELECTION_DOCTRINE_v1.1.md` · `14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` · `12_DECISION_RECONCILIATION.md` · `13_CHANGELOG.md`

**Rule:** where this master conflicts with `10_MARKETING_FOUNDATION_v1.1.md` or `11_MINIMUM_SELECTION_DOCTRINE_v1.1.md`, those two masters win. Where it conflicts with `14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` on what the Check makes public, that document's public/backend boundary (its §2, inherited from Doctrine §2) wins.

**SCOPE BOUNDARY:** this is copy direction and wireframe structure only — real sample headlines, body copy, section order, CTA placement, and design direction in prose. It is not pixel design, not HTML/CSS/JS, not the actual page build, and does not wire any ad destination URL. A later Phase 1B implementation session builds from this document. No claim, CTA, or proof category below goes beyond what `10_MARKETING_FOUNDATION_v1.1.md` and `11_MINIMUM_SELECTION_DOCTRINE_v1.1.md` already approved.

---

## 0. Edmund's rulings (binding, 2026-07-16)

Recorded here as the governing decisions this entire document executes. Do not reopen.

| # | Ruling | Where applied below |
|---|---|---|
| **R-1** | **Tone and purpose.** The page is the opt-in gate before the Readiness Check — genuinely marketable and emotionally driven, not a technical rundown. Every section makes the specific reader recognise their own situation, builds toward "you need expert help, and it's obviously us" as an earned conclusion, and closes with clear next-step direction. | Throughout — §1, all section copy in §3–§4 |
| **R-2** | **Case study given real prominence.** One anonymised composite case study per door, as its own dedicated section, not folded into a generic proof grid. | §2.2 (Door A case study), §3.2 (Door B case study) |
| **R-3** | **Shared visual template.** Same layout/type/component system for both doors, door-specific imagery, subtle accent variation — not fully identical, not fully distinct. | §4.1 |
| **R-4** | **Readiness Check preview** shows only the three canonical route names plus one redacted/blurred sample result screen. No Check questions, gates, or scoring logic previewed. | §2.2, §3.2 (offer-bridge sub-section), §2.5, §3.5 (out-of-scope lists) |
| **R-5** | **Social proof format** = anonymised composite cases only. No named/attributed testimonials, no aggregate statistics/percentages. | §2.2, §3.2, §2.4, §3.4 (compliance guardrails), §2.5, §3.5 |
| **R-6** | **Hybrid hero.** Text-first hero (headline + subhead + CTA, no video); a short video sits lower, inside the case-study/proof section. | §2.1, §3.1 (hero), §4.2 (video placement note) |
| **R-7** | **Dynamic angle-matched hero — new scope.** Hero headline/subhead changes per the 12 locked ad angles via a URL parameter, falling back to the door's static default hero when no angle matches. Requires a later build phase to wire ad destination URLs. | §2.1, §3.1 (hero tables), §4.3 (technical dependency note) |

---

## 1. Purpose (R-1, read before everything below)

This page is not the sales pitch and not the diagnostic — it is the bridge between an ad and the Second Property Readiness Check™ (`10_MARKETING_FOUNDATION_v1.1.md` §10 offer bridge: *Ad or content → Second Property Readiness Check™ → result → appropriate CTA → Next Move Strategy Session™*). Its one job: make the specific reader see their own situation reflected back at them, let the belief reframe and proof do the convincing, and land on one unmistakably clear next step — never a menu of options.

Every headline below is adapted from a locked angle hook in `10_MARKETING_FOUNDATION_v1.1.md` §7 — none is invented. Every process claim traces to the Doctrine's public selection process (§3) or public/backend boundary (§2). Every proof reference traces to the Foundation's proof architecture (§8) and the Doctrine's illustrative case patterns (§10), built as anonymised composites per R-2/R-5 — never a named testimonial, never an aggregate statistic (blocked until the Rejection Ledger produces a measured figure, Doctrine §9, Foundation §11).

---

## 2. Door A — Second Property

**Audience** (Foundation §2): joint-name private-property owners; suitable EC owners; DINK couples; couples considering decoupling; existing owners actively wanting the next property.
**Core question** (Foundation §2): *How can we own the second property, and what must happen first?*
**Public wording** (Foundation §2): *Already own one property? See whether you can get the next one—and what must happen first.*
**Primary CTA** (Foundation §2, §9): **Check My Second-Property Route**

### 2.1 Dynamic hero system (R-7)

The hero band reads a `?angle=` URL parameter set by each ad's destination URL and swaps in the matching row below. If the parameter is absent or unrecognised, the page falls back to the static default hero (last row) — the door's own public wording, not a 13th invented angle.

| Angle code | Angle (Foundation §7) | Hero headline (sample copy) | Hero subhead (sample copy) |
|---|---|---|---|
| **A1** | Direct desire | Already own one property and want the next one? | Start with the route — not the viewing. See what must happen first, before you see another listing. |
| **A2** | Both names trapped | Both names on one property can feel safe. | Until you want the next one. See what your current name structure actually allows. |
| **A3** | Decoupling is not the strategy | Freeing one name is not the strategy. | The real question is what that name must achieve next. See whether decoupling actually makes sense for your route. |
| **A4** | The shrinking window | Your income may keep rising. | Your loan years and family flexibility will not. See what waiting could quietly change. |
| **A5** | One-property dependence | A property can rise in value and still leave you with only one option. | See what your current property could actually unlock next. |
| **A6** | Wrong order, right actions | Sell. Decouple. Refinance. Buy. | Each move may be correct on its own. The expensive mistake is doing them in the wrong order. See what must happen first. |
| **Default (fallback)** | — (door public wording, Foundation §2) | Already own one property? | See whether you can get the next one — and what must happen first. |

Each row's CTA button is the door's primary CTA unless the row's angle has a more specific CTA already locked in Foundation §7 (see per-angle CTA column below, used for the hero button text specifically):

| Angle | Hero CTA button (Foundation §7 CTA) |
|---|---|
| A1 | Check My Second-Property Route |
| A2 | See What Our Name Structure Allows |
| A3 | Check Whether Decoupling Makes Sense |
| A4 | See What Waiting Could Change |
| A5 | See What My Current Property Could Unlock |
| A6 | Show Me What Must Happen First |
| Default | Check My Second-Property Route |

### 2.2 Section-by-section wireframe

**1. Belief reframe** (Foundation §1, §3 Desire-Aware/Problem-Aware example lines)
> Headline: *Property was never the goal. Options were.*
> Body: "Owning one property already put you ahead of most households. But a good property can still be the wrong property for what comes next — if it's not creating the option to move again, the gain sitting in it may just be sitting idle. The question isn't whether your property did well. It's whether it's actually building toward your next move, or quietly boxing you into your only one."

**2. Value proposition** (Foundation §4)
> Headline: *Your next property gets a job description before it gets a name.*
> Body: "Most advisors start with what's available. We start with what your next property has to achieve — for your income, your names, your timeline, and the move after this one. A property that looks impressive but fails that job isn't a shortlisted option here, no matter how popular the project."

**3–5. Objection/angle sections** — expanded, full-body treatment of the three Door A angles not used as first-wave hero test variants (Foundation §7 "first test priority: A1, A3, A6" — these three carry the hero-swap emphasis; A2, A4, A5 below carry the static-body emphasis so the page adds new ground rather than repeating whichever hero the visitor just read):

- **Section 3 — Both names, one trap (A2):** *"Both names on one property can feel like the safe, responsible choice — until you want the next one."* Body: explains that ownership structure is a route decision, not an afterthought, and previews that the Blueprint addresses "what your current name structure actually allows" before any property search begins.
- **Section 4 — The window doesn't stay open (A4):** *"Your income may rise. Your available loan years and family flexibility do not stay unchanged forever."* Body: frames urgency honestly — not "buy now," but "know what waiting changes" — consistent with the cost-of-waiting section below and the prohibited-claims guardrail (§2.4) against implying immediate action is always correct.
- **Section 5 — One property, one option (A5):** *"A property can rise in value and still leave your family with only one option."* Body: reframes paper gains as unused potential, bridging directly into the value proposition's "job description" language.

**6. How the route is actually assessed** (Doctrine §3, verbatim public process)
> Headline: *How we actually assess your next move.*
> Body, walking through the five locked public steps in plain language: "**Define the Job** — what does your next property actually need to achieve for your household. **Set the Search Boundaries** — location, quantum, timing, and what must remain true afterward. **Remove Weak Fits** — most of what's on the market gets screened out before it ever reaches you. **Compare the Survivors** — what's left is compared on the things that actually matter to your plan. **Recommend the Best Fit** — one clear recommendation, not a pile of options to sort through yourself." *(Process wording locked verbatim per Doctrine §3 — no shorter or renamed variant.)*

**7. Case study** (R-2 — dedicated section, Doctrine §10 pattern 1: Decoupled couple)
> Headline: *One name, freed. Here's how we made sure it went to the right property.*
> Body (anonymised composite, no invented statistics): "A couple came to us already clear they wanted to free one name and use it to buy an investment property. The name wasn't the hard part — deciding what that name should actually buy was. We defined the job first: reasonable rental support, a future buyer pool wide enough to exit comfortably, a quantum that didn't strain the household, and enough room left to still make their own-stay move later. Several properties they'd already shortlisted themselves didn't survive that job — a niche one-bedroom unit with a thin resale audience, a project with heavy investor concentration, and one priced on a transformation story that hadn't happened yet. What we recommended instead protected the exact thing the freed name was meant to create: options, not just another purchase." *(Composite pattern per Doctrine §10, pattern 1 — "Decoupled couple.")*
>
> *Video note: a short video sits inside this section, reusing the production pattern already established by the diagnostic's results-video (build note only — see §5.2).*
>
> *Secondary case pattern available for future creative testing, not built out here: Doctrine §10 pattern 3 ("Existing condo owner" — keeping one property and adding another without duplicating the same exposure) — relevant to Door A's "existing owners actively wanting the next property" audience segment.*

**8. Cost of waiting** (Foundation §3 Problem-Aware example; guardrails per §2.4 below)
> Headline: *Waiting without knowing what you're waiting for is not a strategy.*
> Body: "Your property may have increased in value — but if it hasn't created your next move, the gain may still be sitting idle. (Foundation §3.) This isn't a push to act today. It's a question worth answering honestly: what, specifically, does waiting change for your household — your loan years, your names, your timeline?" *Any specific figure (loan tenure, ABSD rate, interest assumption) used here carries "DRAFT — pending platform verification" until fact-checked at implementation time, per constitution §11 and the same rule applied in `14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` §9.*

**9. Readiness Check offer-bridge** (R-4; Foundation §5, §10)
> Headline: *See which route fits — before you look at a single listing.*
> Body: previews the three canonical routes only, verbatim naming (Foundation §5): **Keep and Add** · **Sell and Rebuild** · **Strengthen One First**. One line each, held to the public boundary (Doctrine §2 — what the Readiness Check stage may show: indicative route, main readiness gaps, possible cost of waiting, next recommended action):
> - *Keep and Add* — "Keep what you have, restructure if needed, add another."
> - *Sell and Rebuild* — "Sell, release the funds, buy stronger — possibly two."
> - *Strengthen One First* — "Get one property working harder before adding a second."
>
> Below the three routes, a **redacted/blurred sample result screen** — a simple mockup panel labelled *"Sample result — details blurred"* showing a generic result-card layout (route name, a one-line readiness note, a CTA) with all specific numbers, names, and property details visibly obscured, existing purely as proof the method produces a real, structured output. **No actual Check question, gate condition, or scoring mechanic is shown or implied** (Readiness Check §7, §11 remain internal — see §2.5 out-of-scope below).

**10. FAQ — objection handling** (Doctrine §4, §6, §7, §9 mechanisms, in plain public language — the 4-tier risk classification is never named on-page)
- *"Will you just tell me a property is bad, or actually explain why?"* → "We don't use a rigid pass/fail list. Every property is judged against your specific plan — sometimes a weaker area is worth accepting if the trade-off is right for your household, and we document exactly why before you decide." (Doctrine §4, override mechanism, plain language.)
- *"How do I know I can actually afford it beyond just the bank's approval?"* → "Before you view anything, we check that you can comfortably hold the property for at least a year of full costs — mortgage, maintenance, tax — not just what a bank pre-approval says you qualify for." (Doctrine §6, Safety Net, plain language.)
- *"What if the market shifts after I buy?"* → "We look at who would realistically want to buy this exact property from you in future — not just whether it looks good today." (Doctrine §7, future-buyer analysis, plain language.)
- *"Do you just match me to whatever's available right now?"* → "No. We define what your next property actually needs to achieve for your household first — then we look at what's on the market, not the other way around." (Doctrine §5, Property Job, plain language.)
- *"How much of the market do you actually rule out?"* → "We screen the relevant market and remove most options before producing the shortlist." *(Public wording locked verbatim, Doctrine §9 / Foundation §11 — no percentage used.)*

**11. Final CTA section**
> Headline: *Your next property gets a job description before it gets a name.*
> Body: "See which route fits your household — Keep and Add, Sell and Rebuild, or Strengthen One First — before you look at a single listing."
> Button: **Check My Second-Property Route**

### 2.3 CTA placement table (Door A)

| Section | CTA used | Source (Foundation §9) |
|---|---|---|
| Hero (per angle) | Angle-specific CTA (see §2.1 table) | §7 per-angle CTAs |
| Belief reframe / value proposition | (no button — pure reframe, first CTA appears at objection sections) | — |
| Objection sections 3–5 | See What Our Name Structure Allows / See What Waiting Could Change / See What My Current Property Could Unlock | §7 A2/A4/A5 |
| How the route is assessed | Check Whether You Can Own the Next Property | §9 "Second-property ad" row |
| Case study | See What Your Current Property Could Unlock *(soft, secondary link only — primary CTA stays reserved for the offer-bridge and final sections)* | §9 "Broad emotional content" row |
| Cost of waiting | See What Waiting Could Cost Me | §9 "Cost-of-waiting content" row |
| Readiness Check offer-bridge | Map My Best Route | §9 "Diagnostic result" row |
| FAQ | Check Whether Freeing One Name Makes Sense *(only on the override-mechanism FAQ item, where relevant)* | §9 "Decoupling content" row |
| Final CTA | Check My Second-Property Route | §2 primary CTA / §9 |

Edmund's standing CTA standard applies unchanged (Foundation §9): no CTA defaults to a generic "book a call" — each matches what that section just convinced the reader of.

### 2.4 Compliance guardrails inline (Door A)

Applying Foundation §11 verbatim, at the points of highest careless-copywriter risk on this page:

- **Belief reframe / cost-of-waiting sections:** never imply acting immediately is always better than waiting (§11). The locked honest line stands: "waiting without knowing what you are waiting for is not a strategy," never "waiting is wrong."
- **Objection section A3 / decoupling FAQ:** never state or imply decoupling is always correct, or that ABSD can always be avoided (§11).
- **Case study / value proposition:** never promise everyone can own a second property (§11) — the composite case shows judgement and rejection, not a guaranteed outcome.
- **Readiness Check offer-bridge / FAQ "how much do you rule out":** never state the 90% figure publicly — only the locked wording "We screen the relevant market and remove most options before producing the shortlist" (Doctrine §9, Foundation §11).
- **Cost-of-waiting figures:** any specific loan-tenure, interest-rate, or ABSD figure carries "DRAFT — pending platform verification" until fact-checked (constitution §11).
- **Financing language (A6, FAQ):** never imply guaranteed financing approval or guaranteed profit (§11).

### 2.5 Explicitly out of scope (Door A page)

- Backend system names — REI Method, ProDeck, Ascent Model, Trigger Questions, RAM, or any internal diagnostic code (Foundation §6).
- The exact ranked shortlist, full project/unit research, or detailed scoring/weighting (Doctrine §2, "keep for engaged clients only").
- The Readiness Check's internal question bank, gate logic, or scoring mechanic (`14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` §§4, 5, 6, 7, 11 — internal/backend).
- The public 90% disqualification figure as a stated percentage (Doctrine §9).
- The retired route-naming scheme "Hold Two / Trade Up First / Prepare Before Moving" (superseded per Foundation §5, U-3).
- Named/attributed testimonials of any kind (R-5) and aggregate statistics/percentages of any kind (R-5, blocked until the Rejection Ledger produces a measured figure).

---

## 3. Door B — HDB/EC Next Route

**Audience** (Foundation §2): HDB owners at approximately **S$800,000+**; EC owners at approximately **S$1.5 million+**; households deciding whether to keep, sell, upgrade, restructure or build towards two.
**Core question** (Foundation §2): *What should our current HDB or EC unlock next?*
**Public qualification callout** (Foundation §2): *Own an HDB worth around S$800K+ or an EC worth around S$1.5M+?*
**Primary CTA** (Foundation §2, §9): **Compare My Keep, Sell or Upgrade Routes**

### 3.1 Dynamic hero system (R-7)

Same mechanism as Door A (§2.1): reads `?angle=`, swaps the matching row, falls back to the static default hero if absent/unmatched.

| Angle code | Angle (Foundation §7) | Hero headline (sample copy) | Hero subhead (sample copy) |
|---|---|---|---|
| **B1** | Keep or sell | Is your HDB or EC still helping your next move? | Or is it quietly delaying it? Compare your keep or sell routes before you decide either way. |
| **B2** | Buy one or plan for two | After selling your HDB or EC — one stronger property, or two? | Compare the one-vs-two route before you commit to either. |
| **B3** | Paper gain, no plan | Your home may have increased in value. | But has that gain actually created a better next move? See what your gain could unlock. |
| **B4** | Two clean names | Two available names can create options. | Or they can be used up in one decision you can't easily reverse. Check how you should actually use them. |
| **B5** | Sell high, buy high paralysis | Selling high doesn't help if you land in the same position. | Just at a higher price. Compare your real upgrade routes first. |
| **B6** | Waiting without a target | Waiting can be the right move. | But waiting without knowing what must change first is not a strategy. See whether waiting still helps you. |
| **Default (fallback)** | — (door public wording, Foundation §2) | Own an HDB worth around S$800K+ or an EC worth around S$1.5M+? | See what your current HDB or EC should unlock next. |

Hero CTA buttons per angle (Foundation §7 per-angle CTA):

| Angle | Hero CTA button |
|---|---|
| B1 | Compare My Keep or Sell Routes |
| B2 | Compare My One-vs-Two Route |
| B3 | See What My Gain Could Unlock |
| B4 | Check How We Should Use Our Names |
| B5 | Compare My Real Upgrade Routes |
| B6 | See Whether Waiting Still Helps |
| Default | Compare My Keep, Sell or Upgrade Routes |

### 3.2 Section-by-section wireframe

**1. Belief reframe** (Foundation §1, §3)
> Headline: *Property was never the goal. Options were.*
> Body: "Your HDB or EC may already have done its job well — but the question now isn't whether it performed. It's whether it's still helping your next move, or quietly holding you in place. A good property can still be the wrong property for what your household needs next."

**2. Value proposition** (Foundation §4)
> Headline: *Your next property gets a job description before it gets a name.*
> Body: "Before we talk about keeping, selling, or upgrading, we define what your next property actually needs to do — support your family's lifestyle, remain affordable as expenses grow, and still leave room for the move after this one. Then, and only then, do we compare what that looks like against staying put."

**3–5. Objection/angle sections** — expanded body treatment of the three Door B angles not used as first-wave hero test variants (Foundation §7 "first test priority: B2, B3, B6" carry hero emphasis; B1, B4, B5 below carry static-body emphasis so the page adds new ground rather than repeating whichever hero the visitor just read):

- **Section 3 — Helping, or delaying (B1):** *"Is your HDB or EC still helping your next move—or quietly delaying it?"* Body: reframes "keep vs sell" as a route decision tied to the household's actual plan, not a market-timing guess.
- **Section 4 — Two names, one decision (B4):** *"Two available names can create options—or be used up in one decision you cannot easily reverse."* Body: connects directly to the "how the route is assessed" section below — ownership structure is part of the Property Job, decided before any project is chosen.
- **Section 5 — Higher price, same position (B5):** *"Selling high does not help if the next purchase leaves you in the same position—just at a higher price."* Body: distinguishes a real upgrade from a lateral move dressed up as one.

**6. How the route is actually assessed** (Doctrine §3, verbatim public process)
> Headline: *How we actually assess your next move.*
> Body (same locked five-step wording as Door A, reframed for a keep/sell decision): "**Define the Job** — own-stay, investment, or both, and what your household actually needs from the next property. **Set the Search Boundaries** — timing (including MOP/SSD position), quantum, and location. **Remove Weak Fits** — most alternatives get screened out before they reach you. **Compare the Survivors** — judged on what matters to your family's plan, not just price per square foot. **Recommend the Best Fit** — one clear recommendation for whether to keep, sell, or upgrade, and what to buy if you move." *(Verbatim per Doctrine §3.)*

**7. Case study** (R-2 — dedicated section, Doctrine §10 pattern 2: HDB family upgrading)
> Headline: *One family's HDB sale — here's how we made sure the upgrade actually upgraded them.*
> Body (anonymised composite, no invented statistics): "A family came to us set on selling their HDB and moving into a private property. The desire was clear; what the next property had to do for them wasn't yet. We defined the job first: something that supported their lifestyle as it was and as their children grew, stayed affordable through those growing expenses rather than just at the point of purchase, held its value across the holding period, and still left room for an investment property later. That job ruled out several options they'd already been drawn to — units too small for the family's actual usage, a monthly commitment that looked fine on paper but stretched too thin against rising family expenses, one project with a thin resale pool of family buyers, and another whose eventual exit price outran what a realistic future buyer could afford. What we recommended instead was the one option that did the job on every count that mattered to them, not just the one that showed best." *(Composite pattern per Doctrine §10, pattern 2 — "HDB family moving into private property.")*
>
> *Video note: a short video sits inside this section, reusing the production pattern already established by the diagnostic's results-video (build note only — see §5.2).*

**8. Cost of waiting** (Foundation §3 Problem-Aware example; guardrails per §3.4 below)
> Headline: *Waiting without knowing what you're waiting for is not a strategy.*
> Body: "Your property may have increased in value — but if it hasn't created your next move, the gain may still be sitting idle. (Foundation §3.) This isn't a push to sell today. It's worth knowing plainly: what does waiting change for your MOP or SSD position, your names, your family's timeline?" *Any specific figure used here (MOP/SSD rules, interest-rate assumptions, ABSD rates) carries "DRAFT — pending platform verification" until fact-checked at implementation time, per constitution §11 and the same rule applied in `14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` §9.*

**9. Readiness Check offer-bridge** (R-4; Foundation §5, §10)
> Headline: *See which route fits — before you list or view anything.*
> Body: same three canonical routes, verbatim naming (Foundation §5): **Keep and Add** · **Sell and Rebuild** · **Strengthen One First** — one line each, held to the same public boundary as Door A (Doctrine §2):
> - *Keep and Add* — "Keep your HDB or EC, restructure if needed, add another."
> - *Sell and Rebuild* — "Sell, release the funds, buy one stronger property — possibly two."
> - *Strengthen One First* — "Reposition into one stronger property before adding a second."
>
> Same redacted/blurred sample result screen pattern as Door A (§2.2 section 9) — a generic result-card mockup with all specifics obscured, proving the method produces a real structured output. **No Check question, gate condition, or scoring mechanic shown or implied.**

**10. FAQ — objection handling** (Doctrine §4, §6, §7, §9 mechanisms, plain public language — 4-tier classification never named)
- *"Will you just tell me to sell, or actually explain why?"* → same override-mechanism answer as Door A §2.2 section 10, adapted: "We don't use a rigid keep/sell rule. Every option is judged against your household's plan, and if a trade-off makes sense for your family, we document exactly why before you decide."
- *"How do I know we can actually afford the upgrade long-term?"* → "Before any upgrade, we check you can comfortably hold the new commitment for at least a year of full costs — not just what the bank's pre-approval says." (Doctrine §6, Safety Net.)
- *"What if I sell high and the market shifts before my next purchase?"* → "We look at who would realistically want to buy your next property from you in future — so 'selling high' doesn't just mean 'buying high' right back." (Doctrine §7, future-buyer analysis.)
- *"Are you just going to show me whatever's listed?"* → "No. We define what your next property needs to achieve for your family first — then compare what's actually available against that job." (Doctrine §5, Property Job.)
- *"How much of the market do you rule out?"* → "We screen the relevant market and remove most options before producing the shortlist." *(Locked verbatim, Doctrine §9 / Foundation §11 — no percentage used.)*

**11. Final CTA section**
> Headline: *Your next property gets a job description before it gets a name.*
> Body: "See which route fits your household — Keep and Add, Sell and Rebuild, or Strengthen One First — before you list or view anything."
> Button: **Compare My Keep, Sell or Upgrade Routes**

### 3.3 CTA placement table (Door B)

| Section | CTA used | Source (Foundation §9) |
|---|---|---|
| Hero (per angle) | Angle-specific CTA (see §3.1 table) | §7 per-angle CTAs |
| Belief reframe / value proposition | (no button — pure reframe) | — |
| Objection sections 3–5 | Compare My Keep or Sell Routes / Check How We Should Use Our Names / Compare My Real Upgrade Routes | §7 B1/B4/B5 |
| How the route is assessed | Compare My Keep, Sell or Upgrade Routes | §9 "HDB/EC content" row |
| Case study | See What Your Current Property Could Unlock *(soft, secondary link only)* | §9 "Broad emotional content" row |
| Cost of waiting | See What Waiting Could Cost Me | §9 "Cost-of-waiting content" row |
| Readiness Check offer-bridge | Map My Best Route | §9 "Diagnostic result" row |
| FAQ | Check Whether Freeing One Name Makes Sense *(only on the override-mechanism FAQ item, where relevant — same placement as Door A)* | §9 "Decoupling content" row |
| Final CTA | Compare My Keep, Sell or Upgrade Routes | §2 primary CTA / §9 |

### 3.4 Compliance guardrails inline (Door B)

Applying Foundation §11 verbatim, at the points of highest careless-copywriter risk:

- **Belief reframe / cost-of-waiting:** never imply selling or acting immediately is always better than waiting (§11). Locked honest line stands: "waiting without knowing what you are waiting for is not a strategy."
- **Objection section B4 / FAQ "two names":** never state or imply decoupling or any name-restructuring move is always correct, or that ABSD can always be avoided (§11).
- **Case study / value proposition:** never promise every HDB/EC household can successfully upgrade or build toward two (§11) — the composite case shows judgement and rejection, not a guaranteed outcome.
- **Readiness Check offer-bridge / FAQ "how much do you rule out":** never state the 90% figure publicly — only the locked wording (Doctrine §9, Foundation §11).
- **Cost-of-waiting figures (MOP/SSD, interest rate, ABSD):** carry "DRAFT — pending platform verification" until fact-checked (constitution §11).
- **Financing/sale-readiness language:** never imply guaranteed financing approval, guaranteed sale price, or guaranteed profit (§11).

### 3.5 Explicitly out of scope (Door B page)

- Backend system names — REI Method, ProDeck, Ascent Model, Trigger Questions, RAM, or any internal diagnostic code (Foundation §6).
- The exact ranked shortlist, full project/unit research, or detailed scoring/weighting (Doctrine §2).
- The Readiness Check's internal question bank, gate logic, or scoring mechanic (`14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` §§4, 5, 6, 7, 11).
- The public 90% disqualification figure as a stated percentage (Doctrine §9).
- The retired route-naming scheme "Hold Two / Trade Up First / Prepare Before Moving" (superseded per Foundation §5, U-3).
- Named/attributed testimonials of any kind (R-5) and aggregate statistics/percentages of any kind (R-5).

---

## 4. Shared system (applies to both doors)

### 4.1 Visual/design system direction (R-3)

One shared design system, door-specific variation layered on top — not a pixel spec, a direction for the later build:

- **Layout and component structure:** identical page skeleton for both doors — hero band (headline/subhead/CTA, no video per R-6) → belief reframe → value proposition → three objection sections (same card/block component, reused) → "how the route is assessed" (same five-step visual component, e.g. a horizontal step tracker) → case-study section (same layout slot, video embed lower in this block per R-6) → cost-of-waiting block → Readiness Check offer-bridge (same three-route card component + redacted-sample mockup panel) → FAQ accordion (same component) → final CTA band.
- **Typography and component library:** shared across both doors — same heading/body type scale, same button style, same card/accordion components. Building two independent designs is out of scope; this is one system with a data-driven skin.
- **Door-specific imagery direction:** Door A uses private-property and landed-home imagery (facades, living spaces suited to joint-name owners/DINK couples/EC-to-private movers). Door B uses HDB/EC block and estate imagery (void decks, HDB towns, EC facades) — reflecting each door's actual audience (Foundation §2) rather than generic stock property photography.
- **Subtle accent variation:** a single accent-color or accent-motif shift between doors (e.g. one accent hue for Door A, a distinguishable but harmonious accent hue for Door B) applied to CTA buttons, section dividers, and the route-card component — enough for a visitor to sense "this is the HDB/EC page" vs "this is the second-property page" without the two pages reading as unrelated products. Exact color values are an implementation-phase decision, not specified here.

### 4.2 Video placement note (R-6)

Both doors keep the hero text-first (headline + subhead + CTA, no video) for instant ad message-match and fast load. A short video is placed lower on the page, inside the dedicated case-study section (§2.2 section 7 / §3.2 section 7) — reusing the production pattern already established by the existing diagnostic's results-video section (`_BACKUPS\ECOS_BACKUPS\DIAGNOSTIC_APP_RECOVERY_LIVE_v2.3_2026-07-12` — referenced only as a build note; that build is untouched and not specified further here). Video content, length, and script are implementation-phase work, not designed in this document.

### 4.3 Dynamic hero technical dependency note (R-7)

This document specifies the *mechanism* only, as a dependency the later implementation phase must wire — it does not build it:

- The page reads an angle-identifying URL parameter (e.g. `?angle=A1` for Door A, `?angle=B3` for Door B) appended to each ad's destination URL.
- On load, the page matches the parameter against the door's 6-row hero table (§2.1 / §3.1) and swaps in that row's headline, subhead, and CTA button text.
- If the parameter is absent, malformed, or does not match a known code for that door, the page falls back to the door's static default hero row (last row of each table) — never a 13th invented angle.
- **Build dependency flagged here, not resolved here:** every ad's destination URL must be wired with the correct `?angle=` parameter matching the ad's actual angle at campaign-build time (Phase 1C, per Foundation §14). This document identifies the dependency; ad destination URL wiring itself is out of scope (§4.4).

### 4.4 Out of scope for this document overall

- The actual landing-page code or build (HTML/CSS/JS, CMS/page-builder implementation).
- Wiring real ad destination URLs with the `?angle=` parameter (Phase 1C build dependency, §4.3).
- Video production for the case-study section video (§4.2 build note only).
- Any client-consent workflow for future named testimonials — not designed here, and not needed while R-5's anonymised-composite-only rule holds.
- Everything already out of scope in `10_MARKETING_FOUNDATION_v1.1.md` §13 and `14_SECOND_PROPERTY_READINESS_CHECK_v1.1.md` §13 (REI Method operational rebuild, Year-4 Exit Review Doctrine, the 8-stage buyer consult journey beyond Self-Assessment, the $5M+ segment as a dedicated door, SRX X-Value licensing, `spl_*` data migration).

---

## 5. Next step

Per `10_MARKETING_FOUNDATION_v1.1.md` §14, this closes the Phase 1B wireframe layer. Phase 1C (first creative test packs — three angles per door, multiple treatments per angle) is next, and depends on this document's §4.3 dynamic-hero technical dependency being wired at build time. Phase 1D (proof system) follows.

Approved by Coach Edmund 2026-07-16.
