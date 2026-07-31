# 09_AUDIT_AND_MAINTENANCE
Version: v1.1
Status: APPROVED MASTER
Date: 2026-07-18
Supersedes: v1.0 (2026-07-10) — updates audit coverage for the live workspace, Asset Library lifecycle, active-campaign workbench, private-client boundary and controlled evolution.
Sources: CLAUDE.md v4.4; root CLAUDE.md v4.5; Decision 095; current workspace inventory.

## 1. Audit principle

Audit first. Decide second. Implement third.

An audit may identify and document findings. Structural or destructive action begins only after the scope is approved. Once approved, execute one folder at a time, preserve rollback and verify every move.

There is no formal architecture freeze. Controlled improvement is allowed when it solves a real operating problem.

## 2. Weekly light check

- Command Center indexes match the physical files.
- `03_CURRENT_PRIORITIES.md` matches current revenue work.
- Decision Memory includes recent rulings.
- Pending Approvals contains only genuinely open owner decisions.
- Session Log includes recent material work.
- `12_ECOS_INBOX` is processed to zero.
- No active campaign files have leaked into the AI OS.
- No new bulk media or raw client data has entered the AI OS.
- Platform-specific outputs remain verified or clearly labelled draft.

## 3. Monthly or triggered full audit

Run when:
- a branch or workspace surface changes
- a campaign launches, pauses or completes
- an Asset Library batch completes
- files conflict
- retrieval repeatedly fails
- paths or indexes drift
- new client-data risk is found
- a major system is proposed

### A. Workspace root

Confirm:
- `00_AI_OPERATING_SYSTEM`
- `01_ASSET_LIBRARY`
- `03_ACTIVE_CAMPAIGNS`
- `_ARCHIVE`
- `_BACKUPS`
- `_QUARANTINE`
- technical folders and root control files

No random loose production files.

### B. AI Operating System

Check:
- all governed branches exist
- every branch index is current
- no unnumbered project folder is loose at AI OS root
- no bulk media, active campaign production or raw client data is stored inside the brain
- Marketing OS / Content Engine and Sales OS / Client Advisory overlaps are documented, not silently duplicated

### C. Asset Library

Check lifecycle routing:
- Upload Inbox processed
- Approved Library contains only approved reusable assets
- Source Archive contains raw/editable production sources
- Campaign Finals are distribution-ready
- Creative Intelligence contains tests, swipes and performance learning
- Expired/Retired contains superseded or time-sensitive material
- Migration Archive contains provenance and legacy shells
- duplicate-review folders contain only verified duplicate candidates
- nothing is deleted without explicit approval

### D. Active campaigns

Check:
- one folder per active workstream
- briefs, scripts, working media, tracking and results stay together
- completed campaigns are promoted through the Asset Library lifecycle
- no campaign is split across several competing homes

### E. Private client data

Check:
- names, phone numbers, emails, case records and consent are restricted
- GHL source-of-truth rules are followed
- no raw client data exists in Asset Library or the general AI OS
- do-not-contact and consent rules are preserved

### F. Governance

Read and compare:
- root `CLAUDE.md`
- AI OS `CLAUDE.md`
- `00_MASTER_INDEX.md`
- `02_OPERATING_RULES.md`
- `03_CURRENT_PRIORITIES.md`
- `04_DECISION_MEMORY.md`
- `11_OPERATING_AGREEMENT.md`

Flag any contradiction before acting.

### G. File quality

Check:
- one current master per purpose
- approved masters have version headers
- old versions are archived
- no `(1)`, `final`, `latest`, `copy` authority confusion
- no broken links or stale legacy paths
- path depth and Windows length remain manageable

## 4. Audit report format

- Trigger and scope
- Physical inventory
- Findings by severity
- Exact recommended action
- Approval required
- Rollback method
- Verification method
- Clean items
- Next folder only

## 5. Platform verification

Before launch or final platform-specific production, verify current official requirements for Meta, Google, YouTube, TikTok, Instagram, WhatsApp, GoHighLevel, Canva and other changing platforms.

Labels:
- DRAFT — pending platform verification
- PLATFORM-CHECKED
- LAUNCHED
- PERFORMANCE-REVIEWED

Use internal strategy to decide what to say. Use current platform verification to decide how it must be formatted.

## 6. Maintenance cadence

- Weekly: light check
- Monthly: full audit backstop
- After a major folder cleanup: recount, update guides and log changes
- Before leaving a folder: confirm it is clear and state what remains intentionally
