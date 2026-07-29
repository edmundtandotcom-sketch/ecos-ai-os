# PROMPT — REI Ads Creative & Reporting Intelligence Dashboard (RESCUED — NO CONTENT FOUND)

Version: v1.0
Status: REGISTRY
Date: 2026-07-10
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\_MIGRATION_TO_WINDOWS\cowork-sessions-and-projects\local-agent-mode-sessions\a8b1c985-b212-4e62-94ca-e2141fdcb2ee\ea889d25-268c-495b-b3aa-3d96b212fd26\local_ce14d77b-781e-4d53-865e-bbabd0a954da.json` (session title: "REI Ads Creative  & Reporting Intelligence dashboard"; model: claude-sonnet-4-6)

## Finding
This session JSON was parsed successfully, but its `initialMessage` field (the field that carries the real, business-specific agent prompt in every other rescued session) contains only:

```
its a success...
```

There is no recoverable custom prompt in this session. The `systemPrompt` field is the generic Cowork application boilerplate shared by every session (not a real agent prompt), and `systemPromptRendererAppends` is empty. `slashCommands` is just the full default plugin/skill catalogue available to Cowork at the time — not evidence of a custom build.

## Recommendation
Do not treat this as the source of the live "REI Ads Creative & Reporting" dashboard prompt. The actual dashboard logic is already captured live in `02_SCRIPTS/REI_AppsScript_ACTIVE_v8.43.gs` + `REI_GoogleAds_Script_ACTIVE_v8.gs` and their rules in `01_CRM_AND_TRACKING/02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md`. If a distinct "ads creative & reporting" scheduled task once existed with real instructions, it was not captured in this session — check with Edmund/Cindior whether a working version exists elsewhere (e.g. a Cowork Scheduled Task not present in this migration snapshot) before assuming this session is the source.
