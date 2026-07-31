# 16 — MASTER QA CHECKLIST & RECONCILIATION LOG
**QA performed by the orchestrator, 10 July 2026, against all 15 phase documents + 7 CSVs.**

---

## 1. The 15 quality-standard questions

| # | Question | Verdict | Evidence |
|---|---|---|---|
| 1 | Is the business entity clear? | **PASS** | The REI Method locked as business entity (D1); canonical description + Organization JSON-LD in doc 02; "REI Advisory" and "Singapore Real Estate Insider (as business name)" formally retired in doc 01 |
| 2 | Is the personal brand entity clear? | **PASS w/ gap** | Edmund Tan + Cindior Ho dual authority faces; Person schema + bios written. GAP: Cindior has no verifiable public presence yet — doc 07 makes it Week 1 action |
| 3 | Is the category clear? | **PASS** | The Second Property Ladder™ at `/second-property-ladder`, definition locked, category law Exit Before Entry™, villain One-Property Trap; category-vs-demand-language tension explicitly solved (docs 01 §11, 04 bridge map) |
| 4 | Is the demand-capture strategy clear? | **PASS** | 90-page roadmap CSV mapped to real Singapore queries (sell HDB buy condo, ABSD, decoupling, MOP…); 10 clusters; 100 AEO questions; capture-the-demand-correct-the-frame doctrine |
| 5 | Is the domain strategy clean? | **PASS** | One authority domain; 2 vanity funnel domains with noindex+bridge rules; 2 gated 301s; 1 parked; 35-row redirect map with preconditions |
| 6 | Are old brands handled properly? | **PASS** | Keep/Improve/Merge/Retire table (doc 01); 6FigurePropertyProfits retired w/ toxic-link audit; NLL demoted not deleted (phased rename Month 7, doc 14); SRE Insider scoped to YouTube |
| 7 | Are funnels connected to the authority site? | **PASS** | Funnel-to-Website map (doc 06); bridge-page canonicals (doc 03); footer entity blocks; single calendar CTA (Position Map session) |
| 8 | Are social profiles aligned? | **PASS** | Verbatim bios within character limits; same canonical one-liner everywhere; renames sequenced after domain-live (doc 07 CSV, 55 rows) |
| 9 | Are proof assets mapped? | **PASS w/ gap** | 52-asset inventory with confidence flags + consent requirements. GAP (honestly flagged): ~all figures UNVERIFIED, 3 of 7 proof categories have zero client story — verification is Week 1 work, not a writing problem |
| 10 | Are pages mapped by intent? | **PASS** | Every roadmap row carries intent, primary keyword, PAA secondaries, CTA, schema, funnel connection, priority |
| 11 | Are search and AI visibility both considered? | **PASS** | Answer-first page templates, FAQ/schema discipline, AI-crawler robots policy + llms.txt (doc 11), 62-prompt monthly AI test bank across 6 engines (doc 12) |
| 12 | Is the plan non-spammy? | **PASS** | No doorway pages (estate cluster capped at 4 genuinely distinct pages), funnels noindexed, no incentivised reviews, no fake schema, no thin AI content (transcript-rewrite gate in doc 10) |
| 13 | Is there a 90-day action plan? | **PASS** | Doc 13: 7-day unblockers, 30-day build, 13-week table (~55 rows: owner/effort/dependency/metric), do-NOT-do-yet list |
| 14 | Is there a 12-month roadmap? | **PASS** | Doc 14: quarterly entry/exit criteria, monthly milestones to 162 pages, risk register (8 risks w/ early-warning signals) |
| 15 | Can this be replicated for another edition? | **PASS** | Doc 15: 14-phase framework, 52-question intake bank, variable swap table, edition-specific banned-word logic, entity-separation gate |

## 2. Reconciliation log (conflicts found between parallel-built docs — all resolved)

