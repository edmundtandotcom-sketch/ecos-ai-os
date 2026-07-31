# CHARTER — 26_EXPERIMENTS
Version: v0.1
Status: STUB
Date: 2026-07-11
Supersedes: none
Sources: `10_MARKETING_OS\09_EXPERIMENTS\` (sibling pattern); SALES_OS_BUILD_SPEC_v1 mandate §25/§26

---

## Purpose

Holds the sales-side experiment registry: hypotheses about what changes conversion, sample design, and results — mirroring the Marketing OS experiment-lifecycle pattern for sales-specific tests (e.g. closing-script variants, follow-up cadence tests).

## When To Use

Before running any deliberate test on live sales process — log the hypothesis here first, run it, record the result. Not for informal one-off tries.

## What Exists Elsewhere Already

- Sibling pattern to mirror: `10_MARKETING_OS\09_EXPERIMENTS\` (backlog → active → completed → learnings lifecycle)
- Registry structure: `EXPERIMENT_REGISTRY.csv` + `_REGISTRY_SPEC.md` (both in this folder, built per mandate columns: ID/hypothesis/current/variant/client-type/sample/metric/risk/dates/result/confidence/recommendation/system-update)

The registry is header-only — no sales experiment has run yet.

## What Triggers Build-Out

The deep-build branches (07, 08, 11, 12, 13, 15) are stable enough that a controlled variant test on top of them is meaningful (testing against a moving baseline produces noise, not signal).
