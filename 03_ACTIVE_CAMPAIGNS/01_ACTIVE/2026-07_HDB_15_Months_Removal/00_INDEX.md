# Campaign Index — HDB 15-Month Wait-Out Removal (YouTube weekly video)

Date: 2026-08-07
Status: IN PRODUCTION — draft edit assembled, awaiting Edmund's review pass

## Objective
Weekly YouTube long-form video reacting to the removal of the 15-month wait-out
for private owners buying HDB resale. Script follows the retention framework;
CTA = "BRIDGE" comment + Second Property Strategy Session.

## Files here (source of record)
- `Youtube Script-HDB 15 Months.gdoc` — final script with SCREEN/CITE/DELIVER cues
- `1.mkv` (10:12), `2.mkv` (5:13), `3.mkv` (4:25) — raw talking-head takes, 1080p30

## Production (runtime lives locally, per Code & Portability rule)
- Remotion project: `E:\REMOTION` (composition `HDB15Months`)
- Footage copies (remuxed MP4): `E:\REMOTION\public\footage\`
- Transcripts + cut-list generator: `E:\REMOTION\work\`
- Preview: Remotion Studio at http://localhost:3000 (`npm run dev --prefix E:\REMOTION`)
- Draft edit v6: 217 clips, 43 overlays; 12:19 runtime; 406s dead air removed
  (silencedetect -33dB/0.35s + word cuts). Article segments now use RVM
  CUT-OUT talking head (Backdrop Studio matting → alpha WebM) over full-screen
  article backgrounds; proper YouTube subtitles; screen shouts; data boards;
  13 SG b-roll cutaways; gold progress bar. CapCut-style pass per Edmund's reference:
  Anton/Archivo Black typography, chapter cards with red accent slams,
  "$100,000 MISTAKE" flash card, keyword pop chips, emoji owner badges,
  punch-zoom cuts, 6 article greenscreens, 8 b-roll cutaways
  (own showflat-crowd raws + 8 Pexels free-license SG aerial clips, approved
  by Edmund 2026-08-07, in `E:\REMOTION\public\broll`; chapter cards use
  MBS / skyline-dusk / HDB-block aerial stills as backgrounds)

## Definition of done
1. Edmund reviews draft cut in Studio → adjustment notes
2. Final render (`npx remotion render HDB15Months`) → MP4 lands back in this folder
3. After publish: approved reusable outputs promoted to `01_ASSET_LIBRARY`

## Decision owner
Edmund. AI desk: Content (production executed via Remotion pipeline).
