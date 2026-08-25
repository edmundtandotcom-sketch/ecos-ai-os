# 08_CLAUDE_SKILLS_MAP — Skills-to-Desk Map
Version: v1.1
Status: APPROVED MASTER
Date: 2026-08-25
Supersedes: v1.0 (undated stub, single `/video-produce` row pointing at the E:\REMOTION pipeline as one undifferentiated step)
Sources: `ecos-ai-os/.claude/skills/rei-video-routine`, `ecos-ai-os/.claude/skills/rei-reels-routine`, `ecos-ai-os/.claude/skills/video-produce`; live audit of `sharpcut-studio`, `ecos-runtime`, `property-business` repos (2026-08-25)

## Video creation skills

Committed, portable skills in `ecos-ai-os/.claude/skills/` — identical behavior on desktop and cloud, since they're config in this repo rather than a local slash-command setup.

| Skill | Content desk | Purpose |
|---|---|---|
| `/rei-video-routine` | Content desk | Long-form YouTube/VSL/project-review script generation. Stops at a locked script — does not render. |
| `/rei-reels-routine` | Content desk | Reel script generation — persona ad reels (Legacy Launch G-codes) or organic topical-breakdown reels cut from a long-form. Stops at a script/breakdown — does not cut. |
| `/video-produce` | Content desk | Routes a locked script/breakdown to the right production tier (Backdrop Studio, SharpCut Studio, or the Remotion composite build) and is explicit about which tiers are desktop-only. |

**Production tier note (2026-08-25 audit):** only the cut/caption/export tier (SharpCut Studio, `edmundtandotcom-sketch/sharpcut-studio`) is actually portable — it's a browser app with no backend, deployed on Cloudflare Pages. Background replacement (`E:\BACKDROP`) and the Remotion composite build (`E:\REMOTION`) are desktop-only and not backed up in any of the 4 git repos checked (`ecos-ai-os`, `sharpcut-studio`, `ecos-runtime`, `property-business`). Full breakdown: `video-produce`'s `SKILL.md`.

## READS FROM
Root `CLAUDE.md` §10 (Skills-to-desk map pointer); `00_AI_OPERATING_SYSTEM/08_OPERATIONS/06_CODE_REPOSITORY_REGISTRY.md`.

## FEEDS INTO
`START_HERE.md` ("Say this" table); Desk 03 (Content Studio).
