# START HERE
Version: v1.1
Status: APPROVED MASTER
Date: 2026-08-25
Supersedes: v1.0 (2026-07-31) — added the reels-routine row now that video creation has portable, committed skills (see `01_E.C.O.S/08_CLAUDE_SKILLS_MAP.md`)

**This is the only file you need to open. Ever.**

---

## The one rule

**You don't navigate folders. You say what you want. Claude routes it.**

The folder structure exists for the *system* to stay clean — not for you to memorise. If you are browsing folders to find something, stop and just ask instead.

---

## What do you want to do? → Say this

| You want to… | Say |
|---|---|
| **Anything business** — strategy, content, ads, sales, ops, recruitment | `/desk` + what you need |
| Capture a new idea or a change of direction | `/new-idea` + the idea |
| Pull a competitor's live Meta ads (real copy, video, transcript) | `/rei-ads-scan` + advertiser name |
| Write a long-form YouTube script | `/rei-video-routine` + topic |
| Write reel scripts / break a long-form into reels | `/rei-reels-routine` + campaign name |
| Design the edit of a video ad (look, effects, captions) | `/rei-ads-routine` + campaign + assets |
| Build a quiz, diagnostic, or calculator | `/build-interactive` |
| Check the system for drift, duplicates, mess | `/os-audit` |
| End a working session cleanly | `/session-close` |
| **Not sure which?** | Just describe the problem in plain words |

That last row is the important one. **You never have to pick correctly.** Describe the problem; routing is Claude's job, not yours.

---

## The three places — you only ever touch the first

| Where | What lives there | Your involvement |
|---|---|---|
| **Google Drive** `H:\Shared drives\00_E.C.O.S` | The business brain — strategy, decisions, campaigns, approved assets | This is "the workspace." Claude works here by default. |
| **`E:\` drive** | Heavy things Drive can't hold — Zoom recordings, consult intelligence, video software | Claude reaches it when a task needs it. You don't go here. |
| **GitHub** (all private) | Invisible safety net. Auto-saves the brain every night. | **Never.** It exists so nothing is ever lost. |

<details>
<summary>The four repos — reference only, you don't touch these</summary>

| Repo | What it is |
|---|---|
| `ecos-ai-os` | **The brain.** This Drive's governance + AI OS. Auto-committed nightly. |
| `ecos-weekly-intelligence` | **The weekly engine.** Runs Monday's RSS collect on GitHub's servers (they can reach news sites; the Claude sandbox can't). Output arrives as a PR for your review. |
| `ecos-runtime` | **The local software** — voice command centre on `E:\ECOS`. |
| `sharpcut-studio` | **The video editor** — standalone app, own release cycle. |

Four repos, not one, because each has a different job and lifecycle. Merging them would tangle working automation with your governance records.
</details>

Client names, phone numbers and case records live in a **separate restricted drive** (`00_E.C.O.S_CLIENTS_PRIVATE`). GoHighLevel remains the live source of truth for contacts.

---

## What runs by itself (you do nothing)

- **Nightly** — the brain is committed to private GitHub
- **Monday** — system audit + new-files sweep
- **Monday** — Singapore property content + ads intelligence (Cloud routines; finished creative waits in a PR for your review — it is never auto-published)
- **1st of the month** — new Zoom consults processed into marketing clips *and* consult intelligence

You'll get a report. You don't start these.

---

## If you're stuck or going in circles

Say: **"I'm going in circles — what should I be doing right now?"**

Claude reads current priorities and tells you the next single action. That is always a valid move.

---

## The rules that govern everything

Full constitution: `00_AI_OPERATING_SYSTEM\CLAUDE.md`. You don't need to read it — Claude reads it every session. Three things worth knowing:

1. **The 3-Question Filter** — every asset must pass: *Is it simple? Does it work? Can I do it?*
2. **Decisions happen in chat**, with a recommendation attached. Never buried in a file.
3. **Nothing is a yes-man.** Weak thinking gets challenged, including yours.
