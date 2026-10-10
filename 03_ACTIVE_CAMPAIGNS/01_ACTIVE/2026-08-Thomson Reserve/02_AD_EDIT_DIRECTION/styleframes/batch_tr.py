"""Every Longer-Ads variation from the 'Daughter New Spinoff Ads' doc, rendered in one run.

    python batch_tr.py --folder "<takes folder>"            all 31 ads (skips the ones already rendered)
    python batch_tr.py --folder ... --only H03,H07_EXIT     a few, by id fragment
    python batch_tr.py --folder ... --force                 re-render even if the ad exists

The jobs:  TR_FULL_DH1            Daughter Hook 1-New on its own (hook + Body 1 in one take)
           TR_H01_EXIT … H15_EXIT   each hook from the Hook 1-5 / 6-10 / 11-15 takes + Body-Exit-Short
           TR_H01_BALLOT … H15_BALLOT                           … + Body-Ballot-Short
Finished ads, a contact sheet and a small preview per ad go to  <folder>\\Longer Ads\\RENDERS\\ ;
small split copies of every take go to  <folder>\\Longer Ads\\_cloud\\  so the cut can be checked from the cloud session.
Work files stay on the local disk (LOCALAPPDATA\\TR_render_v1\\<job id>)."""
import sys, os, re, json, time, shutil, argparse, tempfile, traceback
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import styleframes as SF, render_v1 as RV, tr_scripts as TS, looks as LK

SPEED = 1.15            # approved on the one-file ad
SMALL_MB, SMALL_SECS = 5.0, 60.0

def jobs():
    out = [dict(id="TR_FULL_DH1", hook="DH1", body="FULL", hook_take="DH1_NEW", body_take="DH1_NEW",
                headline="WOULD I BUY THIS FOR MY DAUGHTER?", hook_text=TS.DAUGHTER_HOOK_1, body_text=TS.BODIES["FULL"])]
    for k in sorted(TS.HOOKS):
        for b in ("EXIT", "BALLOT"):
            out.append(dict(id=f"TR_H{k:02d}_{b}", hook=k, body=b, hook_take=TS.hook_take(k), body_take=b,
                            headline=TS.HOOKS[k][0], hook_text=TS.HOOKS[k][1], body_text=TS.BODIES[b]))
    return out

def _key(s): return re.sub(r"[^a-z0-9]+", "", s.lower())

def locate(folder):
    """Each take id in tr_scripts.TAKES → the video whose file name carries that fragment."""
    vids = RV.find_videos(folder); found = {}
    for tid, frag in TS.TAKES.items():
        hits = [v for v in vids if _key(v.stem) == _key(frag)] or [v for v in vids if _key(frag) in _key(v.stem)]
        if not hits: continue
        if len(hits) > 1: print(f"  ! {len(hits)} videos match '{frag}' — using {hits[0].relative_to(folder)}; others: " + ", ".join(str(h.relative_to(folder)) for h in hits[1:]))
        found[tid] = hits[0]
    return found

