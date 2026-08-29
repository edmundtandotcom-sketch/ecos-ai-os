---
name: video-produce
description: Route a locked script or reel breakdown to the correct rendering step, and be explicit about which production tiers are portable to any environment and which require the desktop machine. Use when asked to render, produce, cut, or export a video, or invoke /video-produce. Never fake or simulate a render this environment cannot actually perform.
---

# Video Produce — Production Routing

Single entry point for the actual production step. The pipeline has three tiers with very different portability — check this list before assuming any step is available, rather than trusting older docs that describe it as one undifferentiated "E:\REMOTION pipeline."

## The three tiers (confirmed 2026-08-25 against the 4 live repos: `ecos-ai-os`, `sharpcut-studio`, `ecos-runtime`, `property-business`)

1. **Backdrop Studio — background replacement.** Local-only, `E:\BACKDROP` on the desktop machine. Not in any git repo. Desktop-only, no exceptions today.

2. **SharpCut Studio — cut / caption / crop / export.** `edmundtandotcom-sketch/sharpcut-studio` — a browser-only React/Vite app (filler-word and silence removal, captions, true crop, transitions, zoom, MP4 export), fully client-side via WebAssembly/FFmpeg.wasm, no backend, deployed on Cloudflare Pages. **Portable** — identical tool and result whether opened from the desktop machine or any other device's browser, because the user's own browser does the work either way. On the desktop specifically, a local native-FFmpeg bridge (`E:\BACKDROP`'s server) makes export roughly 21x faster than the in-browser wasm engine (measured: 12s vs 259s on the same job) — same tool, same output, just faster locally. Claude cannot drive its UI directly; it can produce the cut list and caption text SharpCut needs.

3. **Remotion composite build — multi-cam productions.** The AmberwoodReview-style long-form builds: composited multi-cam footage, gold-ring PIP, navy data-card interstitials, per-clip subtitle sync. Lives at `E:\REMOTION` on the desktop machine (composition, generator script, verify gate). **Confirmed not present in any of the 4 repos checked** — this tier has no git backup today and is genuinely desktop-only. If asked to render this tier from a cloud/non-desktop session: stop, say so plainly, and do not attempt or simulate a render.

## Procedure

1. Identify which tier the task actually needs — don't assume tier 3 just because a prior campaign used it; a simple reel cut is tier 2 only.
2. **Tiers 1 and 3, cloud/non-desktop session:** produce whatever upstream artifact is possible (script, shot list, cut list, caption copy) and stop there. Tell the user explicitly that the render step needs the desktop machine — do not report a render as done when it wasn't performed.
3. **Tier 2, either environment:** produce the cut list and caption copy; the user runs the actual export themselves in the browser app.
4. **Tier 3, desktop, pipeline present:** use the SHARED library in `E:\REMOTION\work\lib\` — do not copy a previous campaign's scripts. Before it existed there were 37 near-duplicate render scripts across Amberwood, Lucerne and Serra, only three of which verified their output and only three of which resumed, and never the same three. Consolidated 2026-08-29; every rule in it is a scar, and the reasoning is in `EDITING_PLAYBOOK.md` CH.2b.

   | Step | Use |
   |---|---|
   | Choose the master angle | `prep_lib.pick_master` — by MEASURED detail, never by resolution. The OBS program capture is a low-bitrate re-encode; Serra's "1080p" file held a quarter of the detail of the 720p camera feed beside it. |
   | Grade | `prep_lib.measure_grade` / `compare_grade` — "washed out" is a measurable claim, and a natural grade holds face exposure while moving colour. |
   | Build the timeline | `pipeline_checks.collision_pass`, `asset_gate`, `anchor_report` — these fail loudly at build time. A missing asset kills a render outright; an unfound anchor silently drops a display. |
   | Render | `render_campaign.ps1` via `launch.ps1` — resumable ffprobe-verified parts, per-campaign bundle dir, memory-aware worker sizing. |
   | Check on it | `status.sh <campaign>` — reports frame PROGRESS. A process killed by the OS writes no success and no failure marker, so a monitor waiting for either reads a dead render as a healthy one. |

   Then run the campaign's verify gate (pattern: `verify_amberwood.py` — a named checklist gate per production) before marking a version deliverable. Version and log the render (vN naming — never overwrite a previously delivered version silently), update the campaign's `00_INDEX.md` deliverables and status in the same pass.

## If full cloud parity for tier 3 is wanted

That requires committing the actual Remotion project code and required non-footage assets (fonts, audio beds) to a repo cloud can clone — footage itself is too large for git regardless and would need to stay supplied separately. This is a real infrastructure decision with real tradeoffs (repo size, asset licensing, exposing production code) — raise it with Edmund explicitly before acting on it; this skill does not do that migration on its own initiative.
