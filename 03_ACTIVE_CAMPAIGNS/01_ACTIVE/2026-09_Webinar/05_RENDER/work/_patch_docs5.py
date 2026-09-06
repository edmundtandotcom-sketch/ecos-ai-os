from pathlib import Path

p = Path(r"H:\Shared drives\00_E.C.O.S\.claude\skills\rei-ad-build\SKILL.md")
s = p.read_text(encoding="utf-8")
old = "## 6. Growing the library"
new = """- **`minterpolate` repeats its first and last frames** (it needs two to
  interpolate). Per-segment interpolation therefore leaves 2 held frames on
  each side of every tighten join - and shots start on joins. Interpolate
  with 2 source frames of context on each side and trim them
  (`trim=start_frame=lead:end_frame=lead+n`); cut the audio from the exact
  range as a second input.

## 6. Growing the library"""
assert s.count(old) == 1
p.write_text(s.replace(old, new), encoding="utf-8")
print("skill")

p = Path(r"C:\Users\Admin\.claude\projects\H--Shared-drives-00-E-C-O-S\memory\ads-not-reels-playbook.md")
s = p.read_text(encoding="utf-8")
s += """
**The held frame at cuts was the interpolator's edge, not the concat
(2026-09-05, third pass):** minterpolate repeats its first and last frames,
so each tighten segment carried 2 held frames on each end, and shots start
on those joins. Fix in `tighten()`: interpolate with 2 source frames of
extra context each side, `trim` them off, take audio from the exact range
as a second input. The audio-trim fix (video must be the longer stream) is
still right and stays.
"""
p.write_text(s, encoding="utf-8")
print("memory")
