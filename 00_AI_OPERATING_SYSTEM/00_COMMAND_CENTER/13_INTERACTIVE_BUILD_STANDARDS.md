# Interactive & Gamified Platform Build Standards

Version: v1.1
Status: APPROVED MASTER
Date: 2026-07-19
Supersedes: v1.0 (2026-07-17) — adds §§5–11, all extracted from direct inspection of two prior real builds Edmund named as reference quality.
Sources: Second Property Ladder Phase 1A/1B build session (2026-07-16/17); direct source-code inspection of `property_next_move_decision_mirror_v7_hybrid_cta.html` (primary reference — a property decision tool for this same business) and `agent_business_growth_profiler_v3.html` (secondary reference — read for comparison, its patterns noted where genuinely present and NOT overclaimed where absent).

---

## 1. Why this file exists

Any quiz, diagnostic, calculator, or gamified tool built for lead generation went through repeated rebuild cycles because the bar wasn't set before building started. Edmund's own words, verbatim from the session that forced this file into existence:

> "The entire quiz is to be done like a sales page, bringing them through the end to take action... I need a sub session to set criteria for any quiz and platform we build that has gamification instead of me repeating again and again."

And, one round later, after reviewing a rebuild that still fell short:

> "It must be able to bring them from pain to pleasure in the quiz... every step is supposed to hit them emotionally... the cost of inaction is crucial... the output results must be relatable to them and not just another template respond."

This is that standard. Read it — or have it loaded via the `/build-interactive` skill — **before** starting any quiz, diagnostic, or gamified funnel build, not after the first draft disappoints.

---

## 2. The core reframe: it is a sales instrument, not a diagnostic

The single biggest failure mode observed: building a tool that *informs* when it needs to *sell*. A neutral, well-organized, factually-accurate diagnostic that doesn't create desire to act is a failed build, even if every number is correct and nothing overlaps on screen.

Every screen in the flow must do one of two jobs:
- **Build commitment** — each question should feel like it's worth finishing what was started (sunk-cost momentum), and should teach the category vocabulary/mechanism as the respondent answers, not just extract data.
- **Build desire for the outcome** — the respondent should want to see what's on the other side, and once they do, want the next step (the booked session) more than they wanted the result itself.

If a screen does neither, cut it or rewrite it.

---

## 3. The result reveal is the highest-leverage moment — treat it like one

Two specific, non-negotiable requirements, both drawn directly from what was missing in the first three build rounds:

1. **A "thinking" beat before the reveal.** The result must not appear instantly on the last click. Insert a brief (1.5–3 second), animated "processing/calculating your position" moment between the last answer and the result screen. This is not decoration — it is what makes the result feel *earned and personalized* rather than a pre-written template that was always going to show up regardless of the answers. Skip or shorten it only if `prefers-reduced-motion` is set.
2. **The result must close, not just report.** State where they stand, then immediately make the next action feel like the obvious continuation of what they just received — not a bolted-on ask. Show proof of real work having just happened (a redacted/personalized-feeling document, specific gaps named from *their* actual answers, not generic copy) so the CTA reads as "give me the rest of this," not "sign up for something new."

See §5–§7 below for the concrete, reference-validated techniques that make both of these actually work rather than staying abstract.

---

## 4. Interactivity bar — what "good" looks like, concretely

Before building, benchmark against at least one real comparable — a competitor's live tool, or a prior build from this business — rather than guessing the bar from first principles. Screenshot it, click through it yourself, note specifically what makes it feel alive.

Minimum bar, validated against real comparables in this project:

- **Animated progress, tied to the product's own mechanism/metaphor** — not a static "Question 3 of 12" label. A moving element (icon, avatar, fill) that visibly advances as the respondent progresses, ideally interpolating smoothly within a stage, not just jumping between fixed markers.
- **Smooth transitions** between questions (forward and back), not hard cuts.
- **Tactile selection micro-interactions** — hover and selected states should feel responsive (subtle lift/scale/glow), not a flat instant color swap.
- **Constrained-choice UX with live feedback** — for any "select up to N" question, disable the remaining options the moment the cap is hit (`property_next_move_decision_mirror` does this on every multi-select). Don't just validate on submit; make the limit felt as an interaction. This also does real diagnostic work — forcing a pick between competing concerns surfaces which one is primary.
- **Optional sound design** is a legitimate delight lever for this brand family — implement as generated tones (Web Audio API oscillators), never external audio files. Default to **muted** for a professional B2C-advisory audience; one-tap unmute.
- All motion must respect `prefers-reduced-motion` (jump directly instead of animating).

---

## 5. The pre-question hook: mirror their private thought, don't survey them

