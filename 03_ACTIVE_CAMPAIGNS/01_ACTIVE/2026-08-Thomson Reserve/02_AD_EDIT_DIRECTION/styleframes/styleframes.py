#!/usr/bin/env python3
"""Styleframes + motion previews for the Thomson Reserve x Daughter ad set.

Everything is rendered at 1080x1920. The speaker is a STAND-IN plate (the
selfie footage is unreachable from this environment); every device is placed
exactly where it would sit over the real footage, so framing, type sizes,
safe zones and face-avoidance are real even though the face is not.
"""
import math, os, random, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent          # 02_AD_EDIT_DIRECTION (fonts/, emoji/, assets/ live here; see prep_assets.py)
FONTS = ROOT / "fonts"
EMOJI = ROOT / "emoji"
ASSETS = ROOT / "assets"
OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True, parents=True)

W, H = 1080, 1920

# ---------------------------------------------------------------- palette
INK      = (11, 11, 15)        # #0B0B0F  black card ground (bold system)
INK2     = (20, 20, 26)
GOLD     = (255, 230, 0)       # #FFE600  signal yellow: numbers / prices (was gold)
GOLD2    = (255, 240, 120)
IVORY    = (255, 255, 255)     # white (was ivory)
WHITE    = (255, 255, 255)
ORANGE   = (255, 106, 0)       # caption boxed word (ADS_PLAYBOOK lock)
RED      = (255, 45, 45)
GREEN    = (46, 171, 110)
FOREST   = (8, 8, 12)          # near-black tint for interstitials (was forest green)
SAND     = (237, 230, 214)
SHADOW   = (0, 0, 0)

