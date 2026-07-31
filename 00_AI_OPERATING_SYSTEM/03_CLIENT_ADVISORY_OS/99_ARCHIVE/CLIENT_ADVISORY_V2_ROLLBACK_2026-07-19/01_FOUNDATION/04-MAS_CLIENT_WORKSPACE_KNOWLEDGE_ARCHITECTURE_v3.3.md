# 04-MAS_CLIENT_WORKSPACE_KNOWLEDGE_ARCHITECTURE_v3.3

Status: ACTIVE UPGRADED REWRITE
Folder: 02_CLIENT_OS / 00_FOUNDATION
Original Source: Rewritten from v3.2 to match the current simplified Client Edition folder system.
Purpose: Define how MAS Client OS knowledge should be stored, retrieved, updated, reused, and scaled without folder bloat.

## 1. Core Principle

AI does not need more folders.
AI needs consistency, structure, and naming logic.

Humans do not need more complexity.
Humans need clarity, predictability, and simplicity.

The workspace must serve both.

## 2. Current Client Edition Folder Structure

```text
CLIENT_EDITION
├── 00_START_HERE
├── 01_CLIENT_BRAIN
├── 02_CLIENT_OS
├── 03_CONTENT_MARKETING_ENGINE
├── 04_CLIENTS
├── 05_KNOWLEDGE_VAULT
├── 06_OPERATIONS_AND_TRACKING
└── 99_ARCHIVE
```

This replaces older folder maps that separated `Asset Bank`, `Operations`, and `Experiments` as separate top-level folders.

## 3. Folder Roles

| Folder | Purpose | Should Contain | Should Not Contain |
|---|---|---|---|
| 00_START_HERE | Navigation and source-of-truth control | master map, folder rules, source-of-truth index, current priorities | deep strategy docs, campaign drafts |
| 01_CLIENT_BRAIN | AI behaviour and Client Edition principles | AI rules, client principles, decision memory, migration rules | MAS operating manuals, campaign files, ProDeck |
| 02_CLIENT_OS | Advisory operating system | MAS, REI Method, Ascent Stage, ProDeck, Trigger Questions, Client Intelligence | raw ads, active campaign outputs, performance reports |
| 03_CONTENT_MARKETING_ENGINE | Marketing execution | campaign packs, angles, creatives, scripts, landing pages, launch handoffs | deep advisory source files |
| 04_CLIENTS | Actual client files | client assessments, session notes, deliverables, supporting docs | generic frameworks, swipe files |
| 05_KNOWLEDGE_VAULT | Reusable intelligence | research, swipe files, buyer language, objections, case-study learnings | active campaign drafts, private client folders |
| 06_OPERATIONS_AND_TRACKING | Execution and measurement | CRM, dashboards, SOPs, lead quality, ad performance | advisory source-of-truth files |
| 99_ARCHIVE | Historical protection | old versions, superseded files, session logs | active docs |

## 4. Relationship to MAS

MAS is the master advisory operating system for Client Edition.

The workspace is the storage and retrieval environment that protects it.

The workspace must support the four MAS pillars:

1. Attract
2. Diagnose
3. Advise
4. Develop

Every folder and file should make it easier to locate the right knowledge at the right moment in the client journey.

## 5. One-Level Ascent Retrieval Rule

Use **Ascent Stage** as the primary journey label.

Do not create a second property-count ladder as a competing level system.

Retrieval should be possible by:
- Ascent Stage
- Strategic Intent
- Buyer Profile
- Stage / Readiness
- Tier / Priority
- Belief Block
- Campaign Door
- Next Rung
- Next Ascent Trigger
- Property Position as context

Property Position is useful, but it is a context field, not the journey spine.

## 6. Knowledge Promotion Rule

Temporary knowledge starts in active workspaces.
Permanent reusable knowledge gets promoted into Knowledge Vault.

