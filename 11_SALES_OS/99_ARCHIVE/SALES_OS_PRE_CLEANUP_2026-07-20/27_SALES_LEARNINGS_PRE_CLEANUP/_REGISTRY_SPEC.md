# _REGISTRY_SPEC — LEARNING_REGISTRY.csv
Version: v0.1
Status: STUB
Date: 2026-07-11
Supersedes: none
Sources: SALES_OS_BUILD_SPEC_v1 mandate §25/§26 (standard outputs); `10_MARKETING_OS\11_WINNERS_AND_LEARNINGS\LEARNING_REGISTRY.csv` (sibling column pattern)

---

## Purpose

Column definitions for `LEARNING_REGISTRY.csv`. One row = one durable insight, tracked through its full lifecycle so nothing is treated as settled truth before it has earned that status.

## Columns

| Column | Definition |
|---|---|
| `LearningID` | Unique ID, format `LRN-###` |
| `Insight` | The durable claim itself, stated plainly — not the raw observation |
| `Status` | One of the 12 knowledge-lifecycle states (below) |
| `EvidenceTier` | 1 (verified commercial) through 7 (hypothesis) — never leave blank |
| `Context` | What situation/pattern produced this insight |
| `Source` | Full path to the originating file, experiment, or registry row |
| `DateLogged` / `DateStatusChanged` | When captured, and when the status last moved |

## The 12-State Knowledge Lifecycle (mandate §21 — canonical)

Corrected by orchestrator QA 2026-07-11: this is the mandate's own vocabulary (archived at `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §21), replacing a builder-invented list.

1. **CAPTURED** — raw observation logged, not yet reviewed
2. **UNVERIFIED** — logged but no supporting evidence checked yet
3. **HYPOTHESIS** — framed as a testable claim
4. **TESTING** — under a controlled experiment (`26_EXPERIMENTS`)
5. **SUPPORTED** — repeated evidence supports it, not yet conclusive
6. **VALIDATED** — evidence confirmed sufficient to act on
7. **SCALED** — rolled out as standard practice across advisors
8. **CONTEXT-LIMITED** — holds only for a specific client type / stage / condition (state it)
9. **FATIGUED** — was working, effect is decaying
10. **SUPERSEDED** — replaced by a newer, better-evidenced learning
11. **DEPRECATED** — do not use for new work; kept for reference
12. **RETIRED** — closed out; historical record only

Rules from the mandate: one successful consultation never makes a universal rule; one failed consultation never makes a permanent ban. Record context with every status change.

## Rules

- A learning cannot reach VALIDATED or SCALED without EvidenceTier 1–3, or an explicit Edmund override logged in `Context`.
- CONTRADICTED learnings must cross-reference the relevant `CONTRADICTION_REGISTER.md` row.
- PII rule applies: `Context` and `Insight` describe patterns, never named clients.

READS FROM: SALES_OS_BUILD_SPEC_v1 mandate.
FEEDS INTO: `LEARNING_REGISTRY.csv`; `00_COMMAND_CENTER\CURRENT_PRIORITIES.md` (ACTIVE learnings worth protecting focus around).
