Title: Swipe-Library Page-ID Registry — the refresh target list
Status: REGISTRY (single source of truth for `view_all_page_id` per swipe folder)
Created: 2026-08-29 (Decision 128 follow-up — folders were going stale because page IDs were scattered/missing across breakdown docs; the weekly refresh had nothing reliable to iterate)

## How this is used
Every weekly refresh (and every `/rei-ads-scan` catch-up) iterates THIS list: for each folder, navigate `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=SG&view_all_page_id=<ID>&media_type=all` (use country=ALL for the MY/global advertisers noted below), pull the age-filtered NEW videos + the s600 static images, append-only. A folder with no ID here CANNOT be auto-refreshed — resolve its ID and add it before the next run.

## Resolved page IDs
| Folder | view_all_page_id | Notes |
|---|---|---|
| Adrian Lee | 2008367132748627 | 3 active 2026-09-28; all creatives >=35d, 0 new |
| Allan Khazak | 1190372650834809 | image-heavy; still 0 active (re-checked 2026-09-28) |
| Beyond Realtors Club | 1159884363865127 | 34 active 2026-09-28 (full load); +4 statics |
| Caleb Sim | 106092578729020 | HIGH activity; 37 active 2026-09-28 (full load); **+12 videos** (fresh 5-6d wave) + 1 static |
| CP Homes | 104268712429679 | direct competitor (decoupling); 2 active 2026-09-28, **+1 video (8d)** |
| Dan Lok | 998837360158985 | has >10min VSLs (length-cap); 31 active 2026-09-28 (full load), 0 new (2 statics byte-identical) |
| Damien Tan Real Estate | 101766852110723 | resolved 2026-08-29; 7 active 2026-09-28, **+3 videos** |
| Denise Tan | 107119960679980 | direct competitor; 36 active 2026-09-28 (full load), 0 new |
| Eddy Miranda | 663968926972914 | image-only. **REACTIVATED 2026-09-28** - 34 active, +26 statics |
| Entrepedia | 110261508293707 | image-only. **REACTIVATED 2026-09-28** - 31 active, +1 static (other 30 already on disk) |
| Ernee Ong (Proptiply) | 322490897609800 | resolved 2026-08-29; HIGH activity; 56 of ~58 active 2026-09-28 (full load); +9 short (4-11s) visual clips + 3 statics |
| Frank Kern | 137568852956377 | still 0 active (re-checked 2026-09-28) |
| Growth Partners Inc | 872538235944011 | resolved 2026-08-29; image-heavy. **0 active as of 2026-09-28 (campaign ENDED; was 26 on 09-21)** - re-checked twice, page resolves normally |
| I Quadrant | 187151448541930 | resolved 2026-08-29; 18 active 2026-09-28 (carousels), +8 distinct carousel cards |
| Issac Liu | 1052372747963934 | video-led; 10 active 2026-09-28, 0 new (4 videos byte-identical to 2026-09-14 under rotated IDs) |
| King Kong Co (Sabri Suby) | 562378543780840 | cross-vertical; >10min VSLs logged-only. 59 of ~62 active 2026-09-28 (full load), +1 video; 2 over-cap VSLs logged |
| Legacy Advisors Academy | 102969409387188 | **0 active as of 2026-09-28 (campaign ENDED; was 14)** - also 0 under country=ALL |
| M H Simon | 104247242216764 | 6 active 2026-09-28, 0 new |
| Marc Chan | 442189845653421 | **REACTIVATED 2026-09-28** - 36 active (image-only wave), +33 statics |
| Patricia Ang Real Estate | 533704976500523 | **REACTIVATED 2026-09-28** - 2 active, both older creatives (>=35d), 0 new |
| Peng Joon | 143408239118491 | country=ALL. 151 of ~160 active 2026-09-28 (full load); +2 videos + 5 statics (81 pulled, 76 byte-identical) |
| Property Exit Advantage Singapore | 1190078307520774 | still 0 active (re-checked 2026-09-28) |
| Real Estate Mentor | 1018912674640670 | image-only; 2 active 2026-09-28, +1 static |
| Rodney Tan | 114028770064802 | direct competitor. **REACTIVATED 2026-09-28** - 6 active, +5 statics |
| Sarah Lee | 615849231608268 | still 0 active (re-confirmed 2026-09-28) |
| Stella Thio - Singapore Luxury Homes | 101446268410106 | resolved 2026-08-29; 37 active 2026-09-28 (full load); **+12 videos** + 1 static (21 pulled, 9 byte-identical) |
| The Freedom Growth Academy | 297816853407449 | 93 of ~99 active 2026-09-28 (full load); +6 videos + 1 static; 1 over-cap VSL logged |
| The Investor Realtor | 108170522131032 | direct competitor; 12 active 2026-09-28, +1 video (3 byte-identical) |
| The Right Move | 166518753916616 | direct competitor; 9 active 2026-09-28, 0 new |
| Thomas Yap | 2270869307018514 | country=ALL; still INACTIVE (re-checked 2026-09-28) |
| FNX Marketing By Finix Group | 1286193024567598 | orig page 1286193024567598 still 0 ads. **FNX Advertising 1252511721279349: 0 active 2026-09-28 (ENDED; was 3)** |
| Abc Sales AI | 460789450460649 | resolved 2026-09-07; non-English creative -> whisper auto-detect. 20 active 2026-09-28, 0 new |
| Authentic Advisory Systems | 100639661930725 | resolved 2026-09-07; HIGH activity, extreme re-upload. 37 active 2026-09-28 (full load); 15 pulled -> **+3 distinct scripts** (5 byte-identical, 7 script re-encodes) |
| Colin Ee | 102418822374465 | resolved 2026-09-07; direct competitor. 6 active 2026-09-28, +2 statics |
| Cynric Ho | 239864660126575 | resolved 2026-09-07; direct competitor. **REACTIVATED 2026-09-28** - 6 active, **+4 videos (4-5d)** (2 byte-identical to 09-07) |
| Erik Hoffmann | 619905461807712 | resolved 2026-09-07; image-heavy; 8 active 2026-09-28, 0 new (all 4 candidates byte-identical) |
| Jason Evonne Property | 108343127407869 | resolved 2026-09-07; direct competitor, image-only; 1 active 2026-09-28, 0 new |
| Jo Tan | 896274166903494 | resolved 2026-09-07; page name "Jo Tan Real Estate"; direct competitor; 1 active 2026-09-28, 0 new |
| KS Tan | 110637458587684 | resolved 2026-09-07; page name "KS TAN - Real Estate Strategist"; 29 active 2026-09-28, **+9 videos (4-6d, new video wave)** |
| Miles Stutz | 226368730568005 | resolved 2026-09-07; 17 active 2026-09-28, +1 static + 1 short (7s) video |
| Networth Builders | 132637119929833 | resolved 2026-09-07; page name "Networth Prop"; 1 active 2026-09-28, 0 new |
| Raymondlim.rlc | 602457776286259 | resolved 2026-09-07; 2 active 2026-09-28, +1 video (5d) |
| Xccelerate Academy | 102308099542618 | resolved 2026-09-07. **0 active (ENDED 2026-09-14, still ended 2026-09-28)** |
| Live A Home SG | 103133488962134 | added 2026-09-13; DIRECT competitor (presenter "Kelly"); new-launch webinar funnel (Thomson Reserve). **0 active as of 2026-09-28 (campaign ENDED; was 3)** |
| Flexionmarketing | 1190074440850416 | resolved 2026-09-14; 30 active 2026-09-28 (full load, a genuine 30), +1 video (3 videos + 8 statics byte-identical) |
| Success Resources | 550751965021284 | resolved 2026-09-28 (ID was already in the folder's `_ad_breakdown.md` header; confirmed as the dominant "Success Resources" page on an exact-phrase search - other same-named pages exist: 629197097193241, 192780607432011, CN 688585221000651). 12 active 2026-09-28, +3 videos + 6 statics (1 image 403'd: 1397583722348268) |
| Escape Uncertainty | 559289110600596 | resolved 2026-09-28 (from `_ad_breakdown.md` header). 0 active 2026-09-28 |
| Future Adviser Sg | 1052806307905338 | resolved 2026-09-28 (from `_ad_breakdown.md` header). 10 active 2026-09-28, 0 new media |
| Leads SG | 1851368671745396 | resolved 2026-09-28 (from `_ad_breakdown.md` header). 0 active 2026-09-28 |
| The Producer Formula | 840716469132393 | resolved 2026-09-28 (from `_ad_breakdown.md` header). 6 active 2026-09-28, **+5 videos (2-9d, fresh wave)** + 1 static |

