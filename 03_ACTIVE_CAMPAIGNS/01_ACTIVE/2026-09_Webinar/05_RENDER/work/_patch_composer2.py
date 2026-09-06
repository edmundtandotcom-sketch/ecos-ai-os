from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)


# --- 1. tighter gaps
rep("MAX_GAP, PAD_OUT, PAD_IN = 0.38, 0.22, 0.12",
    "MAX_GAP, PAD_OUT, PAD_IN = 0.20, 0.10, 0.07")

# --- 2. speed applied at the tighten stage with frame blending (no judder)
rep("def tighten(pieces):", "def tighten(pieces, speed=1.0):")
rep('''    stamp = WORK / "_tight.json"
    dest = WORK / "_tight.mp4"
    segdir = WORK / "_tight"
    segdir.mkdir(parents=True, exist_ok=True)
    if dest.exists() and stamp.exists() and json.loads(stamp.read_text()) == [list(p) for p in plan]:''',
    '''    tag = f"_s{int(round(speed * 100))}"
    stamp = WORK / f"_tight{tag}.json"
    dest = WORK / f"_tight{tag}.mp4"
    segdir = WORK / f"_tight{tag}"
    segdir.mkdir(parents=True, exist_ok=True)
    # Speed lives HERE, not on the final render: setpts on a 30fps cut sampled
    # back to 30fps drops every ~7th frame and reads as jerking. Blending the
    # neighbouring frames (minterpolate blend) keeps the motion continuous.
    vf = f"scale={W}:{H},setsar=1"
    af = []
    if speed != 1.0:
        vf += f",setpts=PTS/{speed},minterpolate=fps={FPS}:mi_mode=blend"
        af = ["-af", f"atempo={speed}"]
    if dest.exists() and stamp.exists() and json.loads(stamp.read_text()) == [list(p) for p in plan]:''')
rep('''                 "-vf", f"scale={W}:{H},setsar=1",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",''',
    '''                 "-vf", vf, *af,
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",''')
rep('''        for w in words:
            if a - 0.001 <= w["s"] < b:
                out.append(dict(w=w["w"], s=round(base + max(0.0, w["s"] - a), 3),
                                e=round(base + min(d, max(0.0, w["e"] - a)), 3)))''',
    '''        for w in words:
            if a - 0.001 <= w["s"] < b:
                out.append(dict(w=w["w"], s=round(base + max(0.0, (w["s"] - a) / speed), 3),
                                e=round(base + min(d, max(0.0, (w["e"] - a) / speed)), 3)))''')
rep('''    raw = sum(hi - lo for _, lo, hi in pieces)
    print(f"  tight: {raw:.1f}s -> {base:.1f}s ({(1 - base / raw) * 100:.0f}% dead air removed)")''',
    '''    raw = sum(hi - lo for _, lo, hi in pieces)
    print(f"  tight @{speed:.2f}x: {raw:.1f}s -> {base:.1f}s")''')

# --- 3. final pass: no speed change there; music selectable per spec
rep('SPEED = FX.HOUSE["speed"]',
    'SPEED = 1.0   # speed is applied in tighten(); the final pass only mixes')
rep('''    inputs = ["-i", str(part), "-stream_loop", "-1", "-i", str(AUDIO / FX.HOUSE["music"])]''',
    '''    music = spec.get("music", FX.HOUSE["music"])
    music_p = Path(music) if Path(music).is_absolute() else AUDIO / music
    inputs = ["-i", str(part), "-stream_loop", "-1", "-i", str(music_p)]''')
rep('''    f.append(f"[1:a]volume={MUSIC_VOL},afade=t=out:st={out_d-2.0:.2f}:d=2.0[bed]")''',
    '''    mvol = spec.get("music_vol", MUSIC_VOL)
    f.append(f"[1:a]volume={mvol},afade=t=out:st={out_d-2.0:.2f}:d=2.0[bed]")''')

# --- 4. captions on EVERY shot (only explicit nocap skips); per-beat cap_y
rep('''        if sh.get("nocap") or (sh["dev"] and sh["dev"] not in ("icon_row", "lower_ticker", "split_labels")):
            continue
        cue = [w["w"] for w in sh["cue"]]
        png = capdir / f"c{k:03d}.png"
        y = 0.86 if (sh.get("split") or sh.get("backdrops")) else 0.655''',
    '''        if sh.get("nocap"):
            continue
        cue = [w["w"] for w in sh["cue"]]
        png = capdir / f"c{k:03d}.png"
        # one caption band for the whole ad: low (0.80), on the speaker panel
        # of a split (0.86), or wherever a beat says its plate leaves room
        y = sh.get("cap_y") or (0.86 if (sh.get("split") or sh.get("backdrops")) else CAP_Y)''')
rep("CAP_MAX_WORDS = 3", "CAP_MAX_WORDS = 3\nCAP_Y = 0.80\nCAP_SIZE = 82")
rep('''        DV.caption_plate(png, cue, accent=score_accent(sh["cue"]),
                         emoji=DV.pick_emoji(" ".join(cue)), y_frac=y)''',
    '''        DV.caption_plate(png, cue, accent=score_accent(sh["cue"]),
                         emoji=DV.pick_emoji(" ".join(cue)), y_frac=y, size=CAP_SIZE)''')
rep('''                          motion=(dev or {}).get("motion"),
                          nocap=(dev or {}).get("nocap", False)))''',
    '''                          motion=(dev or {}).get("motion"),
                          cap_y=(dev or {}).get("cap_y"),
                          nocap=(dev or {}).get("nocap", False)))''')

# --- 5. a device runs for its own secs, not to the end of the last shot that touched it
rep('''        t0, t1 = owners[0]["out0"], owners[-1]["out1"]
        what = b.get("dev") or b.get("backdrop") or b.get("photo") or b.get("treat") or "shot"''',
    '''        t0 = owners[0]["out0"]
        t1 = min(owners[-1]["out1"], t0 + b["secs"] + 0.15)
        what = b.get("dev") or b.get("backdrop") or b.get("photo") or b.get("treat") or "shot"''')

# --- 6. CLI: --speed, output name suffix; cache keyed on the tight file
rep('''    ap.add_argument("--tighten-only", action="store_true")
    a = ap.parse_args()''',
    '''    ap.add_argument("--tighten-only", action="store_true")
    ap.add_argument("--speed", type=float, default=1.15)
    a = ap.parse_args()''')
rep('''    tight, words, smap = tighten(PIECES)
    if a.tighten_only:
        return
    print("== COMPOSE ==")
    compose(SPEC, tight, words, smap, OUT_NAME)''',
    '''    tight, words, smap = tighten(PIECES, a.speed)
    if a.tighten_only:
        return
    print("== COMPOSE ==")
    name = OUT_NAME.replace(".mp4", f"_{int(round(a.speed * 100))}.mp4")
    compose(SPEC, tight, words, smap, name)''')
rep('''                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig}, sort_keys=True)''',
    '''                         | {"cue": [w["w"] for w in s["cue"]], "cap_sig": cap_sig,
                            "src_file": Path(tight).name}, sort_keys=True)''')

p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("composer patched, syntax ok")
