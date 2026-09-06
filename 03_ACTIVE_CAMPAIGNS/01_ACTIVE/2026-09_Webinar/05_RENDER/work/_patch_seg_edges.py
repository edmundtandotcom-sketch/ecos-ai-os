from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


rep('''    tag = f"_s{int(round(speed * 100))}m"   # m = motion-compensated''',
    '''    tag = f"_s{int(round(speed * 100))}n"   # n = mci with clean segment edges''')

rep('''        for i, (label, a, b) in enumerate(plan):
            q = segdir / f"seg{i:03d}.mp4"
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(SOURCES[label]),
                 "-vf", vf, *af,
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
                 "-pix_fmt", "yuv420p", "-r", str(FPS),
                 "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                 "-video_track_timescale", "90000", str(q)])''',
    '''        for i, (label, a, b) in enumerate(plan):
            q = segdir / f"seg{i:03d}.mp4"
            if speed == 1.0:
                run(["ffmpeg", "-y", "-loglevel", "error",
                     "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(SOURCES[label]),
                     "-vf", vf,
                     "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
                     "-pix_fmt", "yuv420p", "-r", str(FPS),
                     "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                     "-video_track_timescale", "90000", str(q)])
                continue
            # minterpolate repeats its first and last frames (it needs two
            # frames to interpolate), so every segment join carried 2 held
            # frames on each side - a hitch on every cut that lands on a join.
            # Interpolate 2 source frames of EXTRA context on each side, then
            # trim those frames off; audio is cut from the exact range.
            e = 2.0 / FPS
            a2 = max(0.0, a - e)
            lead = int(round((a - a2) / speed * FPS))
            nfr = int(round((b - a) / speed * FPS))
            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a2:.3f}", "-to", f"{b + e:.3f}", "-i", str(SOURCES[label]),
                 "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(SOURCES[label]),
                 "-filter_complex",
                 f"[0:v]{vf},trim=start_frame={lead}:end_frame={lead + nfr},setpts=PTS-STARTPTS[v];"
                 f"[1:a]atempo={speed},asetpts=PTS-STARTPTS[a]",
                 "-map", "[v]", "-map", "[a]",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
                 "-pix_fmt", "yuv420p", "-r", str(FPS),
                 "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                 "-video_track_timescale", "90000", str(q)])''')
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("segment edges patched")
