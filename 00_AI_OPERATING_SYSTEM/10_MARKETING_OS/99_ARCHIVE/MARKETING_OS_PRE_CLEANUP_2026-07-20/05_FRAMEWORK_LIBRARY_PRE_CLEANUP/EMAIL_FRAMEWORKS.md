# EMAIL_FRAMEWORKS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: `FRAMEWORK_REGISTRY.csv` row FR-17; `05_CONTENT_MARKETING_ENGINE\00_FOUNDATIONS\EMAIL_MARKETING_GUIDE_REGISTRY.md` (pointer, content inaccessible)
Evidence level: Tier 5 (FR-17); N/A (registry pointer)
Supersedes: none
Sources: `MAS_MARKETING_INTELLIGENCE_OS_v1.md` §7, `EMAIL_MARKETING_GUIDE_REGISTRY.md`
Next review: when the Email Marketing Guide is converted from .docx to a real .md master

---

### FR-17 — Pre-Event Nurture Email Sequence
**Purpose:** Move a warm lead (post free-diagnostic opt-in) toward the 3-Day event application without pressure. **Best use:** Agent Edition nurture after a Market Maker Scorecard opt-in. **Not for:** Client Advisory (Agent Edition only, and STALE — see below). **Inputs:** lead source tag, sequence timing (pipeline stage → webhook events from the Scorecard → tag system → follow-up timing rules), subject-line formula, proof/value content per email. **Structure outline:** pre-event nurture sequence tied to GHL automation stages; subject lines follow a stated formula (not reproduced here — see source, platform-verification pending). **Failure mode:** sending the sequence without the GHL tag/webhook wiring in place first — the sequence assumes automated triggering, not manual sends. **Evidence:** Tier 5. **Status: STALE (C05)** — usable skeleton only, re-verify against locked Market Maker Method before use. **Source:** `04_AGENT_EDITION_OS\02_MARKETING\MAS_MARKETING_INTELLIGENCE_OS_v1.md` §7.

## Client Advisory Email — Registry Pointer Only
`05_CONTENT_MARKETING_ENGINE\00_FOUNDATIONS\EMAIL_MARKETING_GUIDE_REGISTRY.md` points to `Email Marketing Guide.docx` (11.1 KB, last modified 2026-06-29) — subject line, sequence structure, and CTA guidance for the Client Edition nurture/reactivation engine. **Content is inaccessible** — no .md master exists, and per AI OS build rule 1 a .docx is not converted as part of a migration task. This is the only Client-side email framework reference found in inventory. Feeds `08_OPERATIONS\01_CRM_AND_TRACKING` (nurture/reactivation) once converted.

## Cross-Reference
The Trigger Marketing Bank's Universal [U] cross-door tools (`05_CONTENT_MARKETING_ENGINE\04_TRIGGER_MARKETING\`) include reusable email subject-line and soft/direct CTA variants — swap the door-specific numbers and story per campaign. See `COPY_FRAMEWORKS.md` FR-04 for the underlying content hierarchy those subject lines are built to move a reader through.

## Gap Statement
No Client Advisory email framework exists in readable Markdown form anywhere in this workspace. This is a genuine gap, not an oversight — flag for conversion before any real Client Advisory email sequence is built at scale.

## Selection Rule
Run every choice through `FRAMEWORK_SELECTION.md`. Do not deploy FR-17 language into a Client Advisory email under any circumstance — it is Agent Edition offer-ladder-specific.
