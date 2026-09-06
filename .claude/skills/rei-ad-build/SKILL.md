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
| `E:\REMOTION\ads\effects.py` | Camera moves, transitions, layouts, frame furniture, speaker treatments, and `HOUSE` defaults. |
| **`E:\REMOTION\ads\HOUSE_STYLE_ADS.md`** | **What OUR 128 delivered ads/reels actually do. Where it disagrees with the playbook, it wins - it is what Edmund already approved.** |
| `E:\REMOTION\ads\devices_house.py` | The 10 devices extracted from those finals: grid-paper plate, dread plate, metaphor illustrations, icon devices, black cold-open, burst opener, accumulating captions. |
| `E:\REMOTION\ads\MEME_EXPRESSION_LIBRARY.md` | The reaction/meme shot list - 28 entries Edmund performs (face, hands, props). Comic beats here are props + deadpan, not pulled faces. |

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

## 2b. ASSET FOLDERS - all under `E:\REMOTION\public`, each with `manifest.json`

| Folder | Use in a beat | Contents |
|---|---|---|
| `broll/stock` | `backdrop=` | 37 Singapore/neutral clips |
| `family/` | `photo=` | 24 family/profile stills - green-screen Edmund and transparent Cindior are compositable; real showflat photos are the proof inserts |
| `props/` | `prop=` (PNG slam) or `backdrop=` (clip) | SOLD stamp, SALE post, OPEN HOUSE sign, house icons, keys-in-hand clip, coin stacks |
| `vfx/` | `vfx="lightleak"\|"glitch"\|"burst"\|"celebrate"\|"transition"` | 18 black-ground overlays, screen-style via `effects.vfx_overlay` |
| `reactions/` | `backdrop=` for `meme_card` | **drop folder** for Edmund's own clips - shoot list in MEME_EXPRESSION_LIBRARY §6 |

Beat keys all live on the same dict:

```python
dict(at="returned 22", dev="stat_pop", secs=3.0, backdrop="sg_city_night.mp4",
     vfx="burst", vfx_secs=1.2, params=dict(value=22.9, label="a year")),
dict(at="her first", dev=None, secs=2.4, photo="family_showflat_real.jpg"),
dict(at="sold at", dev=None, secs=1.6, backdrop="sg_marinabay_towers.mp4",
     prop="prop_sold_stamp_5250892.png"),
```

Harvesting more: Pixabay via the in-app browser, same-origin `fetch()`, take
the **`og:image`** tag (never the first CDN URL - often a related thumbnail),
and **eyeball every batch** before promoting - 24 of 59 were rejected on sight.

## 2c. Review-round rules (Edmund, 2026-09-05)

- **Captions on every shot, one band, always.** A plate never replaces the
  caption - the viewer loses the audio. Plates leave the band clear
  (`cap_y` per beat when they cannot).
- **Speed in the tighten stage with frame blending**, never `setpts` on
  the final - that judders. Deliver 1.15x and 1.20x when asked to compare.
- **Condos only** for a condo pitch - no HDB blocks in the inserts.
- Illustrate a radius claim (`pin_radius`), a forest claim with forest, an
  MRT claim with a train. Literal beats generic.
- Faster bed for a fast cut (`bed_powerful_beat_123`).

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

## 3b. Native 9:16 phone takes (webinar campaign, 2026-09)

`03_ACTIVE_CAMPAIGNS/01_ACTIVE/2026-09_Webinar/05_RENDER/render_webinar.py` is
the composer for takes already shot vertical: no face crop, zoom levels are
crops around the measured face centre, the tighten stage re-orders takes
(`PIECES` in `spec_webinar.py` is the edit order), and beats carry
`treat=` (red/bw duotone), `frame=` (CTA red border), `motion=`, `nocap=`,
an `endcard`. Cues are split at beat boundaries so every beat opens on its
own shot. Shots are cached by content hash - a spec tweak re-encodes only
what changed.

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

- **A single-image input does NOT survive a long timeline on ffmpeg 8.1.2.**
  Whatever holds it - `loop`, `tpad=clone`, `-stream_loop`, plain
  `eof_action=repeat` - the overlay stops compositing a few seconds in (a
  plate drew at 4.2s and never at 7.0s, no fade, no `enable`; webinar ad
  2026-09-04, four renders). PNG *sequences* (`%04d.png`) are fine at any
  time, and so is the same PNG on a clip whose timestamps start at zero.
  So: **burn caption plates into their own shot at shot-render time**
  (`render_webinar.render_shots` does this); reserve the assembled-timeline
  overlay pass for multi-frame device sequences and VFX clips.
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
- **ffmpeg 8.1.2 `blend` access-violates (0xC0000005)** whatever the input
  lengths. Screen-style VFX = luma-to-alpha `alphamerge` + plain `overlay`,
  clip looped for the whole cut. `effects.vfx_overlay` already does this.

- **Windows caps a command line at 32K chars.** 114 looped caption inputs
  with absolute Drive paths blew it (`WinError 206`). Write the graph with
  `-filter_complex_script`, run ffmpeg with `cwd=work` and relative inputs.

