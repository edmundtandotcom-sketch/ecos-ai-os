# 01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM

Version: v2.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none (copied as-is; current master at time of migration)
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\06_OPERATIONS_AND_TRACKING\01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md`

Folder: 01_CRM_AND_TRACKING (AI OS) — legacy folder: 06_OPERATIONS_AND_TRACKING
Purpose: Define how CRM, leads, booking status, pipeline and lead quality should be tracked.

## 1. Core Principle

One contact. One record. One journey. One truth.

The CRM should not be a graveyard of names. It must show where each person came from, what they are trying to solve, whether they are qualified, what happened next, and what follow-up is required.

## 2. System of Record

| Area | System of record |
|---|---|
| Contact and pipeline | GHL |
| Ad / creative performance | REI Creative Intelligence master sheet and dashboard |
| Source documents / client files | Google Drive |
| Campaign strategy and assets | Content Marketing Engine |
| Reusable learning | Knowledge Vault |

## 3. Minimum Lead Fields

Every serious lead should eventually have:

- name;
- phone / WhatsApp;
- email if available;
- source channel;
- campaign / asset / offer source;
- campaign pack if known;
- Ascent Stage;
- property context;
- buyer profile;
- main trigger;
- belief block / objection;
- lead quality grade;
- booking status;
- last contact date;
- next follow-up action;
- owner.

## 4. Pipeline Rule

Keep the pipeline simple.

Recommended stages:

1. New Lead
2. Contacted
3. Appointment Set
4. Consult Done
5. Decision Pending
6. Won / Closed
7. Nurture

Do not create too many micro-stages. Use tags or fields for detail instead.

## 5. Lead Quality Grades

Use simple grades first:

| Grade | Meaning | Action |
|---|---|---|
| A | Strong fit, serious timing, clear capacity, advisory-ready | Prioritise quickly |
| B | Real problem but timing/capacity unclear | Nurture and qualify |
| C | Weak fit, low urgency, low clarity or poor capacity | Low-touch nurture |
| D / Exclude | Not relevant, duplicate, no contact method, internal, vendor, spam | Archive / exclude |

## 6. Booking Status

Track these clearly:

- not contacted;
- contacted but no response;
- replied but not booked;
- booking link sent;
- booked;
- no-show;
- completed;
- reschedule required;
- closed / won;
- nurture.

## 7. Contact Cleanup Rule

Contact cleanup sheets are operational references, not permanent active masters.

Keep active only when they are being reviewed or used for import. Once completed, move the final import result and decision summary into Operations. Archive intermediate workbooks and payload JSON files.

## 8. AI Usage Rule

AI may help summarise leads, classify quality, draft follow-up, and flag missing fields.

AI must not import, delete, merge, or approve contacts without explicit human confirmation.
