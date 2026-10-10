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
    "house":   "white Anton, one word in an orange box",
    "yellow":  "white Anton, one word in a yellow box (black text)",
    "redbox":  "white Anton, one word in a red box",
    "bar":     "black lower-third bar, white Oswald, key word yellow",
    "stroke":  "Archivo with a black outline, no box, key word yellow",
    "pill":    "whole line in a dark pill, key word yellow",
    "stack":   "two lines: small line on top, the key word huge below",
}
HEADLINES = {
    "pill_top": "black pill, yellow text, top of frame (as approved)",
    "gold_top": "yellow pill, black text, top of frame",
    "red_top":  "red pill, white text, top of frame",
    "title":    "1.5 s title card over the speaker (serif, dark scrim), then it leaves",
    "chin":     "yellow strip under the chin",
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
ENDS = {
    "gold":  "aerial, serif title, yellow SAVE MY SEAT button (as approved)",
    "dark":  "black, white title, outlined button",
    "photo": "family photo, dark scrim, yellow button",
    "red":   "red card, white title, black button",
}
ACCENTS = {"orange": ORANGE, "yellow": GOLD, "red": RED, "white": WHITE}

# ---------------------------------------------------------------- the 31 looks
def L(caption, headline, hook_dev, body_dev, end, accent, note=""):
    return dict(caption=caption, headline=headline, hook_dev=hook_dev, body_dev=body_dev, end=end, accent=accent, note=note)

LOOKS = {
    "TR_FULL_DH1":  L("house",  "pill_top", "card",       "full",         "gold",  "orange", "the approved one-file look, carried through the long body"),
    "TR_H01_EXIT":  L("yellow", "title",    "slam",       "check_dark",   "dark",  "yellow"),
    "TR_H01_BALLOT":L("bar",    "gold_top", "photo_full", "ballot",       "photo", "yellow"),
    "TR_H02_EXIT":  L("stroke", "red_top",  "ladder",     "same_stack",   "red",   "red"),
    "TR_H02_BALLOT":L("pill",   "chin",     "receipt",    "slam_80k",     "gold",  "yellow"),
    "TR_H03_EXIT":  L("stack",  "corner",   "notyet",     "interstitial", "dark",  "white"),
    "TR_H03_BALLOT":L("house",  "title",    "question",   "plan_abc",     "photo", "orange"),
    "TR_H04_EXIT":  L("redbox", "pill_top", "chart",      "two_three",    "gold",  "red"),
    "TR_H04_BALLOT":L("bar",    "red_top",  "priceline",  "check_white",  "red",   "yellow"),
    "TR_H05_EXIT":  L("yellow", "chin",     "ballot",     "dotgrid",      "dark",  "yellow"),
    "TR_H05_BALLOT":L("stroke", "corner",   "millions",   "ballot",       "gold",  "white"),
    "TR_H06_EXIT":  L("pill",   "gold_top", "two_three",  "check_dark",   "photo", "yellow"),
    "TR_H06_BALLOT":L("stack",  "pill_top", "showflat",   "priceline",    "red",   "orange"),
    "TR_H07_EXIT":  L("house",  "red_top",  "flick",      "interstitial", "gold",  "orange"),
    "TR_H07_BALLOT":L("redbox", "title",    "ladder",     "plan_abc",     "dark",  "red"),
    "TR_H08_EXIT":  L("bar",    "corner",   "millions",   "same_stack",   "photo", "yellow"),
    "TR_H08_BALLOT":L("yellow", "chin",     "question",   "slam_80k",     "red",   "yellow"),
    "TR_H09_EXIT":  L("stroke", "pill_top", "photo_full", "two_three",    "dark",  "white"),
    "TR_H09_BALLOT":L("pill",   "red_top",  "slam",       "check_white",  "gold",  "yellow"),
    "TR_H10_EXIT":  L("stack",  "gold_top", "showflat",   "dotgrid",      "photo", "orange"),
    "TR_H10_BALLOT":L("house",  "corner",   "flick",      "ballot",       "dark",  "orange"),
    "TR_H11_EXIT":  L("redbox", "chin",     "two_three",  "interstitial", "red",   "red"),
    "TR_H11_BALLOT":L("bar",    "title",    "question",   "priceline",    "gold",  "yellow"),
    "TR_H12_EXIT":  L("yellow", "pill_top", "receipt",    "same_stack",   "photo", "yellow"),
    "TR_H12_BALLOT":L("stroke", "gold_top", "slam",       "plan_abc",     "dark",  "white"),
    "TR_H13_EXIT":  L("pill",   "corner",   "millions",   "check_dark",   "red",   "yellow"),
    "TR_H13_BALLOT":L("stack",  "red_top",  "ballot",     "slam_80k",     "gold",  "orange"),
    "TR_H14_EXIT":  L("house",  "chin",     "priceline",  "dotgrid",      "photo", "orange"),
    "TR_H14_BALLOT":L("redbox", "title",    "card",       "ballot",       "dark",  "red"),
    "TR_H15_EXIT":  L("bar",    "gold_top", "ladder",     "two_three",    "red",   "yellow"),
    "TR_H15_BALLOT":L("yellow", "corner",   "photo_full", "check_white",  "photo", "yellow"),
}

def recipe(look):
    return (f"captions: {CAPTIONS[look['caption']]}  |  headline: {HEADLINES[look['headline']]}  |  "
            f"proof: {HOOK_DEVS.get(look['hook_dev'], look['hook_dev'])}  |  body: {BODY_DEVS.get(look['body_dev'], 'the full Body 1 plan (inserts, dot grid, bars, price gap, VS split, checklist)')}  |  "
            f"end card: {ENDS[look['end']]}")

# ---------------------------------------------------------------- captions
def draw_caption(layer, words, ai, look, t=1.0, y=0.70, size=88):
    """The cue in this look's caption style. t = arrival progress (0..1)."""
    st = look["caption"]; acc = ACCENTS[look["accent"]]
    ws = [w.upper() for w in words]
    if st == "house":
        SF.caption_anim(layer, ws, ai, "pop", t, y_frac=y, size=size, box_color=ORANGE)
    elif st == "yellow":
        _caption_box(layer, ws, ai, y, size, box=GOLD, fg=INK, t=t)
    elif st == "redbox":
        SF.caption_anim(layer, ws, ai, "pop", t, y_frac=y, size=size, box_color=RED)
    elif st == "bar":
        f = SF.OSWALD(int(size * 0.78), 700); cy = int(H * y); bh = int(size * 1.25)
        d = ImageDraw.Draw(layer)
        d.rectangle((0, cy - bh // 2, W, cy + bh // 2), fill=INK + (235,))
        _line(layer, ws, ai, f, cy, fill=WHITE, acc=GOLD, gap=int(size * 0.3), t=t)
    elif st == "stroke":
        f = SF.ARCHIVO(int(size * 0.9)); cy = int(H * y)
        _line(layer, ws, ai, f, cy, fill=WHITE, acc=GOLD, gap=int(size * 0.3), stroke=int(size * 0.09), t=t)
    elif st == "pill":
        f = SF.ANTON(size); cy = int(H * y); gap = int(size * 0.28)
        tw = sum(SF.text_w(f, w) for w in ws) + gap * (len(ws) - 1); pad = int(size * 0.4)
        sc = 0.85 + 0.15 * SF.ease_out(t)
        SF.rrect(layer, (W // 2 - (tw // 2 + pad) * sc, cy - int(size * 0.72 * sc), W // 2 + (tw // 2 + pad) * sc, cy + int(size * 0.72 * sc)), int(size * 0.72), INK + (230,), shadow=10)
        _line(layer, ws, ai, f, cy, fill=WHITE, acc=GOLD, gap=gap, t=t)
    elif st == "stack":
        small, big = (ws[:-1], ws[-1]) if len(ws) > 1 else ([], ws[0])      # word order kept: the last word is the big one
        f1 = SF.OSWALD(int(size * 0.6), 600); f2 = SF.ARCHIVO(int(size * 1.35 * (0.8 + 0.2 * SF.ease_out(t))))
        cy = int(H * y)
        if small: SF.shadow_text(layer, (W // 2, cy - int(size * 0.95)), " ".join(small), f1, WHITE + (255,), anchor="mm", blur=8)
        SF.shadow_text(layer, (W // 2, cy + int(size * 0.15)), big, f2, acc + (255,), anchor="mm", blur=12, off=(0, 8))

def _caption_box(layer, ws, ai, y, size, box, fg, t=1.0):
    """Anton line with the key word in a coloured box and box-coloured text (yellow box → black text)."""
    f = SF.ANTON(size); gap = int(size * 0.28); pad_x = int(size * 0.22); pad_y = int(size * 0.10)
    widths = [SF.text_w(f, w) for w in ws]
    total = sum(widths) + gap * (len(ws) - 1) + (2 * pad_x if ai is not None else 0)
    x = (W - total) // 2; asc, desc = f.getmetrics(); lh = asc + desc; top = int(H * y) - lh // 2
    sc = SF.overshoot(t)
    for i, (w, wd) in enumerate(zip(ws, widths)):
        if i == ai:
            bx0, by0, bx1, by1 = x, top - pad_y + int(size * 0.08), x + wd + 2 * pad_x, top + lh + pad_y - int(size * 0.06)
            cxm, cym = (bx0 + bx1) / 2, (by0 + by1) / 2; hw, hh = (bx1 - bx0) / 2 * sc, (by1 - by0) / 2 * sc
            SF.rrect(layer, (cxm - hw, cym - hh, cxm + hw, cym + hh), int(size * 0.18), box + (255,), shadow=8)
            if sc > 0.6: ImageDraw.Draw(layer).text((x + pad_x, top), w, font=f, fill=fg + (255,))
            x += wd + 2 * pad_x + gap
        else:
            SF.shadow_text(layer, (x, top), w, f, WHITE + (255,), blur=10, off=(0, 6), alpha=190); x += wd + gap

def _line(layer, ws, ai, f, cy, fill, acc, gap, stroke=0, t=1.0):
    widths = [SF.text_w(f, w) for w in ws]; total = sum(widths) + gap * (len(ws) - 1); x = (W - total) // 2
    d = ImageDraw.Draw(layer); a = int(255 * min(1, t * 2.5))
    for i, (w, wd) in enumerate(zip(ws, widths)):
        col = (acc if i == ai else fill) + (a,)
        if stroke: d.text((x, cy), w, font=f, fill=col, anchor="lm", stroke_width=stroke, stroke_fill=(0, 0, 0, a))
        else: d.text((x, cy), w, font=f, fill=col, anchor="lm")
        x += wd + gap

# ---------------------------------------------------------------- headline
def draw_headline(layer, text, look, t=1.0, t_abs=0.0):
    st = look["headline"]; sl = SF.ease_out(min(1, t / 0.3)) if t < 1 else 1.0
    if st == "pill_top": SF.eyebrow(layer, text, slide=sl)
    elif st == "gold_top": SF.eyebrow(layer, text, bg=GOLD, fg=INK, slide=sl)
    elif st == "red_top": SF.eyebrow(layer, text, bg=RED, fg=WHITE, slide=sl)
    elif st == "chin": SF.eyebrow(layer, text, y_frac=0.615, size=40, bg=GOLD, fg=INK, slide=sl)
    elif st == "corner":
        f = SF.OSWALD(30, 700); tw = SF.text_w(f, text)
        SF.rrect(layer, (40, int(H * 0.115), 40 + tw + 36, int(H * 0.115) + 56), 8, INK + (230,))
        ImageDraw.Draw(layer).rectangle((40, int(H * 0.115), 48, int(H * 0.115) + 56), fill=GOLD + (255,))
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
            SF.shadow_text(layer, (W // 2, y + i * 96), ln, f, (GOLD if i == len(lines) - 1 else IVORY) + (int(255 * k),), anchor="mm", blur=14, off=(0, 8))

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

def plan_abc(layer, t=1.0):
    """SCENE device: PLAN A / B / C cards flip in, the third one marked 'walk away'."""
    labels = [("PLAN A", "the unit we want"), ("PLAN B", "the stack we'd accept"), ("PLAN C", "the price we walk away at")]
    x0 = 90; y = int(H * 0.30); d = ImageDraw.Draw(layer)
    for i, (a, b) in enumerate(labels):
        ti = SF.ease_out(min(1, max(0, t * 3.5 - i)))
        if ti <= 0: continue
        sl = int((1 - ti) * 400)
        col = (GOLD if i < 2 else RED)
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

def hook_scene(plate, look, hook_id, t=1.0):
    """Returns the full frame for the proof moment of the hook. Scenes replace the plate."""
    dev = look["hook_dev"]; layer = SF.new_layer()
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
        base = Image.new("RGB", (W, H), INK); gain_ladder(layer, t)
    elif dev == "slam":
        base = _photo(0, darken=0.55, zoom=1.06, anchor_y=0.3)
        SF.dev_slam(layer, "$375,000", t, y=0.50, size=200, color=GOLD, rot=-4)
        SF.shadow_text(layer, (W // 2, int(H * 0.62)), "FORWARD", SF.ARCHIVO(70), WHITE + (255,), anchor="mm", blur=12)
    elif dev == "photo_full":
        base = _photo(0, darken=0.15, zoom=1.0, anchor_y=0.3); SF.scrim(layer, int(H * 0.55), int(H * 0.95), alpha=170)
        s = "+$375,000 FORWARD"; f = SF.ARCHIVO(46); tw = SF.text_w(f, s)
        SF.rrect(layer, (W // 2 - tw // 2 - 30, int(H * 0.68), W // 2 + tw // 2 + 30, int(H * 0.68) + 84), 14, GOLD + (255,), shadow=12)
        ImageDraw.Draw(layer).text((W // 2, int(H * 0.68) + 42), s, font=f, fill=INK + (255,), anchor="mm")
    elif dev == "notyet":
        base = Image.new("RGB", (W, H), INK); SF.dev_slam(layer, "NOT YET.", t, y=0.48, size=210)
        SF.eyebrow(layer, "“DAD, WOULD YOU BUY THOMSON RESERVE?”", y_frac=0.30, size=34, bg=GOLD, fg=INK)
    elif dev == "millions":
        base = SF.broll("deck_p06", cx=2250, darken=0.7, zoom=1.04); SF.dev_slam(layer, "$2–3 MILLION", t, y=0.46, size=150, color=GOLD, rot=-3)
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
    if dev == "check_white":
        small(layer, lambda L: SF.dev_checklist(L, t, y_top=0.0, items=items)); return SF.compose(plate, layer), "talking head"
    if dev == "priceline":
        small(layer, lambda L: SF.dev_priceline(L, t, y_top=0.0)); return SF.compose(plate, layer), "talking head"
    if dev == "check_dark":
        base = Image.new("RGB", (W, H), INK)
        SF.eyebrow(layer, "WHAT I'M STUDYING FOR HER" if body_id == "EXIT" else "WHAT I DECIDE BEFORE BALLOT DAY", y_frac=0.26, size=38, bg=GOLD, fg=INK)
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
        SF.card_number(layer, (W // 2, int(H * 0.675)), "1,268", SF.ANTON(200), fill=ORANGE, anchor="mm")
        SF.eyebrow(layer, "UNITS SHE'D COMPETE WITH AT EXIT", y_frac=0.13, size=38, bg=INK, fg=GOLD)
    elif dev == "ballot":
        base = SF.broll("deck_p10", darken=0.70); SF.eyebrow(layer, "BALLOT DAY · YOUR NUMBER IS CALLED", y_frac=0.13, size=38, bg=RED, fg=WHITE); SF.dev_ballot(layer, t, y_top=0.30)
    elif dev == "slam_80k":
        base = SF.broll("deck_p16", darken=0.75, zoom=1.04); SF.dev_slam(layer, "$80,000", t, y=0.46, size=210, color=RED, rot=-4)
        SF.shadow_text(layer, (W // 2, int(H * 0.60)), "“MAYBE WE CAN STRETCH…”", SF.SERIF_I(54), IVORY + (255,), anchor="mm", blur=10)
    elif dev == "plan_abc":
        base = Image.new("RGB", (W, H), INK); plan_abc(layer, t)
    else:
        base = plate
    return SF.compose(base, layer), "SCENE"

# ---------------------------------------------------------------- end cards
def endcard(look, t=1.0):
    st = look["end"]
    if st == "gold": return SF.dev_endcard(t)
    layer = SF.new_layer(); d = ImageDraw.Draw(layer)
    if st == "dark":
        base = Image.new("RGB", (W, H), INK); title_col = IVORY; btn = None; btn_fg = WHITE; sub = IVORY
    elif st == "photo":
        base = _photo(4, darken=0.55, anchor_y=0.3, anchor_x=1.0); SF.scrim(layer, int(H * 0.25), int(H * 0.75), alpha=200, color=INK); title_col = IVORY; btn = GOLD; btn_fg = INK; sub = IVORY
    else:  # red
        base = Image.new("RGB", (W, H), RED); title_col = WHITE; btn = INK; btn_fg = WHITE; sub = WHITE
    d.text((W // 2, int(H * 0.40)), "LIVE 60-MINUTE WEBINAR", font=SF.OSWALD(34, 500), fill=(GOLD if st != "red" else WHITE) + (255,), anchor="mm")
    f = SF.SERIF(96)
    for i, ln in enumerate(("Would I buy", "Thomson Reserve", "for my daughter?")):
        SF.shadow_text(layer, (W // 2, int(H * (0.46 + 0.06 * i))), ln, f, ((GOLD if st != "red" else WHITE) if i == 2 else title_col) + (255,), anchor="mm")
    sc = SF.overshoot(min(1, max(0, (t - 0.2) / 0.45))); s = "SAVE MY SEAT  ›"; fb = SF.ARCHIVO(50); tw = SF.text_w(fb, s)
    bw, bh = (tw + 120) * sc, 120 * sc; cx, cy = W // 2, int(H * 0.68)
    if btn is None: d.rounded_rectangle((cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2), int(60 * sc), outline=WHITE + (255,), width=5)
    else: SF.rrect(layer, (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2), int(60 * sc), btn + (255,), shadow=16)
    if sc > 0.6: d.text((cx, cy), s, font=fb, fill=btn_fg + (255,), anchor="mm")
    d.text((W // 2, int(H * 0.745)), "Link below · before the 17 Oct preview", font=SF.INTER(28, 500), fill=sub + (190,), anchor="mm")
    return SF.compose(base, layer)
