# CHANGE CONTROL
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — governance procedure, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §2 (build rules), §8 (14_CHANGE_LOG); constitution `00_AI_OPERATING_SYSTEM/CLAUDE.md` §9 (version workflow), §15 (evolution protocol)
Next review: after first change proposal is filed

## 1. The 11 change types
1. New framework added
2. Framework promoted (CANDIDATE → APPROVED MASTER)
3. Framework retired/superseded
4. Naming-convention change
5. Campaign-lifecycle/process change
6. KPI/target-threshold change
7. Compliance-rule update
8. Platform-spec update
9. Registry field/schema change
10. Positioning/engine change — cannot be approved inside Marketing OS; routes to Strategy Office and the AI OS constitution
11. Contradiction resolution (closing a C0# item in CONTRADICTION_REGISTER.md)

## 2. Filing a change
Use `12_TEMPLATES/CHANGE_PROPOSAL.md`. File in `PENDING_CHANGES/` as `<ChangeID>.md`, add the matching row to `CHANGE_LOG.csv`.

## 3. Conflict-Detected response format
When a proposed change conflicts with an existing APPROVED item or a locked decision, stop and output:
```
CONFLICT DETECTED
Existing rule: <file + section>
Proposed rule: <what's being proposed>
Conflict: <one sentence>
Recommendation: <keep existing | adopt proposed | escalate to Edmund/Cindior>
```
Never silently overwrite. Log the conflict as a new or updated C0# row in `00_COMMAND_CENTER/CONTRADICTION_REGISTER.md`.

## 4. The 12-status knowledge lifecycle
1. OBSERVED — raw signal, not yet written up
2. HYPOTHESIS — Tier 5, logged to an experiment backlog
3. TESTING — experiment ACTIVE
4. DRAFT — written, unreviewed
5. CANDIDATE — reviewed internally, pending Edmund/Cindior
6. PENDING_APPROVAL — submitted via CHANGE_PROPOSAL.md, sitting in PENDING_CHANGES
7. APPROVED MASTER — promoted, authoritative
8. ACTIVE — in live use / live campaign
9. MONITORING — approved and running, performance being tracked
10. REJECTED — proposal declined, logged not deleted
11. SUPERSEDED — replaced by a newer approved version
12. ARCHIVED — retired, kept for reference, never hard-deleted

## 5. Promotion rules
**May promote (DRAFT/CANDIDATE → APPROVED MASTER) when:**
- Tier 1 or Tier 2 evidence exists, OR
- Edmund/Cindior gives explicit sign-off, OR
- An experiment's minimum-useful-data threshold was met with a clear win (EXPERIMENT_BRIEF.md decision rule).

**May NOT promote when:**
- Only Tier 5 (hypothesis) evidence exists and no test has run.
- It contradicts a LOCKED positioning item (§3 of the build brief).
- It blends the Client Advisory and Agent Edition engines.
- An unresolved C0# contradiction directly touches it.
- Compliance (CEA/PDPA/MAS) has not been checked.
- Only one person's opinion supports it — no data, no second read.

**Only Edmund or Cindior executes a promotion.** Any desk, including this one, may only propose (file a CHANGE_PROPOSAL.md and move status to PENDING_APPROVAL).

## 6. Demotion
An APPROVED MASTER item found wrong or outdated moves to SUPERSEDED (if replaced) or ARCHIVED (if retired outright) via the same CHANGE_PROPOSAL.md route. Never edit an approved master silently — archive the prior version first per constitution §9.
