# FOLDER E.C.O.S. FINAL ARCHITECTURE DECISION REPORT

| | |
|---|---|
| **Version** | v1.0 |
| **Status** | APPROVED MASTER — Controlled Hybrid ratified by Edmund in chat, 2026-07-16 (Decision 093). This report is the migration blueprint. |
| **Date** | 2026-07-16 |
| **Sources** | 5-scout read-only audit, 2026-07-16 (Scouts A–E); root CLAUDE.md v4.3; Decision Memory 084/090/091; Operating Agreement (59 rules) |
| **Scope** | Read-only assessment. No workspace file was modified in producing this report. |

---

## 1. EXECUTIVE VERDICT

**APPROVE WITH REQUIRED CHANGES — as a CONTROLLED HYBRID, not the full proposal.**

In plain English: **Edmund's instinct is right, but his proposed method is too big.** He has correctly spotted two real, serious problems — client data (PII) is sitting in a folder built to be shared, and campaign work is scattered across four different places so nobody knows where a campaign lives. Those must be fixed. But the *way* he proposes to fix them — renaming the nine Asset Library categories he personally ratified three days ago, and rebuilding the whole top level for the third time in six days — would create more disruption than value and re-open the exact "we keep sorting folders" loop he told us to stop (Operating Agreement rules 52/54/59).

**Is another full rebuild justified? No.** A full rebuild (the literal proposal, "Option B") scores **5.98/10**. It loses most of its points to migration churn, a heavier campaign template than a solo owner can sustain, and renaming just-learned folders for little functional gain. The current state as-is ("Option A") scores **4.35/10** — it is genuinely broken in the two ways that matter (privacy and campaign fragmentation) and cannot simply be left alone. The **Controlled Hybrid ("Option C") scores 7.75/10** and wins decisively: it keeps everything Edmund just ratified, changes only what is provably broken, and can be done in small reversible steps.

