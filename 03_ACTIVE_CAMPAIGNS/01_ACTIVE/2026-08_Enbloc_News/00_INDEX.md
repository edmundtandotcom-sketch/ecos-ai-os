# Campaign Index — En-Bloc News (YouTube weekly video #2)

Date: 2026-08-15
Status: v4 FINAL DELIVERED (`ENBLOC_FINAL_1.15x.mp4`) — three review rounds
closed; v1-v3 drafts superseded (safe to delete)

## Review-round log (what each round fixed)
- v1→v2: en bloc spelling, new music, condo card imagery, clean article
  captures, caption-band protection — but the padding fix introduced word
  repeats at cuts (108 overlapping ranges) and the new music was 6.4dB quiet
- v2→v3: padding clamped (0 overlaps), music normalized, restart detector
  tightened (18 auto-removed), 7-point verification gate created, v4
  cinematic components added (BlurQuote / ConceptMap / CornerStat)
- v3→v4 (final): subscribe finishes before chapter card; card-collision rule
  (nothing draws over cards — ever); punch/flash anchored to spoken words;
  cross-take duplicate removed (take1 end trimmed); Stacked screenshot
  repaired (promo + dead hero spliced out); ChapterCard accent auto-fits;
  screencast rows highlight on speech beats (rowTimes)

## Objective
Weekly long-form reacting to TWO en-bloc changes in one week: the proposed
consent-vote drop (80% → 70%/65%, **First Reading — NOT law**) and the
developer ABSD-timeline extension (5.5 → 6.5/7.5 yrs, already in force).
Honest frame: a rebalance, not a green light; en-bloc is a maybe, never a plan.
CTA = comment "REALITY" + Second Property Strategy Session (second opinion).

## Source of record
- `Video Script.docx` — **v4, superseded** (led on the ABSD timeline only)
- **Recorded script = v6** from GitHub `ecos-weekly-intelligence`
  → `weekly_content_intelligence_os/content_outputs/produced/2026-07-30/idea-4-enbloc-thaw`
  (branch `claude/new-session-8uzjcu`). Confirmed against the transcript:
  the recording opens on the consent vote and covers BOTH changes.
- `1.mp4` (9:50), `2.mp4` (8:08) — raw takes, 1080p30

## Production (runtime local, per the Code & Portability rule)
- Pipeline: `E:\REMOTION`, composition `EnblocNews`, generator
  `work/enbloc/build_enbloc.py`
- **Style Variant B — Charcoal & Red** (video #1 used A Navy & Gold; variants
  must differ between consecutive videos)
- Draft v1: 239 clips · 53 overlays · **12:12** · 296s of dead air removed
- 9 cited articles screenshotted → `public/articles/enbloc/`; 3 RVM cut-out
  matte windows → 31 clips composited over article greenscreens
- 5 duplicate/restart takes auto-cut (transcript-verified)
- Subtitle review file: `E:\REMOTION\work\enbloc\subtitles_review.txt`

## Deliverables
- `ENBLOC_DRAFT_v1_1.15x.mp4` — review copy (1.15× + branded outro)
- `ENBLOC_DRAFT_v1_natural.mp4` — natural-speed master
- Reels: 7 approved (pilot v3 passed 2026-08-16) → `REELS/` —
  Reels V2 house format (neon intro / SEE-YOU-IN-THE-NEXT-ONE outro, strict
  copy of the editor examples), speech-complete endings, gold hot-word
  captions, all 1.15x. Composition `EbReel1..7`, generator
  `work/enbloc/build_eb_reels.py`. Review tool: REVIEW_STUDIO.html (this
  folder) or https://claude.ai/code/artifact/3a55b1ff-2d59-4d0c-ade4-cb03f4dc8155

## Definition of done
1. Edmund reviews with timestamps + subtitle corrections
2. Final render → replaces the draft in this folder
3. Reels batch (3 scripted) → `REELS/`
4. Upload kit (title/description/chapters/tags) on request
5. Approved reusable outputs promoted to `01_ASSET_LIBRARY`

## Decision owner
Edmund. Desk: Content. Pipeline: `/video-produce`.
