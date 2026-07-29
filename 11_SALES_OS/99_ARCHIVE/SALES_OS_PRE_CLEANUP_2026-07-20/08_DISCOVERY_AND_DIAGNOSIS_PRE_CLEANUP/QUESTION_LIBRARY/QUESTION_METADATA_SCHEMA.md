# QUESTION_METADATA_SCHEMA
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: Advisory Trigger Question Bank v2.0; Belief-Shift Question Sequences v2.0; Diagnosis Call System v2.0; Decision Psychology v2.1

## Purpose
Defines the **per-question record schema** for the discovery/diagnosis question library. The library does not re-author the Trigger Question Bank — it **wraps each existing question in operating metadata** so questions can be routed, sequenced, and evidence-tracked. Question *text* stays in the masters; this schema adds the operating layer around a pointer. `[T5]`

## Per-question fields
| Field | Definition | Example / controlled values |
|---|---|---|
| `question_id` | Stable ID | Q-SIT-01 (category prefix) |
| `question_text_ref` | Pointer to master + section (not a copy) | Trigger Q Bank v2.0 §2 |
| `category` | One of the 8 mandate categories | situation · motivation · problem · consequence · financial · decision · suitability · commitment |
| `purpose` | What the question is for | free text |
| `client_type` | Segment(s) it fits | FCC / DINK / FHA / DFP / RM / HECO-Q / FAP / any |
| `stage` | Where in the flow it fires | P1-diagnosis / P3-session / P4-decision |
| `listen_for` | The real signal under the answer | free text |
| `follow_ups` | Next question IDs | Q-xxx list |
| `warning_signs` | Answers that signal disqualify / stall risk | free text |
| `common_mistake` | How advisors misuse it | free text |
| `strategy_impact` | What the answer changes in the roadmap | free text |
| `evidence_status` | Backing tier | T3 (field-observed in consults) / T5 (doctrine) / T7 (proposed) |

## Rules
1. **Pointer-first:** `question_text_ref` cites the master; never paste the question body into the registry. `[T5]`
2. **Self-realisation, not interrogation** (Trigger Q Bank §1) — metadata must preserve intent. `[T5]`
3. `evidence_status` defaults to **T5** for doctrine questions; upgrade to **T3** only when a coded transcript shows the question working in the field.
