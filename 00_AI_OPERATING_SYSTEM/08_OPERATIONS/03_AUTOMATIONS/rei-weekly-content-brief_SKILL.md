---
name: rei-weekly-content-brief
description: REI Weekly Content Engine — Monday 8:45 AM (articles + YouTube, full production-ready output for all 5 ranked angles — not outlines)
---

> **RETIRED 2026-07-30 — Claude Code scheduled task disabled, not the active spec.** The Cloud routine "Weekly Content Intelligence" (claude.ai/code/routines, repo `ecos-weekly-intelligence` — renamed from `Property-Business` 2026-07-31) is now the single scheduled content-engine system — real YouTube Data API, auto-PR/merge, already running weekly. This file's requirements (merged article+YouTube scan, Format 3B long-form, full word-for-word production for all 5 angles, image-gen prompts, inline citations, Second Property Ladder synthesis) still need to be folded into that Cloud routine's prompt — that rebuild has not happened yet as of Decision 114. Keep this file as the requirements reference until that rebuild is done; do not treat it as something that runs.

<!--
AI OS MIGRATION HEADER
Version: v2.4
Status: APPROVED MASTER (superseded as an active schedule — see retirement note above; content requirements still valid)
Date: 2026-07-30
Supersedes: v2.3 (2026-07-30, archived at `08_OPERATIONS/99_ARCHIVE/rei-weekly-content-brief_SKILL_v2.3_ARCHIVED_2026-07-30.md`, same-day supersession). v2.3 scoped full word-for-word production to the Rank 1 angle only (Ranks 2-5 as briefs) — a Claude-proposed default, flagged for confirmation rather than assumed. Edmund confirmed the opposite: **all 5 ranked angles get full production every week.** This version removes the Rank-1/Ranks-2-5 split; every Phase C asset type is produced for every one of the top 5 angles.
Sources: rei-weekly-content-brief_SKILL.md v2.3 (archived); REI_Video_Production_Foundation_v1.3.md (Format 3B, rewritten to retention-based structure 2026-07-30, was v1.2 ad-spine version when this file was written); CONTENT_SOURCE_WATCHLIST.md v1.1 (now includes the merged competitor YouTube roster); 02_POSITIONING_AND_IP (Second Property Ladder spine); 2026-07-30 decisions (see 04_DECISION_MEMORY.md, Decisions 113-114).
-->

# REI WEEKLY CONTENT ENGINE — ARTICLES + YOUTUBE, ONE RANKED OUTPUT, FULL PRODUCTION FOR ALL 5
## Version: 2.4 (Monday 8:45 AM — full word-for-word output for every ranked angle)

**Task ID:** rei-weekly-content-brief
**Schedule:** Every Monday, 8:45 AM Singapore time
**Scheduler:** Claude Code scheduled tasks
**Execution Type:** One unified scan across articles + YouTube → top 5 ranked angles → every angle gets full camera/publish-ready production

---

## WHY THIS VERSION CHANGED (from v2.3, same day)

v2.3 limited full production to the Rank 1 angle to keep weekly volume realistic, with Ranks 2-5 left as briefs — this was Claude's proposed default, explicitly flagged as unconfirmed. Edmund confirmed he wants all 5 angles fully produced every week, not just one. This version removes that split. Everything else from v2.3 (expandable source watchlist, Format 3B long-form, full word-for-word standard, inline citations, image-gen prompts) carries forward unchanged — it now just applies 5 times over instead of once.

**Operational reality this creates, stated plainly rather than smoothed over:** 5× (a 20-30 min script + full article + 5-slide carousel with prompts + single-image post with prompt + 4 platform social posts + 3 WhatsApp segments) is a large amount of finished content to produce in one run. If a run genuinely cannot complete all 5 angles to full production quality in one pass, it must say so explicitly in the final report — exactly how many angles were fully completed, which are still pending, and why — rather than silently thinning out quality or skipping asset types to force-fit all 5. No silent caps.

---

## REAL DATA EXTRACTION — NO SYNTHESIS FALLBACK

Unchanged, most important rule in this spec: **never fabricate, estimate, or "research-based" substitute any data if a source is blocked or a tool is unavailable.** Stop that step and report the failure plainly in the final report instead.

---

## PHASE A: SIGNAL SCAN (articles + YouTube, one pass, expandable sources)

Read `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/CONTENT_SOURCE_WATCHLIST.md` for the current source list — **it is a seed list, not a ceiling.** Scan the listed article sites and YouTube channels every week, but also actively look for other credible Singapore property articles, news, and YouTube videos beyond that list. If a source outside the watchlist turns up repeatedly with strong signal, add it to the watchlist file with a one-line rationale and date — do not silently keep using an undocumented source, and never invent or guess a source's existence.