| Input | Starting Home | Permanent Home If Reusable |
|---|---|---|
| New video idea | 03_CONTENT_MARKETING_ENGINE | 05_KNOWLEDGE_VAULT if it becomes reusable |
| Client case study | 04_CLIENTS | 05_KNOWLEDGE_VAULT after sanitising |
| New belief block | Client notes / CRM / campaign project | 05_KNOWLEDGE_VAULT / Belief Block Library |
| New framework | Working doc | 02_CLIENT_OS only if approved as core; otherwise 05_KNOWLEDGE_VAULT |
| Market observation | Research or campaign project | 05_KNOWLEDGE_VAULT / Market Intelligence |
| New follow-up script | Campaign or CRM workflow | 05_KNOWLEDGE_VAULT / Objection or Follow-Up Library |
| Winning creative pattern | Campaign output / tracking | 05_KNOWLEDGE_VAULT / Winning Creative Patterns |
| Performance result | 06_OPERATIONS_AND_TRACKING | 05_KNOWLEDGE_VAULT only after lesson is extracted |

## 7. Campaign vs Foundation Rule

Foundation belongs in Client OS.
Marketing execution belongs in Content Marketing Engine.

| Item | Correct Home |
|---|---|
| MAS / REI / Ascent / ProDeck | 02_CLIENT_OS |
| Client Intelligence system | 02_CLIENT_OS |
| Campaign packs | 03_CONTENT_MARKETING_ENGINE |
| Marketing angles | 03_CONTENT_MARKETING_ENGINE |
| Creative concept library | 03_CONTENT_MARKETING_ENGINE / Shared Marketing IP |
| Image/video/copy outputs | 03_CONTENT_MARKETING_ENGINE / Outputs |
| Swipe ads and market research | 05_KNOWLEDGE_VAULT |
| Ad results and lead quality | 06_OPERATIONS_AND_TRACKING |
| Old versions | 99_ARCHIVE |

## 8. HDB / EC Storage Rule

HDB/EC intelligence should not be stored as broad mass-market content.

If HDB/EC insight is about qualified upgrade-window households, store it under the relevant advisory or campaign layer.

Examples:
- If it affects advisory diagnosis: 02_CLIENT_OS / Client Intelligence.
- If it affects a campaign: 03_CONTENT_MARKETING_ENGINE / Campaign Packs.
- If it is reusable market psychology: 05_KNOWLEDGE_VAULT.
- If it is performance data: 06_OPERATIONS_AND_TRACKING.

## 9. AI Retrieval Priority

When AI retrieves information for Client Edition, follow this order:

1. 00_START_HERE
2. 01_CLIENT_BRAIN
3. 02_CLIENT_OS
4. 05_KNOWLEDGE_VAULT
5. 03_CONTENT_MARKETING_ENGINE
6. 04_CLIENTS, only for actual client work
7. 06_OPERATIONS_AND_TRACKING
8. 99_ARCHIVE
9. General AI knowledge

If a lower-priority file conflicts with a higher-priority source, flag the conflict before using the lower-priority guidance.

## 10. Naming Discipline

Avoid vague names:
- Final
- Final Final
- Latest
- Newest
- Updated
- Real Final

Use names that tell the file's job.

Recommended structure:

```text
SYSTEM_TOPIC_VERSION
```

Examples:

```text
Client_Intelligence_Belief_Block_Library_v2.0.md
CampaignPack_Decoupling_Not_The_Strategy_v1.0.md
CreativeConcept_Library_ClientEdition_v2.0.md
CRM_Lead_Quality_Tracker_v1.0.xlsx
```

## 11. No Folder Bloat Rule

Create a new folder only when:
1. repeated retrieval is needed;
2. it prevents confusion;
3. it supports execution;
4. it has a clear owner or function;
5. it does not duplicate an existing folder.

## 12. Final Rule

The workspace exists to help MAS operate with clarity.

A file is only useful if Coach Edmund, Cindior, future team members, Claude, and ChatGPT can all find it, trust it, and know how to use it.
