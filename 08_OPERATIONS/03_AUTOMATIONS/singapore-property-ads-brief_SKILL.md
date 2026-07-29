---
name: singapore-property-ads-brief
description: Singapore property + adjacent-vertical ads intelligence. Pulls real active ads from Meta Ad Library via the in-app Browser pane (not the Chrome extension), downloads video/copy/thumbnail for ranked ads, transcribes locally, builds a weekly brief + bi-weekly rollup + advertiser swipe library.
---

<!--
AI OS MIGRATION HEADER — v2.0
Version: v2.0
Status: APPROVED MASTER
Date: 2026-07-29
Supersedes: v1.0 (2026-07-10, migrated unchanged 2026-07-16) — v1.0 never fired: it targeted the Claude-in-Chrome
extension against `facebook.com/ads/library/?...ad_type=political_and_issue_ads`, which (a) requires
per-domain browser-extension permissions never granted, and (b) scopes to political/issue ads only — the
one category commercial property/insurance/advisory ads are NOT in. Confirmed failure: see
`06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE` history / `_ARCHIVE/.../Weekly Ads/[2026-06-22] REI Ads
Intelligence — Data Collection Failure Report`. v2.0 fixes the tool, the URL scope, the scoring model,
and the destination paths (all pre-reorg in v1.0), and adds the video/transcript extraction phase that
v1.0 never had.
Sources: v1.0 file; 2026-07-29 live proof-of-method run (Stella Thio / Dunearn House, 10 ads, real download +
faster-whisper transcription, zero synthesis).
-->

TASK: SINGAPORE PROPERTY + ADJACENT-VERTICAL ADS INTELLIGENCE
Weekly Extraction + Brief, Bi-Weekly Rollup, Ongoing Advertiser Swipe Library
NO SYNTHESIS FALLBACK — if a step can't get real data, it stops and reports the failure. It never fabricates or estimates ad data to fill the gap.

═══════════════════════════════════════════════════════════════════════════════════
PHASE 0: SCOPE FOR THIS RUN
═══════════════════════════════════════════════════════════════════════════════════

Two independent scan modes, both run every week:

