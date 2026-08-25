---
name: new-idea
description: Capture a new idea, direction change, or strategy input into the AI OS brain so it is never lost or re-debated. Use when Edmund types /new-idea, says "new idea", "new direction", "change of plan", "remember this decision", or introduces a strategic pivot mid-session.
---

# /new-idea — Evolution Protocol Capture

A new input has arrived: `$ARGUMENTS` (or the idea just discussed).

Run the routing in `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\05_EVOLUTION_PROTOCOL.md`. In short:

1. **Classify it** (one of):
   - **Decision** — Edmund has clearly approved it → append a numbered decision to `00_COMMAND_CENTER\04_DECISION_MEMORY.md` (next number, APPROVED status, decision + reason + impact). If it overrides an older decision, mark the old one `SUPERSEDED by DECISION NNN` — never delete it.
   - **Direction/positioning change** → update `03_CURRENT_PRIORITIES.md` (and `01_BUSINESS_POSITIONING.md` only if the north star itself moved — that requires explicit confirmation from Edmund first). Mark superseded content with a Status line, never delete.
   - **Good idea, not now** → append to `06_PARKING_LOT.md` with a PARK number, one-line value note, and revisit trigger.
   - **Lesson** → append to `07_LESSONS_LEARNED.md`.
2. **Bump versions + indexes.** Any file you touched: bump its Version header and update that folder's `_INDEX.md` if the file list changed.
3. **Log it.** One line in `08_SESSION_LOG.md` under the current session entry (create the entry if none exists today).
4. **Confirm back** in ≤5 lines: what was classified as what, which file(s) now hold it, and what (if anything) it superseded.

Never leave an important input only in chat. If it's not in a file, it's not in the operating system.
