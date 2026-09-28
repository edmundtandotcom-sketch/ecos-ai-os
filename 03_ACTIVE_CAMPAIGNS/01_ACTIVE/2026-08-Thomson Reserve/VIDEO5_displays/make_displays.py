# -*- coding: utf-8 -*-
"""Display templates for VIDEO 5 -- renders one real example of each so the
edit picks from a library instead of designing. 1920x1080, Part 2 palette.
Zones: content <= y850, subtitles y930-1040 / x160-1560, PiP 260px circle at (1740,880)."""
from PIL import Image, ImageDraw, ImageFont
import glob, os, json, math
D = "E:/REMOTION/public_thomson_reserve/compare"
OUT = "E:/REMOTION/work/thomson_compare/displays"
os.makedirs(OUT, exist_ok=True)
INK=(14,32,51); CREAM=(245,242,233); GOLD=(201,164,76); MUTE=(138,151,166); RED=(192,57,43); DARK=(6,16,28); TEAL=(64,160,170)
W, H = 1920, 1080

def font(sz, bold=False):
    pat = "BarlowCondensed-%s*.ttf" % ("Bold" if bold else "Regular")
    c = glob.glob(os.path.join(r"C:\Windows\Fonts", pat)) + glob.glob(os.path.expanduser(os.path.join("~", "AppData", "Local", "Microsoft", "Windows", "Fonts", pat)))
    try:
        return ImageFont.truetype(c[0], sz)
    except Exception:
        return ImageFont.truetype("arialbd.ttf" if bold else "arial.ttf", sz)

# ---------- site plan: strip the slide text, record stack coordinates (grid px -> image px)
S = 1.17
raw = Image.open(f"{D}/site/siteplan_clean.png").convert("RGB")
BG = raw.getpixel((int(1980*S), int(300*S)))
dr = ImageDraw.Draw(raw)
for (x0, y0, x1, y1) in [(40,40,740,115), (360,190,1385,372), (340,385,1305,455), (1530,25,1940,195)]:
    dr.rectangle([x0*S, y0*S, x1*S, y1*S], fill=BG)
CROP = (int(60*S), int(300*S), int(2010*S), int(1150*S))
raw = raw.crop(CROP)
raw.save(f"{D}/site/siteplan_clean_notext.png")
CX, CY = CROP[0], CROP[1]
def P(x, y): return (int(x*S)-CX, int(y*S)-CY)
STK = {
 "1": {"09":(1610,705),"01":(1650,730),"08":(1590,740),"02":(1655,760),"07":(1580,765),"03":(1650,790),"06":(1565,795),"04":(1640,815),"05":(1600,835)},
 "3": {"15":(1340,825),"16":(1375,838),"17":(1400,838),"18":(1430,825),"10":(1465,870),"11":(1440,880),"12":(1405,885),"13":(1380,890),"14":(1350,895)},
 "9": {"37":(1190,700),"38":(1225,690),"39":(1250,690),"40":(1280,675),"41":(1295,720),"42":(1270,740),"43":(1245,745),"44":(1225,745),"45":(1180,745)},
 "11":{"46":(1395,500),"47":(1425,505),"48":(1460,520),"49":(1490,525),"50":(1515,535),"55":(1385,555),"54":(1420,565),"53":(1450,575),"52":(1475,575),"51":(1500,585)},
 "7": {"32":(485,645),"31":(485,675),"30":(485,700),"29":(485,730),"28":(485,760),"33":(540,665),"34":(540,695),"35":(540,725),"36":(540,762)},
 "5": {"23":(632,790),"24":(665,800),"25":(695,805),"26":(725,810),"27":(750,825),"22":(632,850),"21":(665,858),"20":(695,860),"19":(740,878)},
}
BBOX = {"1":(1540,690,1680,850),"3":(1320,815,1480,920),"9":(1165,670,1305,765),"11":(1370,485,1545,605),"7":(450,635,565,785),"5":(595,775,775,905)}
json.dump({"scale_from_grid": S, "stacks": STK, "blocks": BBOX}, open(f"{D}/site/stack_coords.json", "w"), indent=1)

