#!/usr/bin/env python3
"""V1 "The Receipt" — full ad compositor for Thomson Reserve × Daughter.

Takes the two selfie takes (Daughter Hook 1 + Body 1), the family photos and
the deck renders, and produces the finished 9:16 ad the way EDB §4 and the
human-edit pass (§2b) describe it. Runs anywhere Python + ffmpeg run; no GPU.

    python render_v1.py --hook "Selfie Daughter Hook 1.mp4" --body "Selfie Body1.mp4" \
                        --photos ../photos --stage all

Stages: audio → asr → tighten → plan → render → qc  (each cached in OUT_DIR)

Speech recognition: sherpa-onnx zipformer (token timestamps) — the recognised
words are ALIGNED TO THE SCRIPT, so captions show the script's spelling and
digits ("$1.15M", "1,268") with the take's real timing. Misheard words cannot
reach the screen.
"""
import argparse, json, math, random, re, subprocess, sys, wave
from difflib import SequenceMatcher
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import styleframes as SF                                   # devices, captions, palette
from styleframes import W, H, INK, GOLD, RED, ORANGE, WHITE, IVORY

FPS = 30
OUT = HERE / "out" / "v1"
ASR_DIR = HERE.parent / "asr" / "sherpa-onnx-zipformer-en-2023-06-26"
FFMPEG = SF.ffmpeg_bin()

# ------------------------------------------------------------------ the script (what he was asked to say)
SCRIPT_HOOK = ("My daughter already benefited from Parc Clematis — bought at $1.15M, sold at $1.525M. "
               "Now if Thomson Reserve is going to be her next property, I'm asking one thing: "
               "can it move her forward again?")

SCRIPT_BODY = """Thomson Reserve preview starts 17 October.
If you want to find out my analysis if I will buy for her, join me in a LIVE 60-minute webinar.
Here are 3 things that's causing me to think twice about Thomson Reserve.
What I don't like about Thomson Reserve.
First. There are 1,268 units. And 1,066 of them — 84% — the 2 & 3 bedrooms — a high supply risk.
So when you eventually sell, you're not competing with District 20 solely.
You're competing with your direct neighbours.
Second. You're buying this after the Thomson East Coast MRT story, not before it.
Look at what happened to prices within 800m of TEL stations.
Up 20.86% across the four years while the line was being built.
After it opened? 5.87% in two years. Under 3% a year.
Third. The price.
If it launches at $2,800 to $3,000 psf — and that's an estimate, nothing official yet — a 3-bedroom premium lands around $3.2 million onwards.
The highest average quantum a 3-bedroom resale has been fetching in District 20 — near an MRT, near a top primary school, under ten years old — from $2.7m to $2.8 million.
So you'd be paying more than $500,000 above the average the district is currently proving.
What I like about Thomson Reserve. Three reasons.
One. The MRT is genuinely at the door. Two minutes, sheltered, straight into Upper Thomson Exit 2.
Two. Ai Tong School within 1km. No mad rush to drive and get stuck in traffic sending and fetching your kids. Oversubscribed nearly every year. And now you have a chance to buy into it.
Three. Central Catchment. Over 2,000 hectares of forest, more than 20km of trails.
Most views in Singapore are temporary — somebody eventually builds in front of you.
But this one, a forever million dollar view.
Thomson Reserve Preview is on 17 October. So I'm running a live webinar session giving you insights on my full decision making process and analysis on buying Thomson Reserve as my next property and how I will be preparing before and during the ballot.
The exact price I walk away at.
Which stacks I'd go for, and which I wouldn't touch at any price.
How I'd prepare before and during the ballot, so I'm not deciding under pressure on the day.
And whether this works as a second property at all, or only as an own-stay.
If Thomson Reserve is on your list, come and pressure-test it with me before preview — not after.
Click the link below and join me live."""

# ------------------------------------------------------------------ tightening + captions
MAX_GAP, PAD_IN, PAD_OUT = 0.38, 0.14, 0.24
SILENCE_DB, SILENCE_MIN = -35, 0.30
CAP_MAX_WORDS = 3
ZOOM_LADDER = [1.00, 1.10, 1.20, 1.10]
STOP = set("a an the and or but to of for in on at is are was your my i we you it that this so if as with have has be been".split())

def run(cmd, quiet=True):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:]); raise SystemExit(f"ffmpeg failed: {' '.join(map(str, cmd[:6]))}…")
    return r

def probe(path):
    r = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True)
    m = re.search(r"(\d{2,5})x(\d{2,5})[,\s]", r.stderr); d = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    fps = re.search(r"([\d.]+) fps", r.stderr)
    w, h = (int(m.group(1)), int(m.group(2))) if m else (None, None)   # audio-only files have no dims
    dur = int(d.group(1)) * 3600 + int(d.group(2)) * 60 + float(d.group(3))
    # rotation metadata (phones)
    rot = re.search(r"rotate\s*:\s*(-?\d+)", r.stderr) or re.search(r"displaymatrix:.*?(-?\d+\.\d+) degrees", r.stderr)
    if w and rot and abs(int(float(rot.group(1)))) % 180 == 90:
        w, h = h, w
    return dict(w=w, h=h, dur=dur, fps=float(fps.group(1)) if fps else 30.0)

def norm(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"[^a-z0-9$%.,'& ]+", " ", s)
    return s

def script_words(text):
    """Script → tokens that keep '$1.15M', '1,268', '84%' whole; punctuation marks sentence ends."""
    out = []
    for raw in text.replace("—", " — ").split():
        if raw == "—":
            if out: out[-1]["punct"] = True
            continue
        punct = raw[-1] in ".,?!:;"
        w = raw.rstrip(".,?!:;\"”“")
        if not w: continue
        out.append(dict(w=w, punct=punct, num=bool(re.search(r"[\d$%]", w))))
    return out

