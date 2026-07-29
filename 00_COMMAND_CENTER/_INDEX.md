# _INDEX — 00_COMMAND_CENTER
Version: v1.2
Status: APPROVED MASTER
Date: 2026-07-18
Supersedes: v1.1 (2026-07-12) — reconciles the live folder after the Asset Library rebuild, Controlled Hybrid migration, no-freeze ruling, and completed cleanup-record archival.
Sources: AI OS CLAUDE.md v4.4; root CLAUDE.md v4.5; Decision Memory v3.15 through Decision 105; current folder inventory; completed Asset Library guides.

## Purpose

The Command Center is the governing brain of the AI Operating System. It holds the current business direction, operating rules, priorities, approved decisions, anti-drift process, parked work, lessons, session history, audit protocol, approval queue, operating agreement, and the ECOS capture inbox.

Every substantial AI session reads this folder before acting.

## Start-of-session order

1. `00_MASTER_INDEX.md`
2. `02_OPERATING_RULES.md`
3. `03_CURRENT_PRIORITIES.md`
4. `04_DECISION_MEMORY.md`
5. `11_OPERATING_AGREEMENT.md`

Load the other files only when the task requires them.

## Live files and folder

| Item | Status | What it controls |
|---|---|---|
| `00_MASTER_INDEX.md` | APPROVED MASTER | Whole workspace and AI OS map; retrieval guide |
| `01_BUSINESS_POSITIONING.md` | APPROVED MASTER | Second Property Ladder™ and Market Maker Method direction |
| `02_OPERATING_RULES.md` | APPROVED MASTER | Behaviour, versioning, file, asset, campaign and structural rules |
| `03_CURRENT_PRIORITIES.md` | APPROVED MASTER | Revenue-first priorities and current focus |
| `04_DECISION_MEMORY.md` | APPROVED MASTER | Approved decisions and supersession history; do not reopen settled calls |
| `05_EVOLUTION_PROTOCOL.md` | APPROVED MASTER | How changes are routed, versioned, logged and absorbed |
| `06_PARKING_LOT.md` | APPROVED MASTER | Valid ideas and projects that are not active now |
| `07_LESSONS_LEARNED.md` | APPROVED MASTER | Mistakes and safeguards that should shape future work |
| `08_SESSION_LOG.md` | APPEND-ONLY MASTER | What changed in each working session |
| `09_AUDIT_AND_MAINTENANCE.md` | APPROVED MASTER | Weekly and full audits; platform verification |
| `10_PENDING_APPROVALS.md` | APPROVED MASTER | Current owner-decision queue only |
| `11_OPERATING_AGREEMENT.md` | APPROVED MASTER | How Edmund and Claude work together |
| `12_ECOS_INBOX/` | LIVE INBOX | Unprocessed voice or quick-capture inputs; process to zero |
| `13_INTERACTIVE_BUILD_STANDARDS.md` | APPROVED MASTER | Locked criteria for any quiz, diagnostic or gamified funnel build — sales-instrument framing, result-reveal requirements, interactivity bar, mandatory real-screenshot QA. Load via `/build-interactive`. |
| `_INDEX.md` | APPROVED MASTER | This file |

## What does not belong here

- Active campaign scripts, drafts, working media or tracking
- Images, video, decks or bulk production files
- Raw client/contact records
- Software repositories or application runtimes
- Completed cleanup manifests, migration reports or one-time studies
- Random notes without an owner and destination

## Routing boundaries

- Active campaign work → `H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS`
- Approved assets and production sources → `H:\Shared drives\00_E.C.O.S\01_ASSET_LIBRARY`
- Client and contact data → restricted `00_E.C.O.S_CLIENTS_PRIVATE`
- Software code/runtime → local runtime and private Git; recovery packages may live in `_BACKUPS`
- Completed Command Center records → `00_AI_OPERATING_SYSTEM\99_ARCHIVE`

## Archived during the 2026-07-18 cleanup

- Legacy cleanup sign-off manifest
- Legacy cleanup execution log
- Controlled Hybrid architecture decision report
- ECOS voice-capture test

These records remain available in `99_ARCHIVE` but are not live governing files.

## READS FROM

- Workspace root `CLAUDE.md`
- AI OS `CLAUDE.md`
- Approved decisions and current physical workspace state

## FEEDS INTO

Every AI OS branch, `03_ACTIVE_CAMPAIGNS`, `01_ASSET_LIBRARY`, and the restricted private-client system.
