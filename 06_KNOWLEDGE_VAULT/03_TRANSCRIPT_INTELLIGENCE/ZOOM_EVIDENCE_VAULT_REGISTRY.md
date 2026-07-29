Title: ZOOM_EVIDENCE_VAULT_REGISTRY — E:\Zoom Consults - Processed
Version: v1.2
Status: REGISTRY (indexes evidence in place — register, don't migrate)
Date: 2026-07-13
Supersedes: v1.1 (2026-07-12) — backup COMPLETE and verified; status section updated from in-progress to done
Sources: Decision 040 / queue item A5 (ruled by Edmund 2026-07-11, in `00_COMMAND_CENTER\04_DECISION_MEMORY.md` and `10_PENDING_APPROVALS.md`); on-disk structural survey 2026-07-11; O5 backup execution 2026-07-12 (Session Log Entry 026, first pass) + 2026-07-12/13 (Entry 027 resume + Entry 028 completion/verification)

---

## ✅ Backup status (updated 2026-07-13) — COMPLETE & VERIFIED

**Backup COMPLETE.** Per Decision 052/068/072.5, a full copy of this vault now exists at `H:\Shared drives\00_E.C.O.S\ZZ_BACKUP_E_ZOOM_CONSULTS\` (admin@thereimethod.com Workspace pool, Google Drive Streaming mode).

- **Local copy verified exact:** destination file count and total bytes match this registry's source numbers precisely — **3,875 files / 410,415,312,554 bytes (382.2 GB)**, folder count matches (593 dirs incl. root vs 592 sub-dirs counted at destination — a counting-convention difference of exactly 1, not a missing folder).
- **MD5 spot-check: 10/10 files matched** byte-for-byte between E:\ source and the Drive copy, sampled across the full date range (2021–2023) plus the `Transcripts\` and hidden-config folders.
- **Cloud-upload completion verified** via Google Drive's own sync-engine log (`drive_fs.txt`): the last sync-engine status report after the copy finished showed `operation_queue_size: 0`, `active_uploads: 0`, `change_ids_up_to_date: true` — nothing left pending upload. (Verified by log inspection, not a manual Drive-tray/web-UI look — Edmund can spot-check the web UI for extra assurance if desired.)
- Full detail: `ZZ_BACKUP_E_ZOOM_CONSULTS\_BACKUP_MANIFEST.md`.

**E:\ remains the source of record and was never modified.** This Drive copy is the disaster-recovery backup, not a replacement — E:\ stays read-only and primary. Queue item O5 closed in `00_COMMAND_CENTER\10_PENDING_APPROVALS.md`.

---

## The ruling (Decision 040, Edmund, 2026-07-11)

> "E:\ Zoom evidence (382GB) is a registered vault, not migrated. Only cited text excerpts copy into `06_KNOWLEDGE_VAULT\03_PROOF_AND_TRANSCRIPTS\CITED_EVIDENCE\`. E:\ needs a backup (flagged). Codex duplicate videos thereby safe to delete."

Practical effect:
- `E:\Zoom Consults - Processed` stays exactly where it is. It is **registered**, not copied into the Shared Drive.
- Only the **specific text excerpts cited** by Knowledge Vault CANDIDATE files get physically copied into this Drive, into `CITED_EVIDENCE\` below.
- Video/audio citations are **registered by exact path only** — never copied (too large; 382 GB total, 900 MP4 + 564 M4A files alone account for ~376 GB).
- Read-only source. Nothing on E:\ is modified, moved, or deleted by this process.

---

## What the vault holds

`E:\Zoom Consults - Processed` — local Windows drive, **382 GB, 3,875 files, 560 top-level folders**.

### Structure map (top 2 levels)

| Folder type | Count / size | Contents |
|---|---|---|
| **~550 dated consult session folders** (`YYYY-MM-DD HH.MM.SS <client/topic> <zoom-meeting-id>`, a few undated e.g. `Mark Jocelyn Treasure Purchase1`) | bulk of the 382 GB | Raw Zoom export per session: `.mp4` (multiple resolution/gallery/speaker-view variants), `.m4a` audio, `.vtt` captions, `.json`/`.conf` metadata, `.csv`/`.m3u` playlist/index files, `.png`/`.jpg` thumbnails |
| `Transcripts\` | 490 files, 32.8 MB | One `.md` transcript per consult session, filename matches the session folder name — the primary TEXT layer over the raw media |
| `_CONSULT_INTELLIGENCE_OS\` | 225 files, 13.7 MB | Prior AI analysis pass, 10 subfolders: `00_SYSTEM_RULES`, `01_PER_CONSULT_EXTRACTS`, `02_MASTER_INDEX`, `03_CLIENT_LANGUAGE_VAULT` (cited — see below), `04_OBJECTION_BANK`, `05_WINNING_RESPONSES`, `06_CONSULT_GAPS_AND_WEAK_MOMENTS`, `07_CONSULT_FLOW_IMPROVEMENT`, `08_PRESENTATION_IMPROVEMENT`, `09_FOLLOW_UP_LIBRARY` |
| `_TRANSCRIPT_AUDIT\` | 17 files, 0.95 MB | Working files from the transcript-processing project: `PHASE2_EXTRACTS\` (cited — see below), `transcript_inventory.md` (cited), grouping summaries, candidate docs, processing scripts |
| `_non_media_leftovers\` | 182 files, 985 MB | Unclassified leftover images/data not filed into a session folder |
| `.claude`, `(done)-.claude` | 1 file each | Leftover Claude Code config (`settings.local.json`) — not evidence data |
| `__pycache__` | 1 file | Python cache junk |

### File type breakdown (whole vault)

| Type | Count | Size | Note |
|---|---|---|---|
| `.mp4` | 900 | 332.9 GB | Video — largest share |
| `.m4a` | 564 | 42.8 GB | Audio-only recordings |
| `.md` | 935 | 0.06 GB | Transcripts + intelligence extracts — TEXT |
| `.zoom` | 17 | 5.4 GB | Zoom proprietary recording files |
| `.conf`/`.json`/`.vtt`/`.csv`/`.txt`/`.m3u`/`.png`/`.jpg`/other | ~1,459 | ~1.1 GB | Metadata, captions, thumbnails, indexes |

**Date range:** consult sessions run **2020-05-17 → 2024-03-15**. (A few `_CONSULT_INTELLIGENCE_OS` processing files carry later modified dates from prior AI passes — those are metadata artifacts, not consult dates.)

**Transcripts vs media:** 490 consult transcripts (`Transcripts\*.md`) are the primary text evidence layer; video (900 files) and audio (564 files) are the source recordings behind them. `_CONSULT_INTELLIGENCE_OS` holds a further 225-file distilled-intelligence layer on top of the transcripts (objections, winning responses, client language, gaps).

---

## Access note

- **Location:** local `E:\` drive on the Windows machine running this session. **NOT in Google Drive**, not synced, not shared — inaccessible to anyone without physical/network access to this machine.
- **Read-only source for AI OS purposes.** Nothing in this process writes to, moves, or deletes anything under `E:\Zoom Consults - Processed`.
- **Single-copy risk:** see backup reminder at top of this file.

---

## Cited-excerpt migration — executed 2026-07-11

Two Knowledge Vault CANDIDATE files cite E:\ sources directly:
- `06_KNOWLEDGE_VAULT\03_PROOF_AND_TRANSCRIPTS\MAS_CONSULT_BLUEPRINT_REVERSE_ENGINEERED_v1.0_CANDIDATE.md`
- `06_KNOWLEDGE_VAULT\02_BUYER_PSYCHOLOGY\VOICE_OF_CLIENT_EVIDENCE_ANNEX_v1.0_CANDIDATE.md`

All cited E:\ sources are TEXT (no video/audio was cited by exact path). All 3 cited paths existed and were copied in full — well under the 200 MB cap (799 KB total).

| Cited path | Type | Copied to `CITED_EVIDENCE\` |
|---|---|---|
| `E:\Zoom Consults - Processed\_TRANSCRIPT_AUDIT\PHASE2_EXTRACTS\` (6 files) | folder of extraction docs | `extract_A_ethan_kat.md`, `extract_B_mindy_teoskye.md`, `extract_C_paul_rachel.md`, `extract_D_jeannie_eliza.md`, `extract_E_taught_process.md`, `extract_F_unfair_sales.md` |
| `E:\Zoom Consults - Processed\_TRANSCRIPT_AUDIT\transcript_inventory.md` | file | `transcript_inventory.md` |
| `E:\Zoom Consults - Processed\_CONSULT_INTELLIGENCE_OS\03_CLIENT_LANGUAGE_VAULT\CLIENT_LANGUAGE_VAULT.md` | file | `CLIENT_LANGUAGE_VAULT.md` |

**Total: 8 files, 799 KB.** No broken citations — all 3 cited E:\ paths resolved and existed on disk.

Individual verbatim quotes in both CANDIDATE files cite specific consult transcripts by client/date name (e.g. *"2021-07-13 Karan 1st Consult"*) rather than a literal `E:\` path — these resolve to `Transcripts\<name>.md` in the vault and are covered by this registry, not individually copied (copying all 490 transcripts is out of scope for a "cited excerpt" migration; the deep-read set of 25 transcripts + PHASE2_EXTRACTS above is the actual evidence layer the blueprint was built from).

---

## How future files should cite this vault

Any new AI OS file that references Zoom consult evidence must:
1. Cite the **exact E:\ path** (e.g. `E:\Zoom Consults - Processed\Transcripts\2022-07-26 Mindy 1st consult.md`), not a folder-level generality.
2. Cite the **date of verification** — the date the citing author confirmed the file exists at that path (drift risk: E:\ is unmanaged local storage).
3. If the citation is a TEXT file and will be quoted/relied on repeatedly, copy it into `CITED_EVIDENCE\` (same rule this file executed) and note the copy in this registry's table above.
4. If the citation is video/audio, register the exact path only — do not attempt to copy.
5. If the cited path cannot be verified at write time, mark it **BROKEN CITATION** inline and flag it here rather than silently dropping it.

---

## READS FROM
- `E:\Zoom Consults - Processed` (the physical vault, read-only)

## FEEDS INTO
- `03_PROOF_AND_TRANSCRIPTS` consult-blueprint work, `02_BUYER_PSYCHOLOGY` voice-of-client work, `07_BRAND_AND_PROOF_BANK` proof harvesting, workshop case material
