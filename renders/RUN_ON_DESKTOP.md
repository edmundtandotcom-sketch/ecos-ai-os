# How to finish the NL01 S&P-Benchmark render

The cloud sessions cannot download the source footage (see `RENDER_BLOCKED.md`
and `RENDER_BLOCKED_2.md` — Google Drive egress is denied by the environment's
network policy, in **both** available cloud environments). Everything else is
built, tested and committed here, so the render finishes wherever the footage
can actually be downloaded.

Pick **one** of the three routes below. Route A is the least work.

---

## Route A — allow Drive in the cloud environment (~2 minutes, then hands-off)

1. Go to **claude.ai/code → Environments → "Claude Code" → network settings**.
2. Allow these two hosts:
   - `drive.google.com`
   - `drive.usercontent.google.com`  ← the bytes actually come from here;
     allowing only the first one still fails
3. Start a session on branch `claude/ad-render-sp` and say:
   *"Run renders/tools/render_pipeline.py all, then QC and push."*

## Route B — run it on the desktop (`E:\ECOS`)

```bash
git clone <this repo> && cd ecos-ai-os && git checkout claude/ad-render-sp

pip install gdown faster-whisper playwright opencv-python
playwright install chromium          # skip if Chromium is already present
# ffmpeg must be on PATH: https://ffmpeg.org/download.html

python3 renders/tools/render_pipeline.py all
```

Then open `renders/work/framing_before.png` next to `framing_after.png` and the
`renders/contact_sheet_*.jpg` files, confirm they look right, and push.

## Route C — put the footage somewhere the cloud can reach

Upload both clips anywhere the network policy permits, then edit the two URLs
in `stage_fetch()` of `render_pipeline.py` and run Route A step 3.

---

## What the pipeline does

```
python3 renders/tools/render_pipeline.py all
```

runs seven stages, each resumable — a failed encode never forces a
re-transcribe, and any stage can be run on its own by name:

| Stage | What it does |
|---|---|
| `fetch` | Downloads both clips, **verifies exact byte counts** and aborts on a truncated download |
| `probe` | ffprobe resolution / fps / duration → `work/probe.json` |
| `transcribe` | faster-whisper with word timestamps → `work/{body,cta}_words.json` |
| `frame` | Detects the face, computes the 9:16 crop so the head is 12–16% of frame height, writes before/after test frames |
| `graphics` | Renders G1–G10 brand PNGs via headless Chromium |
| `assemble` | Trims dead air, grades, frames, joins body→CTA, burns karaoke captions, composites every overlay on its spoken beat, adds the 3.0s end card, loudnorms to −16 LUFS, encodes under 90 MB |
| `qc` | Samples a frame every 5s and tiles them into contact sheets to review |

Useful flags: `--head 13` (smaller speaker), `--crf 24` (smaller file),
`--model small` (more accurate transcript, slower), `--force` (redo a stage).

## What is already verified

- **Brand graphics: rendered and visually checked in-session.** All 18 PNGs
  produce at the right sizes (full-frame cards 1080×1920, data cards 920×343,
  chips ~104px tall). Palette, hierarchy and copy match the brief.
- **Timing logic: proven by `renders/tools/selfcheck.py`**, which dry-runs the
  whole beat-and-caption engine against the expected script with no media.
  It currently reports all 16 overlay beats matched, zero band collisions,
  zero overlapping caption cues. Re-run it after any edit to `BODY_BEATS`.

The self-check caught four real bugs before they could waste an encode: words
like "that's" and "S&P" split into multiple tokens and broke phrase matching;
"your future buyer" bound to its first mention in the opening instead of the
kinetic list; the two data cards overlapped each other; and adjacent caption
cues overlapped enough to double-stack. All four are fixed.

## What still needs human eyes

These are judgement calls the scripts deliberately do not auto-approve:

1. **Framing.** The face detector sets the crop, but compare
   `work/framing_before.png` with `work/framing_after.png` and confirm the head
   really reads as ~14% of frame height. Adjust with `--head` and re-run
   `frame` + `assemble`.
2. **Fonts.** If Google Fonts is unreachable the graphics fall back to DejaVu
   at weight 900 — close in feel, not identical to Archivo Black. Note whichever
   applies in `QC_REPORT.md`.
3. **The chart cutaway is long.** G1 holds full-frame for roughly 18 seconds,
   because the brief anchors it from "that same money could be invested" all the
   way to "beating the S&P 500". It is per spec, but it is the one beat worth a
   second opinion — shortening means giving G1 an earlier `until` phrase.
4. **The contact sheets.** Confirm no overlay touches the face, captions are
   never clipped, cards are legible, and the end card is present.

## Before pushing

Write `renders/QC_REPORT.md` with the probe results, measured durations, the
real beat timestamps from `work/beats.json` against the brief's estimates, the
CTA variant actually heard, the framing measurements from `work/framing.json`,
every QC check with pass/fail, and any compromises. Then:

```bash
git add -f renders/SP_BENCHMARK_9x16_v1.mp4 renders/QC_REPORT.md \
           renders/contact_sheet_*.jpg renders/work/framing_*.png
git commit -m "Render NL01 S&P-Benchmark 9:16 ad"
git push origin claude/ad-render-sp
```

No pull request — the brief asks for the branch only.
