> **ARCHIVED 2026-07-30 (same day as v2.2's creation) — superseded by `08_OPERATIONS/03_AUTOMATIONS/rei-weekly-content-brief_SKILL.md` v2.3.** Kept verbatim as rollback/history per AI OS file rule. v2.2 shipped with outline-level outputs and a fixed hardcoded source list; v2.3, in the same working session, corrects both after Edmund's follow-up: sources are an expandable watchlist (not a ceiling), every output is full word-for-word production (not an outline), long-form video adopts Foundation v1.2's new Format 3B (20-30 min, was invented generic Format A/B/C here), image assets get ready-to-paste AI image-gen prompts since this automation cannot render images itself, and a dedicated per-platform social post output was added.

---

---
name: rei-weekly-content-brief
description: REI Unified Weekly Organic Content Intelligence — Monday 8:45 AM (articles + YouTube, one ranked output, fans out to scripts/posts/articles)
---

<!--
AI OS MIGRATION HEADER
Version: v2.2
Status: APPROVED MASTER
Date: 2026-07-30
Supersedes: v2.1 (2026-07-11, archived at `08_OPERATIONS/99_ARCHIVE/rei-weekly-content-brief_SKILL_v2.1_ARCHIVED_2026-07-30.md`) — merges the previously-separate shallow YouTube format-study pass into full transcript-based repurposing (one signal pool, not a proposed separate third routine), restructures execution into Phase A (scan) / B (rank) / C (fan-out), corrects the output destination (v2.1/v1.0's documented path under the retired `01_PROPERTY_BUSINESS` folder no longer exists post the 2026-07-20 workspace restructure — verified live output already lands in `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/`, this version documents that as canonical), retires "Cowork" as the scheduler in favor of the Claude Code scheduled-tasks system (this file is now the spec a Claude Code scheduled task points to), and adds an automatic GitHub backup step.
Sources: rei-weekly-content-brief_SKILL.md v2.1 (archived); rei-weekly-content-brief_PROMPT_v1.0.md (historical, already flagged retired); singapore-property-ads-brief_SKILL.md v2.0+ (sibling ads-intelligence routine, out of scope here); root/AI OS CLAUDE.md v4.6/v4.7; 2026-07-30 consolidation decision (see 04_DECISION_MEMORY.md).
-->

# REI WEEKLY ORGANIC CONTENT INTELLIGENCE — ARTICLES + YOUTUBE, ONE RANKED OUTPUT
## Version: 2.2 (Monday 8:45 AM — merged article + YouTube scan, single scheduler)

**Task ID:** rei-weekly-content-brief
**Schedule:** Every Monday, 8:45 AM Singapore time
**Scheduler:** Claude Code scheduled tasks (not Cowork — see 2026-07-30 decision below)
**Execution Type:** One unified scan across articles + YouTube → one ranked angle list → fanned out into every output format

---

## WHY THIS VERSION CHANGED

v2.1 already scanned StackedHomes/EdgeProp/URA/99.co (Tier 1 articles) and glanced at Marcus Luah/JNA/StackedHomes YouTube channels (Tier 2) — but only for format/pacing study, not real repurposing. A proposal to build a third, YouTube-only routine was rejected: it would duplicate this scan and produce a second, disconnected ranked-angle list for the same week, splitting "what's this week's #1 topic" across two reports that could disagree. Instead, articles and YouTube are two input lanes into the *same* signal pool, ranked once, fanned out into every output format needed. v2.1 was also written against the "Cowork" scheduler, which does not appear anywhere in this machine's live Claude Code scheduled-tasks list — it was very likely not actually firing. This version is registered as a Claude Code scheduled task instead, alongside the sibling `singapore-property-ads-brief` routine, so both live on one scheduler that can actually be inspected (`list_scheduled_tasks`).

---

## REAL DATA EXTRACTION — NO SYNTHESIS FALLBACK

Most important rule in this spec, unchanged from v2.1: **never fabricate, estimate, or "research-based" substitute any data if a source is blocked or a tool is unavailable.** Stop that step and report the failure plainly in the final report instead.

---

## PHASE A: SIGNAL SCAN (articles + YouTube, one pass)

### A1 — Article sources (Tier 1, must-scan weekly)
- URA (ura.gov.sg) — official releases, GLS tenders, stats
- EdgeProp — new launches, market commentary
- StackedHomes (stackedhomes.com + stackedhomes.com/category/*) — analysis, buyer guides, case studies
- 99.co blog — resale data, transaction analysis
- PropNex news — market reports
- MoneySmart property — mortgage/finance angle

### A2 — YouTube sources (Tier 2, now full repurposing input, not just format study)
For each channel below, pull the last 7 days of uploads:
- Marcus Luah ("Keep It Real Estate" series)
- JNA Real Estate ("JNA News Dash")
- StackedHomes YouTube
- Any other channel already logged in `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/` as a tracked creator

For each new video: pull the transcript (captions, or the Browser pane), note publish date and view count if visible, and extract the hook (first 15 seconds), the core data point(s) cited, the structural format (data-dump / narrative / myth-bust), and CTA placement. Treat a strong video signal exactly like a strong article signal in Phase B scoring — this is a real content input now, not a stylistic footnote.

### A3 — Signal sources (Tier 3, exploratory)
Google Trends (SG property keywords), Reddit r/singapore + r/singaporefi, HardwareZone property forums, relevant Telegram/FB groups, YouTube comments on Tier 2 videos, Google News alerts.

### Data quality rules
1. Only date-verified signals from the 7-day scan window (Monday–Sunday).
2. All URLs on separate lines, tested live.
3. No repeat of an angle already ranked in last week's brief — check Section 0 of the prior week's file in Knowledge Vault before finalizing.

---

## PHASE B: SCORE & RANK (6-step filter, unchanged from v2.1)

For every signal — article or video — score 0–6:
1. REI Method alignment (R→E→I applicable)?
2. Client belief shift (addresses a false belief)?
3. Content gap (competitors covering this well already)?
4. Emotional hook (urgency/FOMO)?
5. SI-05 / Evergreen Authority relevance?
6. Proof/data available (citable)?

Keep only 6+ scored signals. Rank 1 = highest urgency + strongest proof + clearest REI fit. Aim for 3 news-triggered + 2 evergreen across the top 5.

---

## PHASE C: FAN OUT (one ranked angle → every format, not re-researched per format)

For each of the top 5 ranked angles, produce all of the following from the *same* underlying angle/data:

**YouTube scripts — 3 formats** (still production-ready, not outlines):
- Format A — Fast-Paced Data-Driven (~2–3 min): shocking stat hook → data dump → implication → CTA
- Format B — Narrative/Story-Led (~3–4 min): real scenario hook → context → 3 specific moves → social proof → CTA
- Format C — Authority Breakdown / Myth-Bust (~2.5–3 min): myth hook → evidence → correct framework → next step → CTA
- Model pacing/CTA-timing on the Tier 2 video that best matches the angle (Phase A2), keep REI framing — see Attribution Rule below.

**Social/IG posts:** one carousel concept (slide-by-slide) + one single-image quote/stat post per angle, built on the same hook already validated in the video script.

**WhatsApp broadcast — 3 segments** (unchanged from v2.1): Segment 1 (high intent, existing/warm leads, "Reply AUDIT"), Segment 2 (medium intent, "Reply POSITION"), Segment 3 (cold, narrative only, video link).

**Article outline:** working title, 3–5 section headers, the one stat/data point the whole piece hangs on, internal link target.

### Attribution rule (new in v2.2)
When an angle originates from a specific outlet's proprietary analysis (e.g. a StackedHomes unit-level yield breakdown), reframe it through REI's own data/REI Method rather than rewriting their write-up, and link/credit the source. Do not republish another outlet's original analysis in "our voice" with no reference back — this is a real copyright/reputational exposure, not a style preference.

### On-demand mode (new in v2.2)
Edmund or Cindior can request a single-topic version any day of the week ("spin up an angle on X"): run Phase A scoped to that topic only (skip the full weekly scan) + Phase C fan-out. Same quality bar, same attribution rule — no need to wait for Monday.

---

## LIBRARY & OUTPUT

**Weekly dated brief** → `H:\Shared drives\00_E.C.O.S\00_AI_OPERATING_SYSTEM\06_KNOWLEDGE_VAULT\01_MARKET_INTELLIGENCE\[WEEK] REI Weekly Brief — YYYY-MM-DD.md` — verified live destination; v2.1/v1.0's `01_PROPERTY_BUSINESS/.../Weekly Contents/` path is stale and no longer exists.

**Growing pattern/angle library** (evergreen, not recreated weekly) → same Knowledge Vault folder, one running registry file — append, don't duplicate.

**Bi-weekly rollup** (unchanged condition: only if 2+ weekly briefs exist) → same folder, `[ROLLUP] REI Bi-weekly Insights — YYYY-MM-DD.md`.

**Once Edmund picks a Rank-1 angle to actually shoot** → that becomes its own workbench in `03_ACTIVE_CAMPAIGNS`, per the Content Studio desk rule — it does not stay in the Knowledge Vault brief.

---

## GITHUB BACKUP (new in v2.2)

At the end of every run (weekly or on-demand):
```
cd "H:\Shared drives\00_E.C.O.S\00_AI_OPERATING_SYSTEM"
git add -A
git commit -m "Content brief: <date>"
git push origin main
```
If git reports "nothing to commit," skip silently. If push fails (auth/network), report the failure plainly in the final report — do not retry silently or drop the brief.

---

## CONSTRAINTS

1. No synthesis fallback — real data only.
2. WhatsApp must always be segmented — never mass-blast.
3. No angle repeats from the prior week.
4. All URLs on separate lines, date-verified.
5. Ignore any folder outside the current live workspace map in root `CLAUDE.md` §2 — if a path referenced here looks stale, stop and flag it rather than guessing a replacement (this is the exact failure this version fixes).

---

## CHANGELOG

**v2.2 (2026-07-30)** — Merged YouTube from format-study-only into full repurposing input; restructured into Phase A/B/C; corrected output path to Knowledge Vault; retired Cowork as scheduler in favor of Claude Code scheduled tasks; added attribution rule; added on-demand single-topic mode; added GitHub backup step.

**v2.1 (2026-07-11)** — Decision 067 (O14 ruling): removed Family Legacy/Mash-up/SI-06 classification.

**v2.0 (2026-06-20)** — Consolidated weekly brief + bi-weekly rollup, added live Chrome automation requirement, made rollup conditional.

**v1.0 (2026-06-15)** — Initial weekly brief task created.

## END REI WEEKLY ORGANIC CONTENT INTELLIGENCE v2.2
