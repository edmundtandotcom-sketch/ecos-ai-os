Title: Swipe-Library Page-ID Registry — the refresh target list
Status: REGISTRY (single source of truth for `view_all_page_id` per swipe folder)
Created: 2026-08-29 (Decision 128 follow-up — folders were going stale because page IDs were scattered/missing across breakdown docs; the weekly refresh had nothing reliable to iterate)

## How this is used
Every weekly refresh (and every `/rei-ads-scan` catch-up) iterates THIS list: for each folder, navigate `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=SG&view_all_page_id=<ID>&media_type=all` (use country=ALL for the MY/global advertisers noted below), pull the age-filtered NEW videos + the s600 static images, append-only. A folder with no ID here CANNOT be auto-refreshed — resolve its ID and add it before the next run.

## Resolved page IDs
| Folder | view_all_page_id | Notes |
|---|---|---|
| Adrian Lee | 2008367132748627 | 0 active as of 2026-09-07 |
| Allan Khazak | 1190372650834809 | image-heavy; 0 active as of 2026-09-07 |
| Beyond Realtors Club | 1159884363865127 | |
| Caleb Sim | 106092578729020 | HIGH activity |
| CP Homes | 104268712429679 | direct competitor (decoupling) |
| Dan Lok | 998837360158985 | has >10min VSLs (length-cap) |
| Damien Tan Real Estate | 101766852110723 | resolved 2026-08-29 |
| Denise Tan | 107119960679980 | direct competitor |
| Eddy Miranda | 663968926972914 | image-only |
| Entrepedia | 110261508293707 | image-only |
| Ernee Ong (Proptiply) | 322490897609800 | resolved 2026-08-29; HIGH activity |
| Frank Kern | 137568852956377 | 0 active as of 2026-09-07 (campaign ended) |
| Growth Partners Inc | 872538235944011 | resolved 2026-08-29; image-heavy. **0 active as of 2026-09-07** (campaign ended; 87 statics retained on disk). |
| I Quadrant | 187151448541930 | resolved 2026-08-29; HIGH activity |
| Issac Liu | 1052372747963934 | image-only |
| King Kong Co (Sabri Suby) | 562378543780840 | cross-vertical; 21 >10min VSLs logged-only |
| Legacy Advisors Academy | 102969409387188 | |
| M H Simon | 104247242216764 | |
| Marc Chan | 442189845653421 | **0 active as of 2026-09-07** (7 ads exist under active_status=all → paused, not throttled). Was HIGH activity. |
| Patricia Ang Real Estate | 533704976500523 | |
| Peng Joon | 143408239118491 | country=ALL. **REACTIVATED 2026-09-07** — new ~210-ad wave (2 videos + ~104 static ad cards, 21 distinct creatives). Was marked inactive on 2026-08-29. |
| Property Exit Advantage Singapore | 1190078307520774 | 0 active as of 2026-09-07 |
| Real Estate Mentor | 1018912674640670 | image-only |
| Rodney Tan | 114028770064802 | direct competitor |
| Sarah Lee | 615849231608268 | 0 active (re-confirmed 2026-09-07) |
| Stella Thio - Singapore Luxury Homes | 101446268410106 | resolved 2026-08-29 (was mis-stored); 12 video + 5 static |
| The Freedom Growth Academy | 297816853407449 | 106 videos on disk |
| The Investor Realtor | 108170522131032 | direct competitor |
| The Right Move | 166518753916616 | direct competitor |
| Thomas Yap | 2270869307018514 | country=ALL; still INACTIVE (re-checked 2026-09-07) |
| FNX Marketing By Finix Group | 1286193024567598 | orig page (0 ads now); active spend moved to FNX Advertising 1252511721279349 |
| Abc Sales AI | 460789450460649 | resolved 2026-09-07; country=SG works; non-English creative -> whisper auto-detect |
| Authentic Advisory Systems | 100639661930725 | resolved 2026-09-07; HIGH activity (41 active, heavy re-upload) |
| Colin Ee | 102418822374465 | resolved 2026-09-07; direct competitor |
| Cynric Ho | 239864660126575 | resolved 2026-09-07; direct competitor |
| Erik Hoffmann | 619905461807712 | resolved 2026-09-07; image-heavy |
| Jason Evonne Property | 108343127407869 | resolved 2026-09-07; direct competitor, image-only |
| Jo Tan | 896274166903494 | resolved 2026-09-07; page name "Jo Tan Real Estate"; direct competitor |
| KS Tan | 110637458587684 | resolved 2026-09-07; page name "KS TAN - Real Estate Strategist"; HIGH activity, image-heavy |
| Miles Stutz | 226368730568005 | resolved 2026-09-07; page name "Miles Stutz - 4-Hour Consultant"; image-only |
| Networth Builders | 132637119929833 | resolved 2026-09-07; page name "Networth Prop" — CONFIRMED (its 1 active ad matches the video already on disk) |
| Raymondlim.rlc | 602457776286259 | resolved 2026-09-07 |
| Xccelerate Academy | 102308099542618 | resolved 2026-09-07; fresh video campaign |

## UNRESOLVED — page ID needs capturing before these can be auto-refreshed
(Navigate the Ad Library by name, open any ad, read `view_all_page_id` from the URL, add above. Until then these folders will NOT refresh.)
**Still unresolved after the 2026-09-07 sweep (6 of the original 18):**
Escape Uncertainty · Flexionmarketing · Future Adviser Sg · Leads SG (keyword-only funnel) · Success Resources · The Producer Formula

Resolution notes (2026-09-07): the reliable method is to load
`https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=SG&q=<name>&search_type=keyword_unordered&media_type=all`
and pair `"page_id":"<digits>"` with the nearest `"page_name":"..."` in the page HTML — the ad cards themselves no longer
expose `view_all_page_id` in the DOM. The six above return either no exact page-name match or too generic a keyword set;
they need the page opened manually once, or a distinctive brand keyword from their ad copy.

## Changelog
- **2026-09-07** — weekly `rei-swipe-weekly-refresh` run: 12 of 18 unresolved page IDs resolved and added above; Peng Joon reactivated; Marc Chan / Growth Partners Inc / Frank Kern / Adrian Lee / Allan Khazak / Property Exit Advantage / Sarah Lee / Thomas Yap / FNX (both pages) confirmed 0-active. Registry now holds 43 resolved IDs.
