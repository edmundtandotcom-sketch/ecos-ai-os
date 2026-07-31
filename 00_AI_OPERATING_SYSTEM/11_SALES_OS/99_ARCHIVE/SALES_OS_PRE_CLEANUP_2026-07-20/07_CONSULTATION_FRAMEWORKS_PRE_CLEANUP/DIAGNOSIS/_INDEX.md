# DIAGNOSIS — routing
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: Diagnosis Call System v2.0 §5–§6 (Decision-Maker rule, Tiering); Buyer Segment Library v2.0; Readiness Stage Model v2.0; Decision Psychology v2.1 (belief blocks)

## Purpose
Routes the classification + tiering step of P1: Ascent Stage, buyer segment, decision-maker map, belief block, Tier. `[T5]`

## Routing
| Need | Go to |
|---|---|
| Ascent Stage (A0–A2 — A3/A4 retired per Decision 063) | Diagnosis Call v2.0 §3 Phase 5 |
| Buyer segment / archetype | `08_DISCOVERY_AND_DIAGNOSIS\CLIENT_ARCHETYPES\` |
| Belief block (RB-01..RB-18) | Decision Psychology v2.1 §5, §5A |
| Tier 1/2/3/Excluded criteria | Diagnosis Call v2.0 §6 |
| Decision-maker rule | Diagnosis Call v2.0 §5 |

## Must produce
The Diagnosis Record (see MASTER_CONSULTATION_FLOW P1). Written to CRM + DISCOVERY_REGISTRY.

READS FROM: DISCOVERY. FEEDS INTO: RECOMMENDATION (Tier-1 only) or branch 13 (nurture).
