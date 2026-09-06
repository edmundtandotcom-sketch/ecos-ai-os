from pathlib import Path

p = Path(r"C:\Users\Admin\.claude\projects\H--Shared-drives-00-E-C-O-S\memory\ads-not-reels-playbook.md")
s = p.read_text(encoding="utf-8")
s += """
**The "jerking" root cause (2026-09-05, measured):** the outdoor phone take
DROPS FRAMES IN BURSTS - runs of 6-7 identical frames at 30fps (frame-step
analysis: `work/_judder2.py`). Blend interpolation bridges a gap with a
cross-dissolve (ghosted hands); motion-compensated interpolation rebuilds
the motion. Tighten stage now runs `minterpolate=mi_mode=mci:mc_mode=obmc:
me_mode=bilat:search_param=16:scd=none` (about 10x realtime at 1080x1920;
default mci is 2x slower for no visible gain). Measure with a per-frame
mean-abs-diff series - a periodic near-zero step is a duplicate, a spike
right after is the catch-up.

**Work dirs on E:, never on H: (2026-09-05).** Drive File Stream locks a
freshly written file while it uploads it - `PermissionError [WinError 32]`
on unlink mid-pipeline. `render_webinar.WORK` is `E:\\REMOTION\\work\\...`;
only `out/` stays on the Drive. Same rule as CLAUDE.md section 7.
"""
p.write_text(s, encoding="utf-8")
print("memory")

p = Path(r"H:\Shared drives\00_E.C.O.S\.claude\skills\rei-ad-build\SKILL.md")
s = p.read_text(encoding="utf-8")
old = "## 6. Growing the library"
new = """- **Phone takes drop frames in bursts** (6-7 identical frames). Any speed
  change or even a straight cut looks jerky unless the tighten stage runs
  motion-compensated interpolation (`minterpolate ... mi_mode=mci ...
  me_mode=bilat:search_param=16`). Blend mode ghosts the hands. Check with
  a per-frame difference series before and after.
- **Work directory on E:, not on the Drive.** Drive File Stream locks files
  it is uploading; a 170-shot cache on H: will hit `WinError 32`.

## 6. Growing the library"""
assert s.count(old) == 1
p.write_text(s.replace(old, new), encoding="utf-8")
print("skill")