The single highest-leverage technique found in the reference build. Instead of a neutral multiple-choice question, phrase the key emotional question as a set of **pre-written, first-person inner-monologue statements** the respondent selects from — not "what is your main concern?" but options like *"My property has made money, but I don't know what that gain should unlock next"* and *"I am afraid to sell because I may not be able to buy back something better."*

Selecting one doesn't feel like answering a survey — it feels like being read. This is the mechanism that actually delivers "hit them emotionally," not a general instruction to write punchier copy.

Two requirements to make it work:
1. The statements must be genuinely specific and varied — generic options ("I'm not sure what to do") don't create the recognition effect. Write 5–6 real, distinct inner-monologue lines per question, grounded in real objections/fears already documented in the business's Doctrine/Foundation masters — never invented psychology unconnected to what's actually approved.
2. **The result must explicitly translate the selection back to them** — a dedicated panel structured as: *what you selected → what it usually means → what should be reviewed because of it*. This is the "relatable, not template" requirement made concrete: the respondent's own words open the panel, not a generic label.

Pair this with a **"why this matters" callout on every question screen** — one or two sentences tying the specific question to a real stake ("Property decisions are affected by age, loan runway, family timing, and how long you can comfortably delay"). This makes data collection double as teaching, which is exactly the commitment-building job defined in §2.

---

## 6. The processing phase must be personalized, not just animated

§3's "thinking beat" requirement gets upgraded here with the concrete mechanism that makes it land:

- **Insert the respondent's own name and specific answers into the processing captions**, not a generic "Analyzing your results..." line. The reference pattern: 4 sequenced status lines, each naming what's specifically being computed ("Translating your private thought...", "Checking your 12–36 month decision window...", "Building your illustrative delay examples...", "Preparing your consult agenda..."), synced to a real progress percentage and to visual "moving cards" that highlight which step is currently active.
- If a talking-head/avatar video placeholder is part of the concept, the caption underneath it should also be personalized and reference their actual selections, not be static filler.
- This is what makes the result feel like something that just happened *for them specifically* rather than a template that was always going to render regardless of their answers — which is the exact complaint that made this standard necessary.

---

## 7. The result page must be a visual dashboard, not a wall of text

"Better illustration for data — charts, graphs, instead of just words" is a locked requirement, not a preference. Concretely, every result page needs:

- **A real metrics/stat-card row** at the top with actual computed numbers from the respondent's own inputs (not generic ranges) — e.g. a paper-gain figure, a usable-gain estimate, a decision-window label, a named main risk.
- **A scored "gap map"** — multiple dimensions (5–7 is a good range) each shown with a score and a color-coded risk pill (low/mid/high), not a paragraph describing the same thing. Makes weakness visible at a glance.
- **A real cost-of-inaction visualization** — at minimum a bar/track chart showing a value changing across a timeline (e.g. today / 12 / 24 / 36 months). A hand-coded SVG line chart (two lines, e.g. a rising cost line and a shrinking capacity/runway line, with the gap between them shaded) is achievable in a single self-contained file with no charting library and is significantly more persuasive than a paragraph stating the same fact — build one when the underlying data supports two comparable trending values.
- **A staged timeline/journey**, not just a single verdict — "where you are now" → what changes at defined future checkpoints → the route forward. This is the concrete form of "walk them through where they are now, where they could potentially go."

No result page ships as primarily paragraphs of body text. If a section can be a stat, a scored pill, or a chart instead of a sentence, make it one.

---

## 8. Every result must move the respondent from pain to pleasure — in this order