- **Phone takes drop frames in bursts** (6-7 identical frames). Any speed
  change or even a straight cut looks jerky unless the tighten stage runs
  motion-compensated interpolation (`minterpolate ... mi_mode=mci ...
  me_mode=bilat:search_param=16`). Blend mode ghosts the hands. Check with
  a per-frame difference series before and after.
- **Work directory on E:, not on the Drive.** Drive File Stream locks files
  it is uploading; a 170-shot cache on H: will hit `WinError 32`.

- **Shot audio must end just BEFORE the video** (`atrim=end=nf/30-0.012`).
  AAC frames are 21.3ms, video frames 33.3ms; if the audio track is the
  longer stream the concat demuxer offsets the next shot off the frame grid
  and the CFR re-encode duplicates a frame at the cut - a hitch on every
  other cut at 60 cuts/min.
- **One source per caption.** A shot owned by a plate gets its caption pasted
  onto the plate frames only, never burned into the shot as well - the two
  disagree by a frame at cue changes and print over each other.

- **`minterpolate` repeats its first and last frames** (it needs two to
  interpolate). Per-segment interpolation therefore leaves 2 held frames on
  each side of every tighten join - and shots start on joins. Interpolate
  with 2 source frames of context on each side and trim them
  (`trim=start_frame=lead:end_frame=lead+n`); cut the audio from the exact
  range as a second input.

- **SYNC BY CONSTRUCTION - the rule that replaces all the seam fixes above.**
  Never build the ad's audio from per-shot or per-segment AAC files. Every
  AAC encode leaves a ~30ms timestamp gap at its seam; a player honours the
  gaps (so stage-by-stage checks pass) but the final filter graph packs the
  samples shut and the speech runs ~33ms late per cut - 1.8s by 50s, on
  EVERY round until 2026-09-05. The tighten stage now makes each segment
  EXACTLY N video frames and EXACTLY N*1600 samples of PCM; shots are cut
  video-only on the frame grid; the final mixes the ONE continuous wav.
  Assertions at each stage (segment frames, shot frames, cut frames vs
  timeline, tight audio vs frames) raise instead of shipping drift.
- **Audit before delivery, against the raw take:** speech offset (<=40ms),
  video offset on clean shots (0 frames), caption vs spoken word, whoosh
  impact on the cut, device starts on shot boundaries, held frames.
  `work/_final_audit2.py` is the template.
- Whoosh: `adelay` the file so its IMPACT (0.89s into whoosh1.mp3) lands on
  the cut, not its silent lead-in.

## 6. Growing the library

`python E:\REMOTION\ads\scan_devices.py` sweeps the swipe library, measures
new ads, flags the ones breaking current norms and renders review sheets.
It narrows hundreds of ads to a handful worth watching; it cannot name a
device — that still needs looking at a montage. When a new device is found,
add it to `devices.py`, log it in `DEVICE_LIBRARY.md`, and every variation
picks it up with no composer change. Same for a new move or transition in
`effects.py`.

## 7. House style - the rules that override the playbook

From `HOUSE_STYLE_ADS.md`. Apply these on top of section 1:

- **One word per cue, ~0.3s.** Captions that **accumulate** for the point
  ("IT'S -> IT'S EASY -> IT'S EASY TO RECOMMEND"); replacement for narration.
- **Highlight colour rotates per beat** (`effects.beat_colour`) - yellow, cyan,
  green, red, purple. Not one fixed accent. A serif payoff word is house style.
- **The first 2s are rarely the speaker.** Open on `burst_open`,
  `black_type_open`, a red project plate, or the speaker in `speaker_duotone`.
- **Plates are literal, not charts.** `metaphor_plate` (cage / gift / net /
  chair / facepalm), `dread_plate` for cost-of-holding, `grid_paper_plate` for
  the case-study price, `icon_attrition` for "the few who...".
- **Cross-pollinate.** Ads <-> reels <-> long-form. Dread and metaphor plates go
  into long-form as interstitials; map plates, MRT rail and VAKit charts come
  into ads compressed to 2-3s **in the ad palette, never the brand-colour world**.

## 8. Known gaps - state them, do not paper over them

- **Speaker backdrop.** Every one of the 128 finals is shot OUTDOORS
  (greenery, HDB courtyard, event banner). The grey-curtain S&P take is the
  outlier. This is a shoot note and the single biggest lift available.
- **Memes** still need *recognisable* footage. Three Asian reaction clips
  exist (`rx_*`), all neutral - fine for a "thinking" beat, not a comic one.
  Edmund's own reaction inserts remain the clean route.
- **Props and photos** (red house model, FOR SALE sign, family photo) are
  house style and need shooting.
- **Cartoon crowd** illustration needs assets; **real whip-pan** needs a
  physical camera move.
- **Torn-paper split edge** (`devices.torn_split`) is built but not yet wired
  into the composer.
- Fonts (Anton / Archivo Black / Barlow / Manrope) and generated Singapore
  document plates are **done**.
