# Operations Tool Artifacts — _INDEX
Version: v1.0
Status: CONTROLLED STATIC ARTIFACTS
Date: 2026-07-20

## Purpose

Home for self-contained, non-secret operational artifacts that need shared reference or use but are not source repositories or live runtimes.

## Current artifact

`ZOOM_SUMMARY_GENERATOR_STATIC_ARTIFACT/` — static Zoom-summary generator moved from root `Artifacts` on 2026-07-20. Its detailed boundary is in `../05_ZOOM_SUMMARY_TOOL_REGISTRY.md`.

## Rules

- No client recordings, transcripts, summaries, contact data, tokens or credentials.
- Do not treat generated versions, thumbnails or Drive timestamps as deployment proof.
- Verify source repository, deployment, consent and retention before change/use.
- Source/runtime remains local/private Git.
- Archive a replaced static artifact inside this owning system; do not return it to root `Artifacts`.
