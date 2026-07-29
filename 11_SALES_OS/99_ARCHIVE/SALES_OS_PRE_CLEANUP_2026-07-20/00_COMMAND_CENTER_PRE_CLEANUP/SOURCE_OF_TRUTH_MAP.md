# SOURCE OF TRUTH MAP — SALES OS
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: SALES_OS_BUILD_SPEC_v1 AUTHORITATIVE SOURCES list (scouted 2026-07-11); paths verified live on disk 2026-07-11

---

Purpose: per sales function, the one authoritative path to trust, its status, and what the Sales OS adds on top. Pointer-first — this OS never duplicates the content below.

| Sales function | Authoritative path | Status | What Sales OS adds |
|---|---|---|---|
| Governing constitution | `00_AI_OPERATING_SYSTEM\CLAUDE.md` (v4.1) | APPROVED MASTER | Nothing — binds this whole OS |
| Consultation method (MAS 7-layer) | `00_AI_OPERATING_SYSTEM\03_CLIENT_ADVISORY_OS\01_FOUNDATION\01_MAS_ADVISORY_FOUNDATION_v4.0.md` | APPROVED MASTER | `07_CONSULTATION_FRAMEWORKS\` reconciles this + Diagnosis Call + Strategy Session + ProDeck into one governed flow |
| Discovery call (6 phases) | `...\03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\01_DIAGNOSIS_CALL_SYSTEM_v2.0.md` | APPROVED MASTER | `08_DISCOVERY_AND_DIAGNOSIS\` question-library architecture pointing at this |
| Closing (4 sanctioned closes) | `...\03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\02_STRATEGY_SESSION_CONVERSATION_SYSTEM_v2.0.md` | APPROVED MASTER | `12_CLOSING_AND_DECISION\` maps closes to structures + controlled outcome/lost-reason vocab |
| Objections (RB-01–18, 376/166) | `...\03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\03_DECISION_PSYCHOLOGY_AND_BELIEF_RESOLUTION_v2.1.md` | APPROVED MASTER (evidence Tier 3) | `11_OBJECTION_INTELLIGENCE\` objection-record schema + routing to RB blocks + E: MASTER_OBJECTION_BANK |
| Decision gate | `...\03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\04_RISK_ASSURANCE_AND_NEXT_ACTION_SYSTEM_v2.1.md` | APPROVED MASTER | `12_CLOSING_AND_DECISION\` |
| Buyer archetypes | `...\03_CLIENT_ADVISORY_OS\02_CLIENT_INTELLIGENCE\01_BUYER_SEGMENT_LIBRARY_v2.0.md` | APPROVED MASTER | `08_DISCOVERY_AND_DIAGNOSIS\` archetype pointer file |
| Readiness stages | `...\03_CLIENT_ADVISORY_OS\02_CLIENT_INTELLIGENCE\02_READINESS_STAGE_MODEL_v2.0.md` | APPROVED MASTER | `08_DISCOVERY_AND_DIAGNOSIS\` |
| Traps / private-thoughts language bank | `...\03_CLIENT_ADVISORY_OS\02_CLIENT_INTELLIGENCE\03_TRAPS_PRIVATE_THOUGHTS_LANGUAGE_BANK_v2.1.md` | APPROVED MASTER | `08_DISCOVERY_AND_DIAGNOSIS\`, `11_OBJECTION_INTELLIGENCE\` |
| Trigger questions | `...\03_CLIENT_ADVISORY_OS\04_TRIGGER_QUESTIONS\01_ADVISORY_TRIGGER_QUESTION_BANK_v2.0.md`, `02_BELIEF_SHIFT_QUESTION_SEQUENCES_v2.0.md` | APPROVED MASTER | `08_DISCOVERY_AND_DIAGNOSIS\` per-question metadata schema |
| ProDeck consult delivery | `...\03_CLIENT_ADVISORY_OS\05_PRODECK\01_PRODECK_CONSULT_DELIVERY_SYSTEM_v2.0.md` (+02, 03) | APPROVED MASTER | `07_CONSULTATION_FRAMEWORKS\`, `10_RECOMMENDATION_AND_PRESENTATION\` (stub) |
| CRM SOPs (pipeline, dashboard, follow-up, nurture) | `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md`, `02_DASHBOARD_AD_TRACKING_SYSTEM_v2.0.md`, `03_REPORTING_FOLLOW_UP_AND_HANDOFF_RULES_v2.0.md`, `04_NURTURE_REACTIVATION_AND_DATABASE_MOVEMENT_SYSTEM_v2.0.md` | APPROVED MASTER | `03_LEAD_INTAKE_AND_QUALIFICATION\` (stub) points to lead grading; `13_FOLLOW_UP_AND_NURTURE\`; `15_CRM_AND_PIPELINE\` reconciles against live GHL (SC-01) |
| Live CRM sync code | `00_AI_OPERATING_SYSTEM\08_OPERATIONS\02_SCRIPTS\REI_AppsScript_ACTIVE_v8.43.gs` | ACTIVE (production code) | `15_CRM_AND_PIPELINE\` reads field/status logic from this as live-truth input |
| Contact master / GHL import | `00_AI_OPERATING_SYSTEM\08_OPERATIONS\06_CONTACT_MASTER\` (7,314-row import ready; label dictionary v1.2; import plan v1.1) | READY, import NOT executed | `15_CRM_AND_PIPELINE\` references the import plan; does not instruct execution (separate pending decision) |
| Case studies | `00_AI_OPERATING_SYSTEM\02_POSITIONING_AND_IP\Case_Study_Bank_7_Proof_Categories.md` | CANDIDATE | `19_REVIEWS_TESTIMONIALS_AND_CASE_STUDIES\` (stub) points here |
| Proof bank | `00_AI_OPERATING_SYSTEM\07_BRAND_AND_PROOF_BANK\08_PROOF_BANK\` | REGISTERED (categories 4, 5, 6 EMPTY; category 1 has 1 file) | `19_REVIEWS_TESTIMONIALS_AND_CASE_STUDIES\` (stub) points here; gap noted |
| RAM financial-objection module | `X-Singapore Real Estate Insider - MAS HQ\01_MAS_OS\02_CONVERSATION_CONVERSION_SYSTEM\MAS_RAM_RISK_ASSESSMENT_MODULE_v1.0.md` | LEGACY, content-complete | `09_FINANCIAL_AND_PROPERTY_ANALYSIS\` (stub) points here; `11_OBJECTION_INTELLIGENCE\` surfaces it as the financial-objection tool and proposes promotion |
| End-to-end sales synthesis | `00_COACH_EDMUND_BUSINESS_BRAIN_V1.0\07_CONSULT_SALES_LOGIC.md` | CANDIDATE — **Stage 4 closing tactics (scarcity, takeaway close) CONTRADICT current doctrine; do not build from Stage 4** (SC-02) | Referenced only for Stages 1–3; Stage 4 explicitly excluded |
| Marketing handoff | `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md`, `DATA_SOURCES.md`, `02_CUSTOMER_INTELLIGENCE\OBJECTIONS_MAP.md`, `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`, `DECISIONS_REQUIRED.md` | DRAFT (sibling OS) | `02_MARKETING_TO_SALES_HANDOFF\` (stub) points here |
| Consult corpus (PII-heavy, local) | `E:\Zoom Consults - Processed\` (553 sessions 2020-05→2024-03; 490 transcripts; 365 genuine 1:1 consults) | READ-ONLY reference | `21_CONVERSATION_INTELLIGENCE\` integration contract: extend, never duplicate |
| Consult intelligence (approved) | `E:\Zoom Consults - Processed\_CONSULT_INTELLIGENCE_OS\02_MASTER_INDEX\MASTER_CONSULT_INDEX.md` (166 rows, inferred Outcome col); `03_CLIENT_LANGUAGE_VAULT\`; `04_OBJECTION_BANK\MASTER_OBJECTION_BANK.md` | APPROVED MASTER (2026-07-09) — Outcome column is AI-inferred, not CRM-verified (SC-05) | `21_CONVERSATION_INTELLIGENCE\` extends this; Sales OS holds anonymised intelligence only |
| Transcript audit | `E:\Zoom Consults - Processed\_TRANSCRIPT_AUDIT\` (490-row inventory + grouping + testimonial clip lists) | READ-ONLY reference | `21_CONVERSATION_INTELLIGENCE\` PILOT_SAMPLE draws from this |
| Decision record | `00_AI_OPERATING_SYSTEM\00_COMMAND_CENTER\04_DECISION_MEMORY.md` (Decision 051 = this build's mandate) | APPROVED MASTER | Governs every ruling in this OS |

READS FROM: SALES_OS_BUILD_SPEC_v1 AUTHORITATIVE SOURCES list.
FEEDS INTO: every Sales OS branch's `_INDEX.md` / `00_CHARTER.md` READS FROM line; `CONTRADICTION_REGISTER.md`.
