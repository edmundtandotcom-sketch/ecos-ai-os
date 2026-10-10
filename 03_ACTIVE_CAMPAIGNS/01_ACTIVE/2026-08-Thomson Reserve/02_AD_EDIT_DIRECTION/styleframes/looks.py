"""One look per ad. Every Longer-Ads variation gets its own caption style, headline treatment, proof device,
body scene, accent colour and end card, so no two ads present the same way. The preview sheets
(preview_looks.py) and the renderer draw from the same functions here.

A "scene" is a full-frame graphic with no talking head (the picture cuts away, then comes back)."""
import math
from PIL import Image, ImageDraw, ImageFilter
import styleframes as SF
from styleframes import W, H, INK, GOLD, RED, ORANGE, WHITE, IVORY, GREEN

# ---------------------------------------------------------------- the dimensions
CAPTIONS = {
    "box":       "key word in a filled box (as approved), the rest white",
    "boxtilt":   "key word in a tilted rounded box",
    "bar":       "full-width dark bar, key word in the accent colour",
    "stroke":    "heavy outlined text, no box, key word in the accent",
    "pill":      "whole line in a dark pill, key word in the accent",
    "stack":     "two lines: small line on top, the key word huge below",
    "glow":      "white text with a coloured glow, key word in the accent",
    "underline": "white text, key word with a thick accent underline",
}
HEADLINES = {
    "pill_top": "pill at the top in the accent colour",
    "pill_inv": "black pill at the top, accent text (as approved)",
    "banner":   "full-width strip at the top in the accent colour",
    "title":    "1.5 s title card over the speaker (serif, dark scrim), then it leaves",
    "chin":     "strip under the chin in the accent colour",
    "corner":   "small tag top-left, like a news channel",
}
HOOK_DEVS = {   # the proof moment inside the hook
    "receipt":    "receipt card under the chin ($1.15M → $1.525M, +$375,000)",
    "ladder":     "SCENE · bought / sold ladder on black, the gain bracketed",
    "slam":       "SCENE · '$375,000' slams in over the family photo",
    "photo_full": "SCENE · family photo full frame, '+$375,000 FORWARD' pill",
    "flick":      "three family photos flick onto the frame, speaker dimmed",
    "card":       "photo card beside the face + receipt under the chin (as approved)",
    "notyet":     "SCENE · 'NOT YET.' slam on black",
    "ballot":     "SCENE · ballot tiles: Plan A GONE, Plan B GONE",
    "two_three":  "SCENE · 2-BED vs 3-BED split with buyer pools",
    "question":   "SCENE · the question as a serif interstitial",
    "chart":      "SCENE · showflat chart photo with a hand-drawn circle",
    "priceline":  "'don't cross this' price rail under the chin",
    "showflat":   "SCENE · showflat model photo, caption only",
    "millions":   "SCENE · '$2–3 MILLION' slams in on black",
}
BODY_DEVS = {
    "check_white": "white checklist under the chin, items tick as he says them",
    "check_dark":  "SCENE · checklist large on black with 'WHAT I'M STUDYING'",
    "same_stack":  "SCENE · SAME MRT / SAME SCHOOL / SAME PROJECT stack over the site plan",
    "two_three":   "SCENE · 2-BED vs 3-BED split",
    "interstitial":"SCENE · one question in serif over the aerial",
    "dotgrid":     "SCENE · 1,268 dots, 84% light up",
    "priceline":   "'my maximum price' rail under the chin",
    "ballot":      "SCENE · ballot tiles GONE / GONE / still available",
    "slam_80k":    "SCENE · '$80,000' slams in, 'STRETCH?' under it",
    "plan_abc":    "SCENE · PLAN A / PLAN B / PLAN C cards flip in",
}
PALETTES = {   # acc = the bold colour; on = text colour on top of acc; bg = scene background; paper = light scene
    "signal":    dict(acc=(255, 230, 0),  on=(11, 11, 15),  bg=(11, 11, 15),  paper=False, name="signal yellow on black"),
    "ember":     dict(acc=(255, 106, 0),  on=(255, 255, 255), bg=(22, 10, 4), paper=False, name="ember orange on near-black"),
    "cherry":    dict(acc=(255, 45, 45),  on=(255, 255, 255), bg=(28, 6, 10), paper=False, name="cherry red on dark plum"),
    "electric":  dict(acc=(0, 112, 255),  on=(255, 255, 255), bg=(6, 12, 36), paper=False, name="electric blue on navy"),
    "lime":      dict(acc=(170, 255, 0),  on=(11, 11, 15),  bg=(10, 22, 8),  paper=False, name="lime on forest black"),
    "magenta":   dict(acc=(255, 0, 150),  on=(255, 255, 255), bg=(32, 4, 26), paper=False, name="hot magenta on aubergine"),
    "cyan":      dict(acc=(0, 220, 255),  on=(11, 11, 15),  bg=(4, 26, 36),  paper=False, name="cyan on deep teal"),
    "violet":    dict(acc=(150, 80, 255), on=(255, 255, 255), bg=(18, 8, 42), paper=False, name="violet on indigo"),
    "mint":      dict(acc=(46, 215, 140), on=(11, 11, 15),  bg=(6, 30, 24),  paper=False, name="mint on bottle green"),
    "paper":     dict(acc=(11, 11, 15),   on=(255, 255, 255), bg=(242, 236, 222), paper=True, name="black on cream paper"),
    "tangerine": dict(acc=(255, 150, 0),  on=(11, 11, 15),  bg=(36, 18, 0),  paper=False, name="tangerine on brown-black"),
    "ice":       dict(acc=(255, 255, 255), on=(11, 11, 15), bg=(22, 26, 32), paper=False, name="white on slate"),
    "coral":     dict(acc=(255, 90, 95),  on=(255, 255, 255), bg=(30, 10, 14), paper=False, name="coral on wine"),
    "sky":       dict(acc=(90, 190, 255), on=(11, 11, 15),  bg=(8, 20, 40),  paper=False, name="sky blue on midnight"),
}
SIZES = {"M": 88, "L": 106, "XL": 124}            # caption size: the key word is what stands out
BORDERS = {
    "line":    "thin line runs around the frame as the ad plays",
    "bar":     "thick bar runs around the frame",
    "dash":    "dashed line runs around the frame",
    "corners": "four corner brackets grow as the ad plays",
    "double":  "two lines, inner one runs ahead of the outer",
    "glow":    "soft glowing line runs around the frame",
}
CUTS = {
    "whip":   "whip-pan blur into the scene and back",
    "flash":  "white flash on every cut",
    "dip":    "dip to black between scenes",
    "punch":  "punch-zoom into the speaker, then hard cut",
    "slide":  "the scene slides up over the speaker",
    "wipe":   "diagonal wipe with a coloured edge",
    "glitch": "two-frame glitch (channel split, sliced) on the cut",
    "spin":   "quarter-spin blur into the scene",
}
ENDS = {
    "gold":  "aerial, serif title, yellow SAVE MY SEAT button (as approved)",
    "dark":  "black, white title, outlined button",
    "photo": "family photo, dark scrim, yellow button",
    "red":   "red card, white title, black button",
}
def pal(look): return PALETTES[look["palette"]]

