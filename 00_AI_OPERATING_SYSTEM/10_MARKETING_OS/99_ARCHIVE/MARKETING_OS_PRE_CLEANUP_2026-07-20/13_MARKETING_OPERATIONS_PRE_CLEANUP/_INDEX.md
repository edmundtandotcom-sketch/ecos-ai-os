# 13_MARKETING_OPERATIONS — INDEX
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — index
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §8 (13_MARKETING_OPERATIONS)
Next review: whenever a file in this folder is added or changed

## Purpose
The operating manual for the Marketing OS itself: how things are named, checked, sequenced, commanded, reviewed, defined, and owned. Every other folder in `10_MARKETING_OS` depends on this one running correctly.

| File | Purpose | READS FROM | FEEDS INTO |
|---|---|---|---|
| NAMING_CONVENTIONS.md | CMP-/ANG-/CR-/CP-/FUN-/EXP- ID formats + LL- mapping rule | 01_CAMPAIGN_LEGACY_LAUNCH asset-ID rules | every registry and template |
| QA_CHECKLISTS.md | Stage 8 cross-channel QA + Stage 9 launch-readiness gates | CREATIVE_BRIEF.md, CAMPAIGN_LIFECYCLE.md | 08_CAMPAIGNS, 07_CREATIVE_LIBRARY |
| CAMPAIGN_LIFECYCLE.md | 13 stages, diagnosis hierarchy, kill/keep/iterate/scale, 13-status asset lifecycle | build brief §7 maturity scores | 08_CAMPAIGNS, 09_EXPERIMENTS, 11_WINNERS_AND_LEARNINGS |
| OPERATING_COMMANDS.md | 13 standing commands (input/process/output) | all folders | how any desk invokes the system |
| REVIEW_CADENCE.md | Daily/weekly/monthly/quarterly reviews, owner + output each | CAMPAIGN_LIFECYCLE.md | 10_PERFORMANCE, 00_COMMAND_CENTER/08_SESSION_LOG.md |
| DATA_DICTIONARY.md | Field definitions for every registry CSV | 07/08/09/10/11 registry descriptions | all registries (reconcile on build) |
| RESPONSIBILITIES.md | Marketing OS folder → AI TEAM desk mapping | 01_E.C.O.S/00_TEAM_ROSTER.md + charters | every folder's working owner |

## Rule
This folder is procedural, not strategic — it does not set positioning or make campaign calls. Escalate anything that touches positioning or a locked decision to the Strategy Office per RESPONSIBILITIES.md.
