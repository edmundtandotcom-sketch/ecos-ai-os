> **ARCHIVED 2026-07-30 — superseded by `08_OPERATIONS/03_AUTOMATIONS/rei-weekly-content-brief_SKILL.md` v2.2.** Kept verbatim as rollback/history per AI OS file rule (archive the previous approved version before replacing). Reasons for supersession: (1) v2.1 scanned YouTube only for shallow format study, not real repurposing — v2.2 merges it into the same signal pool as articles, one ranked output instead of a proposed separate third routine; (2) v2.1's documented output path (`01_PROPERTY_BUSINESS/03_SHARED_PROPERTY_ASSETS/.../Weekly Contents/`) no longer exists after the 2026-07-20 workspace restructure — verified live output was already landing in `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/`, which v2.2 documents as canonical; (3) this task was targeted at the "Cowork" scheduler, which does not appear in this machine's live Claude Code scheduled-tasks list and was very likely not actually firing — v2.2 is registered as a Claude Code scheduled task instead, consolidating with the sibling `singapore-property-ads-brief` routine on one inspectable scheduler.

---

name: rei-weekly-content-brief
description: REI Unified Weekly + Bi-weekly Intelligence Task — Monday 9 AM (combines brief + rollup)
---

<!--
AI OS MIGRATION HEADER
Version: v2.1 (re-scoped, matches LIVE source)
Status: APPROVED MASTER
Date: 2026-07-11
Supersedes: v2.0 (2026-07-10 copy, carried the pre-ruling SI-06/Mash-up classification model)
Sources: `H:\Shared drives\00_E.C.O.S\Scheduled\rei-weekly-content-brief\SKILL.md`
Note: YAML frontmatter above is functional (read by the Cowork scheduler) — left untouched.
RE-SCOPED 2026-07-11 per Edmund's O14 ruling (total removal of Family Legacy/Mash-up) — Decision 067. This mirror is edited identically to the LIVE scheduled copy at `H:\Shared drives\00_E.C.O.S\Scheduled\rei-weekly-content-brief\SKILL.md` (both now read v2.1). SI-06 is also RETIRED outright as a Strategic Intent classification per Edmund's O15 ruling (Decision 067) — family/idle-capital situations classify under SI-05 or standard intents inside A0–A2 engagements.
-->

> **Re-scoped 2026-07-11 per Edmund's O14 ruling (total removal of Family Legacy/Mash-up) — Decision 067.** All Family Legacy, Mash-up, and SI-06 classification has been removed from this automation. Angles now classify under SI-05 (decouple / Legacy Launch) or Evergreen Authority. Family situations that surface in scans route into standard SI-05 / A1–A2 engagement content, not a separate family door.

# REI UNIFIED WEEKLY + BI-WEEKLY INTELLIGENCE TASK
## Version: 2.1 (Monday 9 AM Consolidated — SI-06/Mash-up removed, Decision 067)

**Task ID:** rei-weekly-content-brief
**Schedule:** Every Monday, 9:00 AM
**Execution Type:** One unified task for weekly brief + conditional bi-weekly rollup

---

## OVERVIEW

Every Monday at 9 AM, execute BOTH:
- **PART A (Always)**: Weekly Content Intelligence Brief — fresh 7-day market signals
- **PART B (Conditional)**: Bi-weekly Rollup — IF 2+ weeks of library data exist

Do NOT run separate tasks. One execution = both outputs (or just Part A if rollup condition not met).

---

## REAL DATA EXTRACTION — LIVE AUTOMATION

**DO NOT use synthesis fallback. Extract actual live data:**

### Chrome Extension Automation (Required)
- Navigate directly to each source URL
- Extract video transcripts, forum comments, ad creatives, article text
- Pull meta-data: publish date, view count, engagement metrics
- Save raw data → apply analysis second

### Tier 1 Priority (Live Scrape)
1. **URA (ura.gov.sg)** — latest condo transactions, price indices
2. **EdgeProp** — new project launches, market commentary
3. **StackedHomes** — articles, analysis, case studies
4. **99.co** — condo listings, price trends, market pulse
5. **MoneySmart** — mortgage rates, interest trends
6. **PropNex news** — market releases, case studies

