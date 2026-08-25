#!/usr/bin/env python3
"""Dry-run the timing logic against the expected script, with no media.

Synthesises an even-paced word track from the NL01 script and checks that
every overlay beat resolves, that nothing collides, and that the karaoke cues
are well formed. Run this after editing BODY_BEATS — it catches phrase-anchor
mistakes in a second instead of after a 40-minute encode.

    python3 renders/tools/selfcheck.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import render_pipeline as rp  # noqa: E402

SCRIPT = """Is this your second, third or fourth investment property? Then you
already know property makes money. That's not the question anymore. Here's the
question. When you buy a new launch, you commit $500K to $1M of your own cash
and CPF. You take a 25-year mortgage. You pay stamp duty, interest, agent fees.
And you wait four years. That same money could be invested in the S&P 500 which
compounds historically at 10% a year. No mortgage. No stamp duty. No four-year
wait. No wondering who your future buyer is. So the benchmark for a good
property investment is not gains. It's beating the S&P 500. But most agents
only talk about gains. And almost any property in Singapore can make some kind
of gain. It's an easy test to pass. Before I invest in a property myself, and
before any client of mine invests in one, I ask one question. Can this project
beat the S&P 500? Because if it can't, we'd rather just buy the S&P 500 and
save ourselves the mortgage, the stamp duty, the interest, the agent fees and
the four years. I hold my own money to it. One of my properties returned 22.9%
a year on the capital I committed. Another returned 12.9%. My clients are held
to the same standard. One of my new launches was bought at $1.15M. I committed
about $321K of my own capital. Three years later, it sold at $1.525M. After
interest, stamp duty, legal fees, commission and maintenance, the net profit
was about $282K. That worked out to roughly 22.9% a year on the capital
committed. Another property? Bought at $1.05M with about $292K committed.
Exited four years later at $1.28M. The property itself only grew around 5.1% a
year. After costs and rental income, the return on the capital committed worked
out to roughly 12.9% a year. Same Singapore market. Same cooling measures. And
that difference is decided before you buy. At the entry price. The unit you
choose. Your future buyer. Your exit price. And how much usable equity that
property releases for your next move. That's why before I invest in a property
myself, and before a client invests in one, I ask: Can this project actually
beat the S&P 500 benchmark? Because the goal isn't to own more properties. The
goal is for Property #2 to fund Property #3. Property #3 to fund Property #4.
And for every move to push your net asset value higher. That's exactly how we
use the New Launch Ladder. We calculate the Return on Equity the project needs
to produce. We set the walkaway price before you fall in love with the
showflat. And we map your next three moves before you commit to this one.
Because if you're already on your second, third or fourth property, 'I made
money' is no longer good enough. Your capital needs to work harder."""


def synth_words(text, wps=2.8):
    words, t = [], 0.0
    step = 1.0 / wps
    for tok in text.split():
        words.append({"w": tok, "s": round(t, 3), "e": round(t + step * 0.94, 3)})
        t += step + (0.22 if tok.endswith((".", "?")) else 0.0)
    return words, t


def cue_bounds(line):
    f = line.split(",")

    def s2f(x):
        h, m, s = x.split(":")
        return int(h) * 3600 + int(m) * 60 + float(s)
    return s2f(f[1]), s2f(f[2])


def main():
    words, total = synth_words(SCRIPT)
    beats, missed = rp.resolve_beats(words, rp.BODY_BEATS)
    fails = []

    print(f"synthetic body length: {total:.1f}s")
    print(f"beats matched: {len(beats)}/{len(rp.BODY_BEATS)}")
    for b in beats:
        print(f"  {b['graphic']:18s} {b['start']:7.2f} -> {b['end']:7.2f} "
              f"[{b['place']}]")
    if missed:
        fails.append(f"unmatched beats: {[m[0] for m in missed]}")

    if any(b["end"] <= b["start"] for b in beats):
        fails.append("a beat has a non-positive duration")

    bands = {}
    for b in beats:
        bands.setdefault(b["place"], []).append(b)
    for place, items in bands.items():
        items.sort(key=lambda d: d["start"])
        for a, c in zip(items, items[1:]):
            if c["start"] < a["end"]:
                fails.append(f"overlap in band {place}: "
                             f"{a['graphic']}/{c['graphic']}")

    full = [(b["start"], b["end"]) for b in beats if b["place"] == "full"]
    for b in beats:
        if b["place"] == "full":
            continue
        for s, e in full:
            if s < b["end"] and b["start"] < e:
                fails.append(f"{b['graphic']} is stranded under a full-frame card")

    out = pathlib.Path(rp.WORK / "selfcheck.ass")
    out.parent.mkdir(parents=True, exist_ok=True)
    rp.build_ass(words, [], out)
    cues = [l for l in out.read_text().splitlines() if l.startswith("Dialogue")]
    overlaps = sum(1 for a, b in zip(cues, cues[1:])
                   if cue_bounds(a)[1] > cue_bounds(b)[0])
    print(f"caption cues: {len(cues)}, overlapping: {overlaps}")
    if overlaps:
        fails.append(f"{overlaps} caption cues overlap (would double-stack)")
    if not cues:
        fails.append("no caption cues generated")

    print()
    if fails:
        for f in fails:
            print("FAIL:", f)
        sys.exit(1)
    print("PASS — beats, bands and captions are all consistent.")


if __name__ == "__main__":
    main()
