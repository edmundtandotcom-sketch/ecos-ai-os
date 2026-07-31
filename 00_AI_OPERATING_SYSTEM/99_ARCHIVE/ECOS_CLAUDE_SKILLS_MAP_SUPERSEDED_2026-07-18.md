# 08_CLAUDE_SKILLS_MAP.md — Claude Skills per Desk
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none
Sources: installed Claude environment skills audit, 2026-07-10

Which Claude capabilities each desk should reach for. Nothing here needs downloading — these are already installed in Edmund's Claude environment. Workspace command skills (bottom section) live in `.claude\skills\` in this workspace.

---

## Workspace command skills (custom-built, always available here)

| Command | What it does | When |
|---|---|---|
| `/desk <task>` | Routes the task to the right AI TEAM desk and works as it | Any substantial business task |
| `/new-idea <idea>` | Captures a new idea/direction into the brain (Decision Memory / Priorities / Parking Lot) so it is never re-debated | The moment a new direction appears |
| `/session-close` | End-of-session checklist: save decisions, fix indexes, log the session, output summary | End of every working session |
| `/os-audit` | Weekly/monthly system self-audit (drift, duplicates, orphans, CANDIDATE backlog) | Weekly (also scheduled) |

## Installed environment skills, mapped to desks

| Desk | Skill | Use for |
|---|---|---|
| 01 Strategy Office | `deep-research` | Deep, cited, multi-source research before major strategic decisions |
| 01 Strategy Office | `product-management:brainstorm` | Pressure-testing a strategic question with a sharp thinking partner |
| 02 Client Advisory | `anthropic-skills:deep-buyer-profile` | Deep buyer profiling runs (the existing REI method skill) |
| 02 Client Advisory | `anthropic-skills:pdf` / `docx` / `pptx` / `xlsx` | Producing client-facing documents and decks |
| 03 Content Studio | `dataviz` | Any chart/graphic for content or market updates |
| 03 Content Studio | `anthropic-skills:canvas-design` | Visual design work |
| 03 Content Studio | `searchfit-seo:create-content` / `content-brief` | SEO-optimized long-form and YouTube description work |
| 04 Marketing & Ads | `adspirer-ads-agent:keyword-research` | Google Ads keyword research with real CPC data |
| 04 Marketing & Ads | `adspirer-ads-agent:campaign-performance` | Cross-platform campaign performance analysis |
| 04 Marketing & Ads | `marketing:campaign-plan` / `email-sequence` | Campaign planning and nurture sequences |
| 04 Marketing & Ads | Meta Ads MCP tools (connected) | Live Meta campaign/creative/audience work — platform-verification rule applies |
| 05 Agent Recruitment | `marketing:competitive-brief` | Competitive positioning for the Market Maker offer |
| 06 Research Intelligence | `deep-research`, `nimble:search` | Market and competitor sweeps |
| 06 Research Intelligence | `nimble:competitor-intel` / `market-finder` | Structured competitor and market research |
| 07 Operations | GoHighLevel MCP tools (connected) | Contacts, conversations, opportunities, calendars, blogs, social posting |
| 07 Operations | Gmail / Calendar / Drive MCP tools (connected) | Email, scheduling, Drive file operations |
| 07 Operations | Zoom MCP tools (connected) | Meeting assets, recordings, summaries |
| All desks | `anthropic-skills:skill-creator` | Building new workspace skills when a repeated workflow emerges |

## Rule

Before inventing a manual workflow, check this map. If a desk finds itself repeating a workflow 3+ times without a skill, propose a new workspace skill via `anthropic-skills:skill-creator` and register it here.

## READS FROM
- `00_TEAM_ROSTER.md` (desk definitions)

## FEEDS INTO
- Every desk charter (skills are execution accelerators for each desk's SOP)
