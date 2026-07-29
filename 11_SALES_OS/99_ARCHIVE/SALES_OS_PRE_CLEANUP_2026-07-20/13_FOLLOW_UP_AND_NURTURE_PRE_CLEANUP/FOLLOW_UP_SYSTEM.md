# FOLLOW_UP_SYSTEM
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources (point, do not duplicate):
- Risk Assurance & Next Action v2.0 §8 (handoff fields), §9 (follow-up by belief block), §10 (lifetime review loop)
- CRM SOP 03 (Reporting/Follow-up/Handoff Rules) v2.0; CRM SOP 04 (Nurture/Reactivation) v2.0
- Decision Psychology v2.1 (belief blocks); Case Study Bank 7 Proof Categories (D5 routing); Proof Bank
- RAM v1.0 (financial gap)

> Evidence tiers: T1 commercial · T2 CRM-verified · T3 verified conversation · T4 field-observed · T5 doctrine · T6 inference · T7 hypothesis.

## 1. Principle
Follow-up is **staying relevant to the client's next Ascent trigger**, not chasing. It is **gap-based**: every follow-up exists to close ONE named gap left open at the consult close. No gap = no follow-up (route to lifetime review loop instead). `[T5]`

## 2. The 7 Gaps → belief blocks → assets
Each open consult resolves to one primary gap. One folder per gap. `[T5; field weighting T3]`

| Gap folder | Closes | Belief block(s) | Primary asset |
|---|---|---|---|
| `CLARITY_GAP\` | Confusion / need-more-certainty / complexity | RB-02, RB-08 | Decision framework / written recap / step-by-step roadmap |
| `TRUST_GAP\` | Advisor/data/industry trust | RB-10 | Transparent method + what-to-avoid + willingness to say no |
| `FINANCIAL_GAP\` | Loan/CPF/monthly/quantum fear | RB-05, RB-12, RB-16, RB-17 | RAM safety-net framing + worked numbers |
| `SPOUSE_GAP\` | Absent/unaligned decision-maker | RB-07 | Joint session offer (bring both DMs) |
| `TIMING_GAP\` | Market-timing / no-rush (+ suitability) | RB-01, RB-03 | Market-context review (not hype) + cost-of-waiting number |
| `FEAR_GAP\` | Downside / exit / lifestyle threat | RB-01(L4), RB-15 | Downside-survivability + exit-first framing |

**Suitability** (advisory-fit / readiness) is handled as a note inside `TIMING_GAP\` (readiness plan / SAYE) — it is a timing-and-fit question, not a separate emotional gap. `[T5]`

## 3. Follow-Up Record Schema (mandate §13 fields)
| Field | Definition |
|---|---|
| `followup_id` | Stable ID |
| `gap` | One of the 7 gaps |
| `belief_block` | RB-xx driving the gap |
| `objective` | The single outcome this follow-up must produce |
| `asset` | Which asset/case-study/framework is sent (pointer) |
| `channel` | WhatsApp / email / call / joint-session (platform-verify before send) |
| `timing` | When + cadence (dated, not "later") |
| `owner` | Advisor accountable |
| `exit_condition` | What ends this follow-up (gap closed → re-book / next Ascent trigger / lost) |
| `outcome_code` | Links to branch 12 OUTCOME_CODES |

## 4. Asset Routing
- **Case study matched to the client's Step** → Case Study Bank 7 Proof Categories (the "D5 email" pattern: send the case that breaks *this* client's false belief). `[T5]` Map: Timing/Comfort → Case Type 2 (Strategy Over Comfort) / Type 6 (Missed Window); Exit → Type 1 (Exit That Unlocked) / Type 7 (Exit Before Entry); Repositioning → Type 3; 1-to-2 → Type 4; structure → Type 5 (compliance-gated).
- **Proof points** → Proof Bank (`00_AI_OPERATING_SYSTEM\07_BRAND_AND_PROOF_BANK\08_PROOF_BANK\` — categories 4/5/6 currently EMPTY; use `[PROOF NEEDED]` where absent). `[T5]`
- **Financial gap** → RAM v1.0 techniques + worked numbers.

## 5. Tone Rules (all follow-ups)
Advisory, zero pressure, one clear next step, always tied to the client's own position. No urgency/scarcity. Banned openers list: `BANNED_FOLLOW_UPS.md`. All message templates are **DRAFT — pending platform verification** (WhatsApp/email platform rules unverified per constitution §11). `[T5]`

## 6. No-Response Path
If a follow-up gets no response, escalate via the recovery ladder in `NO_RESPONSE\_INDEX.md` — never repeat "just checking in". After the ladder is exhausted → branch 14 (revival / lost).