# ---------------------------------------------------------------- fonts
def _font(name, size, wght=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if wght is not None:
        try:
            f.set_variation_by_axes([wght] if "opsz" not in name else [14, wght])
        except Exception:
            pass
    return f

def ANTON(s):    return _font("Anton-Regular.ttf", s)
def ARCHIVO(s):  return _font("ArchivoBlack-Regular.ttf", s)
def BEBAS(s):    return _font("BebasNeue-Regular.ttf", s)
def SERIF(s):    return _font("PlayfairDisplay[wght].ttf", s, 800)
def SERIF_I(s):  return _font("DMSerifDisplay-Regular.ttf", s)
def INTER(s, w=600): return _font("Inter[opsz,wght].ttf", s, w)
def MONT(s, w=700):  return _font("Montserrat[wght].ttf", s, w)
def OSWALD(s, w=600): return _font("Oswald[wght].ttf", s, w)

def emoji(code, size=64):
    p = EMOJI / f"{code}.png"
    im = Image.open(p).convert("RGBA")
    return im.resize((size, size), Image.LANCZOS)

# ---------------------------------------------------------------- easing
def ease_out(t, p=3):  t = min(max(t, 0), 1); return 1 - (1 - t) ** p
def ease_in_out(t):    t = min(max(t, 0), 1); return t * t * (3 - 2 * t)
def overshoot(t, k=1.6):
    t = min(max(t, 0), 1); s = k
    t -= 1; return t * t * ((s + 1) * t + s) + 1

# ---------------------------------------------------------------- plates
def plate(seed=1, warm=False, zoom=1.0, dx=0, dy=0):
    """Stand-in for the selfie footage: warm room gradient, bokeh, soft
    head-and-shoulders silhouette with eye-line at ~38% and head ~16% tall."""
    rnd = random.Random(seed)
    top = np.array([46, 36, 32]) if warm else np.array([34, 38, 46])
    bot = np.array([92, 72, 58]) if warm else np.array([78, 84, 98])
    g = np.linspace(0, 1, H)[:, None, None]
    arr = (top * (1 - g) + bot * g).astype(np.uint8)
    arr = np.repeat(arr, W, axis=1)
    im = Image.fromarray(arr, "RGB")
    bok = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bok)
    for _ in range(14):
        x, y, r = rnd.randint(-100, W + 100), rnd.randint(-100, int(H * 0.55)), rnd.randint(40, 160)
        c = (220, 228, 240, rnd.randint(14, 36))
        bd.ellipse((x - r, y - r, x + r, y + r), fill=c)
    bok = bok.filter(ImageFilter.GaussianBlur(28))
    im = Image.alpha_composite(im.convert("RGBA"), bok)
    # window light from the left
    light = Image.new("L", (W, H), 0)
    ld = ImageDraw.Draw(light)
    ld.polygon([(0, 0), (int(W * 0.55), 0), (int(W * 0.25), H), (0, H)], fill=70)
    light = light.filter(ImageFilter.GaussianBlur(140))
    im = Image.composite(Image.new("RGBA", (W, H), (235, 240, 250, 255)), im, light.point(lambda v: v))
    # silhouette: eyes at 38% H, head 16% H tall
    sil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sil)
    eye_y = int(H * 0.38); head_h = int(H * 0.16); head_w = int(head_h * 0.74)
    cx = int(W * 0.5)
    top_y = eye_y - int(head_h * 0.42)
    body = (24, 26, 32, 255)
    sd.ellipse((cx - head_w // 2, top_y, cx + head_w // 2, top_y + head_h), fill=body)
    neck_y = top_y + int(head_h * 0.92)
    sd.rounded_rectangle((cx - 70, neck_y, cx + 70, neck_y + 120), 40, fill=body)
    sd.rounded_rectangle((cx - 330, neck_y + 90, cx + 330, H + 200), 180, fill=body)
    sil = sil.filter(ImageFilter.GaussianBlur(6))
    im = Image.alpha_composite(im, sil)
    # faint skin tone so the silhouette does not read as a hole
    face = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(face)
    fd.ellipse((cx - head_w // 2 + 14, top_y + 14, cx + head_w // 2 - 14, top_y + head_h - 10), fill=(140, 120, 104, 110))
    face = face.filter(ImageFilter.GaussianBlur(10))
    im = Image.alpha_composite(im, face)
    # vignette
    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse((-200, -100, W + 200, H + 300), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(220))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    im = Image.composite(im, dark, vig.point(lambda v: 90 + int(v * 0.65)))
    im = im.convert("RGB")
    if zoom != 1.0 or dx or dy:
        im = zoom_img(im, zoom, dx, dy)
    return im

def zoom_img(im, z, dx=0, dy=0, anchor=(0.5, 0.38)):
    w, h = im.size
    cw, ch = int(w / z), int(h / z)
    ax, ay = anchor
    x0 = int(w * ax - cw * ax) + dx; y0 = int(h * ay - ch * ay) + dy
    x0 = min(max(x0, 0), w - cw); y0 = min(max(y0, 0), h - ch)
    return im.crop((x0, y0, x0 + cw, y0 + ch)).resize((w, h), Image.LANCZOS)

_broll_cache = {}
def broll(name, cx=None, cy_top=330, darken=0.0, zoom=1.0):
    """9:16 crop from a deck/ebook page render. cx = source centre x."""
    key = (name, cx, cy_top, darken, zoom)
    if key in _broll_cache:
        return _broll_cache[key].copy()
    src = Image.open(ASSETS / f"{name}.png").convert("RGB")
    sw, sh = src.size
    if sw > sh:   # landscape deck page: avoid the logo strip at the top
        ch = sh - cy_top; cw = int(ch * W / H)
        cx = sw // 2 if cx is None else cx
        x0 = min(max(cx - cw // 2, 0), sw - cw)
        im = src.crop((x0, cy_top, x0 + cw, sh))
    else:
        cw = sw; ch = int(sw * H / W)
        y0 = min(max((sh - ch) // 2 if cx is None else cx, 0), sh - ch)
        im = src.crop((0, y0, cw, y0 + ch))
    im = im.resize((W, H), Image.LANCZOS)
    if zoom != 1.0:
        im = zoom_img(im, zoom, anchor=(0.5, 0.5))
    if darken:
        im = Image.blend(im, Image.new("RGB", (W, H), (8, 12, 18)), darken)
    _broll_cache[key] = im
    return im.copy()

def grade(im):
    """Clean+bright commercial: tiny S-curve, warmth, micro contrast."""
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.05)
    return im

# ---------------------------------------------------------------- drawing helpers
def shadow_text(draw_layer, xy, s, font, fill, anchor="la", blur=10, off=(0, 6), alpha=170):
    """Soft drop shadow + text. draw_layer is an RGBA image."""
    sh = Image.new("RGBA", draw_layer.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(sh)
    d.text((xy[0] + off[0], xy[1] + off[1]), s, font=font, fill=(0, 0, 0, alpha), anchor=anchor)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    draw_layer.alpha_composite(sh)
    ImageDraw.Draw(draw_layer).text(xy, s, font=font, fill=fill, anchor=anchor)

def rrect(layer, box, r, fill, outline=None, width=0, shadow=0):
    if shadow:
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + shadow, box[2], box[3] + shadow), r, fill=(0, 0, 0, 150))
        sh = sh.filter(ImageFilter.GaussianBlur(shadow * 1.6))
        layer.alpha_composite(sh)
    ImageDraw.Draw(layer).rounded_rectangle(box, r, fill=fill, outline=outline, width=width)

def text_w(font, s):
    b = font.getbbox(s); return b[2] - b[0]

def caption(layer, words, accent_idx, emo=None, y_frac=0.70, size=92, font_fn=ANTON,
            box_color=ORANGE, scale=1.0, rot=0, pop=1.0, box_scale=1.0, lines=None):
    """House ad caption: ALL CAPS white, ONE word in an orange rounded box,
    small emoji centred under the line. 2-3 words per cue.
    pop<1 animates the box scale-in; scale animates whole-line punch-in."""
    size = int(size * scale)
    f = font_fn(size)
    words = [w.upper() for w in words]
    gap = int(size * 0.28); pad_x = int(size * 0.22); pad_y = int(size * 0.10)
    widths = [text_w(f, w) for w in words]
    total = sum(widths) + gap * (len(words) - 1) + (2 * pad_x if accent_idx is not None else 0)
    x = (W - total) // 2
    cy = int(H * y_frac)
    asc, desc = f.getmetrics()
    line_h = asc + desc
    top = cy - line_h // 2
    for i, (w, wd) in enumerate(zip(words, widths)):
        if i == accent_idx:
            bx0, by0, bx1, by1 = x, top - pad_y + int(size * 0.08), x + wd + 2 * pad_x, top + line_h + pad_y - int(size * 0.06)
            if pop < 1:  # scale box about its centre
                cxm, cym = (bx0 + bx1) / 2, (by0 + by1) / 2
                hw, hh = (bx1 - bx0) / 2 * pop, (by1 - by0) / 2 * pop
                bx0, by0, bx1, by1 = cxm - hw, cym - hh, cxm + hw, cym + hh
            rrect(layer, (bx0, by0, bx1, by1), int(size * 0.18), box_color + (255,), shadow=8)
            if pop >= 0.6:
                shadow_text(layer, (x + pad_x, top), w, f, WHITE + (255,), blur=6, off=(0, 4), alpha=120)
            x += wd + 2 * pad_x + gap
        else:
            shadow_text(layer, (x, top), w, f, WHITE + (255,), blur=10, off=(0, 6), alpha=190)
            x += wd + gap
    if emo:
        e = emoji(emo, int(size * 0.72))
        layer.alpha_composite(e, (W // 2 - e.width // 2, top + line_h + int(size * 0.12)))
    return (top, top + line_h)

def caption_multiline(layer, cues, y_frac=0.70, size=92, **kw):
    """cues: list of (words, accent_idx) stacked lines."""
    f = ANTON(size); asc, desc = f.getmetrics(); lh = (asc + desc) * 1.08
    n = len(cues); start = y_frac - (n - 1) * lh / H / 2
    for i, (words, ai) in enumerate(cues):
        caption(layer, words, ai, y_frac=start + i * lh / H, size=size, **kw)

def eyebrow(layer, s, bg=(8, 8, 8), fg=GOLD, y_frac=0.13, size=46, font_fn=OSWALD, slide=1.0):
    f = font_fn(size, 700) if font_fn in (OSWALD, INTER, MONT) else font_fn(size)
    tw = text_w(f, s); pad = 34
    bw = tw + pad * 2; bh = int(size * 1.7)
    x0 = (W - bw) // 2; y0 = int(H * y_frac) - bh // 2
    x0 += int((1 - slide) * -W)
    rrect(layer, (x0, y0, x0 + bw, y0 + bh), 14, bg + (240,), shadow=10)
    ImageDraw.Draw(layer).text((x0 + bw // 2, y0 + bh // 2), s, font=f, fill=fg + (255,), anchor="mm")

def stand_in_tag(layer):
    f = INTER(26, 500)
    s = "stand-in plate · selfie footage goes here"
    tw = text_w(f, s)
    rrect(layer, (W - tw - 60, 40, W - 24, 92), 10, (0, 0, 0, 120))
    ImageDraw.Draw(layer).text((W - tw - 42, 66), s, font=f, fill=(255, 255, 255, 170), anchor="lm")

def whip_blur(im, amount=60):
    """Horizontal directional blur = whip-pan frame."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    acc = np.zeros_like(a); n = 0
    for s in range(-amount, amount + 1, 4):
        acc += np.roll(a, s, axis=1); n += 1
    out = Image.fromarray((acc / n).astype(np.uint8))
    return ImageEnhance.Brightness(out).enhance(1.08)

def flash(im, strength):
    if strength <= 0: return im
    return Image.blend(im.convert("RGB"), Image.new("RGB", im.size, (255, 250, 240)), min(strength, 1))

def compose(base, layer):
    return Image.alpha_composite(base.convert("RGBA"), layer).convert("RGB")

def new_layer():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))

def scrim(layer, y0, y1, alpha=160, color=(0, 0, 0)):
    """Vertical gradient scrim between y0..y1 (0 alpha at y0 -> alpha at y1)."""
    g = Image.new("L", (1, H), 0)
    px = g.load()
    for y in range(H):
        if y < y0: v = 0
        elif y > y1: v = alpha
        else: v = int(alpha * (y - y0) / max(1, (y1 - y0)))
        px[0, y] = v
    g = g.resize((W, H))
    col = Image.new("RGBA", (W, H), color + (255,))
    col.putalpha(g)
    layer.alpha_composite(col)

def torn_edge(layer, y, amp=14, seed=3, color=(0, 0, 0, 255), thickness=0):
    """Torn-paper seam at height y: jagged mask applied as a dark edge + light rim."""
    rnd = random.Random(seed)
    pts = []
    x = 0
    while x <= W:
        pts.append((x, y + rnd.randint(-amp, amp)))
        x += rnd.randint(18, 42)
    d = ImageDraw.Draw(layer)
    d.line(pts, fill=(255, 255, 255, 230), width=5)
    d.line([(px, py + 6) for px, py in pts], fill=(0, 0, 0, 120), width=10)

def tear_mask(y, amp=14, seed=3):
    rnd = random.Random(seed)
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
    pts = [(0, 0)]; x = 0
    while x <= W:
        pts.append((x, y + rnd.randint(-amp, amp))); x += rnd.randint(18, 42)
    pts += [(W, 0)]
    d.polygon(pts, fill=255)
    return m

def card_number(layer, xy, s, font, fill=GOLD, anchor="la"):
    shadow_text(layer, xy, s, font, fill + (255,), anchor=anchor, blur=8, off=(0, 5), alpha=150)

# ---------------------------------------------------------------- devices
def dev_receipt(layer, t=1.0, y=0.74):
    """Bottom-third 'proof ledger' card: PARC CLEMATIS bought -> sold -> +$375K.
    t animates the number roll-up and the card rise."""
    rise = int((1 - ease_out(t)) * 260)
    x0, y0, x1, y1 = 60, int(H * y) - 190 + rise, W - 60, int(H * y) + 150 + rise
    rrect(layer, (x0, y0, x1, y1), 28, INK + (242,), outline=GOLD + (110,), width=2, shadow=18)
    d = ImageDraw.Draw(layer)
    d.text((x0 + 40, y0 + 34), "PARC CLEMATIS", font=OSWALD(40, 600), fill=IVORY + (210,))
    d.text((x1 - 40, y0 + 34), "HER LAST PROPERTY", font=INTER(26, 500), fill=IVORY + (130,), anchor="ra")
    d.line((x0 + 40, y0 + 96, x1 - 40, y0 + 96), fill=GOLD + (80,), width=2)
    # roll-up numbers
    # a person lets each number land before the next one starts
    v_in  = 1.15  * ease_out(min(1, t / 0.30))
    v_out = 1.525 * ease_out(max(0, (t - 0.30) / 0.38))
    gain  = 375000 * ease_out(max(0, (t - 0.72) / 0.28))
    d.text((x0 + 40, y0 + 122), "BOUGHT", font=INTER(28, 600), fill=IVORY + (150,))
    card_number(layer, (x0 + 40, y0 + 156), f"${v_in:.2f}M", ANTON(78), fill=IVORY)
    # arrow
    ax = x0 + 400
    d.polygon([(ax, y0 + 200), (ax + 70, y0 + 200), (ax + 70, y0 + 182), (ax + 110, y0 + 212), (ax + 70, y0 + 242), (ax + 70, y0 + 224), (ax, y0 + 224)], fill=GOLD + (255,))
    d.text((x0 + 560, y0 + 122), "SOLD", font=INTER(28, 600), fill=IVORY + (150,))
    card_number(layer, (x0 + 560, y0 + 156), f"${v_out:.3f}M", ANTON(78), fill=GOLD)
    # gain pill
    if t > 0.72:
        s = f"+${gain:,.0f} FORWARD"
        f = ARCHIVO(40); tw = text_w(f, s)
        px0 = x1 - 40 - tw - 48; py0 = y1 - 86
        sc = overshoot(min(1, (t - 0.72) / 0.22))
        cxm, cym = px0 + (tw + 48) / 2, py0 + 34
        hw, hh = (tw + 48) / 2 * sc, 34 * sc
        rrect(layer, (cxm - hw, cym - hh, cxm + hw, cym + hh), 34, GOLD + (255,))
        if sc > 0.5:
            d.text((cxm, cym), s, font=f, fill=INK + (255,), anchor="mm")

def dev_dotgrid(layer, t=1.0, total=1268, lit=1066, cols=32, top=0.16, bottom=0.60):
    """1,268 dots; 84% of them light up orange = the competition lives next door."""
    rows = math.ceil(total / cols)
    x0, x1 = 90, W - 90
    y0, y1 = int(H * top), int(H * bottom)
    sx = (x1 - x0) / (cols - 1); sy = (y1 - y0) / (rows - 1)
    r = int(min(sx, sy) * 0.33)
    n_lit = int(lit * ease_in_out(t))
    d = ImageDraw.Draw(layer)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    k = 0
    for row in range(rows):
        for col in range(cols):
            if k >= total: break
            cx = x0 + col * sx; cy = y0 + row * sy
            if k < n_lit:
                gd.ellipse((cx - r * 1.8, cy - r * 1.8, cx + r * 1.8, cy + r * 1.8), fill=ORANGE + (70,))
                d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ORANGE + (255,))
            else:
                d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=IVORY + (70,))
            k += 1
    layer.alpha_composite(glow.filter(ImageFilter.GaussianBlur(10)))

def dev_bars(layer, t=1.0, y_top=0.46):
    """TEL story: +20.86% while building vs +5.87% after opening."""
    x0, x1 = 90, W - 90
    y0 = int(H * y_top)
    rrect(layer, (x0, y0, x1, y0 + 720), 28, INK + (236,), outline=GOLD + (90,), width=2, shadow=18)
    d = ImageDraw.Draw(layer)
    d.text((x0 + 44, y0 + 36), "PRICES WITHIN 800M OF TEL STATIONS", font=OSWALD(38, 600), fill=IVORY + (220,))
    d.line((x0 + 44, y0 + 96, x1 - 44, y0 + 96), fill=GOLD + (70,), width=2)
    bx = x0 + 44; bw = x1 - x0 - 88; base = y0 + 560; maxh = 330
    # bar 1
    h1 = int(maxh * ease_out(min(1, t * 1.6)))
    rrect(layer, (bx, base - h1, bx + bw * 0.42, base), 10, GOLD + (255,))
    if t > 0.3:
        card_number(layer, (bx + bw * 0.21, base - h1 - 20), "+20.86%", ANTON(74), fill=GOLD, anchor="mb")
    d.text((bx + bw * 0.21, base + 18), "4 YRS WHILE BUILDING", font=INTER(28, 600), fill=IVORY + (190,), anchor="ma")
    # bar 2
    t2 = max(0, (t - 0.5) / 0.5)
    h2 = int(maxh * (5.87 / 20.86) * ease_out(t2))
    rrect(layer, (bx + bw * 0.58, base - h2, bx + bw, base), 10, (120, 130, 150, 255))
    if t2 > 0.6:
        card_number(layer, (bx + bw * 0.79, base - h2 - 20), "+5.87%", ANTON(74), fill=IVORY, anchor="mb")
        d.text((bx + bw * 0.79, base + 18), "2 YRS AFTER OPENING", font=INTER(28, 600), fill=IVORY + (190,), anchor="ma")
    if t2 > 0.95:
        s = "UNDER 3% A YEAR"; f = ARCHIVO(36); tw = text_w(f, s)
        rrect(layer, (x1 - 44 - tw - 40, y0 + 116, x1 - 44, y0 + 180), 12, RED + (255,))
        d.text((x1 - 44 - 20, y0 + 148), s, font=f, fill=WHITE + (255,), anchor="rm")

def dev_pricegap(layer, t=1.0, y_top=0.50):
    """District proven $2.7-2.8M vs TR 3-bed est $3.2M+ -> $500K above."""
    x0, x1 = 70, W - 70; y0 = int(H * y_top)
    rrect(layer, (x0, y0, x1, y0 + 600), 28, INK + (240,), outline=GOLD + (90,), width=2, shadow=18)
    d = ImageDraw.Draw(layer)
    d.text((x0 + 44, y0 + 34), "3-BEDROOM · DISTRICT 20", font=OSWALD(38, 600), fill=IVORY + (220,))
    # ladder rails
    lx = x0 + 44; rx = x1 - 44; ly0 = y0 + 120; ly1 = y0 + 470
    d.line((lx, ly1, rx, ly1), fill=IVORY + (60,), width=2)
    # proven band
    pw = int((rx - lx) * 0.44)
    rrect(layer, (lx, ly1 - int(170 * ease_out(min(1, t * 1.5))), lx + pw, ly1), 12, (120, 130, 150, 255))
    d.text((lx + pw // 2, ly1 + 16), "RESALE · PROVEN", font=INTER(26, 600), fill=IVORY + (190,), anchor="ma")
    d.text((lx + pw // 2, ly1 + 50), "near MRT · top school · <10 yrs", font=INTER(22, 500), fill=IVORY + (130,), anchor="ma")
    if t > 0.3:
        card_number(layer, (lx + pw // 2, ly1 - 170 - 16), "$2.7–2.8M", ANTON(66), fill=IVORY, anchor="mb")
    # TR band
    t2 = max(0, (t - 0.4) / 0.6)
    th = int(260 * ease_out(t2))
    rrect(layer, (rx - pw, ly1 - th, rx, ly1), 12, GOLD + (255,))
    d.text((rx - pw // 2, ly1 + 16), "THOMSON RESERVE · EST.", font=INTER(26, 600), fill=IVORY + (190,), anchor="ma")
    d.text((rx - pw // 2, ly1 + 50), "$2,800–3,000 psf · nothing official yet", font=INTER(22, 500), fill=IVORY + (130,), anchor="ma")
    if t2 > 0.6:
        card_number(layer, (rx - pw // 2, ly1 - 260 - 16), "$3.2M+", ANTON(66), fill=GOLD, anchor="mb")
    if t2 > 0.9:
        # gap bracket
        gx = (lx + pw + rx - pw) // 2
        d.line((gx, ly1 - 170, gx, ly1 - 260), fill=RED + (255,), width=6)
        d.line((gx - 22, ly1 - 170, gx + 22, ly1 - 170), fill=RED + (255,), width=6)
        d.line((gx - 22, ly1 - 260, gx + 22, ly1 - 260), fill=RED + (255,), width=6)
        s = "+$500,000 ABOVE"; f = ARCHIVO(40); tw = text_w(f, s)
        rrect(layer, (x1 - 44 - tw - 40, y0 + 26, x1 - 44, y0 + 90), 12, RED + (255,))
        d.text((x1 - 44 - 20, y0 + 58), s, font=f, fill=WHITE + (255,), anchor="rm")

def dev_vs_split(base_left, base_right, seam=0.5, left_title="WHAT I DON'T LIKE", right_title="WHAT I LIKE",
                 left_items=(), right_items=(), t=1.0):
    """Two worlds, diagonal seam. seam = x fraction of the seam at mid-height."""
    out = base_left.convert("RGBA")
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
    sx = int(W * seam); skew = 90
    d.polygon([(sx + skew, 0), (W, 0), (W, H), (sx - skew, H)], fill=255)
    out = Image.composite(base_right.convert("RGBA"), out, m)
    layer = new_layer(); ld = ImageDraw.Draw(layer)
    ld.line((sx + skew, 0, sx - skew, H), fill=IVORY + (255,), width=6)
    # titles
    for title, col, x, items, anc in ((left_title, RED, 60, left_items, "la"), (right_title, GOLD, W - 60, right_items, "ra")):
        f = ARCHIVO(44); tw = text_w(f, title)
        bx0 = x if anc == "la" else x - tw - 40
        rrect(layer, (bx0, int(H * 0.14), bx0 + tw + 40, int(H * 0.14) + 72), 12, col + (255,), shadow=8)
        ld.text((bx0 + 20, int(H * 0.14) + 36), title, font=f, fill=(WHITE if col == RED else INK) + (255,), anchor="lm")
        yy = int(H * 0.14) + 110
        for k, it in enumerate(items):
            if k / max(1, len(items)) > t: break
            f2 = OSWALD(36, 600)
            n = f"{k + 1}"
            if anc == "la":
                rrect(layer, (x, yy, x + 44, yy + 44), 22, col + (255,))
                ld.text((x + 22, yy + 22), n, font=INTER(26, 700), fill=WHITE + (255,), anchor="mm")
                shadow_text(layer, (x + 60, yy + 22), it, f2, WHITE + (255,), anchor="lm", blur=8)
            else:
                rrect(layer, (x - 44, yy, x, yy + 44), 22, col + (255,))
                ld.text((x - 22, yy + 22), n, font=INTER(26, 700), fill=WHITE + (255,), anchor="mm")
                shadow_text(layer, (x - 60, yy + 22), it, f2, WHITE + (255,), anchor="rm", blur=8)
            yy += 64
    return compose(out, layer)

def dev_slam(layer, s="NOT YET.", t=1.0, y=0.52, size=230, color=WHITE, rot=-3):
    """Punch-slam: giant word scales in from 1.6x with a shadow, slight rotation."""
    sc = 1.6 - 0.6 * ease_out(min(1, t * 1.3), 4)
    f = ARCHIVO(int(size * sc))
    tmp = Image.new("RGBA", (W * 2, H), (0, 0, 0, 0))
    shadow_text(tmp, (W, int(H * y)), s, f, color + (255,), anchor="mm", blur=18, off=(0, 14), alpha=220)
    tmp = tmp.rotate(rot, resample=Image.BICUBIC, center=(W, int(H * y)))
    layer.alpha_composite(tmp.crop((W // 2, 0, W // 2 + W, H)))

def dev_interstitial(s_lines, accent_line, bg="deck_p04", t=1.0):
    """Fullscreen question card: forest-tinted b-roll, serif, one gold line, thin rule."""
    base = broll(bg, darken=0.72, zoom=1.0 + 0.04 * (1 - t))
    layer = new_layer(); d = ImageDraw.Draw(layer)
    # forest tint
    layer.alpha_composite(Image.new("RGBA", (W, H), FOREST + (120,)))
    f = SERIF(118)
    n = len(s_lines); lh = 136
    y = H // 2 - (n - 1) * lh // 2 - 40
    for i, line in enumerate(s_lines):
        if i / n > ease_out(t) + 0.01: break
        col = GOLD if i == accent_line else IVORY
        shadow_text(layer, (W // 2, y + i * lh), line, f, col + (255,), anchor="mm", blur=14, off=(0, 8))
    d.line((W // 2 - 60, y + n * lh + 10, W // 2 + 60, y + n * lh + 10), fill=GOLD + (255,), width=4)
    d.text((W // 2, y + n * lh + 60), "THE EXIT TEST", font=OSWALD(34, 500), fill=IVORY + (170,), anchor="mm")
    return compose(base, layer)

def dev_same_stack(layer, t=1.0, y_top=0.46):
    items = ["SAME MRT", "SAME SCHOOL", "SAME FACILITIES", "SAME PROJECT"]
    x0, x1 = 90, W - 90; y = int(H * y_top)
    d = ImageDraw.Draw(layer)
    for i, s in enumerate(items):
        ti = ease_out(min(1, max(0, (t * (len(items) + 1) - i))))
        if ti <= 0: continue
        slide = int((1 - ti) * 300)
        rrect(layer, (x0 + slide, y, x1 + slide, y + 104), 18, INK + (235,), outline=IVORY + (40,), width=1, shadow=10)
        d.text((x0 + slide + 36, y + 52), s, font=ANTON(64), fill=IVORY + (255,), anchor="lm")
        rrect(layer, (x1 + slide - 150, y + 32, x1 + slide - 36, y + 72), 20, (120, 130, 150, 255))
        d.text((x1 + slide - 93, y + 52), "× 1,066", font=INTER(24, 700), fill=WHITE + (255,), anchor="mm")
        y += 122
    if t > 0.92:
        s = "SO WHY HER UNIT?"; f = ARCHIVO(60); tw = text_w(f, s)
        rrect(layer, (W // 2 - tw // 2 - 30, y + 24, W // 2 + tw // 2 + 30, y + 118), 16, ORANGE + (255,), shadow=12)
        d.text((W // 2, y + 71), s, font=f, fill=WHITE + (255,), anchor="mm")

def dev_priceline(layer, t=1.0, y_top=0.47):
    """'Don't cross this' meter: a horizontal price rail with a red line and needle."""
    x0, x1 = 90, W - 90; y0 = int(H * y_top)
    rrect(layer, (x0, y0, x1, y0 + 520), 28, INK + (240,), outline=GOLD + (90,), width=2, shadow=18)
    d = ImageDraw.Draw(layer)
    d.text((x0 + 44, y0 + 36), "HER WALK-AWAY PRICE", font=OSWALD(38, 600), fill=IVORY + (220,))
    rail_y = y0 + 300; rx0 = x0 + 60; rx1 = x1 - 60
    rrect(layer, (rx0, rail_y - 14, rx1, rail_y + 14), 14, (60, 70, 90, 255))
    # green->red fill up to needle
    frac = ease_out(t)
    fill_x = rx0 + int((rx1 - rx0) * 0.68 * frac)
    rrect(layer, (rx0, rail_y - 14, fill_x, rail_y + 14), 14, GOLD + (255,))
    for k, lab in enumerate(["$2.6M", "$2.8M", "$3.0M", "$3.2M", "$3.4M"]):
        xx = rx0 + (rx1 - rx0) * k / 4
        d.line((xx, rail_y + 24, xx, rail_y + 40), fill=IVORY + (120,), width=2)
        d.text((xx, rail_y + 50), lab, font=INTER(24, 600), fill=IVORY + (160,), anchor="ma")
    # red line at 68%
    lx = rx0 + int((rx1 - rx0) * 0.68)
    if t > 0.85:
        d.line((lx, rail_y - 90, lx, rail_y + 90), fill=RED + (255,), width=8)
        s = "DON'T CROSS THIS"; f = ARCHIVO(40); tw = text_w(f, s)
        rrect(layer, (lx - tw // 2 - 24, rail_y - 170, lx + tw // 2 + 24, rail_y - 106), 12, RED + (255,), shadow=8)
        d.text((lx, rail_y - 138), s, font=f, fill=WHITE + (255,), anchor="mm")
        d.polygon([(lx - 14, rail_y - 106), (lx + 14, rail_y - 106), (lx, rail_y - 92)], fill=RED + (255,))
    d.text((x0 + 44, y0 + 440), "I don't care how crowded the showroom is.", font=SERIF_I(34), fill=IVORY + (190,))

def dev_ballot(layer, t=1.0, y_top=0.44):
    """Ballot-day: three stack tiles; A and B get stamped GONE, C glows 'still available' + $80K creep."""
    x0 = 90; tw_ = (W - 180 - 40) // 3; y0 = int(H * y_top)
    d = ImageDraw.Draw(layer)
    labels = ["PLAN A\n#12-07", "PLAN B\n#08-03", "THE ONE\nTHEY OFFER"]
    for i in range(3):
        bx0 = x0 + i * (tw_ + 20)
        rrect(layer, (bx0, y0, bx0 + tw_, y0 + 300), 22, INK + (240,), outline=IVORY + (50,), width=2, shadow=14)
        d.multiline_text((bx0 + tw_ // 2, y0 + 110), labels[i], font=OSWALD(40, 600), fill=IVORY + (230,), anchor="mm", align="center", spacing=8)
        d.text((bx0 + tw_ // 2, y0 + 220), ["3-BED · PREMIUM", "3-BED · STD", "2-BED · W-FACING"][i], font=INTER(22, 600), fill=IVORY + (140,), anchor="mm")
    for i, delay in ((0, 0.15), (1, 0.45)):
        ti = (t - delay) / 0.2
        if ti > 0:
            sc = 1.8 - 0.8 * ease_out(min(1, ti), 4)
            f = ARCHIVO(int(84 * sc)); bx0 = x0 + i * (tw_ + 20)
            tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(tmp).text((bx0 + tw_ // 2, y0 + 150), "GONE", font=f, fill=RED + (235,), anchor="mm")
            tmp = tmp.rotate(-12 if i == 0 else 9, resample=Image.BICUBIC, center=(bx0 + tw_ // 2, y0 + 150))
            layer.alpha_composite(tmp)
    if t > 0.75:
        bx0 = x0 + 2 * (tw_ + 20)
        ImageDraw.Draw(layer).rounded_rectangle((bx0 - 6, y0 - 6, bx0 + tw_ + 6, y0 + 306), 26, fill=None, outline=ORANGE + (255,), width=6)
        s = "STILL AVAILABLE"; f = ARCHIVO(28); tw2 = text_w(f, s)
        rrect(layer, (bx0 + tw_ // 2 - tw2 // 2 - 16, y0 - 50, bx0 + tw_ // 2 + tw2 // 2 + 16, y0 - 6), 10, ORANGE + (255,))
        d.text((bx0 + tw_ // 2, y0 - 28), s, font=f, fill=WHITE + (255,), anchor="mm")
    if t > 0.9:
        s = "“MAYBE WE CAN STRETCH ANOTHER  $80,000”"; f = SERIF_I(40)
        shadow_text(layer, (W // 2, y0 + 400), s, f, IVORY + (255,), anchor="mm", blur=10)
        s2 = "THAT'S THE DECISION I DON'T WANT HER MAKING"; f2 = OSWALD(34, 500)
        d.text((W // 2, y0 + 460), s2, font=f2, fill=GOLD + (255,), anchor="mm")

def dev_two_three(base_l, base_r, t=1.0):
    """2-BED vs 3-BED vertical split with buyer-pool bubbles."""
    out = base_l.convert("RGBA")
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rectangle((W // 2, 0, W, H), fill=255)
    out = Image.composite(base_r.convert("RGBA"), out, m)
    layer = new_layer(); d = ImageDraw.Draw(layer)
    d.line((W // 2, 0, W // 2, H), fill=IVORY + (255,), width=6)
    for i, (lab, cx, pool, col) in enumerate((("2-BED", W // 4, 11, (150, 160, 180)), ("3-BED", 3 * W // 4, 11, GOLD))):
        f = ARCHIVO(96)
        shadow_text(layer, (cx, int(H * 0.17)), lab, f, WHITE + (255,), anchor="mm", blur=14, off=(0, 8))
        d.text((cx, int(H * 0.23)), "WHO BUYS IT FROM HER?", font=OSWALD(30, 500), fill=IVORY + (190,), anchor="mm")
        rnd = random.Random(i + 7)
        n = int(pool * ease_out(t))
        for k in range(n):
            r = rnd.randint(22, 46)
            x = cx + rnd.randint(-200, 200); y = int(H * 0.52) + rnd.randint(-170, 170)
            d.ellipse((x - r, y - r, x + r, y + r), fill=col + (210,), outline=WHITE + (160,), width=2)
        d.text((cx, int(H * 0.68)), "?", font=ANTON(150), fill=col + (255,), anchor="mm")
        d.text((cx, int(H * 0.74)), "STRONGEST BUYER POOL AT EXIT", font=INTER(20, 600), fill=IVORY + (150,), anchor="mm")
    vs = ARCHIVO(70)
    rrect(layer, (W // 2 - 70, int(H * 0.40) - 70, W // 2 + 70, int(H * 0.40) + 70), 70, ORANGE + (255,), shadow=12)
    d.text((W // 2, int(H * 0.40)), "VS", font=vs, fill=WHITE + (255,), anchor="mm")
    return compose(out, layer)

def dev_checklist(layer, t=1.0, y_top=0.49):
    items = [("THE PRICE I WON'T CROSS", "1f6ab"), ("STACKS TO PICK · TO AVOID", "1f4cd"),
             ("2-BED OR 3-BED", "1f3e2"), ("PREP BEFORE BALLOT DAY", "1f5f3")]
    x0, x1 = 90, W - 90; y = int(H * y_top); d = ImageDraw.Draw(layer)
    for i, (s, e) in enumerate(items):
        ti = ease_out(min(1, max(0, t * (len(items) + 0.5) - i)))
        if ti <= 0: continue
        sl = int((1 - ti) * 120)
        rrect(layer, (x0, y + sl, x1, y + 92 + sl), 46, (255, 255, 255, 236), shadow=10)
        done = ti > 0.95 and (t * (len(items) + 0.5) - i) > 1.3
        rrect(layer, (x0 + 14, y + 14 + sl, x0 + 78, y + 78 + sl), 32, (GREEN if done else (200, 200, 200)) + (255,))
        if done:
            d.line((x0 + 30, y + 46 + sl, x0 + 42, y + 60 + sl, x0 + 64, y + 34 + sl), fill=WHITE + (255,), width=7, joint="curve")
        d.text((x0 + 100, y + 46 + sl), s, font=OSWALD(40, 600), fill=INK + (255,), anchor="lm")
        layer.alpha_composite(emoji(e, 44), (x1 - 70, y + 24 + sl))
        y += 112

def dev_endcard(t=1.0):
    base = broll("deck_p06", cx=2250, darken=0.45, zoom=1.0 + 0.03 * (1 - t))
    layer = new_layer(); d = ImageDraw.Draw(layer)
    layer.alpha_composite(Image.new("RGBA", (W, H), INK + (120,)))
    scrim(layer, int(H * 0.30), int(H * 0.75), alpha=200, color=INK)
    # eyebrow
    f = OSWALD(34, 500); s = "LIVE 60-MINUTE WEBINAR"
    d.text((W // 2, int(H * 0.40)), s, font=f, fill=GOLD + (255,), anchor="mm")
    d.line((W // 2 - 50, int(H * 0.40) + 34, W // 2 + 50, int(H * 0.40) + 34), fill=GOLD + (255,), width=3)
    f = SERIF(96)
    shadow_text(layer, (W // 2, int(H * 0.46)), "Would I buy", f, IVORY + (255,), anchor="mm")
    shadow_text(layer, (W // 2, int(H * 0.52)), "Thomson Reserve", f, IVORY + (255,), anchor="mm")
    shadow_text(layer, (W // 2, int(H * 0.58)), "for my daughter?", f, GOLD + (255,), anchor="mm")
    # countdown chip
    s = "BEFORE THE PREVIEW · 17 OCT"; f = OSWALD(36, 600); tw = text_w(f, s)
    rrect(layer, (W // 2 - tw // 2 - 30, int(H * 0.645) - 34, W // 2 + tw // 2 + 30, int(H * 0.645) + 34), 34, (0, 0, 0, 0), outline=IVORY + (170,), width=2)
    d.text((W // 2, int(H * 0.645)), s, font=f, fill=IVORY + (255,), anchor="mm")
    # CTA button
    sc = overshoot(min(1, max(0, (t - 0.3) / 0.5)))
    s = "SAVE MY SEAT  ›"; f = ARCHIVO(50); tw = text_w(f, s)
    bw, bh = (tw + 120) * sc, 120 * sc
    cx, cy = W // 2, int(H * 0.74)
    rrect(layer, (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2), int(60 * sc), GOLD + (255,), shadow=16)
    if sc > 0.6:
        d.text((cx, cy), s, font=f, fill=INK + (255,), anchor="mm")
    d.text((W // 2, int(H * 0.80)), "Click the link below · free · live Q&A", font=INTER(28, 500), fill=IVORY + (190,), anchor="mm")
    # wordmark lockup
    d.text((W // 2, int(H * 0.90)), "LIVE · 60 MIN · FREE", font=OSWALD(30, 600), fill=IVORY + (200,), anchor="mm")
    return compose(base, layer)

def anatomy():
    """Caption-anatomy diagram: this one IS a diagram."""
    base = plate(2)
    layer = new_layer(); d = ImageDraw.Draw(layer)
    # safe zones
    for y0, y1, lab in ((0, int(H * 0.10), "TOP 10% — FB/IG UI, keep clear"), (int(H * 0.83), H, "BOTTOM 17% — caption/CTA UI overlaps here")):
        d.rectangle((0, y0, W, y1), fill=(0, 120, 255, 60))
        d.text((W // 2, (y0 + y1) // 2), lab, font=INTER(28, 600), fill=WHITE + (230,), anchor="mm")
    # eye-line
    d.line((0, int(H * 0.38), W, int(H * 0.38)), fill=(255, 220, 0, 220), width=3)
    d.text((30, int(H * 0.38) - 36), "EYE-LINE 38–42%", font=INTER(26, 700), fill=(255, 220, 0, 255))
    # face box
    hb = (W // 2 - 115, int(H * 0.38) - 130, W // 2 + 115, int(H * 0.38) + 180)
    d.rectangle(hb, outline=(255, 80, 80, 255), width=4)
    d.text((hb[2] + 14, hb[1]), "FACE BOX\nnothing ever\ncrosses this", font=INTER(24, 600), fill=(255, 120, 120, 255))
    # caption
    caption(layer, ["MY", "DAUGHTER", "MADE"], None, y_frac=0.665, size=92)
    caption(layer, ["$375,000"], 0, emo="1f4b0", y_frac=0.725, size=92)
    d.line((0, int(H * 0.70), W, int(H * 0.70)), fill=(0, 255, 160, 200), width=2)
    d.text((30, int(H * 0.70) + 8), "CAPTION LINE 65–74% · Anton · 92px @1080 · 2–3 words", font=INTER(24, 700), fill=(0, 255, 160, 255))
    d.text((30, int(H * 0.775) + 20), "ONE word boxed orange · emoji 0.7× under the line", font=INTER(24, 700), fill=ORANGE + (255,))
    # margins
    d.line((int(W * 0.06), 0, int(W * 0.06), H), fill=(255, 255, 255, 90), width=2)
    d.line((int(W * 0.94), 0, int(W * 0.94), H), fill=(255, 255, 255, 90), width=2)
    d.text((int(W * 0.06) + 8, int(H * 0.50)), "6% side margin", font=INTER(22, 600), fill=WHITE + (200,))
    eyebrow(layer, "WOULD I BUY THIS FOR MY DAUGHTER?", y_frac=0.13)
    d.text((W // 2, int(H * 0.165)), "banner from the script table · sits under the UI band", font=INTER(22, 600), fill=WHITE + (200,), anchor="mm")
    return compose(base, layer)

# ---------------------------------------------------------------- frames
def save(im, name):
    p = OUT / f"{name}.png"; im.save(p, optimize=True); print("wrote", p.name); return p

def F01():  # V1 hook 0.4s
    base = plate(1, zoom=1.08)
    layer = new_layer(); stand_in_tag(layer)
    eyebrow(layer, "WOULD I BUY THIS FOR MY DAUGHTER?")
    caption(layer, ["MY", "DAUGHTER", "MADE"], None, y_frac=0.665)
    caption(layer, ["$375,000"], 0, emo="1f4b0", y_frac=0.725)
    return compose(base, layer)

def F02():  # V1 receipt card
    base = plate(1, zoom=1.0)
    layer = new_layer(); stand_in_tag(layer)
    dev_receipt(layer, 1.0)
    return compose(base, layer)

def F03():  # whip frame
    a = plate(1, zoom=1.12); b = broll("deck_p06", cx=2250)
    mix = Image.blend(a, b, 0.45)
    return whip_blur(mix, 90)

def F04():  # torn split: b-roll top, speaker bottom
    top = broll("deck_p06", cx=2250, zoom=1.06)
    bot = plate(1, zoom=1.0)
    seam_y = int(H * 0.52)
    m = tear_mask(seam_y)
    out = Image.composite(top, bot.transform((W, H), Image.AFFINE, (1, 0, 0, 0, 1, -int(H * 0.16)), Image.BICUBIC), m)
    layer = new_layer(); torn_edge(layer, seam_y); stand_in_tag(layer)
    caption(layer, ["1,268", "UNITS"], 0, emo="1f3e2", y_frac=0.74)
    eyebrow(layer, "THOMSON RESERVE · 1,268 UNITS · 2 COLLECTIONS", y_frac=0.13, size=30, bg=GOLD, fg=INK)
    return compose(out, layer)

def F05():  # dot grid 84%
    base = broll("deck_p17", darken=0.78)
    layer = new_layer()
    dev_dotgrid(layer, 1.0)
    d = ImageDraw.Draw(layer)
    card_number(layer, (W // 2, int(H * 0.675)), "84%", ANTON(220), fill=ORANGE, anchor="mm")
    caption(layer, ["ARE", "2", "&", "3-BEDROOMS"], 3, y_frac=0.77, size=78)
    caption(layer, ["YOUR", "COMPETITION", "LIVES", "NEXT", "DOOR"], 1, y_frac=0.83, size=56, box_color=RED)
    eyebrow(layer, "1,066 OF 1,268 UNITS", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    return compose(base, layer)

def F06():  # TEL bars
    base = broll("deck_p04", cx=1100, darken=0.62)
    layer = new_layer()
    eyebrow(layer, "YOU'RE BUYING AFTER THE MRT STORY", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    dev_bars(layer, 1.0, y_top=0.19)
    caption(layer, ["AFTER", "IT", "OPENED?"], 2, emo="1f4c9", y_frac=0.70)
    return compose(base, layer)

def F07():  # price gap
    base = plate(1, zoom=1.0)
    layer = new_layer(); stand_in_tag(layer)
    dev_pricegap(layer, 1.0, y_top=0.50)
    return compose(base, layer)

def F08():  # likes VS split
    left = broll("deck_p17", darken=0.55, zoom=1.08)
    right = broll("deck_p16", darken=0.35, zoom=1.04)
    left = ImageEnhance.Color(left).enhance(0.35)
    out = dev_vs_split(left, right, seam=0.5,
                       left_items=("84% ONE UNIT TYPE", "AFTER THE MRT STORY", "$500K ABOVE DISTRICT"),
                       right_items=("MRT · 2-MIN WALK", "AI TONG < 1KM", "A FOREVER VIEW"))
    layer = new_layer()
    caption(layer, ["THREE", "REASONS"], 0, emo="1f9e0", y_frac=0.80)
    return compose(out, layer)

def F09():  # NOT YET slam with flash
    base = plate(1, zoom=1.20)
    base = flash(base, 0.18)
    layer = new_layer(); stand_in_tag(layer)
    layer.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 110)))
    dev_slam(layer, "NOT YET.", 1.0, y=0.62, size=210)
    eyebrow(layer, "“DAD, WOULD YOU BUY THOMSON RESERVE?”", y_frac=0.13, size=36, bg=GOLD, fg=INK)
    return compose(base, layer)

def F10():  # interstitial
    return dev_interstitial(["Who buys it", "from her", "next?"], 2)

def F11():  # same-same stack
    base = broll("deck_p11", cx=1400, darken=0.70, zoom=1.05)
    layer = new_layer()
    eyebrow(layer, "WHEN SHE EVENTUALLY SELLS…", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    dev_same_stack(layer, 1.0, y_top=0.22)
    caption(layer, ["SHE", "COMPETES", "WITH", "NEIGHBOURS"], 3, emo="1f3d9", y_frac=0.78, size=66)
    return compose(base, layer)

def F12():  # price line
    base = plate(1, zoom=1.0)
    layer = new_layer(); stand_in_tag(layer)
    dev_priceline(layer, 1.0, y_top=0.49)
    caption(layer, ["ONCE", "WE", "CROSS", "IT?"], 2, y_frac=0.785, size=68)
    caption(layer, ["WE", "WALK."], 1, y_frac=0.835, size=68, box_color=RED)
    return compose(base, layer)

def F13():  # ballot tiles
    base = broll("deck_p10", darken=0.70, zoom=1.0)
    layer = new_layer()
    eyebrow(layer, "BALLOT DAY · YOUR NUMBER IS CALLED", y_frac=0.13, size=38, bg=RED, fg=WHITE)
    dev_ballot(layer, 1.0, y_top=0.30)
    caption(layer, ["GONE.", "GONE.", "THEN…"], 2, y_frac=0.78, size=80)
    return compose(base, layer)

def F14():  # 2 vs 3 split
    l = broll("deck_p12", cx=900, darken=0.5); r = broll("deck_p18", cx=1800, darken=0.4)
    out = dev_two_three(l, r)
    layer = new_layer()
    caption(layer, ["WHICH", "SELLS", "EASIER?"], 1, emo="1f914", y_frac=0.84, size=78)
    return compose(out, layer)

def F15():  # checklist over selfie
    base = plate(1, zoom=1.06)
    layer = new_layer(); stand_in_tag(layer)
    eyebrow(layer, "NO FLUFF. I'LL SHOW YOU:", y_frac=0.44, size=40, bg=ORANGE, fg=WHITE)
    dev_checklist(layer, 1.0, y_top=0.49)
    caption(layer, ["LIVE", "·", "60", "MINUTES"], 2, y_frac=0.78, size=72)
    return compose(base, layer)

def F16():  # end card
    return dev_endcard(1.0)

def F17():
    return anatomy()

FRAMES = {
    "F01_V1_hook_0.4s": F01, "F02_V1_receipt_card": F02, "F03_whip_pan_frame": F03,
    "F04_V1_torn_split_insert": F04, "F05_V1_dotgrid_84pct": F05, "F06_V1_TEL_bars": F06,
    "F07_V1_price_gap": F07, "F08_V1_likes_VS_split": F08, "F09_V2_NOT_YET_slam": F09,
    "F10_V2_exit_interstitial": F10, "F11_V2_same_stack": F11, "F12_V3_price_line": F12,
    "F13_V3_ballot_GONE": F13, "F14_V4_2v3_split": F14, "F15_V5_checklist": F15,
    "F16_end_card": F16, "F17_caption_anatomy": F17,
}

# ---------------------------------------------------------------- animations
FFMPEG = None
def ffmpeg_bin():
    global FFMPEG
    if FFMPEG is None:
        import imageio_ffmpeg; FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
    return FFMPEG

def render_clip(name, fn, secs=None, fps=30, scale=0.5):
    secs = secs or getattr(fn, "secs", 3.0)
    """fn(t01, frame_idx) -> PIL RGB 1080x1920. Writes an mp4 (h264) at scale."""
    d = OUT / "anim" / name; d.mkdir(parents=True, exist_ok=True)
    for f in d.glob("*.jpg"): f.unlink()
    n = int(secs * fps)
    ow, oh = int(W * scale) & ~1, int(H * scale) & ~1
    for i in range(n):
        t = i / (n - 1)
        im = fn(t, i)
        im.resize((ow, oh), Image.LANCZOS).save(d / f"{i:04d}.jpg", quality=90)
    out = OUT / "anim" / f"{name}.mp4"
    subprocess.run([ffmpeg_bin(), "-y", "-loglevel", "error", "-framerate", str(fps),
                    "-i", str(d / "%04d.jpg"), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-crf", "23", "-preset", "medium", "-movflags", "+faststart", str(out)], check=True)
    for f in d.glob("*.jpg"): f.unlink()
    d.rmdir()
    print("clip", out.name, f"{out.stat().st_size/1024:.0f} KB")
    return out

def A1(t, i):  # hook: punch-in + caption pop + eyebrow slide
    z = 1.0 + 0.13 * ease_out(min(1, t * 2.5), 4)
    base = plate(1, zoom=z)
    base = flash(base, max(0, 0.35 - t * 3))
    layer = new_layer()
    eyebrow(layer, "WOULD I BUY THIS FOR MY DAUGHTER?", slide=ease_out(min(1, (t - 0.05) / 0.3)))
    if t > 0.08:
        caption(layer, ["MY", "DAUGHTER", "MADE"], None, y_frac=0.665, scale=1 + 0.15 * (1 - ease_out(min(1, (t - 0.08) / 0.12))))
    if t > 0.42:
        caption(layer, ["$375,000"], 0, emo="1f4b0", y_frac=0.725, pop=overshoot(min(1, (t - 0.42) / 0.18)))
    return compose(base, layer)

def A2(t, i):  # whip pan selfie -> aerial
    if t < 0.4:
        base = plate(1, zoom=1.0 + 0.04 * t)
        layer = new_layer(); caption(layer, ["THOMSON", "RESERVE"], 1, y_frac=0.70)
        im = compose(base, layer)
        if t > 0.3: im = whip_blur(im, int(140 * (t - 0.3) / 0.1))
        return im
    if t < 0.55:
        k = (t - 0.4) / 0.15
        a = plate(1); b = broll("deck_p06", cx=2250)
        mix = Image.blend(a, b, k)
        return whip_blur(mix, int(160 * (1 - abs(k - 0.5) * 2) + 40))
    base = broll("deck_p06", cx=2250, zoom=1.08 - 0.06 * ease_out((t - 0.55) / 0.45))
    layer = new_layer()
    if t > 0.6: caption(layer, ["1,268", "UNITS"], 0, emo="1f3e2", y_frac=0.74, scale=1 + 0.12 * (1 - ease_out(min(1, (t - 0.6) / 0.12))))
    return compose(base, layer)

def A3(t, i):  # receipt roll-up
    base = plate(1, zoom=1.0 + 0.03 * t)
    layer = new_layer(); dev_receipt(layer, ease_out(min(1, t * 1.15)))
    return compose(base, layer)

def A4(t, i):  # dot-grid fill
    base = broll("deck_p17", darken=0.78, zoom=1.0 + 0.03 * t)
    layer = new_layer(); dev_dotgrid(layer, min(1, t * 1.25))
    if t > 0.78:
        sc = overshoot(min(1, (t - 0.78) / 0.15))
        card_number(layer, (W // 2, int(H * 0.675)), "84%", ANTON(int(220 * sc)), fill=ORANGE, anchor="mm")
    if t > 0.85:
        caption(layer, ["ARE", "2", "&", "3-BEDROOMS"], 3, y_frac=0.77, size=78)
    eyebrow(layer, "1,066 OF 1,268 UNITS", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    return compose(base, layer)

def A5(t, i):  # TEL bars + red flash on 'after'
    base = broll("deck_p04", cx=1100, darken=0.62, zoom=1.0 + 0.03 * t)
    if 0.74 < t < 0.80: base = flash(base, 0.5 * (1 - (t - 0.74) / 0.06))
    layer = new_layer()
    eyebrow(layer, "YOU'RE BUYING AFTER THE MRT STORY", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    dev_bars(layer, min(1, t * 1.1), y_top=0.19)
    if t > 0.5: caption(layer, ["AFTER", "IT", "OPENED?"], 2, emo="1f4c9", y_frac=0.70)
    return compose(base, layer)

def A6(t, i):  # white flash + NOT YET slam + zoom punch
    if t < 0.33:
        base = plate(1, zoom=1.0 + 0.02 * t)
        layer = new_layer(); caption(layer, ["WOULD", "YOU", "BUY", "IT?"], 2, emo="1f914", y_frac=0.70)
        return compose(base, layer)
    k = (t - 0.33) / 0.67
    base = plate(1, zoom=1.08 + 0.12 * ease_out(min(1, k * 2.2), 4))
    base = flash(base, max(0, 0.95 - k * 5))
    layer = new_layer()
    layer.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, int(110 * ease_out(min(1, k * 3))))))
    dev_slam(layer, "NOT YET.", min(1, k * 1.6), y=0.62, size=210)
    return compose(base, layer)

def A7(t, i):  # VS split wipe
    left = ImageEnhance.Color(broll("deck_p17", darken=0.55, zoom=1.08)).enhance(0.35)
    right = broll("deck_p16", darken=0.35, zoom=1.04)
    seam = 1.25 - 0.75 * ease_in_out(min(1, t * 1.6))
    out = dev_vs_split(left, right, seam=seam,
                       left_items=("84% ONE UNIT TYPE", "AFTER THE MRT STORY", "$500K ABOVE DISTRICT"),
                       right_items=("MRT · 2-MIN WALK", "AI TONG < 1KM", "A FOREVER VIEW"),
                       t=max(0, (t - 0.45) / 0.5))
    layer = new_layer()
    if t > 0.5: caption(layer, ["THREE", "REASONS"], 0, emo="1f9e0", y_frac=0.80)
    return compose(out, layer)

def A8(t, i):  # end card
    return dev_endcard(t)

CLIPS = {"A1_hook_punch_caption": A1, "A2_whip_pan_to_aerial": A2, "A3_receipt_rollup": A3,
         "A4_dotgrid_84pct": A4, "A5_TEL_bars_flash": A5, "A6_flash_NOT_YET_slam": A6,
         "A7_VS_split_wipe": A7, "A8_end_card": A8}


# ---------------------------------------------------------------- v2 additions (2026-10-04 feedback)
def dev_photo_card(layer, t=1.0, photo=None, caption_text="MY DAUGHTER", x_frac=0.80, y_frac=0.31, rot=-7, w=300):
    """Family photo as a tilted print that drops in. `photo` is a PIL image
    (a frame from C:\\Users\\Admin\\Pictures\\Family & Daughter on the desktop);
    here a neutral placeholder. Sits off the face: right column, above the chin."""
    h = int(w * 1.25)
    drop = int((1 - ease_out(t, 4)) * -520)
    cx, cy = int(W * x_frac), int(H * y_frac) + drop
    card = Image.new("RGBA", (w + 40, h + 110), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle((0, 0, w + 40, h + 110), 10, fill=(250, 250, 250, 255))
    if photo is None and PHOTOS:
        photo = PHOTOS[0]            # the hook photo is always the first in the folder
    if photo is None:
        cd.rectangle((20, 20, w + 20, h + 20), fill=(190, 196, 206, 255))
        cd.text(((w + 40) // 2, h // 2 + 20), "FAMILY PHOTO\nGOES HERE", font=INTER(24, 600), fill=(90, 96, 110, 255), anchor="mm", align="center")
    else:
        ph = photo.convert("RGB").resize((w, h), Image.LANCZOS)
        card.paste(ph, (20, 20))
    cd.text(((w + 40) // 2, h + 62), caption_text, font=OSWALD(24, 500), fill=(30, 30, 36, 255), anchor="mm")
    card = card.rotate(rot * ease_out(t), resample=Image.BICUBIC, expand=True)
    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    sm = Image.new("RGBA", card.size, (0, 0, 0, 0)); ImageDraw.Draw(sm).rectangle((0, 0, card.width, card.height), fill=(0, 0, 0, 0))
    a = card.split()[3]
    shadow = Image.new("RGBA", card.size, (0, 0, 0, 160)); shadow.putalpha(a)
    sh.alpha_composite(shadow, (cx - card.width // 2, cy - card.height // 2 + 18))
    layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    layer.alpha_composite(card, (cx - card.width // 2, cy - card.height // 2))

def caption_anim(layer, words, accent_idx, style, t, emo=None, y_frac=0.70, size=92, box_color=ORANGE):
    """Animated caption arrivals. style in: pop | slide | wordpop | shake | flip | typebox.
    t in [0,1] over the arrival (~8 frames); the cue then holds."""
    if style == "pop":            # whole line 1.15 -> 1.0
        caption(layer, words, accent_idx, emo=emo, y_frac=y_frac, size=size, box_color=box_color,
                scale=1 + 0.15 * (1 - ease_out(t)))
    elif style == "slide":        # line slides up 60px with fade; box pops after
        dy = int((1 - ease_out(t)) * 60)
        tmp = new_layer()
        caption(tmp, words, accent_idx, emo=emo, y_frac=y_frac, size=size, box_color=box_color,
                pop=overshoot(min(1, max(0, (t - 0.3) / 0.6))))
        tmp = tmp.transform((W, H), Image.AFFINE, (1, 0, 0, 0, 1, -dy))
        a = tmp.split()[3].point(lambda v: int(v * min(1, t * 2.5)))
        tmp.putalpha(a); layer.alpha_composite(tmp)
    elif style == "wordpop":      # words appear one by one, each with its own pop
        n = len(words); k = min(n, int(t * n) + 1)
        shown = words[:k]
        ai = accent_idx if (accent_idx is not None and accent_idx < k) else None
        local = (t * n) - (k - 1)
        caption(layer, shown, ai, emo=emo if k == n else None, y_frac=y_frac, size=size, box_color=box_color,
                scale=1 + 0.18 * (1 - ease_out(min(1, local))))
    elif style == "shake":        # red warning: 2-frame horizontal jitter then settle
        dx = int(math.sin(t * 40) * 14 * (1 - t))
        tmp = new_layer()
        caption(tmp, words, accent_idx, emo=emo, y_frac=y_frac, size=size, box_color=RED)
        layer.alpha_composite(tmp.transform((W, H), Image.AFFINE, (1, 0, -dx, 0, 1, 0)))
    elif style == "flip":         # box flips from black to accent colour (vertical squash)
        sq = abs(math.cos(t * math.pi)) if t < 0.5 else 1.0
        col = INK if t < 0.5 else box_color
        caption(layer, words, accent_idx, emo=emo, y_frac=y_frac, size=size, box_color=col,
                pop=max(0.6, sq))
    elif style == "typebox":      # box width wipes open left->right, word revealed inside
        caption(layer, words, accent_idx, emo=emo, y_frac=y_frac, size=size, box_color=box_color,
                pop=ease_out(t))

def F18():  # photo card over the hook
    base = plate(1, zoom=1.06)
    layer = new_layer(); stand_in_tag(layer)
    eyebrow(layer, "WOULD I BUY THIS FOR MY DAUGHTER?")
    dev_photo_card(layer, 1.0)
    caption(layer, ["MY", "DAUGHTER"], 1, emo="1f467", y_frac=0.70)
    return compose(base, layer)

def F19():  # caption animation bank, six styles at rest + mid-arrival
    base = Image.new("RGB", (W, H), (18, 18, 22))
    layer = new_layer(); d = ImageDraw.Draw(layer)
    d.text((W // 2, int(H * 0.06)), "CAPTION ARRIVALS — six styles, rotated per cue group", font=OSWALD(34, 600), fill=GOLD + (255,), anchor="mm")
    rows = [("pop", ["MY", "DAUGHTER", "MADE"], None, 0.55), ("slide", ["$375,000"], 0, 0.55), ("wordpop", ["NOT", "THE", "2-BEDDER"], 2, 0.75),
            ("shake", ["HIGH", "SUPPLY", "RISK"], 1, 0.3), ("flip", ["AFTER", "IT", "OPENED?"], 2, 0.45), ("typebox", ["84%", "ONE", "TYPE"], 0, 0.6)]
    for i, (st, ws, ai, tt) in enumerate(rows):
        y = 0.16 + i * 0.13
        d.text((60, int(H * y) - 70), st.upper() + f"   t={tt}", font=INTER(24, 600), fill=(150, 156, 170, 255))
        caption_anim(layer, ws, ai, st, tt, y_frac=y, size=76)
    return compose(base, layer)

FRAMES["F18_V1_family_photo_card"] = F18
FRAMES["F19_caption_arrival_bank"] = F19

def A9(t, i):   # caption arrival showcase: 6 cues, ~0.5s each, each a different style
    base = plate(1, zoom=1.0 + 0.04 * t)
    layer = new_layer()
    cues = [("pop", ["MY", "DAUGHTER", "MADE"], None, None), ("slide", ["$375,000"], 0, "1f4b0"),
            ("wordpop", ["NOT", "THE", "2-BEDDER"], 2, None), ("shake", ["HIGH", "SUPPLY", "RISK"], 1, "26a0"),
            ("flip", ["AFTER", "IT", "OPENED?"], 2, "1f4c9"), ("typebox", ["84%", "ONE", "TYPE"], 0, None)]
    k = min(5, int(t * 6)); local = (t * 6) - k
    st, ws, ai, em = cues[k]
    caption_anim(layer, ws, ai, st, min(1, local * 2.2), emo=em, y_frac=0.70)
    return compose(base, layer)

def A10(t, i):  # photo card drop-in on "my daughter"
    base = plate(1, zoom=1.0 + 0.06 * ease_out(min(1, t * 2)))
    layer = new_layer()
    eyebrow(layer, "WOULD I BUY THIS FOR MY DAUGHTER?", slide=ease_out(min(1, t * 3)))
    if t > 0.15: dev_photo_card(layer, min(1, (t - 0.15) / 0.35))
    if t > 0.25: caption_anim(layer, ["MY", "DAUGHTER"], 1, "wordpop", min(1, (t - 0.25) / 0.25), emo="1f467", y_frac=0.70)
    return compose(base, layer)

CLIPS["A9_caption_arrivals"] = A9
CLIPS["A10_family_photo_drop"] = A10


# ---------------------------------------------------------------- v1.2: human-edit rhythm preview + hand-drawn marks
PHOTOS = []          # real family photos, loaded by --photos <dir>; empty -> grey placeholder
_photo_cursor = 0
def load_photos(folder):
    """Load every jpg/png in a folder (e.g. C:\\Users\\Admin\\Pictures\\Family & Daughter),
    EXIF-rotated, centre-cropped to the card's 4:5. Order = filename order, so
    rename with a prefix (01_, 02_...) to control which photo lands first."""
    global PHOTOS
    from PIL import ImageOps
    out = []
    for f in sorted(Path(folder).iterdir()):
        if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".heic"):
            continue
        try:
            im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
        except Exception as e:
            print("skip", f.name, e); continue
        w, h = im.size; tw, th = w, int(w * 1.25)
        if th > h: th, tw = h, int(h / 1.25)
        x0, y0 = (w - tw) // 2, max(0, (h - th) // 3)   # bias up: faces sit high
        out.append(im.crop((x0, y0, x0 + tw, y0 + th)).resize((600, 750), Image.LANCZOS))
        PHOTOS_FULL.append(im)
    PHOTOS = out; print(f"photos: {len(out)} loaded from {folder}")

PHOTOS_FULL = []
def photo_full(idx, darken=0.0, zoom=1.0, anchor_y=0.45, anchor_x=0.5):
    """A family photo as a full-frame 9:16 insert (centre-crop, faces kept)."""
    if idx >= len(PHOTOS_FULL):
        return broll("deck_p06", cx=2250, darken=darken, zoom=zoom)
    im = PHOTOS_FULL[idx]; w, h = im.size
    cw = int(h * W / H)
    if cw <= w:
        x0 = int((w - cw) * anchor_x); im = im.crop((x0, 0, x0 + cw, h))
    else:
        ch = int(w * H / W); y0 = int((h - ch) * anchor_y); im = im.crop((0, y0, w, y0 + ch))
    im = grade(im.resize((W, H), Image.LANCZOS))
    if zoom != 1.0: im = zoom_img(im, zoom, anchor=(0.5, 0.5))
    if darken: im = Image.blend(im, Image.new("RGB", (W, H), (8, 12, 18)), darken)
    return im

def next_photo():
    """Rotate through the loaded photos; never the same one twice in a row."""
    global _photo_cursor
    if not PHOTOS: return None
    im = PHOTOS[_photo_cursor % len(PHOTOS)]; _photo_cursor += 1; return im

_PLATE = None
PLATE_FILE = None    # --plate <png>: a real frame grab from the selfie take replaces the silhouette
def plate_z(z=1.0, dx=0, dy=0):
    """Cached plate, re-framed per frame (fast enough for a 14s preview)."""
    global _PLATE
    if _PLATE is None:
        if PLATE_FILE:
            im = Image.open(PLATE_FILE).convert("RGB")
            sw, sh = im.size; cw = int(sh * W / H)
            if cw <= sw: im = im.crop(((sw - cw) // 2, 0, (sw - cw) // 2 + cw, sh))
            else:
                ch = int(sw * H / W); im = im.crop((0, max(0, (sh - ch) // 3), sw, max(0, (sh - ch) // 3) + ch))
            _PLATE = grade(im.resize((W, H), Image.LANCZOS))
        else:
            _PLATE = plate(1, zoom=1.0)
    return zoom_img(_PLATE, z, dx, dy)

def handheld(t, amp=2.0, seed=0.0):
    """1-2 px micro-shake at 2-4 Hz, two incommensurate sines so it never loops visibly."""
    return (int(round(amp * (math.sin(2 * math.pi * 2.3 * t + seed) + 0.5 * math.sin(2 * math.pi * 3.7 * t + 1.3 + seed)))),
            int(round(amp * (math.cos(2 * math.pi * 1.9 * t + 0.7 + seed) + 0.5 * math.sin(2 * math.pi * 4.1 * t + seed)))))

def scribble_underline(layer, x0, x1, y, t=1.0, color=GOLD, width=10, seed=5):
    """Hand-drawn underline: two slightly different strokes, drawn left->right over t."""
    rnd = random.Random(seed)
    d = ImageDraw.Draw(layer)
    for k, (dy, w) in enumerate(((0, width), (10, int(width * 0.8)))):
        pts = []
        n = 26
        for i in range(n + 1):
            f = i / n
            x = x0 + (x1 - x0) * f
            yy = y + dy + rnd.uniform(-5, 5) + 6 * math.sin(f * math.pi * 1.5 + k)
            pts.append((x, yy))
        m = max(2, int(len(pts) * min(1, max(0, t * 1.15 - 0.15 * k))))
        d.line(pts[:m], fill=color + (255,), width=w, joint="curve")

def hand_circle(layer, box, t=1.0, color=RED, width=9, seed=9):
    """Rough circle around a region: 1.15 turns, wobbly radius, drawn progressively."""
    rnd = random.Random(seed)
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    rx, ry = (x1 - x0) / 2 + 26, (y1 - y0) / 2 + 22
    pts = []
    n = 70
    for i in range(n + 1):
        a = -math.pi * 0.6 + i / n * math.pi * 2.3
        wob = 1 + rnd.uniform(-0.035, 0.035) + 0.03 * math.sin(a * 3)
        pts.append((cx + rx * wob * math.cos(a) + (i / n) * 14, cy + ry * wob * math.sin(a) + (i / n) * 8))
    m = max(2, int(len(pts) * min(1, max(0, t))))
    ImageDraw.Draw(layer).line(pts[:m], fill=color + (255,), width=width, joint="curve")

def cue(layer, t_now, t0, style, words, ai, emo=None, dur=0.27, **kw):
    if t_now >= t0:
        caption_anim(layer, words, ai, style, min(1, (t_now - t0) / dur), emo=emo, **kw)

def A11(t, i):
    """V1 hook as a HUMAN would cut it - 14.3s, varied shot lengths, breaths, a
    long hold on the proof card, one whip, one punch, hand-drawn underline.
    Captions time to Daughter Hook 1 at ~2.6 words/s."""
    T = t * 14.3
    hx, hy = handheld(T)
    layer = new_layer()
    # --- picture
    if T < 1.10:                                   # S1 raw open, flash in
        base = plate_z(1.00, hx, hy); base = flash(base, max(0, 0.6 - T * 6))
    elif T < 2.30:                                 # S2 jump cut, tighter
        base = plate_z(1.10, hx, hy)
    elif T < 6.90:                                 # S3 back out, long hold under the receipt card
        base = plate_z(1.00 + 0.04 * (T - 2.30) / 4.6, hx, hy)
    elif T < 7.05:                                 # whip out to the aerial
        k = (T - 6.90) / 0.15
        base = whip_blur(Image.blend(plate_z(1.04), broll("deck_p06", cx=2250), k), int(60 + 120 * (1 - abs(k - 0.5) * 2)))
    elif T < 8.60:                                 # S5 aerial, slow push
        base = broll("deck_p06", cx=2250, zoom=1.0 + 0.06 * (T - 7.05) / 1.55)
    elif T < 9.70:                                 # S6 punch in on the face
        k = min(1, (T - 8.60) / 0.27)
        base = plate_z(1.08 + 0.12 * ease_out(k, 4), hx, hy)
    elif T < 11.30:                                # S7 settle
        base = plate_z(1.10, hx, hy)
    elif T < 13.90:                                # S8 the question - hold, breathe
        base = plate_z(1.00 + 0.03 * (T - 11.30) / 2.6, hx, hy)
    else:                                          # whip-out to white = detachable hook end
        k = (T - 13.90) / 0.40
        base = flash(whip_blur(plate_z(1.03), int(40 + 160 * k)), k)
    # --- banner (hook only, leaves at the whip)
    if 0.20 <= T < 6.90:
        eyebrow(layer, "WOULD I BUY THIS FOR MY DAUGHTER?", slide=ease_out(min(1, (T - 0.20) / 0.30)))
    # --- devices
    if 1.50 <= T < 6.90:
        dev_photo_card(layer, min(1, (T - 1.50) / 0.40))
    if 3.60 <= T < 6.90:
        dev_receipt(layer, min(1, (T - 3.60) / 2.9))
    # --- captions (none while the receipt card owns the frame)
    if T < 1.10:   cue(layer, T, 0.15, "wordpop", ["MY", "DAUGHTER"], 1, emo="1f467")
    elif T < 2.30: cue(layer, T, 1.12, "pop", ["ALREADY", "BENEFITED"], 1)
    elif T < 3.60: cue(layer, T, 2.32, "slide", ["FROM", "PARC", "CLEMATIS"], 2)
    elif T < 6.90: pass
    elif T < 8.60: cue(layer, T, 7.08, "pop", ["NOW", "IF", "THOMSON", "RESERVE"], 3, size=80)
    elif T < 9.70: cue(layer, T, 8.62, "wordpop", ["IS", "HER", "NEXT", "PROPERTY"], 3, emo="1f3e0", size=80)
    elif T < 11.30: cue(layer, T, 9.75, "slide", ["I'M", "ASKING", "ONE", "THING"], 3, size=80)
    elif T < 13.60:
        cue(layer, T, 11.40, "typebox", ["CAN", "IT", "MOVE", "HER"], None, size=76, y_frac=0.665)
        cue(layer, T, 12.25, "wordpop", ["FORWARD", "AGAIN?"], 0, size=76, y_frac=0.73)
        if T >= 12.70:
            f = ANTON(76); tw = text_w(f, "FORWARD") + int(76 * 0.44)
            x0 = (W - (tw + text_w(f, "AGAIN?") + int(76 * 0.28))) // 2
            scribble_underline(layer, x0 - 6, x0 + tw + 6, int(H * 0.73) + 60, min(1, (T - 12.70) / 0.35), color=GOLD)
    # 13.60-13.90: face alone, no caption - the breath before the whip
    return compose(base, layer)

def F20():  # the question beat with the hand-drawn underline, at T=13.2
    return A11(13.2 / 14.3, 0)

def F21():  # hand-drawn marks bank over the price-gap card: circle + underline
    base = plate_z(1.0)
    layer = new_layer(); stand_in_tag(layer)
    dev_pricegap(layer, 1.0, y_top=0.50)
    # circle the TR number, underline the proven one
    x0, x1 = 70, W - 70; y0 = int(H * 0.50); lx = x0 + 44; rx = x1 - 44; pw = int((rx - lx) * 0.44); ly1 = y0 + 470
    hand_circle(layer, (rx - pw // 2 - 150, ly1 - 260 - 86, rx - pw // 2 + 150, ly1 - 260 - 6), 1.0, color=RED)
    scribble_underline(layer, lx + pw // 2 - 150, lx + pw // 2 + 150, ly1 - 170 - 2, 1.0, color=GOLD, width=8)
    return compose(base, layer)

FRAMES["F20_V1_question_beat_underline"] = F20
FRAMES["F21_hand_drawn_marks"] = F21
A11.secs = 14.3
CLIPS["A11_V1_hook_human_cut_14s"] = A11


def F22():  # B1 "preview starts 17 October" - torn split with the showflat-model photo on top
    top = photo_full(2, zoom=1.04, anchor_y=0.35)
    bot = plate_z(1.0)
    seam_y = int(H * 0.52); m = tear_mask(seam_y)
    out = Image.composite(top, bot.transform((W, H), Image.AFFINE, (1, 0, 0, 0, 1, -int(H * 0.16)), Image.BICUBIC), m)
    layer = new_layer(); torn_edge(layer, seam_y); stand_in_tag(layer)
    eyebrow(layer, "THOMSON RESERVE · PREVIEW", y_frac=0.13, size=34, bg=GOLD, fg=INK)
    caption(layer, ["PREVIEW", "·", "17", "OCTOBER"], 3, emo="1f4c5", y_frac=0.74, size=80)
    return compose(out, layer)

def F23():  # V3 / Hook 4 "only three units left" - the distribution chart photo, hand circle on the sold block
    base = photo_full(3, darken=0.18, zoom=1.0, anchor_y=0.40)
    layer = new_layer()
    eyebrow(layer, "“ONLY THREE UNITS LEFT”", y_frac=0.13, size=38, bg=RED, fg=WHITE)
    # the chart sits mid-frame in this photo; circle its right-hand sold cluster
    hand_circle(layer, (int(W * 0.38), int(H * 0.565), int(W * 0.73), int(H * 0.685)), 1.0, color=RED, width=10)
    caption(layer, ["I", "DON'T", "CARE"], 1, y_frac=0.76, size=84, box_color=RED)
    caption(layer, ["HOW", "FAST", "THEY", "MOVE"], 1, y_frac=0.82, size=64)
    return compose(base, layer)

def F24():  # B31 "a forever million dollar view" - pool photo, slow pull, one caption
    base = photo_full(4, darken=0.10, zoom=1.0, anchor_y=0.30, anchor_x=1.0)
    layer = new_layer()
    scrim(layer, int(H * 0.60), int(H * 0.95), alpha=150)
    caption(layer, ["A", "FOREVER", "VIEW"], 1, emo="1f333", y_frac=0.76)
    return compose(base, layer)

FRAMES["F22_V1_preview_photo_split"] = F22
FRAMES["F23_V3_chart_photo_circle"] = F23
FRAMES["F24_V1_forever_view_photo"] = F24


def dev_photo_flick(layer, t=1.0, idxs=(1, 2, 4), captions=("", "", ""), cx_frac=0.5, cy_frac=0.42, w=520):
    """Three prints flick in one after another (0.33 of t each), each landing at a
    different tilt, stacking like photos dropped on a table. For the "move her
    forward" / "make the next move count" lines - the travel photos go here."""
    tilts = (-9, 7, -3); offs = ((-190, -150), (190, -40), (0, 130))   # spread so all three stay readable
    for k, idx in enumerate(idxs):
        tk = min(1, max(0, (t * 3 - k)))
        if tk <= 0: continue
        ph = PHOTOS[idx % len(PHOTOS)] if PHOTOS else None
        dev_photo_card(layer, ease_out(tk, 4), photo=ph, caption_text=captions[k] if k < len(captions) else "",
                       x_frac=cx_frac + offs[k][0] / W, y_frac=cy_frac + offs[k][1] / H, rot=tilts[k], w=w)

def F25():  # photo flick at rest, over the speaker - the "what the property is for" beat
    base = plate_z(1.0)
    layer = new_layer(); stand_in_tag(layer)
    layer.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 90)))
    dev_photo_flick(layer, 1.0, idxs=(1, 2, 4), captions=("", "", ""), cy_frac=0.40, w=400)
    caption(layer, ["MAKE", "THE", "NEXT", "MOVE"], 3, y_frac=0.76, size=76)
    caption(layer, ["COUNT."], 0, y_frac=0.82, size=76)
    return compose(base, layer)

def A12(t, i):  # the flick in motion, 3s
    base = plate_z(1.0 + 0.03 * t)
    layer = new_layer()
    layer.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, int(90 * min(1, t * 4)))))
    dev_photo_flick(layer, min(1, t * 1.25), idxs=(1, 2, 4), cy_frac=0.40, w=400)
    if t > 0.55: caption_anim(layer, ["MAKE", "THE", "NEXT", "MOVE"], 3, "wordpop", min(1, (t - 0.55) / 0.25), y_frac=0.76, size=76)
    if t > 0.82: caption_anim(layer, ["COUNT."], 0, "flip", min(1, (t - 0.82) / 0.15), y_frac=0.82, size=76)
    return compose(base, layer)

FRAMES["F25_photo_flick"] = F25
CLIPS["A12_photo_flick"] = A12

if __name__ == "__main__":
    args = sys.argv[1:]
    if "--photos" in args:
        i = args.index("--photos"); load_photos(args[i + 1]); del args[i:i + 2]
    if "--plate" in args:
        i = args.index("--plate"); PLATE_FILE = args[i + 1]; del args[i:i + 2]
    which = args or ["frames"]
    if "frames" in which or "all" in which:
        for n, fn in FRAMES.items(): save(fn(), n)
    if "clips" in which or "all" in which:
        for n, fn in CLIPS.items(): render_clip(n, fn)
    for w in which:
        if w in FRAMES: save(FRAMES[w](), w)
        if w in CLIPS: render_clip(w, CLIPS[w])
