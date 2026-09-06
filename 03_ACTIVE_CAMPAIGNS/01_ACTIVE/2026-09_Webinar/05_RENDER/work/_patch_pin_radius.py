

# ---------------------------------------------------------------- map / radius

def pin_radius(outdir, seconds, label="800M", sub="OF THOMSON-EAST COAST LINE STATIONS",
               line_colour=(150, 90, 40), radius_px=330, ground=(16, 24, 40)):
    """A location pin drops onto a stylised map and a radius ring grows out.

    The "within 800m of the station" beat. Ground is a dark map: faint block
    grid, a couple of soft road curves and the MRT line as a thick coloured
    stroke with a station dot. The pin lands (overshoot), the ring expands
    to `radius_px` with a dashed edge and the label rides its rim. Full
    frame; caption band (below 0.78) is left clear.
    """
    outdir = _prep(outdir)
    n = _frames(seconds)
    cx, cy = W // 2, int(H * 0.40)
    f_lab = font(120)
    f_sub = D.font(44, display=False)
    for i in range(n):
        t = i / FPS
        base = Image.new("RGB", (W, H), ground)
        d = ImageDraw.Draw(base)
        # block grid
        for x in range(0, W, 96):
            d.line([(x, 0), (x, H)], fill=(24, 34, 54), width=2)
        for y in range(0, H, 96):
            d.line([(0, y), (W, y)], fill=(24, 34, 54), width=2)
        # soft "roads"
        d.line([(0, cy + 220), (W, cy - 160)], fill=(38, 52, 78), width=26)
        d.line([(cx - 420, 0), (cx + 60, H)], fill=(38, 52, 78), width=22)
        # MRT line (TEL brown) with a station dot at the pin
        d.line([(80, cy + 520), (cx, cy), (W - 60, cy - 470)], fill=line_colour, width=30, joint="curve")
        img = base.convert("RGBA")
        d = ImageDraw.Draw(img)
        # radius ring grows from 0.35s
        p = ease_out(min(1.0, max(0.0, (t - 0.35) / 0.9)))
        r = int(radius_px * p)
        if r > 4:
            ring = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            rd = ImageDraw.Draw(ring)
            rd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 232, 0, 46), outline=(255, 232, 0, 255), width=8)
            img.alpha_composite(ring)
        # station dot
        d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=WHITE, outline=line_colour, width=8)
        # pin drops in the first 0.35s with a bounce
        q = ease_back(min(1.0, t / 0.35))
        py = cy - 40 - int(260 * (1 - q))
        s = 1.0
        d.ellipse([cx - 58 * s, py - 150 * s, cx + 58 * s, py - 34 * s], fill=RED)
        d.polygon([(cx - 44 * s, py - 70 * s), (cx + 44 * s, py - 70 * s), (cx, py)], fill=RED)
        d.ellipse([cx - 22 * s, py - 114 * s, cx + 22 * s, py - 70 * s], fill=WHITE)
        # label on the rim once the ring is out
        if p > 0.55:
            a = int(255 * min(1.0, (p - 0.55) / 0.3))
            lab = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ld = ImageDraw.Draw(lab)
            tw = ld.textlength(label, font=f_lab)
            lx, ly = cx + r - int(tw / 2), cy + r - 20
            ld.rounded_rectangle([lx - 26, ly - 12, lx + tw + 26, ly + 132], 18, fill=(255, 232, 0, a))
            ld.text((lx, ly), label, font=f_lab, fill=(20, 20, 20, a))
            sw = ld.textlength(sub, font=f_sub)
            ld.text(((W - sw) / 2, int(H * 0.68)), sub, font=f_sub, fill=(255, 255, 255, a))
            img.alpha_composite(lab)
        _save(img, outdir, i)
    return n


REGISTRY["pin_radius"] = pin_radius
FULL_FRAME.add("pin_radius")
