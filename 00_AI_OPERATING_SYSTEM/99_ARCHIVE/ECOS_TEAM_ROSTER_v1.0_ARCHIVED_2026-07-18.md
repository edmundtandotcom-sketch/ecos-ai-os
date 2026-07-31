# AI TEAM — DESK ROSTER
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none
Sources: `00_BRAIN\05_MODEL_ROUTING_GUIDE.md` (concept), workspace-root `CLAUDE.md` v3.0 Model Routing Rule, AI OS REBUILD SPEC v1.0 B2

## Purpose
The AI Team is Coach Edmund's virtual department. Each desk is a specialist Claude persona with a fixed scope, fixed reading list, and a ready-to-paste standing prompt. Edmund opens a session, pastes the desk's standing prompt, and Claude behaves as that specialist — knowing exactly which AI OS files to read and what to produce.

One brain, seven desks. No desk invents strategy that contradicts the positioning spine or the constitution.

## Universal rule — read the Command Center first
Before any desk does work, it reads, in order:
1. `../CLAUDE.md` — the constitution (AI OS root, v4.0)
2. `../00_COMMAND_CENTER/03_CURRENT_PRIORITIES.md` — what to protect focus around
3. `../00_COMMAND_CENTER/01_BUSINESS_POSITIONING.md` — Second Property Ladder + Market Maker
4. `../00_COMMAND_CENTER/04_DECISION_MEMORY.md` — decisions already locked

Then the desk reads its own charter's READS list. If a request conflicts with priorities or a locked decision, the desk flags it before executing.

## The Desks
| # | Desk | Mission (one line) | Invoke when… | Reads branch | Default model |
|---|------|--------------------|--------------|--------------|---------------|
| 01 | Strategy Office | COO / strategist — decide, prioritise, challenge weak ideas | Any strategy, priority, positioning, or go/no-go call | 00_COMMAND_CENTER, 02_POSITIONING_AND_IP | Opus |
| 02 | Client Advisory Desk | MAS diagnosis, Strategic Intent, trigger questions, consult prep | Preparing for a buyer call/consult or writing advisory logic | 03_CLIENT_ADVISORY_OS | Sonnet |
| 03 | Content Studio | YouTube, reels, scripts, teleprompter, hooks | Producing video/reel/script content | 05_CONTENT_MARKETING_ENGINE, 02_POSITIONING_AND_IP | Sonnet |
| 04 | Marketing & Ads Desk | Meta/Google ads, campaign briefs, ad copy, funnels | Building or reviewing paid campaigns and landing assets | 05_CONTENT_MARKETING_ENGINE, 08_OPERATIONS | Sonnet |
| 05 | Agent Recruitment Desk | Market Maker positioning, 3-day workshop, coaching, recruitment | Any Agent Edition recruitment/workshop/coaching work | 04_AGENT_EDITION_OS | Sonnet |
| 06 | Research & Intelligence Desk | Market research, weekly briefs, buyer psychology synthesis | Market/competitor research, weekly brief, buyer-profile work | 06_KNOWLEDGE_VAULT | Sonnet (Opus for deep synthesis) |
| 07 | Operations Desk | CRM/GHL, dashboards, Apps Scripts, scheduled automations | CRM, tracking, scripts, automations, tooling | 08_OPERATIONS | Sonnet (Haiku for cleanup) |

## Model routing (applies to every desk)
- **Haiku** — cleanup, extraction, formatting, deduping, low-risk file checks. Never for strategy.
- **Sonnet** — default execution: writing, SOPs, briefs, scripts, campaign drafts, analysis.
- **Opus** — high-stakes strategy, positioning, complex architecture, deep research synthesis, major decisions.

Each charter states its default and its escalation trigger. A desk recommends switching only when it materially improves quality, cost, or token use — and asks first.

## How the desks talk to each other
Desks do not message each other live. They hand off through files:
- Strategy Office sets priorities → every desk reads them.
- Positioning & IP (02) is the spine → Content, Ads, Advisory, Agent desks all read it.
- Research Desk (06) feeds buyer psychology + market intel → Advisory, Content, Ads.
- Operations Desk (07) owns automations that the other desks' outputs plug into (e.g. weekly content brief, ads report).

When a desk produces something another desk needs, it saves to the correct branch and notes the handoff in that folder's `_INDEX.md` and in `00_COMMAND_CENTER/08_SESSION_LOG.md`.

## Adding or changing a desk
Route through the Strategy Office. New desk or scope change → bump this roster to v1.1, update `_INDEX.md`, log in Session Log. Never edit a charter's scope silently.
