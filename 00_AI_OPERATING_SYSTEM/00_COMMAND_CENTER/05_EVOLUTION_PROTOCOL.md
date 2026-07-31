# 05_EVOLUTION_PROTOCOL — HOW THE SYSTEM ABSORBS CHANGE WITHOUT DRIFT
Version: v1.1
Status: APPROVED MASTER
Date: 2026-07-18
Supersedes: v1.0 (2026-07-10) — adds controlled evolution, campaign/asset/private-data routing and folder-by-folder change discipline.
Sources: CLAUDE.md v4.4; 02_OPERATING_RULES v1.1; Decision 095; completed Asset Library and active-campaign architecture.

## 1. The one rule

Every durable new input gets one authoritative home. Chat memory is not the operating system.

## 2. Routing table

| New input | Authoritative home |
|---|---|
| Approved decision | `04_DECISION_MEMORY.md` |
| Proposed decision needing owner approval | `10_PENDING_APPROVALS.md` |
| Priority change | `03_CURRENT_PRIORITIES.md` |
| Valid idea that is not active | `06_PARKING_LOT.md` |
| Mistake or safeguard | `07_LESSONS_LEARNED.md` |
| Positioning/category change | `01_BUSINESS_POSITIONING.md` plus full positioning master |
| Behaviour/file/structural rule | `02_OPERATING_RULES.md` |
| Audit rule or platform-verification rule | `09_AUDIT_AND_MAINTENANCE.md` |
| Session history | `08_SESSION_LOG.md` |
| Live campaign work | `03_ACTIVE_CAMPAIGNS` |
| Permanent asset/source/final | `01_ASSET_LIBRARY` |
| Client/contact/consent record | restricted `00_E.C.O.S_CLIENTS_PRIVATE` |
| Quick or voice capture not yet classified | `12_ECOS_INBOX` |

If something fits two places, save the fact once in the higher-authority file and link to it elsewhere.

## 3. Change discipline

For every governed-file change:

1. Read the current master and Decision Memory.
2. Make the smallest effective change.
3. Bump version and date.
4. Archive the previous approved master before replacement.
5. Update the folder `_INDEX.md` if purpose, status or routing changed.
6. Record the work in `08_SESSION_LOG.md`.
7. Verify the live file after replacement.

## 4. Structural evolution

Decision 095 removed the formal architecture freeze.

Structural work must follow controlled evolution:

1. Solve a defined problem—not a cosmetic preference.
2. Work on one folder/system area at a time.
3. Inventory before moving anything.
4. Verify destination and source parent.
5. Preserve rollback for important files.
6. Move/archive only the approved scope.
7. Recount and verify.
8. Update guides and decision records before continuing.

## 5. Supersession and deletion

- Approved masters are superseded and archived, never silently overwritten or hard-deleted.
- Historical reports and completed one-time records move to `99_ARCHIVE`.
- Obsolete tests, corrupt files, verified exact duplicates and empty shells require explicit deletion approval.
- Similar files are retained until duplication is proven.

## 6. Inbox processing

`12_ECOS_INBOX` is a capture surface, not storage.

For each item:
1. Read it.
2. Decide whether it is a decision, priority, park, lesson, task, campaign input or discardable test.
3. Route it to one home.
4. Remove it from the inbox by moving, archiving or deleting with approval.
5. Return the inbox to zero.

## 7. End-of-session checklist

- Decisions saved or queued?
- Priorities still accurate?
- Parked ideas routed?
- Lessons captured?
- Positioning changes reconciled?
- Files versioned and prior masters archived?
- Indexes updated?
- Active campaign work kept out of the AI OS?
- Assets routed to Asset Library?
- Client data kept private?
- Session logged?
- Inbox processed?
- Platform-specific output verified or labelled draft?

## 8. Audit trigger

Run a full audit when:
- a branch is added or re-scoped
- a major campaign starts or closes
- an Asset Library lifecycle batch completes
- two files give conflicting guidance
- paths stop matching indexes
- a structural problem repeatedly slows execution

Audit first, decide second, implement third. After owner approval, controlled execution may proceed in the same folder-by-folder workflow.
