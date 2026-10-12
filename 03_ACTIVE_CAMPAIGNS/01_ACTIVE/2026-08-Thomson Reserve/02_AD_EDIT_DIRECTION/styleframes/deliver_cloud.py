"""Delivery copies of the cloud-rendered ads (each under the 15 MB artifact file limit) + the review page.
    python deliver_cloud.py <RENDERS dir> <out dir> [EXIT|BALLOT] [sister page url]
One artifact holds at most 256 MB, so the set is split in two pages: the full ad + the Exit-body ads, and the Ballot-body ads.
"""
import sys, json, re, subprocess, html
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import render_v1 as RV, tr_scripts as TS, looks as LK

MAX_MB = 13.5
renders, out = Path(sys.argv[1]), Path(sys.argv[2]); ads = out / "ads"; ads.mkdir(parents=True, exist_ok=True)
GROUP = sys.argv[3] if len(sys.argv) > 3 else None; SISTER = sys.argv[4] if len(sys.argv) > 4 else None
report = {r["id"]: r for r in json.loads((renders / "batch_report.json").read_text())} if (renders / "batch_report.json").exists() else {}

def headline(jid):
    if jid == "TR_FULL_DH1": return "WOULD I BUY THIS FOR MY DAUGHTER?", "Daughter Hook 1-New", "Body 1 (full)"
    m = re.match(r"TR_H(\d+)_(EXIT|BALLOT)", jid); k = int(m.group(1))
    return TS.HOOKS[k][0], f"Hook {k}", {"EXIT": "Body: The Exit", "BALLOT": "Body: Ballot Day"}[m.group(2)]

