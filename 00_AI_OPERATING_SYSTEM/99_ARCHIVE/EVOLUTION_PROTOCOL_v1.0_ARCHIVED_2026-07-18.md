# 05_EVOLUTION_PROTOCOL — HOW THE SYSTEM ABSORBS CHANGE WITHOUT DRIFT
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none (new file)
Sources: 00_BRAIN 01_GLOBAL_OPERATING_RULES (Session Transfer, File Update); Business Brain v1.0 maintenance rules; AI_OS_REBUILD_SPEC v1.0

> This is the mechanism that keeps the AI OS alive and honest. Every session produces new ideas, decisions, and direction changes. Without a routing discipline, the brain drifts — it says one thing while the business does another (the exact failure that hid "Agent Edition is active" behind a "parked" label). This protocol prevents that.

---

## 1. The One Rule

**Every new input gets routed to exactly one home, or it is not part of the system.** Chat memory is not the system. The files are the system.

---

## 2. Routing Table — Where Each New Input Goes

| New input in a session | Route to | Action |
|---|---|---|
| A decision Edmund **approves** | `04_DECISION_MEMORY.md` | Add next-numbered decision (APPROVED) |
| A decision proposed, **not yet confirmed** | `04_DECISION_MEMORY.md` | Add next-numbered decision (CANDIDATE) |
| A good idea that is **not now** | `06_PARKING_LOT.md` | Add PARK entry with trigger-to-revisit |
| Something that **changes focus** | `03_CURRENT_PRIORITIES.md` | Bump version, edit priorities |
| A mistake or insight to not repeat | `07_LESSONS_LEARNED.md` | Add LESSON entry |
| A new/changed positioning direction | `01_BUSINESS_POSITIONING.md` + spine in `02_POSITIONING_AND_IP/` | Bump version, edit; supersede old |
| A behaviour / version / naming rule | `02_OPERATING_RULES.md` | Bump version, edit |
| A new automation, script, or SOP | relevant branch (usually `08_OPERATIONS/`) | Add file + update that `_INDEX.md` |
| A platform-spec change | verify live; note in `09_AUDIT_AND_MAINTENANCE.md` | Label DRAFT until verified |

If an input fits two homes, put it in the most authoritative one and cross-link. If it fits none, it probably belongs in the Parking Lot or should be challenged.

---

## 3. Any File Change → Three-Step Discipline

When you change any AI OS file:

1. **Bump the version** in the header (v1.0 → v1.1 for edits, → v2.0 for a rewrite) and update the `Date`.
2. **Update that folder's `_INDEX.md`** if the file's purpose, status, or cross-links changed.
3. **Note it in `08_SESSION_LOG.md`** — one line: what changed, why, which files.

No silent edits. A change that isn't versioned and logged is invisible to the next session.

---

## 4. New Direction Overrides Old → Supersede, Never Delete

When a new direction replaces an old file's logic:

1. Write/adopt the new master.
2. Edit the **old file's header** to `Status: SUPERSEDED by <relative link>` — do not delete it.
3. If the old file is a full approved master being replaced, archive a copy to `99_ARCHIVE` first (per `02_OPERATING_RULES.md` B4).
4. Log the supersession in `04_DECISION_MEMORY.md` if it's a decision-level change.

The trail must always show: what replaced what, when, and why. Nothing in the operating system is ever hard-deleted.

---

## 5. Conflict Handling

If a new input conflicts with an existing approved file, do NOT silently merge. Flag it:
- Which files conflict, what the conflict is, which is newer/more authoritative.
- Recommended source of truth.
- Whether Edmund approval is required (it is, for any master).

Then wait for the call before overwriting. Known conflicts are tracked; resolving one is a file edit, not a chat note.

---

## 6. END-OF-SESSION CHECKLIST (run at the end of every working session)

Run this before closing. It takes two minutes and prevents drift.

```
[ ] 1. Did we make any decision? → route to 04_DECISION_MEMORY.md (APPROVED or CANDIDATE)
[ ] 2. Did any idea come up that's "not now"? → 06_PARKING_LOT.md
[ ] 3. Did priorities change? → 03_CURRENT_PRIORITIES.md (bump version)
[ ] 4. Did we learn something worth not repeating? → 07_LESSONS_LEARNED.md
[ ] 5. Did positioning/direction shift? → 01_BUSINESS_POSITIONING.md + 02_POSITIONING_AND_IP spine
[ ] 6. For every file changed: version bumped? _INDEX.md updated?
[ ] 7. Did any new direction supersede an old file? → old file header set to SUPERSEDED
[ ] 8. Log the session in 08_SESSION_LOG.md (date, what was built, decisions, files, next action)
[ ] 9. Any unverified platform-specific output still labelled DRAFT?
[ ] 10. If session ran long (~20 exchanges): write a Session Transfer Summary + tell Edmund to continue fresh
```

If every box is checked, the system is current. If not, the next session inherits drift.

---

## 7. Quarterly Full-Audit Trigger

Every quarter (or on any of the triggers in `09_AUDIT_AND_MAINTENANCE.md`), run the full workspace audit: index freshness, CANDIDATE backlog, orphan files, path length, duplicate scan, positioning still current. Audit surfaces; Edmund approves; then act. Never rebuild during an audit.

---

## How AI Should Use This File

- Open this at the **end** of any working session and run the Section 6 checklist. This is not optional — it is the maintenance that keeps the brain honest.
- During a session, when a new input appears, route it immediately via Section 2 rather than "remembering" it.
- On any file edit, apply the Section 3 three-step discipline.
- When new overrides old, use Section 4 — supersede with a header edit, never delete.
