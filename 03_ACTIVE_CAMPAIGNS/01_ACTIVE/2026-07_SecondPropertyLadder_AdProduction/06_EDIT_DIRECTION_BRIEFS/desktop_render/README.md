# Desktop ad renderer — setup and run

Renders the NL01 "Can It Beat the S&P 500?" 9:16 ad from your local DSLR clips,
following `../EDB_SP-Benchmark_NL01_v1.md`. Runs entirely on your machine —
nothing is uploaded, nothing needs Drive access.

Built because cloud sessions **cannot** reach Google Drive's download hosts
(verified 2026-08-25: both cloud environments return 403 CONNECT on
`drive.google.com` and `drive.usercontent.google.com`; the Drive connector has a
hard 10 MB cap and the clips are 87.6 MB and 18.6 MB). On desktop the files are
just local paths, so none of that applies.

---

## 1. Prerequisites (one time)

**FFmpeg** — you already have it: Backdrop Studio ships FFmpeg 8.1.2. Either add
that folder to PATH, or install fresh:

```powershell
winget install Gyan.FFmpeg
```

Check it:

```powershell
ffmpeg -version
ffprobe -version
```

**Python 3.9+** (you have it — ECOS runtime is FastAPI):

```powershell
python --version
```

**Python packages:**

```powershell
pip install faster-whisper pillow opencv-python
```

- `faster-whisper` — word-level timings, so overlays land on the exact spoken
  word instead of an estimated timestamp. CPU-only, no GPU needed.
- `pillow` — draws the brand graphics.
- `opencv-python` — measures the speaker's head so the framing spec is hit
  automatically. Optional; without it you set the crop by hand.

**Fonts (optional but recommended).** Drop `Montserrat-Bold.ttf` and
`ArchivoBlack-Regular.ttf` into a `fonts/` folder next to the script. Without
them it falls back to Impact/Arial Bold, which looks close but not identical to
the Bible's spec. Both are free from Google Fonts.

---

## 2. Run it

```powershell
cd <this folder>
python render_ad.py --stage all
```

That runs six stages in order. First run takes roughly 15–40 minutes, almost all
of it transcription and the final encode.

| Stage | What it does | Notes |
|---|---|---|
| `probe` | Checks FFmpeg + both clips exist, prints resolution/duration | seconds |
| `transcribe` | Word-level timings for both clips; **prints which CTA variant was actually spoken** | slow — cached after the first run |
| `frame` | Measures the speaker, computes the 9:16 crop, writes a proof frame | seconds |
| `graphics` | Generates all 15 brand PNGs | seconds |
| `render` | Grade → captions → timed overlays → end card → join → loudnorm | slowest |
| `qc` | Contact sheet + the checklist to eyeball | seconds |

Re-run any single stage while iterating:

```powershell
python render_ad.py --stage frame
python render_ad.py --stage graphics
python render_ad.py --stage render
```

Output: `out/SP_BENCHMARK_9x16_v1.mp4`

---

## 3. The two things to check by eye

**After `--stage frame`** open `out/frame_framing_check.png`. It draws the spec
over a real frame:

- **Yellow line** — where the eye-line should sit (40% down)
- **Blue bands** — top 10% and bottom 17%, keep the face out of both
- Head crown-to-chin should fill **12–16%** of frame height — a medium shot, not
  a close-up. This is the "speaker not too big" rule.

Wrong? Set `CROP_OVERRIDE = (x, y, w, h)` in the CONFIG block (source pixels) and
re-run the stage. If the source is too narrow for 9:16 the script pillarboxes
over a blurred fill rather than cropping in tighter — deliberately, so the face
never ends up oversized.

**After `--stage qc`** open `out/qc/contact_sheet.jpg` and check:

- no overlay ever covers the face
- captions legible and never clipped
- chips and cards land on the right spoken words
- end card present
- grade looks natural — warm skin, blacks not lifted

---

## 3b. Config knobs that matter — set from the real takes (2026-08-25)

These were tuned against the actual S&P footage on the desktop. If you point the
script at *different* footage, revisit them.

