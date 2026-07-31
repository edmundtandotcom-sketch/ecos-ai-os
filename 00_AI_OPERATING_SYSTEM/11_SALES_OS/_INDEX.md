# 11_SALES_OS — _INDEX
Version: v2.0
Status: APPROVED MASTER — LIVE VERIFIED 2026-07-20
Date: 2026-07-20
Supersedes: the July 2026 thirty-branch phased scaffold.
Sources: AI OS CLAUDE.md v4.5; Decisions 071 and 107; live Drive audit 2026-07-20.

## Purpose

Sales OS owns the movement from lead through qualification, booking/show-up, closing, follow-up, nurture, revival, referral and pipeline outcome.

Client Advisory owns diagnosis, discovery, Strategy Session, RAM, ProDeck, Blueprint and recommendation delivery. Operations owns GHL implementation. Named conversation evidence remains private.

## Required orchestration header

> you are the orchestrator, delegated the building to sonnet 5, opus 4.8, and never spawn another fable 5 agent. you plan, you delegate to cheaper model and you do the QA at the end. /compact

## Active map

| Branch | Purpose |
|---|---|
| `00_GOVERNANCE/` | Authority, outcomes and handoffs |
| `01_QUALIFICATION_AND_BOOKING/` | Lead grading, appointment and show-up system, Marketing handoff |
| `02_OBJECTIONS_AND_CLOSING/` | Objection routing, close and outcome codes |
| `03_FOLLOW_UP_NURTURE_AND_REVIVAL/` | Follow-up, no-show/lost revival, retention and referrals |
| `04_PIPELINE_MOVEMENT/` | Sales-owned stage semantics and Operations implementation handoff |
| `05_TEMPLATES/` | Lean reusable sales planning templates |
| `99_ARCHIVE/` | Pre-cleanup scaffold and superseded material; read only |

## Privacy correction

The former `21_CONVERSATION_INTELLIGENCE` folder was moved intact to the private cited-evidence boundary as `SALES_CONVERSATION_INTELLIGENCE_PRIVATE_2026-07-11`. Sales OS may use de-identified approved patterns from the Knowledge Vault; it must not store per-consult evidence.

## Routing

- Diagnosis/advice → Client Advisory
- Acquisition/funnel strategy → Marketing OS
- Live campaign work → Active Campaigns
- GHL fields/workflows/dashboards → Operations
- Named records and transcript evidence → private client system
- Approved media → Asset Library

No root `CLAUDE.md` or `README.md` is used here; the branch has one front door: this index beneath the AI OS constitution.
