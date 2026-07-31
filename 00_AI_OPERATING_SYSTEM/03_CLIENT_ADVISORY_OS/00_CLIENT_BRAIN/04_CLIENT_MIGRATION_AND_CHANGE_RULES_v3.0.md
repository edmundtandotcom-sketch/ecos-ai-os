# 04_CLIENT_MIGRATION_AND_CHANGE_RULES
Version: v3.0
Status: APPROVED MASTER
Date: 2026-07-19
Supersedes: `04_CLIENT_MIGRATION_RULES_v2.0.md` — replaces retired folder destinations and dual-format rules with the current AI OS controlled-evolution protocol.
Sources: Operating Rules; Evolution Protocol; Project Locations v1.1; branch audit 2026-07-19.

## Core rule

Migration is system protection, not bulk file moving.

## Workflow

1. Inventory the physical folder.
2. Identify each file’s current job.
3. Check the governing decision and current source.
4. Classify: keep, update, move, archive, park or delete-candidate.
5. Preserve rollback for material changes.
6. Make the smallest effective change.
7. Verify source and destination.
8. Update indexes and Session Log.

## Current destinations

| Job | Destination |
|---|---|
| Advisory operating rules and methods | Client Advisory OS |
| Lead conversion, objections, follow-up and referrals | Sales OS |
| GHL/automation/tracking | Operations |
| Reusable research and evidence | Knowledge Vault |
| Active campaigns and production | Active Campaigns |
| Approved reusable assets | Asset Library |
| Client-identifiable records | GHL / restricted private drive |
| Code/runtime | Local repository / private Git |
| Superseded branch material | Branch `99_ARCHIVE` |

## Format rule

Markdown is the authored source of truth. Do not create `.docx` twins unless a separate human-delivery requirement explicitly calls for an export.

## Archive rule

Archive before deletion. Destructive deletion requires explicit owner approval.

## No-bloat rule

Do not create a folder for:
- one temporary note;
- one campaign;
- an idea without an owner;
- a second copy of an existing source;
- a workstream that has not passed priority review.

## Final rule

A change is complete only when the live files, physical structure, indexes and decision/session records agree.
