# CLAUDE.md — SALES OS FRONT DOOR
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM\CLAUDE.md` v4.1 (constitution); Decision 051 (`00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\04_DECISION_MEMORY.md`); SALES_OS_BUILD_SPEC_v1 (Fable, 2026-07-11)

---

## 0. What This System Is

The Sales OS is the **operating layer for lead-to-client conversion**: lead intake through consultation, objection handling, closing, follow-up, CRM/pipeline, onboarding, retention, and referrals — for Coach Edmund Tan, Cindior Ho, and Singapore Real Estate Insider (REI).

It is **not a second brain.** It holds no consultation-method, positioning, or proof masters of its own. Those live in `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\`, `02_POSITIONING_AND_IP\`, and `07_BRAND_AND_PROOF_BANK\`. Sales OS files **point** to those masters by full path and add only the sales-usage layer: registries, records, pipeline mechanics, gap notes, conversation intelligence.

**Nested under `00_AI_OPERATING_SYSTEM\` as a department** (`11_SALES_OS\`) (2026-07-13 spring-clean). Originally built at root level, sibling to Marketing OS, per Decision 051. Edmund's 2026-07-13 spring-clean ruling moved both OS layers inside the AI OS, closing governance conflict C14 — do not re-litigate; track under `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`.

---

## 1. Read This First, Every Session

1. `00_AI_OPERATING_SYSTEM\CLAUDE.md` — the constitution (governs everything below)
2. `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\04_DECISION_MEMORY.md` — esp. Decision 051 (this system's build rulings)
3. `00_COMMAND_CENTER\SALES_OS_STATUS.md` — what's built, what's stub
4. `00_COMMAND_CENTER\CURRENT_PRIORITIES.md` — what to protect focus around
5. `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` — known conflicts (SC-01..06) — never silently resolve
6. `00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md` — where each sales function's master actually lives

---

## 2. Source-Of-Truth Hierarchy (higher wins)

1. `00_AI_OPERATING_SYSTEM\CLAUDE.md` — the constitution
2. `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\` — the AI OS brain
3. `03_CLIENT_ADVISORY_OS\` — MAS 7-layer stack, Diagnosis Call, Strategy Session, Objections, ProDeck, Trigger Questions
4. `02_POSITIONING_AND_IP\` — Second Property Ladder™ spine
5. `08_OPERATIONS\` — CRM SOPs, live sync script, Contact Master
6. **This Sales OS layer** — registries, pipeline architecture, conversation intelligence, templates
7. `E:\Zoom Consults - Processed\_CONSULT_INTELLIGENCE_OS\` — approved consult intelligence (extend, never duplicate)
8. Old read-only folders (historical reference)

If a Sales OS file conflicts with any AI OS master, the AI OS wins and the Sales OS file is corrected. Never silently merge — log it in `CONTRADICTION_REGISTER.md`. Full map: `00_COMMAND_CENTER\SOURCE_OF_TRUTH_MAP.md`.

---

## 3. Build Depth (Decision 051.4 — phased core)

- **Deep-build (real content):** `00_COMMAND_CENTER`, `07_CONSULTATION_FRAMEWORKS`, `08_DISCOVERY_AND_DIAGNOSIS`, `11_OBJECTION_INTELLIGENCE`, `12_CLOSING_AND_DECISION`, `13_FOLLOW_UP_AND_NURTURE`, `15_CRM_AND_PIPELINE`, `21_CONVERSATION_INTELLIGENCE`, `28_TEMPLATES`, `29_CHANGE_LOG`.
- **Stub (folder + `_INDEX.md` + `00_CHARTER.md`, Status: STUB):** every other branch. A stub states purpose, when to use, what exists elsewhere already, and what triggers build-out. Do not build past a stub without a trigger.
- Registries are `.csv` with a companion `_REGISTRY_SPEC.md`.

---

## 4. Operating Principles

1. Markdown only; registries are `.csv`. No `.docx`.
2. Every `.md` carries the header block: Title, Version, Status, Date, Supersedes, Sources.
3. **Everything is Status: DRAFT or STUB.** Only Edmund promotes to APPROVED MASTER.
4. Every folder has a `_INDEX.md`.
5. Max folder depth 4 below `11_SALES_OS\`.
6. **No PII, ever.** No client names, phones, emails, addresses, NRIC, or exact consult quotes attributable to a named client. Anonymise: "Client couple, HDB upgrader, 2022."
7. Evidence discipline: every claim carries a 7-tier evidence label (T1 commercial → T7 hypothesis). The 376-objection frequency table is Tier 3.
8. Business language: "advisors/coaches," never "agents." Second Property Ladder™ positioning. "Move" = the public word everywhere (Decision 055, supersedes the Step ruling); booked session = Next Move Strategy Session™. No artificial urgency/scarcity. The 4 sanctioned closes: Proceed / Prepare / Nurture / No Fit.
9. "PWS" is not a live framework — it was absorbed into MAS → REI Method → RAM. Do not resurrect it as a standalone system.
10. Never write outside `11_SALES_OS\`. All other folders are read-only — pull from them, never edit.
11. Pointer-first: where an APPROVED MASTER exists elsewhere, point to it by full path. Never duplicate master content.

---

## 5. Routing Table

| Task is about… | Folder |
|---|---|
| System status, priorities, decisions, conflicts, source-of-truth map | `00_COMMAND_CENTER\` |
| Business/sales strategy context | `01_BUSINESS_AND_SALES_STRATEGY\` |
| Marketing lead handoff rules | `02_MARKETING_TO_SALES_HANDOFF\` |
| Lead intake, grading, qualification | `03_LEAD_INTAKE_AND_QUALIFICATION\` |
| Booking / appointment setting | `04_APPOINTMENT_SETTING\` |
| Pre-consult prep | `05_PRE_CONSULTATION\` |
| Advisor prep before a consult | `06_ADVISOR_PREPARATION\` |
| The governed consultation flow (Diagnosis → Strategy → ProDeck) | `07_CONSULTATION_FRAMEWORKS\` |
| Discovery questions, archetypes | `08_DISCOVERY_AND_DIAGNOSIS\` |
| Financial / property analysis, RAM | `09_FINANCIAL_AND_PROPERTY_ANALYSIS\` |
| Recommendation & presentation delivery | `10_RECOMMENDATION_AND_PRESENTATION\` |
| Objection handling system | `11_OBJECTION_INTELLIGENCE\` |
| Closing frameworks, outcome/lost-reason codes | `12_CLOSING_AND_DECISION\` |
| Follow-up and nurture | `13_FOLLOW_UP_AND_NURTURE\` |
| CRM & pipeline architecture | `15_CRM_AND_PIPELINE\` |
| Client onboarding | `16_CLIENT_ONBOARDING\` |
| Transaction experience | `17_TRANSACTION_EXPERIENCE\` |
| Retention & portfolio reviews | `18_RETENTION_AND_PORTFOLIO_REVIEWS\` |
| Reviews, testimonials, case studies | `19_REVIEWS_TESTIMONIALS_AND_CASE_STUDIES\` |
| Referrals & advocacy | `20_REFERRALS_AND_ADVOCACY\` |
| Consultation-transcript intelligence pipeline | `21_CONVERSATION_INTELLIGENCE\` |
| Sales analytics & reporting | `22_SALES_ANALYTICS\` |
| Sales enablement content | `23_SALES_ENABLEMENT\` |
| Training & certification | `24_TRAINING_AND_CERTIFICATION\` |
| Compliance & suitability | `25_COMPLIANCE_AND_SUITABILITY\` |
| Experiments | `26_EXPERIMENTS\` |
| Sales learnings | `27_SALES_LEARNINGS\` |
| Reusable templates | `28_TEMPLATES\` |
| Change control | `29_CHANGE_LOG\` |
| Superseded / archived material | `99_ARCHIVE\` |

---

## 6. Conflict Detected — Response Format

When a task touches an unresolved contradiction (SC-01..06 or a new one), stop and surface it — do not pick a side silently:

```
CONFLICT DETECTED — [SC-xx or short name]
Current position:     [what one authoritative source says + path]
Conflicting position: [what the other says + path]
Evidence:             [tier + what data exists, if any]
Consequence:          [what breaks if we guess wrong]
Recommendation:       [my pick + one-line reason]
Required decision:    [the exact call Edmund must make]
```

Log every new conflict in `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` and, if it forces an owner call, in `DECISIONS_REQUIRED.md`.
