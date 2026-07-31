# CHARTER — 02_MARKETING_TO_SALES_HANDOFF
Version: v0.1
Status: STUB
Date: 2026-07-11
Supersedes: none
Sources: `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md`; `10_MARKETING_OS\02_CUSTOMER_INTELLIGENCE\OBJECTIONS_MAP.md`; `10_MARKETING_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`, `DECISIONS_REQUIRED.md`

---

## Purpose

Governs the moment a lead crosses from Marketing OS ownership into Sales OS ownership: what data must travel with it, what "qualified" means at handoff, and where the two systems' definitions currently disagree.

## When To Use

When defining what fields/context a lead must carry at handoff, or when a sales-side report needs to cite a marketing-defined KPI (CTR, CPL, lead source) without redefining it.

## What Exists Elsewhere Already

- KPI definitions (source of truth for marketing metrics): `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md`
- Objection intelligence gathered pre-sale: `10_MARKETING_OS\02_CUSTOMER_INTELLIGENCE\OBJECTIONS_MAP.md`
- Data source inventory: `10_MARKETING_OS\10_PERFORMANCE\DATA_SOURCES.md`
- Cross-system conflicts already logged: `10_MARKETING_OS\00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`, `DECISIONS_REQUIRED.md`

This branch does not redefine any of the above — it points to them and, once built, states the handoff contract only.

## What Triggers Build-Out

`15_CRM_AND_PIPELINE\PIPELINE_ARCHITECTURE.md` lands (resolves SC-01) and the reconciled pipeline has a defined intake stage that Marketing OS can hand into — build the handoff contract against that stage, not before.
