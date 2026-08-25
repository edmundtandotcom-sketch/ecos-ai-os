#!/usr/bin/env python3
"""Build the NL01 brand graphics (G1-G10) as PNGs via headless Chromium.

Usage:  python3 graphics.py OUTDIR

Each graphic is rendered from inline HTML at 1080x1920 (or its own size for the
small chips) and screenshotted with Playwright. Full-frame cards are opaque
navy; overlay elements keep a transparent background so ffmpeg can composite
them.
"""
import sys
import os
import pathlib

NAVY = "#0B1020"
PANEL = "#141B33"
BLUE = "#005CE6"
YELLOW = "#FFE800"

# Montserrat / Archivo Black are pulled from Google Fonts when reachable;
# DejaVu Sans Bold is the documented fallback (note it in QC_REPORT if used).
FONT_LINK = (
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Archivo+Black&family=Montserrat:wght@700;800&display=swap">'
)
DISPLAY = "'Archivo Black','DejaVu Sans',sans-serif"
BODY_FONT = "'Montserrat','DejaVu Sans',sans-serif"


def page_html(body, *, transparent=False, extra_css=""):
    bg = "transparent" if transparent else NAVY
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONT_LINK}
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;background:{bg};
  font-family:{BODY_FONT};-webkit-font-smoothing:antialiased}}
.wrap{{width:1080px;height:1920px;display:flex;flex-direction:column;
  justify-content:center;align-items:center;padding:0 90px}}
/* font-weight:900 keeps the display face heavy when Archivo Black is
   unavailable and the stack falls back to DejaVu Sans. */
.display{{font-family:{DISPLAY};font-weight:900;color:#fff;line-height:1.06;
  letter-spacing:-.01em}}
.y{{color:{YELLOW}}}
.chip{{display:inline-block;background:{BLUE};color:#fff;font-family:{BODY_FONT};
  font-weight:800;border-radius:14px;padding:22px 38px;font-size:52px;
  letter-spacing:.01em;white-space:nowrap}}
{extra_css}
</style></head><body>{body}</body></html>"""


def chart_svg():
    """Two flat polylines, no gridlines, no axis numbers."""
    return f"""
<svg width="900" height="620" viewBox="0 0 900 620">
  <polyline points="40,540 200,470 360,395 520,300 680,205 860,95"
    fill="none" stroke="#fff" stroke-width="2.5"/>
  <polyline points="40,560 200,552 360,540 520,470 680,330 860,120"
    fill="none" stroke="{YELLOW}" stroke-width="2.5"/>
  <text x="600" y="70" fill="#fff" font-family="{BODY_FONT}" font-weight="700"
    font-size="30">S&amp;P 500</text>
  <text x="360" y="600" fill="{YELLOW}" font-family="{BODY_FONT}"
    font-weight="700" font-size="30">YOUR NEW LAUNCH</text>
</svg>"""


def data_card(number, line1, line2):
    """Card only (not full-frame) so ffmpeg controls where it sits."""
    return page_html(f"""
<div style="display:inline-block">
  <div style="width:920px;background:{PANEL};border-radius:12px;padding:44px 52px 48px">
    <div class="display" style="font-size:104px;color:{YELLOW}">{number}</div>
    <div style="height:2px;background:{YELLOW};opacity:.85;margin:22px 0 26px"></div>
    <div style="color:#fff;font-weight:700;font-size:36px;white-space:nowrap;
      letter-spacing:.005em">{line1}</div>
    <div style="color:#fff;opacity:.82;font-weight:700;font-size:30px;
      margin-top:14px;white-space:nowrap;letter-spacing:.005em">{line2}</div>
  </div>
</div>""", transparent=True,
        extra_css="html,body{width:auto;height:auto}")


def build_specs():
    s = {}

    s["G1_chart"] = dict(html=page_html(f"""
<div class="wrap" style="justify-content:flex-start;padding-top:300px">
  <div class="display" style="font-size:96px;text-align:center">
    THE BENCHMARK:<br>BEAT THE <span class="y">S&amp;P 500</span></div>
  <div style="margin-top:220px">{chart_svg()}</div>
</div>"""), size=(1080, 1920))

    s["G2a_card"] = dict(html=data_card(
        "22.9%/YR",
        "BOUGHT $1.15M &rarr; SOLD $1.525M",
        "$321K committed &middot; 3 years &middot; net ~$282K"), size=None)

    s["G2b_card"] = dict(html=data_card(
        "12.9%/YR",
        "BOUGHT $1.05M &rarr; SOLD $1.28M",
        "$292K committed &middot; 4 years"), size=None)

    s["G3_question"] = dict(html=page_html("""
<div class="wrap">
  <div class="display" style="font-size:104px;text-align:center">
    CAN THIS PROJECT<br>BEAT THE S&amp;P 500?</div>
  <div style="width:180px;height:12px;background:%s;margin-top:64px"></div>
