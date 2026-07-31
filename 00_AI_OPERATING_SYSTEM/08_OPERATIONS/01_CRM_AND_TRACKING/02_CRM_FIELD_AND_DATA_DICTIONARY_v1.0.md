# CRM Field and Data Dictionary
Version: v1.0
Status: APPROVED GOVERNANCE
Date: 2026-07-20

## Rule

GHL is the authoritative live field registry. This document governs how fields are proposed and maintained; it does not claim a current field inventory.

## Required definition

For every governed field record:
- display name and internal key;
- data type and permitted values;
- business owner and technical owner;
- source system;
- creation/update rule;
- whether it contains PII or sensitive evidence;
- downstream workflows/reports;
- retention and deletion rule;
- last live verification date.

## Controls

- Reuse an existing verified field before creating another.
- Keep pipeline stage and lead grade as separate fields.
- Keep outcome codes controlled and consistent with Sales.
- Do not place transcript excerpts or free-form sensitive notes in fields designed for reporting.
- Mask or aggregate PII in general dashboards.
- A field change requires impact review for workflows, forms, imports and reporting.

