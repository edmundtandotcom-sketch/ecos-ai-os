# README — SALES OS
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: `CLAUDE.md` (this OS); SALES_OS_BUILD_SPEC_v1 (Fable, 2026-07-11); Decision 051

---

## What This Is

The ECOS Sales Intelligence, Consultation & Client Conversion OS. Built at workspace root (`11_SALES_OS\`), sibling to `10_MARKETING_OS\`, per Decision 051. Covers the full lead-to-client-to-referral lifecycle for Singapore Real Estate Insider's advisory practice. Read `CLAUDE.md` first — this file is orientation only.

## Why "Phased Core" (Decision 051.4)

The full 30-branch structure was scaffolded in one pass so the map exists and nothing gets lost or re-debated later. But not everything was written with real content on day one — that would mean guessing at systems (analytics definitions, training curricula, compliance rules) with no data or ruling behind them, which is exactly the "unvalidated document sprawl" Tight Ship Mode exists to prevent.

Instead:
- **10 branches got deep-build** because they either already have strong authoritative source material to point at and reconcile (consultation frameworks, discovery, objections, closing, follow-up, CRM), or they are net-new infrastructure this build was explicitly mandated to stand up (command center, templates, change log, conversation intelligence).
- **19 branches got a governed stub** — folder, index, and a one-page charter stating purpose, what already exists elsewhere, and what triggers real build-out. A stub is not a placeholder to feel embarrassed about; it is a deliberate "not yet, and here is exactly what unlocks it."

This mirrors how `10_MARKETING_OS` was built and keeps both sibling OS's honest about what is real versus scaffolded.

## What's Deep-Built vs Stub

| Status | Branches |
|---|---|
| **Deep-build** | `00_COMMAND_CENTER`, `07_CONSULTATION_FRAMEWORKS`, `08_DISCOVERY_AND_DIAGNOSIS`, `11_OBJECTION_INTELLIGENCE`, `12_CLOSING_AND_DECISION`, `13_FOLLOW_UP_AND_NURTURE`, `15_CRM_AND_PIPELINE`, `21_CONVERSATION_INTELLIGENCE`, `28_TEMPLATES`, `29_CHANGE_LOG` |
| **Stub** | `01_BUSINESS_AND_SALES_STRATEGY`, `02_MARKETING_TO_SALES_HANDOFF`, `03_LEAD_INTAKE_AND_QUALIFICATION`, `04_APPOINTMENT_SETTING`, `05_PRE_CONSULTATION`, `06_ADVISOR_PREPARATION`, `09_FINANCIAL_AND_PROPERTY_ANALYSIS`, `10_RECOMMENDATION_AND_PRESENTATION`, `16_CLIENT_ONBOARDING`, `17_TRANSACTION_EXPERIENCE`, `18_RETENTION_AND_PORTFOLIO_REVIEWS`, `19_REVIEWS_TESTIMONIALS_AND_CASE_STUDIES`, `20_REFERRALS_AND_ADVOCACY`, `22_SALES_ANALYTICS`, `23_SALES_ENABLEMENT`, `24_TRAINING_AND_CERTIFICATION`, `25_COMPLIANCE_AND_SUITABILITY`, `26_EXPERIMENTS`, `27_SALES_LEARNINGS` |
| **Utility** | `99_ARCHIVE` (build mandate archived here) |

Each stub's `00_CHARTER.md` names its build-out trigger — read it before assuming a branch is dead weight.

## Where To Start

- New to this OS: `CLAUDE.md` → `00_COMMAND_CENTER\SALES_OS_STATUS.md`.
- Have a decision to make: `00_COMMAND_CENTER\DECISIONS_REQUIRED.md`.
- Looking for a master doc: `00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md`.
- Something looks contradictory: check `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` before acting on it — six known conflicts (SC-01..06) are already logged.

## Governance Note

Root-level placement extends the same open item as Marketing OS Contradiction C14: the constitution (`00_AI_OPERATING_SYSTEM\CLAUDE.md` §0) says all new work happens inside `00_AI_OPERATING_SYSTEM\`; both sibling OS's were built at root on owner instruction (Decision 051 for this one). A single constitution amendment covering both root-level OS's remains pending — tracked in `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` and `DECISIONS_REQUIRED.md`.