**What the Hybrid actually does:**
1. **Keep** the current root and the nine Asset Library categories (owner-ratified 3 days ago — do not rename them).
2. **Add** one new root area for private client data — but only if it gets a *real* Google permission boundary (a separate restricted Shared Drive), because a "PRIVATE" folder inside the one shared drive everybody can already see is cosmetic (Scout D).
3. **Add** one campaign workbench that *explicitly retires and absorbs* the other four campaign locations — otherwise it just becomes a fifth.
4. **Move** the 640 MB of images out of the AI brain (they violate the brain's own rule).
5. **Fix** the pre-existing bugs (broken `/desk` routing, a scheduled task about to fail on 2026-07-20, stale governance docs) — these are urgent regardless of any restructure.

**Freeze after? Yes — hard.** Once the Hybrid moves are done and validated, declare a **90-day architecture freeze** (to ~2026-10-16). No new top-level folders, no renames, no re-org without a logged change request meeting evidence thresholds. This is the guardrail that lets Edmund keep his 07-14 promise to himself: foundation is done, the next 90 days are **revenue**.

**One hard gate:** if Edmund will *not* stand up a separate restricted Shared Drive for PII, then the `02_CLIENTS_AND_CONTACTS_PRIVATE` folder should **not** be created at all — a private-labelled folder without a real lock is security theatre and would give false comfort about a 22,069-row contact database. In that case, consolidate the PII in place, restrict who has the drive link, and treat the separate-drive decision as the #1 open question.

---

## 2. CURRENT-STATE FINDINGS (what physically exists vs what the docs claim)

The workspace is in reasonable shape structurally, but its **map is out of date with its territory**. The documents that are supposed to keep everyone oriented are the most drifted (Scout A, obs. 7). Verified physically on 2026-07-16:

- **Root** contains: `.claude`, `00_AI_OPERATING_SYSTEM`, `01_ASSET_LIBRARY`, `Artifacts`, `_ARCHIVE`, `_BACKUPS`, plus `CLAUDE.md`, `PROJECT_LOCATIONS.md`, `START_HERE.md`. **`_DEL` does not exist. `X-Singapore Real Estate Insider - MAS HQ` does not exist at root** — both are still described as live by the front-door docs.
- **The AI OS branch the docs call `01_AI_TEAM` is physically named `01_E.C.O.S`.** This is not a cosmetic doc typo: the `/desk` skill (the core mechanism that routes any business task to the right desk) reads the non-existent `01_AI_TEAM` path. **Routing is broken today** (Scout A contradiction 3, Critical; confirmed by direct listing).
- **9 of 12 AI OS branches are clean and healthy** (Positioning/IP, Client Advisory OS, Agent Edition OS, Knowledge Vault, Brand & Proof Bank, Marketing OS, Sales OS scaffold, Command Center, Archive). The problems are concentrated, not systemic (Scout B).
- **640 MB of media (341 PNGs, 36 CSVs, 4 XLSX) physically live inside the AI brain** at `05_CONTENT_MARKETING_ENGINE`, whose own `_INDEX` claims these files are "registered, NOT copied." They are copied. This violates the brain's own rule 9.7 and the root CLAUDE.md (Scout B).
- **73 MB of raw contact data + Python pipeline + `__pycache__` live in the brain** at `08_OPERATIONS\06_CONTACT_MASTER` — the single most sensitive data location, and the *least* labelled (no PII banner) (Scout B, Scout D obs. 3).
- **A 22,069-row PII master CSV, 173 exports, and 23 cleanup scripts sit in the Asset Library** at `09_CLIENT_DATA` — a library whose stated purpose is browsable, shareable creative assets (Scout C, Scout D). This is the single biggest scope violation in the workspace.
- **Zero consent/release records exist anywhere**, despite the written policy requiring PDPA consent before using client proof; the Proof Bank index flags this against itself (Scout D).
- **Campaign work is split across four claimant locations with zero cross-references** and the most obvious folder (`10_MARKETING_OS\08_CAMPAIGNS`) is empty — a filing trap (Scout C).
- **A scheduled task will fail on 2026-07-20**: four local scheduled-task files still point at `H:\Shared drives\Claude Workspace\...`, a path that stopped existing on 07-14. They live outside the Drive tree so the rename never reached them (Scout E, severity 5, LIVE).
- **A plaintext GHL API token** sits in `02_POSITIONING_AND_IP\01_DIAGNOSTIC_APP\CREDENTIALS_REGISTRY.md` (Scout E) — pre-existing, self-flagged for rotation.

**Contradiction register:** see Appendix D. **Dependency register:** Appendix E.

---

## 3. CURRENT vs PROPOSED vs HYBRID SCORECARD

Weighted 0–10 per criterion. Weights are fixed by the brief and were **not** adjusted to favour any option. "Conf." = confidence in the score given the evidence (H/M/L).

**Option A = Current state as-is. Option B = the full proposal (new 02_ + 03_ roots, rescope 00/01, rename the 9 library categories). Option C = Controlled Hybrid (keep root + 9 categories; add permissioned private area + one campaign workbench; move media; fix bugs).**

| # | Criterion | Wt | A raw | B raw | C raw | Conf. | Evidence basis |
|---|---|---|---|---|---|---|---|
| 1 | Human usability | 15% | 5 | 6 | 8 | M | A: 4 campaign homes + phantom paths confuse. B: cleaner model but 3rd re-org in 6 days disorients a non-technical owner + renames just-learned folders. C: keeps familiar library, adds 2 clear homes. |
| 2 | Claude retrieval | 12% | 4 | 7 | 8 | H | A: `/desk` broken, indexes 3 re-orgs stale. B: cleaner only after full index rewrite (churn). C: fixes routing + stale indexes, clean homes, minimal rewrite. |
| 3 | Daily campaign execution | 14% | 3 | 7 | 8 | H | A: 4 claimants, empty CAMPAIGNS trap. B: single workbench good but risks a 5th home unless others retired. C: one workbench that explicitly supersedes the other 4. |
| 4 | Asset management | 8% | 7 | 6 | 8 | H | A: library clean (7/9 categories) but 06/09 scope violations. B: renaming 9 just-built categories = pure churn, little gain. C: keeps categories, fixes only 06/09. |
| 5 | Client-data privacy | 10% | 2 | 5 | 8 | H | A: PII in shareable library, no ACL, no consent. B: private root aids discovery but WITHOUT a real ACL is cosmetic (Scout D). C: extract PII to a separately-permissioned drive + consent register. |
| 6 | Source-of-truth clarity | 8% | 3 | 7 | 8 | M | A: 3 contact homes, 4 campaign homes, no written CRM policy. B: consolidates if fully executed. C: consolidates + writes GHL-as-truth policy. |
| 7 | Owner editability | 7% | 6 | 5 | 8 | M | A: familiar. B: 10-subfolder campaign template too heavy for a solo owner. C: minimal change + lighter template. |
| 8 | Team collaboration | 6% | 5 | 5 | 7 | M | A/B: still one shared drive, no boundary. C: separate restricted drive gives a real PII boundary. |
| 9 | Automation / path stability | 6% | 3 | 4 | 7 | H | A: live scheduled-task bug + phantom paths. B: big-bang moves risk breaking 5 pipelines + MAX_PATH. C: fix bug first, staged moves, repoint pipelines. |
| 10 | Searchability | 5% | 5 | 7 | 8 | M | A: media-in-brain pollutes brain search. B/C: cleaner; C isolates PII + evicts media. |
| 11 | Scalability | 5% | 3 | 8 | 7 | M | A: campaigns/PII don't scale. B: most scalable structure. C: workbench + private area scale well (slightly less formal than B). |
| 12 | Migration cost / disruption | 4% | 10 | 2 | 6 | H | A: zero (exists). B: full rebuild #3 in 6 days = maximum churn. C: targeted, reversible, staged moves. |

### Weighted totals

| Criterion (weight) | A weighted | B weighted | C weighted |
|---|---|---|---|
| Human usability (15%) | 0.75 | 0.90 | 1.20 |
| Claude retrieval (12%) | 0.48 | 0.84 | 0.96 |
| Daily campaign execution (14%) | 0.42 | 0.98 | 1.12 |
| Asset management (8%) | 0.56 | 0.48 | 0.64 |
| Client-data privacy (10%) | 0.20 | 0.50 | 0.80 |
| Source-of-truth clarity (8%) | 0.24 | 0.56 | 0.64 |
| Owner editability (7%) | 0.42 | 0.35 | 0.56 |
| Team collaboration (6%) | 0.30 | 0.30 | 0.42 |
| Automation / path stability (6%) | 0.18 | 0.24 | 0.42 |
| Searchability (5%) | 0.25 | 0.35 | 0.40 |
| Scalability (5%) | 0.15 | 0.40 | 0.35 |
| Migration cost (4%) | 0.40 | 0.08 | 0.24 |
| **FINAL /10** | **4.35** | **5.98** | **7.75** |

**Reading of the numbers:** The current state (4.35) is not acceptable — it fails privacy, campaign execution, and source-of-truth, which together carry 32% of the weight. The full proposal (5.98) is a real improvement but bleeds points to migration churn (0.08 vs A's 0.40) and owner burden. The **Hybrid (7.75)** wins on 10 of 12 criteria and is the only option that fixes the real problems *without* triggering a third full rebuild. The gap between B and C (1.77 points) is driven almost entirely by disruption, editability, and keeping the just-ratified library intact.

---

## 4. EVIDENCE-BASED ADVANTAGES OF THE PROPOSED ARCHITECTURE

The proposal is not wrong-headed — its diagnosis is largely correct. Genuine strengths worth carrying into the final design:

1. **It names the privacy problem out loud.** A dedicated `02_CLIENTS_AND_CONTACTS_PRIVATE` with an `00_ACCESS_RULES` sub-folder is the first document in this workspace to treat client data as a distinct, governed thing. Scout D confirms PII is currently smeared across five unrelated trees with inconsistent labelling — a single home genuinely improves discoverability and auditability.
2. **It separates knowledge from execution.** Rescoping `00` to "brain only — no bulk media/PII" is exactly right and directly fixes the 640 MB-in-brain and 73 MB-PII-in-brain violations (Scout B). This is the strongest single idea in the proposal.
3. **It gives campaigns one home with a lifecycle.** `03_ACTIVE_CAMPAIGNS` with inbox → active → scheduled → completed → archive, and a self-contained per-campaign folder, is the correct shape for the daily revenue work Decision 090 pivoted to. Today a campaign is split across four systems with zero cross-refs (Scout C); one workbench is a real fix.
4. **It builds a consent surface.** `06_CLIENT_PROOF_CONSENT` finally creates a place for the consent records that currently exist nowhere (Scout D) — a live PDPA exposure.
5. **The `04_IMPORT_EXPORT_STAGING` / `05_DATA_CLEANUP_PROJECTS` split** matches how the data actually flows — the existing `CONTACT_CLEANUP_REBUILD_2026-06-25` staged pipeline is already the good model (Scout D, risk-3 vs the risk-4 raw dumps around it).
6. **`03_APPROVED_PROOF` vs raw** is the right instinct — `02_TESTIMONIALS_PROOF` today has no approved/raw distinction and zero consent gating (Scout C).

The Hybrid keeps advantages 1–6. It declines only the parts that cost more than they return (Section 5).

---

## 5. WEAKNESSES / RISKS IN THE PROPOSED ARCHITECTURE

Challenging the proposal directly. Each of these is why the recommendation is Hybrid, not full-B.

1. **Renaming the 9 just-built library categories is churn for its own sake.** Edmund personally ratified `01_PHOTOS / 02_TESTIMONIALS_PROOF / 03_BRAND_ASSETS / …` three days ago under an explicit "real files, no registries" ruling (Decision 084). The proposed rename to `01_BRAND_ASSETS / 02_PEOPLE_AND_TEAM_PHOTOS / 03_APPROVED_PROOF / …` reorders and relabels 12,800+ files with **no functional gain** — the same assets in the same shape under different names. It also re-teaches muscle memory the owner just learned. **Every file move on Google Drive for Desktop risks delete+create semantics and shortcut breakage** (Scout E, risk 3). This is the single weakest part of the proposal.
2. **A "PRIVATE" folder without a real ACL is cosmetic — possibly worse than nothing.** The entire workspace is *one* Google Shared Drive; access is drive-level. Google Shared Drives do not do clean per-sub-folder permissions (Scout D obs. 2). A folder named `..._PRIVATE` with a `RESTRICTED` text banner enforces nothing — marketing-asset access still equals PII access still equals 410 GB of consult-recording access. Worse, the label may create false confidence that the 22,069-row database is "handled" when it is not. **The real fix is a separate restricted Shared Drive**, not a folder rename.
3. **`03_ACTIVE_CAMPAIGNS` becomes a *fifth* campaign home unless the other four are explicitly retired.** Today: `01_ASSET_LIBRARY\06_CAMPAIGN_OUTPUTS`, `05_CME\01_CAMPAIGN_LEGACY_LAUNCH`, `10_MARKETING_OS\08_CAMPAIGNS`, and the deprecated `07_BRAND_AND_PROOF_BANK` all plausibly hold campaign work (Scout C). Adding a new root without a **written supersession + repoint** just deepens the fragmentation the proposal set out to solve. This is the make-or-break condition.
4. **The 10-subfolder campaign template (00_CAMPAIGN_BRIEF … 09_RESULTS_AND_LEARNINGS) is too heavy for a solo, non-technical owner.** Ten nested folders per campaign, created for every `YYYY-MM_Name_Channel_Wave`, is enterprise ceremony. It will either be half-filled or abandoned — and the current `10_MARKETING_OS\08_CAMPAIGNS` being empty is direct evidence that ceremony without adoption produces empty folders. **Windows MAX_PATH** is also a live constraint: existing paths already run 100+ chars (Scout E, risk 2); `H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-07_LegacyLaunch_Meta_Wave3\09_RESULTS_AND_LEARNINGS\...` risks breaking the deepest files.
5. **It's the third architecture change in six days.** Decision 090 (07-14) declared the foundation DONE and pivoted to revenue; Operating Agreement rules 52 (break-the-loop), 54 (tie-to-business-goal), 59 (build-to-use) all point away from another rebuild. The docs from re-org #2 have not even caught up yet (Scout A obs. 4). A full third rebuild spends the owner's patience on folders, not on the 7,000 GHL contacts waiting to be worked.
6. **Big-bang execution risks the concentrated fragile surface.** Ten operationally fragile files (5 pipeline `.py`, 4 scheduled-task `.md`, 1 automation mirror — Scout E) plus the live 2026-07-20 bug mean a simultaneous mass move could break automation mid-flight. The fragile surface is small and clustered, which *favours* a staged approach and *penalises* big-bang.

---

## 6. BEST FINAL ARCHITECTURE (Controlled Hybrid — minimal-viable)

Top-level tree. **Bold = new. Everything else stays exactly as it is today.**

```
H:\Shared drives\00_E.C.O.S\                (Shared Drive #1 — general / non-PII)
├── .claude\                                 (unchanged; fix skill paths inside)
├── 00_AI_OPERATING_SYSTEM\                  (brain — rescoped: no bulk media, no raw PII)
├── 01_ASSET_LIBRARY\                        (unchanged 9 categories; fix 06 + 09 scope only)
├── 03_ACTIVE_CAMPAIGNS\   ← NEW             (the ONE campaign workbench; supersedes 4 others)
├── Artifacts\                               (unchanged)
├── _ARCHIVE\                                (unchanged)
├── _BACKUPS\                                (unchanged; 410 GB consult recordings live here)
├── _QUARANTINE\           ← NEW (optional)  (replaces the vanished _DEL as a logged review pen)
├── CLAUDE.md / START_HERE.md / PROJECT_LOCATIONS.md   (updated to match reality)

H:\Shared drives\00_E.C.O.S_CLIENTS_PRIVATE\ ← NEW (Shared Drive #2 — RESTRICTED membership)
└── 02_CLIENTS_AND_CONTACTS_PRIVATE\
    ├── 00_ACCESS_RULES\
    ├── 01_ACTIVE_CLIENTS\
    ├── 02_PAST_CLIENTS\
    ├── 03_MASTER_CONTACT_DATABASE\          (single canonical export home; GHL is live truth)
    ├── 04_IMPORT_EXPORT_STAGING\
    ├── 05_DATA_CLEANUP_PROJECTS\            (absorbs CONTACT_CLEANUP_REBUILD + py pipeline)
    ├── 06_CLIENT_PROOF_CONSENT\             (the consent register)
    └── 99_ARCHIVE\
```

Design decisions and rationale:

- **Number the new campaign area `03_` and the private area `02_` conceptually**, but the private area physically lives on a **separate Shared Drive** (name it clearly, e.g. `00_E.C.O.S_CLIENTS_PRIVATE`). The `02_` numbering is retained as the folder name inside that drive so Edmund's mental model and the proposal's naming survive. This is the one place we accept the proposal's structure wholesale — because privacy is the highest-severity finding.
- **Do NOT rename the 9 Asset Library categories.** Keep `01_PHOTOS … 09_CLIENT_DATA` exactly. Two surgical changes only: (a) move `09_CLIENT_DATA`'s contents into the new private drive and retire the folder; (b) resolve `06_CAMPAIGN_OUTPUTS` — its finished, reusable outputs stay as evergreen assets, its *working* files move to `03_ACTIVE_CAMPAIGNS`.
- **`03_ACTIVE_CAMPAIGNS`** uses the proposal's lifecycle (`00_CAMPAIGN_INBOX / 01_ACTIVE / 02_SCHEDULED / 03_COMPLETED / 99_ARCHIVE`) but a **lighter per-campaign template** (Section 13): 4–5 sub-folders, not 10.
- **`_QUARANTINE`** replaces the mystery of the vanished `_DEL` with a *logged* review pen (nothing deleted without a Decision entry — Operating Agreement rules 39/43).
- **AI OS internals stay as-is** except the media eviction and the path/label fixes. 9 of 12 branches are already clean; do not touch them (Section 7).

This is minimal-viable: **two new homes, two surgical library edits, one media eviction, a handful of doc/path fixes.** No mass rename, no third rebuild.

---

## 7. WHAT SHOULD STAY UNCHANGED (protect these)

9 of 12 AI OS branches are clean (Scout B). Protect the intellectual property and the working system:

| Protect | Why |
|---|---|
| `02_POSITIONING_AND_IP` (SPL spine, 64 files) | Core IP — The Second Property Ladder / Market Maker Method. Clean. |
| `03_CLIENT_ADVISORY_OS` (39 files) | MAS client brain. Clean. |
| `04_AGENT_EDITION_OS` (43 files) | Market Maker agent edition. Clean. |
| `06_KNOWLEDGE_VAULT` (53 files) | Market intel, briefs. Clean. |
| `10_MARKETING_OS` content (117 files, healthiest branch) | Marketing OS knowledge. Clean. |
| `11_SALES_OS` scaffold (167 files, 56% intentional stubs) | Documented intent (Decision 051.4). Leave the scaffold. |
| `00_COMMAND_CENTER` core docs (MASTER_INDEX, DECISION_MEMORY, PENDING_APPROVALS, OPERATING_AGREEMENT) | Load-bearing governance. Keep — just update stale references. |
| The 9 Asset Library category names | Owner-ratified 3 days ago (Decision 084). Renaming = pure churn. |
| Decision Memory + Operating Agreement (the record) | Never a decision surface, but the durable record. Protect. |

**Guiding rule:** the assessment is a *path-integrity and privacy* fix, not a redesign (Scout B verdict). If a branch isn't named in Sections 8–11, it is not to be touched.

---

## 8. WHAT MUST BE MOVED (folder-by-folder; DO NOT perform — proposal only)

| # | Source (current) | Destination | Reason |
|---|---|---|---|
| M1 | `01_ASSET_LIBRARY\09_CLIENT_DATA\` (222 files, 22,069-row PII master + 173 exports + 23 scripts) | Private drive → `03_MASTER_CONTACT_DATABASE\` (exports), `05_DATA_CLEANUP_PROJECTS\` (scripts) | Biggest scope violation: raw PII + code in a shareable library (Scout C/D). |
| M2 | `08_OPERATIONS\06_CONTACT_MASTER\` (33 files, 7,314-row import, CONTACT_MASTER v1.0–1.3, 73 MB) | Private drive → `03_MASTER_CONTACT_DATABASE\` | Most sensitive location, least labelled; PII does not belong in the brain (Scout B/D). Repoint the 4 pipeline `.py` DIR/OUTDIR (see Sec. 10). |
| M3 | `05_CONTENT_MARKETING_ENGINE\...\03_IMAGES_BEST_OF / 04_IMAGES_REJECTED / 05_AD_CREATIVE_AUDIT_RESCUED` (341 PNGs, ~574 MB of the 640 MB) | `01_ASSET_LIBRARY` (best-of → evergreen media; rejected/audit → `_ARCHIVE` or `_QUARANTINE`) | 640 MB media violates brain rule 9.7 + root CLAUDE.md (Scout B). |
| M4 | `01_ASSET_LIBRARY\06_CAMPAIGN_OUTPUTS\` working files (subset of 542 files) | `03_ACTIVE_CAMPAIGNS\` (per campaign) | Working files are execution, not evergreen assets (Scout C). Finished reusable outputs STAY. |
| M5 | `05_CME\01_CAMPAIGN_LEGACY_LAUNCH\` briefs/matrices/scripts (391 files, non-media) | `03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-XX_LegacyLaunch_...\` | Consolidate the campaign currently split across 2 systems with zero cross-refs (Scout C). |
| M6 | `_BACKUPS\ZZ_BACKUP_E_ZOOM_CONSULTS\` (410 GB, folder names = real client names) | Stays in `_BACKUPS`, but **the drive-level access question applies** — this is risk-5 PII | Confirm who can see this drive (Scout D). No move; access review. |

**Sequencing rule:** M6 access review and the private drive (Section 12) must exist *before* M1/M2 move any PII. Never move PII into a folder that isn't yet permissioned.

---

## 9. WHAT MUST BE REWRITTEN (genuinely — separate from path updates)

**Default answer: very little.** Almost everything is a move or a path update, not a rewrite. Genuine content rewrites:

1. **Constitution §9.7** ("bulk media = register, not copied") — actively contradicts Decision 084. Rewrite to reflect real-files reality. *(Scout A contradiction 4, High — live rule is wrong.)*
2. **`03_CURRENT_PRIORITIES.md`** (v3.0, 6 days stale) — still frames "build the AI OS" as the priority; Decision 090 pivoted to revenue. Rewrite the priorities. *(Scout A contradiction 7.)*
3. **Two new short policy docs** (net-new, not rewrites): `00_ACCESS_RULES` (who may see the private drive) and the **GHL-as-source-of-truth policy** (currently written nowhere — Scout D). ~1 page each.
4. **`09_AUDIT_AND_MAINTENANCE.md`** — checks "do all 10 branches exist?" against a 12-branch system; the audit is unsatisfiable as written. Light rewrite. *(Scout A contradiction 6.)*
5. **`02_OPERATING_RULES.md`** — substantively superseded by the Operating Agreement but still marked APPROVED MASTER. Either demote to "superseded, see Operating Agreement" (1 line) or reconcile. Not a full rewrite.

Everything else in Sections 8/10/11 is mechanical.

---

## 10. WHAT REQUIRES PATH UPDATES (dependency register — Scout E)

These are find-and-replace edits, not rewrites. Ordered by severity.

| # | File(s) | Current ref | New ref | Severity |
|---|---|---|---|---|
| P1 | 4 scheduled-task SKILL.md in `C:\Users\Admin\.claude\scheduled-tasks\` | `H:\Shared drives\Claude Workspace\...` | `H:\Shared drives\00_E.C.O.S\...` | **5 — LIVE, fires 2026-07-20. FIX BEFORE ANYTHING ELSE.** |
| P2 | `.claude\skills\desk\SKILL.md` + constitution §5 + MASTER_INDEX §2/§4 + root CLAUDE.md skills map | `01_AI_TEAM\` | `01_E.C.O.S\` | **Critical — routing broken today.** |
| P3 | PIPELINE `01_normalize.py`, `03_suppression.py` | SRC = `X-MAS HQ\02_CLIENTS\...` | new private-drive path | 4 |
| P4 | 4 PIPELINE `.py` (DIR/OUTDIR) | `08_OPERATIONS\06_CONTACT_MASTER` | new private-drive `03_MASTER_CONTACT_DATABASE` | 4 (only if M2 executed) |
| P5 | Root CLAUDE.md, START_HERE.md | list `X-MAS HQ` live + `_DEL` extant | remove / correct | 3 (High as governance) |
| P6 | MASTER_INDEX retrieval guide | asset lookups → `07_BRAND_AND_PROOF_BANK` archived-path registries | → `01_ASSET_LIBRARY` | 3 |
| P7 | 5 pointer registries in `07_BRAND_AND_PROOF_BANK` | `X-MAS HQ\05_ASSET_BANK` | archived note or `01_ASSET_LIBRARY` | 3 (docs only) |
| P8 | `04_CONTACT_DATABASE_REGISTRY.md` v1.4, `06_CONTACT_MASTER\_INDEX` v1.6 | cite `X-MAS HQ\02_CLIENTS` as legacy master | correct to private drive | 3 (stale pointer) |
| P9 | 5 automation docs in `03_AUTOMATIONS` + `08_OPERATIONS\_INDEX` | `01_PROPERTY_BUSINESS` / root `Scheduled\` | confirm live? then fix/remove | 2–3 (see Appendix I) |
| P10 | `.claude\settings.local.json` | ~15 stale permission entries | prune | 1 (cosmetic) |

**Confirmed path-SAFE (no action):** Apps Script `.gs` (Sheet/deployment IDs), diagnostic `WEBHOOK_URL`, the `09_CLIENT_DATA` py scripts (relative/argv) (Scout E, severity 0).

---

## 11. WHAT SHOULD BE ARCHIVED

| Item | Destination | Reason |
|---|---|---|
| `05_CME\...\04_IMAGES_REJECTED` (129 files, ~264 MB) | `_ARCHIVE` or `_QUARANTINE` | Explicitly rejected creative — not evergreen, not active. |
| `05_CME\...\05_AD_CREATIVE_AUDIT_RESCUED` (76 files, ~140 MB) | `_ARCHIVE` (rescued history) | Audit rescue, historical. |
| 2 dead cleanup artifacts in `00_COMMAND_CENTER` | `99_ARCHIVE` | Dead files (Scout B). |
| `07_BRAND_AND_PROOF_BANK` deprecated pointer registries | `99_ARCHIVE` with a redirect note | Superseded but physically present with plausible names = confusion trap (Scout C). |
| `04_VIDEO_ADS\Raw_Footage` (67 files, 7.1 GB) | Keep, but flag "raw source, not reusable" | Not evergreen; don't archive, just label (Scout C). |
| Superseded contact-master versions (v1.0–1.2) | Private drive `99_ARCHIVE` | Keep newest canonical only in `03_MASTER_CONTACT_DATABASE`. |

---

## 12. CLIENT-DATA & PERMISSION PLAN

**The core finding (Scout D): the real leverage is ACCESS CONTROL, not relocation. Moving PII without a permission boundary is cosmetic.**

### Access model — the decisive question
The workspace is **one** Shared Drive; access is all-or-nothing at the drive level. Google Shared Drives do not support clean per-sub-folder ACLs. Therefore a `..._PRIVATE` folder inside the current drive **cannot be made more private than the marketing assets next to it.**

**Recommendation: create a second, separate restricted Shared Drive** (e.g. `00_E.C.O.S_CLIENTS_PRIVATE`) with membership limited to Edmund (and named advisors only). Move all PII there. This is the only option that gives a real boundary.

- **If Edmund approves the separate drive:** proceed with M1/M2 into it. Best outcome (privacy score 8).
- **If Edmund declines the separate drive:** **do NOT create `02_CLIENTS_AND_CONTACTS_PRIVATE` as a folder.** A private-labelled folder without a lock gives false comfort about a 22,069-row database. Instead: consolidate PII into ONE folder in place, restrict the whole drive's link-sharing, and log the separate-drive decision as the #1 open risk. (Privacy score capped ~5.)

### Consent register
`06_CLIENT_PROOF_CONSENT` (in the private drive) holds one row per person whose face/name/testimonial is used publicly: name, consent date, medium, PDPA basis, evidence file. Policy exists on paper (PROOF_AND_CLAIMS.md requires written PDPA consent before drafting); **evidence exists nowhere** — this register closes a live exposure. Gate `01_ASSET_LIBRARY\02_TESTIMONIALS_PROOF` and `03_APPROVED_PROOF` on it before any public deployment.

### GHL-as-source-of-truth policy (write this — currently unwritten)
> **CRM Source-of-Truth Policy.** GoHighLevel (GHL) is the single live record for all contacts. Any CSV/XLSX in the Drive is a **dated read-only snapshot**, never authoritative and never edited in place. When Drive and GHL disagree, GHL wins. Snapshots exist for backup, analysis, and migration only.

This resolves the competing masters (MASTER_CONTACT_DATABASE 06-10 vs CONTACT_MASTER v1.3 07-11 vs live GHL — Scout D). Retire the older file to `99_ARCHIVE`; keep one canonical snapshot.

### Naming standard (adopt)
- Backups: `GHL_CONTACT_EXPORT_YYYY-MM-DD_BACKUP.csv`
- Working exports: `GHL_CONTACT_EXPORT_YYYY-MM-DD_<purpose>.csv`
- Cleanup projects: `CONTACT_CLEANUP_YYYY-MM-DD_<scope>\` (the existing 2026-06-25 pipeline is the model)
- No undated / ad-hoc names (three undocumented 2026-07-11 drops with no provenance must be dated or quarantined — Scout D).

### Token
Rotate the plaintext GHL Private Integration Token in `CREDENTIALS_REGISTRY.md` (Scout E). Move secrets to a non-synced store; leave a pointer, not the value.

---

## 13. CAMPAIGN OPERATING MODEL

**Principle: ONE campaign home that explicitly retires the other four. A workbench, not a fifth silo.**

### Final template (lighter than the proposed 10 sub-folders)
Per campaign, folder named `YYYY-MM_Name_Channel_Wave` (e.g. `2026-07_LegacyLaunch_Meta_Wave3`), containing **5** sub-folders:

```
00_BRIEF_AND_PLAN\      (brief, angle, audience, budget, offer — was proposal's 00–02)
01_CREATIVE\            (copy + assets + variations — was 03–05)
02_LIVE_LINKS\          (scheduled/launched links, UTM, ad IDs — was 06–07)
03_TRACKING\            (spend/leads/results snapshot — was 08)
04_RESULTS_LEARNINGS\   (post-mortem → feeds the brain — was 09)
```

**Why 5, not 10:** the proposal's 10-folder template is enterprise ceremony a solo, non-technical owner won't sustain (the current `08_CAMPAIGNS` sits empty — evidence that ceremony without adoption = empty folders). Five folders map cleanly onto how one campaign actually runs, and keep paths under Windows MAX_PATH (Scout E risk 2).

### Lifecycle
`00_CAMPAIGN_INBOX` (raw idea) → `01_ACTIVE` (running) → `02_SCHEDULED` (queued) → `03_COMPLETED` (done, kept for reference) → `99_ARCHIVE` (cold). Move the folder between stages; don't copy.

### Supersession (mandatory — this is what makes it work)
A one-line note in each of the four old locations: *"Campaign work has moved to `03_ACTIVE_CAMPAIGNS`. This location is retired for campaigns as of 2026-07-XX (Decision 09X)."* Update `10_MARKETING_OS` CLAUDE.md §2 (which currently says masters stay in 05_CME "until Edmund approves a migration" — this IS that approval). Without supersession, `03_` is just a fifth home (Section 5, risk 3).

### Learnings flow back to the brain
`04_RESULTS_LEARNINGS` is the execution record; when a durable insight emerges ("navy creative beat white 2:1"), a **one-line distilled lesson** goes into `06_KNOWLEDGE_VAULT`. Execution data stays in the campaign; knowledge graduates to the brain. This is the knowledge-vs-execution separation applied.

### Briefly vs alternatives
- **File-type-first** (all briefs together, all creative together): breaks the "one campaign, one place" retrieval need — rejected.
- **Department-first** (marketing owns campaigns, sales owns pipeline): re-creates today's split-across-systems problem — rejected.
- **Channel-first** (Meta / Email / SMS top-level): a campaign is often multi-channel; fragments one campaign — rejected. Channel belongs *in the folder name*, not as the top axis.
- **Campaign-first (chosen):** matches how revenue work is actually planned, run, and reviewed.

---

## 14. FILE-FORMAT POLICY MATRIX

| # | Work type | Format | Home | Rationale |
|---|---|---|---|---|
| 1 | AI knowledge / brain docs | Markdown (.md) | `00_AI_OPERATING_SYSTEM` | Claude-native, diff-able, version-able. |
| 2 | Collaborative drafting | Google Docs | Drive (working) | Real-time edit, comments; not for AI ingestion. |
| 3 | Trackers / registers | Google Sheets | Campaign `03_TRACKING`, private `03_MASTER…` | Live tabular, formulas, filters. |
| 4 | Live contacts | CRM (GHL) | GHL, not files | Single live record (Sec. 12). |
| 5 | Contact snapshots/backups | CSV/XLSX | Private drive `03_/04_` | Dated read-only exports only. |
| 6 | Photos / images | Native (JPG/PNG) | `01_ASSET_LIBRARY\01_PHOTOS` | No conversion; browsable. |
| 7 | Video | Native (MP4/MOV) | `01_ASSET_LIBRARY\04_VIDEO_ADS` | Raw footage flagged "not reusable". |
| 8 | Final deliverables to send out | PDF (final only) | Campaign `02_/03_`, decks | PDF only when frozen/shipped — never as working format. |
| 9 | Presentations / decks | Google Slides (work) → PDF (final) | `01_ASSET_LIBRARY\05_SALES_DECKS` | Edit live, export final. |
| 10 | Code / pipelines | .py / .gs | With its data (private drive) or repo | Repoint paths on move (Sec. 10). |
| 11 | Consent evidence | PDF / image scan | Private `06_CLIENT_PROOF_CONSENT` | Immutable proof record. |
| 12 | Secrets / tokens | Secret store (not synced files) | Pointer in Drive only | Never plaintext in synced Drive (Sec. 12). |

**Rule of thumb for Edmund:** *md = what Claude reads; Docs/Sheets = what people edit together; CRM = live contacts; native = media; PDF = only when it's final and going out the door.*

---

## 15. OWNER & TEAM UX

**Where Edmund starts every session:** `START_HERE.md` → `00_AI_OPERATING_SYSTEM\CLAUDE.md` → Command Center (`MASTER_INDEX`, `03_CURRENT_PRIORITIES`, `10_PENDING_APPROVALS`). This is unchanged — just make the docs true again.

Daily journeys under the final (Hybrid) architecture, scored /5 for "can Edmund do this without confusion":

| | Journey | Score | Path |
|---|---|---|---|
| A | Start a new campaign | 5 | `03_ACTIVE_CAMPAIGNS\00_CAMPAIGN_INBOX` → promote to `01_ACTIVE\YYYY-MM_Name…` (one obvious home). |
| B | Find an approved photo/testimonial to reuse | 5 | `01_ASSET_LIBRARY\01_PHOTOS` / `03_APPROVED_PROOF` (unchanged names he just learned). |
| C | Pull the latest contact list | 4 | GHL is live truth; snapshot in private drive `03_MASTER…`. Slight friction: two-drive mental model. |
| D | Check "what matters now" | 5 | `03_CURRENT_PRIORITIES.md` (once rewritten — currently 4). |
| E | Route a task to a desk (`/desk`) | 5 | Works once `01_E.C.O.S` path fixed (currently broken → 1). |
| F | Review a campaign's results | 5 | `03_COMPLETED\<campaign>\04_RESULTS_LEARNINGS`. |
| G | Share a marketing asset with a teammate | 5 | General drive is shareable by design; PII is on the *other* drive, so no accidental PII leak. |

The Hybrid raises the two lowest journeys today (A: campaign chaos, E: broken routing) to 5, without disturbing B/D/G that already work.

---

## 16. MIGRATION STRATEGY

**Recommendation: staged + progressive, NOT big-bang.** The fragile surface is small and concentrated in two clusters (Scout E) — that argues for careful sequencing, and a solo non-technical owner cannot supervise a mass move. Do one folder, validate, then the next. Every phase has a rollback.

**STOP conditions (halt the whole migration and ask Edmund if any occur):** a Drive move produces delete+create instead of move; a `.py` pipeline errors after repoint; any path exceeds Windows MAX_PATH; the scheduled tasks fire during a move; PII appears on the general drive after M1/M2; more than a handful of Drive shortcuts break.

| Phase | Purpose | Actions | Validation | Rollback |
|---|---|---|---|---|
| **0 — Pre-flight (do NOW, before any move)** | Kill live bugs | Fix P1 scheduled-task paths (fires 07-20); fix P2 `/desk` routing; **pause** the 2 weekly scheduled tasks; rotate GHL token; ask Edmund the 3 open questions (App. I) | Tasks re-point to `00_E.C.O.S`; `/desk` resolves `01_E.C.O.S`; token rotated | Trivial — text edits, revert from git/history |
| **1 — Decide** | Ratify this report | Edmund picks Hybrid + answers separate-drive Y/N | Decision 09X logged | — |
| **2 — Stand up homes (empty)** | Create containers | Create private Shared Drive (if approved) + `03_ACTIVE_CAMPAIGNS` + `_QUARANTINE`, empty | Folders exist, permissions set on private drive | Delete empty folders |
| **3 — Dry-run** | Prove Drive move semantics | Move ONE small non-critical folder; watch for delete+create + shortcut breakage | Move is a true move; no dupes | Move back |
| **4 — PII first (highest risk)** | M1, M2 into private drive | Move `09_CLIENT_DATA` + `06_CONTACT_MASTER`; repoint P3/P4 pipelines | Pipelines run; no PII left on general drive | Move back; restore paths |
| **5 — Evict media from brain** | M3 | Move best-of → assets; rejected/audit → archive/quarantine | Brain < media threshold; images browsable | Move back |
| **6 — Consolidate campaigns** | M4, M5 + supersession | Move working campaign files to `03_`; write the 4 retirement notes | One campaign, one place; old homes redirect | Notes are reversible; move back |
| **7 — Doc truth-up** | Rewrites (Sec. 9) | Fix §9.7, priorities, audit checklist, operating-rules status | Docs match disk | Revert from history |
| **8 — Path sweep** | Remaining P5–P10 | Fix doc pointers, prune permissions | grep finds no live stale paths | Revert |
| **9 — Consent + policy** | Net-new governance | Write access rules, CRM-truth policy, seed consent register | Docs exist, gate proof usage | — |
| **10 — Freeze + verify** | Acceptance | Run Section 18 tests; unpause scheduled tasks; declare 90-day freeze | 12/12 tests pass | If a test fails, that phase rolls back |

---

## 17. REWRITE ESTIMATE

**Will Claude need to rewrite everything? No. The overwhelming majority is untouched or mechanically moved.** Approximate share of workspace files by treatment under the Hybrid:

| Treatment | Approx. share | Notes |
|---|---|---|
| Untouched | ~80% | 9/12 clean AI OS branches, most of the library, positioning/IP, knowledge vault. |
| Move-only (no content change) | ~10% | PII files, campaign working files, media (M1–M5). |
| Path-update (find/replace) | ~3% | 10 operational files + doc pointers (P1–P10). |
| Index revision | ~2% | Affected `_INDEX.md` after moves. |
| Meaningful rewrite | ~1% | §9.7, current-priorities, audit checklist (Sec. 9). |
| Script mods | <1% | 5 pipeline `.py` path repoints. |
| Human review required | ~1% | Consent decisions, separate-drive decision (App. H). |
| Archive | ~2% | Rejected media, dead artifacts, superseded registries. |
| Duplicates to resolve | <1% | Competing contact masters; split campaign. |

**Plain answer for Edmund:** *~95% of your files either stay exactly where they are or just get dragged to a new folder. Only about 1% needs actual re-writing, and that's mostly two stale documents and a rule that already contradicts your own decision.*

---

## 18. GO-LIVE ACCEPTANCE TESTS

All 12 must pass before the freeze is declared (Phase 10):

1. `/desk <task>` routes correctly (resolves `01_E.C.O.S`, no path error).
2. The 4 scheduled tasks point at `00_E.C.O.S` and do not error on next fire (verify before 07-20).
3. No raw PII file exists anywhere on the *general* Shared Drive (grep for the 22,069-row master + exports = zero hits outside the private drive).
4. The private drive's membership list contains only approved people; a non-member cannot open it.
5. Starting a new campaign lands in exactly one place (`03_ACTIVE_CAMPAIGNS`); the other 4 locations carry a retirement note.
6. The AI brain (`00_...`) contains no file > the media threshold (640 MB of images gone).
7. `03_CURRENT_PRIORITIES.md` names revenue, not "build the OS".
8. Constitution §9.7 matches Decision 084 (real files, not registry).
9. The 5 pipeline `.py` files run end-to-end against their new data paths.
10. One canonical contact snapshot exists; older masters are in `99_ARCHIVE`; the CRM-truth policy is written.
11. The consent register exists and every publicly-used testimonial has a row (or is pulled from public use).
12. `START_HERE.md` + root `CLAUDE.md` describe the workspace that actually exists (no `_DEL`, no `X-MAS HQ` at root).

---

## 19. ARCHITECTURE FREEZE RULES

Effective on passing Section 18, running to **~2026-10-16 (90 days)**:

1. **No new top-level folders** on either drive without a logged change request.
2. **No renames** of existing folders (especially the 9 library categories and the AI OS branches).
3. **No new re-org.** Structural change requires a Change Request that meets an **evidence threshold**: it must cite a *repeated, documented* failure the current structure caused (≥3 real instances), not a preference.
4. **Change-request log** lives in Command Center; every entry: date, problem evidence, proposed change, decision. Silent folder creation is a violation (Operating Agreement rule 37, one-fact-one-home).
5. **Adds within the frozen structure are fine** — a new campaign folder, a new knowledge doc, a new asset. The *shape* is frozen, not the *contents*.
6. **Weekly new-files sweep** (already scheduled) enforces the freeze by catching stray folders.
7. **The 90 days are for revenue** (Decision 090): diagnostic, Legacy Launch ads, the 7,000 GHL contacts. Folder work is done.
8. **Break-glass:** a genuine security/legal issue (e.g. a PII leak) overrides the freeze immediately — log it, fix it, move on.

---

## 20. FINAL RECOMMENDATION

**Adopt the Controlled Hybrid (Option C, 7.75/10). Reject the full rebuild (Option B, 5.98) and reject leaving things as-is (Option A, 4.35).**

Edmund's diagnosis is correct — PII is exposed and campaigns are scattered — but his cure is oversized. Keep everything you ratified three days ago. Change only what is provably broken: extract PII to a properly locked drive, build one campaign workbench that retires the other four, evict the 640 MB from the brain, fix the phantom paths and two stale docs. Then freeze for 90 days and go make money.

**This is NOT a third rebuild.** It is a targeted repair of two real wounds plus a bug-fix pass. It honours the 07-14 pivot instead of relitigating it.

### Before ANY files move — pre-migration blockers (do these first, in order)

1. **Fix the scheduled-task paths** in `C:\Users\Admin\.claude\scheduled-tasks\` (4 files, `Claude Workspace` → `00_E.C.O.S`). **They fail 2026-07-20.** Then pause the 2 weekly tasks for the migration.
2. **Fix `/desk` routing** — repoint `01_AI_TEAM` → `01_E.C.O.S` in the skill, constitution §5, MASTER_INDEX, root CLAUDE.md. Routing is broken *right now*.
3. **Rotate the GHL API token** in `CREDENTIALS_REGISTRY.md` (plaintext, self-flagged) and move it out of the synced Drive.
4. **Ask Edmund the three questions** that only he can answer (Appendix I): (a) Was `_DEL`'s disappearance intentional and logged? (b) Approve a separate restricted Shared Drive for PII — yes/no? (this gates whether `02_` gets built at all). (c) Are the two legacy `Scheduled\` automations still live anywhere?
5. **Get the Decision 09X ratification** of this report logged before Phase 2.

Only after 1–5 are cleared should any folder be created or any file moved.

---

## APPENDIX A — CURRENT FOLDER MAP (verified 2026-07-16)

```
H:\Shared drives\00_E.C.O.S\
├── .claude\                          (settings.local.json, 4 skills)
├── 00_AI_OPERATING_SYSTEM\
│   ├── 00_COMMAND_CENTER\            (15 files; MASTER_INDEX, DECISION_MEMORY 95.9KB, OPERATING_AGREEMENT)
│   ├── 01_E.C.O.S\                   (docs call this "01_AI_TEAM" — MISMATCH)
│   ├── 02_POSITIONING_AND_IP\        (64) [+ 01_DIAGNOSTIC_APP\CREDENTIALS_REGISTRY.md — plaintext token]
│   ├── 03_CLIENT_ADVISORY_OS\        (39)
│   ├── 04_AGENT_EDITION_OS\          (43)
│   ├── 05_CONTENT_MARKETING_ENGINE\  (413; 641.67MB incl. 341 PNGs in brain)
│   ├── 06_KNOWLEDGE_VAULT\           (53)
│   ├── 07_BRAND_AND_PROOF_BANK\      (11; deprecated pointer registries)
│   ├── 08_OPERATIONS\                (80; 73.95MB incl. 06_CONTACT_MASTER PII + pipeline)
│   ├── 10_MARKETING_OS\              (117; healthiest) [08_CAMPAIGNS empty]
│   ├── 11_SALES_OS\                  (167; 56% intentional scaffold)
│   ├── 99_ARCHIVE\                   (9)
│   ├── CLAUDE.md, _INDEX.md
├── 01_ASSET_LIBRARY\                 (9 categories; ~12,800 files)
│   ├── 01_PHOTOS (3,692) 02_TESTIMONIALS_PROOF (87) 03_BRAND_ASSETS (73)
│   ├── 04_VIDEO_ADS (415; Raw_Footage 7.1GB) 05_SALES_DECKS (15)
│   ├── 06_CAMPAIGN_OUTPUTS (542; WORKING files) 07_AD_SWIPE_FILES (121)
│   ├── 08_FRAMEWORKS_PLAYBOOKS (185) 09_CLIENT_DATA (222; 22,069-row PII master)
├── Artifacts\                        (2 mini-tools)
├── _ARCHIVE\                         (12 subfolders incl. X-MAS_HQ absorbed)
├── _BACKUPS\                         (ECOS_BACKUPS + ZZ_BACKUP_E_ZOOM_CONSULTS 410GB PII)
├── CLAUDE.md (v4.3) / PROJECT_LOCATIONS.md / START_HERE.md
                                       [_DEL and X-MAS HQ referenced but DO NOT EXIST]
```

## APPENDIX B — PROPOSED FINAL (HYBRID) MAP

```
Shared Drive #1 — H:\Shared drives\00_E.C.O.S\   (general / non-PII / shareable)
├── .claude\                          (paths fixed)
├── 00_AI_OPERATING_SYSTEM\           (brain only; no bulk media, no raw PII)
│   └── [9 clean branches unchanged; 05_CME media evicted; 06_CONTACT_MASTER moved out]
├── 01_ASSET_LIBRARY\                 (SAME 9 category names; 09_CLIENT_DATA retired, 06 scope-split)
├── 03_ACTIVE_CAMPAIGNS\   NEW
│   ├── 00_CAMPAIGN_INBOX\ 01_ACTIVE\ 02_SCHEDULED\ 03_COMPLETED\ 99_ARCHIVE\
│   └── <YYYY-MM_Name_Channel_Wave>\  {00_BRIEF_AND_PLAN, 01_CREATIVE, 02_LIVE_LINKS, 03_TRACKING, 04_RESULTS_LEARNINGS}
├── Artifacts\  _ARCHIVE\  _BACKUPS\  _QUARANTINE\ NEW
└── CLAUDE.md / START_HERE.md / PROJECT_LOCATIONS.md   (truthful)

Shared Drive #2 — H:\Shared drives\00_E.C.O.S_CLIENTS_PRIVATE\   (RESTRICTED membership)
└── 02_CLIENTS_AND_CONTACTS_PRIVATE\
    ├── 00_ACCESS_RULES\ 01_ACTIVE_CLIENTS\ 02_PAST_CLIENTS\
    ├── 03_MASTER_CONTACT_DATABASE\ 04_IMPORT_EXPORT_STAGING\
    ├── 05_DATA_CLEANUP_PROJECTS\ 06_CLIENT_PROOF_CONSENT\ 99_ARCHIVE\
```
*(If separate drive is declined: `02_` is NOT created; PII consolidated in place with drive-link restriction — see Sec. 12.)*

## APPENDIX C — CURRENT → PROPOSED PATH MAPPING

| Current | Proposed (Hybrid) |
|---|---|
| `01_ASSET_LIBRARY\09_CLIENT_DATA\*` (exports) | Private `02_...\03_MASTER_CONTACT_DATABASE\` |
| `01_ASSET_LIBRARY\09_CLIENT_DATA\*` (scripts) | Private `02_...\05_DATA_CLEANUP_PROJECTS\` |
| `01_ASSET_LIBRARY\09_CLIENT_DATA\CONTACT_CLEANUP_REBUILD_2026-06-25\` | Private `02_...\05_DATA_CLEANUP_PROJECTS\` |
| `08_OPERATIONS\06_CONTACT_MASTER\` | Private `02_...\03_MASTER_CONTACT_DATABASE\` |
| `05_CME\...\03_IMAGES_BEST_OF\` | `01_ASSET_LIBRARY\` (evergreen media) |
| `05_CME\...\04_IMAGES_REJECTED\` | `_ARCHIVE\` or `_QUARANTINE\` |
| `05_CME\...\05_AD_CREATIVE_AUDIT_RESCUED\` | `_ARCHIVE\` |
| `05_CME\01_CAMPAIGN_LEGACY_LAUNCH\` (non-media) | `03_ACTIVE_CAMPAIGNS\01_ACTIVE\2026-XX_LegacyLaunch_...\` |
| `01_ASSET_LIBRARY\06_CAMPAIGN_OUTPUTS\` (working) | `03_ACTIVE_CAMPAIGNS\...` |
| `01_ASSET_LIBRARY\06_CAMPAIGN_OUTPUTS\` (finished reusable) | STAYS (evergreen) |
| `10_MARKETING_OS\08_CAMPAIGNS\` (registry) | Redirect → `03_ACTIVE_CAMPAIGNS\`; retire |
| `00_AI_OPERATING_SYSTEM\01_E.C.O.S\` | UNCHANGED (fix docs to match, don't rename) |
| `_DEL\` (gone) | `_QUARANTINE\` (logged replacement) |

## APPENDIX D — CONTRADICTION REGISTER (Scout A)

| # | Contradiction | Severity | Fix |
|---|---|---|---|
| 1 | Root CLAUDE.md lists `X-MAS HQ` as live root (physically absorbed into `_ARCHIVE`) | High | P5 |
| 2 | CLAUDE.md + START_HERE say `_DEL` exists; it doesn't; no Decision logs its removal | High | Ask Edmund (App. I) + P5 |
| 3 | Constitution/MASTER_INDEX/skills route to `01_AI_TEAM`; folder is `01_E.C.O.S`; `/desk` broken | **Critical** | P2 |
| 4 | Constitution §9.7 "media = register not copied" contradicts Decision 084 | High | Sec. 9 rewrite |
| 5 | MASTER_INDEX sends asset lookups to archived-path registries | Med-High | P6 |
| 6 | MASTER_INDEX says 12 branches; audit checks 10 | Medium | Sec. 9 rewrite |
| 7 | `03_CURRENT_PRIORITIES` still says "build OS"; Decision 090 pivoted to revenue | Med-High | Sec. 9 rewrite |
| 8 | Client data has 3 unlabelled homes | High | Sec. 8/12 consolidation |
| 9 | Campaigns split across 3–4 homes, none canonical | Med-High | Sec. 13 workbench + supersession |

## APPENDIX E — DEPENDENCY REGISTER (Scout E)

See Section 10 (P1–P10). Headline: **10 genuinely operational fragile files** in 2 clusters (5 pipeline `.py`, 4 scheduled-task `.md`, 1 automation mirror). 113 raw matches, ~90 are prose/registries. Confirmed path-safe: Apps Script `.gs`, diagnostic webhook, `09_CLIENT_DATA` py (relative/argv). One plaintext secret (GHL token). MAX_PATH is a live constraint on any added nesting.

## APPENDIX F — DUPLICATE / SOURCE-OF-TRUTH REGISTER

| Concept | Competing copies | Canonical (recommended) |
|---|---|---|
| Contact master | `09_CLIENT_DATA\MASTER_CONTACT_DATABASE` (06-10) · `08_OPS\06_CONTACT_MASTER` v1.3 (07-11) · **live GHL** | GHL (live) + ONE dated snapshot in private `03_MASTER…`; archive the rest |
| Legacy Launch campaign | `06_CAMPAIGN_OUTPUTS\Legacy_Launch` (388/1.8GB) · `05_CME\01_CAMPAIGN_LEGACY_LAUNCH` (391/641MB) — 0 filename overlap, structural split | Merge into `03_ACTIVE_CAMPAIGNS\...\LegacyLaunch` |
| Behaviour/response rules | Constitution §3/7/8/13 · `02_OPERATING_RULES.md` · `11_OPERATING_AGREEMENT.md` | Operating Agreement (07-14) canonical; demote `02_OPERATING_RULES` |
| Campaign tracking | `10_MARKETING_OS\08_CAMPAIGNS` (empty) · `06_CAMPAIGN_OUTPUTS` · `05_CME` | `03_ACTIVE_CAMPAIGNS` (single) |
| Finished video vs campaign output | `04_VIDEO_ADS\Finished_By_Project` vs `06_CAMPAIGN_OUTPUTS\Legacy_Launch` — 0 overlap, different sets | Both valid; label roles (no merge) |

## APPENDIX G — PRIVACY FINDINGS (NO actual PII reproduced)

- 22,069-row contact master + 173 exports + 23 scripts in a *shareable* library (`09_CLIENT_DATA`) — risk 4.
- 7,314-row GHL import + versioned masters in the *brain* (`08_OPS\06_CONTACT_MASTER`) — risk 4, **least labelled** (no PII banner).
- 410 GB consult recordings/transcripts, folder names = real client names (`_BACKUPS`) — risk 5.
- Client-identifying testimonials, some faces unblurred + 455 event photos — risk 4.
- **Zero consent/release records anywhere**; policy on paper, evidence nowhere.
- **No access-rules doc anywhere**; one Shared Drive = drive-level access only; text "RESTRICTED" banners enforce nothing.
- **No written GHL-as-truth policy.**
- Stale legacy pointer to `X-MAS HQ\02_CLIENTS` (gone) still cited by 2 registries.
- Proven-good model exists: `11_SALES_OS\21_CONVERSATION_INTELLIGENCE` (pointer-only + anonymized, PII-free) — replicate its pattern.

## APPENDIX H — FILES REQUIRING HUMAN DECISION

| Item | Decision needed |
|---|---|
| Separate restricted Shared Drive for PII | Edmund: yes/no — gates whether `02_` is built at all |
| `06_CAMPAIGN_OUTPUTS` scope (working vs evergreen) | Edmund: confirm the split rule (Scout C — "resolve with Edmund, not a cleanup") |
| Sales OS 56% scaffold visibility | Keep visible / collapse / label as roadmap |
| Which contact master is canonical | Confirm GHL + which snapshot to keep |
| Testimonials without consent | Pull from public use, or obtain consent, per person |
| 3 undocumented 2026-07-11 data drops | Date/label or quarantine |
| `_DEL` disappearance | Was it intentional and is a backup retained? |

## APPENDIX I — UNRESOLVED QUESTIONS (only genuinely unresolvable without Edmund)

1. **Was `_DEL`'s deletion intentional?** It held 68 files for review (Decision 084) + a 07-14 backup (Decision 091); no Decision 092+ records its removal. Operating Agreement rules 39/43 require sign-off + a shown list for destructive actions. Needs a direct answer + confirmation a backup exists. *(Sharpest governance-integrity finding — Scout A.)*
2. **Separate restricted Shared Drive for PII — yes or no?** This is the single decision that determines whether the privacy fix is real or cosmetic (Scout D). Everything in Section 12 branches on it.
3. **Are the two legacy `Scheduled\` automations (referenced by 5 docs in `03_AUTOMATIONS` / `08_OPS`) still live anywhere?** If dead, delete the references; if live, they need repointing before they break (Scout E, severity 2–3).

---
*End of report. CANDIDATE status — no workspace file was modified. Awaiting Edmund's Decision 09X ratification.*
