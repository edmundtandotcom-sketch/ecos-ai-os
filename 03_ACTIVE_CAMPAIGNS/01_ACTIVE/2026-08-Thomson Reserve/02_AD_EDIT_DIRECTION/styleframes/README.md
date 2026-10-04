# Styleframes — Thomson Reserve × Daughter

What is here:

| File | What |
|---|---|
| `styleframes.py` | Renders 17 styleframes (F01–F17) and 8 motion previews (A1–A8) at 1080×1920. Every device is a function of `t∈[0,1]`, so each one ports to `E:\REMOTION\ads\devices.py` as a frame generator. |
| `prep_assets.py` | One-time: downloads the typefaces (OFL) and Twemoji glyphs, and renders the deck/ebook pages used as b-roll from `../Raw Assets/`. |
| `contact_sheet.jpg` | The 17 frames at thumbnail size, as inspected on 2026-10-04 (second pass, after fixes). |

Not committed (bulk media, constitution §9.7): the full-res PNGs, the MP4 previews, fonts, emoji, rendered pages. Regenerate:

```powershell
cd "<this folder>"
pip install pillow numpy pymupdf imageio-ffmpeg
python prep_assets.py
python styleframes.py all          # frames + clips  (~6 min)
python styleframes.py F05_V1_dotgrid_84pct A4_dotgrid_84pct   # just one of each
```

Outputs land in `out/` and `out/anim/`.

**The speaker is a stand-in plate.** The selfie takes were not reachable from the cloud session, so `plate()` draws a warm-room gradient with a head-and-shoulders silhouette at the spec framing (eye-line 38%, head 16% of frame height). On the desktop, swap `plate()` for a real frame grab (`ffmpeg -ss 12 -i "Selfie Body1.mp4" -frames:v 1 plate.png`) and re-run — every device placement is then checked against the real face.

**What the frames are for**: deciding, before the full render, whether a device is right, where it sits, and how big the type is. Read with `../EDB_TR-Daughter_Spinoff_v1.md` §7, which says what each frame proves.
