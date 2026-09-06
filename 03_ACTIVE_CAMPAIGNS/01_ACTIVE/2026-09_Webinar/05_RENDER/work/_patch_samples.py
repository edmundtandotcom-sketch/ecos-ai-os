from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\render_webinar.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# audio trimmed in whole samples (1600 per frame at 48k) - float seconds left
# a sample short here and there, 110 samples over 156s
rep('''            af += f"apad,atrim=end={N / FPS:.6f},asetpts=N/SR/TB"''',
    '''            af += f"apad,atrim=end_sample={N * 48000 // FPS},asetpts=N/SR/TB"''')
# reuse a video segment that already has exactly N frames (audio is cheap)
rep('''            run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a2:.4f}", "-to", f"{b + e:.4f}", "-i", str(SOURCES[label]),
                 "-vf", vf, "-an", "-frames:v", str(N),''',
    '''            have = (qv.exists() and int(ffprobe(qv, "stream=nb_frames")["streams"][0]["nb_frames"]) == N)
            have or run(["ffmpeg", "-y", "-loglevel", "error",
                 "-ss", f"{a2:.4f}", "-to", f"{b + e:.4f}", "-i", str(SOURCES[label]),
                 "-vf", vf, "-an", "-frames:v", str(N),''')
rep('''        for old in list(segdir.glob("seg*.mp4")) + list(segdir.glob("seg*.wav")):''',
    '''        for old in list(segdir.glob("seg*.wav")):''')
rep('''        if nv != sum(nfs) or abs(da - sum(nfs) / FPS) > 0.002:''',
    '''        if nv != sum(nfs) or abs(da - sum(nfs) / FPS) > 0.001:''')
p.write_text(s, encoding="utf-8")
import ast
ast.parse(s)
print("sample-exact audio, video segments reused")
