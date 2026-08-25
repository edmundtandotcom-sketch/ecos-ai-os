---
name: rei-video-routine
description: Write REI Method long-form video scripts (YouTube Authority Reinforcement, new-launch/project review, or VSL) for Coach Edmund Tan / Singapore Real Estate Insider. Use when asked to write a long-form YouTube script, build a project review video, draft a VSL, or produce the long-form for a campaign. Same procedure and output on desktop and cloud — this skill never renders video, only scripts it.
---

# REI Video Routine — Long-Form Script Generation

Portable version of the `/rei-video-routine` command referenced in `START_HERE.md`. This skill produces a locked script + fact-check map. It does not render — see `video-produce` for that handoff.

## 0. Load context

If not already loaded this session: root `CLAUDE.md`, then `00_AI_OPERATING_SYSTEM/CLAUDE.md` (Second Property Ladder positioning, source-of-truth hierarchy, Tight Ship Mode). Do not invent a generic property framework — align to the MAS stack per that file §10.

## 1. Pick the format

Source: `00_AI_OPERATING_SYSTEM/05_CONTENT_MARKETING_ENGINE/00_PRODUCTION_FOUNDATIONS/REI_Video_Production_Foundation_v1.3.md`.

- **Format 3B (10–30 min, retention-structured)** — default for reactive/topic-driven long-form and cold organic discovery. This is where most output should sit.
- **Format 3 (45 min, ad-conversion spine)** — narrow reinforcement of an angle already proven by Reel/VSL testing (4+ weeks consistent lead quality). Not a coequal alternative to 3B — do not use its persuasion spine for a reactive upload.
- **Format 2 (4–6 min VSL)** — warm/retargeting audience, deeper belief work before booking. Style reference: `REI_VSL_Video_Style_Rules_RESCUED.md` in the same folder.
- **Project review / new-launch long-form** (e.g. a specific condo launch) is none of the above — it's its own genre. Follow the closest existing campaign precedent for structure (hook → point-by-point → verdict scorecard → CTA) and pull that campaign's own locked production rules from its `00_INDEX.md` rather than assuming a generic format.

## 2. Source material

- Trend/topic-driven long-form: pull briefs from `weekly_content_intelligence_os/briefs/` in the `property-business` repo (scored content ideas, hooks, angles already vetted against brand-safety rules). That system produces ideas; it does not write the script itself.
- Project review long-form: pull from the campaign's own `Raw Assets/` (e-book, floor plans, architect briefing, GLS/URA data) inside its `03_ACTIVE_CAMPAIGNS/01_ACTIVE/<campaign>/` folder.

## 3. Campaign home

One folder per campaign under `03_ACTIVE_CAMPAIGNS/01_ACTIVE/<campaign-name>/`, governed by its own `00_INDEX.md` (objective, status, folder map, deliverables, decision owner). Never create a second workbench for the same campaign — update the existing index instead (root `CLAUDE.md` §5).

## 4. Fact-check discipline

Before locking any number or claim, build a cross-check map (figure → source) in the same shape as the `cross check resources.md` precedent (`2026-08_New_Launch_Amberwood/`): every figure traces to a URA/agency/internal source, flagged if unverified. Do not present an unverified figure as fact — flag it as an open item instead.

## 5. Locked production rules (house defaults)

Unless the target campaign's own `00_INDEX.md` states different locked rules (rules evolve per campaign — check first, a newer campaign's rules supersede this default list):

- Talk scenes: front camera only, no B-angle alternation.
- Recorded walkthroughs/site-plan showcases: full-frame, head in circular PIP.
- Every spoken number/price gets an on-screen punchline/display.
- Money/number tokens never split across a subtitle cue.
- Transition style rotates per scene (fade/wipe/slide).
- Subscribe reminders seeded through the mid-stretch.
- Music: original synthesized beds only — no Content-ID-claimable tracks.

## 6. Platform verification

Before finalizing anything platform-specific (YouTube limits, formats), verify current platform rules or label the output `DRAFT — pending platform verification` per root `CLAUDE.md` §11.

## 7. Output

Save the script + cross-check map + open-items list into the campaign folder. Update that campaign's `00_INDEX.md` status and deliverables in the same pass — a script without an updated index is incomplete work.

## 8. Handoff

This skill's job ends at a locked script with verified figures. Filming is the user's job. Reel breakdowns from this script: see `rei-reels-routine`. Actual rendering/production: see `video-produce`.
