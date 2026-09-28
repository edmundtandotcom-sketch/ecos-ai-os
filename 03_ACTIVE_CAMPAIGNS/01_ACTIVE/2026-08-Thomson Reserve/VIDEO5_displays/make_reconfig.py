# -*- coding: utf-8 -*-
"""A10 - the 1,485 study reconfiguration, as a three-frame display.
Frame A: as drawn.  Frame B: the three moves.  Frame C: after.
Geometry is read off FP p12 (plan_p12.png, 300 dpi crop) - all coords in that image's px."""
from PIL import Image, ImageDraw, ImageFont
import glob, os, math
OUT = "E:/REMOTION/work/thomson_compare/displays"; os.makedirs(OUT, exist_ok=True)
INK=(14,32,51); CREAM=(245,242,233); GOLD=(201,164,76); MUTE=(138,151,166); RED=(192,57,43); GREEN=(46,160,110); DARK=(6,16,28)
W, H = 1920, 1080
def font(sz, bold=False):
    pat = "BarlowCondensed-%s*.ttf" % ("Bold" if bold else "Regular")
    c = glob.glob(os.path.join(r"C:\Windows\Fonts", pat)) + glob.glob(os.path.expanduser(os.path.join("~","AppData","Local","Microsoft","Windows","Fonts", pat)))
    try: return ImageFont.truetype(c[0], sz)
    except Exception: return ImageFont.truetype("arialbd.ttf" if bold else "arial.ttf", sz)

plan = Image.open("E:/REMOTION/work/thomson_compare/pages/plan_p12.png").convert("RGB")
ZONE = (700, 1050, 2450, 2250)                       # the crop we annotate
# elements, in plan px
STUDY      = (1165, 1812, 1595, 2140)
WIW        = (1600, 1812, 1940, 2110)
MASTER     = (1105, 1135, 1960, 1605)
STUDY_DOOR = (1400, 1800, 1580, 1800)                  # opening in the study's top wall, hinge at x=1400
STUDY_RWALL= (1595, 1850, 1595, 2090)                  # the wall shared with the walk-in wardrobe
MASTER_DOOR= (1100, 1612, 1260, 1612)                  # opening on the corridor, hinge at x=1260
NEW_DOOR   = (1420, 1612, 1580, 1612)                  # proposed: shifted along the corridor

def frame(title, kicker, step):
    im = Image.new("RGB", (W,H), INK); d = ImageDraw.Draw(im); d.rectangle([0,0,W,12], fill=GOLD)
    d.text((60,30), kicker, font=font(26,True), fill=GOLD); d.text((60,58), title, font=font(50,True), fill=CREAM)
    d.text((W-60,44), "1,485 - DPS1 - Block 5 stack 22", font=font(26), fill=MUTE, anchor="ra")
    # zone card left
    d.rectangle([60,130,1300,850], fill=CREAM)
    crop = plan.crop(ZONE); s = min(1220/crop.width, 700/crop.height); crop = crop.resize((int(crop.width*s), int(crop.height*s)), Image.LANCZOS)
    ox, oy = 60+(1240-crop.width)//2, 130+(720-crop.height)//2; im.paste(crop, (ox,oy)); d = ImageDraw.Draw(im)
    M = lambda p: (ox+(p[0]-ZONE[0])*s, oy+(p[1]-ZONE[1])*s)
    # step panel right (ends above the PiP)
    d.rectangle([1340,130,1860,740], fill=DARK)
    for i, (n, txt) in enumerate((("1","Seal the study door"),("2","Open the wall into the wardrobe"),("3","Shift the master door along"))):
        on = (i < step); col = GOLD if on else MUTE
        d.ellipse([1364,160+i*120,1408,204+i*120], fill=col if on else DARK, outline=col, width=3); d.text((1386,182+i*120), n, font=font(26,True), fill=INK if on else col, anchor="mm")
        d.text((1424,166+i*120), txt, font=font(30,True), fill=col)
    return im, d, M, s

def box(d, M, r, col, w=5): d.rectangle([M((r[0],r[1])), M((r[2],r[3]))], outline=col, width=w)
def label(d, M, p, txt, col=CREAM, sz=26):
    x, y = M(p); f = font(sz,True); tw = d.textlength(txt, font=f)
    d.rounded_rectangle([x-tw/2-10,y-sz/2-6,x+tw/2+10,y+sz/2+6], radius=8, fill=DARK); d.text((x,y), txt, font=f, fill=col, anchor="mm")
def thick(d, M, seg, col, w): d.line([M((seg[0],seg[1])), M((seg[2],seg[3]))], fill=col, width=w)
def cross(d, M, seg, col=RED):
    (x0,y0),(x1,y1) = M((seg[0],seg[1])), M((seg[2],seg[3])); cx, cy = (x0+x1)/2, (y0+y1)/2
    for dx, dy in ((-22,-22),(22,-22)): d.line([cx+dx,cy+dy,cx-dx,cy-dy], fill=col, width=6)
def arrow(d, p0, p1, col, w=6):
    d.line([p0,p1], fill=col, width=w); ang = math.atan2(p1[1]-p0[1], p1[0]-p0[0])
    for sgn in (0.5,-0.5): d.line([p1,(p1[0]-math.cos(ang+sgn)*22, p1[1]-math.sin(ang+sgn)*22)], fill=col, width=w)