</div>""" % YELLOW), size=(1080, 1920))

    rows = [("%", "RETURN ON EQUITY"), ("$", "WALKAWAY PRICE"), ("3", "NEXT 3 MOVES")]
    row_html = "".join(f"""
  <div style="display:flex;align-items:center;gap:44px;margin-top:74px;width:100%">
    <div style="width:132px;height:132px;border:5px solid {YELLOW};border-radius:50%;
      display:flex;align-items:center;justify-content:center;flex:none">
      <span class="display" style="font-size:64px;color:{YELLOW}">{badge}</span></div>
    <div style="color:#fff;font-weight:800;font-size:58px;letter-spacing:.01em">{label}</div>
  </div>""" for badge, label in rows)
    s["G4_framework"] = dict(html=page_html(f"""
<div class="wrap" style="align-items:flex-start">
  <div class="display" style="font-size:82px">THE NEW LAUNCH LADDER&trade;</div>
  <div style="width:100%">{row_html}</div>
</div>"""), size=(1080, 1920))

    for name, text in [("G5_chip_capital", "$500K&ndash;$1M"),
                       ("G5_chip_mortgage", "25 YEARS"),
                       ("G5_chip_wait", "4 YEARS")]:
        s[name] = dict(html=page_html(
            f'<div style="display:inline-block"><span class="chip">{text}</span></div>',
            transparent=True,
            extra_css="body{width:auto;height:auto}html{width:auto;height:auto}"),
            size=None)

    s["G6_hook"] = dict(html=page_html("""
<div style="width:1080px;padding:90px 80px 0">
  <div class="display" style="font-size:92px">
    IS THIS YOUR<br><span class="y">2ND, 3RD OR 4TH</span><br>PROPERTY?</div>
</div>""", transparent=True,
        extra_css="body{height:auto}html{height:auto}"), size=None)

    s["G7a_punch"] = dict(html=page_html(f"""
<div style="width:1080px;padding:0 80px">
  <div class="display" style="font-size:78px">ALMOST ANY PROPERTY<br>
    CAN MAKE <span class="y">SOME</span> GAIN.</div></div>""",
        transparent=True, extra_css="body{height:auto}html{height:auto}"), size=None)

    s["G7b_punch"] = dict(html=page_html(f"""
<div style="width:1080px;padding:0 80px">
  <div class="display" style="font-size:78px">&lsquo;I MADE MONEY&rsquo;<br>
    IS NO LONGER <span class="y">ENOUGH</span>.</div></div>""",
        transparent=True, extra_css="body{height:auto}html{height:auto}"), size=None)

    for name, text in [("G8_entry", "ENTRY PRICE"), ("G8_unit", "THE UNIT"),
                       ("G8_buyer", "FUTURE BUYER"), ("G8_exit", "EXIT PRICE"),
                       ("G8_equity", "EQUITY RELEASED")]:
        s[name] = dict(html=page_html(
            f'<div style="display:inline-block"><span class="chip">{text}</span></div>',
            transparent=True,
            extra_css="body{width:auto;height:auto}html{width:auto;height:auto}"),
            size=None)

    s["G9_cta"] = dict(html=page_html(
        '<div style="display:inline-block"><span class="chip" '
        'style="font-size:56px;padding:26px 46px">TELL ME YOUR PROJECT &rsaquo;</span></div>',
        transparent=True,
        extra_css="body{width:auto;height:auto}html{width:auto;height:auto}"), size=None)

    s["G10_endcard"] = dict(html=page_html(f"""
<div class="wrap">
  <div style="width:260px;height:260px;border:8px solid {BLUE};border-radius:44px;
    display:flex;align-items:center;justify-content:center">
    <span class="display" style="font-size:150px;color:{BLUE}">R</span></div>
  <div style="color:rgba(255,255,255,.6);font-weight:800;font-size:52px;
    letter-spacing:.34em;margin-top:64px">REI METHOD</div>
</div>"""), size=(1080, 1920))

    return s


def find_chromium():
    """Prefer a preinstalled browser over playwright's version-pinned path,
    which often mismatches the pip package's expected build number."""
    root = pathlib.Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for pat in ("chromium-*/chrome-linux/chrome",
                "chromium_headless_shell-*/*/chrome-headless-shell"):
        hits = sorted(root.glob(pat))
        if hits:
            return str(hits[-1])
    return None


def main():
    outdir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "graphics")
    outdir.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright

    specs = build_specs()
    exe = os.environ.get("CHROMIUM_PATH") or find_chromium()
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe, args=["--no-sandbox"]) \
            if exe else p.chromium.launch()
        for name, spec in specs.items():
            w, h = spec["size"] or (1080, 400)
            page = browser.new_page(viewport={"width": w, "height": h},
                                    device_scale_factor=1)
            page.set_content(spec["html"], wait_until="networkidle")
            page.wait_for_timeout(400)  # let webfonts settle
            target = outdir / f"{name}.png"
            if spec["size"]:
                page.screenshot(path=str(target), omit_background=True)
            else:
                el = page.query_selector("body > *")
                el.screenshot(path=str(target), omit_background=True)
            page.close()
            print("wrote", target)
        browser.close()


if __name__ == "__main__":
    main()