NUM_WORDS = {"zero":0,"oh":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,
             "thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,
             "fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,"hundred":100,"thousand":1000,"million":10**6,"point":"."}

def align_key(w):
    """Comparable key for a script word vs an ASR word."""
    k = norm(w).strip(" .,'")
    k = k.replace("$", "").replace(",", "").replace("%", " percent").strip()
    return k

# ------------------------------------------------------------------ stage: audio
def stage_audio(a):
    OUT.mkdir(parents=True, exist_ok=True)
    meta = {}
    for name, clip in (("hook", a.hook), ("body", a.body)):
        wav = OUT / f"{name}.wav"
        run([FFMPEG, "-y", "-loglevel", "error", "-i", str(clip), "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)])
        meta[name] = probe(clip); meta[name]["clip"] = str(clip)
        print(f"{name}: {meta[name]['w']}x{meta[name]['h']} {meta[name]['dur']:.1f}s {meta[name]['fps']:.2f}fps")
    # framing check on the body take: a frame at 25%, Haar face, head% of source
    fr = OUT / "frame_body.png"
    run([FFMPEG, "-y", "-loglevel", "error", "-ss", f"{meta['body']['dur']*0.25:.2f}", "-i", str(a.body), "-frames:v", "1", str(fr)])
    im = Image.open(fr).convert("RGB"); sw, sh = im.size
    crop = dict(x=0, y=0, w=sw, h=sh); head_pct = None
    try:
        import cv2
        g = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml").detectMultiScale(g, 1.1, 5, minSize=(60, 60))
        if len(faces):
            x, y, fw, fh = max(faces, key=lambda f: f[2] * f[3])
            head_h = fh * 1.30; head_pct = head_h / sh
            cx = x + fw // 2
            print(f"face at x={x} y={y} w={fw} h={fh} → head ≈ {head_pct*100:.1f}% of source height")
            if head_pct > 0.14:
                print("  ! source framing is tighter than the 12–16% target. A 9:16 crop only magnifies; "
                      "per /rei-ad-build §3.4 we DO NOT letterbox — expect a tight medium shot.")
        else:
            cx = sw // 2; print("  ! no face found; centre column")
    except Exception as e:
        cx = sw // 2; print("  (no cv2:", e, ")")
    if sw / sh > W / H + 0.01:      # landscape → 9:16 column around the face
        cw = int(sh * W / H); x0 = min(max(cx - cw // 2, 0), sw - cw); crop = dict(x=x0, y=0, w=cw, h=sh)
    elif sw / sh < W / H - 0.01:    # taller than 9:16 → trim height, keep the top third (face sits high)
        ch = int(sw * H / W); crop = dict(x=0, y=max(0, min(int(sh * 0.12), sh - ch)), w=sw, h=ch)
    meta["crop"] = crop; meta["head_pct"] = head_pct
    (OUT / "meta.json").write_text(json.dumps(meta, indent=1))
    # proof frame
    pf = im.crop((crop["x"], crop["y"], crop["x"] + crop["w"], crop["y"] + crop["h"])).resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(pf); d.line((0, int(H*0.38), W, int(H*0.38)), fill=(255, 220, 0), width=3)
    d.rectangle((0, 0, W, int(H*0.10)), outline=(0, 120, 255), width=4); d.rectangle((0, int(H*0.83), W, H), outline=(0, 120, 255), width=4)
    pf.save(OUT / "frame_framing_check.png"); print("wrote frame_framing_check.png")

# ------------------------------------------------------------------ stage: asr + align
MODEL_URL = "https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-zipformer-en-2023-06-26.tar.bz2"
def ensure_model():
    """Fetch + unpack the speech model on first run (one ~290 MB tarball from the sherpa-onnx GitHub release)."""
    if (ASR_DIR / "tokens.txt").exists(): return
    import tarfile, urllib.request
    ASR_DIR.parent.mkdir(parents=True, exist_ok=True)
    tgz = ASR_DIR.parent / "model.tar.bz2"
    print("downloading speech model (~290 MB, once) …"); urllib.request.urlretrieve(MODEL_URL, tgz)
    with tarfile.open(tgz, "r:bz2") as t: t.extractall(ASR_DIR.parent)
    tgz.unlink(); print("model ready:", ASR_DIR)

def ensure_assets():
    """Fonts, emoji and the deck pages: run prep_assets.py if anything is missing."""
    need = not (SF.FONTS / "Anton-Regular.ttf").exists() or not (SF.ASSETS / "deck_p06.png").exists() or not (SF.EMOJI / "1f4b0.png").exists()
    if need:
        print("fetching fonts / emoji / deck pages (once) …")
        subprocess.run([sys.executable, str(HERE / "prep_assets.py")], check=True)

_rec = None
def recognizer():
    global _rec
    if _rec is None:
        ensure_model()
        import sherpa_onnx
        d = str(ASR_DIR)
        _rec = sherpa_onnx.OfflineRecognizer.from_transducer(
            encoder=f"{d}/encoder-epoch-99-avg-1.int8.onnx", decoder=f"{d}/decoder-epoch-99-avg-1.onnx",
            joiner=f"{d}/joiner-epoch-99-avg-1.int8.onnx", tokens=f"{d}/tokens.txt", num_threads=4, decoding_method="greedy_search")
    return _rec

def asr_words(wav_path, chunk=25.0):
    """Recognise in ~25s chunks on silence-ish boundaries; return [{w,s,e}] (ASR spelling)."""
    w = wave.open(str(wav_path)); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    rec = recognizer(); words = []; n = len(x); pos = 0
    while pos < n:
        end = min(n, pos + int(chunk * sr))
        if end < n:  # back off to the quietest 20ms in the last 3s
            seg = np.abs(x[end - int(3*sr):end]); k = int(np.argmin(np.convolve(seg, np.ones(int(0.02*sr))/int(0.02*sr), "same")))
            end = end - int(3*sr) + k
        s = rec.create_stream(); s.accept_waveform(sr, x[pos:end]); rec.decode_stream(s); r = s.result
        cur = None
        for tok, ts in zip(r.tokens, r.timestamps):
            t = pos / sr + ts
            if tok.startswith(" ") or cur is None:
                if cur: words.append(cur)
                cur = dict(w=tok.strip(), s=t, e=t + 0.25)
            else:
                cur["w"] += tok.strip(); cur["e"] = t + 0.12
        if cur: words.append(cur)
        pos = end
    for i in range(len(words) - 1):
        words[i]["e"] = max(words[i]["s"] + 0.08, min(words[i]["e"] + 0.10, words[i+1]["s"] - 0.02))
    return words

def align(script, asr):
    """Transfer ASR timing onto script words. Matched words take their time; unmatched
    script spans are spread across the ASR time between their matched neighbours."""
    sk = [align_key(w["w"]) for w in script]; ak = [align_key(w["w"]) for w in asr]
    # number words in ASR collapse to a single key so '$1.15M' ≈ 'one point one five million'
    sm = SequenceMatcher(None, sk, ak, autojunk=False)
    times = [None] * len(script)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                times[i1 + k] = (asr[j1 + k]["s"], asr[j1 + k]["e"])
        elif tag == "replace" and i2 > i1 and j2 > j1:
            # spread the replaced script words over the replaced ASR span (numbers land here)
            t0, t1 = asr[j1]["s"], asr[j2 - 1]["e"]; n = i2 - i1
            for k in range(n):
                a = t0 + (t1 - t0) * k / n; b = t0 + (t1 - t0) * (k + 1) / n
                times[i1 + k] = (a, max(a + 0.08, b - 0.02))
    # fill remaining gaps (deleted script words) by interpolation between neighbours
    idx = [i for i, t in enumerate(times) if t]
    if not idx: raise SystemExit("alignment found nothing — wrong take for this script?")
    for i in range(len(times)):
        if times[i]: continue
        prev = max([j for j in idx if j < i], default=None); nxt = min([j for j in idx if j > i], default=None)
        if prev is None: t0 = max(0.0, times[nxt][0] - 0.3 * (nxt - i)); t1 = times[nxt][0] - 0.05
        elif nxt is None: t0 = times[prev][1] + 0.05; t1 = t0 + 0.3
        else:
            span0, span1 = times[prev][1], times[nxt][0]; n = nxt - prev; k = i - prev
            t0 = span0 + (span1 - span0) * (k - 1) / n; t1 = span0 + (span1 - span0) * k / n
        times[i] = (t0, max(t0 + 0.08, t1 - 0.02))
    matched = sum(1 for t in sm.get_matching_blocks() for _ in range(t.size))
    out = [dict(w=sw["w"], s=round(t[0], 3), e=round(t[1], 3), punct=sw["punct"], num=sw["num"]) for sw, t in zip(script, times)]
    return out, matched / max(1, len(script))

def stage_asr(a):
    for name, text in (("hook", SCRIPT_HOOK), ("body", SCRIPT_BODY)):
        asr = asr_words(OUT / f"{name}.wav")
        (OUT / f"asr_{name}.json").write_text(json.dumps(asr, indent=0))
        words, ratio = align(script_words(text), asr)
        (OUT / f"words_{name}.json").write_text(json.dumps(words, indent=0))
        print(f"{name}: {len(asr)} words heard → {len(words)} script words timed, {ratio*100:.0f}% exact matches")
        print("   heard:", " ".join(w["w"] for w in asr[:18]).lower(), "…")

# ------------------------------------------------------------------ stage: tighten
def silences(wav):
    r = subprocess.run([FFMPEG, "-i", str(wav), "-af", f"silencedetect=noise={SILENCE_DB}dB:d={SILENCE_MIN}", "-f", "null", "-"], capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(starts, ends[:len(starts)]))

def keep_segments(words, sil, dur):
    """Speech spans padded, merged where the gap is short. Cuts snap to silences so no word is clipped."""
    speech = [(max(0, words[0]["s"] - 0.5), min(dur, words[-1]["e"] + 0.6))]
    cut = []
    for s0, s1 in sil:
        if s1 - s0 >= MAX_GAP + PAD_IN + PAD_OUT and speech[0][0] < s0 < speech[0][1]:
            cut.append((s0 + PAD_OUT, s1 - PAD_IN))
    segs = []; cur = speech[0][0]
    for c0, c1 in cut:
        if c0 - cur > 0.3: segs.append((cur, c0))
        cur = c1
    segs.append((cur, speech[0][1]))
    return segs

def remap(words, segs):
    out = []; off = 0.0; table = []
    for s0, s1 in segs:
        table.append((s0, s1, off)); off += s1 - s0
    def f(t):
        for s0, s1, o in table:
            if s0 - 0.01 <= t <= s1 + 0.01: return o + min(max(t - s0, 0), s1 - s0)
        # inside a removed gap → snap to the nearest kept edge
        best = min(table, key=lambda r: min(abs(t - r[0]), abs(t - r[1])))
        return best[2] + (0 if abs(t - best[0]) < abs(t - best[1]) else best[1] - best[0])
    for w in words:
        out.append({**w, "s": round(f(w["s"]), 3), "e": round(max(f(w["s"]) + 0.06, f(w["e"])), 3)})
    return out, off

def stage_tighten(a):
    meta = json.loads((OUT / "meta.json").read_text()); c = meta["crop"]
    total = 0.0; all_words = []; parts = []
    for name in ("hook", "body"):
        words = json.loads((OUT / f"words_{name}.json").read_text())
        segs = keep_segments(words, silences(OUT / f"{name}.wav"), meta[name]["dur"])
        kept = sum(s1 - s0 for s0, s1 in segs)
        print(f"{name}: {len(segs)} segments, {meta[name]['dur']:.1f}s → {kept:.1f}s")
        words, dur = remap(words, segs)
        # one re-encode per clip: trim+concat, crop column, 1080x1920, grade, 30fps, 48k stereo
        vf = "".join(f"[0:v]trim={s0:.3f}:{s1:.3f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={s0:.3f}:{s1:.3f},asetpts=PTS-STARTPTS[a{i}];" for i, (s0, s1) in enumerate(segs))
        vf += "".join(f"[v{i}][a{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=1[vc][ac];"
        vf += (f"[vc]crop={c['w']}:{c['h']}:{c['x']}:{c['y']},scale={W}:{H}:flags=lanczos,"
               f"eq=contrast=1.06:saturation=1.05,fps={FPS},setsar=1,format=yuv420p[vout];[ac]aresample=48000,aformat=channel_layouts=stereo[aout]")
        p = OUT / f"{name}_cut.mp4"
        run([FFMPEG, "-y", "-loglevel", "error", "-i", meta[name]["clip"], "-filter_complex", vf, "-map", "[vout]", "-map", "[aout]",
             "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-c:a", "aac", "-b:a", "256k", "-video_track_timescale", "90000", str(p)])
        dur = probe(p)["dur"]
        for w in words: w["s"] = round(w["s"] + total, 3); w["e"] = round(w["e"] + total, 3); w["clip"] = name
        all_words += words; total += dur; parts.append(p)
    # join hook + body (same params → concat filter, never -c copy)
    run([FFMPEG, "-y", "-loglevel", "error", "-i", str(parts[0]), "-i", str(parts[1]), "-filter_complex",
         "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "fast", "-crf", "16",
         "-c:a", "aac", "-b:a", "256k", "-video_track_timescale", "90000", str(OUT / "base_cut.mp4")])
    (OUT / "words.json").write_text(json.dumps(all_words, indent=0))
    print(f"base_cut.mp4 {total:.1f}s, {len(all_words)} timed words")

# ------------------------------------------------------------------ stage: plan
def find(words, phrase, after=0.0):
    """First occurrence of a phrase (script spelling, case/punct-insensitive) starting after `after` seconds."""
    want = [align_key(x) for x in phrase.split()]
    keys = [align_key(w["w"]) for w in words]
    for i in range(len(words) - len(want) + 1):
        if words[i]["s"] < after: continue
        if keys[i:i + len(want)] == want:
            return words[i]["s"], words[i + len(want) - 1]["e"], i
    print(f"  ! anchor missed: '{phrase}'"); return None

def cues(words):
    """2–3 words per cue; break at punctuation and at gaps > 0.35s; numbers stay with their unit."""
    out = []; cur = []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        gap = (nxt["s"] - w["e"]) if nxt else 9
        glue = nxt and (w["num"] and align_key(nxt["w"]) in ("psf", "million", "m", "years", "units", "a") )
        if w["punct"] or gap > 0.35 or (len(cur) >= CAP_MAX_WORDS and not glue) or nxt is None or (nxt and nxt["clip"] != w["clip"]):
            out.append(cur); cur = []
    return [c for c in out if c]

def accent(cue):
    best, bi = -99, None
    for i, w in enumerate(cue):
        s = (10 if w["num"] else 0) - (6 if align_key(w["w"]) in STOP else 0) + min(len(w["w"]), 9) * 0.5
        if s > best: best, bi = s, i
    return bi

def stage_plan(a):
    rnd = random.Random(a.seed)
    words = json.loads((OUT / "words.json").read_text())
    total = probe(OUT / "base_cut.mp4")["dur"]
    hook_end = max(w["e"] for w in words if w["clip"] == "hook")
    body = [w for w in words if w["clip"] == "body"]
    F = lambda ph, after=0.0: find(words, ph, after)

    # ---------- beats (devices + inserts), phrase-anchored
    beats = []
    def beat(kind, ph, dur=None, until=None, lead=0.0, tail=0.0, **kw):
        hit = F(ph, kw.pop("after", 0.0))
        if not hit: return
        t0 = max(0.0, hit[0] + lead)
        if until:
            h2 = F(until, hit[1]); t1 = (h2[1] if h2 else hit[1] + 2.0) + tail
        else: t1 = (hit[1] if dur is None else t0 + dur) + tail
        beats.append(dict(kind=kind, t0=round(t0, 3), t1=round(t1, 3), anchor=ph, **kw))
    # hook (the A11 grammar on real timing)
    beat("eyebrow", "my daughter", until="forward again", text="WOULD I BUY THIS FOR MY DAUGHTER?")
    beat("photo_card", "already benefited", until="forward again", tail=-1.0, photo=0)
    beat("receipt", "bought at", until="1.525M", tail=0.9)
    beat("insert", "now if thomson reserve", until="thomson reserve", tail=0.3, lead=-0.1, src="deck_p06", cx=2250, whip=True)
    beat("underline", "forward again", dur=1.6, lead=0.25)
    # body — the reduced device set of §4.0
    beat("split", "preview starts 17 october", until="17 october", lead=-0.1, tail=0.2, src="photo:2", whip=True)
    beat("split", "there are 1,268 units", until="1,268 units", lead=-0.2, tail=0.2, src="deck_p17", whip=True)
    beat("dotgrid", "1,066 of them", until="3 bedrooms", lead=-0.3, tail=0.5, src="deck_p17")
    beat("split", "your direct neighbours", until="direct neighbours", lead=-0.1, tail=0.3, src="deck_p11", whip=True)
    beat("bars", "thomson east coast mrt story", until="under 3% a year", lead=-0.4, tail=0.7, src="deck_p04",
         eyebrow="YOU'RE BUYING AFTER THE MRT STORY", k_bar1="20.86%", k_bar2="5.87%", k_pill="under 3%", whip=True)
    beat("pricegap", "$3.2 million", until="$500,000 above", lead=-0.3, tail=0.9, k_right="$3.2 million", k_left="$2.7m", k_gap="$500,000")
    beat("vs", "three reasons", dur=3.0, lead=-0.2, whip=True)
    beat("insert", "two minutes", until="sheltered", lead=-0.1, tail=0.2, src="deck_p06", cx=2250)
    beat("insert", "central catchment", until="20km of trails", lead=-0.1, tail=0.2, src="deck_p12", cx=900, whip=True)
    beat("insert", "a forever million dollar view", until="dollar view", lead=-0.2, tail=0.6, src="photo:4", anchor_x=1.0, pull=True, dip=True)
    beat("checklist", "exact price i walk away", until="own-stay", lead=-0.2, tail=0.3,
         items=["THE PRICE I WON'T CROSS", "STACKS TO PICK · TO AVOID", "PREP BEFORE BALLOT DAY", "2ND PROPERTY OR OWN-STAY"],
         ticks=["walk away at", "which stacks", "before and during", "own-stay"])
    beats.sort(key=lambda b: b["t0"])

    # ---------- breaths: caption off for 0.4s before these lines
    breaths = []
    for ph in ("what i don't like", "third the price", "click the link below"):
        h = F(ph)
        if h: breaths.append((round(max(0, h[0] - 0.45), 3), round(h[0] - 0.02, 3)))
    # the longest hold: the question on his face, caption static
    hq = F("can it move her forward")

    # ---------- caption cues; suppressed where a copy-carrying device owns the frame or in a breath
    owns = [(b["t0"], b["t1"]) for b in beats if b["kind"] in ("receipt", "pricegap")]
    cue_list = []
    for c in cues(words):
        s, e = c[0]["s"] - 0.08, c[-1]["e"] + 0.10
        if any(o0 - 0.05 < s < o1 for o0, o1 in owns): continue
        if any(b0 <= s <= b1 for b0, b1 in breaths): s = max(s, [b1 for b0, b1 in breaths if b0 <= s <= b1][0] + 0.02)
        if e - s < 0.25: continue
        cue_list.append(dict(s=round(s, 3), e=round(e, 3), words=[w["w"] for w in c], accent=accent(c),
                             num=any(w["num"] for w in c), clip=c[0]["clip"]))
    # caption arrival styles rotate; never the same twice in a row; numbers → typebox, warnings → shake
    styles = ["pop", "slide", "wordpop", "flip"]; last = None
    for i, c in enumerate(cue_list):
        if c["num"]: st = "typebox"
        elif any(align_key(w) in ("risk", "wrong", "don't", "not", "never") for w in c["words"]): st = "shake"
        else:
            opts = [s for s in styles if s != last]; st = opts[(i * 7) % len(opts)]
        c["style"] = st; last = st
    for c in cue_list:
        if c["clip"] == "hook" and c["s"] < 1.0: c["style"] = "wordpop"

    # ---------- speaker shots = cue boundaries with jitter + ladder; inserts override
    shots = []; prev_z = None; ladder_i = 0; since_break = 0
    for i, c in enumerate(cue_list):
        s = c["s"] if i == 0 else shots[-1]["t1"]
        e = c["e"] if i + 1 < len(cue_list) else total
        if i + 1 < len(cue_list): e = round((c["e"] + cue_list[i + 1]["s"]) / 2 + rnd.uniform(-0.08, 0.08), 3)
        if e <= s + 0.2: continue
        # zoom ladder, broken once per ~20s
        z = ZOOM_LADDER[ladder_i % len(ZOOM_LADDER)]; ladder_i += 1; since_break += e - s
        if since_break > 20 and prev_z is not None: z = prev_z; since_break = 0
        move = "punch" if c["num"] else "push"
        shots.append(dict(t0=round(s, 3), t1=round(e, 3), zoom=z, move=move)); prev_z = z
    if shots: shots[0]["t0"] = 0.0; shots[-1]["t1"] = round(total, 3)
    # jitter rule: no two consecutive within ±15% → move the shared boundary (two passes)
    for _pass in range(2):
      for i in range(1, len(shots)):
          d0, d1 = shots[i-1]["t1"] - shots[i-1]["t0"], shots[i]["t1"] - shots[i]["t0"]
          if abs(d1 - d0) < 0.15 * max(d0, d1) and min(d0, d1) > 0.45:
              need = 0.16 * max(d0, d1) - abs(d1 - d0)            # how much longer the longer one must get
              shift = math.ceil(need / 2 * FPS) / FPS + 1 / FPS   # move the boundary by that much (both shots change)
              if d0 >= d1: shots[i-1]["t1"] = round(shots[i-1]["t1"] + shift, 3)
              else:        shots[i-1]["t1"] = round(shots[i-1]["t1"] - shift, 3)
              shots[i]["t0"] = shots[i-1]["t1"]
    # the hold: one shot across the question, zoom 1.00, no ladder
    if hq:
        q0, q1 = hq[0] - 0.1, hook_end + 0.3
        shots = [s for s in shots if s["t1"] <= q0 or s["t0"] >= q1] + [dict(t0=round(q0, 3), t1=round(q1, 3), zoom=1.0, move="push", hold=True)]
        shots.sort(key=lambda s: s["t0"])
        for i in range(1, len(shots)): shots[i]["t0"] = shots[i-1]["t1"] if shots[i]["t0"] < shots[i-1]["t1"] else shots[i]["t0"]
    # transitions
    seams = [hook_end] + [F(p)[0] for p in ("what i don't like", "what i like about", "thomson reserve preview is on") if F(p)]
    plan = dict(total=total, hook_end=hook_end, shots=shots, cues=cue_list, beats=beats, breaths=breaths, seams=seams, seed=a.seed)
    (OUT / "plan.json").write_text(json.dumps(plan, indent=1))
    human_pass(plan)

def human_pass(plan):
    sh = plan["shots"]; d = [s["t1"] - s["t0"] for s in sh]
    cuts = len(sh) + len([b for b in plan["beats"] if b["kind"] in ("insert", "split", "vs", "dotgrid", "bars")]) * 2
    print(f"\n== HUMAN-PASS REPORT ==\n{len(sh)} speaker shots, {len(plan['beats'])} beats, {len(plan['cues'])} caption cues over {plan['total']:.1f}s → ≈{cuts / plan['total'] * 60:.0f} cuts/min")
    hist = {}
    for x in d: hist[round(x * 2) / 2] = hist.get(round(x * 2) / 2, 0) + 1
    print("shot-length histogram (s):", " ".join(f"{k:.1f}:{'#'*v}" for k, v in sorted(hist.items())))
    viol = [(sh[i-1]["t0"], round(d[i-1], 2), round(d[i], 2)) for i in range(1, len(d)) if abs(d[i] - d[i-1]) < 0.15 * max(d[i], d[i-1])]
    print(f"consecutive shots within ±15%: {len(viol)}", viol[:6])
    print("breaths:", plan["breaths"]); print("longest hold:", max(d), "s")

# ------------------------------------------------------------------ stage: render
def read_frames(path):
    p = subprocess.Popen([FFMPEG, "-loglevel", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE, bufsize=W*H*3*4)
    n = W * H * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n: break
        yield Image.frombuffer("RGB", (W, H), b, "raw", "RGB", 0, 1)
    p.stdout.close(); p.wait()

def src_image(src, cx=None, darken=0.0, zoom=1.0, anchor_x=0.5):
    if src.startswith("photo:"):
        return SF.photo_full(int(src.split(":")[1]), darken=darken, zoom=zoom, anchor_x=anchor_x, anchor_y=0.35)
    return SF.broll(src, cx=cx, darken=darken, zoom=zoom)

class CaptionCache:
    def __init__(self): self.c = {}
    def layer(self, cue, t, y=0.70):
        k = (id(cue), min(8, int((t - cue["s"]) * FPS)), y)
        if k not in self.c:
            tt = min(1, (t - cue["s"]) / (8 / FPS))
            L = SF.new_layer()
            emo = None
            SF.caption_anim(L, cue["words"], cue["accent"], cue["style"], tt, emo=emo, y_frac=y, size=88)
            self.c[k] = L
            if len(self.c) > 60: self.c.pop(next(iter(self.c)))
        return self.c[k]

def stage_render(a):
    plan = json.loads((OUT / "plan.json").read_text()); meta = json.loads((OUT / "meta.json").read_text())
    total = plan["total"]; n_frames = int(round(total * FPS)); end_frames = 3 * FPS
    shots, cues, beats = plan["shots"], plan["cues"], plan["beats"]
    cc = CaptionCache()
    enc = subprocess.Popen([FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-video_track_timescale", "90000",
                            str(OUT / "video_only.mp4")], stdin=subprocess.PIPE)
    whip_at = []  # (time, direction)
    for b in beats:
        if b.get("whip"): whip_at += [b["t0"], b["t1"]]
    for s in plan["seams"]: whip_at.append(s)
    whip_at = sorted(set(round(x, 3) for x in whip_at))
    # never two whips within 6s → the later one becomes a plain cut
    kept = []
    for x in whip_at:
        if not kept or x - kept[-1] > 6.0: kept.append(x)
    whip_at = kept
    flashes = [plan["seams"][0]] + [b["t0"] for b in beats if b["kind"] == "insert" and b.get("dip")]
    print(f"rendering {n_frames + end_frames} frames …")
    src = read_frames(OUT / "base_cut.mp4")
    last_frame = None
    for i in range(n_frames):
        t = i / FPS
        try: frame = next(src); last_frame = frame
        except StopIteration: frame = last_frame
        shot = next((s for s in shots if s["t0"] <= t < s["t1"]), shots[-1])
        # ---- picture
        active = [b for b in beats if b["t0"] <= t < b["t1"]]
        full = next((b for b in active if b["kind"] in ("insert", "dotgrid", "bars", "vs")), None)
        split = next((b for b in active if b["kind"] == "split"), None)
        hx, hy = SF.handheld(t)
        if full:
            k = (t - full["t0"]) / max(0.1, full["t1"] - full["t0"])
            z = (1.08 - 0.06 * k) if full.get("pull") else (1.0 + 0.06 * k)
            dark = {"dotgrid": 0.78, "bars": 0.62, "vs": 0.0}.get(full["kind"], 0.0)
            if full["kind"] == "vs":
                L = SF.ImageEnhance.Color(SF.broll("deck_p17", darken=0.55, zoom=1.08)).enhance(0.35); R = SF.broll("deck_p16", darken=0.35, zoom=1.04)
                seam = 1.25 - 0.75 * SF.ease_in_out(min(1, k * 1.6))
                base = SF.dev_vs_split(L, R, seam=seam, left_items=("84% ONE UNIT TYPE", "AFTER THE MRT STORY", "$500K ABOVE DISTRICT"),
                                       right_items=("MRT · 2-MIN WALK", "AI TONG < 1KM", "A FOREVER VIEW"), t=max(0, (k - 0.3) / 0.6))
            else:
                base = src_image(full["src"], cx=full.get("cx"), darken=dark, zoom=z, anchor_x=full.get("anchor_x", 0.5))
        else:
            # speaker: zoom ladder + move, handheld
            k = (t - shot["t0"]) / max(0.1, shot["t1"] - shot["t0"])
            z = shot["zoom"] + (0.05 * k if shot["move"] == "push" else 0.13 * SF.ease_out(min(1, k * 3), 4))
            base = SF.zoom_img(frame, z, hx, hy)
            if split:
                top = src_image(split["src"], cx=split.get("cx"), zoom=1.04 + 0.03 * (t - split["t0"]) / max(0.1, split["t1"] - split["t0"]))
                seam_y = int(H * 0.52)
                shifted = base.transform((W, H), Image.AFFINE, (1, 0, 0, 0, 1, -int(H * 0.16)), Image.BICUBIC)
                base = Image.composite(top, shifted, SF.tear_mask(seam_y))
        layer = SF.new_layer()
        if split: SF.torn_edge(layer, int(H * 0.52))
        # ---- devices
        for b in active:
            k = (t - b["t0"]) / max(0.1, b["t1"] - b["t0"])
            if b["kind"] == "eyebrow": SF.eyebrow(layer, b["text"], slide=SF.ease_out(min(1, (t - b["t0"]) / 0.3)))
            elif b["kind"] == "photo_card": SF.dev_photo_card(layer, min(1, (t - b["t0"]) / 0.4), photo=(SF.PHOTOS[b["photo"]] if SF.PHOTOS else None))
            elif b["kind"] == "receipt": SF.dev_receipt(layer, min(1, (t - b["t0"]) / max(1.5, (b["t1"] - b["t0"]) * 0.8)))
            elif b["kind"] == "underline":
                f = SF.ANTON(88); tw = SF.text_w(f, "FORWARD")
                SF.scribble_underline(layer, W // 2 - tw // 2 - 10, W // 2 + tw // 2 + 10, int(H * 0.70) + 64, min(1, (t - b["t0"]) / 0.35))
            elif b["kind"] == "dotgrid":
                SF.dev_dotgrid(layer, min(1, k * 1.4))
                if k > 0.7: SF.card_number(layer, (W // 2, int(H * 0.675)), "84%", SF.ANTON(max(8, int(220 * SF.overshoot(min(1, (k - 0.7) / 0.15))))), fill=ORANGE, anchor="mm")
            elif b["kind"] == "bars":
                SF.eyebrow(layer, b["eyebrow"], y_frac=0.13, size=38, bg=INK, fg=GOLD)
                w1 = find_t(plan, b["k_bar1"], b["t0"]); w2 = find_t(plan, b["k_bar2"], b["t0"]); wp = find_t(plan, b["k_pill"], b["t0"])
                tt = 0.0 if t < w1 else (0.5 * min(1, (t - w1) / 0.8) if t < w2 else 0.5 + 0.45 * min(1, (t - w2) / 0.8) + (0.05 if t >= wp else 0))
                SF.dev_bars(layer, tt, y_top=0.19)
            elif b["kind"] == "pricegap":
                wr = find_t(plan, b["k_right"], b["t0"]); wl = find_t(plan, b["k_left"], b["t0"]); wg = find_t(plan, b["k_gap"], b["t0"])
                # right (TR) bar first in the script, then proven, then the gap
                tt = min(0.39, (t - b["t0"]) / 1.0 * 0.39)
                if t >= wl: tt = 0.4 + 0.5 * min(1, (t - wl) / 0.8)
                if t >= wg: tt = 0.95 + 0.05 * min(1, (t - wg) / 0.3)
                SF.dev_pricegap(layer, tt, y_top=0.50)
            elif b["kind"] == "checklist":
                ticks = [find_t(plan, p, b["t0"]) for p in b["ticks"]]
                done = sum(1 for x in ticks if t >= x + 0.4)
                SF.dev_checklist(layer, min(1, 0.25 + 0.25 * done + 0.2 * min(1, (t - b["t0"]) / 0.5)), y_top=0.46)
        # ---- captions
        if not full or full["kind"] in ("bars", "dotgrid", "vs"):
            cue = next((c for c in cues if c["s"] <= t < c["e"]), None)
            if cue and not (full and full["kind"] == "dotgrid" and t < full["t0"] + 1.2):
                y = 0.80 if (full and full["kind"] == "dotgrid") else (0.74 if split else 0.70)
                layer.alpha_composite(cc.layer(cue, t, y))
        out = SF.compose(base, layer)
        # ---- transitions
        for wt in whip_at:
            if abs(t - wt) < 0.12:
                out = SF.whip_blur(out, int(60 + 120 * (1 - abs(t - wt) / 0.12)))
        for ft in flashes:
            if 0 <= t - ft < 0.12: out = SF.flash(out, 0.8 * (1 - (t - ft) / 0.12))
        if t > total - 0.35: out = SF.flash(SF.whip_blur(out, int(40 + 160 * (t - (total - 0.35)) / 0.35)), (t - (total - 0.35)) / 0.35)
        enc.stdin.write(out.tobytes())
        if i % 300 == 0: print(f"  {t:6.1f}s / {total:.1f}s")
    for j in range(end_frames):
        enc.stdin.write(SF.dev_endcard(j / (end_frames - 1)).tobytes())
    enc.stdin.close(); enc.wait()
    # ---- audio: base_cut audio + 3s silence, loudnorm, mux
    run([FFMPEG, "-y", "-loglevel", "error", "-i", str(OUT / "video_only.mp4"), "-i", str(OUT / "base_cut.mp4"),
         "-filter_complex", f"[1:a]apad=pad_dur=3,atrim=0:{total + 3:.3f},afade=t=out:st={total - 0.3:.3f}:d=0.3,loudnorm=I=-16:TP=-1.5:LRA=11[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-shortest", str(OUT / "TR_V1_Receipt_9x16.mp4")])
    print("wrote", OUT / "TR_V1_Receipt_9x16.mp4")

def find_t(plan, phrase, after=0.0):
    words = json.loads((OUT / "words.json").read_text())
    h = find(words, phrase, after - 1.0)
    return h[0] if h else after

# ------------------------------------------------------------------ stage: qc
def stage_qc(a):
    final = OUT / "TR_V1_Receipt_9x16.mp4"; q = OUT / "qc"; q.mkdir(exist_ok=True)
    run([FFMPEG, "-y", "-loglevel", "error", "-i", str(final), "-vf", "fps=1,scale=270:-2,tile=8x8", "-frames:v", "1", str(q / "contact_sheet.jpg")])
    r = subprocess.run([FFMPEG, "-i", str(final), "-vf", "select='gt(scene,0.24)',metadata=print", "-an", "-f", "null", "-"], capture_output=True, text=True)
    cuts = len(re.findall(r"pts_time", r.stderr)); dur = probe(final)["dur"]
    print(f"QC: {dur:.1f}s, {cuts} scene changes detected → {cuts / dur * 60:.0f}/min (speaker jump-cuts under the threshold are not counted)")
    print("contact sheet:", q / "contact_sheet.jpg")


# ------------------------------------------------------------------ folder mode: pick the takes by listening to them
SCRIPT_BODY2_HEAD = ("Thomson Reserve showflat preview is on 17 October. And because I'm looking at this as a potential next "
                     "property for my own daughter I'm running a live 60-minute webinar before the preview. The exit.")

def head_ratio(clip, text, secs=45):
    """How well the first `secs` of a take match the start of a script (0..1)."""
    wav = OUT / ("probe_" + re.sub(r"[^A-Za-z0-9]+", "_", Path(clip).stem) + ".wav")
    run([FFMPEG, "-y", "-loglevel", "error", "-t", str(secs), "-i", str(clip), "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)])
    heard = asr_words(wav)
    if not heard: return 0.0, ""
    sk = [align_key(w["w"]) for w in script_words(text)][:len(heard) + 10]
    ak = [align_key(w["w"]) for w in heard]
    sm = SequenceMatcher(None, sk, ak, autojunk=False)
    m = sum(b.size for b in sm.get_matching_blocks())
    return m / max(1, len(ak)), " ".join(w["w"] for w in heard[:12]).lower()

def pick_takes(folder):
    """Every video in the folder is listened to; the best match for the hook script and for the
    Body 1 script wins. Ties go to the larger picture (the DSLR take over the phone)."""
    vids = sorted([p for p in Path(folder).iterdir() if p.suffix.lower() in (".mp4", ".mov", ".m4v")])
    if not vids: raise SystemExit(f"no videos in {folder}")
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for v in vids:
        try: m = probe(v)
        except Exception: continue
        if not m["w"] or m["dur"] < 5: continue
        rh, heard = head_ratio(v, SCRIPT_HOOK, 30)
        rb, _ = head_ratio(v, SCRIPT_BODY, 45)
        r2, _ = head_ratio(v, SCRIPT_BODY2_HEAD, 30)
        rows.append(dict(path=str(v), w=m["w"], h=m["h"], dur=m["dur"], hook=rh, body=rb, body2=r2, heard=heard))
        print(f"  {v.name[:40]:40s} {m['w']}x{m['h']} {m['dur']:6.1f}s  hook {rh:.2f}  body1 {rb:.2f}  body2 {r2:.2f}  | {heard[:60]}")
    (OUT / "takes.json").write_text(json.dumps(rows, indent=1))
    def best(key, min_dur, other):
        c = [r for r in rows if r["dur"] >= min_dur and r[key] >= 0.35 and r[key] > r[other]]
        if not c: raise SystemExit(f"no take matches the {key} script well enough (best {max(r[key] for r in rows):.2f}) — is the right folder selected?")
        return max(c, key=lambda r: (round(r[key], 1), r["w"] * r["h"], r["dur"]))
    hook = best("hook", 5, "body"); body = best("body", 15, "body2")
    print(f"→ hook: {Path(hook['path']).name}  ({hook['w']}x{hook['h']}, match {hook['hook']:.2f})")
    print(f"→ body: {Path(body['path']).name}  ({body['w']}x{body['h']}, match {body['body']:.2f})")
    return hook["path"], body["path"]

# ------------------------------------------------------------------ main
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--hook", required=False); ap.add_argument("--body", required=False)
    ap.add_argument("--photos"); ap.add_argument("--stage", default="all"); ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out"); ap.add_argument("--folder", help="the takes folder; the hook and body takes are picked by listening to them")
    a = ap.parse_args()
    if a.folder:
        OUT = Path(a.folder) / "_render_v1"
    if a.out: OUT = Path(a.out)
    import shutil
    if not a.photos:
        for cand in (r"C:\Users\Admin\Pictures\Family & Daughter", str(HERE.parent / "photos")):
            if Path(cand).is_dir(): a.photos = cand; break
    if a.photos: SF.load_photos(a.photos)
    ensure_assets(); ensure_model()
    stages = ["audio", "asr", "tighten", "plan", "render", "qc"] if a.stage == "all" else a.stage.split(",")
    if a.folder and not (a.hook and a.body):
        print("\n== PICK TAKES =="); a.hook, a.body = pick_takes(a.folder)
    for s in stages:
        print(f"\n== {s.upper()} =="); globals()[f"stage_{s}"](a)
    if a.folder and (OUT / "TR_V1_Receipt_9x16.mp4").exists() and ("render" in stages or "qc" in stages):
        dest = Path(a.folder) / "TR_V1_Receipt_9x16.mp4"; shutil.copy(OUT / "TR_V1_Receipt_9x16.mp4", dest)
        shutil.copy(OUT / "qc" / "contact_sheet.jpg", Path(a.folder) / "TR_V1_contact_sheet.jpg")
        print("\nFINAL →", dest)
