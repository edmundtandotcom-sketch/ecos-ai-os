Title: Swipe-Library Page-ID Registry — the refresh target list
Status: REGISTRY (single source of truth for `view_all_page_id` per swipe folder)
Created: 2026-08-29 (Decision 128 follow-up — folders were going stale because page IDs were scattered/missing across breakdown docs; the weekly refresh had nothing reliable to iterate)

## How this is used
Every weekly refresh (and every `/rei-ads-scan` catch-up) iterates THIS list: for each folder, navigate `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=SG&view_all_page_id=<ID>&media_type=all` (use country=ALL for the MY/global advertisers noted below), pull the age-filtered NEW videos + the s600 static images, append-only. A folder with no ID here CANNOT be auto-refreshed — resolve its ID and add it before the next run.

## Resolved page IDs
| Folder | view_all_page_id | Notes |
|---|---|---|
| Adrian Lee | 2008367132748627 | |
| Allan Khazak | 1190372650834809 | image-heavy |
| Beyond Realtors Club | 1159884363865127 | |
| Caleb Sim | 106092578729020 | HIGH activity |
| CP Homes | 104268712429679 | direct competitor (decoupling) |
| Dan Lok | 998837360158985 | has >10min VSLs (length-cap) |
| Damien Tan Real Estate | 101766852110723 | resolved 2026-08-29 |
| Denise Tan | 107119960679980 | direct competitor |
| Eddy Miranda | 663968926972914 | image-only |
| Entrepedia | 110261508293707 | image-only |
| Ernee Ong (Proptiply) | 322490897609800 | resolved 2026-08-29; HIGH activity |
| Frank Kern | 137568852956377 | |
| Growth Partners Inc | 872538235944011 | resolved 2026-08-29; image-heavy |
| I Quadrant | 187151448541930 | resolved 2026-08-29; HIGH activity |
| Issac Liu | 1052372747963934 | image-only |
| King Kong Co (Sabri Suby) | 562378543780840 | cross-vertical; 21 >10min VSLs logged-only |
| Legacy Advisors Academy | 102969409387188 | |
| M H Simon | 104247242216764 | |
| Marc Chan | 442189845653421 | HIGH activity |
| Patricia Ang Real Estate | 533704976500523 | |
| Peng Joon | 143408239118491 | currently INACTIVE (campaign ended); country=ALL |
| Property Exit Advantage Singapore | 1190078307520774 | |
| Real Estate Mentor | 1018912674640670 | image-only |
| Rodney Tan | 114028770064802 | direct competitor |
| Sarah Lee | 615849231608268 | |
| Stella Thio - Singapore Luxury Homes | 101446268410106 | resolved 2026-08-29 (was mis-stored); 12 video + 5 static |
| The Freedom Growth Academy | 297816853407449 | 106 videos on disk |
| The Investor Realtor | 108170522131032 | direct competitor |
| The Right Move | 166518753916616 | direct competitor |
| Thomas Yap | 2270869307018514 | country=ALL; currently INACTIVE |
| FNX Marketing By Finix Group | 1286193024567598 | orig page (0 ads now); active spend moved to FNX Advertising 1252511721279349 |

## UNRESOLVED — page ID needs capturing before these can be auto-refreshed
(Navigate the Ad Library by name, open any ad, read `view_all_page_id` from the URL, add above. Until then these folders will NOT refresh.)
Abc Sales AI · Authentic Advisory Systems · Colin Ee · Cynric Ho · Erik Hoffmann · Escape Uncertainty · Flexionmarketing · Future Adviser Sg · Jason Evonne Property · Jo Tan · KS Tan · Leads SG (keyword-only funnel) · Miles Stutz · Networth Builders · Raymondlim.rlc · Success Resources · The Producer Formula · Xccelerate Academy
