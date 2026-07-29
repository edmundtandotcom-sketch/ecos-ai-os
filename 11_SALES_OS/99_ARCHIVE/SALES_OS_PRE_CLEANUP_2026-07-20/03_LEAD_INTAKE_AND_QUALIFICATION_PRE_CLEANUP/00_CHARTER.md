# CHARTER — 03_LEAD_INTAKE_AND_QUALIFICATION
Version: v0.1
Status: STUB
Date: 2026-07-11
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md`; `00_AI_OPERATING_SYSTEM\08_OPERATIONS\06_CONTACT_MASTER\` (label dictionary v1.2)

---

## Purpose

Governs how a raw lead becomes a graded, qualified lead ready for appointment setting: the A–D lead-grade criteria, source rules, and disqualification logic.

## When To Use

When someone asks "how do we grade a lead" or "what makes a lead qualified" — the answer already exists in the CRM SOP; this branch is where a sales-specific usage layer (e.g. grading examples, edge cases) would go if built.

## What Exists Elsewhere Already

- Lead grading and pipeline/lead-quality system (APPROVED MASTER): `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` — this is the authoritative A–D grading logic. Do not recreate it here.
- Contact labelling / dictionary: `00_AI_OPERATING_SYSTEM\08_OPERATIONS\06_CONTACT_MASTER\CONTACT_LABEL_DICTIONARY_v1.2` (APPROVED MASTER)
- Known definitional conflict: "qualified" = pipeline stage vs A–D grade (SC-03, `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`)

## What Triggers Build-Out

SC-03 is resolved (Edmund confirms the two-field model) and `15_CRM_AND_PIPELINE\CRM_FIELDS.md` exists to anchor grading fields against — build the usage layer against a settled field model, not before.
