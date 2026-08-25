---
name: rei-ads-scan
description: On-demand pull of a specific advertiser's active Meta ads (Singapore) — real ad copy, video/image download, thumbnail, local transcription. Use when Edmund names an advertiser and wants their current ads extracted right now. Distinct from the scheduled Cloud routine "Weekly Ads Intelligence" at claude.ai/code/routines, which uses the Meta Ads API instead — the Cloud sandbox has no browser-control tool available, so it cannot do what this skill does. This is the on-demand counterpart, same relationship as `/rei-video-routine` is to "Weekly Content Intelligence".
---

# /rei-ads-scan — pull one advertiser's active ads on demand

**Scope:** a single advertiser (or a short named list), on-demand, same-session. Not the scheduled weekly system.

**Why we scan advertisers OUTSIDE property (standing rule, confirmed 2026-07-31):** the goal is to source strong *marketing angles, hooks, and funnel mechanics* to repurpose INTO property/Second Property Ladder content — the source vertical does not matter. Sales coaches, marketing agencies, AI tools, trading/wealth education, high-ticket coaching, training programs are all valid and valuable targets. Do NOT dismiss a cross-vertical advertiser as "low priority because it's not property" — a great story hook or belief-reframe from a trading-education ad translates directly to a One-Property-Trap ad. When logging a cross-vertical advertiser, capture the transferable ANGLE (the hook structure, the belief shift, the funnel move) and note how it could map onto property, not just "cross-vertical, not property."

Advertiser name (required): `$ARGUMENTS`

## 1. Check for existing data first

Look up the advertiser in `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/ADS_LIBRARY/SOURCE_REGISTRY/Master_Ad_Database.md` and `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/COMPETITOR_WATCHLIST.md`. If already marked COMPLETE with no reason to expect new ads, say so and ask whether to re-check for new ad IDs or skip. Never re-download or re-transcribe an ad ID already logged there — check by library ID first, every time.

## 2. Extract via the in-app Browser pane (proven method — never the Claude-in-Chrome extension, that was v1.0's documented failure mode)

