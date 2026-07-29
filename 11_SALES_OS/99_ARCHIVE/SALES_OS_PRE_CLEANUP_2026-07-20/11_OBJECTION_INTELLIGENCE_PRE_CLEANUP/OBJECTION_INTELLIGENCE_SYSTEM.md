# OBJECTION_INTELLIGENCE_SYSTEM
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources (point, do not duplicate):
- Decision Psychology & Belief Resolution v2.1 (RB-01..RB-18, 376 objections / 166 consults): `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\03_DECISION_PSYCHOLOGY_AND_BELIEF_RESOLUTION_v2.1.md`
- Master Objection Bank v1.0 (APPROVED, E: — raw verbatim, PII): `E:\Zoom Consults - Processed\_CONSULT_INTELLIGENCE_OS\04_OBJECTION_BANK\MASTER_OBJECTION_BANK.md`
- Belief-Shift Question Sequences v2.0
- RAM Risk Assessment Module v1.0 (legacy): `X-Singapore Real Estate Insider - MAS HQ\01_MAS_OS\02_CONVERSATION_CONVERSION_SYSTEM\MAS_RAM_RISK_ASSESSMENT_MODULE_v1.0.md`

> Evidence tiers: T1 commercial · T2 CRM-verified · T3 verified conversation (the 376-objection / 166-consult table = **T3**) · T4 field-observed · T5 doctrine · T6 inference · T7 hypothesis.

---

## 1. What This System Is
The governed objection layer. It does **not** re-author the belief blocks — those live in Decision Psychology v2.1 (RB-01..RB-18) and the raw verbatim lives in the E: Objection Bank. This system defines: (a) the **objection record schema**, (b) the **operating loop**, (c) the **7 category folders** that route to RB blocks, and (d) the **real-vs-not-real** differentiation. `[T5]`

Objection handling is a **cross-cutting layer** invoked inside consult phases P3/P4 (branch 07), never a standalone stage.

## 2. Objection Record Schema (mandate §11 fields)
Every logged objection is one row against this schema. Verbatim client text is stored anonymised only (no client name/PII in 11_SALES_OS). `[HARD RULE 5]`

| Field | Definition |
|---|---|
| `objection_id` | Stable ID (OBJ-NNNN) |
| `category` | One of 7: TRUST / TIMING / FINANCIAL / SPOUSE_AND_FAMILY / PROPERTY / PROCESS / DECISION |
| `belief_block` | RB-01..RB-18 (maps to Decision Psychology v2.1) |
| `surface_statement` | What the client said (anonymised paraphrase; no attributable quote) |
| `root_cause_diagnosis` | The real thing being protected (money/identity/safety/control/trust) — the "observed real meaning" `[T3]` |
| `resistance_level` | Level 1 Info / 1.5 Confidence-as-info / 2 Confidence / 3 Identity / 4 Lifestyle-threat |
| `strong_response` | Field-tested response that resolves (must include a number/comparable/case) |
| `weak_response_to_avoid` | The losing pattern for this objection |
| `when_to_stop_pushing` | The point at which continuing damages trust (see §4) |
| `evidence_tier` | T3 if from coded consults; T5 if doctrine-only |
| `outcome_history` | What happened after (resolved / stalled / lost) — CRM-linked, T2 when available |
| `owner` | Advisor / desk |