# ---------------------------------------------------------------- the 31 looks
def L(caption, headline, hook_dev, body_dev, end, palette, size, border, cut, note=""):
    return dict(caption=caption, headline=headline, hook_dev=hook_dev, body_dev=body_dev, end=end, palette=palette, size=size, border=border, cut=cut, note=note)

LOOKS = {  #                caption      headline    proof         body            end      palette      size  border     cut
    "TR_FULL_DH1":  L("box",       "pill_inv", "card",       "full",         "gold",  "signal",    "M",  "line",    "whip",   "the approved one-file look, carried through the long body"),
    "TR_H01_EXIT":  L("stroke",    "title",    "slam",       "check_dark",   "dark",  "electric",  "XL", "bar",     "punch"),
    "TR_H01_BALLOT":L("bar",       "banner",   "photo_full", "ballot",       "photo", "magenta",   "L",  "corners", "slide"),
    "TR_H02_EXIT":  L("glow",      "pill_top", "ladder",     "same_stack",   "red",   "cherry",    "L",  "dash",    "glitch"),
    "TR_H02_BALLOT":L("pill",      "chin",     "receipt",    "slam_80k",     "dark",  "lime",      "M",  "double",  "dip"),
    "TR_H03_EXIT":  L("stack",     "corner",   "notyet",     "interstitial", "dark",  "ice",       "XL", "line",    "spin"),
    "TR_H03_BALLOT":L("underline", "title",    "question",   "plan_abc",     "photo", "tangerine", "L",  "glow",    "wipe"),
    "TR_H04_EXIT":  L("boxtilt",   "pill_inv", "chart",      "two_three",    "red",   "coral",     "XL", "bar",     "flash"),
    "TR_H04_BALLOT":L("bar",       "banner",   "priceline",  "check_white",  "dark",  "cyan",      "M",  "corners", "whip"),
    "TR_H05_EXIT":  L("box",       "chin",     "ballot",     "dotgrid",      "dark",  "violet",    "L",  "dash",    "slide"),
    "TR_H05_BALLOT":L("stroke",    "corner",   "millions",   "ballot",       "gold",  "signal",    "XL", "double",  "punch"),
    "TR_H06_EXIT":  L("pill",      "pill_top", "two_three",  "check_dark",   "photo", "mint",      "M",  "glow",    "glitch"),
    "TR_H06_BALLOT":L("stack",     "banner",   "showflat",   "priceline",    "red",   "ember",     "L",  "line",    "dip"),
    "TR_H07_EXIT":  L("glow",      "title",    "flick",      "interstitial", "dark",  "sky",       "XL", "bar",     "wipe"),
    "TR_H07_BALLOT":L("underline", "corner",   "ladder",     "plan_abc",     "photo", "paper",     "M",  "corners", "spin"),
    "TR_H08_EXIT":  L("boxtilt",   "chin",     "millions",   "same_stack",   "dark",  "magenta",   "L",  "dash",    "flash"),
    "TR_H08_BALLOT":L("bar",       "pill_inv", "question",   "slam_80k",     "red",   "electric",  "XL", "double",  "whip"),
    "TR_H09_EXIT":  L("stroke",    "banner",   "photo_full", "two_three",    "dark",  "coral",     "M",  "glow",    "slide"),
    "TR_H09_BALLOT":L("box",       "pill_top", "slam",       "check_white",  "photo", "cyan",      "L",  "line",    "punch"),
    "TR_H10_EXIT":  L("stack",     "chin",     "showflat",   "dotgrid",      "red",   "lime",      "XL", "bar",     "glitch"),
    "TR_H10_BALLOT":L("pill",      "title",    "flick",      "ballot",       "dark",  "violet",    "M",  "corners", "dip"),
    "TR_H11_EXIT":  L("glow",      "corner",   "two_three",  "interstitial", "photo", "ember",     "L",  "dash",    "wipe"),
    "TR_H11_BALLOT":L("underline", "pill_inv", "question",   "priceline",    "gold",  "ice",       "XL", "double",  "spin"),
    "TR_H12_EXIT":  L("boxtilt",   "banner",   "receipt",    "same_stack",   "dark",  "sky",       "M",  "glow",    "flash"),
    "TR_H12_BALLOT":L("bar",       "chin",     "slam",       "plan_abc",     "red",   "mint",      "L",  "line",    "whip"),
    "TR_H13_EXIT":  L("stroke",    "pill_top", "millions",   "check_dark",   "photo", "tangerine", "XL", "bar",     "slide"),
    "TR_H13_BALLOT":L("box",       "title",    "ballot",     "slam_80k",     "dark",  "cherry",    "M",  "corners", "punch"),
    "TR_H14_EXIT":  L("stack",     "corner",   "priceline",  "dotgrid",      "red",   "paper",     "L",  "dash",    "glitch"),
    "TR_H14_BALLOT":L("pill",      "banner",   "card",       "ballot",       "photo", "electric",  "XL", "double",  "dip"),
    "TR_H15_EXIT":  L("glow",      "chin",     "ladder",     "two_three",    "dark",  "magenta",   "M",  "glow",    "wipe"),
    "TR_H15_BALLOT":L("underline", "pill_inv", "photo_full", "check_white",  "gold",  "lime",      "L",  "line",    "spin"),
}