### Tier 2 Priority (Content Creators)
1. **Marcus Luah YouTube** — video scripts, thumbnails, engagement
2. **JNA YouTube** — video format, narrative patterns
3. **StackedHomes YouTube** — content structure, CTA placement
4. **Cindior's archive** — previous successful angles, performance patterns

### Tier 3 Priority (Signals)
1. **Google Trends** — keyword velocity week-over-week
2. **Reddit r/singapore** — sentiment, pain points, belief blocks
3. **Hardwarezone forums** — property discussion threads
4. **Facebook groups** — decoupling / next-move prospect conversations
5. **Telegram channels** — investor networks, deal talk
6. **LinkedIn Singapore property** — professional signals
7. **YouTube comments** — audience objections, questions
8. **Instagram/TikTok** — viral formats, creator styles
9. **Google News alerts** — breaking property news

---

## PART A: WEEKLY CONTENT INTELLIGENCE BRIEF (Always Run)

### STEP 1: Extract & Rank Weekly Signals (Mon-Sun data)
- Pull 8-12 signals from Tier 1 sources (URA, EdgeProp, StackedHomes, 99.co)
- Extract 4-6 creator insights (Marcus Luah, JNA, top performer formats)
- Scan Tier 3 for emerging sentiment shifts, keyword spikes
- **Minimum data required:** actual numbers, quotes, links, timestamps

### STEP 2: Apply 6-Step Angle Filter
For each signal, ask:
1. **REI Method alignment?** (R → E → I applicable?)
2. **Client belief shift?** (addresses a false belief?)
3. **Content gap?** (do competitors cover this well?)
4. **Emotional hook?** (triggers urgency or FOMO?)
5. **SI-05/Evergreen relevance?** (decouple / first-portfolio-move angle, or evergreen authority?)
6. **Proof/data available?** (can we cite sources?)

**Score:** 0-6 points. Keep only 6+ signals.

### STEP 3: Rank & Segment by Strategic Intent
- **SI-05 (Legacy Launch / Decouple)**: First portfolio move, decoupling mechanics, new investor psychology
- **Evergreen Authority**: Market data, category-law, exit-before-entry angles not tied to a specific life-stage trigger

Rank each angle:
- **Rank 1**: Highest urgency + strongest proof + clearest REI fit
- **Rank 2-3**: Strong secondary angles
- **Rank 4-5**: Evergreen/supporting angles

### STEP 4: Generate YouTube Scripts (3 Format Variations per Angle)

**Format A — Fast-Paced Data-Driven**
- Hook (0:00-0:15): Shocking statistic or gap identification
- Data Dump (0:15-1:30): 3-4 key numbers, trends, comparisons
- Implication (1:30-2:00): What this means for condo owners
- CTA (2:00-2:15): "Watch next: [Related angle]" or "Book audit" (AUDIT code)
- Length: ~2-3 minutes

**Format B — Narrative/Story-Led**
- Hook (0:00-0:20): Real client scenario or market moment
- Context (0:20-1:15): Why this happened, historical context
- Opportunity (1:15-2:00): Three specific moves condo owners can make
- Social Proof (2:00-2:15): Past results or case study hint
- CTA (2:15-2:30): "Let's map your moves" (POSITION or LEGACY code)
- Length: ~3-4 minutes

**Format C — Authority Breakdown / Myth-Bust**
- Myth Hook (0:00-0:15): Common belief + why it's wrong
- Evidence (0:15-1:45): Data, expert contradiction, real examples
- Correct Framework (1:45-2:15): REI Method applied to this situation
- Next Step (2:15-2:30): "Here's what you should do instead"
- CTA (2:30): Knowledge gap identifier (UNLOCK code)
- Length: ~2.5-3 minutes

**Modeling:** Research top creators (Marcus Luah, JNA, StackedHomes, etc.) — mirror their opening pace, data presentation, CTA timing, but keep REI framing.

### STEP 5: Generate WhatsApp Broadcast Segments

Create 3 separate WhatsApp messages (not one blast — segmented by intent level):

**Segment 1 (High Intent)**: Existing clients, past enquiries, warm leads
- Hook: Directly relevant to their stated goal
- Data: 1-2 key numbers
- Action: "Reply AUDIT for full analysis"

