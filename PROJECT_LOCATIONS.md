# PROJECT_LOCATIONS.md — code projects, runtimes and recovery locations
Version: v1.2
Status: REGISTRY
Date: 2026-07-20
Supersedes: v1.1 (2026-07-18) — distinguishes source/runtime, self-contained static artifacts and generated-artifact staging.
Sources: Decisions 075, 076, 095 and 108; verified `_BACKUPS/ECOS_BACKUPS` recovery files; root and AI OS `CLAUDE.md`; live Drive audit 2026-07-20.

## Operating Rule

Google Drive is the shared business knowledge system and may hold immutable recovery packages and governed self-contained static artifacts. It must not be used as the live runtime for repositories, databases, `node_modules`, virtual environments, model files or services with continuous file churn.

For cross-device operation:

1. Keep source code in a private Git remote and clone it locally on each development machine.
2. Run the application on a suitable machine or server.
3. Reach that running machine through the approved secure remote-access method.
4. Store recovery bundles, source ZIPs and setup documentation in Shared Drive.
5. Store a static non-secret HTML artifact in Drive only when the owning campaign/OS index identifies its authority, purpose and source/deployment boundary.

## 1. CURRENT — Edmund OS Local (“Jarvis”)

**Runtime path:** `E:\ECOS`

This is the current private, voice-controlled local AI command centre using local components such as Ollama, faster-whisper and Piper.

- Setup and usage: `E:\ECOS\docs\`
- Machine audit: `E:\ECOS\docs\MACHINE_AUDIT.md`
- New-session development state: `E:\ECOS\CLAUDE.md`

The runtime remains local because it depends on the computer, local models, audio devices and continuously changing application files. Portability comes from source control and secure remote access—not from running the repository inside Google Drive.

## 2. SUPERSEDED — Earlier cloud/API ECOS repository

**Former local path:** `C:\Users\Admin\ecos-ai-os`

This TypeScript/cloud-API project was superseded by the current Edmund OS Local direction. It is not a current working system and must not be moved into Shared Drive as a live folder.

Authoritative recovery copies are stored in `_BACKUPS/ECOS_BACKUPS/`:

- `ecos-ai-os-20260711.bundle` — complete Git history; bundle integrity verified on 2026-07-18.
- `ecos-ai-os-source-20260711.zip` — source snapshot containing 507 entries.

The old local folder is disposable only after confirming it contains no files or commits newer than 2026-07-11. Preferred restore: clone the private Git remote. Recovery fallback: clone/fetch from the bundle, then install dependencies locally.

## 3. Artifact Classes

| Class | Correct home | Rule |
|---|---|---|
| Live repository/runtime | Local machine/server + private Git | Never run from Drive |
| Immutable recovery package | `_BACKUPS` | Dated, verified and not edited in place |
| Static campaign tool | Owning campaign `03_TOOLS_AND_APPS` | Campaign index governs; no secrets |
| Static operational tool | Owning AI OS tool-artifact folder | Registry identifies purpose and runtime/source boundary |
| Newly generated unclassified artifact | `Artifacts` | Triage within 7 days; not a permanent home |
| Superseded generated versions | Owning system’s `99_ARCHIVE` | Read-only; not deployment proof |

`Artifacts` is a staging inbox, not a project location. Generated version history does not replace private Git, deployment records or a current repository.

## 4. Shared Drive Relationship

Software projects may read business knowledge from this Shared Drive. They must not treat Google Drive as their execution filesystem. Business documents remain governed by `00_AI_OPERATING_SYSTEM`, active campaign work by `03_ACTIVE_CAMPAIGNS`, reusable assets by `01_ASSET_LIBRARY`, and technical permission settings by `.claude`.
