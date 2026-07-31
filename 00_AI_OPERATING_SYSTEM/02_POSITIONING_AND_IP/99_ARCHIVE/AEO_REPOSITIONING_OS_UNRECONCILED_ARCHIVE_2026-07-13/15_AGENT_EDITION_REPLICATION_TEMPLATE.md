# 15 — AGENT EDITION REPLICATION TEMPLATE
**Phase 14 · AEO Repositioning OS · Replication Layer**
**Owner:** Sonnet agent · **Date:** 9 July 2026 · **Status:** DRAFT for orchestrator QA. Built on LOCKED decisions D1–D8 in `_MASTER_CONTEXT_BRIEF.md` and the completed structure of docs 01–12 (Client Edition). Does not relitigate any Client Edition ruling — it extracts the reusable *process* from those rulings so a second edition can be built without re-deriving methodology from zero.

---

## EXECUTIVE SUMMARY

The Client Edition (docs 01–12) is not just a finished positioning — it is a proof-of-method for a repeatable 14-phase repositioning process (asset inventory → foundation audit → entity → domain → website → clusters → funnels → social → GBP → proof → content → technical → measurement → calendars). This document extracts that process into a swap-variable template so the operators can run the same OS for the **Agent Edition** — a future second business line teaching Singapore property agents/salespersons the method (or otherwise attracting them to a team; the exact offer is undecided and must be settled before Phase 1 starts) — without re-deriving the frameworks, QA standards, or compliance guardrails from scratch.

The central risk this template manages is **entity contamination**, not content quality: this project's single largest structural finding was that one GHL sub-account already runs two unrelated business lines (the advisory business and Changi Green, a room-rental operation) under one CRM, and the fix was hard quarantine — no shared `sameAs`, no shared schema, no shared pipeline. The Agent Edition creates the identical risk at a higher stakes level, because unlike Changi Green it shares the *same two founders* and the *same regulator* (CEA) as the Client Edition, and its audience (property agents) can overlap with — and be recruited from — the very buyer audience the Client Edition is building trust with. A buyer who discovers their "advisory, not agency" advisor is simultaneously running a recruitment funnel for agents is a credibility risk the Client Edition cannot absorb.

This document delivers: (1) the Replication Framework — what transfers as-is (methodology, templates, QA standards, compliance discipline) vs what must be rebuilt per edition (audience, vocabulary, category, proof); (2) a 52-question Agent Edition intake bank across 14 swap-variable groups; (3) a full Variable Swap Table; (4) domain, page-map, and funnel-map placeholders with decision rules; (5) a content-cluster placeholder; and (6) a generalised 15-point Replication QA Checklist plus an entity-separation gate. Every placeholder in this document is marked `[FILL]`; nothing here should be read as a decision about the Agent Edition — it is the empty form the next builder fills in only after the Agent Edition Question Bank (Section 2) has been answered.

**Concerns note (per brief instruction):** `16_MASTER_QA_CHECKLIST.md` does not exist yet in this Drive folder as of this writing — it is listed as an Orchestrator deliverable in the Master Brief's deliverable map but has not been built. Section 8 of this document therefore derives its 15 QA points directly from the Writing Standards (Master Brief §5) and the recurring quality gates visible across docs 01–12, rather than copying an existing checklist. If `16_MASTER_QA_CHECKLIST.md` is later built with a different structure, reconcile Section 8 against it.

---

## 1. REPLICATION FRAMEWORK

The Client Edition build ran 14 phases. Each phase has a stable *shape* (purpose, key questions, inputs, outputs) that is edition-agnostic, and a *content* layer that is entirely edition-specific. The table below is the reusable spine — read it as "how to run this phase for any edition," with the Client Edition columns showing what was actually produced, so a builder can see the pattern instantiated once before instantiating it again.

