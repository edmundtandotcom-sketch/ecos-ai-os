# PIPELINE SUMMARY — SALES OS
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: SALES_OS_BUILD_SPEC_v1; SC-01 (`CONTRADICTION_REGISTER.md`)

---

## Placeholder — Data Blocked

This file will hold the live pipeline snapshot (stage counts, conversion rates, stalled-lead volume) once two prerequisites clear:

1. **Live GHL read-only audit** (Decision 051.3) — needed to establish which of the four conflicting pipeline definitions (SC-01) is the reporting truth.
2. **`15_CRM_AND_PIPELINE\PIPELINE_ARCHITECTURE.md`** — the reconciled pipeline recommendation that this summary would report against.

Until both exist, any pipeline numbers quoted here would be built on an unreconciled architecture and would misrepresent conversion at every stage boundary. No numbers are asserted in this file for that reason.

## What Will Populate This File

- Stage-by-stage lead counts (per the reconciled architecture)
- Conversion rate per stage transition
- Stalled / no-action lead volume
- Source attribution split (once `CRM_FIELDS.md` gap table is built)
- Evidence tier on every figure — no unlabelled numbers

READS FROM: `15_CRM_AND_PIPELINE\PIPELINE_ARCHITECTURE.md` (once built), live GHL audit report.
FEEDS INTO: `SALES_OS_STATUS.md`, `22_SALES_ANALYTICS\` (once built out).
