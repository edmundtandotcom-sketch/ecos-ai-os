from pathlib import Path
p = Path(r"H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-09_Webinar\05_RENDER\work\_final_audit2.py")
s = p.read_text(encoding="utf-8")


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)


# video: compare frame ZERO of the shot (push zoom is 1.0 there) with tight frames f0-3..f0+3
rep('''    ref = gray(FINAL, ss=s["out0"] + 1 / 30)[0]          # frame 1 of the shot, in the final
    cands = gray(TV, vf, ss=(f0 - 2) / 30, n=7)             # tight frames f0-2..f0+4
    d = [np.abs(c - ref).mean() for c in cands]
    o = int(np.argmin(d)) - 3                               # 0 == exact (frame f0+1)''',
    '''    ref = gray(FINAL, ss=s["out0"])[0]                    # frame 0 of the shot, in the final (zoom 1.0)
    cands = gray(TV, vf, ss=(f0 - 3) / 30, n=7)             # tight frames f0-3..f0+3
    d = [np.abs(c - ref).mean() for c in cands]
    o = int(np.argmin(d)) - 3                               # 0 == exact (frame f0)''')
# speech: a longer reference window so the correlation is not dominated by the bed
rep('''    ref_a = audio(SRC[label], T - 0.3, 0.6, tempo=SPEED)
    sig = audio(FINAL, F - 0.3 / SPEED - 0.5, 0.6 / SPEED + 1.0)
    off, c = best_lag(ref_a, sig, int(0.5 * SR))
    ok = abs(off) <= 40 and c > 0.5''',
    '''    ref_a = audio(SRC[label], T - 0.4, 1.0, tempo=SPEED)
    sig = audio(FINAL, F - 0.4 / SPEED - 0.5, 1.0 / SPEED + 1.0)
    off, c = best_lag(ref_a, sig, int(0.5 * SR))
    ok = abs(off) <= 40 and c > 0.4''')
p.write_text(s, encoding="utf-8")
print("audit corrected")
