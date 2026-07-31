# CRM_NURTURE
Version: v1.0
Status: DRAFT — pending platform verification
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE (playbook) — CRM logic defers to sources below
Evidence level: N/A (process) / no performance data of any tier found
Supersedes: none
Sources: `00_AI_OPERATING_SYSTEM/08_OPERATIONS/01_CRM_AND_TRACKING/04_NURTURE_REACTIVATION_AND_DATABASE_MOVEMENT_SYSTEM_v2.0.md`, `01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md`, `08_OPERATIONS/04_CONTACT_DATABASE_REGISTRY.md`, `04_AGENT_EDITION_OS/02_MARKETING/MAS_MARKETING_INTELLIGENCE_OS_v1.md` §11 (STALE, C05)
Next review: when the GHL contact import is executed

## Strategic role
Client Advisory: the Nurture/Reactivation system (APPROVED MASTER) governs post-lead relationship management for both engines; GHL is system of record for contact/pipeline. Agent Edition: a GHL automation skeleton exists (STALE C05, pipeline/tag structure) — needs re-verification against the locked Market Maker Method.

## Best use cases
Readiness-tier-based follow-up (P1–P4); trigger-monitoring reactivation (property/family/financial/market/behaviour/belief triggers); past-client/rung-review cadence; database review before increasing ad spend (Nurture system §11).

## Required inputs
Minimum lead fields (source, campaign, Ascent Stage, buyer profile, trigger, belief block, quality grade, booking status, next action, owner — CRM Pipeline §3); pipeline stage (7 stages: New Lead → Contacted → Appointment Set → Consult Done → Decision Pending → Won/Closed → Nurture); lead quality grade (A–D).

## Process
Tag every lead with a nurture state (Active / Trigger Watch / Content / Client Development / Parked, §3) → set priority P1–P4 (§4) → monitor primary + next trigger (§5) → set cadence by priority (§8) → on a reactivation signal, run the scenario-specific review (§9) → every follow-up states what changed and why it matters (§10) → periodic database review before spend increases (§11).

## Outputs
CRM field updates, follow-up message content, database review reports. GHL is system of record — Marketing OS references this system, does not rebuild it.

## KPIs
Define: reactivation rate by trigger type, readiness-direction movement (increasing/stable/declining), P1 response time (target same-day–72hr per §8), database review cadence adherence. **No live baseline exists** — the 17,663-contact database has **not been imported to GHL yet** (import NOT executed per the Contact Database Registry), so nurture cannot yet be measured against these fields at scale.

## Common failure modes
Nurture used as a "holding bin" instead of an active relationship state (§3's explicit warning); chasing without a trigger or context (banned follow-up language, §10); over-serving low-priority (P4) contacts with advisor time; skipping database review before spend increases.

## Integration with other channels
Receives leads from every paid/organic channel; EMAIL.md / WHATSAPP.md / SMS.md are the execution arms; feeds REFERRAL.md (Client Development stage) and WEBINAR.md / EVENTS_WORKSHOPS.md (registration/reminders). The Contact Database import (17,663 unique, 7,272 import-eligible, **not executed**) is the current blocking dependency.

## Evidence status
Nurture/CRM Pipeline systems = **APPROVED MASTER** (Tier N/A, process spec). GHL automation skeleton for Agent Edition = **STALE (C05)**. No performance data of any tier exists for nurture-driven reactivation outcomes, and cannot exist at scale until the GHL import is executed.

## Known gaps
GHL import not executed (blocking); Agent Edition automation needs re-verification against the Market Maker Method; no reactivation performance data found anywhere in this workspace.
