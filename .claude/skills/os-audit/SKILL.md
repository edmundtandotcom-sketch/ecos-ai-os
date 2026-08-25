---
name: os-audit
description: Run the AI Operating System self-audit — drift, duplicates, orphans, index freshness, CANDIDATE backlog, urgent risks. Use when Edmund types /os-audit, asks "is the workspace clean", "audit the system", or on the scheduled weekly run.
---

# /os-audit — System Audit

Run the checks defined in `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\09_AUDIT_AND_MAINTENANCE.md`. Default scope is the weekly light check; run the monthly deep audit if Edmund asks or if it's the first audit of a calendar month.

## Weekly light check (≤10 minutes of work)
1. **Urgent items:** read `10_PENDING_APPROVALS.md` section A — are the urgent risks resolved? If not, surface them first.
2. **CANDIDATE backlog:** count CANDIDATE files/decisions across the AI OS (grep `Status: CANDIDATE`). If >10 or older than 14 days, flag for a decision session.
3. **Orphan scan:** files created in `00_AI_OPERATING_SYSTEM\` in the last 7 days (LastWriteTime) that are not listed in their folder's `_INDEX.md` → fix indexes.
4. **Duplicate/naming scan:** any new "(1)", "final", "latest", or unversioned files → flag with correct rename.
5. **Write-protection check:** any files modified in the read-only folders (`00_BRAIN`, `01_PROPERTY_BUSINESS`, `X-...MAS HQ`, `_MIGRATION_TO_WINDOWS`) in the last 7 days → flag (someone is working in the old system).
6. **Session log freshness:** does `08_SESSION_LOG.md` have entries for recent working sessions?

## Monthly deep audit (adds)
7. Index↔disk full reconciliation per branch; path-length check (>200 chars); folder depth check (>4 levels); cross-link resolution sweep; platform-verification staleness review per `09_AUDIT_AND_MAINTENANCE.md`.

## Output
A short audit report: PASS/FLAG per check, fixes applied automatically (index updates only — never delete or rename without listing first), and a max-5-item action list for Edmund. Log the audit as a line in `08_SESSION_LOG.md`.
