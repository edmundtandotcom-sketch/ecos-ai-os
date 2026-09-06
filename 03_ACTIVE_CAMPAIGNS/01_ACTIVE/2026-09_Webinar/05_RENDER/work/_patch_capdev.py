from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# helper: paste shot captions onto a device frame sequence
rep('''# ============================================================== compose
''', '''# ============================================================== compose

def burn_caps_into_device(devdir, t0, t1, shots):
    """Captions are burned into the SHOT, so an opaque plate (dread, icon
    compare, pin map, black type) would hide them. Paste each shot's caption
    plate onto the device frames it overlaps - the band then rides on top of
    every plate, and nothing single-image is ever overlaid on the timeline."""
    from PIL import Image
    frames = sorted(devdir.glob("*.png"))
    if not frames:
        return 0
    n = 0
    caps = [(sh["out0"], sh["out1"], sh["cap"]) for sh in shots
            if sh.get("cap") and sh["out1"] > t0 and sh["out0"] < t1]
    cache = {}
    for i, fpath in enumerate(frames):
        t = t0 + i / FPS
        hit = next((c for a, b, c in caps if a - 0.001 <= t < b), None)
        if not hit:
            continue
        if hit not in cache:
            cache[hit] = Image.open(hit).convert("RGBA")
        im = Image.open(fpath).convert("RGBA")
        im.alpha_composite(cache[hit])
        im.save(fpath)
        n += 1
    return n

''')

rep('''        d = devdir / f"{bi:02d}_{b['dev']}"
        DEVICES[b["dev"]](d, max(0.8, t1 - t0), **b.get("params", {}))
        dev_overlays.append((d, t0, t1))
        print(f"  device  {what:26} {t0:6.2f} -> {t1:6.2f}")''',
    '''        d = devdir / f"{bi:02d}_{b['dev']}"
        DEVICES[b["dev"]](d, max(0.8, t1 - t0), **b.get("params", {}))
        nb = burn_caps_into_device(d, t0, t1, shots)
        dev_overlays.append((d, t0, t1))
        print(f"  device  {what:26} {t0:6.2f} -> {t1:6.2f}  (+{nb} caption frames)")''')

p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("patched")

# spec: drop the redundant forest split beat (its window was already owned)
q = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\spec_webinar.py")
t = q.read_text(encoding="utf-8")
old = '''        dict(at="more than 20km", dev=None, secs=1.8, backdrop="sg_forest_leaves.mp4", split=True),
'''
assert t.count(old) == 1
q.write_text(t.replace(old, ""), encoding="utf-8")
print("spec: forest split beat removed")
