# Second Property Ladder — Second Property Readiness Check™ v1.0 (Phase 1A Strategy)

Version: v1.0
Status: APPROVED MASTER — approved by Coach Edmund 2026-07-16
Date: 2026-07-16
Owner: Coach Edmund (Programme Owner)
Supersedes: none as a strategy master. **Replaces the strategy layer of the live "Which Move Are You On?" diagnostic** (`Which_Move_Are_You_On_Diagnostic.md` v1.2) per Edmund's ruling R-1 (2026-07-16) — see Section 2. That file and the live `01_DIAGNOSTIC_APP\` build are untouched, read-only reference until a separate future implementation/cutover session executes the replacement.
Sources: `10_MARKETING_FOUNDATION_v1.0.md` (APPROVED MASTER, esp. §§1–2, 5, 9, 11, 14) · `11_MINIMUM_SELECTION_DOCTRINE_v1.0.md` (APPROVED MASTER, esp. §2 "what each stage provides") · `12_UNRESOLVED_DECISIONS.md` (U-1, U-3, U-4, U-5) · `01_PHASE_1_MARKETING_FOUNDATION\90_SOURCE_MARKDOWN\02_SECOND_LADDER_NEW_EXECUTION.md` (8-stage buyer journey, Table 5 readiness-dimension mapping, direct-desire bank) · `Which_Move_Are_You_On_Diagnostic.md` v1.2 (existing live diagnostic — read-only reference for question patterns, `spl_*` field naming, tag vocabulary, "never say no on screen" rule) · `01_DIAGNOSTIC_APP\GO_LIVE_RUNBOOK_v1.1.md` + `_INDEX.md` (live build/host status, read-only reference) · `00_COMMAND_CENTER\04_DECISION_MEMORY.md` Decision 073 (close-label vocabulary) · Edmund's rulings R-1–R-5 (2026-07-16, this session)
Related: `10_MARKETING_FOUNDATION_v1.0.md` · `11_MINIMUM_SELECTION_DOCTRINE_v1.0.md` · `12_UNRESOLVED_DECISIONS.md` · `13_CHANGELOG.md`

**Rule:** where this master conflicts with `10_MARKETING_FOUNDATION_v1.0.md` or `11_MINIMUM_SELECTION_DOCTRINE_v1.0.md`, those two masters win. Where it conflicts with the AI OS constitution (`00_AI_OPERATING_SYSTEM\CLAUDE.md` v4.3), see the naming note inherited from the Marketing Foundation master §1 and `12_UNRESOLVED_DECISIONS.md` (U-1) — this document uses the Phase 1 package's renamed session/deliverable terms throughout.

