# CLAUDE.md — Workspace Front Door
Version: v4.6
Status: APPROVED MASTER
Date: 2026-07-20
Supersedes: v4.5 (2026-07-18) — governs the Active Campaign lifecycle, converts `Artifacts` into a controlled triage inbox, and hardens `.claude` configuration boundaries.
Sources: `START HERE — E.C.O.S`; `00_AI_OPERATING_SYSTEM/CLAUDE.md`; Decisions 095, 107 and 108; completed Asset Library guides; `PROJECT_LOCATIONS.md`; live Drive audit 2026-07-20.

---

## 1. Governing Rule

The working business operating system is:

**`00_AI_OPERATING_SYSTEM/`**

Its constitution is **`00_AI_OPERATING_SYSTEM/CLAUDE.md`**. Read that file first for any substantial session. It governs role, positioning, source-of-truth hierarchy, AI desk routing, operating discipline, file rules and session hygiene.

This root file is the workspace map. If it conflicts with the AI OS constitution, the constitution wins and this file must be corrected.

## 2. Live Workspace Map

| Location | Purpose |
|---|---|
| `00_AI_OPERATING_SYSTEM/` | **LIVE — strategy, decisions, SOPs, positioning, frameworks and business intelligence.** No bulk campaign media and no raw PII. |
| `01_ASSET_LIBRARY/` | **LIVE — governed permanent asset library.** Lifecycle: upload inbox → approved library → source archive → creative intelligence → expired/retired → migration archive. No client PII. |
| `03_ACTIVE_CAMPAIGNS/` | **LIVE — the single campaign workbench.** Lifecycle: inbox → active → scheduled → completed → archive. One campaign has one workbench and one governing index. |
| `00_E.C.O.S_CLIENTS_PRIVATE/` | **RESTRICTED — client and contact PII only.** GHL remains the live contact source of truth. |
| `_QUARANTINE/` | Temporary review pen for uncertain, duplicate, corrupt or deletion-candidate items. Nothing here is approved for use. |
| `_ARCHIVE/` | Historical read-only reference and rollback records. Not a current source of truth. |
| `_BACKUPS/` | Disaster-recovery and immutable recovery copies. Not a live working location. |
| `Artifacts/` | **CONTROLLED GENERATED-ARTIFACT INBOX.** Triage within 7 days to the owning campaign/OS, local/private Git, archive or quarantine. Never a permanent home. |
| `.claude/` | Claude Code configuration and workspace skills. Technical control folder, not a business filing location; archive configuration before changing it. |

**Write authority:** `00_AI_OPERATING_SYSTEM`, `01_ASSET_LIBRARY`, `03_ACTIVE_CAMPAIGNS`, and the restricted private client drive. Storage and technical folders are changed only for a defined cleanup, migration, backup, artifact-triage or configuration task.

## 3. Controlled Evolution — No Formal Freeze

Decision 095 supersedes Decision 093 §6. **There is no 90-day structural freeze.**

1. Change structure only to solve a real operating, retrieval, compliance, duplication or execution problem.
2. Complete one governed batch before opening the next.
3. Inventory and verify before moving, renaming, archiving or deleting.
4. Preserve rollback before structural or configuration changes.
5. Root-level or cross-system changes must be reflected in the relevant guide, index and decision record.
6. Avoid cosmetic churn, speculative folders and parallel sources of truth.
7. Revenue remains the priority; structure exists to make execution faster.

## 4. Work Routing

- Business strategy, positioning, SOPs, decisions and frameworks → `00_AI_OPERATING_SYSTEM`
- A campaign currently being produced or run → `03_ACTIVE_CAMPAIGNS/01_ACTIVE`
- Approved reusable assets and production sources → `01_ASSET_LIBRARY`
- Client names, phone numbers, case records, consent and contact data → `00_E.C.O.S_CLIENTS_PRIVATE`
- Historical material → `_ARCHIVE` or the appropriate lifecycle archive
- Suspected duplicates or uncertain files → the relevant review/quarantine folder until verified
- Generated standalone artifact awaiting classification → `Artifacts` for no more than 7 days
- Static non-secret operational artifact → owning OS tool-artifact folder
- Software source/runtime → local runtime and private Git; Drive may hold immutable recovery packages and documentation

Do not save random files loose at the Shared Drive root.

## 5. Campaign and Asset Rule

Keep one active campaign together inside one folder in `03_ACTIVE_CAMPAIGNS/01_ACTIVE`. Do not create a second workbench for recording output, scripts or tools belonging to the same campaign.

Every active campaign index must state objective, authority, folder map, current deliverables, decision owner, handoffs and definition of done. Move the campaign through lifecycle folders without changing its identity.

After completion, promote only approved reusable outputs into `01_ASSET_LIBRARY`. Raw/editable sources go to Source Archive; approved reusable assets go to Approved Library; distribution-ready finals go to Campaign Finals; testing and performance learnings go to Creative Intelligence.

## 6. One File, One Home

One permanent file has one permanent home. Indexes and registries point to it; they do not create working duplicates.

- Active production home → Active Campaigns
- Approved reusable media home → Asset Library
- Strategy/doctrine home → AI OS
- PII/evidence home → private client drive
- Source/runtime home → local/private Git
- Superseded material → the archive inside its owning system

## 7. Code, Static Artifacts and Portability

Google Drive is **not** a live runtime for software repositories, databases, `node_modules`, virtual environments or local AI services.

- Current local AI runtime: `E:\ECOS`
- Portable source access: private Git, cloned locally on each machine
- Shared Drive: immutable recovery files, documentation and self-contained static artifacts only
- A static HTML artifact may live with its owning campaign or OS only when it contains no secrets, has a governing index and is not represented as the source repository or deployed runtime.
- Generated version folders are not deployment proof. Verify the current repository/deployment before changing or running a tool.

The superseded `C:\Users\Admin\ecos-ai-os` repository is not a source of truth. Valid recovery copies exist in `_BACKUPS/ECOS_BACKUPS`. Do not move the live folder into Shared Drive.

See `PROJECT_LOCATIONS.md` for the exact project map and restoration instructions.

## 8. Technical Configuration Rule

`.claude` contains technical configuration only.

1. Never store credentials, tokens or client data in settings or skills.
2. Auto-allow rules must be minimal and task-scoped; broad write, install, commit, deletion or process-kill patterns are prohibited.
3. Archive the current config before replacement.
4. Business instructions belong in the AI OS, not in settings permission lists.
5. Skills must route to current folder names and respect privacy, campaign and asset boundaries.

## 9. Quick Start

1. Read `00_AI_OPERATING_SYSTEM/CLAUDE.md`.
2. Read `00_COMMAND_CENTER/00_MASTER_INDEX.md`, `03_CURRENT_PRIORITIES.md` and `04_DECISION_MEMORY.md`.
3. Route the task to the correct desk in `00_AI_OPERATING_SYSTEM/01_E.C.O.S`.
4. Work only inside the agreed folder or system area.
5. Before closing, save decisions, update affected indexes and record the session where required.

## 10. Workspace Commands

| Command | Purpose |
|---|---|
| `/desk <task>` | Route and execute a business task through the correct AI desk. |
| `/new-idea <idea>` | Capture a new direction without losing it or reopening old debates. |
| `/session-close` | Save decisions, update indexes and close the session cleanly. |
| `/os-audit` | Run the operating-system audit. |

Skills-to-desk map: `00_AI_OPERATING_SYSTEM/01_E.C.O.S/08_CLAUDE_SKILLS_MAP.md`.
