# CLAUDE.md — MARKETING OS FRONT DOOR
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `00_AI_OPERATING_SYSTEM\CLAUDE.md` (constitution). THIS FILE governs the Marketing OS layer only and is subordinate to it.
Evidence level: N/A (governance file)
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM\CLAUDE.md` v4.0; `00_COMMAND_CENTER\01_BUSINESS_POSITIONING.md`; `00_COMMAND_CENTER\02_OPERATING_RULES.md`; MARKETING_OS_BUILD_BRIEF (Fable 5, 2026-07-11)
Next review: on approval of C14/C15 (root-level OS + front-door amendment)

---

## 0. What This System Is

The Marketing OS is the **operating layer of the marketing department** for Coach Edmund Tan, Cindior Ho, and Singapore Real Estate Insider (REI): registries, frameworks, playbooks, campaign lifecycle, performance memory, and change control.

It is **not a second brain.** It holds no positioning, buyer, or proof masters of its own. Those live in the AI OS. Marketing OS files **point** to the authoritative AI OS masters by path and add only the marketing-usage layer on top.

This system is **nested under `00_AI_OPERATING_SYSTEM\` as a department** (`10_MARKETING_OS\`) (2026-07-13 spring-clean). It was originally built at root level per owner instruction (Decision 054); Edmund's 2026-07-13 spring-clean ruling moved it inside the AI OS, closing governance conflict C14. See `00_COMMAND_CENTER\DECISIONS_REQUIRED.md`.

---

## 1. Source-Of-Truth Hierarchy (higher wins)

1. `00_AI_OPERATING_SYSTEM\CLAUDE.md` — the constitution
2. `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\` — the AI OS brain (positioning, priorities, decisions)
3. `02_POSITIONING_AND_IP\` — Second Property Ladder™ spine
4. `03_CLIENT_ADVISORY_OS\` / `04_AGENT_EDITION_OS\` — edition masters
5. Other AI OS branch masters (incl. `05_CONTENT_MARKETING_ENGINE\`, `07_BRAND_AND_PROOF_BANK\`)
6. **This Marketing OS layer** — usage rules, registries, lifecycle, memory
7. Old read-only folders (historical reference)

If a Marketing OS file conflicts with any AI OS master, the AI OS wins and the Marketing OS file is corrected. Never silently merge. Full map: `00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md`.

---

## 2. Relationship To The AI OS Desks (C15)

Desks in `00_AI_OPERATING_SYSTEM\01_E.C.O.S\` are **operating roles** (who does the work). The Marketing OS is the **system layer** they operate (registries, lifecycle, memory). They are complements, not duplicates.

- Marketing & Ads Desk (`01_E.C.O.S\04_MARKETING_ADS_DESK.md`) owns this system for client-engine paid/organic work.
- Agent Recruitment Desk (`01_E.C.O.S\05_AGENT_RECRUITMENT_DESK.md`) owns the agent-engine campaigns run through it.
- Campaign **content masters** stay in `05_CONTENT_MARKETING_ENGINE\` until Edmund approves a migration. The Marketing OS references them; it does not move or copy them.

---

## 3. The Two-Engine Rule (never blend in one asset)

| Engine | Audience | Positioning | Pointer |
|---|---|---|---|
| **Engine 1 — Client Advisory** | SG property owners / climbers | The Second Property Ladder™ | `04_POSITIONING_AND_OFFERS\ENGINE_1_CLIENT_POINTER.md` |
| **Engine 2 — Agent Edition** | Other SG property agents | The Market Maker Method (LOCKED 2026-07-06) | `04_POSITIONING_AND_OFFERS\ENGINE_2_AGENT_POINTER.md` |

Every campaign, framework, playbook, creative, and experiment entry **must state which engine it serves.** No single asset speaks to both. Identity rule: REI is an advisory practice; staff are advisors/coaches, never "agents" (client-facing). PropNex = regulatory wrapper only.

---

## 4. Evidence Before Confidence

Nothing in this system asserts a result it cannot cite. Label everything with an evidence tier (full definitions: `00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md` §Evidence, mirrored from the build brief §5):

- **Tier 1** — verified commercial outcome (our revenue/clients/CAC). **Currently NONE machine-verifiable.**
- **Tier 2** — verified behavioural (our CTR/CPL/bookings). Only source: archived Codex xlsx/json aggregates (through 2026-06-24; PII-free, aggregates only).
- **Tier 3** — credible external with data.
- **Tier 4** — observed market usage (competitor libraries, "winning"-labelled assets carry NO attached data — visibility ≠ proof).
- **Tier 5** — hypothesis (all 16 Legacy Launch ads, all 10 scored reel scripts, all angle matrices — rubric-scored, zero market data).

Hard rules: no invented facts, results, testimonials, stats, or deadlines. Every figure cites its source file. Founder NAV figures ($6.6M→$9M etc.) are **UNVERIFIED — always mark `[VERIFY]`** (C10). Platform specs (Meta/Google/YouTube/GHL limits) are **"DRAFT — pending platform verification"** — never asserted from memory.

---

## 5. Operating Principles (from build brief §2)

1. Markdown only; registries are `.csv`. No `.docx`.
2. Every `.md` carries the standard header block (Version/Status/Date/Owner/Source of truth/Evidence level/Supersedes/Sources/Next review).
3. **Everything is Status: DRAFT.** Only Edmund/Cindior promote to APPROVED MASTER. Never label anything APPROVED.
4. Every folder has a `_INDEX.md` (purpose · one line per file · READS FROM · FEEDS INTO).
5. Max folder depth 4; short names.
6. Never copy media — reference the `07_BRAND_AND_PROOF_BANK\` registries in place.
7. **Never write outside `10_MARKETING_OS\`.** All other folders are read-only.
8. No PII: archived lead exports hold real names/phones/emails — aggregates only, source-cited.
9. Tight Ship style: boardroom-ready, lean, no filler. Playbooks ≤~120 lines; templates ≤~80 lines.
10. Smallest effective change; do not modify, rename, move, or delete any existing file anywhere.

---

## 6. Routing Table (which folder for what)

| Task | Folder |
|---|---|
| System status, priorities, decisions, conflicts, maturity | `00_COMMAND_CENTER\` |
| Who we are, brand, offers, audiences, voice, claims, compliance | `01_BUSINESS_AND_BRAND\` |
| Objections, awareness stages, segment usage | `02_CUSTOMER_INTELLIGENCE\` |
| Ad/funnel/trend/competitor intelligence | `03_MARKET_INTELLIGENCE\` |
| Which engine / mechanism / qualification for a campaign | `04_POSITIONING_AND_OFFERS\` |
| Find the right framework | `05_FRAMEWORK_LIBRARY\` |
| How to run a channel | `06_CHANNEL_PLAYBOOKS\` |
| Concepts, hooks, headlines, CTAs, creative registry | `07_CREATIVE_LIBRARY\` |
| Campaign records + registry | `08_CAMPAIGNS\` |
| Experiments + backlog | `09_EXPERIMENTS\` |
| Where the data lives, KPIs, baselines | `10_PERFORMANCE\` |
| Winners, learnings, failed tests | `11_WINNERS_AND_LEARNINGS\` |
| Briefs and review templates | `12_TEMPLATES\` |
| Naming, lifecycle, commands, cadence | `13_MARKETING_OPERATIONS\` |
| Change control | `14_CHANGE_LOG\` |

---

## 7. Intelligent Challenge Protocol

You are not a yes-machine. Before building any marketing asset, challenge it against the AI OS Tight Ship standard:

1. **Does it serve a current priority?** (`00_COMMAND_CENTER\CURRENT_PRIORITIES.md`) If not, say so and park it.
2. **Which engine, and is it kept pure?** Blended assets are rejected on sight.
3. **What is the evidence tier?** A Tier 5 hypothesis may not be described as a proven winner.
4. **Does any claim need `[VERIFY]` or a platform-verification flag?** Add it.
5. **Does it collide with an open contradiction (C01–C17)?** If yes, run the Conflict Detected format below — do not pick a side silently.

Challenge weak thinking, vague briefs, overbuilding, and unverified claims. Respectful, direct, decision-first. Edmund/Cindior approve; you provide the thinking, the risk, and the path.

---

## 8. Conflict Detected — Response Format

When a task touches an unresolved contradiction, stop and surface it in this shape (do not proceed on a guess):

```
CONFLICT DETECTED — [Cxx or short name]
Current position:     [what one authoritative source says + path]
Conflicting position: [what the other says + path]
Evidence:             [tier + what data exists, if any]
Consequence:          [what breaks if we guess wrong]
Recommendation:       [my pick + one-line reason]
Required decision:    [the exact call Edmund/Cindior must make]
```

Log every new conflict in `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` and, if it needs an owner call, in `DECISIONS_REQUIRED.md`. The 17 known conflicts (C01–C17) are already registered — flag the relevant one in any file that touches it. Naming conflicts C01 (Step vs Move) and C02 (session name) were RESOLVED by Decision 055 (2026-07-11): the public word is "Move" everywhere; the booked session is the Next Move Strategy Session™.
