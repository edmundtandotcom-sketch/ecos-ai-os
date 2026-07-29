---
name: rei-vsl-pipeline-recurring-bugs
description: Recurring REI video pipeline bugs that must be QC-checked before every delivery
metadata: 
  node_type: memory
  type: project
  originSessionId: bad9308c-240d-41df-aa8e-23b2f0255cc2
---

Recurring bugs in the REI FFmpeg pipeline (/tmp/rei_rebuild_v*.py on Cindior's Mac) — flagged in v5 review (12 Jun 2026), some flagged earlier and not fixed:

1. **Audio cutoffs at cut boundaries** — words clipped where cuts land mid-word. v5 examples: 0:12 "framework", 1:24 "avoid" (end of video). Flagged before v5 and regressed. Fix: validate all CUTS boundaries against transcript word end-times (≥80ms clearance) in an automated QC pass.
2. **End card missing from final export** — Phase 9 builds the 3s logo card but v5 shipped without it; Phase 10 concat likely failed silently. Always verify final duration = main + 3s and the logo is visually present.

**Why:** Edmund noticed both; repeat regressions damage trust in the pipeline.
**How to apply:** Run the QC checklist in SI05_VSL_v6_CHANGE_SPEC.md (02_VSL folder) before showing Edmund any version. See [[rei-vsl-video-style-rules]].
