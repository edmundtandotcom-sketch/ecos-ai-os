---
name: yt-repurpose-scan
description: On-demand scan of the Singapore property YouTube competitor roster (or a given topic) for time-sensitive videos worth repurposing, transcribed and mined for talking points, then rebuilt into an upgraded Second Property Ladder script. Use when Edmund types /yt-repurpose-scan, asks what's trending/hot in SG property YouTube right now, or gives a topic and wants to see what competitors are saying about it before scripting.
---

# /yt-repurpose-scan — competitor scan → transcript-mine → upgraded script

Topic (optional): `$ARGUMENTS`. On-demand only — this does not run on a schedule; it runs when invoked.

Two entry modes. Decide which one applies before doing anything else:
- **Topic given** — a subject, project, or news item was named.
- **Blank scan** — no topic; the ask is "what's hot right now."

## 1. Load the roster
Read `Competitor_Channel_Roster_v1.0.md` in this same folder. **There is no active vidiq subscription (confirmed 2026-07-30) — treat vidiq as opportunistic-only everywhere in this skill, never as the planned path.** If any channel is marked `TBD`, resolve it via the Browser pane: search `https://www.youtube.com/results?search_query=<channel name> singapore property`, open the top matching channel result, and read its handle from the URL (`/@handle`). Write the resolved handle back into the roster file so future runs skip the lookup. Never scan the excluded channel. Never scan the own-channel row as a competitor source.

## 2. Find candidates (cheap pass — no transcripts yet)
**Primary path — browser search, both modes (proven live, 2026-07-29/30):**
- **Topic mode:** open the Browser pane at `https://www.youtube.com/results?search_query=<topic terms>`. Use `get_page_text` / `read_page` to pull title, channel, view count, and age for each result; construct the video URL from the `/watch?v=<id>` or `/shorts/<id>` href. Cross-reference results against the roster (§1) to flag which hits are on channels Edmund already tracks vs. new to the roster (§1's "adding a new channel" note).
- **Blank scan mode:** since there's no single keyword, run 3-4 searches with genuinely different phrasings (e.g. `"singapore property news"`, `"singapore property market update"`, plus 1-2 on whatever's recurring in recent sessions/memory), sorted by upload date (append `&sp=CAISAhAB` to the search URL). **Confirmed live 2026-07-30: different seed phrases return substantially different result sets — one search missed the single biggest story of the week entirely while another surfaced it prominently.** This is not a true trending-detection pass; it's a phrase-dependent spot-check, and it will miss real stories if the seed phrasing doesn't happen to match how creators titled their videos. Say this plainly in the output every time, don't let it read as equivalent to a real "scanned everything" claim. More seed phrases genuinely helps — don't stop at one and call the scan complete.
- Cap at the top 5 candidates. For each: title, channel, video URL, published date, views/age, and a one-line read on *why* it's worth a look.

**Opportunistic only — vidiq, if a subscription happens to be active:** check `vidiq_balance` first (free) before spending any other vidiq call. If credits exist, `vidiq_outliers` (channelIds = roster, plus `keyword` for topic mode, `publishedWithin: thisWeek`/`thisMonth`, sorted by `breakoutScore`/`vph`) gives a genuinely better trending signal than browser search and is worth using *in addition to*, not instead of, the browser pass. Never let a vidiq step block the run — if it fails or the balance is 0, that's expected, not an error to fix; proceed on the browser path alone.

## 3. Shortlist checkpoint
Present the ranked shortlist. Pulling a transcript and building a full script is the expensive, slow step — don't spend it on the wrong video. Two exceptions where this checkpoint is skipped:
- `$ARGUMENTS` was already a specific video URL or an unambiguous single topic with one clear best match.
- Only one candidate came back.
Otherwise, confirm which candidate(s) to take forward before continuing.

**Once confirmed, mine all of them.** Do not silently narrow the confirmed list down to "the best 2" for speed or token cost — that decision belongs to Edmund, not to a unilateral efficiency call made mid-run. If a real constraint (API credits, a genuinely dead/thin source) means fewer get mined, say so explicitly and why, don't just quietly do less than what was confirmed.

