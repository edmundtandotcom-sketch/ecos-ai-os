# The Continuum — Edit Workbench

Storyboard (live): https://claude.ai/code/artifact/99cdbb7a-508c-484c-a0a6-fc40d73b32c5
3D unit model:     https://claude.ai/code/artifact/2c18006b-e1ca-4f29-84f9-9f91902904f0

## Deliverables

| File | What it is |
|---|---|
| `CONTINUUM_v1_SUBS.mp4` | **The render.** 27m20s. 23 scenes, silence tightened, 29 pictures on their trigger words, 40 b-roll cutaways, 836 burned subtitle cards. 960x540 review copy - the 1080p master is a re-run of the same pipeline. |
| `subtitles.ass` | The caption file. 836 cards, 247 figures in gold. **Upload this to YouTube rather than auto-captioning** - Whisper mis-hears every proper noun in this script and 28 of those were corrected by hand. |
| `Scene4b_LEVELLED.mp4` | Scene4b with the camera roll corrected (8.70 deg -> 0.78 deg). 1080p. **Use this, not the original**, for all further work. |
| `CUT_LIST.csv` | 128 rows. Source file, in/out timecode, duration, timeline position, content. Editor-ready. |
| `EDL_full.json` | The same cut list as structured data, with the reasoning for each retake choice. |
| `picture_positions.json` | Where each of the 29 pictures lands on the timeline. |
| `script_vs_footage_conflicts.json` | The 14 places the script and the footage disagree. |

## Definition of done — outstanding

1. **Nine pickup VO lines** (~1 min of recording). Listed in the storyboard. Blocks the graphics layer for Acts II-IV.
2. **SC11 has no A-roll** — the showflat arrival bridge (Act II into Act III). Needs a VO line over gallery b-roll, or accept a hard cut.
3. **SC18 runs 3:54** — the trim candidate if the target is under 27 minutes.
4. **Developer 3D assets** — site plan, 360 tour, CGI flythrough master. Three scenes designed around them.
5. **Google Earth descent** — must be built in Earth Studio. Long-form only; not permitted in the ads cut.

## Known in the current assembly

- Slate at ~21:30 where the monthly rent figure should be (never spoken on either take).
- Pictures hold a plain 3.5s with no animation — that is the graphics layer, still pending.
- Picture 14 is missing from the source folder; Picture 4 duplicates Picture 3.

## Method

Footage surveyed frame-by-frame, all 13 takes transcribed at word level, cuts made on exact words.
Retakes and false starts resolved to the better take (documented in `EDL_full.json`).
