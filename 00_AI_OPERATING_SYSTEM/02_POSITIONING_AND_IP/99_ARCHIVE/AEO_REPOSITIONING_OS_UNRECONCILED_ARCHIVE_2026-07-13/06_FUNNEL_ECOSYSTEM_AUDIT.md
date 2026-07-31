# 06 — FUNNEL ECOSYSTEM AUDIT
**Owner:** Sonnet agent · **Companion file:** `Funnel_Audit_Table.csv` (60 rows, 15 criteria x 4 funnels) · **Date:** 9 July 2026

## Executive Summary

Four funnel-shaped assets exist across three states — one live-unaudited, one built-unpublished, one spec'd-unbuilt, one referenced-but-nonexistent — and none of them is currently safe to scale traffic into. **Legacy Launch V2** (`ILuFW2Qv6l9UIXk6lUIM`) is the closest to launch: its offer, CTA sequence, and disqualification framing are strong, but it has no domain, no tracking pixel, no CEA licence block, and a PDPA consent that names a different entity ("Legacy Launch") than its own footer ("Singapore Real Estate Insider") — none of which is the founders' registered name. The old **"Legacy Launch"** funnel (`4W2JREPZkCv6GQknDUOQ`) is live today and almost certainly carries the same compliance gaps, but no research pass has ever captured its actual page copy, so it cannot be scored on 11 of 15 criteria — it must be audited before any sunset decision, not after. The **"Which Step Are You On?" diagnostic** is the strategically strongest asset (it is the only one using the full locked Second Property Ladder™ vocabulary) but is entirely unbuilt, and its GHL `spl_*` custom fields do not exist — this is a hard, independent blocker that should be cleared before the diagnostic's UI is even designed. The **missing lead magnets** ("Exit-Trap Checklist," free training) referenced across 11 L1 reel scripts do not exist, leaving the widest, coldest part of the funnel with no capture asset at all — every top-of-funnel reel view today either dead-ends or, worse, is quietly funnelled straight into V2's high-commitment application form, a cold-to-hot mismatch.

**Recommended sequencing:** (1) fix V2's compliance/tracking/domain gaps and ship it first — it is the only asset close to revenue; (2) audit the old Legacy Launch funnel's live copy and traffic in parallel, then decide keep/sunset with real data, not assumption; (3) build the `spl_*` CRM fields as a standalone prerequisite, then build the diagnostic as the strategic front door; (4) build the Exit-Trap Checklist last, once the diagnostic exists downstream of it to receive the handoff.

---

## 1. Scope & Method

This audit evaluates all 15 criteria (offer clarity, audience clarity, category alignment, search visibility, AEO readiness, proof strength, CTA strength, form fields, qualification logic, CRM handoff, tracking, retargeting, follow-up sequence, compliance/disclaimer, domain placement) against four funnel-shaped assets named in the Master Context Brief and Research Appendix Report 3:

| Ref | Funnel | GHL/asset ID | State |
|---|---|---|---|
| (a) | "Legacy Launch" (old) | `4W2JREPZkCv6GQknDUOQ` | Live, DO-NOT-TOUCH per build guide, **content never audited** [VERIFY] |
| (b) | "Legacy Launch V2" | `ILuFW2Qv6l9UIXk6lUIM` | Built, fully audited in Report 3, **no domain attached** |
| (c) | "Which Step Are You On?" diagnostic | none (not built) | Spec complete (Diagnostic build doc v1.0), **no `spl_*` fields exist in GHL** |
| (d) | Missing lead magnets ("Exit-Trap Checklist," free training) | none (not built) | Referenced in 11 L1 reel scripts, **asset does not exist** |

**Method note:** Report 3 gave a full copy/field/disclaimer audit of (b). It gave zero copy audit of (a) — only its existence, funnel ID, and "do not touch" instruction are confirmed. Every (a) row in the CSV that reads "unknown/unverified" is a genuine research gap, not a placeholder — do not infer (a)'s content from (b)'s, since (a) predates the Mechanism v1.3 vocabulary entirely and may differ materially.

