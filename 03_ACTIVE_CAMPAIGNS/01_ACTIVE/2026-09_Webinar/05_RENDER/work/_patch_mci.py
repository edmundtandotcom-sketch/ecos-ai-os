from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")
old = '''    tag = f"_s{int(round(speed * 100))}"'''
new = '''    tag = f"_s{int(round(speed * 100))}m"   # m = motion-compensated'''
assert s.count(old) == 1
s = s.replace(old, new)
old = '''    if speed != 1.0:
        vf += f",setpts=PTS/{speed},minterpolate=fps={FPS}:mi_mode=blend"
        af = ["-af", f"atempo={speed}"]'''
new = '''    # The phone take drops frames in bursts (runs of 6-7 identical frames at
    # 30fps). Plain blend bridges the gap with a cross-dissolve (ghosted
    # hands); motion-compensated interpolation rebuilds the movement. bilat +
    # search_param 16 is ~10x realtime, half the cost of the default mci.
    if speed != 1.0:
        vf += (f",setpts=PTS/{speed},minterpolate=fps={FPS}:mi_mode=mci:mc_mode=obmc:"
               f"me_mode=bilat:search_param=16:scd=none")
        af = ["-af", f"atempo={speed}"]'''
assert s.count(old) == 1
s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("tighten now motion-compensated")
