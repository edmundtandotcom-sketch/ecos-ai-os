# 14_BRAIN_PORTABILITY.md — Getting the Brain Onto a New Machine, and Recovering It If GitHub Is Down
Version: v1.0
Status: APPROVED MASTER
Date: 2026-08-07
Supersedes: n/a — new file.
Sources: Decision 125 (One Brain — Staged Relocation, AI-HQ Rejected); CLAUDE.md §7/§14 (code portability rule); Operating Agreement rule 39/43 (destructive-action guardrail).

> Check this file before setting up a new computer, restoring from backup, or reasoning about where "the brain" actually lives. If this file conflicts with CLAUDE.md §7/§14, CLAUDE.md wins.

---

## 1. What the brain is

The canonical business brain is the git repository currently checked out at `H:\Shared drives\00_E.C.O.S` (branch `main`), with its GitHub remote at:

`https://github.com/edmundtandotcom-sketch/ecos-ai-os.git` (private)

The repo — not any single machine's copy of it, not a parallel vault, not a second "AI-HQ" — is the one brain (Decision 125). As of Phase A (2026-08-07) the working copy is synced through Google Drive for Desktop at the H: path above. Phase B (a separate, not-yet-authorized decision) would move the live working copy to a local SSD and demote Drive to an asset warehouse and backup target only. Until Phase B is approved, H: remains the live working copy.

Google Drive never holds the brain long-term as a *runtime* — see CLAUDE.md §7/§14 — but it does hold this repo's working tree today, plus immutable recovery bundles and documentation. Bulk media (video, images, raw asset library content) lives in `01_ASSET_LIBRARY`, not inside the git repo.

---

## 2. Setup on a new computer

1. Install Git for Windows: `winget install --id Git.Git`
2. Install GitHub CLI: `winget install --id GitHub.cli`
3. Authenticate: `gh auth login` (choose GitHub.com, HTTPS, browser login) then `gh auth setup-git` so HTTPS git operations use gh's stored credentials — no separate password/token entry.
4. Set git identity (once per machine, or use `--global` to cover all repos):
   `git config --global user.name "Edmund Tan"`
   `git config --global user.email "edmundtandotcom@gmail.com"`
5. Clone the private repo to a local SSD path (not inside Google Drive — see the code portability rule):
   `git clone https://github.com/edmundtandotcom-sketch/ecos-ai-os.git E:\ECOS_BRAIN`
6. Open the cloned folder in Claude Code, and/or open it as an Obsidian vault for browsing/linking. Either tool can point at the same local clone.

This gives a full, current copy of the markdown brain. It does **not** include `01_ASSET_LIBRARY` bulk media or anything under the restricted `00_E.C.O.S_CLIENTS_PRIVATE` drive — those stay on Google Drive per the campaign/asset/PII rules in the root `CLAUDE.md`.

---

## 3. Recovery levels

**Level A — GitHub is reachable (normal case).**
Clone or pull from the remote as in §2. This is always the first thing to try.

**Level B — GitHub itself is down or the repo is inaccessible.**
Restore from the newest git bundle:
1. Locate the newest bundle in `E:\ECOS_BACKUPS\ecos-ai-os\` or, as a second copy, `H:\Shared drives\00_E.C.O.S\_BACKUPS\ECOS_BACKUPS\`. Bundles are named `ecos-ai-os-<date>.bundle`; take the latest date.
2. Verify it before trusting it: `git bundle verify <path-to-bundle>`
3. Clone from the verified bundle: `git clone <path-to-bundle> E:\ECOS_BRAIN_RESTORED`
4. Once GitHub is reachable again, add the remote back and push/reconcile: `git remote add origin https://github.com/edmundtandotcom-sketch/ecos-ai-os.git`

**Level C — Validate before trusting a restored copy.**
A restored bundle clone may be older than the live repo. Before treating it as current:
1. Check the newest daily-snapshot commit date in its log: `git log -1 --format=%cd --date=short "Daily snapshot: *"` (or `git log --oneline -5`).
2. Compare that date against the known last-push date (ask Edmund, or check GitHub's web UI if reachable from another device).
3. If the restored copy is stale, treat it as reference only until a newer bundle or live GitHub access is available — do not overwrite a newer working copy with an older restored one.

---

## 4. Rule: large assets never go in the repo

Git and GitHub are for the markdown brain — decisions, SOPs, positioning, scripts, indexes, small self-contained artifacts. Large or bulk media (video, raw photo libraries, exported ad creative, `.pptx`/`.docx` decks over a few MB) belong in `01_ASSET_LIBRARY` or the owning campaign folder in `03_ACTIVE_CAMPAIGNS`, tracked by an index — not committed to git. This keeps the repo small, clone times fast, and bundles portable.

---

## 5. ChatGPT access

ChatGPT reads the brain through its own GitHub connector, pointed at the private `ecos-ai-os` repo. This is **read-only** — ChatGPT never writes back to the repo, never gets push access, and never edits files directly.

When a ChatGPT session produces something worth keeping (a decision, a draft, a piece of analysis), the conclusions come back through the handoff template at `00_AI_OPERATING_SYSTEM/00_COMMAND_CENTER/12_ECOS_INBOX/CHATGPT_HANDOFF_TEMPLATE.md`. Claude reconciles that handoff into the owning campaign/OS files. Approved decisions only get added to `04_DECISION_MEMORY.md` after Edmund confirms them in chat — a ChatGPT session output is an input to be reconciled, not itself an approved decision.

---
*Approved 2026-08-07 (Decision 125). Amend via `/new-idea` or an in-chat ruling; bump the version.*