---

## 2. Funnel Audit Table — Score Summary

Full 60-row detail (current_state, issue, recommendation, priority, owner, status) is in `Funnel_Audit_Table.csv`. Scores are 1 (missing/critical failure) to 5 (excellent, no changes needed).

| Criterion | (a) Legacy Launch (old) | (b) Legacy Launch V2 | (c) Diagnostic | (d) Missing lead magnets |
|---|---|---|---|---|
| Offer clarity | 1 — unaudited | 4 — clear, unlinked to master ladder | 4 — strong on paper | 1 — promised, doesn't exist |
| Audience clarity | 1 — unaudited | 2 — threshold below Mechanism filter | 4 — Gates encode filter | 3 — correctly broad by design |
| Category alignment | 2 — likely pre-SPL | 2 — NLL, no bridge to SPL | 5 — full SPL vocabulary | 2 — pre-SPL scripts |
| Search visibility | 1 — domain unknown | 1 — no domain attached | 1 — not built, domain owned | 1 — doesn't exist |
| AEO readiness | 1 — unaudited | 1 — no bridge page | 4 — best-suited asset | 1 — doesn't exist |
| Proof strength | 1 — unaudited | 3 — strong stats, all [VERIFY] | 2 — proof not in result screens | 1 — doesn't exist |
| CTA strength | 1 — unaudited | 4 — clear two-step CTA | 4 — strong, spec'd | 2 — mechanism unclear |
| Form fields | 1 — unaudited | 2 — no income/capacity field | 3 — fields under-specified | 1 — doesn't exist |
| Qualification logic | 1 — unaudited | 2 — copy-only, no branching | 5 — Gates + Checkpoints | 3 — correctly none, by design |
| CRM handoff | 2 — presumed functioning | 2 — no confirmed stage automation | 1 — `spl_*` fields don't exist | 1 — doesn't exist |
| Tracking | 1 — unaudited | 1 — no pixel found | 4 — 9 events spec'd | 1 — doesn't exist |
| Retargeting | 1 — unaudited | 1 — blocked on tracking | 2 — planned, not built | 1 — doesn't exist |
| Follow-up sequence | 2 — presumed exists | 1 — none found | 1 — not built | 1 — doesn't exist |
| Compliance/disclaimer | 1 — unaudited, high-risk assumption | **1 — CEA block missing, entity mismatch, risk line present** | 2 — consent/CEA copy not drafted | 1 — doesn't exist |
| Domain placement | 1 — unknown | 2 — right target identified, not executed | 3 — right plan, not executed | 1 — doesn't exist |

The single lowest-scoring, highest-priority cell in the whole table is **(b) Compliance/disclaimer = 1**: it is the only asset that is both fully built and closest to shipping, yet it stacks three defects — missing CEA block, the flagged risk line "This is advisory, not agency," and a PDPA consent naming a different entity than the footer. Fix this before anything else ships.

---

## 3. Keep / Improve / Rebuild Decision

| Funnel | Decision | Rationale | Sequence |
|---|---|---|---|
| (a) Legacy Launch (old) | **Audit, then decide Keep-in-parallel vs Sunset** — do not decide blind | It is live and presumably still generating pipeline; sunsetting it without traffic/backlink data risks killing working revenue (Master Brief Q8: does it still receive ad traffic? — [VERIFY]). Equally, if it duplicates V2 with a worse compliance posture, it should not stay live indefinitely. | **Step 2** (parallel to V2 fix): pull live copy, ad account traffic, Search Console data. Decide within the same sprint V2 ships. |
| (b) Legacy Launch V2 | **Improve (light-touch), then ship** | Strong offer and CTA architecture already exist; the fixes needed are structural/compliance (domain, pixel, CEA block, consent entity, income-band field) not a rewrite. Matches the user's own instruction that V2 ships first. | **Step 1** — highest priority, closest to revenue. |
| (c) Diagnostic | **Rebuild from spec** (net-new build) | Nothing exists yet; this is the strategic, category-defining asset and deserves a full build, not a patch. `spl_*` CRM fields must be created before UI work starts. | **Step 3** — the strategic build, sequenced after V2 ships so the team isn't building two things live at once, but the CRM-field prerequisite (Section 5) can start immediately in parallel with Step 1. |
| (d) Missing lead magnets | **Build (new, minimal)** | Needed to give L1 reels something real to hand off to, and to stop the current cold-to-hot mismatch of routing L1 traffic into V2's application form. | **Step 4** — build last, once the diagnostic (c) exists downstream to receive the handoff; building it earlier just creates a second dead-end. |

