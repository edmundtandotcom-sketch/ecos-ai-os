from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# Every shot's audio ends a hair BEFORE its video. The concat demuxer offsets
# the next file by the longer stream; AAC frames are 21.3ms, video frames
# 33.3ms, so a longer audio track put the next shot off the frame grid and
# the CFR re-encode duplicated a frame at the cut (measured 2026-09-05).
rep('''            run(["ffmpeg", "-y", "-loglevel", "error", *ins, *aud, *ins_cap,
                 "-filter_complex", chain, "-map", "[v]", "-map", amap,
                 "-frames:v", str(nf), *ENC, str(p)])''',
    '''            a_end = nf / FPS - 0.012
            chain += f";[{amap}]atrim=end={a_end:.4f},asetpts=PTS-STARTPTS[a]"
            run(["ffmpeg", "-y", "-loglevel", "error", *ins, *aud, *ins_cap,
                 "-filter_complex", chain, "-map", "[v]", "-map", "[a]",
                 "-frames:v", str(nf), *ENC, str(p)])''')
# cache version bump so every shot re-encodes with the aligned audio
rep('''                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig,
                            "src_file": Path(tight).name}, sort_keys=True)''',
    '''                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig,
                            "src_file": Path(tight).name, "v": 2}, sort_keys=True)''')
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("audio aligned to the frame grid")
