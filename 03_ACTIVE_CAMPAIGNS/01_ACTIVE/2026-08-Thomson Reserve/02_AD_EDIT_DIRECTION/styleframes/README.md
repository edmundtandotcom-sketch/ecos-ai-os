# Styleframes — Thomson Reserve × Daughter

What is here:

| File | What |
|---|---|
| `styleframes.py` | Renders 25 styleframes (F01–F25) and 12 motion previews (A1–A12; A11 is the 14.3s hand-timed hook — the reference for "edited like a human"), bold palette (black / yellow / red / orange) at 1080×1920. Every device is a function of `t∈[0,1]`, so each one ports to `E:\REMOTION\ads\devices.py` as a frame generator. |
| `prep_assets.py` | One-time: downloads the typefaces (OFL) and Twemoji glyphs, and renders the deck/ebook pages used as b-roll from `../Raw Assets/`. |
| `contact_sheet.jpg` | 20 of the 25 frames at thumbnail size (the five that carry family photos are left out of the repo on purpose), as inspected on 2026-10-04. |

Not committed (bulk media, constitution §9.7): the full-res PNGs, the MP4 previews, fonts, emoji, rendered pages. Regenerate:

```powershell
cd "<this folder>"
pip install pillow numpy pymupdf imageio-ffmpeg
python prep_assets.py
python styleframes.py all          # frames + clips  (~6 min)
python styleframes.py F05_V1_dotgrid_84pct A4_dotgrid_84pct   # just one of each
```

Outputs land in `out/` and `out/anim/`.

**Family photos — the desktop one-liner.** The cloud session cannot see `C:\Users\Admin\Pictures\Family & Daughter`, so the committed frames use a grey placeholder. On the desktop:

```powershell
python styleframes.py --photos "C:\Users\Admin\Pictures\Family & Daughter" F18_V1_family_photo_card A10_family_photo_drop A11_V1_hook_human_cut_14s
```

`--photos` loads every jpg/png in the folder (EXIF-rotated, centre-cropped 4:5 for prints, full frame kept for inserts). Filename order is the assignment table in the EDB §1: `01_` the balcony hook photo, `02_` facade, `03_` showflat model, `04_` the distribution chart, `05_` pool, then the travel photos for the flick. The photo card never repeats a photo inside one ad.

**Real face instead of the silhouette.** Grab one frame from the take and pass it as the plate; every placement is then checked against the actual face:

```powershell
ffmpeg -ss 12 -i "Selfie Body1.mp4" -frames:v 1 plate.png
python styleframes.py --plate plate.png --photos "C:\Users\Admin\Pictures\Family & Daughter" frames
```

**The speaker is a stand-in plate** unless `--plate` is given: a neutral grey-blue room with a head-and-shoulders silhouette at the spec framing (eye-line 38%, head 16% of frame height).

**What the frames are for**: deciding, before the full render, whether a device is right, where it sits, and how big the type is. Read with `../EDB_TR-Daughter_Spinoff_v1.md` §7, which says what each frame proves.

---

## Full render — `render_v1.py` (added 2026-10-08)

The finished V1 ad from the two selfie takes, end to end, on any machine with Python + ffmpeg (no GPU):

```powershell
pip install pillow numpy opencv-python-headless imageio-ffmpeg sherpa-onnx pymupdf
# speech model (one tarball, ~290 MB) from the sherpa-onnx GitHub release, unpacked to ..\asr\
#   https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-zipformer-en-2023-06-26.tar.bz2
python prep_assets.py
python render_v1.py --hook "H:\...\Selfie Daughter Hook 1.mp4" --body "H:\...\Selfie Body1.mp4" --photos "C:\Users\Admin\Pictures\Family & Daughter" --stage all
```

| Stage | What it does | Output |
|---|---|---|
| `audio` | wav per take, resolution/duration, Haar face → crop column + head-size check | `meta.json`, `frame_framing_check.png` |
| `asr` | sherpa-onnx zipformer (word timestamps) → **aligned to the script**, so captions carry the script's spelling and digits with the take's real timing | `words_*.json` |
| `tighten` | silence detection, pauses carved (gap cap 0.38s), one re-encode per take, hook + body joined | `base_cut.mp4`, `words.json` |
| `plan` | phrase-anchored beats (EDB §4), caption cues (2–3 words, one boxed word, six arrival styles), zoom ladder with jitter and a ladder break, breaths, the hold on the question; prints the **human-pass report** | `plan.json` |
| `render` | frame-by-frame compositor: moves, torn splits, inserts, devices, captions, whips/flashes, end card; loudnorm −16 | `TR_V1_Receipt_9x16.mp4` |
| `qc` | 1 fps contact sheet + scene-cut count | `qc/contact_sheet.jpg` |

### The no-complications way: one script

```powershell
.\run_v1.ps1
```

`run_v1.ps1` (in this folder) installs the Python packages, and `render_v1.py` fetches the speech model, fonts, emoji and deck pages by itself on first run. Then it renders from the takes folder and opens the result. Nothing else to set up.

### Or point it at the folder yourself

```powershell
python render_v1.py --folder "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"
```

`--folder` listens to the first 75s of every video in the folder **and its subfolders** (so a `Longer Ads` folder inside it is fine), matches each against the Daughter Hook 1 and Body 1 scripts wherever they start in the take, and picks the best take for each (ties go to the larger picture, so a DSLR take beats the phone). A take that carries the hook and the body in one recording is used for both. Filenames do not matter; only what is said does. Photos come from `C:\Users\Admin\Pictures\Family & Daughter` automatically if it exists. Work files go to `%LOCALAPPDATA%\TR_render_v1\`; the log is written to `<folder>\TR_V1_render_log.txt`; the finished ad lands next to the takes as **`TR_V1_Receipt_9x16.mp4`** with `TR_V1_contact_sheet.jpg` beside it.

**Paste-into-desktop-Claude-Code version** (does the install, the model download and the run):

> In the repo folder `03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-08-Thomson Reserve\02_AD_EDIT_DIRECTION\styleframes`: run `pip install pillow numpy opencv-python-headless imageio-ffmpeg sherpa-onnx pymupdf`; download `https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-zipformer-en-2023-06-26.tar.bz2` and extract it so that `..\asr\sherpa-onnx-zipformer-en-2023-06-26\tokens.txt` exists; run `python prep_assets.py`; then run `python render_v1.py --folder "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"`. Show me the human-pass report it prints, then open `TR_V1_Receipt_9x16.mp4` and `TR_V1_contact_sheet.jpg` from that folder.

`test_v1.py` runs the whole chain on synthetic footage (stand-in plate + the model's sample speech) so the mechanics can be checked without the takes — that is how it was proven on 2026-10-08.
