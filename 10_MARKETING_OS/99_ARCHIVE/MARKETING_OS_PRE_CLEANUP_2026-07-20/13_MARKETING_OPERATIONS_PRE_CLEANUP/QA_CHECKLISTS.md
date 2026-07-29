# QA CHECKLISTS
Version: v1.0
Status: DRAFT
Date: 2026-07-11
Owner: Marketing & Ads Desk (approval authority: Edmund / Cindior)
Source of truth: THIS FILE
Evidence level: N/A — operating checklist, not a factual claim
Supersedes: none
Sources: MARKETING_OS_BUILD_BRIEF.md §2 (build rules 8–11), §8 (13_MARKETING_OPERATIONS); CAMPAIGN_LIFECYCLE.md Stage 8–9; 12_TEMPLATES/CREATIVE_BRIEF.md
Next review: after first campaign runs Stage 8–9 in anger

Two gates. Stage 8 = cross-channel QA (creative/copy level). Stage 9 = launch readiness (business level). Both must pass before Stage 10 (Launch). No self-sign-off on Kill/Scale-relevant gates — Edmund/Cindior reviews.

## Stage 8 — Cross-channel QA (per asset)
1. Asset ID assigned (CR-/CP- + linked LL- if applicable) per NAMING_CONVENTIONS.md.
2. Copy tied to a named belief block + Ladder Move / Ascent stage — not generic.
3. Proof cited from an authoritative source, or explicitly `[VERIFY]`-flagged — no fabricated claims.
4. Platform specs verified, or asset labelled `DRAFT — pending platform verification`.
5. Engine separation confirmed — no Client Advisory / Agent Edition blend in one asset.
6. Compliance pass logged (CEA/PDPA/MAS ad rules) — reviewer named.
7. Tracking plan attached (UTM/pixel/GHL stage) and matches the owning campaign's qualified-lead definition.
8. CREATIVE_BRIEF.md 18-criteria scorecard completed; no unresolved score <7.

## Stage 9 — Launch readiness (per campaign)
1. Sales capacity confirmed against projected lead volume (CAMPAIGN_BRIEF.md §5).
2. Budget approved, funding source confirmed.
3. Landing/funnel destination live and tested — no broken links, form submits correctly.
4. CRM pipeline stage + lead owner assigned for incoming leads.
5. Qualified-lead definition shared with whoever screens leads.
6. Kill/scale thresholds pre-agreed and logged (CAMPAIGN_LIFECYCLE.md §Kill/Keep/Iterate/Scale).
7. CAMPAIGN_BRIEF.md filed and campaign registry row created, status set to ACTIVE.
8. Minimum useful data / evaluation window defined (per attached EXPERIMENT_BRIEF.md if applicable).
9. Decision owner named for the first go/no-go review after launch.

## Failure handling
Any Stage 8 item unmet → asset status `QA Failed – Revise` (see 13-status lifecycle, CAMPAIGN_LIFECYCLE.md). Any Stage 9 item unmet → campaign stays `PLANNED`, cannot move to `ACTIVE`. Log the blocker in `00_COMMAND_CENTER/DECISIONS_REQUIRED.md` if it needs an owner call.
