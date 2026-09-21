Title: Swipe-Library Page-ID Registry — the refresh target list
Status: REGISTRY (single source of truth for `view_all_page_id` per swipe folder)
Created: 2026-08-29 (Decision 128 follow-up — folders were going stale because page IDs were scattered/missing across breakdown docs; the weekly refresh had nothing reliable to iterate)

## How this is used
Every weekly refresh (and every `/rei-ads-scan` catch-up) iterates THIS list: for each folder, navigate `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=SG&view_all_page_id=<ID>&media_type=all` (use country=ALL for the MY/global advertisers noted below), pull the age-filtered NEW videos + the s600 static images, append-only. A folder with no ID here CANNOT be auto-refreshed — resolve its ID and add it before the next run.

## Resolved page IDs
| Folder | view_all_page_id | Notes |
|---|---|---|
| Adrian Lee | 2008367132748627 | 3 active 2026-09-21; all creatives >=35d, nothing new to pull |
| Allan Khazak | 1190372650834809 | image-heavy; still 0 active (re-checked 2026-09-21) |
| Beyond Realtors Club | 1159884363865127 | 30 active 2026-09-21 (server-render cap - true count may be higher); +18 statics |
| Caleb Sim | 106092578729020 | HIGH activity; 22 active 2026-09-21, 0 new |
| CP Homes | 104268712429679 | direct competitor (decoupling); 1 active 2026-09-21, 0 new |
| Dan Lok | 998837360158985 | has >10min VSLs (length-cap); 30 active 2026-09-21 (cap); +1 static; 4 over-cap VSLs logged only |
| Damien Tan Real Estate | 101766852110723 | resolved 2026-08-29; 5 active 2026-09-21; 0 new - the 1 video pulled was a re-upload of the 2026-09-07 script under a rotated ID |
| Denise Tan | 107119960679980 | direct competitor; 30 active 2026-09-21 (cap), 0 new |
| Eddy Miranda | 663968926972914 | image-only. **0 active as of 2026-09-21 (campaign ENDED)** |
| Entrepedia | 110261508293707 | image-only. **0 active as of 2026-09-21 (campaign ENDED)** |
| Ernee Ong (Proptiply) | 322490897609800 | resolved 2026-08-29; HIGH activity; 30 active 2026-09-21 (cap), 0 new |
| Frank Kern | 137568852956377 | still 0 active (re-checked 2026-09-21) |
| Growth Partners Inc | 872538235944011 | resolved 2026-08-29; image-heavy. 26 active 2026-09-21, +46 statics (still running since the 2026-09-14 reactivation) |
| I Quadrant | 187151448541930 | resolved 2026-08-29; HIGH activity; 17 active 2026-09-21, 0 new |
| Issac Liu | 1052372747963934 | VIDEO-led since 2026-09-14; 10 active 2026-09-21, +6 statics |
| King Kong Co (Sabri Suby) | 562378543780840 | cross-vertical; >10min VSLs logged-only. **REACTIVATED 2026-09-21** - 30 active (cap), +1 video (5d) + 3 statics; 4 over-cap VSLs logged |
| Legacy Advisors Academy | 102969409387188 | 14 active 2026-09-21, 0 new |
| M H Simon | 104247242216764 | 6 active 2026-09-21, 0 new |
| Marc Chan | 442189845653421 | still 0 active (re-checked 2026-09-21). Was HIGH activity. |
| Patricia Ang Real Estate | 533704976500523 | **0 active as of 2026-09-21 (campaign ENDED)** |
| Peng Joon | 143408239118491 | country=ALL. **REACTIVATED 2026-09-21** - 30 active (cap), +7 statics (44 pulled, 37 byte-identical dups). (The 2026-09-07 wave had ended by 2026-09-14; this is a fresh one.) |
| Property Exit Advantage Singapore | 1190078307520774 | still 0 active (re-checked 2026-09-21) |
| Real Estate Mentor | 1018912674640670 | image-only; 1 active 2026-09-21, 0 new |
| Rodney Tan | 114028770064802 | direct competitor. **0 active as of 2026-09-21 (campaign ENDED)** |
| Sarah Lee | 615849231608268 | still 0 active (re-confirmed 2026-09-21) |
| Stella Thio - Singapore Luxury Homes | 101446268410106 | resolved 2026-08-29; 30 active 2026-09-21 (cap); **+1 video + 36 statics** (4 videos pulled, 3 were re-uploads of 2026-08-29 scripts under rotated IDs) |
| The Freedom Growth Academy | 297816853407449 | 124 videos on disk; 30 active 2026-09-21 (cap), 0 new |
| The Investor Realtor | 108170522131032 | direct competitor; 13 active 2026-09-21, 0 new |
| The Right Move | 166518753916616 | direct competitor; 9 active 2026-09-21, 0 new |
| Thomas Yap | 2270869307018514 | country=ALL; still INACTIVE (re-checked 2026-09-21) |
| FNX Marketing By Finix Group | 1286193024567598 | orig page 1286193024567598 still 0 ads. **FNX Advertising 1252511721279349: 3 active 2026-09-21** (down from 6 on 2026-09-14), 0 new. |
| Abc Sales AI | 460789450460649 | resolved 2026-09-07; country=SG works; non-English creative -> whisper auto-detect. 11 active 2026-09-21, 0 new (both candidates were byte-identical dups) |
| Authentic Advisory Systems | 100639661930725 | resolved 2026-09-07; HIGH activity, extreme re-upload. 30 active 2026-09-21 (cap); 19 videos pulled but **only +1 distinct script** - 18 collapsed (17 match scripts already captured 2026-09-07/09-14, 1 byte-identical) |
| Colin Ee | 102418822374465 | resolved 2026-09-07; direct competitor. **REACTIVATED 2026-09-21** - 14 active, +2 statics |
| Cynric Ho | 239864660126575 | resolved 2026-09-07; direct competitor. **0 active as of 2026-09-21 (campaign ENDED)** - was 4 active on 2026-09-14 |
| Erik Hoffmann | 619905461807712 | resolved 2026-09-07; image-heavy; 7 active 2026-09-21, 0 new (all 6 candidates were byte-identical dups) |
| Jason Evonne Property | 108343127407869 | resolved 2026-09-07; direct competitor, image-only; 3 active 2026-09-21, 0 new |
| Jo Tan | 896274166903494 | resolved 2026-09-07; page name "Jo Tan Real Estate"; direct competitor; 1 active 2026-09-21, 0 new |
| KS Tan | 110637458587684 | resolved 2026-09-07; page name "KS TAN - Real Estate Strategist"; **15 active 2026-09-21 (down from 42)**, +1 static |
| Miles Stutz | 226368730568005 | resolved 2026-09-07; page name "Miles Stutz - 4-Hour Consultant"; image-only; 17 active 2026-09-21, +3 statics |
| Networth Builders | 132637119929833 | resolved 2026-09-07; page name "Networth Prop"; 1 active 2026-09-21, 0 new |
| Raymondlim.rlc | 602457776286259 | resolved 2026-09-07; 3 active 2026-09-21, 0 new |
| Xccelerate Academy | 102308099542618 | resolved 2026-09-07. **0 active (campaign ENDED 2026-09-14, still ended 2026-09-21)** |
| Live A Home SG | 103133488962134 | added 2026-09-13; DIRECT competitor (presenter "Kelly"); new-launch webinar funnel (Thomson Reserve, liveahomesg.com). 3 active 2026-09-21, **+1 video (3d)** |
| Flexionmarketing | 1190074440850416 | resolved 2026-09-14; 30 active 2026-09-21 (cap), +19 statics (58 pulled, 39 byte-identical dups) |

## UNRESOLVED — page ID needs capturing before these can be auto-refreshed
(Navigate the Ad Library by name, open any ad, read `view_all_page_id` from the URL, add above. Until then these folders will NOT refresh.)
**Still unresolved after the 2026-09-14 sweep (5 of the original 18):**
Escape Uncertainty · Future Adviser Sg · Leads SG (keyword-only funnel) · Success Resources · The Producer Formula

(Flexionmarketing was resolved on 2026-09-14 via exact page-name match on the keyword search — page 1190074440850416.
The remaining 5 return no exact `page_name` match under either country=SG or country=ALL; they need the page opened
manually once, or a distinctive brand keyword lifted from their ad copy.)

Resolution notes (2026-09-07): the reliable method is to load
`https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=SG&q=<name>&search_type=keyword_unordered&media_type=all`
and pair `"page_id":"<digits>"` with the nearest `"page_name":"..."` in the page HTML — the ad cards themselves no longer
expose `view_all_page_id` in the DOM. The five still-unresolved names above return either no exact page-name match or too generic a keyword set;
they need the page opened manually once, or a distinctive brand keyword from their ad copy.

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