## 4. Transcript-mine every confirmed video
For each confirmed video: pull the transcript via the browser (primary path — open the video, expand the description, click "Show transcript," read it via `get_page_text`; free, no subscription needed, proven reliable). Only use `vidiq_video_transcript` opportunistically if a subscription happens to be active and it's genuinely faster than the browser path — don't plan around it. Pull stats via the browser (views/age already visible on the video page) rather than `vidiq_video_stats`. Extract, don't summarize generically:
- **Hook/open** — exactly how the first 15-30 seconds earns attention (and whether it's actually good or just got lucky on topic timing)
- **Teaching structure** — the real content/value delivered, and any named framework or numbered system used
- **Authority signals** — credentials, case specifics, data points, confident claims that build trust
- **Objection-handling / proof** — anything that pre-empts skepticism
- **CTA mechanics** — how and when they ask for the next step
- **Gaps** — where it's thin, generic, unverified, or where a REI-Method-trained advisor would add something this creator can't

Flag every factual claim (numbers, thresholds, project details, policy specifics) for verification — a competitor's numbers are not ground truth, even when two competitors happen to agree (that's corroboration, not proof — still trace it to a primary source where one exists). Cross-check against primary sources before reusing any of them, same discipline as `/yt-second-property-script` step 2. Label opinion/speculation from a source as opinion, explicitly, if it's used at all — don't let a creator's stated guess read as fact.

**If a video has no transcript** (captions disabled — check the player's captions-button state, don't assume): the only real fallback is downloading the audio and running it through separate speech-to-text tooling. That is a file download, which needs Edmund's explicit go-ahead before it happens, and the STT tooling's availability on the machine isn't guaranteed — don't assume it works. Default to noting the video as source-unavailable and moving on; only pursue the download+STT path if the source is clearly high-value enough to justify asking, not for a thin/low-engagement video that just happens to be on the roster.

## 5. Build the upgraded script
Hand off to the same build discipline as `/yt-second-property-script` (read that skill's steps 3-5 if unclear):
- Blueprint source: `01_SOURCE_REFERENCES/The Second Property Ladder x One-Property Trap - FINAL CATEGORY KING HANDOVER BLUEPRINT.docx` — apply only where the mined talking points genuinely map to it; don't force a fit.
- Structure: `YouTube_LongForm_Script_Framework_and_Checklist_v1.0.md` in this same folder, applied in full.
- Voice: `marketer-copywriter-persona` standing mode — psychology-led, conversion-first, direct-response.
- This is a **rebuild, not a repurpose-by-copying.** Reuse the talking points and the gap analysis from step 4, not the competitor's phrasing or sentence structure — write it in Edmund's structure and voice, close the specific gaps found in step 4 (length, teaching depth, evergreen framing per [[sg-property-youtube-competitive-landscape]]'s structural-gap findings), and never reproduce more than a short attributed quote of the source transcript.
- **Every fact, data point, or structural beat in the script gets an inline source tag** — e.g. `[CNA/Chee Hong Tat]`, `[Yvette Huang]`, `[blueprint §15]`, `[original]` for anything that's genuinely new synthesis, not traceable to a single mined source. This is a permanent requirement, not a one-off: Edmund needs to know at a glance what's verified-primary, what's competitor-sourced, what's opinion, and what's this skill's own construction, without re-deriving it from a separate talking-points list.

## 6. Self-grade
Grade against the 5 most relevant criteria: grounding in real (verified) data, teaching depth vs. information, blueprint alignment, retention-framework fidelity, and originality (genuinely rebuilt, not a close paraphrase of the source). State one-line critiques for anything short of a 10, revise before presenting.

## 7. Output
1. **Sources used** — title, channel, URL, publish date for every video pulled into step 4, including any that were confirmed but yielded no usable transcript (state why).
2. **Talking points extracted** — the step 4 breakdown, labeled by source video.
3. **Full script** — word-for-word, with the inline per-beat source tags from step 5, timing/word-count table.
4. Note the topic/scan basis so a future run doesn't need this process re-explained.
