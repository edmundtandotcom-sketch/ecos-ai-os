# E.C.O.S — SPECIALIST DESK ROSTER
Version: v2.0
Status: APPROVED MASTER
Date: 2026-07-18
Supersedes: v1.0 (2026-07-10) — adds Sales & Conversion, renames Agent Recruitment to Agent Edition, removes manual prompt-pasting as the default, and installs Fable 5 orchestration.
Sources: AI OS CLAUDE.md v4.4; Command Center; Operating Agreement; live branches `10_MARKETING_OS` and `11_SALES_OS`.

## Purpose

E.C.O.S is one coordinated AI department with eight specialist desks. Desks are functional lenses applied to a task. They do not create separate business truths, duplicate storage or competing strategies.

## Required orchestration header

> you are the orchestrator, delegated the building to sonnet 5, opus 4.8, and never spawn another fable 5 agent. you plan, you delegate to cheaper model and you do the QA at the end. /compact

## Universal read order

For every substantial task:

1. `../CLAUDE.md`
2. `../00_COMMAND_CENTER/00_MASTER_INDEX.md`
3. `../00_COMMAND_CENTER/03_CURRENT_PRIORITIES.md`
4. `../00_COMMAND_CENTER/04_DECISION_MEMORY.md`
5. `../00_COMMAND_CENTER/11_OPERATING_AGREEMENT.md`
6. The selected desk charter
7. Only the task-relevant branch files

Do not load the entire AI OS.

## The eight desks

| # | Desk | Invoke for | Primary sources |
|---|---|---|---|
| 01 | Strategy Office | Priority, sequencing, go/no-go, positioning and system decisions | Command Center; Positioning & IP |
| 02 | Client Advisory | Property diagnosis, consultation logic and advisory methodology | Client Advisory OS |
| 03 | Content Studio | YouTube, reels, organic scripts and content systems | Content Marketing Engine; Positioning & IP |
| 04 | Marketing & Ads | Campaign strategy, paid media, funnel copy and performance | Marketing OS; active campaign; Content Engine |
| 05 | Agent Edition | Market Maker Method, recruitment, preview, workshop and coaching | Agent Edition OS |
| 06 | Research & Intelligence | Market research, buyer psychology, competitor and evidence synthesis | Knowledge Vault; current external sources |
| 07 | Operations | CRM/GHL, automation, tracking, scripts, tooling and reliability | Operations; private data boundary; local runtime |
| 08 | Sales & Conversion | Lead qualification, appointment, objection, closing, follow-up, revival and referrals | Sales OS; Client Advisory OS where relevant |

## Model routing

- **Fable 5:** orchestrates, plans, assigns work and performs final QA. It does not do the heavy build.
- **Sonnet 5:** default builder for writing, analysis, SOPs, campaign work, research assembly and operational design.
- **Opus 4.8:** high-stakes strategy, complex synthesis, architecture or difficult advisory/sales reasoning.
- Use the cheaper suitable builder. Do not spawn another Fable 5 agent.

## Single-desk rule

Select one lead desk. Add a second desk only for a genuine handoff.

Examples:
- Ad campaign: Marketing leads; Research supplies evidence; Operations implements tracking.
- Client consult: Advisory leads on diagnosis; Sales leads on conversion/follow-up.
- Workshop funnel: Agent Edition leads; Marketing supports acquisition; Sales supports conversion.
- CRM rebuild: Operations leads; Sales defines pipeline requirements.

## Source-of-truth rule

A desk produces work in the existing authoritative destination:

- live campaign work → `03_ACTIVE_CAMPAIGNS`
- approved assets → `01_ASSET_LIBRARY`
- business frameworks → relevant AI OS branch
- client/contact information → restricted drive or GHL
- code/runtime → local/private Git

## Changing a desk

A desk scope change requires:
1. Strategy Office review
2. roster and index update
3. archive of the prior charter
4. Session Log entry
5. Decision Memory entry only when the change is decision-level
