# CRM QA and Reporting
Version: v1.0
Status: APPROVED GOVERNANCE
Date: 2026-07-20

## Release gates

Before a CRM change is released:
- confirm governing owner and approved specification;
- export or record rollback state;
- test positive, negative, duplicate and exception paths;
- confirm no unintended messages or stage moves;
- confirm privacy and access controls;
- compare expected versus actual records;
- capture live verification date and responsible reviewer.

## Reporting rules

- Distinguish snapshots from current live truth.
- Every metric must name source, definition, time window and refresh time.
- Do not mix people, opportunities, appointments and sessions as one denominator.
- Label manual adjustments.
- Do not expose names, phone numbers, emails or transcript content in general AI OS reports.
- Treat historical counts as historical evidence, never as current status.

Failures must be routed to a named operational queue and resolved or explicitly accepted before closure.