| # | Phase | Purpose | Key questions the phase must answer | Inputs required | Outputs produced | Transfers as-is (methodology/templates/QA/compliance) | Must be rebuilt per edition (audience/vocabulary/category/proof) |
|---|---|---|---|---|---|---|---|
| 0 | **Research & Asset Inventory** (produced `_RESEARCH_APPENDIX.md` for Client Edition; no numbered doc of its own) | Establish ground truth before any positioning work starts — what already exists, under what name, at what URL, in what state. | What domains/handles/GHL objects/funnels/strategy docs already exist? Which are live vs dormant vs conflicting? What dollar figures, claims, and proof fragments are floating in copy with no verification? | Founder interviews; GHL account audit; domain/DNS registrar list; social handle list; existing strategy docs (rank-ordered); ad account access; Search Console/GA4 access if any | A research appendix: verified facts, `[VERIFY]` flags, a fragmentation table (every competing brand token and where it lives) | The discipline of "flag, don't assume" — every unverified figure gets `[VERIFY]`; every competing name gets logged, not silently merged; rank strategy docs by authority before trusting any of them | The actual assets found — an Agent Edition may have zero existing assets (clean-slate) or may inherit some (e.g. Edmund's existing YouTube library already contains agent-facing content) — this must be re-inventoried, not assumed absent |
| 1 | **Business Foundation Audit** (`01_BUSINESS_FOUNDATION_AUDIT.md`) | Diagnose brand/name fragmentation; lock target-state entity names, vocabulary, banned words, and public positioning language. | Which of the competing tokens is the authority face, the business brand, the category? What must be retired, demoted, or merged? What words are banned and why? | Phase 0 outputs; founder interview on identity preferences; compliance guardrails (D7-equivalent) | A ruling on every brand token (keep/improve/merge/retire); founder bios; business bio; banned-word list; category-ownership plan | The **method** of auditing fragmentation (the "if a stranger lands on X, they conclude the business is called Y" table technique); the E-E-A-T/entity-recognition reasoning; the "reasoning a skeptical founder would accept" persuasion structure | The actual tokens, the actual target-state names, the actual banned words (agent-facing banned words differ sharply — "agent" itself cannot be banned when the audience *is* agents) |
| 2 | **Entity Architecture** (`02_ENTITY_ARCHITECTURE.md`) | Define the machine-readable identity layer: Person/Organization/Category/Offer entities, their `sameAs` graphs, and their schema.org types. | Which entities does this edition need (new Organization? new Category/Method? does it reuse the existing Person entities)? What is quarantined from what? | Phase 1 rulings; full entity list with priority (P0/P1/P2) | An entity register (fields: official name, aliases, canonical description, primary URL, sameAs, supporting pages, proof assets, schema type, internal link targets, priority) | The entity-register template itself (the 12-field table); the schema-type decision logic (e.g. why `DefinedTerm`+`Article`+`FAQPage` over retired `HowTo`); the quarantine doctrine (Changi Green precedent) | Every entity's actual name, description, and sameAs list; whether the edition gets its own Organization entity (near-certain yes, per Section 4) or shares one |
| 3 | **Domain Architecture** (`03_DOMAIN_ARCHITECTURE.md`) | Decide one authority domain, which vanity domains host funnels, which retire, which park — and build the redirect/canonical/noindex map. | Does this edition need its own domain, or a section of an existing one? Which existing domains (if any) are already owned/relevant? | Phase 2 entity register; Phase 0 domain inventory; DNS/registrar access; Search Console access (for any live domain) | Domain decision table (role/verdict/rationale/risks/sequencing); redirect map; canonical map; noindex map | The 9-criteria evaluation framework (authority strengthening, AI entity confusion, duplicate content, doorway risk, traffic, backlinks, tracking, clear role, future fit); the bridge-page mechanic (noindex funnel steps, one indexable bridge page canonical to the hub); the 12-month minimum redirect-hold rule | The actual domain(s) chosen and the same-vs-separate decision itself (Section 4 gives the decision rule — this is the highest-leverage edition-specific call in the whole template) |
| 4 | **Website Sitemap & Page Roadmap** (`04_WEBSITE_SITEMAP_AND_PAGE_ROADMAP.md`) | Build the full site tree: authority/entity pages, offer pages, proof hub, demand-capture layer, compliance footer block. | What does this audience actually search vs what is the category vocabulary? How do demand pages bridge to category pages? | Phase 3 domain decision; Phase 2 entities; keyword/demand research for this audience | Full sitemap tree with slugs; page-roadmap CSV (page-by-page: slug, type, priority, target query, internal links, schema type) | The two-layer demand-capture + category-page architecture; the "every page routes to one universal CTA" discipline; the CEA compliance block pattern (rendered sitewide, four required identifiers); the page-roadmap CSV column set | The actual page list, slugs, and — critically — the actual demand vocabulary (agents do not search "sell HDB buy condo"; they search career/income/training-shaped queries — Section 5 placeholder) |
| 5 | **AEO Topic Clusters** (`05_AEO_TOPIC_CLUSTERS.md`) | Map cluster types (best/top, comparison, timing, mistakes, framework, local, long-term) to slugs and content types; write FAQ questions in literal search phrasing. | What are this audience's real Google/AI query patterns inside each cluster type? | Phase 4 sitemap; keyword research; competitor content scan | Cluster index (cluster, type, pillar slug); FAQ question banks with literal phrasing preserved even where it uses a banned word in the *query*, never in the *answer/title* | The 7-cluster-type taxonomy itself (best/top, comparison, timing/mistakes, framework, local, long-term — reused verbatim in Section 7); the "preserve literal search phrasing in FAQ answers, never in our own titles/slugs" rule | The actual clusters and queries — agent-audience demand is entirely different (e.g. "how to get my first listing," "CEA exam tips," "best team to join" vs buyer queries) |
| 6 | **Funnel Ecosystem Audit** (`06_FUNNEL_ECOSYSTEM_AUDIT.md`) | Inventory every funnel-shaped asset by state (live/built-unpublished/spec'd/referenced-but-nonexistent); score against a fixed criteria set; sequence fixes by proximity to revenue. | What funnels exist for this edition (probably none)? What is the offer ladder? What CRM objects (custom fields, pipelines) must exist before UI work starts? | Phase 0 funnel/GHL inventory; Phase 4/5 page and cluster maps | Funnel audit table (15 criteria × N funnels); funnel-to-website bridge map; keep/improve/rebuild decision with sequencing | The 15-criterion scoring rubric (offer clarity → domain placement); the "audit before you decide keep/sunset" discipline; the bridge-page-per-funnel rule; the "fix what's closest to revenue first" sequencing logic | The actual funnels, offer ladder rungs, and CRM field prefix (Client Edition uses `spl_*`; Agent Edition needs its own prefix, e.g. `[FILL, e.g. age_*]`, never reusing `spl_*` or `cg_*`) |
| 7 | **Social Profile Repositioning** (`07_SOCIAL_PROFILE_REPOSITIONING.md`) | Platform-by-platform audit (current diagnosis, what's confusing, what's strong, remove/add) with a sequenced rename/bio plan. | Which platforms does this audience actually use? Does the edition get new handles or does it live inside existing profiles' bio/pinned content? | Phase 0 handle inventory; Phase 1 vocabulary; Phase 2 entities | Platform audit + rebuild plan; social profile update checklist CSV | The per-platform audit structure (current diagnosis → confusing → strong → remove → add); the "rename only after the authority domain is live" sequencing rule; the handle-convergence logic | The actual platform mix (agent-facing content likely leans LinkedIn/Telegram/agent-community Facebook groups over IG — different platform priority than the Client Edition's buyer-facing IG/FB/YouTube mix) |
| 8 | **Google Business Profile Plan** (`08_GOOGLE_BUSINESS_PROFILE_PLAN.md`) | Audit/build one GBP; resolve naming-match, category, and practitioner-vs-business-listing questions. | Does an agent-training/recruitment offer even qualify for a GBP (it may not be a "local business" in Google's sense — see Section 4)? Does it share the existing GBP or need its own? | Phase 2 entities; Phase 3 domain; existing GBP state | GBP audit checklist; naming/category decision; services list + description; NAP block; citation targets | The audit-before-edit discipline; the name-matching-to-real-world-usage rule; the SAB (service-area business, address hidden) recommendation logic; the practitioner-vs-parent-listing distinction | The actual GBP decision — an agent-training offer may not be GBP-eligible at all (Google's local-business categories assume a service rendered to the public, not B2B-style recruitment/training; flag as `[OPEN]`, do not assume a GBP is even the right instrument) |
| 9 | **Proof Library System** (`09_PROOF_LIBRARY_SYSTEM.md`) | Classify all proof fragments into types; build the case-study production system, consent rules, and a compliance-safe claims guide. | What proof exists for this offer (results from agents trained/recruited, income claims, team growth)? What consent do agents (not buyers) need to give? | Phase 1 vocabulary; Phase 0 asset inventory; any existing testimonials/team data | Proof inventory by type; consent/anonymisation rules; forward pipeline (case-study ideas, review prompts, authority angles) | The 10-proof-type taxonomy; the PDPA consent checklist (8 points); the "no client story = no claim" discipline; the confidence-state labelling (VERIFIED/INFERRED/UNTESTED/GAP) | The actual proof — and a much sharper compliance bar: **agent-recruitment income proof is the single highest-liability content type in the entire replication** (see Section 4's compliance flags) — no earnings claim can ship without the same rigour applied to the Client Edition's $160M/100-buyers figures, arguably more |
| 10 | **Content Engine SOP** (`10_CONTENT_ENGINE_SOP.md`) | Turn one weekly source asset into N downstream assets using existing tools; respect real team-capacity constraints. | Who creates content for this edition (same founders? different voice?)? What existing back-catalogue can be repurposed? | Phase 4/5 page/cluster maps; Phase 7 social platforms; team capacity | Atomisation chain (asset-by-asset table); weekly calendar; thin-content/QA gates | The atomisation-chain template (source asset → N downstream assets, each with owner/tool/time/QA gate); the transcription-is-not-an-article rule; the back-catalogue-repurposing workstream pattern | The actual pillar topics, the actual back-catalogue (does 600+ videos contain any agent-facing content already?), and team capacity (adding a second content line to the same two-person team is a real capacity question, not a copy-paste) |
| 11 | **Technical AEO/SEO Checklist** (`11_TECHNICAL_AEO_SEO_CHECKLIST.md`) | Decide the platform (and confirm it can be the same GHL sub-account or must be separate — see Section 4); spec schema injection, redirects, crawler policy. | Same platform as Client Edition or new? Same GHL sub-account (contamination risk) or separate? | Phase 3 domain decision; Phase 8 platform capability limits | Platform decision; schema injection plan; AI-crawler allow policy; sequenced P0→P2 checklist | The platform-decision framework (who operates it > what's theoretically best); the AI-crawler-allow reasoning (being cited requires letting the citing bots in); the schema-budget discipline | The actual platform pick if it differs, and definitely the GHL sub-account decision (Section 6 — recommend separate sub-account, reusing the Changi Green lesson) |
| 12 | **Measurement & Automation System** (`12_MEASUREMENT_AND_AUTOMATION_SYSTEM.md`) | Build a two-track KPI system (manual now, automated later); build an AI Visibility Test Bank; segment reporting by business line. | What does success mean for this offer (agents trained? agents recruited to team? revenue per agent?)? Must reporting be segmented from the Client Edition and Changi Green? | Phase 6 funnel/CRM fields; Phase 9 proof; existing GA4/GSC state | KPI dashboard spec; AI Visibility Test Bank (prompts × engines); monthly reporting template; automation backlog | The two-track Sheets-now/Looker-later migration logic; the AI Visibility Test Bank scoring rubric (0–3, not-mentioned/mentioned/cited/recommended); the "segment out other business lines via tags immediately" discipline; the baseline-before-changes rule | The actual KPIs, the actual test-bank prompts (agent-audience AI queries are entirely different from buyer queries), and the tag/segmentation scheme (three business lines now: advisory, Changi Green, Agent Edition — each needs its own tag from day one) |
| 13 | **Action Calendars** (90-day + 12-month) | Sequence every phase's actions into a dependency-ordered execution calendar. | What must happen before what (e.g. domain live before handle renames, per Client Edition's Phase 3→7 dependency)? | All prior phase outputs | 90-day calendar; 12-month roadmap | The dependency-sequencing method itself (map every "X must happen before Y" relationship across phases before assigning dates) | The actual dates and task list, and critically: **whether the Agent Edition calendar can even start before the Client Edition's own 90-day plan is substantially executed** — running two repositioning builds on the same two founders simultaneously is a capacity call, not a template call (flag in Dependencies) |

---

## 2. AGENT EDITION QUESTION BANK

52 intake questions across 14 groups. These mirror the hard-won discoveries of the Client Edition build — real handles, real domains, licence numbers, verified proof, existing funnel inventory — so the next builder does not have to rediscover the same categories of gap by trial and error. Answer every question before starting Phase 1. Questions marked **(hard filter)** mirror the Client Edition's buyer hard-filter (Mechanism v1.3) and must produce an equally sharp exclusion rule, not a vague "agents who want to grow."

### A. Audience
1. Which agents specifically — new/unlicensed entrants studying for CEA exams, newly licensed agents in their first 12 months, or experienced agents underperforming and seeking a system? These are three different offers with three different funnels.
2. What agency affiliation does the target agent have — PropNex only (matching the founders' own agency), any CEA-registered agency, or agency-agnostic? This changes both the compliance frame (Section 4) and the "join our team" vs "learn our method independent of agency" offer shape.
3. **(hard filter)** What production level (transactions/month or GCI) qualifies an agent as "in scope" vs excluded? Define this as precisely as the Client Edition's "$20k+/month household income, $2.5m+ serviceable" filter.
4. Is the audience Singapore-only, or does it include agents in other markets who could apply the same method (expansion risk/opportunity — flag, do not decide now)?
5. Does the target agent need to be recruitable into the founders' own team/agency structure, or is this a pure education/training product sold to agents who stay at their existing agency?

### B. Problem
6. What is the named villain (equivalent to "The One-Property Trap")? Is it "commission-chasing without a system," "agent-led transaction thinking with no repeatable process," "burnout from cold prospecting," or something else?
7. What supporting villains exist (equivalent to Buy-To-Stay Thinking, Agent-Led Transaction Thinking, etc.)? List at least 3–5 named sub-problems.
8. Is the core problem income instability, lack of a repeatable client-acquisition system, lack of a credible personal brand, or lack of technical/advisory competence (these lead to very different offers)?

### C. Transformation
9. What is the agent's "after" state in one sentence (equivalent to "higher net asset value, more options, long-term family freedom")?
10. Is the transformation career-shaped (income growth, production growth) or identity-shaped (from "salesperson" to "advisor," mirroring the founders' own repositioning)? This is the single most important strategic choice — it decides whether the Agent Edition is a sales-skills product or an identity/positioning product like the Client Edition itself.
11. What is the realistic timeline for the transformation (weeks/months/years), and is it defensible without an income guarantee?

### D. Category
12. What is the category name (equivalent to "The Second Property Ladder™")? Does it extend the existing Second Property Ladder / Exit Before Entry IP into an agent-facing application (risk: dilutes the buyer category, mirrors the New Launch Ladder situation this project just resolved) or is it a wholly separate, named category?
13. What is the category law (equivalent to "Exit Before Entry™")?
14. Does this category compete with, sit subordinate to, or sit entirely separate from The Second Property Ladder™ in the public mind? State the relationship explicitly — do not let it default to ambiguous, the exact mistake New Launch Ladder™ made for two years.

### E. Offer
15. Free content → lead magnet → what paid offer? Course, coaching, done-with-you system, team recruitment (join the founders' agency team), or a hybrid?
16. Is there a recruitment component (agents join the founders' PropNex team/downline)? If yes, is compensation ever tied to recruiting other agents (this triggers the Multi-Level Marketing and Pyramid Selling (Prohibition) Act risk screen — Section 4) or purely to the recruit's own transaction production?
17. What is the offer ladder's price point at each rung, and can every claim about outcomes at each rung be verified before publish (same discipline as Client Edition's `[VERIFY]` rule)?
18. Is there a Two-Property-Club-style "parked, do not build yet" future offer that should be logged now and explicitly not built?

### F. Proof
19. What proof exists today of agents who succeeded using this method — named, consented, verifiable? (Expect the Client Edition's finding to repeat: proof *material* exists in memory/anecdote, proof *assets* with consent and verified figures do not.)
20. Do the founders have any existing downline/mentee agents whose results could form the first 3–5 case studies?
21. What production/income figures, if any, are safe to publish without triggering income-guarantee or misleading-earnings-claim risk (Section 4)?
22. Is there an existing "founders built it before they taught it" proof arc for the agent side (e.g., the founders' own production numbers as PropNex agents) equivalent to the buyer-side "we built it before we advised it" line?

### G. Domain
23. Does the business already own or need to acquire a domain for this edition? (Per Section 4's decision rule — do not default to a subdirectory of thereimethod.com without running the criteria.)
24. If a new domain is needed, is it available, and does its string collide with any existing owned domain's brand equity (mirroring the "REI" vs REI-the-retailer collision flagged in doc 02)?
25. Will the Agent Edition domain need its own Search Console/GA4 property from day one (yes, per the segmentation discipline in Phase 12), and who owns that setup?

### H. Funnel
26. Does an equivalent "Which Step Are You On?" diagnostic make sense for agents (e.g. "Which stage of [Agent Edition method] are you at?"), and if so what are its gating questions (mirroring the hard filter in B3)?
27. What GHL custom-field prefix will this edition use (must be unique — never `spl_*` or `cg_*`)?
28. What existing funnel-shaped assets (if any) already target agents — has anyone in the business ever run a recruitment ad, a "join our team" landing page, or an agent-facing webinar? Audit before assuming a clean slate (same discipline as doc 06's "audit the old Legacy Launch funnel before deciding" ruling).
29. What is the single universal CTA for this edition (mirroring "Position Map session")?

### I. Social platforms
30. Which platforms do target agents actually use for professional development content — LinkedIn, agent-only Facebook/Telegram groups, YouTube, TikTok? Rank by expected reach, do not assume the Client Edition's IG-heavy mix transfers.
31. Do the founders need new, separate handles for the Agent Edition, or does it live as a content vertical inside existing profiles (mirroring the "bio/pinned content first, rename later" sequencing in doc 07)?
32. Is there a risk that Agent Edition content posted to the founders' existing buyer-facing profiles (facebook.com/coachedmundtan, instagram.com/propertycoachedmundtan) confuses or alienates the buyer audience? If yes, this argues for platform separation, not just domain separation.

### J. Content pillars
33. What are this edition's 5–6 content pillars (equivalent to the Client Edition's 6 buyer pillars)?
34. Can any of the founders' existing 600+ YouTube videos be re-tagged or re-cut for the agent audience, or is this a fully net-new content library?
35. Who creates Agent Edition content — the same two founders (capacity question, flagged in Phase 10/13) or a delegated team member/mentee agent as co-host?

### K. Keywords & search demand
36. What do agents actually type into Google/AI engines — "how to get more listings," "CEA exam tips," "best real estate team Singapore," "how to become a full-time property agent"? Run real keyword research; do not assume category vocabulary is searched (same finding as doc 04's "nobody searches 'Second Property Ladder'").
37. Is there meaningful search demand at all, or is this audience better reached via direct outreach/agency-network channels than SEO/AEO (a real possibility for a B2B-shaped, community-driven audience — flag honestly rather than force an SEO plan onto a channel that doesn't fit)?
38. What comparison queries exist (e.g. "[Agency A] vs [Agency B] team," "become an agent vs stay employed") that map to the `/compare/` cluster type?

### L. Case studies
39. How many named, consenting agent case studies can realistically be produced in the first 90 days?
40. What anonymisation default applies (first-name-plus-context, as with buyer case studies, or full-name-with-photo, which is more common and more persuasive in recruitment-style content but raises consent/scope questions — Section 9 of doc 09 applies here too)?
41. Does a case study about an agent's income results require a different consent/verification bar than a case study about a buyer's property outcome? (Likely yes — income claims about a third party carry higher regulatory exposure than a property-value claim.)

### M. CTA
42. Is the CTA a booked call (mirroring Position Map), an application (mirroring the old Legacy Launch's high-commitment form), a webinar registration, or a self-serve enrolment?
43. Does the CTA route into the same GHL pipeline structure (1-To-1 Pipeline) or a dedicated pipeline (recommended, per Section 6)?
44. What disqualifies a lead at the CTA stage (mirroring the diagnostic's Gates/Checkpoints), and is that logic built before or after the offer itself is finalised?

### N. Compliance
45. Do CEA's advertising/conduct rules apply to recruitment-style advertising (attracting a licensed or prospective salesperson to a team) in the same way they apply to consumer-facing property advertising, or is this a different regulatory lane? **[VERIFY with PropNex compliance / CEA guidance directly — do not assume either answer.]**
46. If the offer includes "join our PropNex team," does PropNex have its own internal recruitment-advertising or branding policy that governs what the founders can claim publicly about team benefits, splits, or income potential? **[VERIFY with PropNex compliance.]**
47. If any compensation structure rewards an agent for recruiting other agents (not just for their own transactions), does this fall under Singapore's Multi-Level Marketing and Pyramid Selling (Prohibition) Act, and has this been screened by a lawyer? **[VERIFY — treat as a hard blocker, not a checklist item, if the offer has any recruit-a-recruiter component.]**
48. If the training content strays from "real estate sales skill" into "how to advise clients on property as an investment/wealth vehicle," does that cross into regulated financial advice under the Financial Advisers Act (MAS), requiring a licence the founders do not currently hold? **[VERIFY — this is the same boundary the Client Edition already manages carefully by using "advisory" language for property sequencing, not investment advice; the Agent Edition must draw the same line for a different audience.]**
49. What earnings/income claims (if any) are planned, and can every one be substantiated per the Consumer Protection (Fair Trading) Act's prohibition on misleading claims, with the same rigour the Client Edition applies to its $160M/100-buyers figures? **[VERIFY — no income claim ships without a source ledger, same as D7's discipline.]**
50. Does this edition require its own PDPA consent language (distinct from the buyer-facing forms), given it collects different data (CEA registration status, current agency, production history) from a different data-subject population?
51. Should agent-facing advertising carry the same CEA-registration/PropNex-licence compliance block used sitewide on thereimethod.com, or does a different disclosure apply because the audience being addressed is licensees, not consumers? **[VERIFY.]**
52. Is there a reputational/regulatory reason PropNex itself (as the agency both founders belong to) needs to be consulted or formally sign off before any public Agent Edition recruitment content ships, given it could be read as unofficial/unauthorised agency recruitment activity?

---

## 3. VARIABLE SWAP TABLE

Every variable that changes between editions. `[FILL]` = must be answered from Section 2 before this row can be actioned. Rows marked **(shared)** are candidates to stay identical across editions — verify against Section 4/6's separation criteria before assuming any "(shared)" row is safe to actually share.

| Variable | Client Edition value | Agent Edition placeholder |
|---|---|---|
| Business/advisory brand | The REI Method | `[FILL — likely a distinct sub-brand, e.g. "The REI Method [Agent Program name]" or a wholly separate name; do not default to reusing "The REI Method" bare — see Section 4]` |
| Founder brand (authority faces) | Coach Edmund Tan & Cindior Ho **(shared — same real people)** | Coach Edmund Tan & Cindior Ho, but verify whether their agent-facing bio needs a distinct canonical description separate from the buyer-facing one (a `Person` entity can carry two `knowsAbout`/role contexts, but the two contexts should not be presented identically) |
| Audience | Property Climber (Singaporean owners, early-30s–mid-40s, $20k+/month household income, $2.5m+ serviceable) | `[FILL per Q1–Q5 — likely: named agent-tier identity term, e.g. "[FILL identity term]", production/licence-status hard filter per Q3]` |
| Problem/villain | The One-Property Trap (+ 4 supporting villains) | `[FILL per Q6–Q8]` |
| Transformation | Higher NAV, more options, long-term family freedom | `[FILL per Q9–Q11 — career-shaped or identity-shaped per Q10]` |
| Category | The Second Property Ladder™ | `[FILL per Q12–Q14 — must state relationship to The Second Property Ladder™ explicitly: subordinate, separate, or extension]` |
| Category law | Exit Before Entry™ | `[FILL per Q13]` |
| Method/mechanism steps | 5 Steps (Position Map, Direction Statement, Move Sequence, Selection Research, Climb Cadence) | `[FILL — same step-count/structure pattern is reusable as a *template shape*, not the actual step names]` |
| Offer ladder | Free content → diagnostic → Position Map session → Blueprint → Climb Review → Two-Property Club (parked) | `[FILL per Q15–Q18]` |
| Universal CTA | Position Map session (45 min) | `[FILL per Q42]` |
| Authority domain | thereimethod.com | `[FILL per Section 4 decision — new domain vs subdirectory]` |
| Vanity/campaign domains | secondpropertyladder.com, legacylaunch.com.sg | `[FILL per Q23–Q25]` |
| Retired/redirected domains | singaporerealestateinsider.com, 6figurepropertyprofits.com → thereimethod.com | `[FILL — none identified yet; re-run Phase 0 inventory for any dormant agent-facing domain]` |
| Parked domain | familylegacy.com.sg | `[FILL — none identified yet]` |
| Social handles | facebook.com/coachedmundtan, instagram.com/propertycoachedmundtan, youtube.com/@singaporerealestateinsider | `[FILL per Q30–Q32 — may reuse existing handles as a content vertical, or require new handles; LinkedIn is likely higher-priority for this audience than it was for buyers]` |
| GHL sub-account/CRM | Location `cyeYxFVQE1l73kO6S6Lx` ("Coach Edmund & Cindior") — shared with Changi Green today (flagged contamination) | `[FILL per Section 6 — recommend separate sub-account, not a third business line inside the same contaminated account]` |
| CRM field prefix | `spl_*` (Second Property Ladder diagnostic) | `[FILL — new unique prefix, e.g. Section 2 Q27; never reuse `spl_*` or `cg_*`]` |
| Proof line | "We built it before we advised it." | `[FILL per Q19–Q22 — likely: founders' own production/career proof, distinct verification bar for any income claim]` |
| GBP | share.google/bpyWTGgjlyNxt8Xiz (existing, [VERIFY] state) | `[FILL — Section 4/Phase 8: may not be GBP-eligible at all; do not assume a GBP is the right instrument]` |
| Banned words — universal (apply to every edition regardless of audience) | No income guarantees; no unverified performance claims; every $ figure `[VERIFY]`d against records; no fake reviews; no doorway pages; no schema for off-page content | Same — these are compliance/quality doctrines, not audience-specific vocabulary; they transfer to every future edition without modification |
| Banned words — edition-specific (Client Edition) | "Homeowner" (outright); "agent," "advice," "consultation," "project" (except one exempted phrase), "unit," "good buy," "investment property," "asset progression"; "This is advisory, not agency" | `[FILL — "agent" CANNOT be banned for the Agent Edition; it is the audience's own professional identity. Re-derive the entire banned-word list from the Agent Edition's own compliance/positioning needs — do not inherit the Client Edition list by default. Likely new bans: any bare income/earnings promise, "guaranteed," "passive income," "downline" (MLM-coded language), unqualified "join my team" without disclosure]` |

---

## 4. AGENT EDITION DOMAIN ARCHITECTURE PLACEHOLDER

### 4.1 Decision rule (apply before choosing a domain)

The Client Edition's one-authority-domain doctrine (D2) does not automatically dictate whether the Agent Edition gets its **own** authority domain or a **section of** thereimethod.com. Score the decision against four criteria, in this order — the first criterion that produces a clear "separate" signal should usually win, because entity contamination is asymmetric (easy to create, hard to undo once buyers or agents have seen cross-contaminated content):

| Criterion | Question | Signal toward SEPARATE domain | Signal toward SUBDIRECTORY of thereimethod.com |
|---|---|---|---|
| **1. Audience overlap** | Do property buyers and property agents search the same terms, land on the same pages, or benefit from seeing both offers? | Overlap is low — a buyer researching "should I sell my HDB" has no reason to see agent-recruitment content, and vice versa. → **Separate** | Overlap is high (e.g. the edition is genuinely "how The Second Property Ladder method applies if you're also an agent-investor") → subdirectory viable |
| **2. Brand risk of buyers seeing agent-recruitment content** | If a Property Climber visits thereimethod.com and discovers a "join our agent team" section, does that undermine the "advisory, not agency" trust position (already a flagged compliance risk under D7) by making the business look like it profits from recruiting salespeople, not just advising buyers? | High risk — recruitment-adjacent content sitting one click from buyer-trust content reads as a credibility problem even if legally compliant. → **Separate** | Low risk only if the Agent Edition offer has zero recruitment/income component and reads purely as thought-leadership (unlikely per Section 2 Q15–16) |
| **3. Entity separation (schema/AI graph)** | Does adding a second Organization-shaped offer under the same `Organization` `@id` risk Google/AI answer engines conflating "The REI Method" between two different services (consumer advisory vs agent training/recruitment) — the same ambiguity problem doc 02 already flags for "REI" vs the US retailer? | Two materially different services under one Organization schema node is exactly the kind of entity ambiguity this whole project was built to eliminate. → **Separate** Organization entity (new domain strongly preferred; a subdirectory sharing one Organization node inherits the ambiguity) | Only safe if the subdirectory is scoped as a clearly labelled `sub-brand`/`department` with its own schema `Organization` node distinct from the parent (technically possible but adds complexity GHL Websites may not support cleanly per doc 11's schema-budget constraints) |
| **4. Regulatory/compliance separation** | Does the offer trigger a different regulatory regime (recruitment advertising, MLM-prohibition screening, possible Financial Advisers Act boundary — Section 2 Q45–48) that is cleaner to manage on an entirely separate public surface, so a compliance issue on one edition cannot be read as attaching to the other? | Any "yes" on Q46–48 → **Separate**, with its own footer compliance block, its own disclaimers, and ideally its own legal review sign-off page | Only if legal counsel confirms the same compliance block suffices for both audiences (unlikely given Q45–48 remain open) |

**Working recommendation pending Section 2 answers:** on the evidence available today (undecided offer, likely recruitment component per the brief's framing "attracting them to a team"), **all four criteria point toward a separate domain and a separate Organization schema entity**, sharing only the two Person entities (Edmund Tan, Cindior Ho) via `sameAs` cross-reference — mirroring exactly how the Client Edition treats Changi Green as a hard-quarantined separate entity, except here the Person entities are legitimately shared (the same two humans really do run both lines) where Changi Green's Person/Organization entities should never touch the advisory graph at all. **This is a recommendation to re-confirm once Section 2 is answered, not a locked ruling** — if the Agent Edition offer turns out to be pure thought-leadership content with zero recruitment/income component, revisit criterion 2 and 4 and a subdirectory becomes defensible.

### 4.2 Domain Decision Table (placeholder — mirrors doc 03's structure)

| Domain | Role | Verdict | Rationale (against §4.1 criteria) | Key risks | Sequencing — check BEFORE acting |
|---|---|---|---|---|---|
| `[FILL — new domain candidate, e.g. thereagentedge.com / [agency-name]team.com — must be checked for availability and brand-collision per Q24]` | Authority hub for Agent Edition: founder-as-mentor pages, category hub for `[FILL category name]`, case studies, offer page | `[FILL — pending §4.1 scoring]` | `[FILL]` | `[FILL — likely: new-domain zero-authority cold-start problem, same as thereimethod.com faced; budget for a 12+ month authority-build runway, do not expect fast AEO citability]` | Confirm domain availability and registration; stand up before any Agent Edition ad spend; do NOT launch on a GHL preview URL (same lesson as Legacy Launch V2's undomained-launch mistake in doc 06) |
| `[FILL — vanity/funnel domain if a diagnostic-style lead magnet is built, per Q26]` | Vanity funnel host for `[FILL diagnostic name]` | `[FILL]` | Same bridge-page-canonical-to-hub pattern as `secondpropertyladder.com` | Doorway/duplicate risk if not noindexed correctly — reuse doc 03 §4–5 mechanics verbatim | Build only after the authority hub above is live |
| thereimethod.com (existing) | `[FILL — if criterion 2/4 confirm separation, thereimethod.com's ONLY relationship to the Agent Edition should be a single, clearly-labelled cross-link from the founders' bio pages ("Edmund and Cindior also run a training program for agents at [new domain]") — never a shared nav item, never shared schema `sameAs` pointing both directions as if they were one Organization]` | Do NOT host Agent Edition content | Hosting Agent Edition content here directly contradicts criteria 1–3 above | Buyer-trust dilution; entity ambiguity in Google/AI graphs | N/A — this domain stays Client-Edition-only per this recommendation |

---

## 5. AGENT EDITION PAGE MAP PLACEHOLDER

Mirrors the Client Edition's page-roadmap pattern from doc 04 — authority/entity layer, offer layer, demand-capture layer, compliance layer — scaled to a ~15-page starter spine (vs the Client Edition's 90-page, 3-month roadmap) because a second edition should launch minimally viable before scaling content volume.

```
[FILL DOMAIN — e.g. new-agent-domain.com]/
│
├── /                                    Homepage — category/offer entry, routes to [FILL universal CTA]
│
├── AUTHORITY / ENTITY LAYER
│   ├── /about                           [FILL business/program name] — the Agent Edition entity page
│   ├── /edmund-tan                      Founder page — REUSE canonical bio block from thereimethod.com/edmund-tan,
│   │                                    add an agent-audience-specific paragraph (production history, mentee results)
│   ├── /cindior-ho                      Founder page — same reuse pattern
│   └── /[FILL category slug]            CATEGORY/METHOD HUB — [FILL category name] explained
│
├── OFFER LAYER
│   ├── /[FILL offer page slug]          OFFER PAGE — single universal CTA (mirrors /position-map-session)
│   ├── /case-studies                    Proof hub — agent success stories (consent-gated per Q40–41)
│   │   └── /case-studies/[FILL — 3–5 stubs once Q19–20 answered]
│   └── /reviews                         Testimonials — [FILL: are agent reviews collected the same way as buyer
│                                        GBP reviews, or via LinkedIn recommendations / internal team testimonials?]
│
├── DEMAND-CAPTURE LAYER
│   ├── /guides                          [FILL — 3–5 guide stubs once Q36 keyword research exists, e.g.
│   │                                    "how-to-get-your-first-listing-singapore", "cea-exam-tips-singapore" [FILL]]
│   ├── /compare                         [FILL — e.g. "join-a-team-vs-go-solo-real-estate-singapore" [FILL]]
│   └── /faq                             Sitewide FAQ (AEO answer surface) — literal agent search phrasing preserved
│                                        per doc 05's rule, even where it includes words banned in OUR voice
│
├── UTILITY / TRUST
│   └── /contact                         Contact + booking (PDPA-compliant form — DISTINCT consent copy from the
│                                        buyer-facing form per Q50, since data subjects and data collected differ)
│
└── COMPLIANCE (sitewide footer + dedicated page)
    ├── /privacy
    ├── /disclaimer                      [FILL — per Q45/51: does this need the SAME CEA/PropNex compliance block
    │                                    as thereimethod.com, or a DIFFERENT disclosure because the audience is
    │                                    licensees, not consumers? Do not ship with a blank or assumed-safe block.]
    └── /pdpa                            PDPA 2012 + DNC consent (agent-data-specific copy)
```

**Page count check:** 4 authority + 2 offer/proof + 3 demand + 1 utility + 3 compliance = 13 pages minimum; add 2 more guide stubs once keyword research (Q36) lands real queries to hit the ~15-page starter spine. Do not build past 15 pages until the domain has at least one verified indexed page and a working CTA — mirror the Client Edition's phased build (entity foundation first, before volume).

---

## 6. AGENT EDITION FUNNEL MAP PLACEHOLDER

### 6.1 Lead magnet pattern reuse

The Client Edition's strongest strategic asset was the **diagnostic-style lead magnet** ("Which Step of The Second Property Ladder Are You On?") — a gamified, gated quiz that filters cold traffic into qualified vs disqualified before any human time is spent. This pattern transfers directly:

| Element | Client Edition instance | Agent Edition placeholder |
|---|---|---|
| Diagnostic name | "Which Step of The Second Property Ladder Are You On?" | `[FILL — e.g. "Which Stage of [Category] Are You At?"]` |
| Question count | 14 | `[FILL — 10–15 recommended, same gamified-not-tedious range]` |
| Gating logic | Gates + Checkpoints encode the buyer hard filter (income/serviceability) | `[FILL — encode the agent hard filter from Q3: production level, licence status, agency affiliation]` |
| CRM field prefix | `spl_*` | `[FILL — new unique prefix, per Q27]` |
| Downstream CTA | Position Map session (universal) | `[FILL per Q42]` |
| Build sequencing | Built AFTER the CRM fields exist as a standalone prerequisite (doc 06's ruling) | Same sequencing rule: create `[FILL prefix]_*` fields in GHL BEFORE any UI/quiz-builder work starts |

### 6.2 Offer ladder skeleton

```
Free content ([FILL — e.g. YouTube/LinkedIn agent-development content])
        ↓
Lead magnet: [FILL diagnostic name] (per §6.1)
        ↓
[FILL universal CTA — e.g. a "Team Fit Call" or "Mentorship Intro Session"]
        ↓
[FILL core paid offer — course / coaching program / team-join agreement]
        ↓
[FILL retention/upsell rung — e.g. annual mentorship renewal, advanced program]
        ↓
[FILL parked future offer, if any — log now, do NOT build, mirroring Two-Property Club's "parked" status]
```

Every rung must answer Section 2 Q15–18 before being built, and every dollar/production claim attached to a rung must clear the compliance screen in Section 2 Q45–49 before publish — this is not optional polish, it is the same `[VERIFY]`-before-publish discipline applied throughout docs 01–12, applied here to a higher-liability claim type (third-party income results).

### 6.3 GHL sub-account decision rule

**Recommendation: give the Agent Edition its own GHL sub-account, separate from `cyeYxFVQE1l73kO6S6Lx`.**

Rationale — the Changi Green contamination lesson, restated for this decision: the Client Edition's own GHL account already demonstrates the failure mode this recommendation prevents. One sub-account currently runs the advisory business AND Changi Green (180+ `cg_*` custom fields, a dedicated "Changi Green-Tenant Cycle" pipeline, contacts and reporting that must now be manually tagged out of every KPI in doc 12 to avoid silently polluting advisory metrics). That contamination was avoidable if Changi Green had been given its own sub-account from day one; it was not, and the cost is now a permanent tagging/segmentation tax on every future report.

Adding the Agent Edition as a *third* business line inside the same already-contaminated sub-account would compound the exact problem this project's Phase 12 (Measurement) had to build workarounds for. A separate sub-account costs a recurring GHL seat/location fee but buys: clean pipelines with no cross-line field collisions (no risk of an `[FILL prefix]_*` field ever being confused with `spl_*` or `cg_*`); clean reporting with no tag-based segmentation required; and — most importantly given Section 2's open compliance questions (Q45–48) — a clean audit boundary if a regulator or PropNex compliance review ever needs to examine the Agent Edition's marketing and CRM data in isolation from the advisory business's buyer data.

**Only reconsider a shared sub-account if:** the Agent Edition offer turns out to be genuinely minimal (a single lead-magnet-to-call funnel with no recruitment/income component) AND the operators are unwilling to pay for a second location fee AND a disciplined tagging convention is enforced from field #1 — the same conditions that were absent for Changi Green and caused the current contamination.

---

## 7. AGENT EDITION CONTENT CLUSTER PLACEHOLDER

Reuses the Client Edition's 7-cluster-type taxonomy (doc 05) verbatim as a *shape*; every example below is a stub pending Section 2's audience/keyword answers (Q33–38) — do not treat any bracketed example as a decision.

| Cluster type | Client Edition instance | Agent Edition example stub |
|---|---|---|
| **Best/top** (compliance-sensitive — never a self-proclaimed "best" claim) | "How to Choose Property Help" — reframed as a how-to-choose guide, not a "best advisor" claim | `[FILL, e.g. "how-to-choose-a-real-estate-team-to-join-in-singapore" — same compliance framing: how-to-choose, never "best team," per the same CEA-adjacent caution applied in doc 05]` |
| **Comparison** | `/compare/property-decisions-singapore` | `[FILL, e.g. "join-a-team-vs-go-independent-real-estate-singapore", "propnex-vs-[other-agency]-for-new-agents" (verify defamation/comparative-advertising exposure before publishing any named-competitor comparison — the Client Edition has no equivalent risk since it never names competing advisors)]` |
| **Timing** | "When to Sell Your HDB After MOP" (cooling-measure/regulatory timing) | `[FILL, e.g. "best-time-to-become-a-property-agent-in-singapore", "cea-exam-schedule-and-timing" — date-stamp any regulatory/exam-schedule content per the same D7 discipline]` |
| **Mistakes** | "Second-Property Mistakes" | `[FILL, e.g. "common-mistakes-new-property-agents-make-in-singapore"]` |
| **Framework** | "The Second Property Ladder Framework" | `[FILL — the Agent Edition's own named method, per Q12–14]` |
| **Local** | "Best HDB Towns to Upgrade From" | `[FILL, e.g. region/estate-specific agent-territory content if the offer has a geographic-territory angle — otherwise this cluster type may not apply; do not force it]` |
| **Long-term** | "Property Retirement & Legacy Planning" | `[FILL, e.g. "building-a-long-term-real-estate-career-in-singapore", "from-agent-to-team-leader-career-path"]` |

**Note carried over from doc 05:** FAQ questions should preserve literal agent search phrasing even where it uses a word banned from the business's own voice (e.g. a real query like "is being a property agent a pyramid scheme" should be answered honestly on-page, not avoided — this is exactly the AEO discipline the Client Edition applies to buyer queries containing "decoupling" or "sell one buy two").

---

## 8. REPLICATION QA CHECKLIST

Generalised from the Writing Standards (Master Brief §5) and the recurring quality gates visible across docs 01–12 (see Concerns note in the Executive Summary — `16_MASTER_QA_CHECKLIST.md` does not yet exist to cross-check against). Run all 15 points, plus the entity-separation gate, before any Agent Edition deliverable is considered done.

1. **Market-context grounding.** Does every regulatory/market reference carry the correct Singapore-specific framing for *this* audience (CEA licensing rules and PropNex/agency structures for the Agent Edition, vs HDB/ABSD/MOP for the Client Edition) — and is every regulatory figure date-stamped and `[VERIFY]`-flagged?
2. **Specificity over genericism.** Does the deliverable name real pages, real slugs, real handles, real GHL object IDs — or does it fall back to filler ("post consistently," "build trust")? Every placeholder in this template must be filled with something concrete before it counts as done.
3. **Table-for-inventory, prose-for-reasoning.** Are decisions and inventories tabulated, with reasoning in prose only where genuine judgement is being explained?
4. **Vocabulary and banned-word discipline.** Does every piece of copy use the *this edition's* locked vocabulary and banned-word list (Section 3), not the Client Edition's list by inherited habit? Re-check every sample headline/meta description explicitly — banned words hide in the smallest fields.
5. **Sequencing stated.** Does every recommendation say what must happen first and what depends on it (e.g. CRM fields before diagnostic UI, domain live before handle renames)?
6. **CSV hygiene.** Do companion CSVs use comma separation, a header row, quoted fields containing commas, UTF-8 encoding, and the exact column set specified for that deliverable?
7. **Named sources, no invented URLs.** Where platform rules are cited (Google Search Central, CEA guidance, PDPA, MAS/Financial Advisers Act), is the source named generically and correctly, with no fabricated specific URL or clause number?
8. **British/Singapore spelling; SGD currency.** Consistent throughout.
9. **No spam tactics.** No fake reviews, no doorway pages, no thin/duplicate content, no schema markup for content that does not actually exist on the page.
10. **`[VERIFY]` discipline on every unverified figure.** Every dollar amount, production number, income claim, or statistic carries `[VERIFY]` until confirmed against a real record — with EXTRA weight for this edition given the higher compliance exposure of third-party income claims (Section 2 Q45–49).
11. **PDPA/consent completeness.** Does every form and every named case study have its consent mechanism specified (scope, anonymisation level, withdrawal process), and is it edition-appropriate (agent data ≠ buyer data)?
12. **Single CTA per page.** Does every page in the page map route to exactly one universal CTA, with no competing calls-to-action diluting the funnel?
13. **Canonical/noindex hygiene.** Does every vanity/funnel domain in the domain map specify its bridge page, its canonical target, and its noindex scope explicitly — no funnel step left ambiguously indexable?
14. **Internal link bridging.** Does every demand-capture page link up to a category/authority page and a conversion object (tool/CTA), mirroring the Client Edition's two-layer demand-capture architecture?
15. **Baseline-before-changes.** Before any Agent Edition asset goes public, has a baseline been captured (AI Visibility Test Bank equivalent, GA4/GSC state, existing handle/domain state) so "before" and "after" can actually be compared, per Phase 12's discipline?

**Entity separation check (Agent Edition-specific gate, run in addition to the 15 above):** Does this deliverable — page, schema block, social post, or funnel — create any shared `sameAs`, shared Organization `@id`, shared nav link, shared pipeline, or shared custom-field prefix between the Agent Edition and either (a) the Client Edition advisory business or (b) Changi Green? If yes, does Section 4's decision rule actually justify that specific sharing (e.g. the two shared Person entities), or has contamination crept in by convenience? **Any "crept in by convenience" answer fails this gate outright** — this is the single check this entire template exists to enforce, and it is the one most likely to be silently skipped under launch-date pressure.

---

## QUESTIONS TO CLARIFY

1. Has the Agent Edition's exact offer (course vs coaching vs team recruitment vs hybrid) been decided yet, or does Phase 1 of the Agent Edition build start with that decision still open? (Section 2 Q15–16 must be answered before Section 4's domain recommendation can be finalised — the current recommendation assumes a recruitment component exists.)
2. Do the founders have any existing agent mentees, downline, or team members today whose results could seed the first proof assets (Section 2 Q20), or is proof entirely to-be-built?
3. Has PropNex been consulted about whether/how its own agents can be marketed to for recruitment by two of its own licensed salespersons, and does PropNex have an internal policy governing this (Section 2 Q46, Q52)?
4. Is there Founder bandwidth to run a second repositioning build (research → 12 phases) concurrently with executing the Client Edition's own 90-day plan, or must the Agent Edition build wait until the Client Edition's Phase 13 calendar substantially completes?
5. Does `16_MASTER_QA_CHECKLIST.md` exist by the time this document is reconciled by the orchestrator, and if its structure differs from Section 8 above, which version wins?

## DEPENDENCIES

- **Client Edition Phase 3 (Domain) and Phase 11 (Technical) must be substantially live** before Agent Edition domain work starts, so the "how does GHL Websites handle a second domain/site" question (schema budget, per-page character limits) is answered from real experience, not theory.
- **Client Edition Phase 7 (Social)** should be far enough along that the founders' existing handles carry consistent bio/positioning language before any Agent Edition cross-link from those bios is added (Section 4.2) — cross-linking from a still-fragmented profile just adds a ninth confusing token, not a tenth clean one.
- **Legal/compliance review (Section 2 Q45–48) is a hard blocker**, not a parallel-track item, for any deliverable involving recruitment or income claims — do not sequence content production ahead of this review.
- **A GHL sub-account decision (Section 6.3)** must be made before any `[FILL prefix]_*` custom fields are created — creating fields in the wrong sub-account first and migrating later recreates the exact Changi Green cleanup burden this template is designed to avoid.
- **This document itself depends on Section 2 being answered** by the operators (founders) before Sections 4–7's placeholders can be converted from `[FILL]` into real, build-ready content — this file is the empty form, not the filled one.

## FIRST 5 ACTIONS

1. Put the 52 questions in Section 2 in front of the founders as a structured intake session (mirrors how the Client Edition's own strategy docs were rank-ordered before trusting any of them) — do not let the team start building pages or funnels before this intake is answered in writing.
2. Run a Phase-0-equivalent asset inventory specifically for the Agent Edition: search for any dormant domain, handle, funnel, or content that might already exist related to agent training/recruitment (mirroring the discipline that found Changi Green living inside the same GHL account unexamined).
3. Get a legal/compliance read on Section 2 Q45–48 (CEA recruitment-ad rules, PropNex internal policy, MLM-Prohibition-Act exposure, Financial Advisers Act boundary) before any public-facing Agent Edition asset is drafted — treat this as gating, not parallel work.
4. Decide the GHL sub-account question (Section 6.3) and, if a new sub-account is chosen, provision it and define the `[FILL prefix]_*` field-naming convention before any CRM fields are built.
5. Once Section 2 is answered, reconvene to convert Sections 4–7 of this document from `[FILL]` placeholders into a real, build-ready Agent Edition domain/page/funnel/cluster plan — at that point Phases 1–13 of Section 1's framework can be re-run in full for the Agent Edition.