def tint(im, M, r, col, alpha=0.30):
    (x0,y0),(x1,y1) = M((r[0],r[1])), M((r[2],r[3])); reg = im.crop((int(x0),int(y0),int(x1),int(y1)))
    ov = Image.new("RGB", reg.size, col); im.paste(Image.blend(reg, ov, alpha), (int(x0),int(y0)))

# ---- A: as drawn
im, d, M, s = frame("As drawn", "A10 - RECONFIG 1 of 3 - AS DRAWN", 0)
box(d, M, STUDY, GOLD); box(d, M, WIW, MUTE); box(d, M, MASTER, MUTE)
thick(d, M, STUDY_DOOR, RED, 8); thick(d, M, MASTER_DOOR, RED, 8)
label(d, M, (1380,1980), "STUDY"); label(d, M, (1530,1290), "MASTER", MUTE, 22)
label(d, M, (1490,1745), "study door - to corridor", RED, 22); label(d, M, (1180,1660), "master door", RED, 22)
d.text((1364,540), "The study sits between the master's", font=font(26), fill=CREAM); d.text((1364,572), "wardrobe and the corridor.", font=font(26), fill=CREAM)
d.text((1364,620), "Its door opens to the corridor.", font=font(26), fill=GOLD)
im.save(f"{OUT}/R1_reconfig_as_drawn.png")

# ---- B: the moves
im, d, M, s = frame("Three moves", "A10 - RECONFIG 2 of 3 - THE MOVES", 3)
box(d, M, STUDY, GOLD); box(d, M, WIW, MUTE); box(d, M, MASTER, MUTE)
thick(d, M, STUDY_DOOR, RED, 8); cross(d, M, STUDY_DOOR); label(d, M, (1490,1745), "1  seal", RED, 24)
(x0,y0),(x1,y1) = M((STUDY_RWALL[0],STUDY_RWALL[1])), M((STUDY_RWALL[2],STUDY_RWALL[3]))
for y in range(int(y0), int(y1), 18): d.line([x0,y,x0,y+9], fill=GREEN, width=8)
arrow(d, M((1540,1990)), M((1650,1990)), GREEN); label(d, M, (1760,1900), "2  open", GREEN, 24)
thick(d, M, MASTER_DOOR, RED, 8); thick(d, M, NEW_DOOR, GREEN, 8); arrow(d, M((1270,1612)), M((1410,1612)), GOLD); label(d, M, (1340,1560), "3  shift", GOLD, 24)
im.save(f"{OUT}/R2_reconfig_moves.png")

# ---- C: after
im, d, M, s = frame("After - a second walk-in", "A10 - RECONFIG 3 of 3 - AFTER", 3)
tint(im, M, STUDY, GOLD, 0.35); d = ImageDraw.Draw(im)
box(d, M, STUDY, GOLD); box(d, M, WIW, GOLD); box(d, M, MASTER, MUTE)
thick(d, M, STUDY_DOOR, INK, 10)                                   # sealed: now wall
(x0,y0),(x1,y1) = M((STUDY_RWALL[0],STUDY_RWALL[1])), M((STUDY_RWALL[2],STUDY_RWALL[3])); d.line([x0,y0,x1,y1], fill=CREAM, width=10)  # opened: gap
thick(d, M, MASTER_DOOR, INK, 10); thick(d, M, NEW_DOOR, GREEN, 8)  # old door walled, new door
# new door arc
hx, hy = M((1580,1612)); r = (M((1580,1612))[0]-M((1420,1612))[0]); d.arc([hx-r,hy-r,hx+r,hy+r], 180, 270, fill=GREEN, width=4)
label(d, M, (1380,1980), "WARDROBE 2", GOLD, 26); label(d, M, (1530,1290), "MASTER SUITE", GOLD, 22)
d.text((1364,540), "Corridor  -  master door  -  bedroom", font=font(24), fill=CREAM); d.text((1364,572), "-  wardrobe  -  wardrobe 2.", font=font(24), fill=CREAM)
d.text((1364,620), "One suite, one entrance,", font=font(26), fill=GOLD); d.text((1364,652), "no study door on the corridor.", font=font(26), fill=GOLD)
d.text((1364,700), "His idea, read off the plan - check with the developer", font=font(20), fill=MUTE)
im.save(f"{OUT}/R3_reconfig_after.png")

# strip
fs = [f"{OUT}/R1_reconfig_as_drawn.png", f"{OUT}/R2_reconfig_moves.png", f"{OUT}/R3_reconfig_after.png"]
tiles = [Image.open(f).convert("RGB") for f in fs]
for t in tiles: t.thumbnail((640,360))
sh = Image.new("RGB", (1940, 380), "#ddd"); dr = ImageDraw.Draw(sh)
for i, (f, t) in enumerate(zip(fs, tiles)): sh.paste(t, (10+i*645, 18)); dr.text((10+i*645, 2), os.path.basename(f), fill="black")
sh.save(f"{OUT}/_reconfig_strip.png"); print("ok", [os.path.basename(f) for f in fs])
