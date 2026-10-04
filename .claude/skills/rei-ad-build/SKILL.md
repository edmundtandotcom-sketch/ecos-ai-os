---
name: rei-ad-build
description: Render a finished 9:16 paid ad reel from raw talking-head footage using the E:\REMOTION\ads pipeline - device library, effects library and the measured ADS_PLAYBOOK norms. Use when Edmund types /rei-ad-build, asks to build/cut/render a paid ad or ad reel from a take, or asks for ad variations. This RENDERS; it is not the brief writer (rei-ads-routine) and not the organic reels pipeline (video-produce).
---

# REI Ad Build — render a paid ad reel

Desktop-only. Builds a finished 9:16 ad from a raw talking-head take.

## 0. Read these first, in this order

| File | What it governs |
|---|---|
| `E:\REMOTION\ADS_PLAYBOOK.md` | The measured norms. Derived from 171 vertical ads in the swipe library, not asserted. |
| `E:\REMOTION\ads\DEVICE_LIBRARY.md` | The graphic devices and how each is placed. |
| `E:\REMOTION\ads\devices.py` | Device code. |
| `E:\REMOTION\ads\effects.py` | Camera moves, transitions, layouts, frame furniture, and `HOUSE` defaults. |

**Ads are not reels.** `REELS_PLAYBOOK.md` (square speaker card, brand-colour
world, captions at 83%) is for ORGANIC short-form and must not be applied here.
An ad is judged by whether a cold stranger stops scrolling and clicks.

## 1. What good looks like

Measured off the reference set, and off the professionally-cut version of the
S&P script Edmund supplied (2026-08-26):

- **40–55 cuts/min, ~1.1s median shot.** One shot per caption phrase; the cut
  lands on the phrase change. The library median (10–14) averages in the lazy
  ads — do not target it.
- **Captions**: white ALL CAPS, **exactly one word in an orange rounded box**,
  small emoji under the line, low in frame (~65%), 2–3 words per cue.
  Rendered as plates (`devices.caption_plate`), not ASS — ASS cannot box a
  single word or carry a colour emoji.
- **Never static.** Every shot carries a camera move from `effects.move`.
- **Full-bleed speaker.** No letterbox, no square card, no persistent chrome.
- **Nothing covers the face.** Devices needing a scrim run over b-roll instead.

## 2. B-ROLL: SINGAPORE ONLY — hard rule

Every insert must read Singapore/Asian: local skyline, HDB, local streets,
local faces, Singapore currency.

- Use only `E:\REMOTION\public\broll\stock` (the vetted SG set).
- `broll/_rejected_non_sg` holds 33 quarantined clips (US dollars, European
  trams, Western faces). **Never use them.** Anything newly fetched must be
  eyeballed before it enters the SG allowlist.
- **Never repeat a clip inside one ad.** Repeats were the clearest tell that a
  cut was machine-assembled.

## 3. Procedure

1. **Confirm the take and the CTA.** Multi-variant CTA recordings are common —
   isolate the one that ships (slates: "Call to Action 1/2/3").
2. **Transcribe** with `language="en"` forced and a domain `initial_prompt`;
   fix the word stream (`S&P`, project names) *before* cues are split.
3. **Tighten**: carve pauses; cap internal gaps around 0.38s.
4. **Check source framing against ADS_PLAYBOOK §7.** A 9:16 crop only ever
   magnifies. If crown-to-chin exceeds ~14% of the SOURCE frame, say so —
   do not letterbox around it.
5. **Write the variation spec** — content blocks, device beats (anchored to
   spoken phrases, not timestamps), SG b-roll per beat.
6. **Render QA stills and look at them** before committing to a full render.
7. Version and log; update the campaign `_INDEX.md`.

## 4. Run it

```
cd <campaign>\06_EDIT_DIRECTION_BRIEFS\desktop_render
python render_ad_v4.py --variation TEST
```

Reference implementation:
`03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-07_SecondPropertyLadder_AdProduction\06_EDIT_DIRECTION_BRIEFS\desktop_render\render_ad_v4.py`

A variation spec is the whole ad:

```python
"TEST": dict(
    blocks=["hook", "cost", "swap", "bench", "proof"],   # argument order
    beats=[
        dict(at="you take a 25", dev="cost_stack", secs=3.4, lead=-0.2,
             backdrop="heartland_roofs.mp4", params=dict(items=[...])),
        dict(at="that same money", dev=None, secs=2.6,
             backdrop="cityscape.mp4", split=True),      # pure b-roll insert
    ],
)
```

Only build multiple variations when Edmund asks for them. Default is ONE ad.

## 5. Traps that have actually bitten

- **A PNG is one frame at t=0.** Fading it leaves that frame at alpha 0, and
  overlay's `eof_action=repeat` then holds it invisible. Loop it, or drop the
  fade. This has caused invisible graphics twice.
- **`drawbox` evaluates size expressions once at init** — a time-based width
  paints a full border for the whole video. Use sliding `overlay` bars.
- **Never `-c copy` the final concat.** A dimension or timebase mismatch
  silently drops the second file's audio; the CTA played mute end to end.
  Use the concat *filter*.
- **Scale every branch to 1080x1920.** A CTA left at crop size (404x720) broke
  the concat and took the audio with it.
- **`loop` counts at the input framerate** — pass `-framerate 30` on image
  inputs or a loop sized in 30fps frames runs 20% long.
- Whisper auto-detect put 55s of English into Malay. Force the language.

## 6. Growing the library

`python E:\REMOTION\ads\scan_devices.py` sweeps the swipe library, measures
new ads, flags the ones breaking current norms and renders review sheets.
It narrows hundreds of ads to a handful worth watching; it cannot name a
device — that still needs looking at a montage. When a new device is found,
add it to `devices.py`, log it in `DEVICE_LIBRARY.md`, and every variation
picks it up with no composer change. Same for a new move or transition in
`effects.py`.

## 7. Known gaps — state them, do not paper over them

- **Memes** need footage that is *recognisable*. Free stock faces read as
  stock, not as memes, and are not Singaporean. Real trending clips are
  copyrighted and this is paid media. The clean route is Edmund shooting his
  own reaction inserts.
- **Torn-paper split edge** (`devices.torn_split`) is built but not yet wired
  into the composer.
- **Document/desk inserts** (loan form, calculator, signing, SOLD sign) do not
  exist in the SG set; generate them as graphic plates or shoot them.
- **Caption face** is Impact. Anton / Archivo Black are the playbook faces and
  need local TTFs for ffmpeg.
