# 09_AUDIT_AND_MAINTENANCE
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: `00_BRAIN\11_WORKSPACE_SYSTEM_AUDIT_PROTOCOL.md`; `00_BRAIN\10_PLATFORM_VERIFICATION_AND_LIVE_RULES_PROTOCOL.md`
Sources: 00_BRAIN 11 (audit protocol) + 10 (platform verification); AI_OS_REBUILD_SPEC v1.0

> How the AI OS checks itself. A system that cannot check itself cannot scale. Audit surfaces gaps; Edmund approves; then act. **Never rebuild, migrate, rename, delete, or promote during an audit.** Two rhythms: a weekly light check and a monthly (or triggered) full audit. Plus the standing Platform Verification rule.

---

## PART A — WEEKLY LIGHT CHECK (5 minutes)

Run once a week or at the end of an active build session.

```
[ ] Index freshness — does every _INDEX.md match the files actually in its folder?
[ ] CANDIDATE backlog — any CANDIDATE files or decisions waiting on Edmund? List them.
[ ] Priorities current — does 03_CURRENT_PRIORITIES.md still match reality?
[ ] Session log — is the last working session logged in 08_SESSION_LOG.md?
[ ] Platform drafts — any platform-specific output still unverified? Still labelled DRAFT?
```

Output: a short list of anything stale. Fix trivial index/log gaps immediately; flag the rest for Edmund.

---

## PART B — MONTHLY / TRIGGERED FULL AUDIT

### When to run
Monthly as a backstop, or on any trigger: a new master file added or versioned · a branch re-scoped · a campaign launched/paused/retired · positioning changes · Claude gives conflicting advice · folder paths stop matching the master index · a media consolidation batch completes.

### Core audit rule
Do not build, create, move, rename, archive, or promote during an audit. Audit first. Approve second. Act third.

### Audit checks
1. **Structure scan** — do all 10 branches exist? Any unexpected folders? Files in the wrong branch? Anything from an old read-only folder accidentally written into the AI OS?
2. **Constitution alignment** — read `CLAUDE.md`, `00_MASTER_INDEX.md`, `02_OPERATING_RULES.md`, `03_CURRENT_PRIORITIES.md`, `04_DECISION_MEMORY.md`. Are priorities consistent? Decisions recorded? No old structure gone live by accident?
3. **Positioning alignment** — is `01_BUSINESS_POSITIONING.md` still consistent with the `02_POSITIONING_AND_IP/` spine? Are the two engines kept separate? Second Property Ladder™ + Market Maker Method still governing?
4. **Index freshness** — every `_INDEX.md` accurate; READS FROM / FEEDS INTO still correct.
5. **CANDIDATE backlog** — list every CANDIDATE file/decision and how long it's waited.
6. **Orphan / duplicate scan** — files referenced but missing; duplicate purposes; "(1)"/"final"/"latest" filenames (banned); stale cross-references to legacy paths.
7. **Path length** — any folder deeper than 4 below the AI OS root, or any path at risk of Windows limits.
8. **Media registries** — do registries still point at valid legacy paths? Any URGENT-flagged asset (e.g. the 16 Legacy Launch videos) still un-moved?
9. **Platform verification alignment** — is every platform-specific output correctly labelled (Draft / Platform-Checked / Launched / Performance-Reviewed)?

### Audit report format
```
AI OS AUDIT REPORT — Date / Trigger / Audited by
A. What changed since last audit (files added/updated/moved, decisions made)
B. Current state (branches present, missing expected files, unexpected files)
C. Findings — per item: File/Folder · Issue · Severity (Critical/Important/Minor) · Recommended action · Approval needed (Y/N)
D. Priority action list (top items needing Edmund's approval — do not implement automatically)
E. Clean items (what passed)
```

After approved actions: update affected files, `04_DECISION_MEMORY.md`, and `08_SESSION_LOG.md` as needed.

---

## PART C — PLATFORM VERIFICATION RULE (standing)

**MAS strategy is stable. Platform rules are not.** Character limits, ad formats, creative specs, placement rules, targeting options, policy restrictions, and reporting fields change on Meta, Google, YouTube, TikTok, Instagram, WhatsApp, GoHighLevel, Canva, and others.

### The rule
Before finalising any platform-specific output, either (1) verify the latest official platform requirements, or (2) label the output **DRAFT — pending platform verification.** Never claim platform limits are current unless verified.

### Applies before
Launching a paid ad · publishing a post · uploading a YouTube video · creating a YouTube/Google/Meta/TikTok/Reel ad · finalising a landing-page headline · sending WhatsApp/email campaigns · preparing a creative brief · setting campaign tracking.

### Output labels
- **Draft Output** — built on MAS strategy, platform rules not yet verified.
- **Platform-Checked Output** — rules checked, ready for human launch review.
- **Launched Output** — published.
- **Performance-Reviewed Output** — has performance data; review under the performance process.

### Verification sources
Official Meta / Google / YouTube / TikTok Business help centres · current ad-manager or upload screens · trusted updated industry references · internal media-buyer confirmation. When in doubt, verify inside the platform before launch.

### Golden rule
Use MAS strategy to decide **what to say.** Use live platform verification to decide **how it must be formatted.** Never let outdated platform rules weaken a strong idea; never launch platform output without verifying the latest specs.

---

## How AI Should Use This File
- Run Part A weekly and at the end of active build sessions.
- Run Part B monthly or on any trigger; produce the report; wait for Edmund's approval before acting.
- Apply Part C on every platform-facing task — it is always on, no trigger needed.
- Surface findings; never self-implement structural changes. Approval before action.
