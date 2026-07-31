# _INDEX — MARKETING OS (top level)
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (index of `10_MARKETING_OS\`)
Evidence level: N/A (index)
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF §8 folder structure
Next review: when any branch is added, renamed, or removed

---

Purpose: single map of the Marketing OS. Each branch below has its own `_INDEX.md` with per-file detail. Depth ≤4; short names; Markdown + `.csv` registries only.

## Front-door files
| File | Purpose |
|---|---|
| `CLAUDE.md` | Front door: role, source-of-truth hierarchy, two-engine rule, evidence tiers, routing, Challenge/Conflict protocols |
| `README.md` | What this is, build provenance, relationship to AI OS desks and `05_CONTENT_MARKETING_ENGINE` |
| `_INDEX.md` | This file |

## Branches
| Branch | Purpose | Status |
|---|---|---|
| `00_COMMAND_CENTER\` | Marketing status, priorities, active campaigns, decisions required, health, maturity diagnosis, source-of-truth map, contradiction register | Built |
| `01_BUSINESS_AND_BRAND\` | Business context, brand positioning, offers, audiences (pointers); brand voice, proof & claims, compliance | Built |
| `02_CUSTOMER_INTELLIGENCE\` | Objections map, awareness stages, segment usage — marketing-facing digests over TRAPS/VoC/segment masters | Built |
| `03_MARKET_INTELLIGENCE\` | Ad library, funnel library, trends feed, search intelligence, competitors — points at live automations + Weekly Ads library | Built |
| `04_POSITIONING_AND_OFFERS\` | Engine-1 and Engine-2 pointers, mechanisms, qualification — with campaign-usage rules | Built |
| `05_FRAMEWORK_LIBRARY\` | Framework registry (20 frameworks) + one `.md` per framework family + selection engine | Built |
| `06_CHANNEL_PLAYBOOKS\` | 17 playbooks, one per channel (all "DRAFT — pending platform verification") | Built |
| `07_CREATIVE_LIBRARY\` | Creative registry (seeds 16 LL ads) + concepts, hooks, headlines, CTAs | Built |
| `08_CAMPAIGNS\` | Campaign registry (1 active, 1 planned, 6 historical) + ACTIVE/PLANNED/COMPLETED/PAUSED records | Built |
| `09_EXPERIMENTS\` | Experiment registry (empty — none run yet) + backlog of 5 real open hypotheses | Built |
| `10_PERFORMANCE\` | Data sources, import specs, KPI definitions, historical baseline (Codex Tier 2, PII-free) | Built |
| `11_WINNERS_AND_LEARNINGS\` | Learning registry (6 cited learnings), winning-assets policy, failed tests | Built |
| `12_TEMPLATES\` | Campaign/creative/funnel/content/experiment briefs, reviews, postmortem, change proposal, weekly review | Built |
| `13_MARKETING_OPERATIONS\` | Naming conventions, QA checklists, campaign lifecycle, operating commands, cadence, data dictionary, responsibilities | Built |
| `14_CHANGE_LOG\` | Change log `.csv` (CHG-001 = this build) + pending/approved/superseded + change-control doc | Built |
| `99_ARCHIVE\` | Retired Marketing OS files + ECOS build mandate (provenance) | Built |

Note: all 15 branches were populated in the 2026-07-11 build pass. All content is Status: DRAFT pending Edmund/Cindior approval.

READS FROM: `00_AI_OPERATING_SYSTEM\` masters (per branch `_INDEX.md` READS FROM lines).
FEEDS INTO: campaign execution, weekly marketing review, and the AI OS pending-approvals queue.