def small_copies(takes, cloud):
    """Every take as 540p parts of ≤ SMALL_SECS seconds and ≤ SMALL_MB MB, readable through the Drive connector."""
    cloud.mkdir(parents=True, exist_ok=True)
    for tid, clip in sorted(takes.items()):
        dur = RV.probe(clip)["dur"]; n = max(1, int(-(-dur // SMALL_SECS)))
        part_len = dur / n; vb = max(100, int(SMALL_MB * 8 * 1024 * 1024 / max(1.0, part_len) / 1000) - 48)
        orient = RV.orient_filter(clip); orient = orient + "," if orient else ""
        for i in range(n):
            dest = cloud / (re.sub(r"[^A-Za-z0-9]+", "_", clip.stem).strip("_") + (f"_part{i+1:02d}of{n:02d}" if n > 1 else "") + "_small.mp4")
            if dest.exists() and dest.stat().st_size > 1000: continue
            RV.run([RV.FFMPEG, "-y", "-loglevel", "error", "-noautorotate", "-ss", f"{i*part_len:.2f}", "-t", f"{part_len:.2f}", "-i", str(clip),
                    "-vf", f"{orient}scale=540:-2", "-c:v", "libx264", "-preset", "fast", "-b:v", f"{vb}k", "-maxrate", f"{vb}k", "-bufsize", f"{2*vb}k",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "48k", "-ac", "1", "-movflags", "+faststart", str(dest)])
            print(f"  cloud copy → {dest.name} ({dest.stat().st_size/1e6:.1f} MB)")

def preview(src, dest):
    dur = RV.probe(src)["dur"]; vb = max(100, int(SMALL_MB * 8 * 1024 * 1024 / max(1.0, dur) / 1000) - 48)
    RV.run([RV.FFMPEG, "-y", "-loglevel", "error", "-i", str(src), "-vf", "scale=540:-2", "-c:v", "libx264", "-preset", "fast",
            "-b:v", f"{vb}k", "-maxrate", f"{vb}k", "-bufsize", f"{2*vb}k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "48k", "-ac", "1",
            "-movflags", "+faststart", str(dest)])

def render_job(j, takes, work, renders, photos, seed=7):
    RV.SINGLE = True; RV.PREFIX = j["id"]; RV.HOOK_ID = j["hook"]; RV.BODY_ID = j["body"]; RV.HOOK_HEADLINE = j["headline"]
    RV.SCRIPT_HOOK = j["hook_text"]; RV.SCRIPT_BODY = j["body_text"]; RV.ALIGN.clear()
    RV.LOOK = LK.LOOKS.get(j["id"]); print("look:", LK.recipe(RV.LOOK) if RV.LOOK else "(base)")
    RV.OUT = work / j["id"]; RV.OUT.mkdir(parents=True, exist_ok=True)
    a = argparse.Namespace(hook=str(takes[j["hook_take"]]), body=str(takes[j["body_take"]]), seed=seed, photos=photos, drop=None, speed=SPEED, stage="all")
    for st in ("audio", "asr", "tighten", "plan", "render", "qc"):
        print(f"\n== {j['id']} · {st.upper()} =="); getattr(RV, f"stage_{st}")(a)
    final = renders / f"{j['id']}_1080x1920.mp4"
    shutil.copy(RV.OUT / "TR_V1_Receipt_9x16.mp4", final)
    shutil.copy(RV.OUT / "qc" / "contact_sheet.jpg", renders / f"{j['id']}_contact_sheet.jpg")
    preview(final, renders / f"{j['id']}_preview_small.mp4")
    return final, dict(RV.ALIGN)

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True, help="the takes folder (searched with its subfolders)")
    ap.add_argument("--only", help="comma-separated id fragments, e.g. FULL,H03,H07_EXIT")
    ap.add_argument("--force", action="store_true", help="re-render ads that already exist")
    ap.add_argument("--photos"); ap.add_argument("--work"); ap.add_argument("--no-cloud", action="store_true")
    a = ap.parse_args(argv)
    folder = Path(a.folder)
    renders = folder / "Longer Ads" / "RENDERS" if (folder / "Longer Ads").is_dir() else folder / "RENDERS"
    renders.mkdir(parents=True, exist_ok=True)
    RV.start_log(renders / "batch_log.txt")
    work = Path(a.work) if a.work else Path(os.environ.get("LOCALAPPDATA") or tempfile.gettempdir()) / "TR_render_v1"
    work.mkdir(parents=True, exist_ok=True); RV.OUT = work; print("work folder:", work)
    if not a.photos:
        for cand in (r"C:\Users\Admin\Pictures\Family & Daughter", str(HERE.parent / "photos")):
            if Path(cand).is_dir(): a.photos = cand; break
    if a.photos: SF.load_photos(a.photos)
    RV.ensure_assets(); RV.ensure_model()
    takes = locate(folder)
    print("\n== TAKES ==")
    for tid, frag in TS.TAKES.items():
        print(f"  {tid:12s} {frag:28s} → {takes[tid].relative_to(folder) if tid in takes else '(not found)'}")
    if not a.no_cloud: print("\n== CLOUD COPIES =="); small_copies({k: v for k, v in takes.items() if k != "SELFIE_DH1"}, renders.parent / "_cloud")
    wanted = jobs()
    if a.only:
        frags = [f.strip().upper() for f in a.only.split(",") if f.strip()]
        wanted = [j for j in wanted if any(f in j["id"] for f in frags)]
    report = []; t_batch = time.time()
    for n, j in enumerate(wanted, 1):
        final = renders / f"{j['id']}_1080x1920.mp4"; t0 = time.time()
        print(f"\n#################### {n}/{len(wanted)}  {j['id']}  ({j['headline']})")
        missing = [t for t in (j["hook_take"], j["body_take"]) if t not in takes]
        if missing:
            report.append((j["id"], "SKIPPED — take not found: " + ", ".join(TS.TAKES[t] for t in missing), 0, {})); print(report[-1][1]); continue
        if final.exists() and final.stat().st_size > 1000 and not a.force:
            report.append((j["id"], "already rendered", 0, {})); print("already rendered → skipped (use --force to redo)"); continue
        try:
            out, al = render_job(j, takes, work, renders, a.photos)
            dur = RV.probe(out)["dur"]; note = f"OK {dur:.1f}s"
            weak = [f"{k} {v*100:.0f}%" for k, v in al.items() if v < 0.55]
            if weak: note += "  ! CHECK — script heard weakly: " + ", ".join(weak)
            report.append((j["id"], note, time.time() - t0, al))
        except BaseException as e:
            if isinstance(e, KeyboardInterrupt): raise
            traceback.print_exc(); report.append((j["id"], f"FAILED — {str(e)[:160]}", time.time() - t0, {}))
    print(f"\n==================== BATCH REPORT  ({(time.time()-t_batch)/60:.0f} min) ====================")
    for jid, note, secs, al in report: print(f"  {jid:16s} {note:60s} {secs/60:4.1f} min")
    print(f"\nads → {renders}")
    (renders / "batch_report.json").write_text(json.dumps([dict(id=i, note=n, minutes=round(s/60, 1), align=al) for i, n, s, al in report], indent=1))
    return report

if __name__ == "__main__":
    main()