**SCOPE BOUNDARY:** this is a strategy specification only — question groups, flow logic, scoring, disqualification/routing, result-page content boundaries, CTA routing, GHL field spec, and valuation methodology. It is not code, not a rebuild instruction, and does not touch, edit, or reference-edit any file under `01_DIAGNOSTIC_APP\` or the live diagnostic build. A later, separate implementation phase builds from this document.

---

## 0. Edmund's rulings (binding, 2026-07-16)

Recorded here as the governing decisions this entire document executes. Do not reopen.

| # | Ruling | Where applied below |
|---|---|---|
| **R-1** | **Replace**, not merge, the live diagnostic. New title **Second Property Readiness Check™**. New URL slug proposed (DRAFT, pending Edmund's final confirmation — touches live infrastructure). New GHL field namespace **`sprc_*`**; old `spl_*` fields become legacy/deprecated, not deleted (deletion is a separate future data-migration decision). Lead-grade vocabulary aligns with **Decision 073: Proceed / Prepare / Nurture / No Fit** — not the old A/B/P/C grading, not a fifth vocabulary. UI/UX must be meaningfully better than the existing tool (build-phase requirement, not designed here). | §2, §5, §7, §11 |
| **R-2** | **Dynamic mid-flow branching.** A shared opening block surfaces which door the prospect is in, then the flow branches into meaningfully different Door A and Door B question paths (not cosmetic wording swaps), reconverging into one scoring/route-output structure. | §3, §4 |
| **R-3** | **DIY free estimator** for property value: self-report band is primary; a "not sure, estimate for me" fallback computes a same-town/type/area-band average from data.gov.sg / URA free public transaction data — labelled an estimate range, not a valuation, DRAFT pending platform verification. SRX X-Value licensing is a possible future upgrade path, out of scope now. | §12 |
| **R-4** | **12–14 questions total**, either path, matching the existing tool's proven completion-rate benchmark. | §4 |
| **R-5** | **No new nurture asset.** The Prepare First result routes to the already-locked CTA **"Show Me What to Do First"** and existing Marketing Foundation copy patterns only. | §7, §8, §10 |

---

## 1. Objective

**Prospect value:** in under 3 minutes, a Property Climber sees what their current property (or properties) can realistically unlock next, what's blocking the move, which of the three canonical routes looks most relevant to them, and what waiting might quietly cost — without being sold a project, a unit, or a hard "no."

**Business value:** this is the offer bridge specified in `10_MARKETING_FOUNDATION_v1.0.md` §10 — *Ad or content → Second Property Readiness Check™ → result → appropriate CTA → Second Property Strategy Session™.* It is the single entry point behind both campaign doors (§2 of the Marketing Foundation master: "one Second Property Readiness Check™, one GHL contact database, one pipeline"). Its job is to qualify silently, teach the category vocabulary (Move, Route, Exit Before Entry™) as the respondent answers, and route every lead — qualified or not — to a useful next step.

This document supersedes, as a matter of business direction, the strategy the live "Which Move Are You On?" diagnostic currently implements. See §2 for exactly what changes and why.

---

## 2. Relationship to the existing live diagnostic

**Decision: REPLACE (R-1).** Not kept in parallel, not merged as-is. Rationale on file: naming has moved on (Decision 055 "Move" vocabulary, then the Phase 1 rename in `10_MARKETING_FOUNDATION_v1.0.md` §1), the route naming has moved on (U-3: "Keep and Add / Sell and Rebuild / Strengthen One First" retires "Hold Two / Trade Up First / Prepare Before Moving"), and the two-door campaign architecture (§2 of that master) needs a diagnostic that actually branches by door — the live tool has one linear question path for everyone.

| | Existing live tool | This replacement |
|---|---|---|
| Title | "Which Move Are You On?" | **Second Property Readiness Check™** |
| Live URL | `legacylaunch.com.sg/diagnostic` | New slug (below) |
| Flow | One linear 14-question path, same for every respondent | Shared opening block + dynamic Door A / Door B branch (§3) |
| Route/outcome naming | Move 1–5 result + A/B/P/C lead grade | Route A/B/C + Prepare First outcome; Proceed/Prepare/Nurture/No Fit lead grade (Decision 073) |
| GHL fields | `spl_*` namespace | `sprc_*` namespace (new) |
| Host | GHL-native page (canonical) + a superseded parallel Apps Script deployment (see `01_DIAGNOSTIC_APP\_INDEX.md`) | Not specified here — hosting/build is implementation-phase scope |

**Proposed new URL slug (DRAFT — pending Edmund's final confirmation, since this touches live infrastructure and redirects):** `/second-property-readiness`. Rationale: shortest slug that still reads as the locked title, avoids the retired "diagnostic" framing, and leaves room for a `/second-property-readiness-check` long form as an alias if SEO/ads copy prefers the fuller phrase. **Do not treat this slug as final** — Edmund confirms the exact path (and whether `/diagnostic` 301-redirects to it or is retired outright) before any implementation session touches DNS, GHL funnel routing, or ad destination URLs.

**Legacy field deprecation:** every `spl_*` field (`spl_move_result`, `spl_total_score`, `spl_band`, `spl_lead_grade`, `spl_gate_*`, `spl_c1`–`spl_c10`) becomes **legacy** the moment `sprc_*` logic goes live. Do not delete them from GHL — historical contact records and any live workflow still referencing them stay intact until a separate, deliberate data-migration session decides what (if anything) gets backfilled or archived. No new automation should read or write `spl_*` fields after cutover.

**UI/UX improvement requirement (build note, not designed here):** the existing tool's known UX debt — mobile scroll/centering fixes needed across v2.0–v2.3, multiple incremental patches to get contrast and Back-button behaviour right (see `01_DIAGNOSTIC_APP\_INDEX.md`) — is not something to inherit by default. The later implementation phase must treat "meaningfully better UI/UX than the existing tool" as a build requirement, evaluated against the shipped `index_LIVE_v2.3.html` as the baseline to beat. This document does not specify pixel-level design; that is the implementation phase's job.

**Reconciliation note (U-4):** the 8-stage buyer consult journey (Attention → Self-Assessment → Conversation → Booking → Preparation → Strategy Session → Implementation → Review, from `90_SOURCE_MARKDOWN\02_SECOND_LADDER_NEW_EXECUTION.md`) was deferred to "the Phase 1A Readiness Check build" per U-4. This document is that build's strategy layer, and it satisfies U-4 narrowly: the Readiness Check corresponds to the journey's **Self-Assessment** stage only ("Am I actually in a position to make another move?" — Table 2 of the source doc). It does not attempt to re-spec Conversation, Booking, Preparation, or the remaining stages — that full journey reconciliation against the locked Discovery → Review → Evaluate → Identify structure is separate future work (see §13).

---

## 3. Flow structure

Per R-2: a shared opening block, a single branch point, then two meaningfully different door-specific paths that reconverge into one scoring/route-output structure. No new proprietary framework name is introduced for this mechanism (per Marketing Foundation §6 — don't create another branded layer); it is described in plain terms below.

### 3.1 Shared opening block (4 questions — S1–S4)

Common to every respondent, regardless of eventual door. Purpose: capture the minimum needed to route correctly, and start the "position map" framing immediately.

| ID | Question | Purpose |
|---|---|---|
| **S1** | *Which best describes your property situation today?* — I own one HDB flat / I own one EC / I own one private condo or landed property / I own two or more properties / I don't own yet (renting or with family) | **Primary branch determinant** (see 3.2) |
| **S2** | *How many properties do you and your household currently hold?* — 1 / 2 or more | Refines S1 for the 2+ segment (portfolio framing carried into whichever door applies — see 3.2) |
| **S3** | *Which feels closer to true for you right now?* — We want to know if/how we can get a next property / We want to know what to do with our current property (keep, sell or upgrade) / Honestly, both / Not sure yet | **Secondary branch determinant** for ambiguous cases (esp. EC owners — see 3.2); also seeds the Direction & Goal readiness dimension |
| **S4** | *When would you want your next property move to actually happen?* — Within 6 months / 6–18 months / 18+ months / Just exploring for now | Feeds the Timing & Action Readiness dimension and the lead-grade timeline gate; identical wording works for either door, so it stays in the shared block rather than being duplicated |

### 3.2 Branch-point logic

The branch fires after S3, using S1 + S3 together (S1 alone is ambiguous for EC owners, since Door A's audience includes "suitable EC owners" while Door B's audience is specifically HDB/EC owners deciding keep/sell/upgrade — see `10_MARKETING_FOUNDATION_v1.0.md` §2):

| S1 answer | S3 answer | Branch |
|---|---|---|
| Private condo or landed, or "2 or more" properties | any | **Door A** |
| HDB | any | **Door B** |
| EC | "get a next property" | **Door A** (EC owner treating current EC as the base for the next move) |
| EC | "what to do with our current property" or "both" or "not sure" | **Door B** (EC owner deciding keep/sell/upgrade first) |
| "Don't own yet" | any | **Nurture routing** — runs a shortened version of the Door B question set (renting households most resemble a pre-HDB/EC position) so they still get a Move-style result, but lands on Nurture lead grade regardless of other answers (§7) |

Respondents already on 2+ properties keep an internal portfolio flag (`sprc_gate_portfolio = 2plus`) carried through Door A so the advisor-facing context preserves the "is your second property pulling its weight" framing the old tool's P-grade gave — this is call-prep context, not a third door and not a fourth route.

The **$5M+ segment** (U-5) is not a separate door here either — high-value private/landed owners simply flow through Door A on their actual answers, consistent with U-5's "in-category, not a dedicated door" ruling.

### 3.3 Door A path — Second Property (already own private/EC, deciding on a second)

Meaningfully different from Door B because the decision Door A prospects face is *whether and how to add*, not *whether to keep or sell what they have*. Question content per §4.1.

### 3.4 Door B path — HDB/EC Next Route (deciding keep/sell/upgrade/build toward two)

Meaningfully different from Door A because the decision is *whether the current asset should even continue in its current form* — MOP/SSD timing, family-driven upgrade triggers, and a keep-vs-sell fork that Door A prospects don't face. Question content per §4.2.

Both paths converge on the same five outputs: Readiness Score/Band (§6), Route result (§5), Lead grade (§7), Result page (§8), CTA (§10) — one backend, per the Marketing Foundation's "two doors, one backend" architecture (§2).

---

## 4. Question groups

Total per path = 4 shared + 9 door-specific = **13 questions**, inside the R-4 band (12–14) and matching the old tool's proven 14-question benchmark closely enough to expect a comparable completion rate.

Each door-specific path carries exactly **five scored checkpoints** — one per readiness dimension (Table 5, `02_SECOND_LADDER_NEW_EXECUTION.md`) — plus **four gate questions** (ownership/value/income/age, non-scored, drive lead grade and route). This is deliberately lighter than the old tool's ten-checkpoint model (§6 explains why).

### 4.1 Door A question bank (A1–A9)

| ID | Question | Type | Dimension (Table 5) |
|---|---|---|---|
| A1 | Property value — self-report band, with "not sure, estimate for me" fallback (§12) | Gate | Current Position |
| A2 | *If you sold or refinanced tomorrow, do you know the CPF refund and the cash you'd actually walk away with?* — Yes, both numbers / I know the CPF used, not the accrued interest / No idea | **Scored (2/1/0)** | Current Position |
| A3 | *Do you know whether getting a second property means keeping both names as-is, freeing one name (decoupling), or restructuring first — and why that's the right order for you?* — Yes, and I can explain why / I've considered it, haven't decided / Never thought about it that way | **Scored (2/1/0)** | Ownership & Order |
| A4 | Combined monthly household income band — Above $30,000 / $20,000–$30,000 / $12,000–$20,000 / Below $12,000 | Gate | — |
| A5 | *What's the second property actually for?* — Rental income / Growing family net worth & options / A head start for the next generation / A lifestyle or second home / Not sure yet | **Scored** (specific reason = 2, "both/general sense" — offer as a middle option if needed = 1, "not sure yet" = 0) | Direction & Goal |
| A6 | *If you took on an additional monthly property commitment on top of what you have now, which is realistic?* — Comfortably within budget / Would need to adjust some spending / Would be a real stretch / Not something we can take on right now | Gate (light capacity signal, feeds route + lead grade) | — |
| A7 | *For the property you're considering — do you know who would buy it from you when you eventually sell?* — Yes, a clear profile / Vaguely, I assume someone would want it / Never thought about it that way | **Scored (2/1/0)** | Exit & Holding Strength |
| A8 | Age band — Under 30 / 30–45 / 46–55 / Over 55 | Gate | — |
| A9 | *Where are you on financing right now?* — Current In-Principle Approval (IPA), ready to move / Had one, it's expired / Never applied | **Scored (2/1/0)** | Timing & Action Readiness |

### 4.2 Door B question bank (B1–B9)

| ID | Question | Type | Dimension (Table 5) |
|---|---|---|---|
| B1 | Property value — self-report band (HDB or EC, type-aware ranges bracketing the $800K/$1.5M campaign thresholds — see §2 of the Marketing Foundation master), with "not sure, estimate for me" fallback (§12) | Gate | Current Position |
| B2 | *Do you know the CPF refund and the cash you'd walk away with if you sold?* — Yes, both numbers / I know the CPF used, not the accrued interest / No idea | **Scored (2/1/0)** | Current Position |
| B3 | *Do you know your MOP or SSD position — the date you're free to sell or restructure without penalty?* — Already free / Within 12 months / More than 12 months away / Not sure | **Scored** (already free or within 12 months = 2, known but 12+ months away = 1, not sure = 0) | Exit & Holding Strength |
| B4 | *What's pulling on the decision right now?* — Keep it as-is, no urgency / Sell and upgrade to one stronger private property / Sell and buy one (or two) properties / Not sure yet | **Scored** (specific direction = 2, general sense = 1, not sure = 0) | Direction & Goal |
| B5 | *Do you know whether keeping your HDB/EC and adding another is realistic for your names and finances, or whether you'd need to sell first — and why?* — Yes, and I can explain why / Considered it, haven't decided / Never thought about it that way | **Scored (2/1/0)** | Ownership & Order |
| B6 | Combined monthly household income band — same bands as A4 | Gate | — |
| B7 | *If you took on an additional monthly property commitment for an upgrade, which is realistic?* — same bands as A6 | Gate (light capacity signal) | — |
| B8 | Age band — same bands as A8 | Gate | — |
| B9 | *Where are you on financing or sale-readiness right now?* — Current IPA or ready to list within 3 months / In progress / Not started | **Scored (2/1/0)** | Timing & Action Readiness |

Note the deliberate 1:1 dimension parity (A2↔B2, A3↔B5, A5↔B4, A7↔B3, A9↔B9) — same five dimensions scored either path, different door-appropriate question, satisfying R-2's "meaningfully different, not cosmetic" bar while keeping one unified scoring structure per R-2's reconvergence requirement.

---

## 5. Route logic

Maps answers to the Marketing Foundation's three canonical routes (§5 of that master) plus the Prepare First outcome. **Only these route names are used** — no other naming scheme.

**Architectural note:** per the Marketing Foundation master (§5): *"a no-go or prepare/wait outcome is delivered as a variant of Route C or as a 'not yet' result, never as a fourth branded route."* Prepare First is therefore built as a distinct **result-page and CTA variant of Route C — Strengthen One First**, not a fourth brand. It is tracked as a distinct value in the `sprc_route_result` field (§11) purely for CRM reporting; the public-facing positioning and copy tone treat it as the "not yet ready to strengthen" flavor of Route C.

### 5.1 Door A → route

| Signal pattern | Route |
|---|---|
| Readiness Score ≥7 (of 10) **and** capacity comfort (A6) is "comfortable" or "adjust some spending" **and** financing (A9) is current or in progress | **Route A — Keep and Add** |
| Readiness Score 4–6 **or** capacity comfort is "a stretch" **or** ownership/order (A3) unresolved, but value/income (A1/A4) still meaningful | **Route C — Strengthen One First** |
| Readiness Score ≤3 **and** capacity comfort is "not realistic right now" **and** timeline (S4) is "just exploring" | **Prepare First** (Route C variant) |
| Direction (A5) signals the current property itself no longer fits the plan (rare for Door A, e.g. respondent's free text / follow-up conversation surfaces a full reset desire) | Escalate to advisor review — may reclassify to Route B at Strategy Session stage, not by the Readiness Check itself |

### 5.2 Door B → route

| Signal pattern | Route |
|---|---|
| Direction (B4) = "sell and upgrade" or "sell and buy" **and** value (B1) at/above the door threshold **and** MOP/SSD (B3) free or near **and** financing/sale-readiness (B9) current or in progress | **Route B — Sell and Rebuild** |
| Direction (B4) = "keep it as-is" **but** Readiness Score is high **and** capacity (B7) supports an addition **and** ownership/order (B5) is clear | **Route A — Keep and Add** (keep HDB/EC, add a private property) |
| Mixed or borderline signals — value near threshold, capacity uncertain, MOP/SSD 12+ months away | **Route C — Strengthen One First** |
| Readiness Score ≤3 **and** direction "not sure yet" **and** timeline "just exploring" | **Prepare First** (Route C variant) |

Route logic is intentionally rule-based and lightweight (a small decision table, not a weighted model) — this is a marketing-facing indicative route, not the Doctrine's post-engagement selection scoring (§6 explains the distinction further).

---

## 6. Scoring

**Explicitly distinct from `11_MINIMUM_SELECTION_DOCTRINE_v1.0.md` §8's full selection scoring** (Plan Fit / Entry Position / Demand Growth / Exit Depth / Supply & Liquidity / Holding Strength / Unit Usability, with Strong Fit/Conditional Fit/Not Recommended conclusions). That scoring is post-engagement, property-specific, and advisor-judgement-weighted. This Readiness Score is a lightweight, entry-funnel signal only.

**Readiness Score:** sum of the five scored checkpoints (§4.1/§4.2), each 0–2 points → **total range 0–10.**

**Readiness Band:**

| Score | Band | Follow-up copy lead |
|---|---|---|
| 0–3 | **Just Starting** | Names the One-Property Trap gently; leads with what's not yet mapped, not with pressure |
| 4–7 | **Building Toward It** | Leads with sequence — they know some things, haven't ordered them yet |
| 8–10 | **Ready to Move** | Leads with timing and the cost of a missed window |

This band drives the *tone* of the result-page copy; the Route (§5) drives *which* route content is shown. The two outputs are deliberately separate, mirroring the old tool's Move-result / Readiness-Band split — but lighter (5 scored checkpoints here vs. the old tool's 10), because this document's scope is the entry-funnel signal, not the full doctrine.

---

## 7. Disqualification / nurture routing

**Inherited non-negotiable rule (from the existing live spec, unchanged): NEVER SAY NO ON SCREEN.** Every respondent gets their route result and a useful next action. Disqualification happens only in backend routing and CRM tagging, never in on-screen copy.

**Lead grade — Proceed / Prepare / Nurture / No Fit (Decision 073, per R-1):**

| Grade | Conditions | On-screen experience | Backend routing |
|---|---|---|---|
| **Proceed** | Door A: owns qualifying property + income $20k+ (A4) + timeline ≤18 months (S4) + financing current/in-progress (A9). Door B: value at/above door threshold (B1) + income $20k+ (B6) + timeline ≤18 months (S4). | Full route result + strongest CTA | Same-window follow-up priority |
| **Prepare** | Meets ownership/value threshold but one or more of: income $12–20k, timeline 18m+, financing not started/expired, capacity "a stretch" | Full route result (often Route C or Prepare First) + booking-oriented CTA | Nurture sequence + booking offered, not pushed |
| **Nurture** | Below value/income threshold (Door B value under door threshold, or income below $12k), or "just exploring" with no near-term intent, or doesn't own yet (S1 = renting/with family) | Full route result + content CTA only, no call CTA | Weekly content sequence; re-scored automatically on retake |
| **No Fit** | Narrow structural mismatches only — e.g. household/property outside the service's operating scope, or already an active client on an assigned route elsewhere in the system | **Identical on-screen experience to Nurture** — same route result, same content CTA | Internal-only CRM tag; deprioritised from active follow-up so sales doesn't waste touches on a true non-fit |

**Reconciliation note:** Decision 073 licenses "No Fit" as a sales-close label, but the existing diagnostic's "never say no on screen" rule (§105 area of `Which_Move_Are_You_On_Diagnostic.md` v1.2, carried forward here) still governs the on-screen experience. No Fit is therefore an **internal-only** classification — it changes what the CRM does with the lead, never what the lead sees. This is how the two governing rules coexist without contradiction.

**Prepare First (R-5):** the only new result-page-level "not yet ready" experience this document specifies. It uses the already-locked warm-retargeting CTA **"Show Me What to Do First"** (`10_MARKETING_FOUNDATION_v1.0.md` §9) and existing Marketing Foundation copy patterns. No new nurture content, sequence, or asset is designed in this phase — that is out of scope (§13).

---

## 8. Result pages (four states)

Per `11_MINIMUM_SELECTION_DOCTRINE_v1.0.md` §2's "what each stage provides" table, the Readiness Check stage provides exactly: **indicative route; main readiness gaps; possible cost of waiting; next recommended action.** No stage may leak content reserved for Discovery or the Strategy Session (deeper situational understanding, method overview, prior cases) or for post-engagement (ranked shortlist, personalised calculations, scoring/weighting detail). Every result page follows this structure:

**Structure (all four states):** Headline → Where You Stand (indicative route + door-appropriate framing) → What's Not Yet Mapped (main readiness gaps, drawn from whichever of the five checkpoints scored 0 or 1) → What Waiting Could Cost (§9, DRAFT-flagged, respondent-specific) → Your Next Move (CTA per §10).

| State | Headline direction | Content boundary note |
|---|---|---|
| **Route A — Keep and Add** | "Your current property may be able to support a second — here's what's not yet mapped." | Names the specific gap checkpoints scored low; does not name specific projects or a shortlist |
| **Route B — Sell and Rebuild** | "The math may favour selling and rebuilding stronger — here's what to check before you list." | Surfaces MOP/SSD and walk-away-cash gaps if unscored; no specific resale valuation beyond the estimate range (§12) |
| **Route C — Strengthen One First** | "Before a second property, one property needs to get stronger first — here's why." | Frames capacity/ownership gaps as the reason, not as a rejection |
| **Prepare First** | Uses the locked "Show Me What to Do First" framing — no separate headline invention beyond what the Marketing Foundation master's copy patterns already support | No new copy system; reuses existing locked language only (R-5) |

All four states end on a CTA from the locked matrix only (§10) — never an invented offer, per Marketing Foundation §7's "one CTA, not a second offer" discipline extended here to all four states, not only the qualified ones.

---

## 9. Cost-of-waiting logic

Per-respondent, built from answers already captured — not a generic scare line. Drawn from the factors already identified in `02_SECOND_LADDER_NEW_EXECUTION.md`: fewer loan years remaining, lower future borrowing ability, income changes, rising family commitments, policy changes, equity sitting unused, suitable properties becoming pricier, losing a clean-name window, being forced into a decision by circumstance rather than choice.

**Assembly rule:** select 1–2 factors that match the respondent's actual gaps — e.g. Age band 46–55 or 55+ pairs with "fewer loan years remaining"; Ownership/Order scored 0 pairs with "losing the clean-name window"; Financing scored 0 (never applied) pairs with "suitable properties becoming pricier while you wait to start." Do not stack more than two factors — this is a nudge, not a pressure tactic.

**Prohibited claims (inherited from `10_MARKETING_FOUNDATION_v1.0.md` §11 — apply without exception):** never claim everyone can own two properties; never claim decoupling is always correct; never claim ABSD can always be avoided; never claim or imply guaranteed financing approval; never claim or imply guaranteed profit; never claim that acting immediately is always better than waiting. The honest version, already locked: *"Waiting without knowing what you are waiting for is not a strategy"* — not *"waiting is wrong."*

**DRAFT flag:** any factual claim in the cost-of-waiting copy that references specific loan-tenure rules, interest-rate assumptions, ABSD rates, or policy thresholds must carry **"DRAFT — pending platform verification"** (constitution §11) until fact-checked against current MAS/IRAS rules at implementation time. This document does not itself verify those figures.

---

## 10. CTA routing

Uses only CTAs already locked in `10_MARKETING_FOUNDATION_v1.0.md` §9 — no invented CTA anywhere in this flow.

| Moment | CTA used |
|---|---|
| Door A ad/landing entry into the Check | Check Whether You Can Own the Next Property |
| Door B ad/landing entry into the Check | Compare My Keep, Sell or Upgrade Routes |
| Generic result-page CTA (all routes, default) | Map My Best Route |
| Proceed lead grade | Book My Second Property Strategy Session |
| Prepare lead grade / Route C — Strengthen One First | Audit My Move Before I Commit, or See What Waiting Could Cost Me where the cost-of-waiting block is the stronger hook |
| Nurture lead grade / **Prepare First result (R-5, mandatory)** | Show Me What to Do First |
| No Fit (internal) | Same on-screen CTA as Nurture — Show Me What to Do First |
| Decoupling-flavoured gap (A3/B5 scored 0 or 1) | Check Whether Freeing One Name Makes Sense |

Edmund's standing CTA standard applies unchanged (Marketing Foundation §9): the CTA must match what the specific answer pattern just convinced the prospect of, not default to a generic "book a call."

---

## 11. GHL data fields

**New namespace: `sprc_*`.** Old `spl_*` fields are legacy/deprecated from cutover onward — not deleted, not written to by any new logic (see §2).

| Field | Type | Values |
|---|---|---|
| `sprc_door` | Dropdown | door_a / door_b |
| `sprc_gate_ownership` | Dropdown | own_hdb / own_ec / own_private / own_landed / own_2plus / own_0 |
| `sprc_gate_portfolio` | Dropdown | none / 2plus (internal advisor-context flag, §3.2) |
| `sprc_gate_income` | Dropdown | inc_30plus / inc_20_30 / inc_12_20 / inc_below12 |
| `sprc_gate_age` | Dropdown | age_u30 / age_30_45 / age_46_55 / age_55plus |
| `sprc_gate_timeline` | Dropdown | time_0_6 / time_6_18 / time_18plus / time_exploring |
| `sprc_gate_value_band` | Dropdown | door- and type-appropriate bands, §12 |
| `sprc_value_source` | Dropdown | self_reported / diy_estimate |
| `sprc_value_estimate_low` | Number | only populated when `diy_estimate` used |
| `sprc_value_estimate_high` | Number | only populated when `diy_estimate` used |
| `sprc_gate_capacity` | Dropdown | comfortable / adjust_spending / stretch / not_now |
| `sprc_financing_readiness` | Dropdown | ipa_current / ipa_expired / not_applied (Door A) — or ipa_current_or_listing / in_progress / not_started (Door B) |
| `sprc_ownership_awareness` | Number 0/1/2 | raw A3/B5 answer, kept for call prep |
| `sprc_readiness_score` | Number | 0–10 |
| `sprc_readiness_band` | Dropdown | just_starting / building_toward_it / ready_to_move |
| `sprc_route_result` | Dropdown | route_a_keep_add / route_b_sell_rebuild / route_c_strengthen_first / prepare_first |
| `sprc_lead_grade` | Dropdown | proceed / prepare / nurture / no_fit |
| `sprc_c1`–`sprc_c5` | Number, 5 fields | raw 0/1/2 answers for the five scored checkpoints (door-specific question ID noted alongside), kept for advisor call prep — mirrors the old tool's `spl_c1`–`spl_c10` pattern at half the field count |

**Tags (mirroring the old `diagnostic-*` / `spl_hot` etc. pattern, renamed):** `sprc_proceed`, `sprc_prepare`, `sprc_nurture`, `sprc_no_fit`, `sprc_door_a`, `sprc_door_b`.

**Legacy note:** `spl_move_result`, `spl_total_score`, `spl_band`, `spl_lead_grade`, `spl_gate_ownership`, `spl_gate_income`, `spl_gate_age`, `spl_gate_timeline`, `spl_c1`–`spl_c10` remain in GHL, untouched, as historical record of the old tool's data. No new workflow reads or writes them after cutover. Migrating or archiving that historical data is a separate future session's decision.

---

## 12. Property valuation methodology (DIY estimator, R-3)

**Confirmed research finding this design accepts as given:** no true live per-unit AVM API is available for external embedding today. SRX X-Value commercial licensing is a possible future path but requires its own vendor conversation and is out of scope for this build (§13).

**Primary input:** self-reported value band via dropdown/range picker, door- and type-aware:

| Property type | Bands |
|---|---|
| HDB (Door B) | Below $600K / $600K–$800K / $800K–$1M / $1M+ (brackets the $800K campaign threshold) |
| EC (Door B or A, per branch logic §3.2) | Below $1.2M / $1.2M–$1.5M / $1.5M–$1.8M / $1.8M+ (brackets the $1.5M campaign threshold) |
| Private/Landed (Door A) | Below $1.5M / $1.5M–$2M / $2M–$2.5M / $2.5M+ |

**Fallback: "Not sure, estimate for me."** Triggers a simple $psf-comparable estimate:

- **HDB:** query data.gov.sg's `datastore_search` API against the HDB Resale Flat Prices dataset, filtered by town, flat type, and floor-area band; compute an average or median transacted price (or $psf) over a recent rolling window.
- **EC / private:** URA private residential transaction data (via URA's API or its data.gov.sg mirror where available), filtered by project/planning area, property type, and floor-area band, same rolling-window average approach.
- **Output labelling (mandatory):** present as a range (e.g. 25th–75th percentile or ±1 SD around the mean), explicitly labelled *"This is a same-town/type/area-band estimate range, not a valuation of your specific unit."* This is a same-town/type/area-band average, not a per-unit AVM, and must not be presented as precision it doesn't have.
- **Platform Verification Rule (constitution §11):** this entire estimator output carries **"DRAFT — pending platform verification"** until the actual data pull is implemented and tested against live data.gov.sg/URA responses.
- **Known limitation to disclose internally (not necessarily to the prospect):** data.gov.sg / URA transaction data carries roughly a 45-day reporting lag — the estimate reflects recently-completed transactions, not real-time market conditions.

**Future upgrade path, explicitly out of scope now:** SRX X-Value commercial licensing, if it becomes commercially justified, would replace the DIY estimator with a true per-unit AVM. That is a separate vendor decision requiring its own in-chat ruling per the constitution's Orchestration Mandate (§12: "no new paid tools, vendors, or accounts without an explicit in-chat ruling") — not something this document authorizes or designs further.

---

## 13. Out of scope for this document

The following are explicitly not covered here and must not be inferred as approved by this master:

- **The actual code or site rebuild.** This document specifies what a later implementation phase builds; it contains no code and does not touch `01_DIAGNOSTIC_APP\` or the live diagnostic.
- **URL cutover execution** — DNS, redirect rules, GHL funnel-page routing, and ad-destination-URL updates for the new slug are implementation-phase work requiring Edmund's live-infrastructure sign-off (§2).
- **SRX X-Value licensing** — a separate future vendor conversation and in-chat ruling (§12).
- **Any new nurture asset or content sequence** — R-5 uses existing locked CTAs/copy only; building new Prepare First nurture content is not authorized here.
- **`spl_*` data migration or deletion** — a separate future data-migration decision (§2, §11).
- **The full 8-stage buyer consult journey** beyond the Self-Assessment stage this Check corresponds to (§2) — Conversation, Booking, Preparation, Implementation, and Review stage design remain deferred per U-4.
- **The Doctrine's full post-engagement selection scoring and Final Selection Pack** (`11_MINIMUM_SELECTION_DOCTRINE_v1.0.md` §§8, 11) — this document's scoring (§6) is a distinct, lighter, marketing-facing signal only.

---

## 14. Next step

Per `10_MARKETING_FOUNDATION_v1.0.md` §14, this closes Phase 1A. Phase 1B (Door A / Door B landing-page wireframes) is next, followed by Phase 1C (first creative test packs) and Phase 1D (proof system).

Approved by Coach Edmund 2026-07-16.
