from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")
old = '''WORK = HERE / "work"
OUT = HERE / "out"'''
new = '''# Working files live on the LOCAL disk. Drive File Stream locks freshly
# written files while it uploads them (PermissionError on unlink, 2026-09-05)
# and the shot cache is thousands of small encodes. Only out/ stays on Drive.
WORK = Path(r"E:\\REMOTION\\work\\webinar_2026-09")
OUT = HERE / "out"'''
assert s.count(old) == 1
s = s.replace(old, new)
# tolerate a locked stale segment: it gets overwritten by the encode anyway
old = '''        for old in segdir.glob("seg*.mp4"):
            old.unlink()'''
new = '''        for old in segdir.glob("seg*.mp4"):
            try:
                old.unlink()
            except PermissionError:
                pass    # locked by a sync client; the encode overwrites it'''
assert s.count(old) == 1
s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("WORK moved to E:")
