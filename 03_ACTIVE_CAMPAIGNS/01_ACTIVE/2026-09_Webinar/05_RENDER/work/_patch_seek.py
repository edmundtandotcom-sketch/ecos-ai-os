from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# -ss written with 4 decimals rounded 44.566667 UP to 44.5667, and ffmpeg
# discards the frame whose pts is below the seek point: one shot in three
# started a frame late (audit 2026-09-05). Seek half a frame early instead;
# -frames:v keeps the count exact.
rep('''        src_in = ["-ss", f"{s['t0']:.4f}", "-to", f"{s['t1'] + 0.5 / FPS:.4f}", "-i", str(tight)]''',
    '''        src_in = ["-ss", f"{s['t0'] - 0.5 / FPS:.6f}", "-to", f"{s['t1'] + 0.5 / FPS:.6f}", "-i", str(tight)]''')
rep('''                            "src_file": Path(tight).name, "v": 3}, sort_keys=True)''',
    '''                            "src_file": Path(tight).name, "v": 4}, sort_keys=True)''')
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("seek fixed")
