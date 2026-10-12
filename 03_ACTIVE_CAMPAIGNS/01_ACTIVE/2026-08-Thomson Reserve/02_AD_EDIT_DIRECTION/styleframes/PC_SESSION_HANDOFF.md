# Daughter ads — hand-off for a session running ON THE PC (2026-10-12)

The cloud session cannot reach the takes (Drive's 10 MB limit) and cannot write video into Drive. The webinar ads
(TR_AD_A1–A16) were made by a session running on the PC; this set is made the same way: a PC session runs the batch,
the files land in the Drive folder, Drive desktop syncs them. Nothing for Edmund to click.

## What to run (PowerShell, on the PC)

```
cd "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-08-Thomson Reserve\02_AD_EDIT_DIRECTION\styleframes"
python -m pip install --quiet numpy pillow imageio-ffmpeg sherpa-onnx opencv-python-headless      # same as run_all.ps1
python batch_tr.py --folder "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"
```

If Google Drive has kept a replaced file as `name (1).py`, run `.\run_all.ps1` instead: it resolves those names, then runs the same command.

## What it does

- 49 ads, in this order: `TR_S_DH1`, `TR_S01…S15`, `TR_SS1`, `TR_SS2` (the 18 selfie ads, one take each: hook + the short
  call to action; the two super-short versions), then `TR_FULL_DH1`, `TR_H01…H15_EXIT`, `TR_H01…H15_BALLOT` (the 31 Longer Ads).
- Output: `Webinar Daughter Spin Off\RENDERS\<id>_1080x1920.mp4` + `<id>_contact_sheet.jpg` + `<id>_preview_small.mp4`,
  `batch_log.txt`, `batch_report.json`. Ads already in RENDERS are skipped, so the run can be stopped and restarted.
- Work files: `%LOCALAPPDATA%\TR_render_v1\<id>\` (local disk, never Drive).
- Photos: `C:\Users\Admin\Pictures\Family & Daughter` (first photo by name = the hook photo card).
- Speed 1.15×, framing as shot (no crop / zoom), captions throughout, one look per ad (`looks.py`), progress border, end card.
- Expect 3–6 min per ad on the PC → 3–5 hours for all 49. The selfie ads come first.

## Known state

- 11 Oct run on this PC: every ad failed at "cut came out 1920x1080" — the phone rotation tag was copied onto the cut.
  FIXED (render_v1.py reads takes with `-display_rotation 0`). Verified in the cloud on the 540p copies: 22 of the 31 Longer Ads
  rendered correctly (see https://claude.ai/artifact/VwryAwjnRKXmZhpYdY436Y and https://claude.ai/artifact/F3fscZYNS71Dj7QYy6c8jg).
- A memory leak in `styleframes.broll` (10 GB over one long ad) is fixed.
- The selfie hook ads: hook k and its call to action sit in the same take; the body is searched after the hook's last spoken
  word (verified on a doubled take). Alignment below 55 % is flagged `CHECK` in `batch_report.json` — look at those contact sheets.

## After the run

1. Open `batch_report.json`: every id should say `OK`. A `CHECK` means the script was heard weakly — watch that ad.
2. Look at a few `_contact_sheet.jpg` files: captions under the chin, nothing over the face, border running, end card last.
3. Log the shipped ids in `VARIATION_REGISTER.md` (this folder) and tell Edmund the RENDERS folder is filled.

The 16 webinar ads used the house pipeline on E:\REMOTION. This set uses its own self-contained pipeline (python + ffmpeg,
everything in this folder; fonts/emoji/deck pages and the speech model are fetched on first run). README.md explains it.
