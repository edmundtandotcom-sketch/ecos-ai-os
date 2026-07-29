# 07_LESSONS_LEARNED
Version: v2.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: `00_BRAIN\07_LESSONS_LEARNED.md`
Sources: 00_BRAIN 07_LESSONS_LEARNED; AI OS rebuild observations 2026-07-10

> Use this to avoid repeating mistakes, overbuilding, creating confusion, or reviving rejected ideas. If a lesson improves future decisions, save it here — not in chat.

---

## Carried Lessons (001–008)

| # | Lesson | Future rule |
|---|---|---|
| 001 | Too many folders create confusion, not power. | Only create a folder with a repeated need, clear owner, clear retrieval purpose. |
| 002 | Brain and storage are not the same. | Build brain architecture before migrating execution documents. |
| 003 | Shared assets must stay lean. | Shared folders hold only master reusable materials. |
| 004 | Old work can be valuable without being live. | Classify every old file (Keep / Rewrite / Archive / Reject / Reference) before migrating. |
| 005 | Instructions must be saved to become system memory. | Save decisions, rules, priorities, lessons into the correct file. |
| 006 | Build → Verify → Approve → Continue. | Complete a segment, verify, approve, then continue. |
| 007 | ~~Google Docs and Markdown serve different purposes.~~ **Revised — see Lesson 009.** | Markdown is now the single source of truth. |
| 008 | Client segmentation must not become generic. | Strategic Intent is primary; broad market type is only outer classification. |

*Note:* Lesson 007's "keep both formats" guidance is superseded by the md-only rule (Decision 027). Kept here as history.

---

## New Lessons From The AI OS Rebuild (009–013)

### LESSON 009 — Dual .md/.docx Twins Caused Duplication And Authority Confusion
Status: ACTIVE
Lesson: requiring every file in both Markdown and Google Doc form (old Decision 015) doubled the file count and created "which twin is the master?" ambiguity, plus stale drift between the two.
Future rule: **Markdown is the single source of truth.** No `.docx` twins. Render `.md` for human review. (See Decision 027.)

### LESSON 010 — "(1)" Duplicate Filenames Caused Authority Confusion
Status: ACTIVE
Lesson: files like `03_CURRENT_PRIORITIES (1).md` sitting next to `03_CURRENT_PRIORITIES.md` made it impossible to know which was live without opening both.
Future rule: **versioned filenames only** (v1, v2, v3). No "(1)", "final", "latest", or "copy" suffixes. One file per purpose. (See `02_OPERATING_RULES.md` C3.)

### LESSON 011 — Brain Drift: The Brain Said "Parked" While The Area Was The Most Active
Status: ACTIVE
Lesson: the brain still labelled Agent Edition "parked until Segment 6" while it had become the most active build area (positioning, workshop, scorecard). The map contradicted the territory.
Future rule: **run the end-of-session routing checklist** (`05_EVOLUTION_PROTOCOL.md` §6) so priorities and parks reflect reality. Drift is a maintenance failure, not an accident.

### LESSON 012 — Deep Nesting Broke Windows Paths
Status: ACTIVE
Lesson: long, deeply nested folder chains hit Windows path-length limits and made files unreachable.
Future rule: **max folder depth 4** below the AI OS root; short folder/file names; no nested archives. (See `02_OPERATING_RULES.md` C4.)

### LESSON 013 — Empty Mandated Folders Were Gaps Hiding In Plain Sight
Status: ACTIVE
Lesson: folders that "should" exist (Brand Assets, Proof Bank) sat empty, so the system looked complete while a real capability was missing.
Future rule: every folder's `_INDEX.md` must state what's present AND flag gaps ("GAP: no centralized logo/headshot pack — Edmund to fill"). An empty folder with no gap note is a hidden hole.

---

## New Lessons From The Marketing OS Build + Decision-Ruling Session (014)

### LESSON 014 — Parallel Same-Day Sessions Can Rule Conflicting Decisions
Status: ACTIVE
Lesson: Decision 036 ("Step is the public word") and Decision 055 ("Move" everywhere) were both ruled by Edmund on 2026-07-11 in two different sessions running close together. The second ruling was presented as if it might be new, when a naming decision already existed — caught only because the decision-numbering collision was surfaced explicitly before writing (Edmund confirmed "use moves" once the full cascade cost was shown). Silent overwrite would have left two contradictory masters both claiming APPROVED status.
Future rule: **immediately before appending a new decision number, re-read `04_DECISION_MEMORY.md` fresh** (not from earlier-in-session memory) — decision numbers and rulings can move mid-session when other sessions are active in parallel. If a collision is found, present both rulings side-by-side to Edmund with the rework cost before proceeding, rather than assuming the newer instruction silently wins.

---

## New Lesson From The Second Property Ladder Interactive Build Session (015)

### LESSON 015 — Gamified/Quiz Builds Fail When Treated As Diagnostics Instead Of Sales Instruments; Subagent Self-Reports Are Not Sufficient QA
Status: ACTIVE
Lesson: the Second Property Readiness Check™ and its landing pages went through four rebuild rounds in one session. Each round fixed what was asked but missed the actual bar until Edmund named it directly: "the entire quiz is to be done like a sales page, bringing them through the end to take action." Separately, real user-visible bugs (overlapping text, a progress-bar label overflowing its container, a sticky bar covering content) were repeatedly missed by build agents that self-reported successful testing via DOM/console checks only — every one of them was only caught when the orchestrator personally drove the artifact in a real, foregrounded browser and looked at actual screenshots.
Future rule: **before building any quiz, diagnostic, or gamified funnel, load `13_INTERACTIVE_BUILD_STANDARDS.md` (via the `/build-interactive` skill) and set the sales-instrument framing, result-reveal plan, and interactivity benchmark explicitly before writing anything.** Separately, for ANY visual/interactive artifact regardless of type: a subagent's self-reported testing is never sufficient sign-off — the orchestrator must personally verify with real screenshots in a properly-foregrounded browser before presenting or publishing. If a subagent reports it couldn't get screenshots working, that is a flag to re-verify personally, not evidence the build is clean.

---

## Lesson Update Rule
When a mistake or insight is worth not repeating, add the next-numbered lesson here and route it via `05_EVOLUTION_PROTOCOL.md`. Do not rely on memory.
