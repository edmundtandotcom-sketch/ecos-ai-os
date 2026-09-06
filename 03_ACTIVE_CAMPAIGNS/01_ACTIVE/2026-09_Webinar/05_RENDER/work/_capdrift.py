"""Which caption is on device frame i, vs which shot is active at t0 + i/FPS,
vs what the final shows at that time."""
import json, subprocess
from pathlib import Path
from PIL import Image

B = Path(r"E:\REMOTION\work\webinar_2026-09\build_115")
OUT = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\out\WEBINAR_THOMSON_RESERVE_9x16_115.mp4")
W = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\work")
shots = json.load(open(B / "shots.json"))
# the "2 MIN" stat_pop device
devs = sorted((B / "dev").glob("*_stat_pop"))
d = devs[1]
frames = sorted(d.glob("*.png"))
print(d.name, len(frames), "frames")
# shots owning it
owners = [s for s in shots if s.get("dev") == "stat_pop" and 20 < s["out0"] < 30]
for s in owners:
    print(f"  shot {s['out0']:7.3f}-{s['out1']:7.3f}  {s['text']}")
t0 = owners[0]["out0"]
# make a strip: device frame i (with pasted caption) next to the final frame at t0+i/30 and the _cut frame
tiles = []
for i in (5, 30, 55, 80):
    t = t0 + i / 30
    im = Image.open(frames[i]).convert("RGBA")
    bg = Image.new("RGBA", im.size, (60, 60, 60, 255)); bg.alpha_composite(im)
    tiles.append(bg.convert("RGB").resize((216, 384)))
    for src in (B / "_cut.mp4", OUT):
        png = W / "_cd.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(src), "-frames:v", "1", "-vf", "scale=216:384", str(png)], check=True)
        tiles.append(Image.open(png).convert("RGB"))
    act = next((s for s in shots if s["out0"] - 0.001 <= t < s["out1"]), None)
    print(f"  frame {i:3d} t={t:7.3f}  active shot: {act['text'] if act else None}")
strip = Image.new("RGB", (216 * len(tiles), 384))
for k, tl in enumerate(tiles):
    strip.paste(tl, (k * 216, 0))
strip.save(W / "_capdrift.png")
print("strip: device | _cut | final, x4")
