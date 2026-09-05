# 2026-09 Webinar — Thomson Reserve live webinar ads
Status: ACTIVE · Opened 2026-09-02 · Index created 2026-09-04

## Objective
Fill the live 60-minute Thomson Reserve webinar (review is in October). Paid 9:16 ads
built from Edmund's outdoor phone takes (HDB estate, native vertical, house-style
backdrop). Decision owner: Edmund. Producer: Claude via `/rei-ad-build`.

## Authority
- Ads follow `E:\REMOTION\ADS_PLAYBOOK.md` + `E:\REMOTION\ads\HOUSE_STYLE_ADS.md` only
  (not the reels/long-form playbooks).
- Singapore-only b-roll (`E:\REMOTION\public\broll\stock`), no repeats inside one ad.

## Folder map
| Item | What |
|---|---|
| `1-Webinar Hooks.mp4` | 3 hook takes (60s): H1 "$3.5M budget — will Thomson Reserve be the one?", H2 "$5M budget", H3 "considering Thomson Reserve" |
| `2-Webinar Body.mp4` | Body take (281s): likes ×3, dislikes ×3, webinar CTA. Contains restarts at 144s and 202–223s |
| `3–7, X-*.mp4` | Other hook families (S&P / Own Story / Daughter / 2nd Property / Decouple) — not yet cut |
| `05_RENDER/render_webinar.py` | Composer for native 9:16 takes (tighten + re-order + devices + captions + VFX) |
| `05_RENDER/spec_webinar.py` | The ad: edit order (PIECES) and beats (SPEC) |
| `05_RENDER/work/` | transcripts (`words_*.json`), tight cut, shot cache, QA sheets |
| `05_RENDER/out/` | **Deliverables** |

## Current deliverables
| File | Hook | Length | Notes |
|---|---|---|---|
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16.mp4` | H1 ($3.5M budget) | 2:55 (174.8s) | Hook + full body at 1.15x, 178 shots, 53 cuts/min, 39 beats, 111 caption plates, endcard "CLICK THE LINK / JOIN ME LIVE" |

## Edit decisions (2026-09-04)
- Hook 1 chosen: number + question in the first 2s. H2/H3 available as variants on request.
- Body re-ordered: likes → "three things making me think twice" → dislikes → CTA.
- Dropped: 144–149s restart, 202.7–212.6s take that trails off, 218s fragment.
- Transcript fixes: Tre Ver, Parc Clematis, Ai Tong, Central Catchment, "stacks" (not tax), "analysis".

## Definition of done
Edmund watches the cut end to end and either approves for upload or returns
timestamped notes. Approved final → `01_ASSET_LIBRARY/.../CAMPAIGN_FINALS`.

## Handoffs / open
- Thumbnail + primary text + headline for Meta (not started).
- Hook 2 / Hook 3 variants only if asked.
- Other hook families (files 3–7, X) are separate ads for the same webinar.
