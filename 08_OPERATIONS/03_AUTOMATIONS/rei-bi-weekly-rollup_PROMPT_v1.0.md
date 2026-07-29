# REI BI-WEEKLY ROLLUP SUMMARY — FILLED-IN EXAMPLE

Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none — copied as-is
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\Templates\rei-bi-weekly-rollup_PROMPT_v1.0` (no file extension in legacy Drive; saved here as `.md`)

## Applied Master Scheduled Task Template v1.0

---

## SECTION 1: TASK HEADER

**Task ID:** rei-bi-weekly-rollup  
**Task Name:** REI Bi-Weekly Rollup Summary (Internal + External Digest)  
**Owner:** Edmund Tan  
**Created:** 2026-06-20  
**Last Updated:** 2026-06-20  
**Status:** ACTIVE  
**Version:** 1.0  
**Scheduler Type:** Cowork Scheduled Task (bi-weekly)

---

## SECTION 2: TASK OVERVIEW & PURPOSE

### Business Objective
Every other Sunday night, synthesize 2 weeks of content briefs + library learnings into:
1. **Part A (Internal):** Strategic trends, format performance, CTA conversion, emerging patterns for Edmund's decision-making
2. **Part B (External):** Shareable digest for Cindior + team showing market signals, content wins, library growth, next week's opportunities

### Key Benefits
- **Strategic clarity:** Edmund sees 2-week patterns, performance trends, what's working
- **Team alignment:** Cindior + team get digestible summary (not raw data, actionable insights)
- **Compounding intelligence:** Library patterns emerge, competitive positioning clarifies
- **Momentum tracking:** Measure which formats/CTAs/segments drive results
- **Forward planning:** Next week's content prep informed by this week's learnings

### Stakeholders
**Reviews:** Edmund Tan (strategy review)  
**Acts On:** Cindior Ho (shares with content team, informs next week's plan)  
**Consumes:** Content team (adjust strategy based on rollup), library updates

### Success Metric
- Rollup completed by Sunday 11 PM (on schedule)
- Part A: Clear trends identified + actionable insights
- Part B: Shareable, digestible format (<500 words)
- Library sections updated based on 2-week learnings
- Team acts on recommendations within 24 hours of receiving

---

## SECTION 3: EXECUTION SCHEDULE

**Frequency:** Bi-weekly  
**Day & Time:** Every other Sunday at 11:00 PM Singapore time (UTC+8)  
**Pattern:** Weeks 1-2, then skip Week 3, then Weeks 4-5, then skip Week 6 (constant rolling bi-weekly)  
**Cron Expression:** `0 23 * * 0` [Note: Manual bi-weekly management required; set manually for odd/even weeks]  
**Timezone:** Singapore (UTC+8)  
**Estimated Duration:** 1-1.5 hours per run

### Run Requirements
- **App State:** Can run when app is closed (results reviewed Monday morning)
- **Network:** Internet required (Google Drive access, data compilation)
- **Tools/Connectors Needed:** Google Drive, Library access, prior 2 weeks' briefs
- **Authentication:** Google Drive (pre-authorized)

---

## SECTION 4: INPUT DATA SOURCES

### Primary Input
- **Prior 2 weekly briefs:** Last 2 Mondays' briefs (e.g., June 16 + June 23)
- **Library sections:** CaseStudyRegistry, KeywordTrends, CompetitorIntel, CreatorPatterns
- **Performance data:** YouTube Analytics (if available), WhatsApp reply logs, CTA conversion tracking

### Reference Materials
- **Belief Block Playbook:** What blocks did we encounter?
- **Content Gap Map:** What's our positioning vs competitors?
- **Creator Format Patterns:** How did Formats A, B, C perform this 2 weeks?

---

## SECTION 5: PROCESSING & ANALYSIS

### Step 1: Data Collection
**Extract from past 2 briefs:**
- All 10 angles (5 per week)
- Ranking, belief blocks addressed, CTAs used
- Library sections updated

**Compile performance data:**
- YouTube engagement rates (if published)
- WhatsApp CTR per segment
- CTA conversion counts
- Comment sentiment/feedback

### Step 2: Filtering & Scoring
**Identify patterns:**
- Which formats drove highest engagement? (A vs B vs C)
- Which CTAs converted best? (POSITION > LEGACY > UNLOCK > AUDIT?)
- Which segments engaged most? (L2 > L3 > L4?)
- Which themes/signals dominated?
- Which competitors moved?

### Step 3: Synthesis & Analysis
**Synthesize into narrative:**
- What worked? Why?
- What didn't? What to adjust?
- Emerging keywords/trends from 2 weeks
- Competitor positioning shifts
- Library growth summary

### Step 4: Output Generation
**Part A (Internal):** Detailed trends analysis for Edmund (strategic)  
**Part B (External):** Digestible summary for Cindior + team (tactical)

---

## SECTION 6: OUTPUT FORMAT & STRUCTURE

### File Naming Convention
`[YYYY-MM-DD] Bi-Weekly Rollup Summary` (Part A)  
`[YYYY-MM-DD] Weekly Digest (Cindior + Team)` (Part B)  
Example: `[2026-06-22] Bi-Weekly Rollup Summary`

### Output Locations
**Part A:** Google Drive `/Weekly Contents/[YYYY-MM-DD] Bi-Weekly Rollup Summary.md`  
**Part B:** Google Drive `/Weekly Contents/[YYYY-MM-DD] Weekly Digest (Cindior + Team).md`

### Document Structure

**PART A — INTERNAL TRENDS DOCUMENT**

1. **Header:** Date range, week numbers, data sources compiled
2. **Dominant Signals:** Which 3-5 signals/themes dominated these 2 weeks?
3. **Format Performance:** A vs B vs C — which drove engagement?
4. **CTA Conversion Ranking:** POSITION > LEGACY > UNLOCK > AUDIT (with %)
5. **Segment Engagement:** L2 vs L3 vs L4 reply rates, dominant segments
6. **Emerging Keywords/Patterns:** New search terms rising, pattern shifts
7. **Competitor Moves:** What did Marcus Luah, JNA, StackedHomes do this 2 weeks?
8. **Library Growth:** New patterns documented, new case studies, new creator formats discovered
9. **Strategic Insights:** What does Edmund need to know for next week's strategy?
10. **Recommendations:** Adjust angle selection? Format weighting? CTA messaging?

**PART B — EXTERNAL DIGEST (Shareable)**

1. **Key Market Signals This Week:** 2-3 biggest findings (plain language, no jargon)
2. **Content Performance Snapshot:** Top-performing angle + why, audience segments that engaged
3. **What's Trending:** Emerging keywords, competitor positioning shifts, market sentiment shifts
4. **Library Growth:** New patterns discovered, new case studies, new creator formats tested
5. **Next Week's Opportunities:** Recommended angles to prepare, thematic continuity from this 2 weeks, early signals to watch
6. **Actionable Next Steps for Cindior/Team:** 2-3 concrete actions based on this rollup

---

## SECTION 7: METRICS & KPIs TO TRACK

### Output Metrics
- **Metric 1:** Number of patterns identified per rollup
  - Target: 5-10 patterns
- **Metric 2:** Quality of insights (qualitative review by Edmund)
  - Target: Actionable + novel (not obvious)

### Downstream Metrics
- **Metric A:** % of recommendations acted on by team
  - Target: >80% adoption within next week
- **Metric B:** Impact on next week's brief quality
  - Target: Learnings from rollup visible in improved Rank 1 angles

### Tracking Location
Library / CaseStudyRegistry / Performance logs

---

## SECTION 8: UPDATE CADENCE & DEPENDENCIES

### Primary Update Schedule
- Rolls up every 2 weeks (Sunday 11 PM)
- Updates library sections based on findings
- Triggers any strategy adjustments for next Monday

### Upstream Dependencies
- Both weekly briefs must be complete (Monday briefs from weeks 1-2)
- Performance data (YouTube views, WhatsApp replies) must be available

### Downstream Outputs
- Edmund uses Part A for strategic decisions
- Cindior shares Part B with team
- Findings inform next Monday's brief (improved angle selection)

---

## SECTION 9: CONSTRAINTS & RULES

### Hard Boundaries
- [ ] Both weeks' data must be consolidated (no cherry-picking one week)
- [ ] Performance claims must be backed by data (no speculation)
- [ ] Part B must be <500 words (digestible for team)

### Soft Guidelines
- Part A can be 1,500-2,000 words (detailed for Edmund)
- Focus on learnings over raw metrics
- Tie recommendations to next week's brief

---

## SECTION 10: HANDOFF & APPROVAL WORKFLOW

### Who Reviews & Approves
**Primary Reviewer:** Edmund Tan  
**Secondary Reviewer:** Cindior Ho (reviews Part B before sharing with team)

### Review Checklist
- [ ] Part A: Accurate data, clear trends, actionable insights
- [ ] Part B: Digestible, no jargon, actionable for team

### Approval Decision
✅ **APPROVE** — Part B shared with team immediately. Part A filed for strategic review.  
⚠️ **REQUEST CHANGES** — Specific adjustments requested. Resubmit within 2 hours.

### Timeline
- Task completes: Sunday 11 PM
- Review begins: Monday morning
- Approval deadline: Monday 10 AM
- Part B shared with team: Monday 10 AM

---

## SECTION 11: CHANGE LOG & VERSION CONTROL

### Version History

**v1.0** — 2026-06-20
- Initial version created
- Both Part A + Part B structure defined
- Status: ACTIVE

---

## END REI BI-WEEKLY ROLLUP SUMMARY — FILLED-IN EXAMPLE v1.0