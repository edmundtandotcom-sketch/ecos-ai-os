# CRM Implementation Boundary
Version: v1.0
Status: APPROVED
Date: 2026-07-20

## Operations owns

- GHL custom fields and data types
- workflow triggers, conditions, actions and stops
- pipeline/stage configuration after a Sales-approved movement specification
- integrations, attribution plumbing and operational notifications
- dashboards, tracking, data-quality checks and technical QA
- release, rollback and change records

## Operations does not own

- qualification, closing or follow-up doctrine
- the business meaning of pipeline stages and outcomes
- Strategy Session, RAM, ProDeck or Blueprint delivery
- named contact files in the general AI OS
- live campaign briefs or working creative

## Implementation contract

Every requested change must identify:
1. the governing business rule and owner;
2. the affected live GHL objects;
3. the expected trigger, action, stop and exception behavior;
4. privacy impact;
5. test cases and rollback;
6. the live verification evidence.

Never infer live CRM state from a dated document. Inspect GHL before implementation.

