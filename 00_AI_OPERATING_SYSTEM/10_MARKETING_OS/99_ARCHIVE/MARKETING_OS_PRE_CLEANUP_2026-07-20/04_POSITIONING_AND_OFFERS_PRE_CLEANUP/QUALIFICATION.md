# QUALIFICATION — MARKETING OS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `00_AI_OPERATING_SYSTEM\02_POSITIONING_AND_IP\Which_Move_Are_You_On_Diagnostic.md` (Engine 1 gate logic) + `04_AGENT_EDITION_OS\00_POSITIONING\MAS_AgentEdition_DeepBuyerProfile_v2.0_CANDIDATE.md` (Engine 2). THIS FILE is a pointer + usage layer.
Evidence level: N/A (pointer)
Supersedes: none
Sources: `Which_Move_Are_You_On_Diagnostic.md` §3/§5/§7; AI OS audience masters
Next review: on resolution of C03/C04

---

Purpose: how marketing **qualifies and routes** leads per engine, as a pointer with usage rules. The gate logic master is the diagnostic spec — do not restate it.

## Engine 1 — client qualification (from the live diagnostic)
Cite: `00_AI_OPERATING_SYSTEM\02_POSITIONING_AND_IP\Which_Move_Are_You_On_Diagnostic.md`.
- **Qualified buyer:** owns exactly one property · combined income **$20k+** · timeline within 18 months · **$2.5m+** capacity.
- **Silent grading (never shown on screen):** A (direct calendar) · B (booking link + nurture) · P (portfolio track) · C (nurture, no call CTA).
- **Rule:** disqualification happens in **routing, never in copy** — "never say no on screen." A C-grade lead still gets a useful result.

## Engine 2 — agent qualification
Cite: `...\MAS_AgentEdition_DeepBuyerProfile_v2.0_CANDIDATE.md` (CANDIDATE). Audience: other Singapore property agents entering via the free Market Maker Scorecard. Treat the profile as provisional and flag its CANDIDATE status.

## Marketing-usage rules
- Qualify by **gate logic, not by copy** (Engine 1). Build ad targeting to the gates, not the other way round.
- Keep engines separate: never route an agent lead into the client funnel or vice-versa.
- **PDPA:** the contact-capture step needs compliant consent copy before launch (`COMPLIANCE.md` §2). Capture consent status as a CRM field.
- **PII:** lead data stays in the CRM; **never copy PII into the Marketing OS** — aggregates only.

## Conflicts to flag
- **C03** buyer-definition drift changes who qualifies — flag in any targeting spec.
- **C04** whether qualified HDB/EC owners are in-audience is unresolved.
See `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md`.

READS FROM: `Which_Move_Are_You_On_Diagnostic.md`; AI OS audience masters; `01_BUSINESS_AND_BRAND\COMPLIANCE.md`.
FEEDS INTO: ad-set targeting; `08_CAMPAIGNS\`; `10_PERFORMANCE\` (lead-grade definitions).
