from pathlib import Path

# ---- device catalogue
p = Path(r"E:\REMOTION\ads\DEVICE_LIBRARY.md")
s = p.read_text(encoding="utf-8")
s += """
## CHANGELOG 2026-09-05 (webinar ad, Edmund's review round 1)

- **`pin_radius`** (devices_house.py) - location pin drops onto a stylised
  dark map with the MRT line; a yellow radius ring grows out with the label
  on its rim ("800M / OF THOMSON-EAST COAST LINE STATIONS"). Full frame,
  caption band left clear. Cross-pollinated from the long-form pin maps.
- **Captions on EVERY shot**, one band at 0.80 (0.86 on the speaker panel of
  a split; beats may set `cap_y` when a plate needs the band, e.g. dread
  0.90, versus_bars 0.88). Device shots are no longer caption-free - the
  viewer lost the audio the moment a plate came up.
- `caption_plate` orange box now hugs the glyph bbox (Anton sits low in its
  em box, the box used to float above the word). `punch_slam(y_frac=)` so the
  slam sits above the caption band instead of over the face.
- **Speed is applied in the tighten stage** with `setpts` + `minterpolate
  mi_mode=blend`, never on the final render: speeding a 30fps cut and
  sampling it back to 30fps drops every ~7th frame and the whole ad reads
  as jerking. `--speed 1.15 / 1.20` produce two files.
- Gaps: MAX_GAP 0.20, PAD_OUT 0.10, PAD_IN 0.07.
- **New b-roll (Pixabay, eyeballed)**: `sg_condo_cloudy`, `sg_condo_cranes`,
  `sg_cbd_boatquay`, `sg_mrt_condos` (train on a viaduct in front of condos,
  green cast corrected), `sg_forest_aerial` + `sg_forest_leaves` (tropical
  rainforest - not Singapore-specific but no foreign tell; used for Central
  Catchment). Rejected on sight: Pattaya beach towers, Hong Kong estates.
- **New beds** (`public/audio`): `bed_powerful_beat_123.mp3` (123 BPM
  future-bass, the webinar ad bed) and `bed_upbeat_corporate_120.mp3`.
  `rei_bed_pulse` reads slow under a 50-cuts/min ad.
"""
p.write_text(s, encoding="utf-8")
print("catalogue")

# ---- skill
p = Path(r"H:\Shared drives\00_E.C.O.S\.claude\skills\rei-ad-build\SKILL.md")
s = p.read_text(encoding="utf-8")
old = "## 3. Procedure"
new = """## 2c. Review-round rules (Edmund, 2026-09-05)

- **Captions on every shot, one band, always.** A plate never replaces the
  caption - the viewer loses the audio. Plates leave the band clear
  (`cap_y` per beat when they cannot).
- **Speed in the tighten stage with frame blending**, never `setpts` on
  the final - that judders. Deliver 1.15x and 1.20x when asked to compare.
- **Condos only** for a condo pitch - no HDB blocks in the inserts.
- Illustrate a radius claim (`pin_radius`), a forest claim with forest, an
  MRT claim with a train. Literal beats generic.
- Faster bed for a fast cut (`bed_powerful_beat_123`).

## 3. Procedure"""
assert s.count(old) == 1
s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
print("skill")

# ---- memory: bash heredoc trap (refines bash-quoting-backticks)
p = Path(r"C:\Users\Admin\.claude\projects\H--Shared-drives-00-E-C-O-S\memory\bash-quoting-backticks.md")
s = p.read_text(encoding="utf-8")
s += """

**2026-09-05 recurrence, worse than thought:** even a QUOTED heredoc
(`<<'EOF'`) in this harness behaves like a double-quoted string - an
apostrophe in prose ("DON'T"), a `\\\\n` escape, or a `$` inside the body
broke four patch scripts in one session ("unexpected EOF while looking for
matching quote", or a backslash-n turned into a real newline). Rule: any
script or file body with quotes, backslashes or dollars goes through the
Write tool to a file, then `python file.py` - never inline in Bash.
"""
p.write_text(s, encoding="utf-8")
print("memory")

# ---- ads memory: review-round learnings
p = Path(r"C:\Users\Admin\.claude\projects\H--Shared-drives-00-E-C-O-S\memory\ads-not-reels-playbook.md")
s = p.read_text(encoding="utf-8")
s += """
**Edmund's review of the webinar ad (2026-09-05):** "jerking" = speed-up
judder (setpts on a 30fps cut sampled back to 30fps drops a frame every
~0.23s) - speed now applied in the tighten stage with minterpolate blend,
delivered at 1.15x AND 1.20x to compare. "Captions do not display well" =
plates were replacing captions; now captions on every shot in one band at
0.80 with per-beat cap_y, orange box hugging the glyphs, slam moved above
the band. Condos only (no HDB) for a condo pitch; forest for a forest claim;
a train for an MRT claim; a pin+radius plate (`pin_radius`) for "within
800m"; tighter gaps (0.20/0.10/0.07); faster bed (123 BPM future-bass from
Pixabay, `bed_powerful_beat_123`).
"""
p.write_text(s, encoding="utf-8")
print("ads memory")
