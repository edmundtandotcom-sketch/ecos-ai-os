# FRAMEWORK_LIFECYCLE
Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: MASTER_CONSULTATION_FLOW.md (this branch); the six conversation masters (paths therein); PWS_DISPOSITION.md (this branch)

## 1. Purpose
Give every consultation framework a controlled **lifecycle status** so the OS knows what is safe to run, what is being tested, and what is retired. A framework's status governs whether an advisor may use it live. `[T5]`

## 2. Status Vocabulary (controlled)
| Status | Meaning | May run live? |
|---|---|---|
| **Active** | Approved master, in daily use | Yes |
| **Experimental** | New/changed; being trialled under observation | Yes, flagged, with capture |
| **Supported** | Stable but not the primary; kept for specific contexts | Yes |
| **Validated** | Field-evidenced against outcomes (T1/T2/T3) | Yes — highest confidence |
| **Context-specific** | Valid only for a named segment/situation | Yes, within its context |
| **Superseded** | Replaced by a newer framework; reference only | No (reference) |
| **Deprecated** | Being phased out; avoid for new work | No for new work |
| **Retired** | Withdrawn from use; absorbed or dead | No |

## 3. Current Status Register
| Framework | Master file | Status | Note |
|---|---|---|---|
| Diagnosis Call System | v2.0 (Conversation Conversion) | **Active** | 6-phase spine of P1 |
| Strategy Session Conversation System | v2.0 | **Active** | REI spine of P3 |
| ProDeck Consult Delivery | v2.0 | **Active** | Delivery tool for P3 |
| Decision Psychology & Belief Resolution | v2.1 | **Validated** | Grounded in 376 objections / 166 consults `[T3]` |
| Risk Assurance & Next Action | v2.0 | **Active** | Decision gate P4 |
| Trigger Question Bank | v2.0 | **Active** | Question tool |
| Belief-Shift Question Sequences | v2.0 | **Active** | Objection sequences |
| RAM (Risk Assessment Module) | v2.0 (`03_CLIENT_ADVISORY_OS\03_CONVERSATION_CONVERSION\05_RAM_RISK_ASSESSMENT_MODULE_v2.0.md`) | **Supported — promoted to v2.0 CANDIDATE per Decision 071(2)** | Promoted from legacy MAS HQ v1.0 into the AI OS with mandatory doctrine remap (Ascent A0–A2, RB-01–18, R1–R4, Move vocab); legacy v1.0 kept read-only in place. Content approval pending Edmund. `[T4]` |
| **PWS (legacy consult system)** | — | **Retired / absorbed** | Absorbed into MAS → REI Method → RAM. Do NOT resurrect as a live framework. See PWS_DISPOSITION.md. `[T5]` |
| Historical Stage-4 closing tactics | `00_COACH_EDMUND_BUSINESS_BRAIN_V1.0\07_CONSULT_SALES_LOGIC.md` (Stage 4) | **Deprecated (pending ruling)** | Scarcity/takeaway close contradict doctrine — SC-02. Not for use. `[T5]` |

## 4. Promotion Path
DRAFT → Experimental → (field capture) → Validated/Active. Only Edmund or Cindior promote a framework to Active/Validated (constitution §9). Status changes are logged in `29_CHANGE_LOG` (WS-A) and reflected in CONSULTATION_REGISTRY.csv.