**Segment 2 (Medium Intent)**: Engaged followers, video watchers, engagement history
- Hook: Market observation + opportunity framing
- Data: Single compelling stat
- Action: "Reply POSITION to learn your next move"

**Segment 3 (Cold/Remainder)**: Broad audience, new followers
- Hook: General market insight
- Data: None (pure narrative)
- Action: "Watch [Video Link] for details"

### STEP 6: Build Library Entries

For each of the 5 ranked angles, add to **REI_Content_Research_Resources** (Google Drive):

**Location**: `REI_Content_Research_Resources/[Angle Name]_YYYY-MM-DD.md`

**Content**:
- Angle summary (1 paragraph)
- Source links + timestamps
- Competitor coverage (who else is covering this?)
- Belief block addressed
- Script format performance prediction
- CTA recommendation
- Follow-up angle suggestions

### STEP 7: Save Weekly Output

**File naming**: `[WEEK] REI Weekly Brief — 2026-06-20.md`
**Location**: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\03_SHARED_PROPERTY_ASSETS\03_SHARED_MARKET_RESEARCH\Weekly Contents\`

**Output structure**:
```
# REI Weekly Content Intelligence Brief
**Week of:** June 16-22, 2026

## Executive Summary (for Edmund)
- Top 3 signals and why
- Recommend focus angle
- Expected content velocity

## Ranked Angles (1-5)
For each angle:
- Signal summary
- REI Method fit (R/E/I application)
- Belief block addressed
- YouTube scripts (Format A, B, C)
- WhatsApp segments (1, 2, 3)
- Keyword opportunities
- Competitor gaps
- Next steps

## Library Growth
- 5 new angle entries created
- Patterns observed
- Creator format insights

## Production Sprint (Rank 1 Angle)
- 10-day content calendar
- Scripts ready
- Assets needed
- Posting schedule
```

---

## PART B: BI-WEEKLY ROLLUP (Conditional — Only if 2+ Weeks Data Exist)

**Condition Check:**
- Look at `REI_Content_Research_Resources/` folder
- Count how many weekly brief outputs exist
- If ≥ 2 weeks of data: **PROCEED**
- If < 2 weeks: **SKIP and note in output**

### STEP 1: Synthesize 2-Week Patterns

Pull all angle entries from past 2 weeks. Identify:
- **Dominant signals**: Which 2-3 topics recurred?
- **Format winners**: Which script formats drove engagement?
- **CTA ranking**: Which codes (POSITION, LEGACY, AUDIT, UNLOCK) converted?
- **Segment performance**: Which WhatsApp segments had highest reply rate?
- **Emerging keywords**: New search terms trending up week-over-week?
- **Competitor moves**: New angles launched by competitors?
- **Library growth**: Total new angles, patterns, creator insights added

### STEP 2: Generate Part B Output (Internal Brief for Edmund)

**File naming**: `[ROLLUP] REI Bi-weekly Insights — 2026-06-20.md`
**Location**: Same Weekly Contents folder
**Audience**: Edmund + internal strategy

**Content**:
```
# REI Bi-Weekly Intelligence Rollup
**Period:** June 8-22, 2026 (2 weeks)

## Dominant Signals (What Stuck?)
- Signal A: [recurring theme, proof, client relevance]
- Signal B: [recurring theme, proof, client relevance]
- Signal C: [emerging pattern]

## Format Performance
- Format A (Data-Driven): X engagements, Y conversion rate
- Format B (Narrative): X engagements, Y conversion rate
- Format C (Myth-Bust): X engagements, Y conversion rate
→ **Recommendation**: Lock in [winner] for next week

## CTA Conversion Ranking
1. POSITION: X% reply rate (highest urgency)
2. LEGACY: X% reply rate
3. AUDIT: X% reply rate
4. UNLOCK: X% reply rate

## Segment Engagement
- Segment 1 (High Intent): X% response
- Segment 2 (Medium Intent): X% response
- Segment 3 (Cold): X% response

## Keyword Velocity (Week 1 → Week 2)
- [Keyword 1]: +15% searches (rising)
- [Keyword 2]: -5% searches (cooling)
- [Keyword 3]: NEW (emerging)

