# 06_CODE_REPOSITORY_REGISTRY — LIVE CODE POINTERS
Version: v1.1
Status: APPROVED MASTER
Date: 2026-07-31
Supersedes: v1.0 (2026-07-31) — v1.0 listed the repo under its old name;
`property-business` was renamed to `ecos-weekly-intelligence` the same day
(old name now redirects; do not treat this as a separate repo).
Sources: Operating Agreement rule 6 (§14 Code Portability rule) — live code stays in git, not Shared Drive.

## Purpose
Single index of every live software repository the business runs, so E.C.O.S is the one place to *find* code — while the code itself stays in its correct git-native runtime, per CLAUDE.md §14: *"Google Drive is knowledge storage and immutable recovery, not a live software runtime."* This registry never holds the code, only a pointer + description.

## Repositories

| Repo | What it is | Where it lives | Notes |
|---|---|---|---|
| `edmundtandotcom-sketch/ecos-weekly-intelligence` (renamed from `property-business` on 2026-07-31) | Weekly Ads Intelligence OS (Meta Ad Library scan/score/report pipeline, Python + generated dashboard) and Weekly Content Intelligence OS. Runs on a scheduled branch/PR workflow. | GitHub — https://github.com/edmundtandotcom-sketch/ecos-weekly-intelligence | Old URL (`.../property-business`) 302-redirects, but update remotes/bookmarks to the new name. Dashboard republished each week as a stable Claude Artifact link. |
| `edmundtandotcom-sketch/sharpcut-studio` | SharpCut Studio — browser-only video editor (React/Vite/TypeScript). Removes filler words/silence from talking-head video, adds captions/zoom/transitions, exports MP4. No backend, no upload, all client-side (WebAssembly/Web Workers). | GitHub — https://github.com/edmundtandotcom-sketch/sharpcut-studio | Private repo. Unrelated to the rename above — a genuinely separate project. |

## Adding a repo
When a new live codebase starts, add a row here (name, one-line description, GitHub URL, any operating notes) rather than moving it into Shared Drive. Only Git bundles / source ZIPs / documentation snapshots belong in Drive for recovery purposes (§14) — never a live clone as the working copy.

## READS FROM
`00_COMMAND_CENTER` (Code Portability rule, §14).

## FEEDS INTO
Desk 07 (Operations) — first stop when locating or spinning up work on any live codebase.