## UNRESOLVED — page ID needs capturing before these can be auto-refreshed
**None as of 2026-09-28.** All 5 names carried since 2026-09-14 were resolved this run — every one of their IDs was already written in
the folder's own `_ad_breakdown.md` header line (`page-ID <digits>`). **Check that header first** before any keyword-search resolution.

Resolution method if a new folder ever lacks an ID: load
`https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=SG&q=%22<name>%22&search_type=keyword_exact_phrase&media_type=all`
(exact-phrase, quoted — far cleaner than `keyword_unordered`) and pair `"page_id":"<digits>"` with the nearest `"page_name":"..."`; if
several pages share the name, pick the one carrying the most `ad_archive_id`s in that result.

## Changelog
- **2026-09-07** — weekly `rei-swipe-weekly-refresh` run: 12 of 18 unresolved page IDs resolved and added above; Peng Joon reactivated; Marc Chan / Growth Partners Inc / Frank Kern / Adrian Lee / Allan Khazak / Property Exit Advantage / Sarah Lee / Thomas Yap / FNX (both pages) confirmed 0-active. Registry now holds 43 resolved IDs.
- **2026-09-14** - weekly `rei-swipe-weekly-refresh` run: Flexionmarketing page ID resolved (44 -> 45 resolved IDs, 5 still unresolved).
  REACTIVATED: Growth Partners Inc, FNX Advertising, Adrian Lee (no new media). ENDED: King Kong Co, Colin Ee, Xccelerate Academy, Peng Joon.
  Issac Liu switched from image-only to video-led. Still 0-active: Allan Khazak, Frank Kern, Marc Chan, Property Exit Advantage, Sarah Lee, Thomas Yap, Eddy Miranda, FNX Marketing (orig page).
  **Extraction note:** the documented `s60x60` -> `s600x600` stp rewrite now returns HTTP 403 "URL signature mismatch" - Meta tightened
  per-URL signature validation. Prefer the unresized `original_image_url` (no `stp=` param, full resolution), then a *natively-served*
  `s600x600` URL; never rewrite the stp parameter. Bases that exist only at `s60x60` are skipped (60px thumbnails, not creatives).
  **Video URLs** must come from the rendered DOM - the server-rendered JSON payload carries unsigned `video_hd_url`s that 403 with "Bad URL hash".
