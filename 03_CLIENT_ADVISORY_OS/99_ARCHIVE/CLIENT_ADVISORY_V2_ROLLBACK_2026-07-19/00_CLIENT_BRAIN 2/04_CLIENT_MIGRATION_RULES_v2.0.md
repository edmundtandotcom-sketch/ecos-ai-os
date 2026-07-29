# 04_CLIENT_MIGRATION_RULES_v2.0

Status: ACTIVE SOURCE OF TRUTH
Folder: 01_CLIENT_BRAIN
Purpose: This file defines how old Client Edition files should be reviewed, rewritten, moved, archived, parked, rejected, or deleted later.

## 1. Core Rule

Do not bulk migrate old files.

Every old file must be reviewed by job, relevance, conflict risk, and correct destination.

Migration is not file moving. Migration is system protection.

## 2. Migration Workflow

For every folder:

1. List every file.
2. Review one file at a time.
3. Identify the file's current job.
4. Decide if the job is still needed.
5. Decide whether the file belongs in its current folder.
6. Check whether it conflicts with v2.0 source-of-truth files.
7. Classify it.
8. Move, rewrite, archive, or park it.
9. Do not delete until the cleanup round is complete and Coach Edmund approves.

## 3. Migration Classifications

Use one of these classifications:

| Classification | Meaning |
|---|---|
| Keep Active | File is current and belongs where it is |
| Rewrite Into v2.0 | Logic is useful but file needs updated structure/name/path |
| Move As-Is | File is still useful and belongs elsewhere |
| Move And Rename | File is useful but needs clearer naming |
| Extract Logic | Only part of the file is useful; extract into a new v2 file |
| Archive | Historical or superseded; keep for reference |
| Park | Not active now but may be useful later |
| Reject | Not useful or conflicts with current direction |
| Delete Later | Candidate for deletion after confirmation |

## 4. Destination Rules

| File Job | Destination |
|---|---|
| AI behaviour / principles / decisions / migration | 01_CLIENT_BRAIN |
| Advisory frameworks / client intelligence / consult logic | 02_CLIENT_OS |
| Campaign packs / angles / creatives / scripts / landing pages | 03_CONTENT_MARKETING_ENGINE |
| Actual client work | 04_CLIENTS |
| Research / swipes / market intelligence / reusable proof | 05_KNOWLEDGE_VAULT |
| CRM / dashboards / SOPs / performance / lead quality | 06_OPERATIONS_AND_TRACKING |
| Superseded or historical files | 99_ARCHIVE |

## 5. Active Format Rule

For source-of-truth operating docs, create both:

- `.md`
- `.docx`

Do not leave native Google Doc versions active unless explicitly requested.

## 6. Folder Cleanup Rule

A folder is clean when:

- every file has a clear job;
- active files are current;
- old files are archived;
- duplicate logic is removed or merged;
- no campaign drafts sit inside brain/OS folders;
- no advisory foundation is hidden inside marketing folders;
- a human can understand the folder within 30 seconds.

## 7. Old Logic To Archive Or Ignore Unless Reapproved

Archive or ignore:

- old source-of-truth indexes that conflict with v2.0;
- old Client Brain files that treat Client Brain as the whole business;
- old Google Doc operating files when raw `.md` + `.docx` are required;
- old 5-pack/6-pack campaign matrices if contradicted by new campaign-pack direction;
- old “decoupling retired” logic where current v2 direction treats decoupling as campaign-worthy;
- broad HDB-first logic as core Client Edition content;
- old installation instructions;
- old migration trackers that do not reflect current folders.

## 8. HDB/EC Migration Guardrail

When migrating old HDB/EC or HECO files, preserve the useful strategic logic but prevent audience dilution.

Keep:

- MOP/TOP timing logic;
- two-name structure logic;
- 1-to-2 private property pathway;
- upgrade-window planning;
- capital/equity/holding-power assessment;
- advisory qualification.

Avoid:

- broad HDB-owner messaging;
- generic HDB-upgrader content;
- price-only upgrade logic;
- non-MAS-fit mass-market targeting;
- treating every HDB/EC owner as a campaign lead.

## 9. Migration Decision Log Rule

For major cleanup decisions, update:

- 01_CLIENT_BRAIN / 03_CLIENT_DECISION_MEMORY_v2.0

For folder-specific cleanup, keep notes in the working conversation or folder audit summary until a proper tracker is created under Operations & Tracking.

## 10. Current Cleanup Sequence

Use this order:

1. 00_START_HERE
2. 01_CLIENT_BRAIN
3. 02_CLIENT_OS / 00_FOUNDATION
4. 02_CLIENT_OS / 01_CLIENT_INTELLIGENCE
5. 03_CONTENT_MARKETING_ENGINE
6. 05_KNOWLEDGE_VAULT
7. 06_OPERATIONS_AND_TRACKING
8. 99_ARCHIVE

## 11. Final Rule

Move only what strengthens the upgraded Client Edition.

When unsure, archive first. Do not delete casually.
