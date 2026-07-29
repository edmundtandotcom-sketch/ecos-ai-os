# 11_CLEANUP_SIGNOFF_LIST — Legacy Folder Deletion Sign-Off
Version: v1.0
Status: EXECUTED (Tiers 1+2) / RETAINED (Tier 3) — Edmund, 2026-07-11 (Decision 044; execution record initially misnumbered 041 — see `04_DECISION_MEMORY.md`). Per-item execution log: `12_CLEANUP_EXECUTION_LOG_2026-07-11.md`
Date: 2026-07-11
Supersedes: none
Sources: AI OS rebuild scout reports (2026-07-10), on-disk verification 2026-07-11 (file counts, sizes, SHA256/MD5 hashes, E:\ cross-checks), full content review of all 22 Cowork sessions (second pass, 2026-07-11)

---

## ✅ EXECUTION RECORD — 2026-07-11

Edmund approved in chat: "Approve Tier 1. For Tier 2, rule A5 first, then option B on Codex." Sequence executed:

1. **Option B rescue first:** 3 testimonial clips + transcripts copied from E:\ originals into `07_BRAND_AND_PROOF_BANK\08_PROOF_BANK\00_GENERAL_AUTHORITY\` (TESTIMONIAL_Whiz_2020-06-04, TESTIMONIAL_Mark_Joycelyn_2020-06-11, TESTIMONIAL_Mark_Joycelyn_Treasure_Purchase2) — size-verified.
2. **A5 ruled** (Decision 040): E:\ stays as registered evidence vault — registry + cited-excerpt migration at `06_KNOWLEDGE_VAULT\03_PROOF_AND_TRANSCRIPTS\`.
3. **Tier 1 + Tier 2 deleted** (~3.6 GB / ~15,500 files), every item verified gone and every keeper verified intact afterward. Deep long-path trees (node_modules, 3 transcript folders) needed robocopy empty-mirror + `rd` — plain Remove-Item cannot reach them (noted for future cleanups).
4. All items now in the shared drive's trash — restorable ~30 days. **Diarized follow-up: spot-check the trash ~2026-08-01 before the window closes.**

Tier 3 items are untouched and remain read-only archive. The rest of this file is preserved below as the audit record of what was approved and why.

---

## How to use this file (original, pre-execution)

Every item below was verified on disk today. Approve per tier — say "approve Tier 1", "approve Tier 2", etc. — and the deletion runs as its own session with this file as the manifest. Items you strike stay put.

**Rescues already done (2026-07-11, before this list was finalized):** the second-pass content review found the first Cowork rescue only read session JSONs and missed the `outputs\` folders. Six unique files were rescued into the AI OS today, so no Tier below is blocked on a rescue:

| Rescued file | Now at |
|---|---|
| MAS_Doc1_Industry_Icons_Deep_Dive_RESCUED.md (35 KB) | `06_KNOWLEDGE_VAULT\04_MARKETING_REFERENCES\` |
| MAS_Coaching_Influencer_Deep_Dive_RESCUED.md (28 KB) | `06_KNOWLEDGE_VAULT\04_MARKETING_REFERENCES\` |
| MAS_Doc2_3Day_Workshop_Adaptation_Playbook_RESCUED.md (29 KB) | `04_AGENT_EDITION_OS\01_WORKSHOP\` (input to pending ruling A7) |
| REI_VSL_Video_Style_Rules_RESCUED.md | `05_CONTENT_MARKETING_ENGINE\00_FOUNDATIONS\` |
| REI_VSL_Pipeline_Recurring_Bugs_RESCUED.md | `05_CONTENT_MARKETING_ENGINE\00_FOUNDATIONS\` |
| YOUTUBE_SCAN_METHOD_RESCUED.md | `08_OPERATIONS\03_AUTOMATIONS\` |

**Recovery net:** everything here lives on the Google Drive shared drive. Deleted files go to the shared drive's trash and are restorable by any content manager for **30 days**; a Workspace admin can restore for roughly **25 further days** via the Admin console. After that, gone for good. Recommendation: run the deletion session, then diarize a +21-day spot-check before the trash window closes.

All paths below are relative to `H:\Shared drives\00_E.C.O.S\`.

---

## TIER 1 — Safe delete (app cache and hash-verified duplicates; no business content)

| # | Path | Size / count | Verified rationale |
|---|---|---|---|
| 1.1 | `_MIGRATION_TO_WINDOWS\claude-config-backup\` | **7,189 files / 479 MB** | Pure Electron/Chromium app state from the old Mac Claude install: IndexedDB, Local/Session Storage, Partitions, shared_proto_db, VideoDecodeStats, sentry, vm_bundles, installed-extension binaries. Spot-checked: the only session-like folder inside (`claude-code-sessions`) is 8 files / 2 MB, and the full session export lives in the sibling `cowork-sessions-and-projects\` (Tier 2.1) — nothing unique here. |
| 1.2 | `deep-buyer-profile.skill` (workspace root, loose file) | 74,274 bytes | SHA256-identical to `Alex Deep Buyer Profiling\deep-buyer-profile.skill` (hash `953754F2…FD42` on both). Keep the Alex-folder copy (it sits with its source materials); delete the loose root copy. |

Tier 1 recovers ~479 MB and 7,190 files.

---

## TIER 2 — Delete after confirmation (superseded, duplicated elsewhere, or empty)

| # | Path | Size / count | Verified rationale |
|---|---|---|---|
| 2.1 | `_MIGRATION_TO_WINDOWS\cowork-sessions-and-projects\` | **1,826 files / 119 MB** | All 22 Cowork sessions content-reviewed today (per-session verdicts in Appendix A). 5 prompts were rescued 2026-07-10; the 6 remaining unique files were rescued today (table above). Everything left is session chatter, app state, duplicates of rescued content, or drafts superseded by current AI OS masters. **Caution note:** `local_ce14d77b…\outputs\REI_GHL_Leads_Import.json` contains real client PII (names/emails/phones). It duplicates live GHL CRM data — not unique — but its presence is why this branch is Tier 2, not Tier 1: confirm you're comfortable trashing a PII file (it stays in Drive trash 30 days). |
| 2.2 | `01_PROPERTY_BUSINESS\01_CLIENT_EDITION\99_ARCHIVE\OLD_OPERATIONS_AND_DASHBOARD_SUPERSEDED_2026-07-04\Codex\` | **6,435 files / 3.02 GB** | The scout report called this "unrelated engineering scratch" — verification found it's more nuanced, but still deletable: see the breakdown below this table. **Testimonial clips rescued 2026-07-11 ✓** — Whiz (107 MB), Mark & Joycelyn (42 MB), Mark & Joycelyn Treasure Purchase2 (77 MB) copied + transcribed into `07_BRAND_AND_PROOF_BANK\08_PROOF_BANK\00_GENERAL_AUTHORITY\` per option B; safe to proceed with deletion once approved. |
| 2.3 | `00_BRAIN\` — the 6 stale non-"(1)" twins: `03_CURRENT_PRIORITIES.md`, `04_DECISION_MEMORY.md`, `05_ACTIVE_PROJECTS.md`, `06_PARKING_LOT.md`, `08_SESSION_TRANSFER_LOG.md`, `09_MIGRATION_AUDIT_LOG.md` | 6 files / ~29 KB | Header-verified: each "(1)" twin is the newer superset (v2.4 APPROVED MASTER vs v2.3 CANDIDATE; session log "(1)" contains 55 of the old file's 56 substantive lines and runs 2 weeks later). One anomaly: `09_MIGRATION_AUDIT_LOG (1).md` is mislabeled "v2.0" in its header but is the later, larger file (batches 004–008 vs 004–006, modified 5:20pm vs 9:07am same day) — the label is wrong, the file is right. All content absorbed into the AI OS Command Center. |
| 2.4 | Empty shell folders (9, zero items each): `Claude Dispatch Files\`; `01_PROPERTY_BUSINESS\02_AGENT_EDITION\` → `99_ARCHIVE`, `06_EXPERIMENTS`, `05_OPERATIONS`, `04_ASSET_BANK`; `01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\` → `99_ARCHIVE`, `02_SHARED_PROOF`, `01_BRAND_ASSETS`, `03_SHARED_RESEARCH\Weekly Ads\REI_Ads_Research_Resources\ARCHIVE` | 0 files | Verified empty (including hidden files). Nothing to lose. |
| 2.5 | `9_ARCHIVE\` | 19 files / 0.35 MB | v2.1–v2.2-era install packs, manifests, and superseded brain files (CLAUDE.md v2.x, master indexes, decision memory). Superseded twice over; the AI OS `99_ARCHIVE` carries the version lineage that matters. Tiny, but it's root-level clutter with no live references. |

### 2.2 Codex breakdown (why it's Tier 2, not Tier 1)

The scout report undersold this folder. Verified contents:

- **`Zoom_Content_Mining\outputs\` — 63 files / 2.80 GB.** 14 Zoom recordings + machine transcripts: REI Method Masterclass sessions, web classes, and **client testimonial/consult videos** (Whiz, Mark & Joycelyn, Kevin & Yuzhen, Christopher, Binu, Joey). This IS business content — but every video was cross-checked against `E:\Zoom Consults - Processed` by filename and byte size: **all are copies; the originals plus all 222 transcripts exist on E:\** (each folder's `SOURCE_FILES.txt` records the E:\ provenance).
- **`Zoom_Content_Mining\.venv_transcribe\` — 6,325 files / 284 MB.** Python virtualenv (numpy, onnxruntime). Pure junk.
- **Loose files — 15 / 4.9 MB.** `REI_AppsScript_v8.21.gs` and `REI_GoogleAds_Script_v3.gs` (superseded by the ACTIVE v8.43 / v8 copies in `08_OPERATIONS\02_SCRIPTS\`), lead-list analysis xlsx/json (superseded by `CONTACT_MASTER_v1.0_2026-07-11.xlsx`, 17,663 contacts — see A9), Chrome-bookmark dashboards (personal scratch). `.git\` and `.agents\` are empty shells.

**The one real decision:** deleting this folder removes the shared drive's only *cloud* copy of those 14 recordings — after deletion they exist solely on the local E:\ drive, which is the exact single-point-of-failure that pending ruling **A5** (E:\ as registered evidence vault + backup) is about. Options:

- **My pick — B:** approve 2.2 together with A5's registered-vault approach, and copy just the 2–3 strongest testimonial clips (Whiz 102 MB, Mark & Joycelyn 40+74 MB) into `07_BRAND_AND_PROOF_BANK\` first — testimonials are proof-bank material and the proof-bank curation chip is already queued. ~220 MB buys cloud safety for the highest-value clips.
- A (fastest): approve as-is; accept E:\-only until A5's backup lands.
- C (safest, costly): copy all 14 recordings (2.8 GB) into the proof bank first.

**Deletion-method note:** 3 subfolders under `outputs\transcripts_by_video_name\` exceed the Windows 260-char path limit and error under normal tools (`2021-03-11 18.09.09…`, `2021-03-11 18.25.37…`, `2022-11-11 23.08.24…`). Verified reachable via a `subst` drive-letter alias — the deletion session must use that (or delete via the Drive web UI), or these folders will be left behind half-deleted.

Tier 2 recovers ~3.14 GB and ~8,286 files.

---

## TIER 3 — Keep as archive (historical or operational value; NOT for deletion)

| Path | Why it stays |
|---|---|
| `_MIGRATION_TO_WINDOWS\` root files + `Scheduled\` | Migration provenance: `COWORK_MIGRATION_HANDOVER.md`, import/export scripts, manifests, global-instructions, `.gdoc` handover docs. Tiny footprint. (The session copy of the handover doc inside 2.1 differs from this root copy by one trivial line — root copy is the keeper.) After Tiers 1–2 execute, this folder shrinks to ~20 small files; fold them into `00_AI_OPERATING_SYSTEM\99_ARCHIVE` in a later pass if root tidiness matters. |
| `00_BRAIN\` (everything except the 6 stale twins in 2.3) | Read-only reference per the constitution. The "(1)" files are the final approved v2.4 brain — the historical record of the pre-AI-OS system. The 7 `.docx` twins in here violate the md-only rule but are part of the frozen historical snapshot; not worth a separate deletion decision now. |
| `01_PROPERTY_BUSINESS\`, `00_COACH_EDMUND_BUSINESS_BRAIN_V1.0\`, `X-Singapore Real Estate Insider - MAS HQ\` | Read-only reference / legacy media archive per the constitution and `07_BRAND_AND_PROOF_BANK` registries. Out of scope for this cleanup. |
| `Alex Deep Buyer Profiling\` | Keeps the surviving `deep-buyer-profile.skill` copy plus source `.docx`/`.gdoc` (their md conversions are pending promotion — see B2 in `10_PENDING_APPROVALS.md`). Revisit only after B2 is promoted. |
| `E:\Zoom Consults - Processed` (local drive) | 382 GB / 3,875 files — the evidence vault. Governed by pending ruling A5, not this list. |

---

## Appendix A — Per-session verdicts for 2.1 (all 22 Cowork sessions + agent/spaces/rpm)

Reviewed 2026-07-11, second pass, reading `outputs\` folders and Space memories, not just session JSONs.

| Session | Topic | Verdict |
|---|---|---|
| local_028f85a3 | "(outdated) MAS agent coaching programme" brainstorm | Junk — user-labeled outdated, no outputs; the influencer deep-dives it chased exist as REF_ files in the Knowledge Vault |
| local_8bfcb449 | Lentor asset bank setup housekeeping | Junk — no outputs |
| local_7fff550c | Google Tasks dedup (Jun 15 snapshot) | Junk — stale cache; live source of truth is Google Tasks itself |
| local_4013e6fd | VSL video feedback | Junk — durable style rules captured via Space memory (rescued) |
| local_1881adab | REI Monday content intelligence | Duplicate of rescued prompt |
| **local_d7845817** | MAS agent coaching programme | **Unique — 3 strategy docs RESCUED today** (see table at top) |
| local_bf86375b | Monday income focus briefing | Duplicate of rescued prompt |
| local_cc932e5d | "Customize Claude to your role" | Junk — plugin catalog dump |
| local_98bf23c3 | X-REI Monday content intelligence | Duplicate of rescued prompt |
| local_9b34f63d | Mac storage cleanup review | Junk — moot post-migration |
| local_80bc00f8 | Rei monday content intelligence | Duplicate — SKILL.md matches rescued prompt verbatim |
| local_35ef77c6 | X-REI Monday Tasks To Income | Junk — one question, no outputs |
| local_f78747e4 | Emails / Calendar / GHL | Near-identical earlier draft of rescued Monday briefing prompt |
| local_44adf842 | Workspace migration (v2.3 Command Center drafts) | Superseded — decisions 016–019 carried into current `04_DECISION_MEMORY.md` |
| local_1723d446 | Cowork Mac→Windows migration | Covered — handover doc + scripts exist at `_MIGRATION_TO_WINDOWS\` root (Tier 3); scripts hash-identical, doc differs by one trivial line |
| local_ce14d77b | REI Ads dashboard build | Superseded (AppsScript v3–v7 vs ACTIVE v8.43). **Contains the PII file noted in 2.1** |
| local_97907f76 | MAS docx builds v3.0 | Superseded — v3.1/v4.0 live in `03_CLIENT_ADVISORY_OS` |
| local_35bb80b9 | X-REI Friday performance report | Duplicate of rescued prompt |
| local_395e9d51 | Project knowledge access test | Junk — literal test session |
| local_a622b666 | "(outdated) Lentor asset bank meta ads" | Junk — user-labeled outdated, superseded dashboard v1 |
| local_95e08805 | MAS Agent Edition business plan build | Superseded — every output exists in `02_AGENT_EDITION` / `04_AGENT_EDITION_OS` / Knowledge Vault |
| local_4a9f2b7e | System audit prompt draft (2026-06-05) | Superseded by `09_AUDIT_AND_MAINTENANCE.md` |
| agent\ ("Ditto") | Agent workspace | Junk/superseded; `master-log-sop.md` memory contradicts Decision 027 (no docx twins) — deleting it removes a drift source |
| spaces\698d9e88 | VSL Space memory | **Unique — 3 memory files RESCUED today** |
| spaces\b8720057 | MAS Agent Edition Space memory | Duplicate — content lives in `04_AGENT_EDITION_OS`; generic preference notes |
| rpm\ | Third-party plugin cache (Zoom etc.) | Junk — published plugin code |

---

## What Edmund decides

1. **Tier 1** — approve? (479 MB app cache + 1 duplicate file; zero risk)
2. **Tier 2** — approve, and for 2.2 pick option A / **B (my pick)** / C on the testimonial clips? (2.1's PII file noted; 2.2 ideally ruled together with A5)
3. **Tier 3** — confirm keep-as-archive (no action)

Once ruled, outcomes go to `04_DECISION_MEMORY.md`, this file's approved tiers become the deletion-session manifest, and this item leaves the pending queue.