### A1 — Articles
Scan the watchlist's article sources plus a broader sweep (site: searches, Google News, SG property publication roundups) for the last 7 days.

### A2 — YouTube
For each watchlist channel plus any other relevant SG property YouTube channel found this week: pull the last 7 days of uploads, get the full transcript (captions, or the Browser pane — never estimate a transcript), publish date, view count if visible, hook (first 15s), core data points cited, structural format, CTA placement. This is real repurposing input, weighted the same as a strong article signal in Phase B.

### A3 — Signals
Google Trends (SG property keywords), Reddit r/singapore + r/singaporefi, HardwareZone forums, relevant Telegram/FB groups, YouTube comments on tracked videos, Google News alerts.

### Data quality rules
1. Only date-verified signals from the 7-day scan window (Monday–Sunday).
2. All source URLs kept and logged — every claim used downstream must be traceable back to one.
3. No repeat of an angle already ranked in last week's brief — check Section 0 of the prior week's Knowledge Vault file before finalizing.

---

## PHASE B: SCORE & RANK (6-step filter, unchanged)

For every signal — article or video — score 0–6:
1. REI Method alignment (R→E→I applicable)?
2. Client belief shift (addresses a false belief)?
3. Content gap (competitors covering this well already)?
4. Emotional hook (urgency/FOMO)?
5. SI-05 / Evergreen Authority relevance?
6. Proof/data available (citable)?

Keep only 6+ scored signals. Rank 1 = highest urgency + strongest proof + clearest REI fit. Aim for 3 news-triggered + 2 evergreen across the top 5.

---

## ALL 5 RANKED ANGLES GET FULL PRODUCTION

Every one of the top 5 ranked angles from Phase B gets the complete Phase C treatment below — full word-for-word script, article, carousel, single-image post, per-platform social posts, and WhatsApp segments. There is no brief-only tier. If time/tool constraints mean not all 5 can be finished to full quality in one run, finish as many as possible completely and report exactly which are done vs. pending in the final report — do not thin out quality across all 5 to force completion.

---

## PHASE C: FULL PRODUCTION FOR EACH RANKED ANGLE — WORD-FOR-WORD, NOT OUTLINES

Run this once per ranked angle (×5). Every asset below must be the finished version for that angle — synthesized across every source gathered for it this week, built to be the single highest-converting, attention-grabbing, scroll-stopping version of the angle, not a first draft. Every distinct claim or segment carries an inline citation — `[Source: <url>, accessed <date>]` — so it can be cross-referenced against the original later. This is not optional: it is what keeps multi-source synthesis honest and keeps this from becoming a rewrite of any single outlet's proprietary work (see Attribution Rule below).

Every asset must thread through the Second Property Ladder frame (Exit Before Entry, the 5 Moves — see `02_POSITIONING_AND_IP`) — this week's signal is the trigger/proof, not the subject. If a piece reads like a news recap with REI's name attached at the end, it has not passed this bar; rewrite it so the REI frame is what the piece is actually about.

### C1 — Long-form YouTube script (20–30 minutes)

Use `05_CONTENT_MARKETING_ENGINE/00_PRODUCTION_FOUNDATIONS/REI_Video_Production_Foundation_v1.2.md`, **Format 3B**. Full word-for-word script across all seven blocks (Hook+Promise, Mirror, Lie+Hard Truth, Reframe+Method, Proof, Implementation Depth, Soft Close), synthesizing the strongest material from every source gathered this week — not a single source rewritten. Score it against the Foundation's 100-point rubric before finalizing; **below 70 = revise, do not deliver as final.**

Mark the three short-form extraction ranges directly in the finished script per Format 3B's clip guide (Hook clip, Lie+Hard Truth clip, Reframe+Proof clip) — this is how one recording becomes the long-form upload plus its 3 short-form cutdowns, instead of scripting four videos separately.

### C2 — Full article

Complete word-for-word draft: title, full intro, full body (every section written out, not headers), conclusion, CTA. Inline source citations throughout. Ready to publish, not a brief for someone else to write from.

### C3 — Carousel (minimum 5 slides)

Full word-for-word copy for every slide (minimum 5). For each slide, also provide a ready-to-paste AI image-generation prompt — this automation cannot render images itself, so the prompt is the deliverable: subject/scene, composition and framing, exact text overlay (verbatim, with placement), visual style, aspect ratio (1:1 for feed carousel unless the platform calls for otherwise), and a note to pull palette/style reference from `01_ASSET_LIBRARY/01_APPROVED_LIBRARY/01_BRAND_KIT` before generating, so slides stay visually consistent with existing brand assets.

### C4 — Single-image quote/stat post