| # | Conflict | Ruling | Where fixed |
|---|---|---|---|
| R1 | Authority-site platform: doc 03 recommended WordPress; doc 11 (decision owner) recommended GHL Websites | **GHL Websites for phase 1**, WordPress migration triggers documented (custom-code limits block JSON-LD / blog >100 posts unmanageable / CWV stays poor) | Doc 03 §7 rewritten; doc 03 Q6 marked resolved |
| R2 | Category hub slug: `/the-second-property-ladder` (docs 02, 11, 09, Proof CSV) vs `/second-property-ladder` (docs 03, 04, 06) | **`/second-property-ladder`** — normalised everywhere (17 slug fixes); founder URLs normalised to `/edmund-tan`, `/cindior-ho` (21 URL fixes) | Docs 02, 05, 09, 11, Proof_Library_Inventory.csv edited; logged in doc 13 |
| R3 | Cluster 7 pillar placed at `/guides/the-second-property-ladder-framework` (doc 05) vs root hub (doc 04) | Root hub is the pillar; the /guides/ page becomes its deep-dive (no duplicate) | Doc 05 §cluster-index, §cluster-7, Concern 2 |
| R4 | GBP rename timing: doc 02 said rename to "The REI Method" early; doc 08 said rename only after the name exists publicly (Google name-match rule) | **Doc 08 wins** — interim name "Coach Edmund Tan", rename evaluated Week 8+ | Adopted by doc 13 calendar; confirmed by orchestrator |
| R5 | Diagnostic sequencing: docs 05/10 assumed diagnostic live early; doc 06 sequences it after V2 ships | Diagnostic build starts Week 5; all pre-Week-8 CTAs route to Position Map session; pages written so the diagnostic link slots in later | Doc 13 §conflicts #3 |
| R6 | "Agent" is banned (D5) but appears in the locked one-liner ("38,000 agents…") and is the Agent Edition's audience | Banned as self-description only; permitted in the locked market one-liner, the villain name "Agent-Led Transaction Thinking", and verbatim user-phrased FAQ questions; NOT banned in the Agent Edition | Docs 05, 10, 15 apply this consistently |
| R7 | Legacy Launch V2 bridge canonical: category hub (doc 06) vs possible dedicated `/legacy-launch` page (doc 04) | Default = category hub; build `/legacy-launch` only if campaign content justifies it — decide before Week 2 placeholder build | Doc 13 §conflicts #2 (open sub-question, default set) |
| R8 | CSV integrity: AEO_Page_Roadmap.csv had rows of 15–18 cols; Funnel_Audit_Table.csv rows of 11 | Both repaired by their original builder agents and re-validated with csv parser (90×14; 60×10) | CSVs rewritten |
| R9 | NAV claim inconsistency: $6.6M→$9M (strategy docs) vs <$1M→>$5M in <5yrs (reel claims bank) | Not resolvable internally — likely different timeframes/scopes; BOTH quarantined behind [VERIFY]; added to founder verification session agenda | Doc 09 Concerns; doc 00 §6 |

## 3. Residual open items (cannot be closed without the founders)

1. CEA reg numbers (Edmund, Cindior) + PropNex licence number → unblocks compliance blocks, schema, ads.
2. Portfolio/case figure verification session (all 9 flagged claims incl. R9).
3. Cindior: LinkedIn creation, bio sign-off, on-camera role decision.
4. Domain/infrastructure access audit: thereimethod.com live state, Search Console/GA4 existence, registrar/DNS access, backlink exports before any 301.
5. GBP listing details behind share.google/bpyWTGgjlyNxt8Xiz (name, category, reviews, verification state).
6. Old "Legacy Launch" funnel: still receiving traffic? (audit before sunset).
7. IG handle `@coachedmundtan` availability.
8. PropNex compliance review of the replacement for "This is advisory, not agency".
9. Two-Property Club framing — parked by design; revisit Q4.
10. Legacy Launch bridge canonical choice (R7) — default stands unless overridden before Week 2.

## 4. [VERIFY] discipline — the standing rule

Any dollar figure, count, regulatory rate (ABSD/SSD/MOP/CPF/TDSR), subscriber count, or session-length promise carries `[VERIFY]` until checked against records or an official source, and regulatory content is date-stamped with a quarterly re-check (doc 04 cadence). **Nothing ships to a public surface with a live `[VERIFY]` tag.** The Friday content QA (doc 10 §checklist) enforces this weekly.

## 5. Keeping the OS in sync (maintenance rules)

1. `_MASTER_CONTEXT_BRIEF.md` is the single contract. Change a locked decision there first, then propagate; log the change in this doc's §2.
2. New conflicts between docs get a row in §2 — never silently edit one doc to disagree with another.
3. Quarterly repositioning review (doc 14) re-runs §1's 15 questions.
4. When the Agent Edition starts, doc 15's entity-separation gate is mandatory before any shared asset is touched.

## 6. Build provenance

Research: 3 Sonnet agents (Drive docs, GHL account pull, local funnel/reels audit). Build: Opus 4.8 (docs 01–04), Sonnet 5 (docs 05–15 + CSVs). Orchestration, locked decisions D1–D8, QA, reconciliations R1–R9, and docs 00/16: repositioning architect. All 21 build files complete; CSVs machine-validated.