## 3. Operating Loop
```
CAPTURE ──► CLASSIFY ──► DIAGNOSE ──► RESPOND ──► TRACK
```
1. **Capture** — log the objection (anonymised) against the schema at point of occurrence. `[T5]`
2. **Classify** — assign category + belief block (RB-xx) + resistance level.
3. **Diagnose** — name the root cause (what is being protected), not the surface. Most objections are protective. `[T5, Decision Psych §2]`
4. **Respond** — apply the field-tested strong response. **Rule: never resolve on a verbal reframe alone — attach a worked number, comparable, or case study** (the #1 winning pattern; verbal-only reframe is the #1 losing pattern). `[T3, Decision Psych Appendix A]`
5. **Track** — record outcome_history; feed recurring patterns to branch 21 (conversation intelligence) and content (objection pre-emption).

## 4. When To Stop Pushing (the restraint rule)
Resistance is often legitimate. Stop pushing and switch mode when:
- the objection is **values-driven** (RB-05 debt-aversion, RB-13 emotional attachment) — honour the value, change the sequence, don't argue past it. `[T3]`
- trust/rigor is being challenged — **defensiveness is the single worst observed pattern**; slow down, go step by step. `[T3, RB-10]`
- the real blocker is an **absent decision-maker** — resolve by bringing them in, not by re-convincing the present partner. `[T3, RB-07]`
- the correct advisory answer is **"no / not yet"** — a NO FIT or NURTURE close is a legitimate, sanctioned outcome (branch 12). `[T5]`

## 5. Objection Frequency (what to pre-empt first)
Point to Decision Psychology v2.1 §1A for the full ranked table (376 rows). Headline: **Trust (~24%) + Market timing (~22%) + Price (~19%) ≈ two-thirds of all objections.** Pre-empt RB-10, RB-01, RB-06/RB-11 in the front half of any deck/consult before the client voices them. Spouse/alignment (~4%) is under-surfaced relative to its deal-killing power — the biggest late-stage stall. `[T3]`

## 6. Real vs Not-Real Objection Differentiation (mandate §11)
A "not-real" objection is a placeholder for an unspoken real concern. Chasing the stated words wastes the session. `[T3 — recurring field pattern]`

| Signal | Likely REAL objection | Likely NOT-REAL (placeholder) |
|---|---|---|
| Specificity | Names a concrete number, scenario, or constraint | Vague ("need to think", "market too high") with no specifics |
| Consistency | Holds under a clarifying question | Dissolves or shifts when probed |
| Emotional charge | Calm, factual, verifiable | Charged, repeated, or contradicts an earlier agreement |
| Decision-maker | The person speaking owns the decision | Deflects to an absent party ("spouse won't agree") |
| Movement | Resolving it visibly advances the client | Resolving it produces a new objection immediately |

**Diagnostic move:** when an objection looks not-real, do NOT rebut it — ask the belief-surfacing question ("what specifically would you need to see to feel safe?", Belief-Shift §2) and watch whether it holds. A stated contradiction left unnamed is a top-5 loser (*e.g.* "totally agree" then "save 2 more years"). `[T3]`

Common not-real → real translations (point to RB evidence):
- "Market too high / wait for cooling" → often loss-aversion + a request for external permission (RB-01). `[T3]`
- "Need to think / more research" → often confidence gap + no forcing event, not an information gap (RB-02, Level 1.5). `[T3]`
- "I'll discuss with spouse" → often an unknown/absent spouse position + blame-avoidance (RB-07). `[T3]`

## 7. Category → Belief-Block Map (routes to the 7 folders)
| Category folder | Belief blocks (RB) | Notes |
|---|---|---|
| TRUST | RB-10 | #1 objection type (~91). Also data/methodology trust. |
| TIMING | RB-01 (+ RB-03 no-rush) | #2 (~82). Market-timing/comfort. |
| FINANCIAL | RB-05, RB-11, RB-12, RB-16, RB-17, RB-18 (+ price RB-06) | Loan/CPF/quantum/monthly/seller-price/opp-cost → **RAM 5 techniques** |
| SPOUSE_AND_FAMILY | RB-07, RB-09 | Alignment + legacy; biggest late-stage stall |
| PROPERTY | RB-06, RB-13, RB-14, RB-15 | New-launch/resale, attachment, renting, exit-risk |
| PROCESS | RB-08, RB-02 | Complexity/numeracy + need-more-certainty |
| DECISION | RB-02, RB-03, RB-04 | Paralysis, comfort, sell-high-buy-higher, commitment stalls |

Each folder's `_INDEX.md` carries the detailed routing.
