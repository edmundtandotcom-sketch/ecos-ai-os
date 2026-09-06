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

## Current deliverables (round 3, 2026-09-05)
| File | Speed | Length | Notes |
|---|---|---|---|
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16_115.mp4` | 1.15x | 2:38 (158.4s) | sync rebuilt from scratch and audited against the raw take (see round 3) |
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16_120.mp4` | 1.20x | 2:32 | round-2 build - NOT rebuilt, carries the round-2 sync defect; do not use |
| `05_RENDER/out/WEBINAR_THOMSON_RESERVE_9x16.mp4` | 1.15x | 2:55 | round-1 cut - superseded |

## Edit decisions
**Round 1 (2026-09-04)**
- Hook 1 chosen: number + question in the first 2s. H2/H3 available as variants on request.
- Body re-ordered: likes -> "three things making me think twice" -> dislikes -> CTA.
- Dropped: 144-149s restart, 202.7-212.6s take that trails off, 218s fragment.
- Transcript fixes: Tre Ver, Parc Clematis, Ai Tong, Central Catchment, "stacks" (not tax), "analysis".

**Round 2 (2026-09-05, from Edmund's timestamped notes)**
- Jerking: the phone take drops frames in bursts; speed is now applied with
  motion-compensated interpolation in the tighten stage, not on the final.
- Captions on every shot in one band (0.80), including on plates; orange box
  hugs the word; hook slam moved above the band so the face stays clear.
- Gaps tightened (0.20 / 0.10 / 0.07); 1:57.9-2:01.0 ("So you'll be
  potentially paying more thaaan") cut; graph-paper plate removed.
- Condos only (no HDB) in the LIKE/DISLIKE beat; real forest for Central
  Catchment; a train on a viaduct for the MRT beat; an 800m pin-and-radius
  map for "within 800m of TEL stations".
- Faster bed: 123 BPM future-bass (Pixabay, commercial licence).
- Working files now on E:\REMOTION\work\webinar_2026-09 (Drive locks).

**Round 3 (2026-09-05, "nothing is synced")**
- Root cause: audio was assembled from per-shot and per-segment AAC files;
  every AAC seam carries a ~30ms timestamp gap that a player honours but the
  final mix packs shut - speech ran 1.8s late by the 50s mark in every round.
- Rebuilt sync by construction: exact-N-frame video segments + exact-sample
  PCM audio in the tighten stage, video-only shots on the frame grid, one
  continuous speech track in the final mix, assertions at every stage.
- Seek fix: shot seeks are now half a frame early (a 4-decimal seek dropped
  the first frame on one shot in three).
- Whoosh impact (0.89s into the sample) now lands on the cut.
- Audit before delivery (`05_RENDER/work/_final_audit2.py`): speech offset vs
  raw take, video frame offset on clean shots, caption vs spoken word, whoosh
  vs cut, device starts on shot boundaries, held frames.

## Definition of done
Edmund watches the cut end to end and either approves for upload or returns
timestamped notes. Approved final → `01_ASSET_LIBRARY/.../CAMPAIGN_FINALS`.

## Handoffs / open
- Thumbnail + primary text + headline for Meta (not started).
- Hook 2 / Hook 3 variants only if asked.
- Other hook families (files 3–7, X) are separate ads for the same webinar.