## Competitor Moves
- [Competitor] launched [angle] — white-space opportunity in [gap]
- [Creator] posted [format innovation] — consider adopting

## Library Growth
- 10 new angle entries (2 weeks × 5 angles/week)
- 3 pattern discoveries added to Pattern Intelligence section
- 2 new creator format insights
- Belief block reframe playbook expanded by X entries

## Strategic Insights
- Market is shifting toward [observation]
- Client inquiries cluster around [pain point]
- Content opportunity: [white-space angle not yet covered]
- Next week focus recommendation: [which angle to lead with]

## Tactical Next Steps
1. Double down on [highest-performing format]
2. Test [emerging keyword] in next week's brief
3. Add competitor insight to library: [note]
4. Prepare [white-space angle] for Rank 1 next week
```

---

## EXECUTION CHECKLIST

### Pre-Execution
- [ ] Open Google Drive, navigate to `Weekly Contents` folder
- [ ] Open `REI_Content_Research_Resources` folder (library)
- [ ] Prepare Chrome automation for live scraping (URA, EdgeProp, 99.co, YouTube, etc.)

### Part A Execution (Every Monday)
- [ ] Extract 8-12 signals from Tier 1 (with links, timestamps, data)
- [ ] Apply 6-step filter, keep 6+ signals
- [ ] Rank and segment by SI-05/Evergreen Authority
- [ ] Generate YouTube scripts (Format A, B, C for top 5 angles)
- [ ] Generate WhatsApp segments (Seg 1, 2, 3 for each angle)
- [ ] Create 5 library entries in Research folder
- [ ] Save Part A output to Weekly Contents folder
- [ ] Verify all links are live and data is recent

### Part B Execution (Conditional)
- [ ] Check if 2+ weeks of data exist (count weekly outputs)
- [ ] If YES: synthesize patterns, generate rollup brief, save to Weekly Contents
- [ ] If NO: note in Part A output "Rollup scheduled for next execution (data accumulation in progress)"

### Post-Execution
- [ ] Save all outputs to Google Drive
- [ ] Notify Edmund of completion
- [ ] Note any technical issues (Chrome automation failures, source access problems)

---

## CONSTRAINTS & RULES

1. **No synthesis fallback** — Real data only. If a source is unreachable, note it and move to next source.
2. **Chrome automation required** — For video transcript extraction, live comment scraping, ad creative pulls. Do not rely on descriptions or summaries.
3. **Bi-weekly condition is strict** — Only generate Part B if 2 full weeks of weekly outputs exist. Don't extrapolate.
4. **CTA codes matter** — Every angle must have a mapped CTA (POSITION, LEGACY, AUDIT, UNLOCK). Track which codes drive responses.
5. **Library is living** — Every angle entry becomes a pattern reference for future briefs. Build redundancy into library structure so future briefs can discover related angles.
6. **Segmentation is non-negotiable** — Never mass-blast WhatsApp. Always create 3 segments with unique hooks and CTAs.
7. **Competitor tracking is ongoing** — Library includes competitor move log. Update weekly.

---

## CHANGELOG

**v2.1 (2026-07-11) — Decision 067 (O14 ruling)**
- Removed all Family Legacy, Mash-up, and SI-06 classification from angle filtering and segmentation
- Angle Filter Q5 and STEP 3 re-scoped to SI-05 (decouple) + Evergreen Authority
- Tier 3 Facebook-groups scan target re-scoped from "Family Legacy prospect conversations" to "decoupling / next-move prospect conversations"
- Execution checklist updated to match

**v2.0 (2026-06-20)**
- Consolidated weekly brief + bi-weekly rollup into ONE Monday 9 AM task
- Added live Chrome automation requirements (no synthesis fallback)
- Made bi-weekly rollup conditional (only if 2+ weeks data exist)
- Expanded Tier 1/2/3 source list with specific URLs
- Added execution checklist
- Streamlined file naming and storage locations

**v1.0 (2026-06-15)**
- Initial weekly brief task created
- 6-step angle filter defined
- Three YouTube script formats established
- WhatsApp segmentation defined
