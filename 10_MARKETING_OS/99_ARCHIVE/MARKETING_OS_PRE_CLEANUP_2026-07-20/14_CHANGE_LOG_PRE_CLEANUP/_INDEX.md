# 14_CHANGE_LOG — INDEX
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — index
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §8 (14_CHANGE_LOG)
Next review: whenever a change is filed, approved, or rejected

## Purpose
The Marketing OS's own audit trail. Nothing in `05_FRAMEWORK_LIBRARY`, `06_CHANNEL_PLAYBOOKS`, `13_MARKETING_OPERATIONS`, or any registry changes without a logged reason, evidence, and approval status here.

| File/folder | Purpose | READS FROM | FEEDS INTO |
|---|---|---|---|
| CHANGE_LOG.csv | Master ledger of every proposed change (CHG-### rows) | 12_TEMPLATES/CHANGE_PROPOSAL.md instances | every folder a change touches |
| CHANGE_CONTROL.md | 11 change types, Conflict-Detected format, 12-status lifecycle, promotion rules | constitution §9, §15 | how any change gets executed |
| PENDING_CHANGES/ | Filed, undecided proposals | CHANGE_PROPOSAL.md | APPROVED_CHANGES/ or SUPERSEDED/ |
| APPROVED_CHANGES/ | Executed, Edmund/Cindior-approved changes | PENDING_CHANGES/ | target files (rule executed there) |
| SUPERSEDED/ | Rejected or later-replaced changes, kept for audit | PENDING_CHANGES/, APPROVED_CHANGES/ | historical reference only |

## Rule
CHG-001 (this build) is the only row filed at launch, status PENDING. No file in `10_MARKETING_OS` is APPROVED until Edmund/Cindior reviews it — see constitution §9 version workflow.