- Navigate: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=SG&q=<name>&search_type=page`
- `get_page_text` captures full ad copy, headline, CTA, and "Started running" date for every ad shown — no DOM parsing needed.
- **Defeating the pagination ceiling (discovered 2026-07-31 — this beats the limit that capped Marc Chan/Dan Lok at ~28-30):** the Browser pane isn't visually composited, so Facebook's scroll-triggered infinite-load does NOT fire on plain `window.scrollTo` alone. Instead, in a `javascript_tool` loop, EACH iteration: `window.dispatchEvent(new Event('scroll'))` + `window.dispatchEvent(new Event('resize'))`, then `window.scrollTo(0, document.body.scrollHeight)`, then find all elements whose trimmed text is exactly `"See more"` and `.click()` the LAST one (the load-more trigger at the page tail), then wait ~1.4s. Loop until the distinct `Library ID` count stops growing for ~8 iterations. This loaded 110 of ~120 cards for Freedom Growth Academy where plain scrolling was stuck at 28. If a JS return exceeds the tool's token cap, it's saved to a file — parse it with `python`/`json.JSONDecoder().raw_decode()` (the inner text has a trailing note, so `raw_decode` not `json.loads`).
- Per-ad video/image: navigate to `...?id=<library_id>` (keep the rest of the query string, e.g. `q=`/`view_all_page_id=`), then `javascript_tool` to find the `[role="dialog"]` whose innerText contains `Library ID: <id>`, and grab its `<video>` `currentSrc`/`duration` (or `<img>` src for static ads).
- **Static/image ads get downloaded too, not just logged** — every distinct ad's creative is saved, video ads as `.mp4` and static ads as `.jpg`. The number of saved creatives must equal the number of distinct ads in the registry (learned 2026-07-30: first live run logged 10 static ads' copy but skipped their images — Edmund caught it). Batch tip: all static images can be grabbed in ONE `javascript_tool` pass on the search-results page (walk text nodes for `Library ID:`, climb to each card's container, take its largest `<img>` src) — no need for 10 separate per-ID navigations.
- Download: `curl -sL -o video.mp4 "<src>"` — no auth/referer headers needed, the signed CDN URL is enough.
- Thumbnail: `ffmpeg -y -i video.mp4 -ss 00:00:01 -frames:v 1 thumbnail.jpg`.
- Transcribe: `ffmpeg -i video.mp4 -ar 16000 -ac 1 -vn audio.wav`, then local `faster-whisper` (`WhisperModel("small", device="cpu", compute_type="int8")`). For non-English creative, omit the `language` param and let it auto-detect — never force `language="en"`.
- Run transcription as a **backgrounded Bash command** (`run_in_background: true`) — never block/sleep waiting on it.

## 3. Standing policies — identical to the weekly system, do not relax them because this is on-demand

- **APPEND-ONLY REFRESH (STANDING RULE, Edmund 2026-08-06 / Decision 124):** every advertiser already in the swipe library is RE-SCANNED and auto-refreshed — on the weekly run and whenever re-supplied on demand — so the folder accumulates over time. On a refresh: load the advertiser's current active ads, diff their library IDs against what's already in `Master_Ad_Database.md`, and download + transcribe ONLY the NEW IDs (add them to the existing folder). **NEVER delete, overwrite, or re-date previously captured assets** — an ad that has since gone inactive stays in the folder as a historical asset; mark it "no longer active" in the registry rather than removing it. The library only grows. Existing `<date>_<id>` files keep their original first-seen date; new ones get today's date. Report per-advertiser: N already had, M new added, K now inactive-but-retained.

- **Folder structure (reorganized 2026-07-30 — media-type folders, NOT one-folder-per-ad):** under `01_ASSET_LIBRARY/03_CREATIVE_INTELLIGENCE/03_EXTERNAL_REFERENCE_SWIPES/<Advertiser>/`, save each creative into its type folder, named `<YYYY-MM-DD>_<library_id>.<ext>`:
  - video → `01_VIDEOS/<date>_<id>.mp4`
  - static image → `02_IMAGES/<date>_<id>.jpg`
  - video thumbnail (ffmpeg) → `03_THUMBNAILS/<date>_<id>.jpg`
  - transcript (faster-whisper) → `04_TRANSCRIPTS/<date>_<id>.txt`
  Date = first-seen/capture date, set once, never renamed on later runs. The date prefix makes newest sort to the top by filename. Do NOT recreate the old `<date>_<id>/` per-ad subfolders — that's the structure this replaced (it made browsing require opening every folder). Do not keep `audio.wav` intermediates — regenerable from the retained `.mp4` via ffmpeg in seconds.
  - After the scan, regenerate the library index: `python "01_ASSET_LIBRARY/03_CREATIVE_INTELLIGENCE/03_EXTERNAL_REFERENCE_SWIPES/build_index.py"` (rewrites `_MASTER_INDEX.md` with fresh counts + latest-scan dates).
- **Length cap:** any single ad video over ~10 minutes gets copy/duration logged only, never downloaded or transcribed — state this explicitly, never silently drop it.
- **Dedupe:** when Meta flags shared creative/duplicate IDs with identical body copy, only ONE representative per distinct script gets the video/audio treatment. Log every duplicate ID in `Master_Ad_Database.md` as "dup, not downloaded."
- **Append-only `ad_breakdown.md`** per advertiser, at `<Advertiser>/ad_breakdown.md`. Never rewrite existing analysis — new ads become new dated rows/paragraphs.
- **No synthesis fallback:** if the Browser pane, curl, ffmpeg, or faster-whisper is unavailable, stop and report exactly what failed. Never fabricate or estimate ad data. Quote ad copy verbatim, never paraphrase.
- **Same registries as the weekly system, not a separate on-demand log:** update `Master_Ad_Database.md` and `COMPETITOR_WATCHLIST.md` with whatever's found — one source of truth for "what's been processed," whether it came from this skill or the scheduled routine.

## 4. WEEKLY FULL-LIBRARY SWEEP (STANDING, Edmund 2026-08-06 / Decision 125)

This skill is not only for a single named advertiser — it is also the **browser-side half of the weekly Ads Intelligence cycle**. The Cloud "Weekly Ads Intelligence" routine (Meta API) runs Monday but is network-blocked from facebook.com, so it can only produce metadata (page IDs, headlines, new library-IDs) — it CANNOT download media/transcribe. That media-download + transcription half MUST run here (a browser-capable session). Run this full sweep weekly (Edmund triggers it, or on request), ideally right after the Cloud routine's Monday run:

1. **Refresh every advertiser already in the library** (append-only, Decision 124). For each folder under `03_EXTERNAL_REFERENCE_SWIPES/<Advertiser>/`: get its page ID (from the folder's `_ad_breakdown.md` header or `Master_Ad_Database.md`), load the live page, diff current active library-IDs against the files already in `01_VIDEOS`/`02_IMAGES`, and download+transcribe ONLY the new distinct creatives. Never delete; an ad gone inactive stays and is marked "no longer active." Report per advertiser: N had / M new / K now-inactive-retained.
2. **Fill Cloud scaffolds.** Any folder whose `_ad_breakdown.md` says "media not yet downloaded" / "PENDING EXTRACTION" is a metadata-only scaffold the Cloud routine created for a NEW relevant advertiser it found. Extract its media (page ID is in the scaffold header) and update the note.
3. **Pull the Cloud routine's new-advertiser list.** Read the latest Cloud "Weekly Ads Intelligence" report/PR (or its `data/` output) for advertisers it flagged as new/relevant that don't have a folder yet — property competitors AND cross-vertical angle sources per Decision 120 — and run each through the standard §2 extraction. If the report isn't reachable, still do steps 1, 2, 4.
4. **Integrity repair (do every sweep):** every `.mp4` must have a matching `03_THUMBNAILS/<id>.jpg` (regenerate with ffmpeg if missing) and a `04_TRANSCRIPTS/<id>.txt` (regenerate from the retained mp4 if missing — this catches transcripts lost in past folder moves). No leftover `.wav`. Then regenerate `_MASTER_INDEX.md` via `build_index.py`.
5. **Commit** the git-tracked registry/watchlist/decision-memory changes (media/index/breakdowns are Drive-only per Decision 118). If the push is rejected, `git pull --rebase` then push.

Reusable helper scripts live in the session scratchpad pattern (`dl_videos.py` = download+thumb+audio deduped by CDN filename; `dl_imgs.py`; `tx_folder.py` / `tx_missing_all.py` = whisper, force `language=en` except known non-English advertisers Abc Sales AI / Thomas Yap). Path note: Windows Python needs `H:/...` not git-bash `/h/...`; write scratchpad JSON to a `/c/Users/.../scratchpad` path both agree on; keep FULL untrimmed signed CDN URLs (trimming `efg`/`_nc_*` params → 403).

## 5. Output

Report: advertiser name, total ads found, how many are new vs. already logged, how many downloaded/transcribed vs. skipped (length cap / duplicate) and why, any tool failures encountered, and the exact folder path(s) where files landed. For a full-library sweep, also report: advertisers refreshed with new creatives, scaffolds filled, new advertisers added, and any thumbnail/transcript gaps repaired.
