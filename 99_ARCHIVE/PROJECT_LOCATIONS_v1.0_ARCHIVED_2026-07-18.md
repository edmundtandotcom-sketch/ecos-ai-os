# PROJECT_LOCATIONS.md — where the local (non-Drive) projects live
Version: v1.0
Status: REGISTRY (pointer)
Date: 2026-07-13
Supersedes: `ECOS_REPO_LOCATION.md` + `EDMUND_OS_REPO_LOCATION.md` (merged into this one file, 2026-07-13 spring-clean)
Sources: Decisions 075 / 076 (`00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\04_DECISION_MEMORY.md`)

Some code projects can't live on this Google Drive (Drive corrupts databases, chokes on node_modules/venv churn, and can't run local apps). They live on the PC's local disks instead. This file is the single signpost to them.

> ⚠️ **Two different projects share the short name "ECOS" — don't confuse them.** The current one is `E:\ECOS`; the old one is `C:\Users\Admin\ecos-ai-os`.

## 1. CURRENT — Edmund OS Local ("Jarvis") → `E:\ECOS`
Private, voice-controlled local AI command centre (Ollama + faster-whisper + Piper, free/local runtime). This is the **active** command-centre direction (Decision 075; path corrected to `E:\ECOS` by Decision 076).
- Setup / usage: `E:\ECOS\docs\` (INSTALLATION.md, USER_GUIDE.md)
- Machine audit: `E:\ECOS\docs\MACHINE_AUDIT.md`
- Dev state for a new session: `E:\ECOS\CLAUDE.md`

## 2. OLD (superseded, kept as reference) — ECOS → `C:\Users\Admin\ecos-ai-os`
The earlier "Edmund & Cindior Operating System" — cloud-API, TypeScript. **Superseded as direction** by Edmund OS Local (Decision 075), but the folder is kept, not deleted. Backups of it are in `_BACKUPS\ECOS_BACKUPS\`.
- Why local: Google Drive can't handle its pnpm symlinks / node_modules churn (ADR-0001).
- Resume (if ever needed): open a session in `C:\Users\Admin\ecos-ai-os`, read `BUILD_STATE.md` then `docs/SESSION_RESUME.md`.

Both treat this Google Drive workspace (`00_AI_OPERATING_SYSTEM`, etc.) as a **read-only knowledge source** only.
