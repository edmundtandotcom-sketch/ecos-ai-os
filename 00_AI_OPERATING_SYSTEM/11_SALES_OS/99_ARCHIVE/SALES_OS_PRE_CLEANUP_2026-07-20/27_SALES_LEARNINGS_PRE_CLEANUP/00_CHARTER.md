# CHARTER — 27_SALES_LEARNINGS
Version: v0.1
Status: STUB
Date: 2026-07-11
Supersedes: none
Sources: `10_MARKETING_OS\11_WINNERS_AND_LEARNINGS\` (sibling pattern); SALES_OS_BUILD_SPEC_v1 mandate §25/§26

---

## Purpose

Holds the sales-side learning registry: durable insights extracted from consults, experiments, and CRM data, tracked through a 12-state knowledge lifecycle so a learning's current standing is never ambiguous.

## When To Use

When a real insight surfaces (from a consult pattern, a concluded experiment, or a contradiction resolution) that should outlive the session it was found in.

## What Exists Elsewhere Already

- Sibling pattern to mirror: `10_MARKETING_OS\11_WINNERS_AND_LEARNINGS\LEARNING_REGISTRY.csv`
- Registry structure: `LEARNING_REGISTRY.csv` + `_REGISTRY_SPEC.md` (both in this folder, columns per mandate: ID/insight/status-per-12-state-lifecycle/evidence-tier/context/source/dates)
- Raw material this registry will eventually draw from: `21_CONVERSATION_INTELLIGENCE\` (consult patterns), `26_EXPERIMENTS\` (concluded tests), `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` (resolved contradictions)

The registry is header-only — no learning has been logged yet.

## What Triggers Build-Out

The first experiment in `26_EXPERIMENTS\` concludes, or the `21_CONVERSATION_INTELLIGENCE\` pilot produces a pattern worth tracking as a durable insight.
