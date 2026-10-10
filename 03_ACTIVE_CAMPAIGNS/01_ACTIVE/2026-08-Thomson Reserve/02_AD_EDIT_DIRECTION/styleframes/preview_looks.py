"""Format sheets: one strip per ad showing its look over clean frames of the real take, before any full render.
    python preview_looks.py <plates folder> <photos folder> <out folder>"""
import sys, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
from PIL import Image, ImageDraw
import styleframes as SF, looks as LK, tr_scripts as TS
from styleframes import W, H, INK, GOLD, WHITE

plates_dir, photos_dir, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
SF.load_photos(str(photos_dir))
PLATES = [Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS) for p in sorted(plates_dir.glob("*.png"))]

def words_of(text, n=3, start=0): return [w.strip(".,?!:;—") for w in text.split()][start:start + n]
def proof_words(hook_id):
    t = TS.DAUGHTER_HOOK_1 if hook_id == "DH1" else TS.HOOKS[hook_id][1]
    ws = [w.strip(".,?!:;—") for w in t.split()]
    for i, w in enumerate(ws):
        if "$" in w: return ws[max(0, i - 1):i + 2], 1 if i > 0 else 0
    return ws[-3:], 2
def question_words(hook_id):
    t = TS.DAUGHTER_HOOK_1 if hook_id == "DH1" else TS.HOOKS[hook_id][1]
    ws = [w.strip(".,?!:;—") for w in t.split()]; return ws[-3:], 2
BODY_WORDS = {"EXIT": (["WHO", "BUYS", "IT"], 1, ["2-BED", "OR", "3-BED?"], 2, ["JOIN", "ME", "LIVE"], 2),
              "BALLOT": (["MY", "MAXIMUM", "PRICE"], 2, ["STRETCH", "ANOTHER", "$80,000"], 2, ["BEFORE", "BALLOT", "DAY"], 1),
              "FULL": (["1,268", "UNITS"], 0, ["$500,000", "ABOVE"], 0, ["CLICK", "THE", "LINK"], 2)}

def sheet(ad_id, look):
    m = re.match(r"TR_H(\d+)_(EXIT|BALLOT)", ad_id)
    hook_id = int(m.group(1)) if m else "DH1"; body_id = m.group(2) if m else "FULL"
    headline = TS.HOOKS[hook_id][0] if m else "WOULD I BUY THIS FOR MY DAUGHTER?"
    hook_text = TS.HOOKS[hook_id][1] if m else TS.DAUGHTER_HOOK_1
    frames = []
    # 1. open: headline + first caption (title looks show the title card)
    L = SF.new_layer(); plate = PLATES[0]
    LK.draw_headline(L, headline, look, t=1.0, t_abs=0.6)
    if look["headline"] != "title": LK.draw_caption(L, words_of(hook_text, 3), 1, look)
    frames.append((SF.compose(plate, L), "0:00 open · " + LK.HEADLINES[look["headline"]].split(",")[0]))
    # 2. hook caption on the talking head (no device) — how a plain line reads
    L = SF.new_layer(); LK.draw_headline(L, headline, look, t=1.0, t_abs=3.0); LK.draw_caption(L, words_of(hook_text, 3, 6), 2, look)
    frames.append((SF.compose(PLATES[1], L), "talking head · captions in this style"))
    # 3. proof device / scene
    pw, pa = proof_words(hook_id)
    im, kind = LK.hook_scene(PLATES[2], look, hook_id)
    L = SF.new_layer()
    if kind != "SCENE": LK.draw_headline(L, headline, look, t=1.0, t_abs=5.0)
    LK.draw_caption(L, pw, pa, look, y=0.64 if look["hook_dev"] in ("receipt", "card", "priceline") else (0.82 if kind == "SCENE" else 0.70))
    frames.append((SF.compose(im, L), ("SCENE, no talking head · " if kind == "SCENE" else "talking head · ") + LK.HOOK_DEVS[look["hook_dev"]].replace("SCENE · ", "")))
    # 4. back to the talking head: the question, underline
    qw, qa = question_words(hook_id); L = SF.new_layer(); LK.draw_headline(L, headline, look, t=1.0, t_abs=9.0); LK.draw_caption(L, qw, qa, look)
    frames.append((SF.compose(PLATES[3], L), "back to the talking head · the question"))
    # 5. body device / scene
    bw = BODY_WORDS[body_id]
    if body_id == "FULL":
        im = SF.compose(SF.broll("deck_p17", darken=0.78), (lambda L: (SF.dev_dotgrid(L, 1.0), SF.card_number(L, (W // 2, int(H * 0.675)), "84%", SF.ANTON(220), fill=SF.ORANGE, anchor="mm"), L)[2])(SF.new_layer())); kind = "SCENE"
        desc = "SCENE · 1,268 dots, 84% light up (one of the Body 1 devices)"
    else:
        im, kind = LK.body_scene(PLATES[4], look, body_id); desc = LK.BODY_DEVS[look["body_dev"]].replace("SCENE · ", "")
    L = SF.new_layer()
    if kind != "SCENE": SF.eyebrow(L, "LIVE WEBINAR · 17 OCT")
    LK.draw_caption(L, bw[2], bw[3], look, y=0.64 if kind != "SCENE" else 0.84)
    frames.append((SF.compose(im, L), ("SCENE, no talking head · " if kind == "SCENE" else "talking head · ") + desc))
    # 6. CTA on the talking head
    L = SF.new_layer(); SF.eyebrow(L, "LIVE WEBINAR · 17 OCT"); LK.draw_caption(L, bw[4], bw[5], look)
    frames.append((SF.compose(PLATES[6], L), "talking head · the call to action"))
    # 7. end card
    frames.append((LK.endcard(look), "end card · " + LK.ENDS[look["end"]]))
    # ---- the sheet
    fw, fh = 300, 533; pad = 14; top = 150; cap = 70
    S = Image.new("RGB", (pad + len(frames) * (fw + pad), top + fh + cap + pad), (245, 244, 240)); d = ImageDraw.Draw(S)
    d.rectangle((0, 0, S.width, top), fill=INK)
    d.text((pad + 4, 22), ad_id, font=SF.ARCHIVO(40), fill=GOLD)
    d.text((pad + 4, 74), f"HOOK {hook_id}: {headline}   +   BODY: {body_id}", font=SF.OSWALD(28, 600), fill=WHITE)
    d.text((pad + 4, 110), LK.recipe(look)[:230], font=SF.INTER(19, 500), fill=(200, 200, 210))
    for i, (im, label) in enumerate(frames):
        x = pad + i * (fw + pad); S.paste(im.resize((fw, fh), Image.LANCZOS), (x, top))
        words = label.split(); lines = []; cur = ""
        for w in words:
            if len(cur) + len(w) > 34: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        lines.append(cur)
        for j, ln in enumerate(lines[:3]): d.text((x, top + fh + 8 + j * 20), ln, font=SF.INTER(16, 600 if j == 0 else 500), fill=(30, 30, 36) if j == 0 else (90, 90, 100))
    p = out / f"{ad_id}_format.jpg"; S.save(p, quality=84); return p

only = sys.argv[4].split(",") if len(sys.argv) > 4 else None
for ad_id, look in LK.LOOKS.items():
    if only and not any(o in ad_id for o in only): continue
    print("sheet", sheet(ad_id, look).name)
