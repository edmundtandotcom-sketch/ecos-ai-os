#!/usr/bin/env python3
"""One-time prep for styleframes.py: fonts, emoji glyphs, and the deck/ebook
pages used as b-roll, rendered at 220 dpi.

    pip install pillow numpy pymupdf imageio-ffmpeg
    python prep_assets.py

Writes ../fonts, ../emoji, ../assets next to this folder's parent (the same
layout styleframes.py expects: ROOT/fonts, ROOT/emoji, ROOT/assets). Fonts are
OFL from the google/fonts repo; emoji are Twemoji (CC-BY 4.0) 72px PNGs.
"""
import sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   # ../  (02_AD_EDIT_DIRECTION)
FONTS = ROOT / "fonts"; EMOJI = ROOT / "emoji"; ASSETS = ROOT / "assets"
RAW = ROOT.parent / "Raw Assets"

GF = "https://raw.githubusercontent.com/google/fonts/main/"
FONT_FILES = {
    "Anton-Regular.ttf": "ofl/anton/Anton-Regular.ttf",
    "ArchivoBlack-Regular.ttf": "ofl/archivoblack/ArchivoBlack-Regular.ttf",
    "Montserrat[wght].ttf": "ofl/montserrat/Montserrat%5Bwght%5D.ttf",
    "Oswald[wght].ttf": "ofl/oswald/Oswald%5Bwght%5D.ttf",
    "PlayfairDisplay[wght].ttf": "ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf",
    "Inter[opsz,wght].ttf": "ofl/inter/Inter%5Bopsz,wght%5D.ttf",
    "BebasNeue-Regular.ttf": "ofl/bebasneue/BebasNeue-Regular.ttf",
    "DMSerifDisplay-Regular.ttf": "ofl/dmserifdisplay/DMSerifDisplay-Regular.ttf",
}
TW = "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/"
EMOJI_CODES = ["1f4b0", "1f3e0", "1f4c9", "1f4c8", "26a0", "1f467", "1f687", "1f3eb", "1f333",
               "1f5f3", "274c", "2705", "1f3af", "1f4c5", "1f511", "1f4b8", "1f914", "1f6a9",
               "1f4cd", "1f3d9", "1f44b", "1f6ab", "1f9e0", "1f4ca", "1f3e2", "23f3"]
PAGES = {
    "260825 Thomson Reserve - Presentation deck to ICs.pdf": ("deck", [1, 4, 6, 10, 11, 12, 16, 17, 18, 33]),
    "Thomson Reserve Ebook V3 - English.pdf": ("ebook", [2, 5, 6, 7, 8, 9, 12, 13, 15, 16, 17]),
}

def fetch(url, dest):
    if dest.exists():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    print("get", dest.name)
    urllib.request.urlretrieve(url, dest)

def main():
    for name, rel in FONT_FILES.items():
        fetch(GF + rel, FONTS / name)
    for c in EMOJI_CODES:
        fetch(TW + f"{c}.png", EMOJI / f"{c}.png")
    try:
        import pymupdf
    except ImportError:
        sys.exit("pip install pymupdf")
    ASSETS.mkdir(exist_ok=True)
    for pdf, (tag, pages) in PAGES.items():
        src = RAW / pdf
        if not src.exists():
            print("missing", src); continue
        d = pymupdf.open(src)
        for p in pages:
            out = ASSETS / f"{tag}_p{p:02d}.png"
            if out.exists():
                continue
            d[p - 1].get_pixmap(dpi=220).save(out); print("page", out.name)
    print("ok")

if __name__ == "__main__":
    main()
