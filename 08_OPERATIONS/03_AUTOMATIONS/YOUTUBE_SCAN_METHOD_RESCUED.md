---
name: youtube-scan-method
description: "How to reliably scan Tier 2 YouTube channels for the REI Monday content agent — RSS first, channel pages return metadata only"
metadata: 
  node_type: memory
  type: project
  originSessionId: ca391c1c-ae09-4cdc-8163-b8884dedc132
---

For the REI Monday Content Intelligence Agent runs: YouTube channel /videos pages fetched via web_fetch return only channel About-metadata (no video list). Each page does expose the channel's RSS feed URL (https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID), which lists the latest ~15 uploads with exact dates.

**Why:** On 2026-06-12 the upload-level scan failed entirely (RSS feeds timed out that day too); the brief had to honestly mark all Tier 2 YouTube channels "not verifiable this run."

**How to apply:** Try RSS feeds EARLY in each run with retries. Known IDs: Marcus Luah UCsBykziko5f-FOki0K1GKQw, JNA UCZadT9cUz_mQkXnZ-uiTO1Q, Edmund's own channel UC12TZzfi-FetecybXqWdOqg. Also: @AaronLin is a Roblox channel — the catalog's Aaron Lin handle is wrong and needs correcting. Catalog v4 records all of this in the Tier 2 scanning-method note. Related: [[rei-catalog-fetch-quirks]]