# ---------- views: crop the 8 photos + 4 key maps out of the composites
VIEWS = {25: ("VIEW 1 - SOUTH-EAST - CBD skyline", "VIEW 2 - SOUTH - MacRitchie & Orchard skyline"),
         26: ("VIEW 3 - SOUTH - MacRitchie & Orchard skyline", "VIEW 4 - SOUTH-WEST - low-rise landed & Windsor NP"),
         27: ("VIEW 5 - SOUTH-WEST/WEST - GCBA Windsor, Windsor NP, Bukit Timah (levels to 30)", "VIEW 6 - SOUTH-WEST/WEST - same (levels to 30)"),
         28: ("VIEW 7 - NORTH-WEST - SICC, Lower & Upper Peirce (levels to 30)", "VIEW 8 - SOUTH-EAST - MacRitchie, CBD & Orchard (levels to 30)")}
os.makedirs(f"{D}/views/photos", exist_ok=True); vi = 1; idx = {}
for p, pair in VIEWS.items():
    im = Image.open(f"{D}/views/view_p{p}_1.png").convert("RGB"); w, h = im.size
    for k, (y0, y1) in enumerate([(0.145, 0.575), (0.595, 0.99)]):
        im.crop((int(w*0.024), int(h*y0), int(w*0.55), int(h*y1))).save(f"{D}/views/photos/view{vi}.png"); idx[f"view{vi}"] = pair[k]; vi += 1
    im.crop((int(w*0.617), int(h*0.595), int(w*0.817), int(h*0.967))).save(f"{D}/views/photos/keymap_p{p}.png")
json.dump(idx, open(f"{D}/views/photos/INDEX.json", "w"), indent=1)

# ---------- helpers
def frame(title, kicker, tag=None):
    im = Image.new("RGB", (W, H), INK); d = ImageDraw.Draw(im); d.rectangle([0,0,W,12], fill=GOLD)
    d.text((60,30), kicker, font=font(26,True), fill=GOLD); d.text((60,58), title, font=font(50,True), fill=CREAM)
    if tag: d.text((W-60,44), tag, font=font(26), fill=MUTE, anchor="ra")
    return im, d
def zones(d):
    for x in range(160,1560,24): d.line([x,930,x+12,930], fill=MUTE); d.line([x,1040,x+12,1040], fill=MUTE)
    d.text((166,905), "subtitle zone", font=font(18), fill=MUTE)
    d.ellipse([1740-136,880-136,1740+136,880+136], outline=GOLD, width=4); d.text((1740,880), "PiP", font=font(30,True), fill=MUTE, anchor="mm")
def caption(d, a, b):
    f = font(46,True); wa = d.textlength(a, font=f); wb = d.textlength(b, font=f); tx = 860-(wa+wb)/2; ty = 960
    d.rounded_rectangle([tx-24,ty-10,tx+wa+wb+24,ty+56], radius=12, fill=DARK); d.text((tx,ty), a, font=f, fill=CREAM); d.text((tx+wa,ty), b, font=f, fill=GOLD)
def compass(d, cx, cy, r=44, facing=None):
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=DARK, outline=GOLD, width=3)
    for ang, lab in ((0,"N"),(90,"E"),(180,"S"),(270,"W")):
        a = math.radians(ang-90); d.text((cx+math.cos(a)*(r-14), cy+math.sin(a)*(r-14)), lab, font=font(20,True), fill=GOLD if lab=="N" else CREAM, anchor="mm")
    if facing is not None:
        a = math.radians(facing-90); d.line([cx,cy,cx+math.cos(a)*(r-6),cy+math.sin(a)*(r-6)], fill=RED, width=5)
def arrow(d, p0, p1, col=GOLD, w=5, label=None, lf=26):
    d.line([p0,p1], fill=col, width=w)
    for (a, b) in ((p0,p1),(p1,p0)):
        ang = math.atan2(a[1]-b[1], a[0]-b[0])
        for s in (0.5,-0.5): d.line([a,(a[0]-math.cos(ang+s)*18, a[1]-math.sin(ang+s)*18)], fill=col, width=w)
    if label:
        mx, my = (p0[0]+p1[0])/2, (p0[1]+p1[1])/2; f = font(lf,True); tw = d.textlength(label, font=f)
        d.rounded_rectangle([mx-tw/2-8,my-lf/2-6,mx+tw/2+8,my+lf/2+6], radius=8, fill=DARK); d.text((mx,my), label, font=f, fill=col, anchor="mm")
