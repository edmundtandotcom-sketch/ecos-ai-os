from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# the whoosh IMPACT (peak at 0.89s into whoosh1.mp3) lands on the cut; the
# rise leads into it. adelay of the file start put the impact 0.3s late.
rep("PROGRESS_BAR = 12", "PROGRESS_BAR = 12\nWHOOSH_PEAK = 0.89   # seconds into whoosh1.mp3 where the impact sits")
rep('''    for i, t in enumerate(segs):
        f.append(f"[{3+i}:a]adelay={int(t*1000)}|{int(t*1000)},volume=0.45[wh{i}]")
        mixin += f"[wh{i}]"''',
    '''    for i, t in enumerate(segs):
        ms = max(0, int((t - WHOOSH_PEAK) * 1000))
        f.append(f"[{3+i}:a]adelay={ms}|{ms},volume=0.45[wh{i}]")
        mixin += f"[wh{i}]"''')
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("whoosh impact on the cut")
