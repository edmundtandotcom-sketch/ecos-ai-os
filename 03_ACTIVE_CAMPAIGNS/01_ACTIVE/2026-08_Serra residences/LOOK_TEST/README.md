# Serra — look bake-off (2026-08-24)

Five 60-second clips, all the same take and the same 60 seconds of the cold
open, so the only variable is the look. Watch them back to back.

| File | What it is |
|---|---|
| `VX_ungraded_reference.mp4` | Straight out of the camera. The reference for "washed out". |
| `V0_original_room.mp4` | Your real room + the new **S5 grade**. No backdrop. |
| `V1_studio_woodslat.mp4` | Composited into an angled wood-slat studio — warm, deepest room, practical lamp. |
| `V2_studio_slatcove.mp4` | Composited into a wider slat-cove set — cooler, more air around the head. |
| `V3_studio_lounge.mp4` | Composited into an evening lounge — window on the left gives real side light. |

Stills: `LOOK_GRID.jpg` (all five at the same frame) ·
`GRADE_BEFORE_AFTER.jpg` (the grade candidates) ·
`CUTOUT_EDGE_3x_ZOOM.jpg` (hair edge at 3× — the halo check).

## Two decisions

**1. The grade.** The raw footage measured genuinely flat: highlights topped
out at 180/255, blacks were lifted to ~30, and colour separation was almost
nil (saturation spread 14.6). S5 puts the black and white points back, warms
the skin, takes the magenta cast off the wall, and adds a light S-curve and
micro-sharpen. Face reads 154/135/109 against 129/114/104 raw.
This one is close to a no-brainer — VX is only here as the reference.

**2. Original room or a studio backdrop.** On Lucerne you looked at eleven
composites and chose the real room, because they read as overlays. Two things
changed here:

- **Halo.** The old chain lifted the alpha with a gamma of 0.72, which
  *widens* the soft edge — that is what made the fringe. It now erodes the
  matte first and hardens with gamma 1.25. `CUTOUT_EDGE_3x_ZOOM.jpg` is the
  hair edge blown up 3×: no green fringe, no white halo, individual strands
  intact.
- **Integration.** Wall shadow, contact shadow, a directional rim, a light
  wrap sampled from the actual plate, matched grain, and a depth-graded
  defocus so the far corner falls off like a real lens. The room is also
  white-balanced *toward you*, not the other way round.

Serra's real room is a plain grey curtain, which is flatter than Lucerne's —
so a backdrop has more to add here than it did there. But it is your call,
and V0 is a perfectly good answer.

My read: **V1 (wood-slat desk)** is the strongest of the three — the deepest
room, and the practical lamp gives the rim light something to be motivated
by. V0 is the safe answer if any of them still read as composited to you.

## Note
The three studios are built from the existing backdrop library, including the
angled lounge that was generated for Amberwood and never used — so none of
them repeats what Amberwood shipped. Gamma's image credits are exhausted, so
I could not generate a purpose-made Serra set; top it up and I will.