Same treatment as C3 but one slide: full copy + one ready-to-paste image-generation prompt.

### C5 — Social posts, per platform, full copy (this was missing from v2.2)

Write the actual caption for each of: Instagram, Facebook, LinkedIn, and TikTok/X (short-form caption variant). Each platform's post is written in that platform's native voice/length convention, not one caption copy-pasted four times. Reference the carousel/single-image asset from C3/C4 as the accompanying visual.

### C6 — WhatsApp broadcast (3 segments, full text, unchanged discipline from v2.2)

Segment 1 (high intent, existing/warm leads, "Reply AUDIT"), Segment 2 (medium intent, "Reply POSITION"), Segment 3 (cold, narrative only, video link). Full word-for-word text for all three — never mass-blast, never one generic message.

### Attribution & sourcing rule

When an angle draws on a specific outlet's proprietary analysis (e.g. a competitor's unit-level data breakdown), synthesize it through REI's own data/REI Method rather than rewriting their write-up, and cite it inline. Do not republish another outlet's original analysis in "our voice" with no reference back — this is a real copyright/reputational exposure, not a style preference, and it applies to every asset in this phase, not just the video.

### On-demand mode

Edmund or Cindior can request this same Phase A (scoped to one topic) + full Phase C production any day of the week — no need to wait for Monday. Same quality bar, same attribution rule, same full-production standard (not an outline) applies.

---

## LIBRARY & OUTPUT

**Weekly dated brief** (all 5 angles, each fully produced, in one file) → `H:\Shared drives\00_E.C.O.S\00_AI_OPERATING_SYSTEM\06_KNOWLEDGE_VAULT\01_MARKET_INTELLIGENCE\[WEEK] REI Weekly Brief — YYYY-MM-DD.md`.

**Growing pattern/angle library** (evergreen, not recreated weekly) → same Knowledge Vault folder, one running registry file — append, don't duplicate.

**Bi-weekly rollup** (only if 2+ weekly briefs exist) → same folder, `[ROLLUP] REI Bi-weekly Insights — YYYY-MM-DD.md`.

**Once Edmund picks the Rank-1 angle (or escalates a Rank 2-5 brief) to actually shoot** → that becomes its own workbench in `03_ACTIVE_CAMPAIGNS`, per the Content Studio desk rule — it does not stay in the Knowledge Vault brief.

---

## GITHUB BACKUP (unchanged from v2.2)

At the end of every run (weekly or on-demand):
```
cd "H:\Shared drives\00_E.C.O.S\00_AI_OPERATING_SYSTEM"
git add -A
git commit -m "Content brief: <date>"
git push origin main
```
If git reports "nothing to commit," skip silently. If push fails (auth/network), report the failure plainly — do not retry silently or drop the brief.

---

## CONSTRAINTS

1. No synthesis fallback — real data only, and every claim traceable to a source.
2. WhatsApp must always be segmented — never mass-blast.
3. No angle repeats from the prior week.
4. All 5 ranked angles get full production, word-for-word, every asset type in Phase C — no brief-only tier. If a run cannot complete all 5 to full quality, report exactly how many finished and what's pending rather than thinning out quality to force-fit all 5.
5. This automation does not render images. Every image need becomes a full, ready-to-paste generation prompt instead — never a vague "concept" description.
6. Ignore any folder outside the current live workspace map in root `CLAUDE.md` §2 — if a path referenced here looks stale, stop and flag it rather than guessing a replacement.

---

## CHANGELOG

**v2.4 (2026-07-30)** — Removed the Rank-1/Ranks-2-5 split: all 5 ranked angles now get full Phase C production every week. Added an explicit no-silent-caps rule for runs that can't finish all 5 in one pass.

**v2.3 (2026-07-30)** — Expandable source watchlist (not hardcoded); Format 3B (20-30 min) from Foundation v1.2 replaces invented Format A/B/C; full word-for-word production for every Rank-1 asset (script, article, carousel, single-image, per-platform social, WhatsApp) instead of outlines; inline source citations required throughout; AI image-generation prompts for every image need; Rank-1-full/Ranks-2-5-brief split to keep weekly volume realistic.

**v2.2 (2026-07-30)** — Merged YouTube into article scan as one signal pool; Phase A/B/C structure; corrected output path; retired Cowork; GitHub backup step.

**v2.1 (2026-07-11)** — Decision 067: removed Family Legacy/Mash-up/SI-06 classification.

**v2.0 (2026-06-20)** — Consolidated weekly brief + bi-weekly rollup; live Chrome automation requirement; conditional rollup.

**v1.0 (2026-06-15)** — Initial weekly brief task created.

## END REI WEEKLY CONTENT ENGINE v2.4
