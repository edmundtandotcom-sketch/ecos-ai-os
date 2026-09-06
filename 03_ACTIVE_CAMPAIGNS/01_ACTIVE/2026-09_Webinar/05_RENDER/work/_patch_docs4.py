from pathlib import Path

p = Path(r"H:\Shared drives\00_E.C.O.S\.claude\skills\rei-ad-build\SKILL.md")
s = p.read_text(encoding="utf-8")
old = "## 6. Growing the library"
new = """- **Shot audio must end just BEFORE the video** (`atrim=end=nf/30-0.012`).
  AAC frames are 21.3ms, video frames 33.3ms; if the audio track is the
  longer stream the concat demuxer offsets the next shot off the frame grid
  and the CFR re-encode duplicates a frame at the cut - a hitch on every
  other cut at 60 cuts/min.
- **One source per caption.** A shot owned by a plate gets its caption pasted
  onto the plate frames only, never burned into the shot as well - the two
  disagree by a frame at cue changes and print over each other.

## 6. Growing the library"""
assert s.count(old) == 1
p.write_text(s.replace(old, new), encoding="utf-8")
print("skill")

p = Path(r"C:\Users\Admin\.claude\projects\H--Shared-drives-00-E-C-O-S\memory\ads-not-reels-playbook.md")
s = p.read_text(encoding="utf-8")
s += """
**Two more cut-seam mechanisms (2026-09-05):** (1) a duplicated frame at
cuts came from shot AUDIO being the longer stream - AAC 21.3ms frames put
the concat offset off the 33.3ms video grid and the CFR re-encode filled the
gap with a held frame; trim each shot's audio to nf/30 - 0.012 so video is
always the longer stream. (2) captions on plate windows must have ONE
source - pasted onto the device frames only; burning them into the shot as
well double-prints at cue changes (plate and shot disagree by a frame).
Diagnose both with a per-frame mean-abs-diff series through each stage
(tight -> shot -> _cut -> _body -> final): the stage where the zero-step
appears is the culprit.
"""
p.write_text(s, encoding="utf-8")
print("memory")
