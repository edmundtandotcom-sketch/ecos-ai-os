# CLAUDE.md — Workspace Front Door
Version: v4.4
Status: APPROVED MASTER
Date: 2026-07-16
Supersedes: v4.3 (2026-07-13) — Controlled Hybrid architecture complete (Decision 093): PII extracted to private drive, campaigns consolidated to 03_ACTIVE_CAMPAIGNS, media evicted from brain, 90-day freeze in effect (to ~2026-10-16). Prior: v4.2 (2026-07-13) — Marketing/Sales OS nested; root decluttered from 24 → 6 live folders.

---

## The One Rule

The working system for this entire workspace is:

**`00_AI_OPERATING_SYSTEM\`**

Its constitution is **`00_AI_OPERATING_SYSTEM\CLAUDE.md`** — read that file first, every session, and follow it. It defines role, Tight Ship Mode, positioning (The Second Property Ladder™ / Market Maker Method), the AI TEAM desk routing, source-of-truth hierarchy, output formats, file and version rules, and session hygiene.

## Folder Map (post migration, 2026-07-16 — LIVE)

| Folder | What it is |
|---|---|
| `00_AI_OPERATING_SYSTEM\` | **LIVE — the working system + constitution.** Brain (no bulk media, no raw PII). Contains 10_MARKETING_OS, 11_SALES_OS, and 8 other departments (LOCKED — 90-day freeze to ~2026-10-16). |
| `01_ASSET_LIBRARY\` | **LIVE — all evergreen media** (9 categories: Photos, Testimonials/Proof, Brand, Video Ads, Sales Decks, Campaign Outputs, Ad Swipes, Frameworks, Client Data). Synced to team. |
| `03_ACTIVE_CAMPAIGNS\` | **LIVE — the ONE campaign workbench.** Lifecycle: INBOX → ACTIVE → SCHEDULED → COMPLETED → ARCHIVE. Single source of truth for all campaign work. |
| `_QUARANTINE\` | Review pen for items needing final disposition before archive/delete (replaces the deleted `_DEL`). Logged deletions per Operating Agreement Rule 39. |
| `_ARCHIVE\` | Read-only reference (00_BRAIN, 01_PROPERTY_BUSINESS, old campaign homes, etc.). Not a source of truth. |
| `_BACKUPS\` | Disaster-recovery copies (410 GB Zoom backup, ECOS backups). See `_BACKUPS\README.md`. |
| `Artifacts\` | Standalone Claude-built mini-tools (kept). |
| **Private Shared Drive:** `00_E.C.O.S_CLIENTS_PRIVATE\02_CLIENTS_AND_CONTACTS_PRIVATE\` | **RESTRICTED membership.** All PII: contact master, consent records, cleanup pipelines, access rules. GHL is the live source of truth. |

**Write authority:** `00_AI_OPERATING_SYSTEM\`, `01_ASSET_LIBRARY\`, `03_ACTIVE_CAMPAIGNS\`, private drive (restricted). Everything else is read-only reference.

**90-day freeze rule (to ~2026-10-16):** No new top-level folders, no renames, no restructuring without a logged evidence-based change request. Foundation LOCKED. Next 90 days: REVENUE.

## Quick Start (any session)

1. Read `00_AI_OPERATING_SYSTEM\CLAUDE.md` (constitution).
2. Read `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\00_MASTER_INDEX.md` + `03_CURRENT_PRIORITIES.md` + `04_DECISION_MEMORY.md`.
3. Route the task to the right desk in `00_AI_OPERATING_SYSTEM\01_E.C.O.S\`.
4. Pending items needing Edmund's decision live in `00_COMMAND_CENTER\10_PENDING_APPROVALS.md`.
5. Before ending a working session, run the checklist in `00_COMMAND_CENTER\05_EVOLUTION_PROTOCOL.md`.

## Commands (workspace skills in `.claude\skills\`)

| Command | Purpose |
|---|---|
| `/desk <task>` | Route any business task to the right AI TEAM desk and execute as it |
| `/new-idea <idea>` | Capture a new idea/direction into the brain so it is never lost or re-debated |
| `/session-close` | End-of-session checklist: save decisions, fix indexes, log the session |
| `/os-audit` | System self-audit (also runs automatically every Monday 8:05am) |

Skills-to-desk map: `00_AI_OPERATING_SYSTEM\01_E.C.O.S\08_CLAUDE_SKILLS_MAP.md`.

If this file and the AI OS constitution ever conflict, the constitution wins — fix this file.
