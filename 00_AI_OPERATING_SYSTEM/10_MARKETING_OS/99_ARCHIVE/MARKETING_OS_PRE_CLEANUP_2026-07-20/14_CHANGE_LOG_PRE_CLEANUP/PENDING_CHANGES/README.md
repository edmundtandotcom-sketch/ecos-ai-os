# PENDING_CHANGES — README
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — folder rule, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §8 (14_CHANGE_LOG); CHANGE_CONTROL.md
Next review: when the first change proposal is filed

## Purpose
Holds every `CHANGE_PROPOSAL.md` instance (as `<ChangeID>.md`) with `ApprovalStatus = PENDING` in `CHANGE_LOG.csv`.

## Rules
- File here the moment a change is proposed (OPERATING_COMMANDS.md command 13, UPDATE MARKETING OS).
- Never edit a pending file's core proposal in place after filing — if the proposal changes, note it in the file and update `CHANGE_LOG.csv`, don't silently rewrite.
- On decision: Edmund/Cindior approves or rejects. Approved → move the file to `../APPROVED_CHANGES/`, update `CHANGE_LOG.csv` (ApprovalStatus = APPROVED). Rejected → move to `../SUPERSEDED/` with the rejection reason appended, update `CHANGE_LOG.csv` (ApprovalStatus = REJECTED, still logged, never deleted).
- Empty is the healthy default state — a full backlog here means reviews are overdue.