| Knob | Set to | Why |
|---|---|---|
| `WHISPER_MODEL` | `medium` | Captions burn from this transcript, so a mishearing ships on screen. Worth the extra minutes. |
| `WHISPER_LANG` | `"en"` | Auto-detect put the first ~55s of the body take into **Malay** and produced gibberish — which also broke every beat anchor inside it. |
| `WHISPER_PROMPT` | domain vocab | Without it: "S&P 500"→"SMP 500", "stamp duty"→"stem beauty", "walkaway price"→"work away price". |
| `FIT_OVERRIDE` | measured crown/chin/eye | This footage is framed **tighter** than the 12–16% target. Cropping can only make a head *bigger*, so the fix is to scale the whole picture back inside the canvas. |
| `FILL_MODE` | `"navy"` | What surrounds the scaled-back picture. Navy reads as designed letterbox; blur at this magnification is just a smear of face. |
| `MAX_GAP` | `0.38` | **57% of the body clip is dead air**, in 31 gaps of up to 12s. Untightened the ad runs ~7.5 minutes. |
| `CTA_VARIANT` | `"C"` | The CTA take contains **all three** variants read back to back, each slated "Call to Action 1 / 2 / 3". The script finds the slates and uses only the one you name. |

**On the framing knob specifically.** `FIT_OVERRIDE` takes three numbers you read
off a real frame in any image viewer: `head_top` (top of the hair), `head_bottom`
(bottom of the chin), `eye_y` (pupil centre), in source pixels. The script then
scales so the head lands at `TARGET_HEAD_PCT` and the eyes land on the eye-line.
It never upscales and never exceeds canvas width — so the head can only come out
at or under target. An over-tight face is the failure mode this exists to
prevent.

## 4. How the timing works

Overlays are anchored to **spoken phrases**, not fixed timestamps. The `BEATS`
table says things like "start when he says *that same money*, end 1.2s after
*beating the S&P*". The script fuzzy-matches those phrases in the transcript and
computes real times, so the edit is correct regardless of how fast the take
actually runs.

If a phrase doesn't match (he ad-libbed, or Whisper misheard), the render prints
`! MISSED anchor '<phrase>'` and skips just that overlay. Fix by editing the
phrase in `BEATS` to match what he actually said — the transcript is at
`out/words_body.json`.

---

## 5. Known limitations

- **No music bed.** Voice only. Your original beds live in `E:\REMOTION\audio\rei_*`;
  add one in your editor if wanted. The script deliberately adds nothing it has
  no licence for.
- **Karaoke is per-word via ASS `\k`.** Rendering depends on libass being built
  into your FFmpeg (it is, in standard Windows builds).
- **Auto head measurement uses a Haar cascade**, which finds forehead-to-chin and
  misses the hair (`HAAR_TO_HEAD` compensates). On this footage it's bypassed
  entirely by `FIT_OVERRIDE`, which uses numbers measured by eye — more reliable.
  Either way the proof frame is there so you confirm visually.
- **Pause removal re-encodes each speech segment**, then stream-copies them
  together, so no sync drift accumulates across ~30 cuts. It costs render time
  but it's the reason the audio stays locked to picture.
- **9:16 only.** 1:1 and 4:5 crops are a re-run away (change `W`/`H` and the
  caption anchor) but weren't part of this brief.

## 5b. If a beat anchor misses

The render prints `! MISSED anchor '<phrase>'` and skips just that overlay.
Whisper transcribes numbers as digits, so an anchor written `"wait four years"`
will not match `"wait 4 years"` — two anchors needed exactly that fix on this
take. Open `out/words_body.json`, find how the line was actually transcribed, and
edit the phrase in `BEATS` to match. Anchors resolve in script order from a
moving cursor, so a phrase said twice (e.g. "your future buyer") anchors to the
right occurrence rather than the first.

---

## 6. If you'd rather do it in SharpCut

The cut/caption/crop/export part of this is exactly what SharpCut Studio does,
and it has a native-FFmpeg bridge on your machine (~21× faster than its browser
engine). What SharpCut can't do is the timed brand-graphic overlays — those are
why this script exists. Reasonable split: this script for the full build, or
SharpCut for a fast rough cut when graphics don't matter.