rows = []
for src in sorted(renders.glob("TR_*_1080x1920.mp4")):
    jid = src.name.replace("_1080x1920.mp4", ""); dest = ads / f"{jid}.mp4"; poster = ads / f"{jid}.jpg"
    dur = RV.probe(src)["dur"]
    if not dest.exists() or dest.stat().st_size < 1000:
        vb = int(min(1400, MAX_MB * 8 * 1024 * 1024 / dur / 1000 - 96 - 40))
        RV.run([RV.FFMPEG, "-y", "-loglevel", "error", "-i", str(src), "-c:v", "libx264", "-preset", "medium", "-b:v", f"{vb}k", "-maxrate", f"{vb}k",
                "-bufsize", f"{2*vb}k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(dest)])
        RV.run([RV.FFMPEG, "-y", "-loglevel", "error", "-ss", "1.0", "-i", str(src), "-frames:v", "1", "-vf", "scale=360:-2", "-q:v", "5", str(poster)])
    h, hook, body = headline(jid); look = LK.LOOKS.get(jid)
    rows.append(dict(id=jid, headline=h, hook=hook, body=body, dur=round(dur, 1), mb=round(dest.stat().st_size / 1e6, 1),
                     look=LK.recipe(look) if look else "the approved base look (as the one-file ad)",
                     note=report.get(jid, {}).get("note", ""), group="FULL" if "FULL" in jid else jid.split("_")[-1]))
    print(jid, f"{dur:.0f}s", f"{rows[-1]['mb']} MB")
(out / "ads.json").write_text(json.dumps(rows, indent=1))
if GROUP: rows = [r for r in rows if r["group"] == GROUP or (GROUP == "EXIT" and r["group"] == "FULL")]

cards = []
for r in rows:
    flag = ' <span class="flag">check the words</span>' if "CHECK" in r["note"] else ""
    cards.append(f'''<article class="card" data-group="{r["group"]}">
  <video controls preload="none" playsinline poster="ads/{r["id"]}.jpg" src="ads/{r["id"]}.mp4"></video>
  <div class="meta">
    <div class="idline"><span class="id">{r["id"]}</span><span class="dur">{r["dur"]:.0f} s · {r["mb"]} MB</span></div>
    <h3>{html.escape(r["headline"])}</h3>
    <p class="combo">{html.escape(r["hook"])} + {html.escape(r["body"])}{flag}</p>
    <p class="look">{html.escape(r["look"])}</p>
  </div>
</article>''')
n = len(rows); nE = sum(r["group"] == "EXIT" for r in rows); nB = sum(r["group"] == "BALLOT" for r in rows); nF = n - nE - nB
title = "Daughter Spin Off Ads" if not GROUP else ("Daughter Spin Off Ads · Exit" if GROUP == "EXIT" else "Daughter Spin Off Ads · Ballot")
sub = (f"{n} ads from the Longer Ads takes: {nF} full ad, {nE} hook × Exit, {nB} hook × Ballot." if not GROUP else
       (f"The full Daughter Hook 1 ad and the {nE} Exit-body ads (Hooks 1 to 15 + Body: The Exit)." if GROUP == "EXIT" else
        f"The {nB} Ballot-body ads (Hooks 1 to 15 + Body: Ballot Day)."))
sister = (f' <a href="{SISTER}">The {"Ballot" if GROUP == "EXIT" else "Exit"} set is on its own page.</a>' if SISTER else "")
bar = ("" if GROUP else f"""<div class="bar" role="group" aria-label="Filter by body">
  <button type="button" data-f="ALL" aria-pressed="true">All {n}</button>
  <button type="button" data-f="FULL" aria-pressed="false">Full ad</button>
  <button type="button" data-f="EXIT" aria-pressed="false">Exit body ({nE})</button>
  <button type="button" data-f="BALLOT" aria-pressed="false">Ballot body ({nB})</button>
</div>""")
page = f'''<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;900&family=IBM+Plex+Sans:wght@400;500&display=swap">
<style>
/* layout: one sticky filter bar, then a responsive grid of phone-shaped players; dark-first like the ads themselves */
:root {{ --bg:#101014; --panel:#1a1a21; --line:#2c2c36; --fg:#f2f1ec; --muted:#a3a2ac; --acc:#ffd400; --warn:#ff7a59;
        --display:'Archivo', 'Arial Narrow', Arial, sans-serif; --body:'IBM Plex Sans', system-ui, sans-serif; color-scheme:dark }}
@media (prefers-color-scheme: light) {{ :root:not([data-theme="dark"]) {{ --bg:#f5f4ef; --panel:#ffffff; --line:#dcdad2; --fg:#15151a; --muted:#5d5c66; --acc:#b08900; --warn:#c0431f; color-scheme:light }} }}
:root[data-theme="light"] {{ --bg:#f5f4ef; --panel:#ffffff; --line:#dcdad2; --fg:#15151a; --muted:#5d5c66; --acc:#b08900; --warn:#c0431f; color-scheme:light }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--body); padding-inline:16px; padding-block:0 48px; }}
header {{ max-width:1200px; margin:0 auto; padding-block:28px 12px; }}
h1 {{ font-family:var(--display); font-weight:900; font-size:clamp(28px,5vw,44px); letter-spacing:-0.02em; margin:0 0 6px; text-wrap:balance }}
.sub {{ color:var(--muted); margin:0; max-width:70ch; line-height:1.5 }}
.sub a {{ color:var(--acc); font-weight:500 }}
.bar {{ position:sticky; top:env(safe-area-inset-top,0px); background:var(--bg); z-index:2; max-width:1200px; margin:0 auto; padding-block:12px; display:flex; gap:8px; flex-wrap:wrap; border-bottom:1px solid var(--line) }}
.bar button {{ font:inherit; font-weight:500; background:var(--panel); color:var(--fg); border:1px solid var(--line); border-radius:999px; padding:8px 16px; cursor:pointer }}
.bar button[aria-pressed="true"] {{ background:var(--acc); color:#111; border-color:var(--acc) }}
.bar button:focus-visible {{ outline:2px solid var(--acc); outline-offset:2px }}
.grid {{ max-width:1200px; margin:20px auto 0; display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:20px }}
.card {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; overflow:hidden; display:flex; flex-direction:column; min-width:0 }}
.card[hidden] {{ display:none }}
video {{ width:100%; aspect-ratio:9/16; background:#000; display:block; max-width:100% }}
.meta {{ padding:12px 14px 16px; display:flex; flex-direction:column; gap:6px }}
.idline {{ display:flex; justify-content:space-between; gap:8px; font-size:12px; color:var(--muted); font-variant-numeric:tabular-nums }}
.id {{ font-family:var(--display); font-weight:700; letter-spacing:0.04em; color:var(--acc) }}
h3 {{ font-family:var(--display); font-weight:700; font-size:17px; line-height:1.2; margin:0; text-wrap:balance }}
.combo {{ margin:0; font-size:13px; color:var(--fg) }}
.look {{ margin:0; font-size:12px; color:var(--muted); line-height:1.45 }}
.flag {{ display:inline-block; margin-left:6px; padding:1px 8px; border-radius:999px; background:var(--warn); color:#fff; font-size:11px; font-weight:500 }}
.note {{ max-width:1200px; margin:16px auto 0; padding:12px 16px; border:1px solid var(--line); border-radius:10px; color:var(--muted); font-size:13px; line-height:1.5 }}
@media (prefers-reduced-motion: no-preference) {{ .bar button {{ transition:background .15s }} }}
</style>
<header>
  <h1>Thomson Reserve × “Would I buy it for my daughter?”</h1>
  <p class="sub">{sub} Every ad has its own colours, caption style, scene and cut, with the timing border running the whole way round. Tap a card to play; each one is 1080×1920 at 1.15× speed.{sister}</p>
</header>
{bar}
<section class="grid">
{chr(10).join(cards)}
</section>
<p class="note">These were rendered in the cloud from the 540p review copies of the takes, so the talking head is softer than the originals; captions, cards, scenes and the end card are full resolution. Running RUN_ALL.bat on the PC later rebuilds the same ads from the full-size takes into Webinar Daughter Spin Off\\RENDERS.</p>
<script>
const btns = document.querySelectorAll('.bar button'), cards = document.querySelectorAll('.card');
function apply(f) {{ btns.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.f === f))); cards.forEach(c => {{ c.hidden = !(f === 'ALL' || c.dataset.group === f); }}); try {{ localStorage.setItem('tr_filter', f) }} catch (e) {{}} }}
btns.forEach(b => b.addEventListener('click', () => apply(b.dataset.f)));
let f = 'ALL'; try {{ f = localStorage.getItem('tr_filter') || 'ALL' }} catch (e) {{}} apply(f);
document.querySelectorAll('video').forEach(v => v.addEventListener('play', () => document.querySelectorAll('video').forEach(o => {{ if (o !== v) o.pause() }})));
</script>
'''
name = {"EXIT": "index.html", "BALLOT": "ballot.html", None: "index.html"}[GROUP]
(out / name).write_text(page, encoding="utf-8")
print("page:", out / name, "ads:", n, "total MB:", round(sum(r["mb"] for r in rows), 1))
print("FILES", json.dumps({f"ads/{r['id']}.{e}": f"ads/{r['id']}.{e}" for r in rows for e in ("mp4", "jpg")}))
