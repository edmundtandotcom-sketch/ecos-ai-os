# 05_ZOOM_SUMMARY_TOOL_REGISTRY

Version: v1.0
Status: REGISTRY
Date: 2026-07-10
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\Artifacts\zoom-summary-generator\`, `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\04_CLIENTS\ZOOM_SUMMARY\`

## Purpose
Registry of the live Zoom summary generator tool and its supporting Google Doc guides. Not copied — this is a live artifact plus cloud-only gdocs, both stay in place.

## Live Tool
`H:\Shared drives\00_E.C.O.S\Artifacts\zoom-summary-generator\`

| Item | Detail |
|---|---|
| `index.html` | Current live version of the tool |
| `thumbnail.png` | Tool thumbnail |
| `versions\` | 14 prior versions (timestamped `.html` files, epoch-ms filenames), newest to oldest revision history |

This is a working Claude Artifact (HTML tool) — functional, in active use. Do not move; Artifacts are managed by their own system, not standard Drive files.

## Supporting Google Doc Guides (cloud-only, pointer files)
`H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\01_CLIENT_EDITION\04_CLIENTS\ZOOM_SUMMARY\`

| File | Note |
|---|---|
| `ZOOM_SUMMARY_PRODUCTION_GUIDE.md.gdoc` | Production guide — cloud-only Google Doc, not readable as plain text via file system |
| `GETTING_STARTED.md.gdoc` | Getting-started guide |
| `GETTING_STARTED_CORRECTED.md.gdoc` | Corrected version — check which is current with Edmund/Cindior before use |
| `BACKEND_IMPLEMENTATION.md.gdoc` | Backend implementation notes |
| `BACKEND_IMPLEMENTATION_CORRECTED.md.gdoc` | Corrected version — check which is current |
| `PRODUCTION_GUIDE_CORRECTED.md.gdoc` | Corrected version — check which is current |

**Note:** These are Google Drive shortcut files (`.gdoc`), not plain text — they cannot be read or copied as markdown via file system access. Content lives in Google Docs; open via Drive to read. Three of the six have a "_CORRECTED" twin — flag for Edmund/Cindior to confirm which version (original or corrected) is the current master and archive the superseded one.

## Migration Recommendation
- Leave the Artifact tool where it is — it is live and functioning.
- Do not copy the `.gdoc` pointer files (cloud-only, no local content to copy).
- **Gap to flag:** duplicate "GETTING_STARTED" / "BACKEND_IMPLEMENTATION" / "PRODUCTION_GUIDE" docs with and without "_CORRECTED" suffix — this is exactly the kind of ambiguous-authority naming Global Rule 3 (no "(1)"-style duplicates) is meant to prevent. Recommend Edmund/Cindior pick the correct one, archive the other, during the next Drive cleanup pass.

## READS FROM
- None (standalone tool)

## FEEDS INTO
- `01_E.C.O.S/07_OPERATIONS_DESK.md` (owns tool maintenance)
- Client meeting workflow (consult/coaching call summaries)