**Sequencing logic in one line:** fix-and-ship what's closest to money (V2) -> audit the unknown live asset in parallel so no decision is made blind (old Legacy Launch) -> lay the CRM prerequisite and build the category-defining front door (diagnostic) -> close the top-of-funnel gap last so it has somewhere real to send people (lead magnet).

---

## 4. Funnel-to-Website Map

Per D2/D3 (locked domain architecture), funnels are conversion surfaces, not content surfaces. Each funnel needs exactly one indexable bridge page that is canonical to a real content hub on the authority domain (`thereimethod.com`) — this is what keeps the ecosystem inside D8's no-doorway-page doctrine.

| Funnel | Hosting domain (end-state) | Feeds FROM (authority pages) | Bridges TO (indexable page) | Funnel pages indexed? |
|---|---|---|---|---|
| (a) Legacy Launch (old) | [VERIFY current domain] | Unknown until audited | None currently — build one only if funnel is kept | [VERIFY — likely indexed by default today, a D8 violation if confirmed] |
| (b) Legacy Launch V2 | `legacylaunch.com.sg` (D3-mandated, not yet attached) | Category hub: "The Second Property Ladder™" on `thereimethod.com`; founder profile pages (Edmund Tan, Cindior Ho); "New Launch Ladder™ explained" cluster page (once written per doc 05) | One bridge page on `legacylaunch.com.sg` (e.g. `/new-launch-ladder`), canonical to the SPL category hub on `thereimethod.com`, footer linking to authority domain + founder pages | No — funnel steps (`/strategy-call`, `/schedule-call`) noindexed; only the bridge page is indexable |
| (c) Diagnostic | `secondpropertyladder.com` (D3-mandated) | Category hub + all 6 content-pillar pages on `thereimethod.com` (this diagnostic is the universal front door referenced from every pillar's CTA) | One bridge page on `secondpropertyladder.com` canonical to the SPL category hub | No — quiz steps noindexed; bridge page only |
| (d) Missing lead magnets | `thereimethod.com` (authority domain, per D2 — this is evergreen content, not a campaign) | Exit Before Entry™ / Selection Research content-pillar page | The checklist page **is** the indexable asset — no separate bridge needed since it lives on the authority domain directly | Yes — hosted directly on the authority domain as real content, per D8's "genuinely answer-complete" standard |

Note: doc `03_DOMAIN_ARCHITECTURE.md` (Opus agent's deliverable) is the canonical source for bridge-page mechanics; this section applies its D3 rules to the four funnels in scope and should be reconciled against doc 03 once it exists.

---

## 5. Funnel-to-CRM Map (GHL)

### 5.1 Form → Custom Fields → Pipeline Stage → Tags → Workflow

| Funnel | Form | Key custom fields (existing, reuse) | New fields needed | Pipeline | Stage mapping | Tags |
|---|---|---|---|---|---|---|
| (a) Legacy Launch (old) | Unknown [VERIFY] | Unknown [VERIFY] | None assumed — audit first | Presumed 1-To-1 Pipeline | Unknown | Unknown — **must confirm no cg_* Changi Green cross-tagging** |
| (b) Legacy Launch V2 | "Legacy Launch V2 — Qualify" (`cw6XigpSZy8OCZgtDC34`) | `utm_source`, `campaign_id`, `ad_id`, `click_id` (attribution); `next_budget` (repurpose as banded capacity proxy — see CSV row 8); `property_type`/`what_do_you_currently_own` (map to "current property" question) | One banded income-range field (e.g. `hh_income_band`) if no suitable existing field is found — check first whether `what_is_your_monthly_revenue` can be repurposed instead of creating new | 1-To-1 Pipeline | Form submit -> **New Lead**; calendar booking confirmed -> **Booked Call**; reminder sent/attended -> **Appointment**; call held -> **Strategy Session**; outcome -> **Close** (converts to paid Blueprint) / **Nurture** (not ready) / **Unqualified** (fails gates) / **Won** / **Lost** | `llv2-lead`, `spl-property-climber` (once diagnostic exists, for cross-funnel identification) |
| (c) Diagnostic | Net-new GHL Survey (to be built) | Reuse attribution fields above | **Full new `spl_*` field set (create before UI build):** `spl_step_result` (1-6), `spl_total_score`, `spl_band` (Standing Still / Aware but Unsequenced / Ready to Move), `spl_lead_grade` (A/B/P/C), `spl_gate_g1`, `spl_gate_g2`, `spl_gate_g3`, `spl_gate_g4`, `spl_c1` through `spl_c10` | 1-To-1 Pipeline (Grade A/B) or a new lightweight nurture track (Grade C) | Quiz complete + Grade A/B -> **New Lead** direct to booking; Grade P (Portfolio) -> **New Lead**, routed to senior-advisor calendar variant; Grade C -> **Nurture** (skip Booked Call entirely) | `spl-lead`, `spl-grade-a` / `-b` / `-p` / `-c`, `spl-step-{1-6}` |
| (d) Missing lead magnets | Net-new simple opt-in form | Reuse attribution fields | `lead-magnet-source` (checklist vs training), or simply a tag | 1-To-Many Pipeline (Signup stage) or held pre-pipeline until diagnostic taken | Download -> **Signup** (1-To-Many) or straight to a holding tag with no pipeline stage until they take the diagnostic, which then promotes them into the 1-To-1 Pipeline | `lead-magnet-exit-trap` |

### 5.2 The `spl_*` field creation list (from Signature Mechanism/Diagnostic build doc, Report 1 Section E)

Create in GHL **before** any diagnostic UI work begins — this is Section 3's independent CRM prerequisite:

1. `spl_step_result` (number, 1–6, where 6 = "Climber in Motion")
2. `spl_total_score` (number, sum of C1–C10)
3. `spl_band` (dropdown: Standing Still 0–7 / Aware but Unsequenced 8–14 / Ready to Move 15–20)
4. `spl_lead_grade` (dropdown: A / B / P / C)
5. `spl_gate_g1`, `spl_gate_g2`, `spl_gate_g3`, `spl_gate_g4` (boolean/text — silent qualification gates, never shown on-screen per naming rule)
6. `spl_c1` through `spl_c10` (number, 0/1/2 each — the 10 scored Checkpoints)

### 5.3 Changi Green contamination risk

The same GHL sub-account (`cyeYxFVQE1l73kO6S6Lx`) runs 180+ `cg_*` Changi Green tenancy-ops fields alongside all property-advisory funnels. Per D1, Changi Green is a separate business line and must never cross-link into the advisory entity's schema. **Immediate (now):** separate by tag and smart list — every advisory-funnel contact gets an `spl-*`/`llv2-*` tag family; every Changi Green contact keeps its existing `cg_*` field population; build smart lists filtered to exclude any contact carrying `cg_*` field values from advisory reporting, workflows, and any future email/WhatsApp sends. **Later (Phase 2):** split into a separate GHL sub-account once volume or a PDPA purpose-limitation review makes the shared-account risk material — do not wait for an incident to trigger this.

---

## 6. Funnel-to-Ad-Campaign Map

| Reel level | Content stance | Current CTA (per Report 3) | Feeds funnel step | Status |
|---|---|---|---|---|
| **L1 — Problem Aware** (11 scripts) | No brand/method named; polished, no Singlish | Soft CTA to "Exit-Trap Checklist" or a short free training | Should feed → (d) Missing lead magnet → then → (c) Diagnostic | **Broken today** — CTA asset does not exist; interim fix needed (Section 3, Step 4) |
| **L2 — Solution Aware** (11 scripts) | Names "New Launch Ladder™" once, late; critiques agents/courses/data platforms | Comment-keyword capture: **LADDER, EXIT, LOOP, MATH, HERD** → DM automation | Should feed → (b) Legacy Launch V2 booking (`/strategy-call`), or → (c) Diagnostic once live, depending on intent signalled by which keyword is used | Comment-to-DM automation not confirmed built; needs a single Meta-native or ManyChat-style keyword listener routing all five keywords to one link |
| **L3 — Product Aware** (11 scripts) | Attributed "Coach Edmund Tan · Singapore Real Estate Insider · New Launch Ladder™"; objection-handling format | Direct booking CTA | Feeds → (b) Legacy Launch V2 `/strategy-call` directly (highest-intent traffic, correct as-is once V2's domain/tracking/compliance fixes land) | Already correctly wired conceptually; blocked only by V2's own readiness (Section 3) |

**Recommended DM-automation routing (once built):** all five keywords (LADDER/EXIT/LOOP/MATH/HERD) trigger a DM with one link; that link should route to `legacylaunch.com.sg/strategy-call` in the near term (V2 is the only live-ready destination), and to `secondpropertyladder.com`'s diagnostic once it exists — do not build five separate destination links for five keywords; the keyword only needs to vary the DM copy/personalisation, not the destination.

---

## 7. Recommended New Funnel Structure (End-State)

```
                    ORGANIC / REELS (L1/L2/L3) + PAID ADS
                                    |
        --------------------------------------------------
        |                                                  |
        v                                                  v
  secondpropertyladder.com                        legacylaunch.com.sg
  "Which Step Are You On?" Diagnostic              Legacy Launch V2
  (universal front door — ALL traffic              (new-launch campaign line —
   without a launch-specific hook lands here)        L3 reels, new-launch-specific
                                                       IG bio link during promos)
        |                                                  |
        v                                                  v
  Lead Grade A/B/P/C -> spl_* fields                Qualify form -> next_budget +
        |                                            income-band (added)
        v                                                  |
        ----------------------->  ONE shared calendar  <----
                                  "Position Map Session"
                                  (replaces the funnel-specific
                                   "New Launch/Family Legacy Ladder"
                                   calendar name; both entry points
                                   book into the same calendar object
                                   so pipeline reporting is unified)
                                          |
                                          v
                              1-To-1 Pipeline (single source of truth)
                              New Lead -> ... -> Won/Lost
```

Both funnels terminate in the same universal CTA (**Position Map session**) on a single calendar, regardless of entry point. This is the mechanism that lets Legacy Launch V2 keep its own campaign identity (per D5, no forced rename) while still rolling every booked lead into one pipeline for reporting and follow-up — today V2 uses its own calendar ("New Launch/Family Legacy Ladder," `34KkdVJncaYiuAOjE0FP`); recommend either renaming that calendar to "Position Map Session" or making it one bookable variant inside a single calendar group so stage-mapping (Section 5.1) stays consistent across both funnels.

---

## 8. CTA Library

### Standardise (keep, use consistently across all assets)

| CTA string | Where used | Notes |
|---|---|---|
| "Start the Climb" | Diagnostic hook screen | Gamified entry point — do not shorten or reword |
| "Reveal My Step!" | Diagnostic result-reveal / contact capture | Pairs with the Checkpoint scoring mechanic |
| "Check If You Qualify" | V2 Step 1 button | Correct, matches by-application framing — keep |
| "Request My Strategy Call" | V2 Step 2 button | Keep for now (light-touch per D5); optionally test "Submit My Application" for tighter by-application framing (CSV row, priority P2, not urgent) |
| "What's Your Next Property Move?" | Ad headline / campaign line | Correct use of "Next Move" as CTA verb only, per D5 naming rule |
| "Book Your Position Map Session" | Diagnostic post-result CTA (to be written) | The universal terminal CTA across the whole ecosystem — use this exact phrase wherever the ecosystem needs one shared booking call-to-action |

### Kill / Replace

| Current string | Where found | Replace with | Reason |
|---|---|---|---|
| "This is advisory, not agency" | V2 subhead | "Advisory-first. We plan the sequence before any transaction." | D7-mandated — compliance risk while operating as licensed PropNex salespersons |
| Any use of banned words in CTA/button microcopy ("homeowner," "agent," "advice," "consultation," "project" outside the approved phrase, "unit," "good buy," "investment property," "asset progression") | Not yet found in audited CTAs, but must be actively screened for in every new CTA written for (c) and (d) | Locked vocabulary equivalents (Property Climber, Step, Position Map, etc.) | D5 banned-words list |

---

## 9. Thank-You Page Strategy

Qualification-based branching by lead grade (diagnostic) or by form answers (V2, until diagnostic-level grading exists on it):

| Grade | Thank-you experience | Calendar embed? | Proof video? | What NOT to promise |
|---|---|---|---|---|
| **A** (highest fit) | Immediate "You qualify — book your Position Map session now" | Yes, embedded directly on the page | Yes — a short founder-journey/proof clip | No guaranteed returns, no "you will definitely be approved," no unverified $ outcome, no unconfirmed session-length promise ("45 minutes" is currently [VERIFY]) |
| **B** (good fit) | "You're a strong fit — here's what happens next" + calendar | Yes | Yes | Same as above |
| **P** (Portfolio / multi-property) | Distinct message routing toward a senior-advisor or Blueprint-level conversation, not the standard call | Yes, but a different calendar variant if advisor capacity requires it | Yes, a portfolio-specific case study if one exists | Do not promise a specific portfolio strategy outcome before the actual session |
| **C** (nurture / not yet ready) | Thank-you only — no calendar; soft "we'll be in touch" + redirect into a free-content pillar page | **No** | Optional, lower-key | Do not promise a callback timeframe that ops capacity cannot support; do not silently disqualify without explanation — give a reason tied to readiness, not rejection |

General rule across all grades: never overstate advisor availability, never state a guaranteed callback window without confirming ops capacity, and never let the thank-you page make a claim that isn't already [VERIFY]-cleared in the proof library.

---

## 10. Follow-Up Sequence Strategy

Day-by-day skeleton, WhatsApp + email, PDPA/DNC-compliant (consent already captured at form submission is required before any WhatsApp/SMS send; every message must carry an opt-out; no banned words in any touch).

| Day | Grade A | Grade B | Grade P (Portfolio) | Grade C (Nurture) |
|---|---|---|---|---|
| 0 (same day) | WhatsApp: booking confirmation + proof video link | WhatsApp: booking confirmation | Email: personal note from Edmund/Cindior re: portfolio conversation | Email: thank-you + link to a free-content pillar page |
| 1 | Email: "What to bring to your Position Map session" (numbers checklist) | Email: same | WhatsApp: soft check-in | — |
| 2 | — | WhatsApp: reminder if not yet booked | — | WhatsApp (only if explicit consent given): one soft nudge toward the diagnostic if not yet taken |
| 3 | WhatsApp: reminder if no-show risk (call is within 48h) | Email: case-study proof send (Exit Before Entry category) | Email: case-study proof send (Two-Name Advantage / portfolio-relevant category) | — |
| 5 | — | — | — | Email: second content-pillar touch (The One-Property Trap) |
| 7 | Post-call: outcome-based branch (Close / Nurture / Unqualified) | Same | Same | WhatsApp: final soft touch, diagnostic invite, then stop active WhatsApp cadence |
| 14 | — | — | — | Email: third content touch; offer diagnostic again |
| 30 | Re-engagement check for any Nurture-branch outcome from Day 7 | Same | Same | Move to standard monthly newsletter/content cadence; remove from active sequence |

**Rules applied throughout:** DNC — no WhatsApp/SMS without checkbox consent captured at the originating form; PDPA — every send traceable to a specific consent record tied to the correct data-controller entity (Section 5 fix); banned words screened out of every touch (no "advice," "consultation," "homeowner," etc.); no income-guarantee or performance-guarantee language in any nurture email.

---

## Concerns

1. **(a) Legacy Launch (old) is being treated as "do not touch" while simultaneously being scoped for an eventual sunset decision.** These two instructions are in tension until the live-copy/traffic audit (Section 3, Step 2) happens — flagging so the orchestrator can confirm the audit is authorised even though the asset itself is not to be edited.
2. **V2's stated buyer threshold ($1M+, 3–6 months) is meaningfully below the Mechanism v1.3 hard filter ($2.5m+ capacity).** This audit treats it as a fixable copy/targeting gap (CSV row, Audience clarity), but if this gap is intentional — e.g. a deliberate wider net before the on-call disqualification — the recommendation to tighten it should be confirmed with the founders before execution, not assumed.
3. Per the Master Brief's own Section 6 Q8, whether the old Legacy Launch funnel still receives ad traffic is unresolved — this audit's "audit-then-decide" sequencing for funnel (a) depends entirely on that answer and should not be skipped in the 90-day plan.

---

## Questions To Clarify

1. Does the old "Legacy Launch" funnel (`4W2JREPZkCv6GQknDUOQ`) still receive live ad traffic today, and from which ad account/campaigns? (Master Brief Q8 — blocks the keep/sunset decision.)
2. What domain currently hosts the old Legacy Launch funnel, and does it have existing Search Console data or backlinks? (Master Brief Q6 — blocks any redirect/sunset execution.)
3. Is the $1M+ / 3–6-month buyer threshold on V2 a deliberate wide-net choice, or should it be tightened to match the Mechanism v1.3 $2.5m+ filter as recommended in Section 2?
4. Does an existing GHL field (e.g. `what_is_your_monthly_revenue`) already serve as a usable income-band proxy, avoiding the need to create a brand-new `hh_income_band` field?
5. What is the actual advisor call capacity (Edmund/Cindior availability) — this determines whether Grade P leads can be routed to a distinct senior-advisor calendar variant (Section 9) or must share the standard calendar.
6. CEA registration numbers and PropNex licence number for the compliance block (Master Brief Q1) — required before V2 or the diagnostic can legally go live.

## Dependencies

- Doc `03_DOMAIN_ARCHITECTURE.md` (Opus agent) must confirm the bridge-page mechanics referenced in Section 4 — this audit applies D3 provisionally and should be reconciled once doc 03 exists.
- Doc `05_AEO_TOPIC_CLUSTERS.md` (Sonnet agent) should supply the specific content-pillar/cluster pages referenced as bridge-page canonical targets in Section 4.
- Compliance review (CEA reg numbers, PropNex licence number) is a hard dependency for Section 2 row (b)/(c) Compliance fixes and for any funnel going live.
- `spl_*` CRM field creation (Section 5.2) is a hard, standalone dependency for the diagnostic build (Section 3, Step 3) — it can and should start immediately, independent of the diagnostic UI work.
- V2's pixel/tracking installation (CSV row, Tracking) is a dependency for both the Retargeting rows and for any paid traffic being sent to V2.

## First 5 Actions

1. **Fix and ship Legacy Launch V2**: attach `legacylaunch.com.sg`, install Meta Pixel + GA4, add the CEA compliance block, replace "This is advisory, not agency," and unify the PDPA consent/footer entity name — all five before any paid traffic increase.
2. **Audit the old Legacy Launch funnel's live copy, domain, and current ad traffic** in parallel with Action 1, to unblock the keep/sunset decision with real data.
3. **Create the full `spl_*` custom-field set in GHL now**, independent of the diagnostic's UI build, so the CRM prerequisite is cleared before design work starts.
4. **Add the income-band and capacity-proxy fields to V2's qualify form** (reusing `next_budget`), and build the New Lead → Booked Call → Appointment → Strategy Session workflow automation that currently does not exist.
5. **Build the Exit-Trap Checklist as a real, indexable page on `thereimethod.com`**, sequenced so its handoff routes into the diagnostic once built — closing the current top-of-funnel leak from the 11 L1 reel scripts.