A result page that ends on pain (naming what's wrong) without a lift, or jumps straight to pleasure (the pitch) without earning it, both fail. The validated structure, in sequence:

1. **Pain, named precisely** — the private-thought mirror (§5) reflecting their own words back with more clarity than they had it themselves.
2. **Pain, quantified** — the gap map and cost-of-inaction visualization (§7) turning the vague worry into a specific, visible cost.
3. **Direction, offered** — the staged journey/timeline showing that a path forward exists and roughly what it looks like (§7, §9).
4. **Pleasure, made concrete** — the close: a specific next step, framed as the natural continuation of what they just received, with a low-friction preparation checklist (§10) so booking feels administrative, not like a cold ask.

Never end a result mid-pain. Never open on the pitch before the pain has been named and quantified — it reads as generic and gets tuned out.

---

## 9. Give the why and the what — never the how

The result explains what's wrong and why it matters, and states a recommended direction — but must never teach the respondent to actually execute, calculate, or solve it themselves. The "how" is the paid service; giving it away in the free tool removes the reason to book.

Concretely: naming that a specific dimension (e.g. future-buyer clarity, cash-buffer safety) is weak, and explaining in one sentence why that matters, is in scope. Providing the actual calculation method, a negotiation script, or a step-by-step execution sequence they could run without the business is not — that content stays reserved for the paid engagement, consistent with whatever "what each stage provides" boundary already exists in the relevant Doctrine master for this business line.

---

## 10. Long result pages need a hybrid CTA, not a single ask at the bottom

If a result page has more than ~4–5 sections (which most good ones will, per §7), a single CTA at the very bottom gets lost. The validated pattern — literally named by its own iteration history (`v7_hybrid_cta`, seven rounds to arrive here) — is **both at once**:
- An **early or embedded CTA panel** partway through the result content (essential on mobile, where sticky elements don't work well or eat too much screen).
- A **persistent sticky sidebar/bar CTA** on desktop that stays visible as the page scrolls, so a ready respondent never has to hunt for the next step.

Immediately before the final CTA, include a short **"what to bring / what we'll cover"** checklist — it reframes booking as a natural administrative next step rather than a sales ask, and increases show-up commitment for the eventual appointment.

---

## 11. Two build-architecture questions to resolve explicitly, not by default

These are genuine judgment calls with real tradeoffs — present them to Edmund as a decision, don't silently pick one:

1. **Opt-in placement.** Contact capture can sit *before* the quiz (higher friction, but the lead is captured even if they abandon mid-quiz — the reference tool's pattern: a value-preview hero, then a gated opt-in with PDPA + estimate-disclaimer consent, then the quiz) or *after/never* (lower friction, better completion rate, but an abandoning respondent leaves no trace). Which is right depends on traffic source and offer strength — ask, don't assume.
2. **Consent structure**, if capturing contact info at all: use **two separate, explicit checkboxes** — one for contact/marketing consent, one for an "these are educational estimates, not advice" disclaimer — never combine them into one. This is a real compliance pattern already used correctly in a prior build for this business; keep it.

---

## 12. Compliance still governs — sharper is not the same as hype

Getting more persuasive does not license violating whatever prohibited-claims list governs the underlying product (see the relevant Marketing Foundation / Doctrine masters for the specific business line). The lever for sharper copy is **specificity grounded in real, already-approved proof** — concrete case details, named mechanisms, real stakes — never an invented statistic, a guarantee, or an absolute claim the business can't back up. If sharper copy is tempting a claim that isn't already locked/approved somewhere, flag it as a question, don't ship it.

---

## 13. Visual and brand consistency

- Reuse the established design-token system (color variables, type pairing) across every tool in the same product family — a quiz, its landing pages, and any related tool should read as one product, not visually related cousins.
- Segment/audience-specific accent differentiation (e.g. a different accent hue per audience door) is good practice when the product already has that architecture — keep it consistent across every surface.

---

## 14. Mandatory QA discipline — the single most validated lesson from this project

**Never trust DOM/console checks or a subagent's self-reported "I tested it" as sufficient for anything visual or interactive.** Across this project's build rounds, real, visible bugs (overlapping text, a progress-bar label overflowing its container, a sticky bar covering page content) were missed by DOM geometry checks and by build agents that claimed to have tested live — and were only caught when the orchestrator personally drove the artifact in a real, properly-foregrounded browser and looked at actual screenshots.

Before presenting or publishing any visual/interactive artifact:

1. Serve it and open it in a real, foregrounded browser session (not a backgrounded/hidden tab — screenshot compositors can silently corrupt in that state and produce false readings in both directions).
2. Take real screenshots at every major state — not just the happy path: click through edge cases (a perfect score, a worst score, each branch, each result state) via whatever QA/preview shortcut the build includes.
3. Cross-check anything visually ambiguous with `getBoundingClientRect()` geometry — use geometry to *investigate* what a screenshot shows, not as a replacement for looking.
4. Run a compliance scan (prohibited claims, invented CTAs, banned language) as text, not just a visual pass.
5. If a subagent reports it couldn't get screenshots working and relied on geometry only, treat that as a flag to re-verify personally before trusting the result — not as sufficient QA on its own.

---

## 15. Before starting the next build, resolve

1. Who is this screen for, and what does it need to feel to move them forward — not just what does it need to say.
2. What does the *result* prove, and how is that proof made visible (§7) in under 3 seconds of looking at it.
3. What's the one real comparable to benchmark interactivity against.
4. What's already locked (compliance, positioning, CTAs) that sharper copy must work inside of, not around (§12).
5. Opt-in placement and consent structure (§11) — resolved explicitly, not defaulted.
6. Where the pain-to-pleasure arc (§8) turns — mapped before writing a single line of result copy.

---

## READS FROM
Second Property Ladder Phase 1A/1B session lessons (2026-07-16/17); direct inspection of `property_next_move_decision_mirror_v7_hybrid_cta.html` and `agent_business_growth_profiler_v3.html`; relevant Marketing Foundation and Doctrine masters for compliance boundaries on any specific build.

## FEEDS INTO
Any future quiz, diagnostic, calculator, or gamified funnel build across the AI OS. Invoked via the `/build-interactive` skill.