- **2026-09-21** - weekly `rei-swipe-weekly-refresh` run: 45 resolved IDs re-checked (46 page loads incl. both FNX pages); still 5 unresolved.
  **+4 distinct videos / +142 static images** appended (26 videos and 246 images were pulled, then collapsed by the dedupe rules: 22 videos matched an
  existing script and 104 images were byte-identical). REACTIVATED: King Kong Co, Colin Ee, Peng Joon. ENDED: Cynric Ho, Rodney Tan, Patricia Ang Real Estate, Eddy Miranda, Entrepedia.
  Still 0-active: Allan Khazak, Frank Kern, Marc Chan, Property Exit Advantage, Sarah Lee, Thomas Yap, Xccelerate Academy, FNX Marketing (orig page).
  **ENVIRONMENT CHANGE - the load-more loop is no longer available.** `static.xx.fbcdn.net` now serves every `rsrc.php` JS/CSS bundle with
  `cross-origin-resource-policy: same-origin` and **no** `Access-Control-Allow-Origin`, so facebook.com's React app cannot hydrate in either the
  in-app Browser pane or Playwright (identical CORS/CORP failures in both -> it is network-level, not browser-specific). A plain `curl` of the Ad
  Library returns an HTTP 403 `__rd_verify_...?challenge=3` bot-detection interstitial. Consequence: **no rendered DOM, no "See more" load-more loop,
  so the server-rendered payload's 30-ad cap is a hard ceiling this run.** Folders showing exactly 30 active may have more.
  **CORRECTION to the 2026-09-14 note - payload video URLs DO work.** `video_hd_url`/`video_sd_url` from the server-rendered JSON downloaded fine for
  all 27 attempted assets (0 failures, 1.7-26 MB each). The 403 "Bad URL hash" seen previously reproduces only on *stale* assets (a 226-day-old Adrian
  Lee URL); every asset under the 35-day age filter succeeded. Since the age filter is exactly what the weekly pull uses, **the whole video pull now works
  without hydration** - the rendered DOM is not required. Static image URLs in the payload remain signed and valid (full-res `original_image_url`,
  often 1080x1350-1649x2048), so the `s600x600` preference is moot when no-`stp=` originals are present.
- **2026-09-28** - weekly `rei-swipe-weekly-refresh` run: all 45 resolved IDs + both FNX pages re-checked, **and the last 5 UNRESOLVED
  resolved** (Success Resources, Escape Uncertainty, Future Adviser Sg, Leads SG, The Producer Formula - IDs were in each folder's
  `_ad_breakdown.md` header). Registry now 50 resolved / 0 unresolved.
  **Hydration is BACK** - the Ad Library React app renders again in the in-app Browser pane, the "See more" load-more loop works, and the
  30-ad cap is gone (Peng Joon 151 of ~160, Freedom Growth Academy 93/99, King Kong Co 59/62, Ernee Ong 56/58).
  **+74 videos / +99 static images** net across 25 folders (library 677 -> 751 videos, 948 -> 1047 images).
  REACTIVATED: Eddy Miranda, Entrepedia, Marc Chan, Rodney Tan, Cynric Ho, Patricia Ang Real Estate.
  ENDED: Growth Partners Inc, Legacy Advisors Academy, Live A Home SG, FNX Advertising.
  Still 0-active: Allan Khazak, Frank Kern, Property Exit Advantage, Sarah Lee, Thomas Yap, Xccelerate Academy, FNX Marketing (orig page), Escape Uncertainty, Leads SG.
