# 08_DISCOVERY_AND_DIAGNOSIS — INDEX
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: Trigger Question Bank v2.0; Belief-Shift Sequences v2.0; Buyer Segment Library v2.0; Readiness Stage Model v2.0; Traps Language Bank v2.1; Diagnosis Call System v2.0

## Purpose
The discovery + diagnosis intelligence layer: the question library architecture, archetype/readiness routing, client-language pointer, and diagnostic-model routing that feed P1–P2 of the consultation flow. Pointer-first; no master content duplicated.

## Subfolders
| Folder | One-liner |
|---|---|
| `QUESTION_LIBRARY\` | Per-question metadata schema + 8-category routing onto the trigger banks |
| `CLIENT_ARCHETYPES\` | Routing to Buyer Segment + Readiness + Traps; archetype coverage-gap note |
| `CLIENT_LANGUAGE\` | Registry pointer to E: Client Language Vault (PII — not copied) |
| `DIAGNOSTIC_MODELS\` | Stub routing to Ascent / REI / Readiness / Tiering / belief-block models |

## Files
| File | One-liner |
|---|---|
| `DISCOVERY_REGISTRY.csv` | Index of discovery assets (questions, models, archetypes, language) |
| `DISCOVERY_REGISTRY_SPEC.md` | Column definitions |

READS FROM: `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\`; E: Consult Intelligence OS (reference).
FEEDS INTO: branch 07 (DISCOVERY/DIAGNOSIS stages); branch 11 (objections originate in problem/consequence questions).