def recipe(look):
    return (f"colours: {pal(look)['name']}  |  captions: {CAPTIONS[look['caption']]}, size {look['size']}  |  headline: {HEADLINES[look['headline']]}  |  "
            f"proof: {HOOK_DEVS.get(look['hook_dev'], look['hook_dev'])}  |  body: {BODY_DEVS.get(look['body_dev'], 'the full Body 1 plan')}  |  "
            f"cuts: {CUTS[look['cut']]}  |  border: {BORDERS[look['border']]}  |  end card: {ENDS[look['end']]}")

# ---------------------------------------------------------------- captions
def _fit(ws, size, font_of, gap_ratio, extra=0, limit=W - 100):
    """Shrink the caption size until the line fits the frame with a margin."""
    while size > 40:
        f = font_of(size); gap = int(size * gap_ratio)
        if sum(SF.text_w(f, w) for w in ws) + gap * (len(ws) - 1) + int(extra * size) <= limit: return size
        size = int(size * 0.94)
    return size

def draw_caption(layer, words, ai, look, t=1.0, y=0.70, size=None):
    """The cue in this look's caption style, colour from its palette, size from its size dial.
    Lines always fit the frame; on the cream-paper palette the text is ink with a white edge."""
    st = look["caption"]; P = pal(look); acc, on = P["acc"], P["on"]; paper = P["paper"]
    size = size or SIZES[look["size"]]
    ws = [w.upper() for w in words]
    txt = INK if paper else WHITE; edge = WHITE if paper else INK; key = acc if acc != INK else (255, 45, 45)
    if st in ("box", "boxtilt"):
        size = _fit(ws, size, SF.ANTON, 0.28, extra=0.44)
        if st == "box": _caption_box(layer, ws, ai, y, size, box=acc, fg=on, t=t, txt=txt, edge=edge)
        else:
            tmp = SF.new_layer(); _caption_box(tmp, ws, ai, y, size, box=acc, fg=on, t=t, radius=0.5, txt=txt, edge=edge)
            layer.alpha_composite(tmp.rotate(-3, resample=Image.BICUBIC, center=(W // 2, int(H * y))))
    elif st == "bar":
        size = _fit(ws, size, lambda z: SF.OSWALD(int(z * 0.78), 700), 0.3)
        f = SF.OSWALD(int(size * 0.78), 700); cy = int(H * y); bh = int(size * 1.25)
        ImageDraw.Draw(layer).rectangle((0, cy - bh // 2, W, cy + bh // 2), fill=(INK if not paper else (250, 246, 236)) + (235,))
        _line(layer, ws, ai, f, cy, fill=WHITE if not paper else INK, acc=key, gap=int(size * 0.3), t=t)
    elif st == "stroke":
        size = _fit(ws, size, lambda z: SF.ARCHIVO(int(z * 0.9)), 0.3, extra=0.2)
        f = SF.ARCHIVO(int(size * 0.9)); cy = int(H * y)
        _line(layer, ws, ai, f, cy, fill=WHITE, acc=acc if acc != INK else WHITE, gap=int(size * 0.3), stroke=int(size * 0.1), t=t, stroke_col=INK if acc != INK else acc)
    elif st == "pill":
        size = _fit(ws, size, SF.ANTON, 0.28, extra=0.8)
        f = SF.ANTON(size); cy = int(H * y); gap = int(size * 0.28)
        tw = sum(SF.text_w(f, w) for w in ws) + gap * (len(ws) - 1); pad = int(size * 0.4)
        sc = 0.85 + 0.15 * SF.ease_out(t)
        SF.rrect(layer, (W // 2 - (tw // 2 + pad) * sc, cy - int(size * 0.72 * sc), W // 2 + (tw // 2 + pad) * sc, cy + int(size * 0.72 * sc)), int(size * 0.72), INK + (230,), shadow=10)
        _line(layer, ws, ai, f, cy, fill=WHITE, acc=acc if acc != INK else (255, 230, 0), gap=gap, t=t)
    elif st == "stack":
        if look["headline"] == "chin" and y < 0.72: y = 0.745          # the strip under the chin owns 0.615; the stack sits below it
        small, big = (ws[:-1], ws[-1]) if len(ws) > 1 else ([], ws[0])
        bs = _fit([big], int(size * 1.35), SF.ARCHIVO, 0, limit=W - 80)
        f1 = SF.OSWALD(int(size * 0.6), 600); f2 = SF.ARCHIVO(int(bs * (0.8 + 0.2 * SF.ease_out(t))))
        cy = int(H * y)
        if small: _text(layer, (W // 2, cy - int(size * 0.95)), " ".join(small), f1, txt, edge, paper, blur=8)
        _text(layer, (W // 2, cy + int(size * 0.15)), big, f2, key if not paper else INK, edge, paper, blur=12, off=(0, 8))
    elif st == "glow":
        size = _fit(ws, size, SF.ANTON, 0.28, extra=0.3)
        f = SF.ANTON(size); cy = int(H * y); gap = int(size * 0.28)
        g = SF.new_layer(); _line(g, ws, ai, f, cy, fill=key, acc=key, gap=gap, stroke=int(size * 0.12), t=t, stroke_col=key)
        layer.alpha_composite(g.filter(ImageFilter.GaussianBlur(int(size * 0.2))))
        _line(layer, ws, ai, f, cy, fill=WHITE, acc=WHITE, gap=gap, t=t, key_stroke=(int(size * 0.07), key))
    elif st == "underline":
        size = _fit(ws, size, SF.ANTON, 0.28)
        f = SF.ANTON(size); cy = int(H * y); gap = int(size * 0.28)
        widths = [SF.text_w(f, w) for w in ws]; total = sum(widths) + gap * (len(ws) - 1); x = (W - total) // 2
        _line(layer, ws, ai, f, cy, fill=txt, acc=txt, gap=gap, t=t, stroke=int(size * 0.05) if paper else 0, stroke_col=edge)
        if ai is not None:
            x0 = x + sum(widths[:ai]) + gap * ai; x1 = x0 + widths[ai] * SF.ease_out(t)
            ImageDraw.Draw(layer).rounded_rectangle((x0 - 6, cy + int(size * 0.42), x1 + 6, cy + int(size * 0.42) + int(size * 0.16)), int(size * 0.08), fill=key + (255,))

def _text(layer, xy, s_, f, fill, edge, paper, blur=8, off=(0, 6)):
    if paper: ImageDraw.Draw(layer).text(xy, s_, font=f, fill=fill + (255,), anchor="mm", stroke_width=max(2, f.size // 18), stroke_fill=edge + (255,))
    else: SF.shadow_text(layer, xy, s_, f, fill + (255,), anchor="mm", blur=blur, off=off)

def _caption_box(layer, ws, ai, y, size, box, fg, t=1.0, radius=0.18, txt=WHITE, edge=INK):
    """Anton line with the key word in a coloured box; text on the box in the palette's 'on' colour."""
    f = SF.ANTON(size); gap = int(size * 0.28); pad_x = int(size * 0.22); pad_y = int(size * 0.10)
    widths = [SF.text_w(f, w) for w in ws]
    total = sum(widths) + gap * (len(ws) - 1) + (2 * pad_x if ai is not None else 0)
    x = (W - total) // 2; asc, desc = f.getmetrics(); lh = asc + desc; top = int(H * y) - lh // 2
    sc = SF.overshoot(t); d = ImageDraw.Draw(layer)
    for i, (w, wd) in enumerate(zip(ws, widths)):
        if i == ai:
            bx0, by0, bx1, by1 = x, top - pad_y + int(size * 0.08), x + wd + 2 * pad_x, top + lh + pad_y - int(size * 0.06)
            cxm, cym = (bx0 + bx1) / 2, (by0 + by1) / 2; hw, hh = (bx1 - bx0) / 2 * sc, (by1 - by0) / 2 * sc
            SF.rrect(layer, (cxm - hw, cym - hh, cxm + hw, cym + hh), int(size * radius), box + (255,), shadow=8)
            if sc > 0.6: d.text((x + pad_x, top), w, font=f, fill=fg + (255,))
            x += wd + 2 * pad_x + gap
        else:
            if txt == INK: d.text((x, top), w, font=f, fill=INK + (255,), stroke_width=max(2, size // 18), stroke_fill=edge + (255,))
            else: SF.shadow_text(layer, (x, top), w, f, WHITE + (255,), blur=10, off=(0, 6), alpha=190)
            x += wd + gap

def _line(layer, ws, ai, f, cy, fill, acc, gap, stroke=0, t=1.0, stroke_col=(0, 0, 0), key_stroke=None):
    widths = [SF.text_w(f, w) for w in ws]; total = sum(widths) + gap * (len(ws) - 1); x = (W - total) // 2
    d = ImageDraw.Draw(layer); a = int(255 * min(1, t * 2.5))
    for i, (w, wd) in enumerate(zip(ws, widths)):
        col = (acc if i == ai else fill) + (a,)
        sw, sc = (stroke, stroke_col)
        if i == ai and key_stroke: sw, sc = key_stroke
        if sw: d.text((x, cy), w, font=f, fill=col, anchor="lm", stroke_width=sw, stroke_fill=sc + (a,))
        else: d.text((x, cy), w, font=f, fill=col, anchor="lm")
        x += wd + gap

# ---------------------------------------------------------------- headline
def draw_headline(layer, text, look, t=1.0, t_abs=0.0):
    st = look["headline"]; P = pal(look); acc, on = P["acc"], P["on"]; sl = SF.ease_out(min(1, t / 0.3)) if t < 1 else 1.0
    if st == "pill_top": SF.eyebrow(layer, text, bg=acc, fg=on, slide=sl)
    elif st == "pill_inv": SF.eyebrow(layer, text, bg=INK, fg=acc if acc != INK else WHITE, slide=sl)
    elif st == "banner":
        f = SF.OSWALD(40, 700); d = ImageDraw.Draw(layer); y0 = int(H * 0.105)
        d.rectangle((int((1 - sl) * -W), y0, int((1 - sl) * -W) + W, y0 + 86), fill=acc + (245,))
        d.text((W // 2 + int((1 - sl) * -W), y0 + 43), text, font=f, fill=on + (255,), anchor="mm")
    elif st == "chin": SF.eyebrow(layer, text, y_frac=0.615, size=40, bg=acc, fg=on, slide=sl)
    elif st == "corner":
        f = SF.OSWALD(30, 700); tw = SF.text_w(f, text)
        SF.rrect(layer, (40, int(H * 0.115), 40 + tw + 36, int(H * 0.115) + 56), 8, INK + (230,))
        ImageDraw.Draw(layer).rectangle((40, int(H * 0.115), 48, int(H * 0.115) + 56), fill=(acc if acc != INK else WHITE) + (255,))
        ImageDraw.Draw(layer).text((40 + 26, int(H * 0.115) + 28), text, font=f, fill=WHITE + (255,), anchor="lm")
    elif st == "title":
        # only in the first 1.5 s: a scrim and the headline as a two-line serif title, mid-frame, then gone
        if t_abs > 1.5: return
        k = 1.0 if t_abs < 1.2 else max(0, 1 - (t_abs - 1.2) / 0.3)
        layer.alpha_composite(Image.new("RGBA", (W, H), INK + (int(150 * k),)))
        f = SF.SERIF(80); lines = []; cur = ""
        for w in text.split():                                                # wrap to the frame, up to three lines
            if cur and SF.text_w(f, cur + " " + w) > W - 120: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        lines.append(cur); lines = lines[:3]
        y = int(H * 0.67) - (len(lines) - 1) * 48                             # under the chin, not on the face
        for i, ln in enumerate(lines):
            SF.shadow_text(layer, (W // 2, y + i * 96), ln, f, ((acc if acc != INK else WHITE) if i == len(lines) - 1 else IVORY) + (int(255 * k),), anchor="mm", blur=14, off=(0, 8))

# ---------------------------------------------------------------- hook proof devices / scenes
def _photo(idx, **kw):
    return SF.photo_full(idx, **kw)

def gain_ladder(layer, t=1.0):
    """SCENE device: BOUGHT $1.15M → SOLD $1.525M as two bars on a black card, +$375,000 bracket."""
    x0, x1 = 90, W - 90; y0 = int(H * 0.30)
    SF.rrect(layer, (x0, y0, x1, y0 + 760), 28, INK + (245,), outline=GOLD + (90,), width=2, shadow=18)
    d = ImageDraw.Draw(layer)
    d.text((W // 2, y0 + 50), "PARC CLEMATIS · HER LAST PROPERTY", font=SF.OSWALD(34, 600), fill=IVORY + (220,), anchor="mm")
    lx = x0 + 44; rx = x1 - 44; base = y0 + 620; pw = int((rx - lx) * 0.42)
    h1 = int(300 * SF.ease_out(min(1, t * 1.6)))
    SF.rrect(layer, (lx, base - h1, lx + pw, base), 12, (120, 130, 150, 255))
    d.text((lx + pw // 2, base + 18), "BOUGHT", font=SF.INTER(28, 600), fill=IVORY + (190,), anchor="ma")
    if t > 0.3: SF.card_number(layer, (lx + pw // 2, base - h1 - 16), "$1.15M", SF.ANTON(78), fill=IVORY, anchor="mb")
    t2 = max(0, (t - 0.4) / 0.6); h2 = int(420 * SF.ease_out(t2))
    SF.rrect(layer, (rx - pw, base - h2, rx, base), 12, GOLD + (255,))
    d.text((rx - pw // 2, base + 18), "SOLD", font=SF.INTER(28, 600), fill=IVORY + (190,), anchor="ma")
    if t2 > 0.6: SF.card_number(layer, (rx - pw // 2, base - h2 - 16), "$1.525M", SF.ANTON(78), fill=GOLD, anchor="mb")
    if t2 > 0.9:
        gx = (lx + pw + rx - pw) // 2
        d.line((gx, base - 300, gx, base - 420), fill=GREEN + (255,), width=6)
        s = "+$375,000 FORWARD"; f = SF.ARCHIVO(40); tw = SF.text_w(f, s)
        SF.rrect(layer, (W // 2 - tw // 2 - 24, y0 + 680, W // 2 + tw // 2 + 24, y0 + 740), 12, GREEN + (255,))
        d.text((W // 2, y0 + 710), s, font=f, fill=WHITE + (255,), anchor="mm")

def plan_abc(layer, t=1.0, acc=GOLD):
    """SCENE device: PLAN A / B / C cards flip in, the third one marked 'walk away'."""
    labels = [("PLAN A", "the unit we want"), ("PLAN B", "the stack we'd accept"), ("PLAN C", "the price we walk away at")]
    x0 = 90; y = int(H * 0.30); d = ImageDraw.Draw(layer)
    for i, (a, b) in enumerate(labels):
        ti = SF.ease_out(min(1, max(0, t * 3.5 - i)))
        if ti <= 0: continue
        sl = int((1 - ti) * 400)
        col = (acc if i < 2 else RED)
        SF.rrect(layer, (x0 + sl, y, W - 90 + sl, y + 200), 22, INK + (240,), outline=col + (160,), width=3, shadow=14)
        d.text((x0 + sl + 40, y + 70), a, font=SF.ARCHIVO(64), fill=col + (255,), anchor="lm")
        d.text((x0 + sl + 40, y + 140), b.upper(), font=SF.OSWALD(34, 500), fill=IVORY + (200,), anchor="lm")
        y += 230

def small(layer, draw, scale=0.78, y_frac=0.70):
    """A card drawn at native size with its top at y=0, shrunk and placed under the chin (the selfie framing
    fills the frame with the face down to ~0.58; the approved receipt sits here too)."""
    tmp = SF.new_layer(); draw(tmp)
    tw, th = int(W * scale), int(H * scale)
    layer.alpha_composite(tmp.resize((tw, th), Image.LANCZOS), ((W - tw) // 2, int(H * y_frac)))

def scene_bg(look):
    """A flat scene background in the palette: dark colour (or cream paper) with a soft vignette."""
    P = pal(look); base = Image.new("RGB", (W, H), P["bg"])
    v = Image.new("L", (W, H), 0); ImageDraw.Draw(v).ellipse((-300, -200, W + 300, H + 400), fill=255); v = v.filter(ImageFilter.GaussianBlur(260))
    edge = tuple(max(0, c - 24) if not P["paper"] else min(255, c - 30) for c in P["bg"])
    return Image.composite(base, Image.new("RGB", (W, H), edge), v)

def hook_scene(plate, look, hook_id, t=1.0):
    """Returns the full frame for the proof moment of the hook. Scenes replace the plate."""
    dev = look["hook_dev"]; layer = SF.new_layer(); P = pal(look); acc = P["acc"] if P["acc"] != INK else (255, 45, 45)
    if dev == "receipt":
        SF.dev_receipt(layer, t, y=0.82); return SF.compose(plate, layer), "talking head"
    if dev == "card":
        SF.dev_photo_card(layer, t, x_frac=0.84, y_frac=0.28, w=260, rot=-6); SF.dev_receipt(layer, t, y=0.82); return SF.compose(plate, layer), "talking head"
    if dev == "flick":
        layer.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 110)))
        SF.dev_photo_flick(layer, t, idxs=(0, 1, 4), cy_frac=0.42, w=400); return SF.compose(plate, layer), "talking head dimmed"
    if dev == "priceline":
        small(layer, lambda L: SF.dev_priceline(L, t, y_top=0.0)); return SF.compose(plate, layer), "talking head"
    # ---- scenes (no talking head)
    if dev == "ladder":
        base = scene_bg(look); gain_ladder(layer, t)
    elif dev == "slam":
        base = _photo(0, darken=0.55, zoom=1.06, anchor_y=0.3)
        SF.dev_slam(layer, "$375,000", t, y=0.50, size=200, color=acc, rot=-4)
        SF.shadow_text(layer, (W // 2, int(H * 0.62)), "FORWARD", SF.ARCHIVO(70), WHITE + (255,), anchor="mm", blur=12)
    elif dev == "photo_full":
        base = _photo(0, darken=0.15, zoom=1.0, anchor_y=0.3); SF.scrim(layer, int(H * 0.55), int(H * 0.95), alpha=170)
        s = "+$375,000 FORWARD"; f = SF.ARCHIVO(46); tw = SF.text_w(f, s)
        SF.rrect(layer, (W // 2 - tw // 2 - 30, int(H * 0.68), W // 2 + tw // 2 + 30, int(H * 0.68) + 84), 14, acc + (255,), shadow=12)
        ImageDraw.Draw(layer).text((W // 2, int(H * 0.68) + 42), s, font=f, fill=P["on"] + (255,), anchor="mm")
    elif dev == "notyet":
        base = scene_bg(look); SF.dev_slam(layer, "NOT YET.", t, y=0.48, size=210, color=WHITE if not P["paper"] else INK)
        SF.eyebrow(layer, "“DAD, WOULD YOU BUY THOMSON RESERVE?”", y_frac=0.30, size=34, bg=acc, fg=P["on"])
    elif dev == "millions":
        base = SF.broll("deck_p06", cx=2250, darken=0.7, zoom=1.04); SF.dev_slam(layer, "$2–3 MILLION", t, y=0.46, size=150, color=acc, rot=-3)
        SF.shadow_text(layer, (W // 2, int(H * 0.58)), "OF HER MONEY", SF.ARCHIVO(60), WHITE + (255,), anchor="mm", blur=12)
    elif dev == "ballot":
        base = SF.broll("deck_p10", darken=0.72); SF.dev_ballot(layer, t, y_top=0.30)
    elif dev == "two_three":
        return SF.dev_two_three(SF.broll("deck_p12", cx=900, darken=0.5), SF.broll("deck_p18", cx=1800, darken=0.4), t), "SCENE"
    elif dev == "question":
        q = {3: ["Dad,", "would you", "buy it?"], 8: ["The", "$3 million", "question."], 9: ["Would you tell", "your own daughter", "to buy it?"], 11: ["2-bed", "or", "3-bed?"], 13: ["If it was", "your daughter's", "money?"]}.get(hook_id, ["Would I buy it", "for my", "daughter?"])
        return SF.dev_interstitial(q, len(q) - 1, bg="deck_p06", t=t), "SCENE"
    elif dev == "chart":
        base = _photo(3, darken=0.18, anchor_y=0.40); SF.hand_circle(layer, (int(W * 0.38), int(H * 0.565), int(W * 0.73), int(H * 0.685)), t, color=RED, width=10)
        SF.eyebrow(layer, "“ONLY THREE UNITS LEFT”", y_frac=0.13, size=38, bg=RED, fg=WHITE)
    elif dev == "showflat":
        base = _photo(2, darken=0.10, zoom=1.04, anchor_y=0.35); SF.scrim(layer, int(H * 0.55), int(H * 0.95), alpha=150)
    else:
        base = plate
    return SF.compose(base, layer), "SCENE"

# ---------------------------------------------------------------- body scenes / devices
EXIT_ITEMS = [("2-BED OR 3-BED?", "1f3e2"), ("WHICH STACKS EXIT STRONGER?", "1f4cd"), ("WHAT PRICE LEAVES UPSIDE?", "1f4b0"), ("UNITS I WOULDN'T TOUCH", "1f6ab")]
BALLOT_ITEMS = [("MY MAXIMUM PRICE", "1f6ab"), ("MY PREFERRED STACKS", "1f4cd"), ("PLAN A, B AND C", "1f5f3"), ("UNITS I'D WALK AWAY FROM", "1f3e2")]

def body_scene(plate, look, body_id, t=1.0):
    dev = look["body_dev"]; layer = SF.new_layer(); items = EXIT_ITEMS if body_id == "EXIT" else BALLOT_ITEMS
    P = pal(look); acc = P["acc"] if P["acc"] != INK else (255, 45, 45)
    if dev == "check_white":
        small(layer, lambda L: SF.dev_checklist(L, t, y_top=0.0, items=items)); return SF.compose(plate, layer), "talking head"
    if dev == "priceline":
        small(layer, lambda L: SF.dev_priceline(L, t, y_top=0.0)); return SF.compose(plate, layer), "talking head"
    if dev == "check_dark":
        base = scene_bg(look)
        SF.eyebrow(layer, "WHAT I'M STUDYING FOR HER" if body_id == "EXIT" else "WHAT I DECIDE BEFORE BALLOT DAY", y_frac=0.26, size=38, bg=acc, fg=P["on"])
        SF.dev_checklist(layer, t, y_top=0.33, items=items)
    elif dev == "same_stack":
        base = SF.broll("deck_p11", cx=1400, darken=0.70, zoom=1.05)
        SF.eyebrow(layer, "WHEN SHE EVENTUALLY SELLS…", y_frac=0.13, size=38, bg=INK, fg=GOLD); SF.dev_same_stack(layer, t, y_top=0.22)
    elif dev == "two_three":
        return SF.dev_two_three(SF.broll("deck_p12", cx=900, darken=0.5), SF.broll("deck_p18", cx=1800, darken=0.4), t), "SCENE"
    elif dev == "interstitial":
        q = ["Who buys it", "from her", "next?"] if body_id == "EXIT" else ["Decide before", "the showroom,", "not inside it."]
        return SF.dev_interstitial(q, 2, bg="deck_p04", t=t), "SCENE"
    elif dev == "dotgrid":
        base = SF.broll("deck_p17", darken=0.78); SF.dev_dotgrid(layer, t)
        SF.card_number(layer, (W // 2, int(H * 0.675)), "1,268", SF.ANTON(200), fill=acc, anchor="mm")
        SF.eyebrow(layer, "UNITS SHE'D COMPETE WITH AT EXIT", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    elif dev == "ballot":
        base = SF.broll("deck_p10", darken=0.70); SF.eyebrow(layer, "BALLOT DAY · YOUR NUMBER IS CALLED", y_frac=0.13, size=38, bg=RED, fg=WHITE); SF.dev_ballot(layer, t, y_top=0.30)
    elif dev == "slam_80k":
        base = SF.broll("deck_p16", darken=0.75, zoom=1.04); SF.dev_slam(layer, "$80,000", t, y=0.46, size=210, color=acc, rot=-4)
        SF.shadow_text(layer, (W // 2, int(H * 0.60)), "“MAYBE WE CAN STRETCH…”", SF.SERIF_I(54), IVORY + (255,), anchor="mm", blur=10)
    elif dev == "plan_abc":
        base = scene_bg(look); plan_abc(layer, t, acc)
    else:
        base = plate
    return SF.compose(base, layer), "SCENE"

# ---------------------------------------------------------------- end cards
def endcard(look, t=1.0):
    st = look["end"]; P = pal(look); acc = P["acc"] if P["acc"] != INK else (255, 230, 0); on = P["on"] if P["acc"] != INK else INK
    if st == "gold" and look["palette"] == "signal": return SF.dev_endcard(t)
    layer = SF.new_layer(); d = ImageDraw.Draw(layer)
    if st in ("gold", "dark"):
        base = scene_bg(look) if st == "dark" else SF.broll("deck_p06", cx=2250, darken=0.45, zoom=1.0 + 0.03 * (1 - t))
        if st == "gold": layer.alpha_composite(Image.new("RGBA", (W, H), INK + (120,))); SF.scrim(layer, int(H * 0.30), int(H * 0.75), alpha=200, color=INK)
        title_col = IVORY if not P["paper"] else INK; btn = acc if st == "gold" else None; btn_fg = on if st == "gold" else (WHITE if not P["paper"] else INK); sub = title_col
    elif st == "photo":
        base = _photo(4, darken=0.55, anchor_y=0.3, anchor_x=1.0); SF.scrim(layer, int(H * 0.25), int(H * 0.75), alpha=200, color=INK); title_col = IVORY; btn = acc; btn_fg = on; sub = IVORY
    elif P["paper"]:  # "red" on the paper palette: the cream card, ink text, black button
        base = scene_bg(look); title_col = INK; btn = INK; btn_fg = WHITE; sub = INK
    else:  # "red": the whole card in the accent colour
        base = Image.new("RGB", (W, H), acc); title_col = on; btn = INK if on != INK else WHITE; btn_fg = WHITE if on != INK else INK; sub = on
    last_col = (acc if st in ("dark", "photo", "gold") else on) if not P["paper"] else ((255, 45, 45) if st != "photo" else acc)
    d.text((W // 2, int(H * 0.40)), "LIVE 60-MINUTE WEBINAR", font=SF.OSWALD(34, 500), fill=last_col + (255,), anchor="mm")
    f = SF.SERIF(96)
    for i, ln in enumerate(("Would I buy", "Thomson Reserve", "for my daughter?")):
        SF.shadow_text(layer, (W // 2, int(H * (0.46 + 0.06 * i))), ln, f, (last_col if i == 2 else title_col) + (255,), anchor="mm")
    sc = SF.overshoot(min(1, max(0, (t - 0.2) / 0.45))); s_ = "SAVE MY SEAT  ›"; fb = SF.ARCHIVO(50); tw = SF.text_w(fb, s_)
    bw, bh = (tw + 120) * sc, 120 * sc; cx, cy = W // 2, int(H * 0.68)
    if btn is None: d.rounded_rectangle((cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2), int(60 * sc), outline=(WHITE if not P["paper"] else INK) + (255,), width=5)
    else: SF.rrect(layer, (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2), int(60 * sc), btn + (255,), shadow=16)
    if sc > 0.6: d.text((cx, cy), s_, font=fb, fill=btn_fg + (255,), anchor="mm")
    d.text((W // 2, int(H * 0.745)), "Link below · before the 17 Oct preview", font=SF.INTER(28, 500), fill=sub + (190,), anchor="mm")
    return SF.compose(base, layer)

# ---------------------------------------------------------------- progress border (runs around the frame for the whole ad)
def draw_border(layer, look, progress):
    """progress 0..1 = how much of the ad has played. The line starts top-centre and runs clockwise."""
    st = look["border"]; P = pal(look); acc = P["acc"] if P["acc"] != INK else (255, 45, 45)
    thick = {"line": 10, "bar": 26, "dash": 12, "corners": 16, "double": 8, "glow": 10}[st]
    d = ImageDraw.Draw(layer); m = thick // 2
    perim = 2 * (W + H)
    def pt(u):                                   # u along the perimeter from top-centre, clockwise
        u = u % perim
        if u < W / 2: return (W / 2 + u, m)
        u -= W / 2
        if u < H: return (W - m, u)
        u -= H
        if u < W: return (W - m - u, H - m)
        u -= W
        if u < H: return (m, H - m - u)
        u -= H
        return (m + u, m)
    def run(length, width, col, off=0, dash=None):
        pts = []; u = off; step = 24
        while u <= off + length:
            pts.append(pt(u)); u += step
        pts.append(pt(off + length))
        if dash:
            for i in range(0, len(pts) - 1):
                if (i // dash) % 2 == 0: d.line([pts[i], pts[i + 1]], fill=col, width=width)
        else:
            d.line(pts, fill=col, width=width, joint="curve")
    if st == "corners":
        L = int(min(W, H) * 0.12 + progress * min(W, H) * 0.35)
        for (x, y, sx, sy) in ((m, m, 1, 1), (W - m, m, -1, 1), (W - m, H - m, -1, -1), (m, H - m, 1, -1)):
            d.line([(x, y + sy * L), (x, y), (x + sx * L, y)], fill=acc + (255,), width=thick)
        return
    track = (255, 255, 255, 60) if not P["paper"] else (0, 0, 0, 50)
    run(perim, thick, track)
    if st == "glow":
        g = SF.new_layer(); gd = ImageDraw.Draw(g)
        pts = [pt(u) for u in range(0, int(perim * progress) + 1, 24)] + [pt(perim * progress)]
        gd.line(pts, fill=acc + (255,), width=thick * 3)
        layer.alpha_composite(g.filter(ImageFilter.GaussianBlur(14)))
        run(perim * progress, thick, acc + (255,))
    elif st == "dash": run(perim * progress, thick, acc + (255,), dash=2)
    elif st == "double":
        run(perim * progress, thick, acc + (255,))
        d2 = ImageDraw.Draw(layer); inner = thick * 3
        pts = [(min(max(x, inner), W - inner), min(max(y, inner), H - inner)) for x, y in [pt(u) for u in range(0, int(perim * min(1, progress * 1.3)) + 1, 24)]]
        if len(pts) > 1: d2.line(pts, fill=acc + (160,), width=thick)
    else: run(perim * progress, thick, acc + (255,))

# ---------------------------------------------------------------- cuts (a single mid-transition frame, for the sheets; the renderer animates the same idea)
def cut_frame(a, b, look, k=0.5):
    """The frame half-way through the cut from picture a to picture b in this look's cut style."""
    st = look["cut"]; P = pal(look); acc = P["acc"]
    if st == "whip":
        return SF.whip_blur(Image.blend(a, b, k), 150)
    if st == "flash":
        return SF.flash(Image.blend(a, b, k), 0.75)
    if st == "dip":
        return Image.blend(Image.new("RGB", (W, H), (0, 0, 0)), b, 0.25)
    if st == "punch":
        z = SF.zoom_img(a, 1.35, anchor=(0.5, 0.4)); return SF.whip_blur(z, 40)
    if st == "slide":
        out = a.copy(); dy = int(H * (1 - k)); out.paste(b, (0, dy)); ImageDraw.Draw(out).rectangle((0, dy - 10, W, dy), fill=acc); return out
    if st == "wipe":
        m = Image.new("L", (W, H), 0); x = int(W * k * 1.4); ImageDraw.Draw(m).polygon([(0, 0), (x, 0), (x - int(W * 0.4), H), (0, H)], fill=255)
        out = Image.composite(b, a, m); ImageDraw.Draw(out).line([(x, 0), (x - int(W * 0.4), H)], fill=acc, width=22); return out
    if st == "glitch":
        import numpy as np
        arr = np.asarray(a).copy(); r = np.roll(arr[:, :, 0], 28, axis=1); bch = np.roll(arr[:, :, 2], -28, axis=1); arr[:, :, 0] = r; arr[:, :, 2] = bch
        rows = np.random.RandomState(3).randint(0, H - 40, 9)
        for y in rows: arr[y:y + 40] = np.roll(arr[y:y + 40], np.random.RandomState(y).randint(-120, 120), axis=1)
        out = Image.fromarray(arr); return Image.blend(out, b, 0.3)
    if st == "spin":
        out = a.rotate(18 * (1 - k), resample=Image.BICUBIC, expand=False); out = SF.zoom_img(out, 1.25, anchor=(0.5, 0.5)); return SF.whip_blur(Image.blend(out, b, k * 0.6), 60)
    return b