site = Image.open(f"{D}/site/siteplan_clean_notext.png").convert("RGB")
def site_fit(box):
    x0,y0,x1,y1 = box; s = min((x1-x0)/site.width, (y1-y0)/site.height); im = site.resize((int(site.width*s), int(site.height*s)), Image.LANCZOS)
    ox, oy = x0+((x1-x0)-im.width)//2, y0+((y1-y0)-im.height)//2
    return im, (ox,oy), (lambda p: (ox+p[0]*s, oy+p[1]*s))
def site_zoom(blk, pad=90, box=(60,130,1130,850)):
    bx0,by0,bx1,by1 = BBOX[blk]; cx0,cy0 = P(bx0-pad, by0-pad); cx1,cy1 = P(bx1+pad, by1+pad)
    crop = site.crop((cx0,cy0,cx1,cy1)); x0,y0,x1,y1 = box; s = min((x1-x0)/crop.width, (y1-y0)/crop.height)
    im = crop.resize((int(crop.width*s), int(crop.height*s)), Image.LANCZOS); ox, oy = x0+((x1-x0)-im.width)//2, y0+((y1-y0)-im.height)//2
    return im, (ox,oy), (lambda p: (ox+(P(*p)[0]-cx0)*s, oy+(P(*p)[1]-cy0)*s))
def ring(d, pt, r=22, col=RED): d.ellipse([pt[0]-r,pt[1]-r,pt[0]+r,pt[1]+r], outline=col, width=5)
def card(im, box, plan, maxw, maxh):
    d = ImageDraw.Draw(im); d.rectangle(box, fill=CREAM)
    p = Image.open(f"{D}/plans/{plan}").convert("RGB"); q = p.copy(); q.thumbnail((maxw, maxh))
    ox, oy = box[0]+((box[2]-box[0])-q.width)//2, box[1]+((box[3]-box[1])-q.height)//2; im.paste(q, (ox,oy))
    return p, q, (ox,oy)

# ======================================================================= TEMPLATES
def S1_site_full():
    im, d = frame("The site - six blocks", "S1 - SITE FULL - cluster highlight", "2 x 30-storey  -  4 x 21-storey")
    sp, off, M = site_fit((60,130,1860,850)); im.paste(sp, off); d = ImageDraw.Draw(im)
    for blk, col in (("5",GOLD),("7",GOLD),("1",TEAL),("3",TEAL),("9",TEAL),("11",TEAL)):
        b = BBOX[blk]; p0 = M(P(b[0],b[1])); p1 = M(P(b[2],b[3])); d.rectangle([p0,p1], outline=col, width=5); d.text((p0[0],p0[1]-30), f"BLK {blk}", font=font(26,True), fill=col)
    d.rectangle([60,780,560,850], fill=DARK); d.text((76,790), "LUXURY - private lift - 30 storeys", font=font(24,True), fill=GOLD); d.text((76,818), "CLASSIC - every 2 & 3-bed - 21 storeys", font=font(24,True), fill=TEAL)
    compass(d, 1800, 190); zones(d); caption(d, "Two blocks are thirty storeys. ", "Four are twenty-one."); im.save(f"{OUT}/S1_site_full.png")

def S2_site_zoom():
    im, d = frame("732 - BPS1 - Block 11 stack 54", "S2 - SITE ZOOM - one block, one stack", "floors #03 - #21")
    zi, off, M = site_zoom("11", pad=170, box=(60,130,1130,850)); im.paste(zi, off); d = ImageDraw.Draw(im)
    p = M(STK["11"]["54"]); ring(d, p, 26); q = M(STK["3"]["17"]); arrow(d, p, q, label="77-80 m"); compass(d, 1040, 220, 44, facing=180)
    d.rectangle([1180,130,1860,740], fill=DARK); y = 150
    for k, v in (("BLOCK - STACK","Block 11 - stack 54"),("FACE","SOUTH - across the north pool"),("IN FRONT","Block 3 at 77-80 m"),("FLOORS","#03 to #21"),("SUN","south - least direct"),("YOU'LL SEE","L5 the pool - L10 over Blk 3 - L21 its roofline")):
        d.text((1210,y), k, font=font(22,True), fill=GOLD); d.text((1210,y+28), v, font=font(30), fill=CREAM); y += 96
    d.text((1210,700), "read off the developer's site plan - confirm at the gallery", font=font(20), fill=MUTE)
    zones(d); caption(d, "Block 11, stack 54. ", "That's the pool-view showflat unit."); im.save(f"{OUT}/S2_site_zoom.png")

