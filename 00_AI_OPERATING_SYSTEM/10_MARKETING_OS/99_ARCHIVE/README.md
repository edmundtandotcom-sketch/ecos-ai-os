# 99_ARCHIVE — README
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — folder rule, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §8 (99_ARCHIVE); constitution `00_AI_OPERATING_SYSTEM/CLAUDE.md` §9 rule 4, §14
Next review: on first archive event

## Purpose
Holds superseded or retired Marketing OS files that are part of the operating system's history. This is not a dumping ground and not the same folder as `14_CHANGE_LOG/SUPERSEDED/` (which holds change-proposal records, not the files themselves).

## Rules
1. **Never hard-delete.** Anything that was ever DRAFT, CANDIDATE, or APPROVED MASTER inside `10_MARKETING_OS` gets archived here, not deleted, when replaced.
2. **Archive before overwrite.** Per constitution §9 rule 4: archive the previous approved version into `99_ARCHIVE` before replacing it. Never silently overwrite an approved master.
3. **Keep provenance.** When archiving a file, keep its original filename and add a one-line header note: `Archived: <date> — superseded by <new file/ChangeID>`.
4. **Structure.** Subfolder by origin path when volume grows (e.g. `99_ARCHIVE/12_TEMPLATES/`, `99_ARCHIVE/13_MARKETING_OPERATIONS/`) — do not flatten history into one folder once it exceeds ~20 files.
5. **Disposable junk only, and only with sign-off.** Hard-delete is reserved for clearly disposable junk (empty stub files, accidental duplicates) and only after showing Edmund/Cindior the list first, per constitution §14.
6. **Log it.** Every archive event gets a row in `14_CHANGE_LOG/CHANGE_LOG.csv` (Type: framework retired/superseded, or the relevant change type) so the audit trail stays intact.

Currently empty — no Marketing OS file has been superseded yet (this is the initial build).
