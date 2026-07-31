# _INDEX — 03_AUTOMATIONS

Version: v1.2
Status: APPROVED MASTER (live skills/templates) + REGISTRY (rescued prompts)
Date: 2026-07-11
Supersedes: v1.1 (2026-07-11) — updated for Decision 067 (Edmund's O14/O15 rulings): `rei-weekly-content-brief_SKILL.md` re-scoped to v2.1 (Family Legacy/Mash-up/SI-06 fully removed from the live automation and its mirror; SI-05 + Evergreen Authority replace the old segmentation)
Sources: `H:\Shared drives\00_E.C.O.S\Scheduled\`, `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\Templates\`, `H:\Shared drives\00_E.C.O.S\_MIGRATION_TO_WINDOWS\cowork-sessions-and-projects\local-agent-mode-sessions\`

## Purpose
Live scheduled-task skills, the task-template standard, and rescued agent prompts recovered from the pre-Windows-migration Cowork session archive. This is the operations team's automation DNA.

## Files — Live, currently scheduled

| File | Description |
|---|---|
| `rei-weekly-content-brief_SKILL.md` | v2.1 — REI Unified Weekly + Bi-weekly Intelligence Task. Runs Monday 9 AM. Combines the weekly content brief and conditional bi-weekly rollup into one scheduled task. **Re-scoped 2026-07-11 (Decision 067, O14 ruling): Family Legacy, Mash-up, and SI-06 classification fully removed; angles now segment by SI-05 (decouple) or Evergreen Authority.** Mirrors the live file 1:1. |
| `singapore-property-ads-brief_SKILL.md` | v1.0 — Singapore property ads intelligence: pulls top 50 real ads from Meta/Google/YouTube via Chrome extension, builds weekly brief + bi-weekly rollup + resource library. Chrome-tool dependent, no synthesis fallback. |

## Files — Templates

| File | Description |
|---|---|
| `MASTER_SCHEDULED_TASK_TEMPLATE_v1.0.md` | The standard format for any new recurring scheduled task. Copy this before building a new automation. |
| `rei-bi-weekly-rollup_PROMPT_v1.0.md` | Filled-in example applying the master template — REI Bi-Weekly Rollup Summary. |
| `rei-weekly-content-brief_PROMPT_v1.0.md` | Filled-in example applying the master template — REI Weekly Content Intelligence Brief. |

## Files — Rescued prompts (from `_MIGRATION_TO_WINDOWS`)

Source: session folder `_MIGRATION_TO_WINDOWS\cowork-sessions-and-projects\local-agent-mode-sessions\a8b1c985-b212-4e62-94ca-e2141fdcb2ee\ea889d25-268c-495b-b3aa-3d96b212fd26\` — 22 local Cowork session JSONs total. Each carries a generic harness `systemPrompt` (identical across all, not rescued) and a session-specific `initialMessage` (the real custom agent prompt, rescued below). Titles/session IDs were read directly from each JSON's `title` field; content matched against scheduled-tasks.json where possible.

| File | Session title | Status |
|---|---|---|
| `PROMPT_REI_Monday_Content_Intelligence_RESCUED.md` | REI Monday content intelligence | Full, usable prompt (11,608 chars). This is the LIVE session — confirmed by cross-reference to `scheduled-tasks.json`'s `rei-monday-content-intelligence` task, which points at this exact session ID. Source JSON stored the prompt twice verbatim; de-duplicated in the rescue. |
| `PROMPT_XREI_Friday_Performance_Report_RESCUED.md` | X-REI Friday performance report | Full, usable prompt (4,414 chars) — ad campaign Scale/Watch/Kill scoring logic for the Friday performance report. |
| `PROMPT_MAS_Agent_Coaching_Programme_RESCUED.md` | MAS agent coaching programme | Partial — a short continuation/status message about a "handoff memory" build, not the full coaching programme content. Registered as a pointer only; see QA note inside the file. |
| `PROMPT_Monday_Income_Focus_Briefing_RESCUED.md` | Monday income focus briefing | Full, usable prompt (2,447 chars) — Calendar + Gmail scan, income-priority tabulation, work/family balance check. |
| `PROMPT_REI_Ads_Creative_Reporting_Dashboard_RESCUED.md` | REI Ads Creative & Reporting Intelligence dashboard | **No usable content found.** `initialMessage` was only "its a success..." — see file for full finding and recommendation. |
| `YOUTUBE_SCAN_METHOD_RESCUED.md` | (Cowork Space memory, rescued 2026-07-11) | RSS-feed workaround + known channel IDs for the Monday Content agent, incl. a note that the catalog's "@AaronLin" handle is wrong. Supports `rei-weekly-content-brief_SKILL.md`. |

### Sessions found but not rescued — CLOSED 2026-07-11
The remaining ~17 sessions were content-reviewed in full on 2026-07-11 (cleanup sign-off verification, second pass that read `outputs\` folders, not just session JSONs). All unique content is now rescued: 3 MAS coaching-programme strategy docs → `06_KNOWLEDGE_VAULT\04_MARKETING_REFERENCES\` + `04_AGENT_EDITION_OS\01_WORKSHOP\` (see `MAS_Doc1/Doc2/Coaching_Influencer_*_RESCUED.md`), 3 Space-memory files → `05_CONTENT_MARKETING_ENGINE\00_FOUNDATIONS\` + this folder. Everything else in the session archive is junk, duplicates, or superseded — full per-session verdicts in `00_COMMAND_CENTER\11_CLEANUP_SIGNOFF_LIST_v1.0_CANDIDATE.md`.

## READS FROM
- `01_CRM_AND_TRACKING` (rules these automations implement)
- `06_KNOWLEDGE_VAULT` (source catalogs referenced by the content intelligence prompt)

## FEEDS INTO
- `01_E.C.O.S/07_OPERATIONS_DESK.md` (owns automation maintenance)
- `01_E.C.O.S/03_CONTENT_STUDIO.md` (consumes weekly content brief output)
- `01_E.C.O.S/04_MARKETING_ADS_DESK.md` (consumes Friday performance report + ads brief output)

## Pending Edmund approval (CANDIDATE)
None as new CANDIDATE — rescued prompts are tagged REGISTRY (historical record, not active masters). If Edmund wants to reactivate any rescued prompt as a live scheduled task, promote it through the version workflow (DRAFT → CANDIDATE → APPROVED MASTER) first.