def S3_site_pip():
    im, d = frame("678 - BP1/BP3 - Block 1 east face", "S3 - SITE FULL + PiP ZOOM", "a third of the project faces outward")
    sp, off, M = site_fit((60,130,1860,850)); im.paste(sp, off); d = ImageDraw.Draw(im)
    for s in ("02","03"): ring(d, M(P(*STK["1"][s])), 16)
    zi, zoff, ZM = site_zoom("1", pad=120, box=(80,540,520,840)); d.rectangle([76,536,524,844], fill=DARK); im.paste(zi, zoff); d = ImageDraw.Draw(im)
    d.rectangle([76,536,524,844], outline=GOLD, width=4)
    for s in ("02","03"): ring(d, ZM(STK["1"][s]), 18)
    tgt = M(P(*STK["1"]["02"])); d.line([(524,690),(tgt[0]-18,tgt[1])], fill=GOLD, width=3)
    compass(d, 1800, 190, facing=90)
    d.rectangle([60,130,620,200], fill=DARK); d.text((76,140), "EAST face - Bright Hill Drive - 24 m to boundary", font=font(24,True), fill=CREAM)
    zones(d); caption(d, "Stacks 02 and 03 look ", "out, not in."); im.save(f"{OUT}/S3_site_pip.png")

def S4_view():
    im, d = frame("What stack 05 sees - SOUTH", "S4 - VIEW - drone photo, level marker", "TF p25 - developer drone")
    ph = Image.open(f"{D}/views/photos/view2.png").convert("RGB"); ph.thumbnail((1460,700)); im.paste(ph, (60,130)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([1560,130,1860,740], radius=10, fill=DARK); y = 150
    for lv, txt in (("5","rooftops"),("10","over the landed"),("15","over most of it"),("21","skyline")):
        col = GOLD if lv=="15" else MUTE; d.text((1590,y), f"LEVEL {lv}", font=font(32,True), fill=col); d.text((1590,y+38), txt, font=font(24), fill=col); y += 96
    d.text((1590,560), "2 & 3-bed stacks stop at 21", font=font(22), fill=MUTE); d.text((1590,590), "lift stacks go to 30", font=font(22), fill=MUTE)
    compass(d, 1800, 680, 44, facing=180)
    zones(d); caption(d, "At fifteen you're over the landed. ", "At twenty-one, that's the skyline."); im.save(f"{OUT}/S4_view.png")

def L1_layout_full():
    im, d = frame("732 - 2-Bed Premium + Study - BPS1", "L1 - LAYOUT FULL", "120 units - Classic Tier 1")
    card(im, (60,130,1460,850), "tr_732.png", 1360, 680); d = ImageDraw.Draw(im)
    d.rectangle([1500,130,1860,740], fill=DARK); y = 150
    for k, v in (("STRATA","68 sqm / 732 sqft"),("LABELLED","67.6 sqm"),("UNACCOUNTED","0.4 sqm"),("BALCONY","4.8 sqm - 7.1%"),("STACKS","1-04   3-11   11-54")):
        d.text((1520,y), k, font=font(22,True), fill=GOLD); d.text((1520,y+28), v, font=font(32), fill=CREAM); y += 112
    zones(d); caption(d, "Sixty-seven point six ", "out of sixty-eight."); im.save(f"{OUT}/L1_layout_full.png")

def L2_layout_spotlight():
    im, d = frame("732 - the study is in the bedroom", "L2 - LAYOUT SPOTLIGHT - dim + zone", "")
    p, q, (ox,oy) = card(im, (60,130,1460,850), "tr_732.png", 1360, 680)
    dim = Image.blend(q, Image.new("RGB", q.size, (120,118,110)), 0.55); im.paste(dim, (ox,oy))
    zone = (0.50,0.08,0.80,0.36); zx0,zy0,zx1,zy1 = int(q.width*zone[0]), int(q.height*zone[1]), int(q.width*zone[2]), int(q.height*zone[3])
    im.paste(q.crop((zx0,zy0,zx1,zy1)), (ox+zx0, oy+zy0)); d = ImageDraw.Draw(im); d.rectangle([ox+zx0,oy+zy0,ox+zx1,oy+zy1], outline=RED, width=5)
    d.rectangle([1500,130,1860,740], fill=DARK); d.text((1520,160), "STUDY - inside the master - 5.2 sqm", font=font(28,True), fill=CREAM)
    d.text((1520,220), "A desk. A chair. A shelf.", font=font(30), fill=CREAM); d.text((1520,260), "And it's in your bedroom.", font=font(30), fill=GOLD)
    zones(d); caption(d, "The study's ", "five point two square metres."); im.save(f"{OUT}/L2_layout_spotlight.png")

def L3_layout_split():
    im, d = frame("678 - the kitchen has no door", "L3 - LAYOUT SPLIT - plan + zoomed zone", "416 units")
    p, q, (ox,oy) = card(im, (60,130,900,850), "tr_678.png", 800, 680); d = ImageDraw.Draw(im)
    zone = (0.0,0.55,0.55,1.0); sx = q.width/p.width; zx0,zy0,zx1,zy1 = int(p.width*zone[0]), int(p.height*zone[1]), int(p.width*zone[2]), int(p.height*zone[3])
    d.rectangle([ox+zx0*sx, oy+zy0*sx, ox+zx1*sx, oy+zy1*sx], outline=RED, width=5)
    d.rectangle([940,130,1860,850], fill=CREAM); z = p.crop((zx0,zy0,zx1,zy1)); z = z.resize((int(z.width*2.2), int(z.height*2.2)), Image.LANCZOS); z.thumbnail((880,660))
    im.paste(z, (940+(920-z.width)//2, 130+(720-z.height)//2)); d = ImageDraw.Draw(im)
    d.line([(ox+zx1*sx, oy+zy0*sx),(940,130)], fill=RED, width=3); d.line([(ox+zx1*sx, oy+zy1*sx),(940,850)], fill=RED, width=3)
    d.rectangle([940,790,1860,850], fill=DARK); d.text((960,802), "KITCHEN - open - no door", font=font(30,True), fill=CREAM)
    zones(d); caption(d, "Cooking smells go one place: ", "the bedrooms."); im.save(f"{OUT}/L3_layout_split.png")

def L4_layout_areas():
    im, d = frame("732 - room by room", "L4 - LAYOUT + AREAS - numbers animate in", "TF p29")
    card(im, (60,130,1160,850), "tr_732_pins.png", 1060, 680); d = ImageDraw.Draw(im)
    d.rectangle([1200,130,1860,740], fill=DARK)
    rows = [("Living / dining","23.5"),("Master","10.9"),("Bedroom 2","8.9"),("Study","5.2"),("Master bath","5.1"),("Kitchen","4.9"),("Balcony","4.8"),("Bath 2","3.9"),("Store","0.4")]
    y = 160
    for i, (k, v) in enumerate(rows):
        col = CREAM if i < 7 else MUTE; d.text((1220,y), k, font=font(26), fill=col); d.text((1840,y), v, font=font(28,True), fill=GOLD if i < 7 else MUTE, anchor="ra"); y += 52
    d.line([1220,y+4,1840,y+4], fill=GOLD, width=2); d.text((1220,y+14), "labelled", font=font(28,True), fill=CREAM); d.text((1840,y+14), "67.6 / 68", font=font(34,True), fill=GOLD, anchor="ra")
    zones(d); caption(d, "Point four square metres ", "unaccounted for."); im.save(f"{OUT}/L4_layout_areas.png")

if __name__ == "__main__":
    for fn in (S1_site_full, S2_site_zoom, S3_site_pip, S4_view, L1_layout_full, L2_layout_spotlight, L3_layout_split, L4_layout_areas):
        fn(); print("ok", fn.__name__)
    fs = sorted(glob.glob(f"{OUT}/[SL]*.png")); tiles = [Image.open(f).convert("RGB") for f in fs]
    for t in tiles: t.thumbnail((640,360))
    sh = Image.new("RGB", (1300, (len(tiles)+1)//2*380+20), "#ddd"); dr = ImageDraw.Draw(sh)
    for i, (f, t) in enumerate(zip(fs, tiles)):
        x, y = 10+(i%2)*645, 10+(i//2)*380; sh.paste(t, (x,y+18)); dr.text((x,y+2), os.path.basename(f), fill="black")
    sh.save(f"{OUT}/_contact.png"); print("contact sheet", sh.size)
