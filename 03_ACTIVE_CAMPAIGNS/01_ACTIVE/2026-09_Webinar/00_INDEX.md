# 2026-09 Webinar — Thomson Reserve live webinar ads
Status: ACTIVE · Opened 2026-09-02 · Index created 2026-09-04

## Objective
Fill the live 60-minute Thomson Reserve webinar (review is in October). Paid 9:16 ads
built from Edmund's outdoor phone takes (HDB estate, native vertical, house-style
backdrop). Decision owner: Edmund. Producer: Claude via `/rei-ad-build`.

## Registration & share links (live, added 2026-09-09)
- **Registration URL:** `https://legacylaunch.com.sg/webinar` — the canonical
  join link. Used in `04_META_AD_COPY_v1.md`'s primary text and CTA, and in
  the script's booking CTA (`02_SCRIPT_AND_STRUCTURE/`).
- **Webinar session:** 16 September 2026 (Wed), 8:00 PM. This is the live
  session date, separate from Thomson Reserve's own project preview date
  (~October, still to reconfirm) referenced inside the webinar content.
- **WhatsApp invite/share link** (attendee-facing "invite a friend" link,
  pre-filled message pointing to the registration URL above):
  `https://api.whatsapp.com/send?text=I%20just%20signed%20up%20for%20the%20Thomson%20Reserve%20Webinar%2C%20a%20live%20session%20on%2016%20September%202026%20%28Wed%29%20at%208%3A00%20PM.%0A%0AI%20think%20it%27d%20be%20great%20if%20we%20went%20through%20it%20together.%0A%0AHere%27s%20the%20link%20if%20you%20want%20to%20join%20me%3A%0A%F0%9F%91%89%20https%3A%2F%2Flegacylaunch.com.sg%2Fwebinar`
  — supersedes an earlier version of this link that pointed to a
  `propnex.zoom.us/webinar/register/...` URL; only the destination link
  changed, the date/time and message wording are untouched. **If the
  webinar date changes, this link needs rebuilding too** — the date is
  baked into the pre-filled text, not read dynamically.

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
| `Webinar-Thomson Reserve/`, `(Daughter)/`, `(Plain Text)/` | Image ad sets — "Breaking News" style, family/legacy angle, minimal-text angle |
| `02_SCRIPT_AND_STRUCTURE/` | The webinar itself: `Thomson_Reserve_60min_Webinar_Script_v1.md` (full word-for-word script, internally **v6** as of 2026-09-09 — **the version to record from**). v6 dropped the Amberwood/Serra comparison (diluted focus) in favour of **Two Questions** that organize the whole session — Fit (is it right for you) and Probability (can you actually get it) — plus a **live, tangible fair-price build** on Thomson Reserve's real $1,178 psf ppr land cost, held against a real beat-the-S&P benchmark. Trap-busting content is now grounded in **real market research** (HardwareZone forum sentiment, public buyer-education sources — logged in the script's Appendix B), not invented objections. Thomson Reserve stays the explicit hook/spine throughout per Edmund's direction — every concept resolves into real project specifics, not abstract theory. Closing frame: nobody decides in 60 minutes; they leave knowing the process exists and who runs it. `Thomson_Reserve_Webinar_STRUCTURE_BREAKDOWN_v1.md` (module list, internally v3) is now well behind the script on content — script v6 governs; the structure doc mainly still applies for the earlier framing/psych-technique documentation. 60 min scripted + 30–45 min open Q&A. **Moved here 2026-09-08 from `2026-08-Thomson Reserve/02_Webinar/`** — that was the wrong campaign; this folder is the one, governing workbench for the webinar per the one-campaign-one-workbench rule. |
| `04_META_AD_COPY_v1.md` | Meta headline / primary text / description, six angles matched to the creative above — closes the "Handoffs / open" item below. |
| `03_DELIVERY_CHEAT_SHEET_v1.md` | Companion to the script: a pre-framing phrase bank (per module) so delivery stays conversational, and a 5-slot case-study placement map (mistake → diagnostic catch → outcome shape). **All 5 case studies are bracketed placeholder templates, not real events** — must be swapped for real, consented client cases before this goes live; cut any slot without a real case rather than deliver the placeholder. |
| `07_EMAIL_INVITE_SEQUENCE_v1.md` | 7-email main invite sequence, Fri 11 Sep → Wed 16 Sep (session day gets 2 — morning + ~4 hrs before), plus a 3-email no-show follow-up sequence (reusable for future sessions via a `[NEXT SESSION DATE]` placeholder). Subject line options + full body copy for all 10 emails, consistent with the script v6 / ad copy voice. |
| `08_MASTER_WEBINAR_DOC_v1.md` | **Everything combined** — script v6 + delivery cheat sheet (phrase bank + 5 case-study slots) merged module-by-module, with deck slide numbers cross-referenced. One doc to run the whole session from. If the script or cheat sheet source files change later, re-merge rather than hand-editing this copy. |
| `Thomson_Reserve_Webinar_Deck.pptx` | **The presentation deck**, 30 slides, built from the script's `[SCREEN:]` cues via pptxgenjs. Navy/gold/crimson palette matching the existing ad creative. Speaker notes on every slide carry the full spoken script. Schema-validated and content-QA'd (markitdown) clean; **visual/image QA was NOT possible in this environment** (no LibreOffice or Poppler `pdftoppm` installed) — do a manual flip-through in PowerPoint before presenting. Slide 27 (proof stack) carries the same placeholder-only content as the script/cheat sheet — replace or cut before recording. |
| `06_WHATSAPP_LEAD_QUALIFICATION_FLOW_v2.md` | Post-signup WhatsApp qualification → phone-call booking flow (Messages 1–8), internally v3. Notable: the old urgency-score branch and its 5A/5B off-ramp are gone (every qualified lead flows straight to the Message 6 call pitch); Message 7 now proactively offers 2 time slots within 48h instead of asking an open question; Messages 4/6 fixed to first person to match Message 1's voice. **Open decision flagged in the file:** confirm whether Edmund himself or a team member actually sends Messages 2+ — the first-person voice assumes it's genuinely him. |
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
- ~~Thumbnail + primary text + headline for Meta~~ — done, see
  `04_META_AD_COPY_v1.md` (2026-09-08). Still needs: registration link,
  confirmed preview date, and Edmund's pick of which angles launch first.
- Hook 2 / Hook 3 variants only if asked.
- Other hook families (files 3–7, X) are separate ads for the same webinar.
- Webinar script/deck structure now lives in `02_SCRIPT_AND_STRUCTURE/` in
  this same folder (see above) — still needs Edmund's review before the
  deck gets built and before this gets recorded.
