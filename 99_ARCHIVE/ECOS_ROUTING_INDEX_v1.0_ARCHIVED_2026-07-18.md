# _INDEX — 01_E.C.O.S
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none
Sources: AI OS REBUILD SPEC v1.0 B2

## Purpose
The AI department roster. Defines seven specialist Claude "desks" — each a fixed-scope persona with a reading list and a ready-to-paste standing prompt. Edmund pastes a desk's standing prompt to run that specialist. This branch tells the ecosystem *who does what and what they read*.

## Files
| File | Description |
|------|-------------|
| `00_TEAM_ROSTER.md` | Master table of all 7 desks: mission, when to invoke, branch read, model routing. Universal rule (read Command Center first) + how desks hand off via files. |
| `01_STRATEGY_OFFICE.md` | Desk 01 — COO/strategist. Decisions, priorities, challenge weak ideas. Opus. |
| `02_CLIENT_ADVISORY_DESK.md` | Desk 02 — MAS diagnosis, Strategic Intent, trigger questions, consult prep. Reads 03_CLIENT_ADVISORY_OS. Sonnet. |
| `03_CONTENT_STUDIO.md` | Desk 03 — YouTube/reels/scripts via Reel Script Rulebook. Reads 05_CONTENT_MARKETING_ENGINE + 02_POSITIONING_AND_IP. Sonnet. |
| `04_MARKETING_ADS_DESK.md` | Desk 04 — Meta/Google ads, campaign briefs, copy. Platform-verification rule applies. Reads 05_CONTENT + 08_OPERATIONS. Sonnet. |
| `05_AGENT_RECRUITMENT_DESK.md` | Desk 05 — Market Maker recruitment, 3-day workshop, coaching. Reads 04_AGENT_EDITION_OS. Sonnet. |
| `06_RESEARCH_INTELLIGENCE_DESK.md` | Desk 06 — market research, weekly briefs, buyer psychology. Reads 06_KNOWLEDGE_VAULT. Sonnet/Opus. |
| `07_OPERATIONS_DESK.md` | Desk 07 — CRM/GHL, dashboards, Apps Scripts, automations. Reads 08_OPERATIONS. Sonnet/Haiku. |
| `08_CLAUDE_SKILLS_MAP.md` | Which installed Claude skills + workspace commands (/desk, /new-idea, /session-close, /os-audit) each desk uses. |

## READS FROM (which branches feed this one)
- `00_COMMAND_CENTER` — constitution, priorities, positioning, decisions, evolution protocol. Every desk reads it first; the roster's universal rule points here.

## FEEDS INTO (which branches consume this one)
- **All branches, indirectly.** This is the routing layer. Each charter directs a desk to read and write in a specific downstream branch:
  - Desk 02 → `03_CLIENT_ADVISORY_OS`
  - Desk 03 → `05_CONTENT_MARKETING_ENGINE`, `02_POSITIONING_AND_IP`
  - Desk 04 → `05_CONTENT_MARKETING_ENGINE`, `08_OPERATIONS`, `07_BRAND_AND_PROOF_BANK`
  - Desk 05 → `04_AGENT_EDITION_OS`
  - Desk 06 → `06_KNOWLEDGE_VAULT` → feeds Desks 02/03/04
  - Desk 07 → `08_OPERATIONS`
- `00_COMMAND_CENTER` — the constitution's AI Team routing rule points here to select a desk.

## Pending Edmund approval (CANDIDATE)
None. All roster and charter files are APPROVED MASTER v1.0. Scope changes route through the Strategy Office (Desk 01) and bump the roster to v1.1.

## Notes
- Model routing per desk follows the constitution: Haiku (cleanup) / Sonnet (default) / Opus (high-stakes).
- Automations referenced by Desks 04/06/07 are built by B7 in `08_OPERATIONS/03_AUTOMATIONS/`; charters reference them by path.
