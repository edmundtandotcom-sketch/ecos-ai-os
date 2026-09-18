# Continuum — long-form YouTube cut

Two cuts, **same edit underneath** — the only difference is the motion, so they
can be compared directly.

| | |
|---|---|
| **`CONTINUUM_v6_MOTION_1.15x.mp4`** | the motion version — kinetic captions, counting figures, drawn-on highlights |
| `CONTINUUM_v5_1.15x.mp4` | the same cut with static captions |

20:33 · 1920×1080 · 1.15× (34.5fps) · branded SAFE outro · **−16.5 LUFS**,
true peak −1.0 dBFS, 48 kHz · A/V sync 0.05s across the programme.
173 clips · 116 overlays / 21 kinds · 426 subtitle cues.

## The motion layer (v6)

**Captions are spoken, not printed.** Each word lands on its own timing, the
word being said is gold, and upcoming words sit ghosted at 22% so the line
never reflows. Word timings come from the carve itself, not a separate pass.

**Figures box and hold.** A money amount, a percentage, or a figure precise
enough to be a measurement gets a gold box and keeps it after it is said - the
only part of a sentence a property viewer is really scanning for.

The rule is deliberately NOT "any number". At `[$%]|\d{2,}` it boxed 141
words, so "10 years old, 3 bedrooms, 300 units" arrived as three highlights in
one sentence and the emphasis stopped meaning anything. Now 101 words: money,
percentages, and figures with a comma, a decimal, or three digits. Plain counts
like "99 years" stay in the sentence. A lone "%" is glued to the number in
front of it, or "15 % to 20 %" renders as four boxes instead of two figures.

**Figures count up.** `$2,650 PSF` rolls to its value over 0.65s. Only the
numeric run animates - prefix, suffix and thousands separators are preserved,
and a non-numeric value passes through untouched. A number that appears reads
as decoration; one that climbs reads as a measurement.

**Highlights draw on.** The stroke on a table screenshot draws across the cell
over 0.55s with a light sweep running ahead of it, and the dim mask settles
separately so it does not animate with the stroke.

Built through the Remotion pipeline (`ContinuumLong`), not a flat assembly:
173 talking-head and b-roll clips, 116 graphic overlays across 21 kinds, 426
burned-in subtitle cues.

## Why v5 is calmer than v3

A cut has to earn itself. v3 made 506 cuts, and the smallest half saved only
52.7s between them — about 0.21s each — landing a cut every 2.43s against
sentences of roughly 3.5s. That is what "multiple transitions in one sentence"
was. Below `MIN_GAP` (0.55s) the pause is now simply kept.

| | v3 | v5 |
|---|---|---|
| clips | 525 | 173 |
| a cut every | 2.43s | 8.4s |
| clips under 1.5s | 169 | 9 |
| first word already running | 56% | 0 |
| last word cut mid-word | 24% | 0 |
| speech replayed | 7.2s | 0 |

Boundaries now snap to whole words. `silencedetect` marks low ENERGY, not word
edges, so a soft onset or a consonant tail read as silence and the cut landed
inside a word — one lost 0.73s of "$2". No hold value fixes that; the error is
a misaligned edge, not a margin.

Every join also carries a transition now (157 fade inside a continuing
thought, 11 wipe at a scene change, 4 slide in and out of b-roll). A
transition OVERLAPS its clips, so all overlay and caption times are corrected
for the cumulative 45s that introduces.

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
