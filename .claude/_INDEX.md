# .claude — Technical Control Index
Version: v1.0
Status: APPROVED TECHNICAL CONTROL
Date: 2026-07-20

## Purpose

This folder contains Claude Code workspace configuration and skills only. It is not a business knowledge branch, campaign home, asset library or client-data store.

## Active map

| Item | Purpose |
|---|---|
| `settings.local.json` | Minimal local permission configuration. Unlisted actions use the product’s normal permission flow. |
| `skills/` | Current workspace skills; each must route to current governed paths. |
| `99_ARCHIVE/` | Pre-change settings and skill snapshots. Read-only rollback. |

## Rules

1. Never store API keys, passwords, tokens, private contact data or client evidence here.
2. Archive configuration before changing it.
3. Do not auto-allow broad write, install, deletion, commit, push, process-kill or privilege-escalation commands.
4. Do not use permission rules as business governance; business authority belongs in the AI OS.
5. Review absolute paths after any machine, workspace or root-folder change.
6. Skills may point to business files but must not duplicate them.

The 2026-07-20 hardening removed legacy absolute-path grants and broad mutation allowances. The preserved rollback is `99_ARCHIVE/CLAUDE_CONFIG_PRE_CLEANUP_2026-07-20/`.
