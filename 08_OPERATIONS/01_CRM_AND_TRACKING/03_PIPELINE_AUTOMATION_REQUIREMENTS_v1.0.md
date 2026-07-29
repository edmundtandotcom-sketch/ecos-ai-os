# Pipeline Automation Requirements
Version: v1.0
Status: APPROVED GOVERNANCE
Date: 2026-07-20

## Authority

Sales defines stage meaning, entry/exit criteria and valid outcomes in `11_SALES_OS/04_PIPELINE_MOVEMENT`. Operations implements those rules in GHL.

## Minimum automation specification

Each stage or outcome automation must define:
- business trigger;
- entry criteria;
- required field checks;
- action sequence and timing;
- stop conditions;
- manual override;
- owner notification;
- failure handling;
- duplicate/idempotency behavior;
- QA cases and rollback.

## Current architecture constraint

Decision 071 preserves the ten-stage architecture:
`New Lead`, `Responded`, `Booked Call`, `Appointment`, `Strategy Session`, `Close`, `Nurture`, `Unqualified`, `Won`, `Lost`.

These names are decision architecture, not proof of current live configuration. Verify GHL before any change.

Stage and A–D lead grade must remain separate. The Sales outcome model is `Proceed`, `Prepare`, `Nurture`, `No Fit`.