**A. Fixed watchlist** — named advertisers, checked every week for new/changed active ads.
Watchlist lives in: `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/COMPETITOR_WATCHLIST.md`
(seed: Stella Thio - Singapore Luxury Homes. Add advertisers as they're identified — do not guess names.)

**B. Keyword/project sweep** — catches advertisers not yet on the watchlist.
Run one Ad Library keyword search per entry in `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/SWEEP_KEYWORDS.md`
(seed: current SG launch names e.g. "Dunearn House"; property-adjacent verticals e.g. "Singapore property advisory",
"Singapore insurance advisor", "Singapore financial advisory" — expand only on explicit instruction, don't invent verticals).

═══════════════════════════════════════════════════════════════════════════════════
PHASE 1: DATA COLLECTION — PROVEN METHOD (use this exactly; do not substitute the Chrome extension)
═══════════════════════════════════════════════════════════════════════════════════

CRITICAL: Use the in-app **Browser pane** tools (`mcp__Claude_Browser__*`), NOT `Claude in Chrome`.
The Browser pane does not need a permission grant per domain and does not need the display compositing
that only `computer{action:"screenshot"}` requires — `read_page`, `get_page_text`, `javascript_tool`,
and `navigate` all work headless. This is what made real data collection possible on 2026-07-29 after
v1.0 failed outright.

Step 1A — Watchlist advertisers:
- `preview_start`/`navigate` to `https://www.facebook.com/ads/library/?active_status=active&country=SG&view_all_page_id=<if known>&q=<advertiser name>`
  or the advertiser's known Ad Library page if a stable link exists.
- `get_page_text` to capture full ad copy for every active ad shown (this alone got 100% of the ad copy,
  headline, CTA, description and "Started running" date in one call — no DOM parsing needed).

Step 1B — Keyword/project sweep:
- `navigate` to `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=SG&q=<keyword>&media_type=all`
  (NEVER use `ad_type=political_and_issue_ads` — that is the bug that killed v1.0).
- `get_page_text` per result page.

Step 1C — Per-ad video/image extraction (for every NEW ad ID not already in `SOURCE_REGISTRY`):
- `navigate` to `https://www.facebook.com/ads/library/?id=<library_id>` to isolate that ad in its own dialog.
- `javascript_tool`: read `document.querySelectorAll('[role="dialog"]')`, find the dialog whose
  `innerText` contains "Library ID:", grab its `<video>` element's `currentSrc`. (Static-image-only ads:
  grab the `<img>` inside that same dialog instead.)
- Folder name is **date-prefixed by first-seen date**: `<Advertiser>/<YYYY-MM-DD>_<library_id>/` — the date
  is when WE first captured it, set once, never changed on later runs (folder is never renamed). This is
  what makes "what's newest in this advertiser's swipe file" visible at a glance without opening any file.
- Download via `Bash: curl -sL -o video.mp4 "<src>"` — no auth/referer headers needed, confirmed working.
- Extract poster frame: `ffmpeg -y -i video.mp4 -ss 00:00:01 -frames:v 1 thumbnail.jpg`

Step 1D — Transcription (local, real, not estimated):
- `ffmpeg -i video.mp4 -ar 16000 -ac 1 -vn audio.wav`
- `faster-whisper` (`small`, CPU, int8) → timestamped transcript.
- ~5 min/video on this machine's CPU. **Only transcribe ads not already transcribed in a prior week**
  (check `SOURCE_REGISTRY/Master_Ad_Database.md` by library ID first) — this is the only way weekly
  runtime stays bounded as the watchlist grows.

Step 1E — Verification (replaces v1.0's "verify destination URL" step, which required navigating to
every destination and isn't necessary for copy/creative analysis):
- Confirm advertiser name + library ID + "Started running" date captured for every ad.
- Flag (don't silently drop) any ad where video/image extraction failed — report it, move on.

Output per ad: `[Advertiser]/[library_id]/video.mp4` or `image.jpg`, `thumbnail.jpg`, transcript, plus
the ad copy captured in Phase 1A/B text.

═══════════════════════════════════════════════════════════════════════════════════
PHASE 2: RANK & ANALYZE (fixes the v1.0 scoring model — see Watch Out below)
═══════════════════════════════════════════════════════════════════════════════════

Step 2A — Score every ad (0–10). Meta does NOT expose impression/reach numbers for commercial (non-political)
ads — only a binary "Low impression count: <100" flag. v1.0's Reach Score (">50K imp=2...") is not
obtainable and is retired. Use observable proxies instead:

| Dimension | 2 pts | 1.5 pts | 1 pt | 0.5 pt |
|---|---|---|---|---|
| **Longevity** (from "Started running" + still Active) | >4wk | 2–4wk | <2wk | Low-impression flagged |
| **Variant investment** (simultaneous scripts on same offer) | 3+ variants | 2 variants | 1 variant | — |
| **Cross-week recurrence** (appeared in a prior week's scan) | Sustained (2+ weeks) | New this week | — | Dropped since last week (0 pt — likely killed) |
| **Creative quality** (qualitative) | Professional | Adequate | Basic | Poor |
| **Psych trigger clarity** (qualitative) | Clear + strong | One clear | Weak | None |

Step 2B — For each ad, document: psychological trigger (fear/greed/FOMO/lifestyle/social proof/investment
logic), consumer angle, creative elements, hook type (first 0–15s), and — per advertiser with 2+ live
variants — what's constant (the reusable spine) vs. what's being tested (the hook).

Step 2C — Weekly brief: `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/[WEEK] REI Ads Brief — <date>.md`
(same content structure as v1.0 Step 2C: quick wins, ranked table, key insights, format breakdown,
trigger ranking, competitor highlights, new angles, data-integrity note with timestamp).

═══════════════════════════════════════════════════════════════════════════════════
PHASE 2B: UPDATE LIBRARY (weekly)
═══════════════════════════════════════════════════════════════════════════════════

Location: `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/ADS_LIBRARY/` (9 sections, same taxonomy as v1.0:
AdFormats, CompetitorIntel, BeliefBlockPlaybook, EvergreenAngles, PsychTriggerPatterns, CreatorPatterns,
CopyPatternLibrary, ContentGapMap, CaseStudyRegistry) + `SOURCE_REGISTRY/Master_Ad_Database.md` (every
ad ever processed, by library ID, with date first/last seen — this is the dedupe key for Step 1D and
Step 2A's recurrence score). Never delete entries; archive >6mo old into the section's own archive.

Raw creative (video/image/thumbnail/transcript) does NOT live in Knowledge Vault (no bulk media in the
AI OS — rule 9.7). It lives in `01_ASSET_LIBRARY/03_CREATIVE_INTELLIGENCE/03_EXTERNAL_REFERENCE_SWIPES/<Advertiser>/<YYYY-MM-DD>_<library_id>/`
(date = first-seen, set once), one folder per advertiser, new dated subfolders appended each week — an
existing dated `<library_id>` folder is NEVER re-downloaded, renamed, or overwritten once captured. The
library sections above only ever *link* to these files, never duplicate them.

**Advertiser-level `ad_breakdown.md`** (one per advertiser, at `<Advertiser>/ad_breakdown.md`): this is a
living document, not a per-run artifact. On a later scan that finds new ad IDs for an advertiser already
on file — APPEND, do not regenerate: add new rows to the per-ad table, add a dated note if the script/hook
pattern changed, and update the "known but not yet pulled" list if applicable. Never rewrite the existing
narrative/analysis sections for ads already documented — if new ads change the read (e.g. a new hook
angle emerges), add it as a new dated paragraph, don't silently edit prior conclusions.

═══════════════════════════════════════════════════════════════════════════════════
PHASE 3: BI-WEEKLY ROLLUP (conditional — unchanged logic from v1.0)
═══════════════════════════════════════════════════════════════════════════════════

If ≥2 weekly briefs exist: aggregate, trend across 6 dimensions (psych triggers, competitor intel,
creative/format, messaging, seasonal/macro, sustained-vs-emerging), produce:
- `[ROLLUP] REI Ads Rollup — Internal Brief — <date>.md` (Edmund + Cindior)
- `[DIGEST] REI Ads Digest — Team Share — <date>.md` (shareable)
Both in `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/`.
If <2 briefs: skip, log "Rollup: not yet (N briefs collected)".

═══════════════════════════════════════════════════════════════════════════════════
CRITICAL EXECUTION RULES
═══════════════════════════════════════════════════════════════════════════════════

- Browser pane tools only for Ad Library access. No Claude-in-Chrome. No web-fetch fallback.
- If Browser pane, curl, ffmpeg, or faster-whisper is unavailable: STOP and report exactly what failed —
  never substitute estimated/synthetic ad data. This is the single rule that mattered most in v1.0's failure.
- Quote ad copy verbatim. No paraphrasing.
- Incremental only: skip video download + transcription for any library ID already in Master_Ad_Database.
- Report actual runtime and ad count at the end — no silent caps. If volume is too high to fully process
  in one run, say exactly what was skipped and why.

═══════════════════════════════════════════════════════════════════════════════════
GITHUB BACKUP (added 2026-07-30)
═══════════════════════════════════════════════════════════════════════════════════

At the end of the run, after the weekly brief and library updates are saved:
```
cd "H:\Shared drives\00_E.C.O.S\00_AI_OPERATING_SYSTEM"
git add -A
git commit -m "Ads brief: <date>"
git push origin main
```
If git reports "nothing to commit," skip silently. If push fails (auth/network), report the failure plainly in the final report — do not retry silently or drop the brief. This is the only automated backup path for the AI OS brain (constitution, knowledge vault, automations) — Google Drive's own backup/archive layer covers everything else (bulk media, active campaigns, client data), which never goes to this git repo.

═══════════════════════════════════════════════════════════════════════════════════
OUTPUT CHECKLIST
═══════════════════════════════════════════════════════════════════════════════════

EVERY MONDAY:
✓ Watchlist advertisers scanned (Phase 1A)
✓ Keyword sweep run (Phase 1B)
✓ New ad IDs (vs. Master_Ad_Database) had video/image + thumbnail downloaded to Asset Library (Phase 1C)
✓ New ad IDs transcribed locally (Phase 1D)
✓ All ads scored + ranked (Phase 2A) with the fixed proxy model, not the retired Reach Score
✓ Weekly brief written to Knowledge Vault
✓ 9 library sections + Source Registry updated
✓ Data-integrity note states real extraction timestamp, not "synthesis"
✓ GitHub backup committed + pushed (or failure reported plainly)

EVERY OTHER MONDAY (if 2+ briefs exist): bi-weekly rollup + team digest produced.

FINAL REPORT: [Date/time SGT] | [# ads found: watchlist X / sweep Y] | [# new ads processed vs. skipped-as-duplicate]
| [# video/transcript extractions: success/failed] | [Top 3 trends] | [Library sections updated: X/9]
| [Rollup: YES/NO] | [GitHub backup: pushed/failed] | [Any step that failed and what was skipped]
