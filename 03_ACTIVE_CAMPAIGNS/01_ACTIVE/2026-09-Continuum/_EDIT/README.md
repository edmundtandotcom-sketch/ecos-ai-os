# Continuum — long-form YouTube cut

**`CONTINUUM_v3_1.15x.mp4`** — 18:47, 1920×1080, delivered at 1.15× (34.5fps)
with the branded SAFE outro attached. Audio normalised to **−16.4 LUFS**,
true peak −1.1 dBFS, 48 kHz.

Built through the Remotion pipeline (`ContinuumLong`), not a flat assembly:
525 talking-head and b-roll clips, 118 graphic overlays across 21 kinds, 414
burned-in subtitle cues.

---

## What was cut out of the takes

The cut is carved against **measured audio**, not the transcript — Whisper's
source timings are unreliable (on one take it placed a word at 0.00s where the
file is provably silent until 6.25s).

| Removed | |
|---|---|
| Silence | 11.5 min — `silencedetect`, −33dB / 0.35s, 0.12s held at each edge |
| Fumbles | 4.7s — any single token ≥2.8s is a fumble hiding inside a long word |
| Restarts | 27.0s — a phrase begun, abandoned and said again |

**Restarts are the category that silence detection cannot see**, because the
speaker never pauses while doing it. Thirteen were found and cut, across four
passes — removing one unmasks the next. Examples:

- "scan the QR code…" — said three times, the third kept
- "have an extra *this set of big*" → "have an extra set of data"
- "1,121 units including Tembusu Grand 200" — said twice, 6.2s
- "your your gains", "live in **in** prime district"

**Deliberately kept** — repetition is not automatically a defect:

- "maybe you want to **stay** / maybe you want to **sell**"
- "should you be selling / keeping it / leaving it"
- "run **far far** away" — idiom
- "three honest scenario**s**. **Scenario** A" — two different words
- "people, people kill for…" — emphasis

---

## Audio and figures are exactly as shot

Nothing was re-voiced, re-ordered or corrected. Fourteen places where the
spoken figure disagrees with the graphic on screen are catalogued in
**`FIX_LIST.md`**, timestamped against this delivered file. One is a genuine
factual error worth fixing before publishing; the rest are smaller.

Two points in the script have **no recording at all** — the rent figure and the
SC11 bridge. Both need a pickup, not an edit.

---

## Files

| | |
|---|---|
| `CONTINUUM_v3_1.15x.mp4` | the cut — **this is the deliverable** |
| `FIX_LIST.md` | 14 spoken-vs-graphic mismatches, timestamped |
| `subtitles_review.txt` | all 414 captions as text, for proofreading |
| `CUT_LIST.csv`, `EDL_full.json` | which passage of which take, in order |
| `picture_positions.json` | where each supplied picture lands |
| `Scene4b_LEVELLED.mp4` | Scene4b with the camera roll corrected |

`CONTINUUM_v1_SUBS.mp4` and `CONTINUUM_v2_1.15x.mp4` are superseded and can be
deleted once you are happy with v3 — that reclaims about 1.2 GB. v1 is the
first flat assembly (stutters and caption defects in it); v2 is this same cut
before "TOP" was corrected in two captions.

## Loudness

The render comes out around −22 LUFS. YouTube turns loud uploads down but
never lifts quiet ones, so that plays noticeably quieter than everything
around it. `fix_loudness.sh` brings the finished file to −16 LUFS to match
`THOMSON_RESERVE_FINAL`, audio only, video copied — a couple of minutes rather
than a re-render:

    bash work/continuum/fix_loudness.sh <in.mp4> <out.mp4>

---

## Scene4b

The recording rolls continuously between −8.76° and +2.34°. It is corrected
per-segment with rotation clamped at ±5°: **15.5% crop, 13 of 14 measured
points inside ±0.78°**. Clamping is what keeps the crop at 15.5% — an
unclamped correction took it to 23.5% for no visible gain.

---

## Rebuilding

    bash work/continuum/rebuild.sh     # captions, overlays, gates, timeline, meta
    bash work/continuum/bundle.sh      # only if src/ changed

`rebuild.sh` runs the three build gates (anchor, collision, asset) and writes
the TypeScript timeline Remotion actually compiles. A re-carve moves every
absolute second in the programme, so nothing downstream survives one — run the
whole chain, never a single step.
