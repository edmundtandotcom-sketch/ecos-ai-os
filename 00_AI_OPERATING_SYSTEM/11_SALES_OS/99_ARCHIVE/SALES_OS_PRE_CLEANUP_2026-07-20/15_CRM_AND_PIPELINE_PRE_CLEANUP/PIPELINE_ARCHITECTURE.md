# PIPELINE_ARCHITECTURE

Version: v0.1
Status: DRAFT
Date: 2026-07-11
Supersedes: none
Sources: GHL live read-only audit 2026-07-11, T2 (`GHL_LIVE_AUDIT_2026-07-11.md`, orchestrator scratchpad); `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` (SOP, T1 approved master); `00_AI_OPERATING_SYSTEM\08_OPERATIONS\02_SCRIPTS\REI_AppsScript_ACTIVE_v8.43.gs` (direct code read, T1); `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md` (T2 draft); `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §14 (mandate intent); `SALES_OS_BUILD_SPEC_v1.md` (Fable, orchestrator)

Resolves: **SC-01** (four pipeline definitions) — logged in `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` per the AI OS conflict-detected format, not silently.

---

## 1. The Four Definitions (why SC-01 exists)

| # | Definition | Where | Stage count |
|---|---|---|---|
| 1 | Live GHL pipeline ("1-To-1 Pipeline", id `BdutTA7xHUrNoPpWc5Nu`) | GHL production, 397 live opportunities | 10 stages |
| 2 | SOP intent | `01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` §4 | 7 stages |
| 3 | Apps Script dashboard funnel (`FUNNEL_STAGES`, v8.43) | `REI_AppsScript_ACTIVE_v8.43.gs` | 9 dashboard statuses, partially GUID-mapped |
| 4 | Marketing-facing shorthand | `KPI_DEFINITIONS.md` | "Lead → Responded → Booked → Show → Session → Closed" (6-step gloss over #3) |

None of these four fully agree. This file resolves them to one target architecture (§4) and frames the residual naming call as a decision for Edmund (§5).

## 2. Live 10-Stage Truth (T2, live audit 2026-07-11)

| # | Stage | Stage ID | Opps (of 397) | % |
|---|---|---|---:|---:|
| 0 | New Lead | `29567d9f-bddf-485d-85dc-da928856d1e7` | 166 | 41.8% |
| 1 | Responded | `ddc85555-52a5-4e98-8361-2eb74d84a8ec` | 56 | 14.1% |
| 2 | Booked Call | `4d146356-b947-4a8a-ade9-7dafea62202d` | 116 | 29.2% |
| 3 | Appointment | `baf695fb-be5c-4f5b-8596-4193beca03c6` | 44 | 11.1% |
| 4 | Strategy Session | `9881c6e9-2350-43b4-8518-5f8899b86a7e` | 11 | 2.8% |
| 5 | Close | `9c4607fd-a265-4ab4-8acf-705b2fd18ff6` | 4 | 1.0% |
| 6 | Nurture | `ccf2a191-99f2-4180-a4be-fb3c29a20d76` | 0 | 0% |
| 7 | Unqualified | `d5df529e-232a-4b9c-b9c7-563db9f21df1` | 0 | 0% |
| 8 | Won | `626cf974-a751-4dd4-a854-fd05fde9dda0` | 0 | 0% |
| 9 | Lost | `0829d917-331f-4ee2-a240-ee99d97a6a28` | 0 | 0% |

Key facts (T2): 282 of 397 opportunities (71%) sit in New Lead + Booked Call. Stages 6–9 have **never** held an opportunity in this pipeline's 9-month history (2025-10-12 → 2026-07-10). `status` field is `open` on all 397/397 — including the 4 already in Close. 36% of the 220-record sample is untouched 30+ days, concentrated in New Lead/Booked Call.

**Reading:** this is not a 10-stage funnel with a Won/Lost gap at the end. It is effectively a 6-stage funnel (New Lead → Close) with four unused terminal stages and zero outcome discipline — the pipeline has never once recorded a win or a loss.

## 3. SOP 7-Stage Intent (T1, approved master)

`01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` §4: New Lead → Contacted → Appointment Set → Consult Done → Decision Pending → Won/Closed → Nurture. Written as a lean, non-technical stage list — it describes an intended process, not the built CRM. **None of "Contacted," "Appointment Set," "Consult Done," or "Decision Pending" exist as GHL stage names in the live pipeline.**

## 4. Apps Script Mismatch (T1, direct code read of `REI_AppsScript_ACTIVE_v8.43.gs`)

The script's `STAGE_ID_STATUS` map (lines 1358–1365) hardcodes 6 of the 10 live stage GUIDs: New, Responded, Appointment, Strategy Session, Close, Lost. Confirmed gaps against the live 10-stage list in §2:

- **Booked Call GUID (`4d146356-b947-4a8a-ade9-7dafea62202d`) is missing from `STAGE_ID_STATUS`** — confirmed by direct read, not just the audit. Booked Call holds 29.2% of live volume (~30%, matching the audit's estimate). Because the map falls through to a stage-*name* lookup (`STAGE_STATUS['booked call'] → 'Booked Call'`) it still resolves correctly today only because GHL's `stage.name` string happens to match — this is brittle (a GHL stage rename breaks it silently) where the other 6 stages are ID-pinned.
- **Nurture, Unqualified, and Won GUIDs are also missing from `STAGE_ID_STATUS`.** Won in particular has no dashboard status of its own — an opportunity in the live Won stage would fall through to the `status`-field check (`oppStatus === 'won' ? 'Closed'`) and get folded into the same "Closed" bucket as the Close stage, or (if `status` isn't `won`) fall through further to a raw `New` default. Net effect: the dashboard cannot currently distinguish Close (pending) from Won (actually closed).
- **Lost GUID — the live audit (T2) flags this reference as wrong.** Direct code read (lines 1364 and 1427, T1) shows the literal value `0829d917-331f-4ee2-a240-ee99d97a6a28` in both `STAGE_ID_STATUS` and `STAGE_IDS`, and this **matches** the live pipeline's Lost stage ID reported in the same audit (§2 above). The two evidence sources disagree on this one point. **Do not trust either claim blindly** — re-run a live write-test (move a test opportunity to Lost via the dashboard, confirm it lands on the correct GHL stage) before shipping any Lost-related fix.
- **`updateGHLOpportunity()` (the dashboard→GHL write path) only ever writes `pipelineStageId`.** It does not write `monetaryValue` or `lostReasonId`. Even a perfect GUID map would not fix the 0-Won/0-Lost-with-reason problem — the write function needs to be extended once the fields in `CRM_FIELDS.md` exist.
- The Apps Script's own dashboard funnel (`FUNNEL_STAGES`, 9 buckets including "Appt Qualified") does not map 1:1 to the live 10 GHL stages — "Appt Qualified" is inferred from GHL stage *names* ("implementation opportunity," "attended") that do not appear anywhere in the live stage list in §2. It is a dashboard-only construct, not a live pipeline stage.

## 5. Target Architecture (recommendation)

**Keep the live 10-stage GHL pipeline as the physical pipeline.** Do not add, remove, or reorder stages. Define stage-entry/exit criteria and remap the SOP's language onto it (per Hard Rule 3, pointer not duplicate — the SOP file itself is untouched; this is the reconciliation layer).

### 5.1 Name mapping (SOP intent → live stage)

| SOP stage (§4 intent) | Live stage | Note |
|---|---|---|
| New Lead | **New Lead** | Same name, same meaning. |
| Contacted | *(no live stage)* | Live pipeline has no "attempted contact, no reply" stage. Recommend: track as a contact-level sub-status/tag inside New Lead, not a pipeline stage move — a stage move should mean something changed, not that an attempt was logged. |
| Appointment Set | **Booked Call** → **Appointment** | Live pipeline splits this into two: Booked Call (booking confirmed, not yet happened) and Appointment (the appointment stage proper). Keep both — they answer different questions (booked vs. shown up) and 29.2%+11.1% of volume sits across them. |
| Consult Done | **Strategy Session** | Direct match. |
| Decision Pending | **Close** | Direct match — this is the "client has the recommendation, hasn't decided" holding stage. |
| Won / Closed | **Won** | Live pipeline separates Won from Close; SOP collapses them. Recommend keeping them separate live (see §5.2) — Close = pending decision, Won = confirmed transaction. |
| Nurture | **Nurture** | Same name, exists live, never used (0 opps ever). |
| *(no SOP equivalent)* | **Unqualified** | No SOP stage maps here. SOP's closest concept is the A–D lead-quality grade (§5 of the SOP, especially "D/Exclude"). Recommend: Unqualified = the pipeline-stage home for a D-grade/no-fit lead once it's clear the person isn't advisory-ready, kept distinct from **Lost** (which implies a real deal that didn't close). This is a genuine gap, not just a naming mismatch — see Decision 2 below. |
| *(no SOP equivalent)* | **Lost** | SOP's "Won/Closed" bucket implicitly covers "everything that isn't won," which is too coarse. Live Lost stage should carry a lost-reason code (§5.2). |

### 5.2 Stage-exit rules that force outcome capture

The core defect (§2) is that nothing in this pipeline has ever required an outcome to be recorded. Every stage-exit rule below is a **process/automation requirement**, not yet built — cross-reference `AUTOMATIONS\PROPOSED.md`.

| Moving TO stage… | Required before the move is allowed to "count" |
|---|---|
| **Strategy Session** | `consultation_outcome` field populated at session end (new field, `CRM_FIELDS.md`) |
| **Close** | `next_follow_up_date` (DATE) set — a deal sitting in "Decision Pending" with no next action is exactly the 36%-stale pattern already observed |
| **Won** | `monetaryValue` populated (>0) **and** native `status` field flips from `open` to `won` in the same action. Both conditions, not one — the 4 existing "Close" opportunities are proof that stage alone doesn't capture outcome (they're all still `status: open`). |
| **Lost** | Native `lostReasonId` populated, value drawn from the controlled LOST_REASON list at `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` (WS-B, in build). `status` flips to `lost`. |
| **Unqualified** | A reason is required here too. **Gap:** no controlled vocabulary currently exists for "why unqualified" distinct from LOST_REASON. Recommend WS-B extend `OUTCOME_CODES.md` with an UNQUALIFIED_REASON subtype, or Edmund rules that Unqualified reuses LOST_REASON with a "not a fit" style code — see Decision 2. |
| **Nurture** | `next_follow_up_date` required, same as Close — Nurture is a parking stage, not an exit. |

### 5.3 Apps Script fix list (ranked, ties to §4)

1. Add the missing `4d146356-b947-4a8a-ade9-7dafea62202d` (Booked Call) GUID to `STAGE_ID_STATUS`, explicitly — do not rely on the name-string fallback.
2. Add the missing Nurture (`ccf2a191-99f2-4180-a4be-fb3c29a20d76`), Unqualified (`d5df529e-232a-4b9c-b9c7-563db9f21df1`), and Won (`626cf974-a751-4dd4-a854-fd05fde9dda0`) GUIDs to `STAGE_ID_STATUS`, and give Won its own dashboard status distinct from Closed.
3. Re-verify the Lost GUID end-to-end with a live write-test (§4) before relying on either the audit's "wrong" flag or the code's apparent match.
4. Extend `updateGHLOpportunity()` to write `monetaryValue` and `lostReasonId` alongside `pipelineStageId`, once those fields exist (`CRM_FIELDS.md`).
5. Rebuild `FUNNEL_STAGES` to mirror the live 10 stages exactly (retire the invented "Appt Qualified" bucket) once Edmund rules on Decision 1 below.

These are proposals only — **no script change ships from this file.** Building/testing the script patch is out of scope for this branch; hand off to `01_E.C.O.S\07_OPERATIONS_DESK.md` once Edmund approves.

## 6. DECISION REQUIRED — Edmund

**Decision 1 — Rename live GHL stages to match SOP language, or remap the SOP/script/KPI docs to match live GHL stage names?**

My pick: remap the documents (SOP §4, `KPI_DEFINITIONS.md`, Apps Script comments) to the live stage names; do not rename anything in the live pipeline.
Reason: (1) 397 live opportunities and 9 months of history sit on the current stage IDs — a GHL stage *rename* is technically low-risk (the script keys off IDs, not names, in 6 of 10 stages) but any deeper pipeline surgery is not, and the pipeline already has zero outcome discipline; don't add migration risk on top of that. (2) Lower blast radius: 3 documents change vs. one production system with live records and a live dashboard script reading it in real time. (3) The live names (Booked Call, Strategy Session, Close) already read as plain English — the SOP's "Consult Done"/"Decision Pending" aren't meaningfully clearer.
Avoid: renaming the live pipeline before Won/Lost tracking even works — that's sequencing risk on top of the real problem (§2).

**Decision 2 — What reason-code list governs the Unqualified stage-exit?**

My pick: extend `12_CLOSING_AND_DECISION\OUTCOME_CODES.md` (WS-B, in build) with a short UNQUALIFIED_REASON subtype (e.g., "not advisory-ready," "no contact method," "duplicate/internal," "spam") rather than overloading LOST_REASON, which should stay reserved for "we pursued this and it didn't close."
Reason: (1) Unqualified and Lost answer different questions for reporting — conflating them would make "lost reason" analysis noisy with non-deals. (2) The SOP's existing D/Exclude grade (§5) already implies a short, closed list — this just gives it a stage-exit home.
Avoid: leaving Unqualified with no required field at all — that reproduces the exact defect (a stage nothing is ever required to explain) this file is trying to fix.

**Decision 3 — Authorize the Apps Script GUID-map patch (§5.3, items 1–3) now, or hold until the full stage-exit automation ships together?**

My pick: hold — patch the GUID map and the stage-exit enforcement automations (`AUTOMATIONS\PROPOSED.md`) in the same release.
Reason: (1) fixing the GUID map alone makes the dashboard display Booked Call/Nurture/Unqualified/Won correctly, but it does nothing for the underlying problem — opportunities can still move to Won/Lost with no `monetaryValue` or `lostReasonId`. (2) Shipping the display fix first risks Edmund reading a "fixed" dashboard as "problem solved" when the actual leak (0 outcomes ever recorded) is still open.
Avoid: shipping partial fixes that create a false sense of resolution.

## 7. Migration Implications

No live GHL changes are proposed or executed by this file. If Decision 1–3 are approved: (a) doc updates are zero-risk and can ship immediately; (b) the Apps Script patch needs a sandboxed test against a duplicate/test opportunity before touching the live script (per constitution §11, platform behavior must be verified, not assumed); (c) stage-exit automations should be piloted on new opportunities only, not retroactively enforced on the 397 existing ones (retroactive enforcement would instantly generate 393 "incomplete" records with no fair way to backfill monetaryValue/lost reasons for deals that closed or died before this system existed).

## READS FROM
`GHL_LIVE_AUDIT_2026-07-11.md` (T2, orchestrator scratchpad, this session) · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\01_CRM_AND_TRACKING\01_CRM_PIPELINE_AND_LEAD_QUALITY_SYSTEM_v2.0.md` · `00_AI_OPERATING_SYSTEM\08_OPERATIONS\02_SCRIPTS\REI_AppsScript_ACTIVE_v8.43.gs` · `10_MARKETING_OS\10_PERFORMANCE\KPI_DEFINITIONS.md` · `99_ARCHIVE\ECOS_SALES_BUILD_MANDATE_2026-07-11.md` §14

## FEEDS INTO
`CRM_FIELDS.md` · `DATA_DICTIONARY.md` · `REPORTING\METRICS.md` · `AUTOMATIONS\PROPOSED.md` · `00_COMMAND_CENTER\CONTRADICTION_REGISTER.md` (SC-01) · `00_COMMAND_CENTER\DECISIONS_REQUIRED.md`
