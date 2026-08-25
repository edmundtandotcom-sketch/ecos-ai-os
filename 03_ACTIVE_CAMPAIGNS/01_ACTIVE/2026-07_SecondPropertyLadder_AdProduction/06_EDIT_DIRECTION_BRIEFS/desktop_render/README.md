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
- **Head measurement uses a Haar cascade**, which finds forehead-to-chin rather
  than true crown-to-chin — it lands within a couple of percent, which is inside
  the spec band, but the proof frame is there so you confirm with your own eyes.
- **9:16 only.** 1:1 and 4:5 crops are a re-run away (change `W`/`H` and the
  caption anchor) but weren't part of this brief.

---

## 6. If you'd rather do it in SharpCut

The cut/caption/crop/export part of this is exactly what SharpCut Studio does,
and it has a native-FFmpeg bridge on your machine (~21× faster than its browser
engine). What SharpCut can't do is the timed brand-graphic overlays — those are
why this script exists. Reasonable split: this script for the full build, or
SharpCut for a fast rough cut when graphics don't matter.
