# SMS
Version: v1.0
Status: DRAFT — pending platform verification
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (playbook)
Evidence level: N/A — no dedicated asset or strategy found in workspace
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM/04_AGENT_EDITION_OS/02_MARKETING/MAS_MARKETING_INTELLIGENCE_OS_v1.md` (STALE, C05, one combined "WhatsApp/GHL SMS" line only)
Next review: when a v1 fallback-channel build is scoped

## Strategic role
Client Advisory / Agent Edition: a potential low-cost, high-open-rate fallback channel for time-sensitive reminders (appointment confirmations, event day-of reminders) where WhatsApp isn't available or opted-in. **No dedicated SMS asset, sequence, or strategy exists anywhere in this workspace.** The only mention found is one line inside the STALE MAS skeleton (WhatsApp/GHL SMS combined, ~95% open-rate claim, unverified). Treat this as a fallback-channel note, not a built channel.

## Best use cases (anticipated, not evidenced)
Appointment-reminder fallback; short urgent day-of nudges for events; never a primary nurture channel.

## Required inputs (for a v1)
GHL SMS gateway/number confirmation; opt-in/consent workflow (PDPA); 160-character message templates; currently-verified SG SMS marketing/regulatory limits (not verified here).

## Process
**None exists.**

## Outputs
N/A currently.

## KPIs
Define: delivery rate, reply rate, opt-out rate. **No live baseline exists — zero evidence of any tier found.**

## Common failure modes (anticipated)
Using SMS as a bulk broadcast channel (deliverability/regulatory risk in Singapore); no opt-out mechanism; exceeding the 160-character limit cited in the unverified skeleton.

## Integration with other channels
Would sit as a fallback/escalation inside CRM_NURTURE.md and EVENTS_WORKSHOPS.md (day-of reminders) — never a standalone campaign leg.

## Evidence status
**N/A.** Only one line inside the STALE MAS_MARKETING_INTELLIGENCE_OS_v1 skeleton (C05) mentions SMS at all — not enough to call this a built channel.

## Known gaps
No SMS gateway, template, or consent workflow found. Genuine ground-zero gap — do not pad with generic SMS best-practice.
