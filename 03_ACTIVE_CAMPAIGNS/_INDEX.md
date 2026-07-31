# 03_ACTIVE_CAMPAIGNS — Lifecycle Index
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-20
Sources: root `CLAUDE.md` v4.6; AI OS campaign-routing rules; Decision 108; live Drive audit 2026-07-20.

## Purpose

This is the single production workbench for campaigns. It holds campaign-specific briefs, scripts, working media, tools, live links, tracking and results until completion.

## Lifecycle

| Folder | Entry rule | Exit rule |
|---|---|---|
| `00_CAMPAIGN_INBOX/` | Unclassified campaign input with a likely owner | Move to Active when objective/owner exist; archive/quarantine if not a campaign |
| `01_ACTIVE/` | Approved work currently being built or run | Move to Scheduled when launch-ready; Completed when work is finished |
| `02_SCHEDULED/` | Approved and launch-ready with a date/window | Move to Active if execution resumes; Completed after the run |
| `03_COMPLETED/` | Finished campaign work retained for result review and promotion | Promote approved reusable outputs; move old closed work to archive under retention rules |
| `99_ARCHIVE/` | Superseded, cancelled, rollback or historical campaign material | Read-only; never current authority |

## One campaign, one workbench

1. Use `YYYY-MM_Campaign_Name` for campaign folders unless an exact date is operationally important.
2. Do not create a second active folder for recording output, scripts or tools belonging to the same campaign.
3. Each active campaign requires one `_INDEX.md` that states objective, authority, map, current outputs, owners/handoffs and definition of done.
4. Move the whole campaign folder through lifecycle stages; do not duplicate it.
5. Keep strategy/doctrine in the AI OS and point to it from the campaign index.
6. Keep named client/contact evidence in the restricted private drive.
7. After completion, promote only approved reusable assets into `01_ASSET_LIBRARY`; do not copy every working file.

## Current active register — 2026-07-20

| Campaign | Status | Governing note |
|---|---|---|
| `2026-07_SecondPropertyLadder_AdProduction/` | ACTIVE | One consolidated workbench; canonical control, source references, current scripts, recordings and archive separated |
| `2026-07_AgentEdition_MarketMaker_Build/` | ACTIVE | Agent Edition OS governs; current tools remain active and superseded MAS artifact is archived |
| `2026-07_LegacyLaunch_Meta_Wave1/` | ACTIVE | Existing five-folder campaign structure retained |

June weekly content briefs were moved from Inbox to Completed. The Inbox is clear after the audit.

## Completion gate

A campaign closes only when:

- result/learning record is captured;
- reusable assets are approved and promoted once;
- PII/evidence is routed privately;
- superseded material is archived;
- the campaign index records the final status and handoffs.
