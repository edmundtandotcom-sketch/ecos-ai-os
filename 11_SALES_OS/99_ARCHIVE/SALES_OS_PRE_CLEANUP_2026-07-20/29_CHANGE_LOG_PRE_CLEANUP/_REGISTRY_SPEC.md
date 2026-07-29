# _REGISTRY_SPEC — CHANGE_LOG.csv
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: SALES_OS_BUILD_SPEC_v1 mandate §22; `10_MARKETING_OS\14_CHANGE_LOG\CHANGE_LOG.csv` (sibling column pattern)

---

## Purpose

Column definitions for `CHANGE_LOG.csv`. One row = one proposed or executed change to any rule, framework, or file in this OS.

## Columns

| Column | Definition |
|---|---|
| `ChangeID` | Unique ID, format `CHG-###` |
| `Date` | Date proposed |
| `ProposedBy` | Who/what proposed it |
| `Type` | One of: New System Build, Framework Update, Registry Schema Change, Naming Change, Content Correction, Contradiction Resolution, Promotion (DRAFT→APPROVED), Demotion, Archive, Rollback, Other |
| `CurrentRule` | What the system currently says/does, cited exactly |
| `ProposedRule` | What should replace it |
| `Reason` | Why the current rule is wrong or outdated |
| `Evidence` | Source(s) + evidence tier |
| `Confidence` | High / Medium / Low + reasoning |
| `Scope` | How broad the change is |
| `FilesAffected` | Exact files touched |
| `BranchesAffected` | Which of the 30 branches |
| `Risk` | What breaks if wrong; blast radius |
| `ApprovalStatus` | PENDING / APPROVED / REJECTED / SUPERSEDED |
| `ReviewDate` | Next check-in or re-check trigger |
| `Rollback` | Exact steps to revert |

## Workflow

1. Draft via `28_TEMPLATES\CHANGE_PROPOSAL.md`, filed in `PENDING_CHANGES\` as `<ChangeID>.md`.
2. Add the matching row to `CHANGE_LOG.csv` with `ApprovalStatus: PENDING`.
3. On Edmund's decision: move the file to `APPROVED_CHANGES\` or mark `REJECTED` in place; update the CSV row.
4. If a later change replaces an approved one, move the old file to `SUPERSEDED\` and set `ApprovalStatus: SUPERSEDED`.

READS FROM: SALES_OS_BUILD_SPEC_v1.
FEEDS INTO: `CHANGE_LOG.csv`; `PENDING_CHANGES\`, `APPROVED_CHANGES\`, `SUPERSEDED\`.
