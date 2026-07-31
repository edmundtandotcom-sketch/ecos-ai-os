# 09_CLAUDE_CAPABILITY_MAP — EXECUTION AND COMMAND ROUTING
Version: v2.0
Status: APPROVED MASTER
Date: 2026-07-18
Supersedes: `08_CLAUDE_SKILLS_MAP.md` v1.0 — replaces a static July 10 plugin inventory with a verify-before-use capability map.
Sources: current E.C.O.S routing model; Operating Agreement; AI OS file and platform-verification rules.

## Purpose

Map tasks to capabilities without assuming a particular skill, connector, command or plugin is permanently installed.

Tool availability changes by environment. Verify before invoking.

## Required orchestration header

> you are the orchestrator, delegated the building to sonnet 5, opus 4.8, and never spawn another fable 5 agent. you plan, you delegate to cheaper model and you do the QA at the end. /compact

## Model roles

| Role | Use |
|---|---|
| Fable 5 | Plan, route, delegate and final QA only |
| Sonnet 5 | Default builder and executor |
| Opus 4.8 | High-stakes, complex or deep-synthesis work |

Never spawn another Fable 5 agent. Use the cheaper suitable builder.

## Capability map

| Need | Lead desk | Capability to verify |
|---|---|---|
| Major strategy or architecture | Strategy | Deep reasoning, research, file audit |
| Property/client diagnosis | Client Advisory | Advisory masters, document analysis |
| Organic scripts and content | Content | Writing, document production, design |
| Paid marketing and funnels | Marketing | Current web research, platform tools, performance data |
| Agent workshop and recruitment | Agent Edition | Presentation, curriculum, campaign support |
| Market/competitor research | Research | Web research, source citation, data analysis |
| CRM/GHL/automation | Operations | GHL, Drive, Gmail, Calendar, code/runtime tools |
| Qualification/closing/follow-up | Sales | Sales OS, CRM context, conversation analysis |

## Workspace commands

Commands such as `/desk`, `/new-idea`, `/session-close` and `/os-audit` may exist in a local Claude Code environment. Before relying on one:

1. verify the command/skill exists
2. verify its paths match `00_E.C.O.S`
3. verify it follows the current eight-desk roster
4. fall back to the charter manually when unavailable

Do not write “always available” unless verified in the current environment.

## Connected-tool rule

- Use connected tools only when they are available and relevant.
- Use official/current web sources for changing public facts.
- Read current files before editing.
- Never expose connector IDs, credentials or internal tool schemas.
- Client PII remains in restricted systems.
- External sends, destructive actions and paid changes require explicit approval.

## Repeated-workflow rule

When a workflow repeats three or more times:
1. confirm it is stable and useful
2. document the manual process
3. propose a reusable skill/automation
4. assign an owner and source of truth
5. register it here only after it exists and is verified

## READS FROM

`00_TEAM_ROSTER.md`, desk charters and current environment capability discovery.

## FEEDS INTO

Every desk’s execution plan.
