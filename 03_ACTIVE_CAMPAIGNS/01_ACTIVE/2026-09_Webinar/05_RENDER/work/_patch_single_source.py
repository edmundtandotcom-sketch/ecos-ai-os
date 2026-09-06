from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# 1. a shot owned by a device beat keeps its plate for the DEVICE paste only;
#    it is not burned into the shot as well (double-drawn a frame apart at cue
#    changes -> "INTO UP..EXIT 2..MSON" garble, 2026-09-05)
rep('''        sh["cap"] = str(png)
        n_caps += 1''',
    '''        sh["cap"] = str(png)
        sh["cap_burn"] = not sh.get("dev")      # device shots: paste on the plate frames instead
        n_caps += 1''')
rep('''        cap = s.get("cap")
        cap_sig = hashlib.md5(Path(cap).read_bytes()).hexdigest() if cap else None''',
    '''        cap = s.get("cap") if s.get("cap_burn", True) else None
        cap_sig = hashlib.md5(Path(cap).read_bytes()).hexdigest() if cap else None''')
rep('''                          if k not in ("out0", "out1", "dev_id", "text", "cue", "segment_start", "cap")}''',
    '''                          if k not in ("out0", "out1", "dev_id", "text", "cue", "segment_start", "cap", "cap_burn")}''')

# 2. device runs for its whole owner window (every owner shot relies on it for the caption)
rep('''        t0 = owners[0]["out0"]
        t1 = min(owners[-1]["out1"], t0 + b["secs"] + 0.15)''',
    '''        t0 = owners[0]["out0"]
        t1 = owners[-1]["out1"]''')
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("single-source captions on device shots")
