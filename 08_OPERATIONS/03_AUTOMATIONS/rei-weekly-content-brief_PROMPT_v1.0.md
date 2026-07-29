# REI WEEKLY CONTENT INTELLIGENCE BRIEF — FILLED-IN EXAMPLE

Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none — copied as-is
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\Templates\rei-weekly-content-brief_PROMPT_v1.0` (no file extension in legacy Drive; saved here as `.md`)

> ⚠️ **RETIRED CLASSIFICATION — HISTORICAL RECORD (Decision 067, 2026-07-11, Edmund's O14/O15 rulings):** this template still classifies content by SI-06 (Family Legacy) and Mash-up. Those doors, SI-06 as a Strategic Intent code, and the A3/A4 ascent levels are all RETIRED — do not build new briefs to those angles. The live automation and its AI OS mirror have been re-scoped to v2.1 (SI-05 + Evergreen Authority) — see `rei-weekly-content-brief_SKILL.md`. This filled-in example is kept as a REGISTRY/historical record of the pre-retirement format; body left verbatim, not rewritten.

## Applied Master Scheduled Task Template v1.0

---

## SECTION 1: TASK HEADER

**Task ID:** rei-weekly-content-brief  
**Task Name:** REI Weekly Content Intelligence Brief  
**Owner:** Edmund Tan  
**Created:** 2026-06-20  
**Last Updated:** 2026-06-20  
**Status:** ACTIVE  
**Version:** 1.0  
**Scheduler Type:** Cowork Scheduled Task

---

## SECTION 2: TASK OVERVIEW & PURPOSE

### Business Objective
Generate a weekly market research and content strategy brief that identifies 3-5 trending Singapore property signals, applies REI's strategic frameworks, generates production-ready YouTube scripts + WhatsApp broadcasts, and continuously builds a living intelligence library for content repurposing.

### Key Benefits
- **Weekly content machine fuel:** 5 ranked angles ready for YouTube, WhatsApp, Reels production
- **Competitive positioning:** Identifies white-space gaps others miss in market commentary
- **Audience segmentation:** Separates content by Legacy Launch (SI-05) vs Family Legacy (SI-06) angles
- **Intelligence compounding:** Library grows every week, patterns emerge, insights deepen
- **Team alignment:** Cindior + team have clear brief to execute content plan

### Stakeholders
**Reviews:** Edmund Tan (strategy approval), Cindior Ho (content execution readiness)  
**Acts On:** Content team (YouTube scripts, WhatsApp broadcasts, Reels), Social media  
**Consumes:** Weekly brief feeds bi-weekly rollup, library updates, trend analysis

### Success Metric
- Brief completed by Monday 9 AM (on schedule)
- 5 ranked angles per brief (3 news-triggered + 2 evergreen)
- All sources date-verified to 7-day window
- YouTube scripts production-ready (can publish same-day)
- WhatsApp segments segmented (never mass-blast all 10K)
- Library grows 8-15 new entries per week (patterns + examples)
- Content published from brief generates >8% engagement rate (YouTube), >12% WhatsApp CTR

---

## SECTION 3: EXECUTION SCHEDULE

**Frequency:** Weekly  
**Day & Time:** Every Monday at 9:00 AM Singapore time (UTC+8)  
**Cron Expression:** `0 9 * * 1`  
**Timezone:** Singapore (UTC+8)  
**Estimated Duration:** 2-3 hours per run

### Run Requirements
- **App State:** Cowork must be open
- **Network:** Internet required (web scraping, Google Drive access, API calls)
- **Tools/Connectors Needed:** Google Drive connector, Web search, Google Trends API (optional), YouTube RSS fallback to web search
- **Authentication:** Google Drive access (pre-authorized on first run)

### If Schedule Changes
Document any delays or early runs in the brief header. Notify Edmund + Cindior if missing deadline.

---

## SECTION 4: INPUT DATA SOURCES

### Tier 1 Sources (Must-Scan Weekly)
- **URA (Singapore Urban Redevelopment Authority):** https://www.ura.gov.sg — Official releases, GLS tenders, stats. Daily refresh.
- **EdgeProp Property News:** https://www.edgeprop.sg — Data-backed Singapore property news, transaction reports, market pulse. Daily.
- **StackedHomes Editorial:** https://stackedhomes.com/editorial/ — Analysis, buyer guides, case studies. 2-3x weekly.
- **PropNex News/Reports:** https://www.propnex.com — Market reports, insights, analysis. 2-3x weekly.
- **99.co Blog:** https://www.99.co/blog/singapore — Resale data, transaction analysis, guides. 2-3x weekly.
- **MoneySmart Property:** https://blog.moneysmart.sg/property/ — Finance-focused property analysis. Weekly.

### Tier 2 Sources (Situational/Seasonal)
- **Marcus Luah YouTube:** https://www.youtube.com/@marcusluahsg — Weekly "Keep It Real Estate" series. Check weekly.
- **JNA Real Estate YouTube:** https://www.youtube.com/@JNArealestate — "JNA News Dash" weekly playlist. Check weekly.
- **StackedHomes Telegram:** https://t.me/stackedhomessg — Real-time signals. Daily scan.
- **PropNex Telegram:** https://t.me/propnexpropertynews — Breaking news. Daily scan.
- **Jack Sheo Blog:** https://www.jacksheo.com/blog/ — Market commentary. 1-2x weekly.
- **Aaron Lin YouTube:** https://www.youtube.com/@AaronLin — Market analysis. Weekly.

### Tier 3 Sources (Exploratory/Ad-hoc)
- **Google Trends:** trending.google.com — Singapore property keyword trends. Weekly.
- **Reddit:** r/singaporefi, r/singaporeproperty — Grassroots sentiment, discussion. Spot-check.
- **LinkedIn:** LinkedIn search "Singapore property" + "real estate" — Expert commentary, thought leaders. Weekly.
- **Twitter/X:** Search "Singapore property market" — Real-time sentiment, hot takes. Weekly.
- **Telegram investor groups:** Various private groups (if accessible) — Investor chatter, early signals. Weekly.
- **Facebook groups:** Singapore property buyer groups — Public sentiment, pain points. Weekly.
- **Google News Alerts:** Property + Singapore keywords — Consolidate news feeds. Daily.
- **Podcasts:** Property-focused podcasts (Spotify). Spot-check monthly.

### External Reference Materials
- **ResearchAI Source Catalog v1.3:** Reference guide for sources (Tier 1/2/3 breakdown)
- **REI Content Research Resources Library:** Compete competitor intel, belief blocks, case studies, patterns
- **Prior weekly briefs:** Last 4 weeks' briefs (check Section 0 for angle repeats)
- **MAS Framework docs:** 00_CLIENT BRAIN, 01_MAS_CLIENT_OS, 03_KNOWLEDGE_VAULT

### Data Quality Rules
- **Rule 1:** Only date-verified signals from 7-day scan window (Monday-Sunday of that week). No older signals in main brief.
- **Rule 2:** Must be from Tier 1 or Tier 2 sources only (Tier 3 exploratory only if Tier 1/2 thin that week).
- **Rule 3:** All URLs must be active, tested, on separate lines (no embedded links in text).
- **Rule 4:** All publication dates verified to nearest hour if possible. No vague "recent" claims.
- **Rule 5:** Signal must directly affect Level 2-4 condo owners or Singapore property market. No tangential stories.

---

## SECTION 5: PROCESSING & ANALYSIS

### Step 1: Data Collection
**Method:** Web search + Tier 1 site scanning + YouTube RSS (fallback: web search) + Telegram/forum monitoring  
**Verification:** Cross-reference sources, confirm dates, check if multiple sources covering same story  
**Exclusion:** Duplicate stories from prior week, signals older than 7 days, non-property topics, speculation without data

### Step 2: Filtering & Scoring
**Selection Criteria:** Must pass 6-step angle filter (Section 3 of brief):
1. Published last 7 days?
2. Affects Level 2-4 condo owners?
3. Maps to belief block?
4. Opens SI-05/SI-06/Mash-up?
5. Not covered in prior brief?
6. Maintains 3-news + 2-evergreen balance?

**Scoring System:** Signals scored 1-10 on:
- Belief-shift power (how strongly it counters an objection)
- Market data strength (hard numbers vs soft narrative)
- TDSR/equity relevance (applicability to portfolio positioning)
- Time-sensitivity/urgency (window-closing signal vs evergreen)
- Audience breadth (Level 2 + 3 + 4 or segmented)
- Content repurposing potential (YouTube + WhatsApp + Reels or single-channel)
- Conversion likelihood (expected CTA response rate)

**Ranking Logic:** Top 5 angles ranked by composite score (Rank 1 = highest overall impact for business)

### Step 3: Synthesis & Analysis
**Frameworks Applied:**
- REI Method: R (Review position) → E (Evaluate market) → I (Identify next moves)
- MAS Hierarchy: Millionaire Advisory System > Ascent Model > REI Method
- Belief Block Reframing: Counter with data/logic that shifts objection
- SI-05/SI-06 Separation: Legacy Launch vs Family Legacy angles

**Cross-referencing:**
- Compare findings to prior week's signals (avoid repeats)
- Check against library (competitor intel, patterns, case studies)
- Map to keyword trends (SEO/search demand validation)

**Insights to Extract:**
- What white-space gap does REI see that competitors miss?
- What belief block does this signal trigger?
- What specific action should Level 2/3/4 take?
- What's the urgency window?

### Step 4: Output Generation
**Primary:** Weekly brief document (markdown, saved to Google Drive)  
**Secondary:** 
- 3 YouTube scripts (Format A, B, C versions for Rank 1 angle; Format A for other news angles; Format B for evergreens)
- 3x WhatsApp broadcast segments per angle (Segment 1 = high intent, Segment 2 = medium intent, Segment 3 = remainder)
- Keyword demand data per angle (SEO targets)
- 10-day campaign sprint for Rank 1 angle
- Library updates (new patterns, competitor moves, keyword trends, case studies)

**Format:** Markdown with clear sections, production-ready copy, specific data/URLs

### Step 5: Quality Check (Before Delivery)
- [ ] All 5 signals extracted and date-verified
- [ ] All URLs tested and on separate lines
- [ ] YouTube scripts full 7-min production-ready (not outline)
- [ ] WhatsApp broadcasts segmented (never all 10K at once)
- [ ] No angle repeats from prior week (checked Section 0)
- [ ] All belief blocks explicitly addressed + reframe language included
- [ ] CTA codes aligned (POSITION, LEGACY, UNLOCK, AUDIT)
- [ ] Library sections updated with new findings
- [ ] File saved to correct location with correct naming
- [ ] Ready for immediate team action/publication

---

## SECTION 6: OUTPUT FORMAT & STRUCTURE

### File Naming Convention
`[YYYY-MM-DD] REI Content Brief.md`  
Example: `[2026-06-23] REI Content Brief.md`

### Output Locations
**Primary:** Google Drive folder `/01 property business/03_SHARED_PROPERTY_ASSETS/Weekly Contents/[YYYY-MM-DD] REI Content Brief.md`  
**Library Updates:** Auto-updated in `/01 property business/03_SHARED_PROPERTY_ASSETS/REI_Content_Research_Resources/` (multiple sections)  
**Archive:** After 6 months, move brief to `/Archive/[Year]/` but keep accessible

### File Format(s)
- Markdown (.md) — primary format, version-controllable
- [Optional] Google Doc version for team sharing

### Document Structure (Sections In Order)
1. **Header:** Task metadata (date, run date, scan window, agent name)
2. **Section 0:** Week-on-week continuity (prior week's angles — do NOT repeat)
3. **Section 1:** Tier 1 source scan results (4-8 raw signals with date/source/URL/data/context)
4. **Section 2:** Tier 2 source scan (YouTube channels, Telegram activity, trends)
5. **Section 3:** Six-step angle filter (each signal: Step 1-6 checklist, PASS/FAIL)
6. **Section 4:** Keyword demand data (per angle: primary keywords, secondary, spike window, long-tail)
7. **Section 5:** Five content angles (full build: 3 news-triggered + 2 evergreen, each with YouTube script + 3 WhatsApp segments)
8. **Section 6:** Rank 1 angle 10-day campaign sprint (day-by-day execution plan)
9. **Section 7:** Library updates (which sections updated, new patterns discovered, metrics)
10. **Section 8:** Permanent constraints checklist (verify all hard boundaries met)

### Appearance & Tone
- **Tone:** Direct, data-driven, actionable (no fluff, no generic property news speak)
- **Audience:** Edmund (strategy approval) + Cindior (execution readiness) + team (production)
- **Formatting:** Headers, bold for key numbers, URLs on separate lines, bullet points for clarity

### Backup & Archive Policy
Keep past 6 months in active `/Weekly Contents/` folder. After 6 months, move to `/Archive/` but do NOT delete. Keep searchable.

---

## SECTION 7: METRICS & KPIs TO TRACK

### Output Metrics (Task Quality)
- **Metric 1:** Number of signals extracted per run
  - Target: 5-8 signals per week
  - Tracking: Logged in brief header
- **Metric 2:** Quality score (1-10)
  - Target: 8+ = excellent, 6-7 = acceptable, <6 = needs review
  - Tracking: Reviewed by Edmund before publication
- **Metric 3:** Time to completion
  - Target: 2-3 hours
  - Tracking: Run date - completion time logged in header

### Downstream Performance Metrics (Impact)
- **Metric A:** YouTube engagement rate on published content
  - Target: >8% (views + likes + comments / total reach)
  - How measured: YouTube Analytics per video
- **Metric B:** WhatsApp CTR per segment
  - Target: Segment 1 >15%, Segment 2 >10%, Segment 3 >5%
  - How measured: Reply count / broadcast recipients
- **Metric C:** CTA conversion rate
  - Target: POSITION >15%, LEGACY >10%, UNLOCK >8%, AUDIT >5%
  - How measured: "POSITION" replies / total recipients
- **Metric D:** Format performance
  - Target: Format A (fast-paced) >10% CTR, Format B (narrative) >8%, Format C (authority) >12%
  - How measured: Tracked in CaseStudyRegistry per format

### Tracking Location
- **Output metrics:** Logged in brief header + CaseStudyRegistry section of library
- **Performance data:** Logged in Bi-weekly Rollup Summary
- **Historical data:** Library/CaseStudyRegistry/

### Success Thresholds
- ✅ If quality score ≥8, engagement >8%, CTR >12% → on track, no changes needed
- ⚠️ If quality 6-7, engagement 5-8%, CTR 8-12% → monitor, minor adjustments
- 🔴 If quality <6, engagement <5%, CTR <8% → escalate, review angle selection + messaging

---

## SECTION 8: UPDATE CADENCE & DEPENDENCIES

### Primary Update Schedule
- **Brief sections:** New brief every Monday 9 AM (weekly)
- **Library sections:** Updated after each brief (keyword trends, competitor intel, case studies)
- **Bi-weekly rollup:** Every other Sunday 11 PM (synthesizes 2 weeks of data)

### Upstream Dependencies
- **Prior brief:** Must exist to check Section 0 (no repeats). Available by Monday 9 AM.
- **00_CLIENT BRAIN / 01_MAS_CLIENT_OS:** Frameworks must be accessible for reference. Pre-loaded.
- **Source access:** All Tier 1/2 sources must be live. Check connectivity before 9 AM run.

### Downstream Outputs
- **Content team:** Uses YouTube scripts to produce videos (publish Tuesday-Thursday same week)
- **WhatsApp broadcasts:** Cindior uses scripts for Days 2, 4, 8 of sprint (segmented sends)
- **Social media:** Reels/Shorts extracted from brief narrative by creative team
- **Bi-weekly rollup:** Feeds into Cindior's team briefing + strategic review
- **Library:** Grows continuously, informs next week's angle selection

### Triggers for Running Early/Late
- **Early trigger:** If major market event (rate announcement, policy change) impacts property market → can run emergency brief
- **Delay acceptable:** If Monday 9 AM misses by <4 hours (e.g., 1 PM same day) → still acceptable
- **Escalation:** If delayed >4 hours → notify Edmund + Cindior, explain blocker

---

## SECTION 9: CONSTRAINTS & RULES

### Hard Boundaries (Cannot Break)
- [ ] **Rule 1:** NEVER use signals outside 7-day scan window. Exceptions require explicit approval.
- [ ] **Rule 2:** MUST segment WhatsApp broadcasts. NEVER mass-blast all 10K contacts. Always batch.
- [ ] **Rule 3:** All URLs on separate lines. No embedded URLs in running text.
- [ ] **Rule 4:** NO angle repeats from prior week. Check Section 0 list before finalizing.
- [ ] **Rule 5:** 3 news-triggered + 2 evergreen always. No exceptions to 5-angle format.
- [ ] **Rule 6:** All belief blocks explicitly reframed in YouTube script. No generic messaging.
- [ ] **Rule 7:** Ignore X-Singapore folder completely. Work ONLY from Google Drive (01 property business/03_SHARED_PROPERTY_ASSETS).

### Soft Guidelines (Should Follow)
- [ ] Prefer Tier 1 sources. Tier 2 as secondary. Tier 3 exploratory only.
- [ ] YouTube scripts should be 7 min average (6-8 min acceptable).
- [ ] WhatsApp broadcasts ~100-150 words each (concise, punchy).
- [ ] Aim for 1 Rank 1 angle that's high-urgency, 2-3 moderate, 2 evergreen.
- [ ] Archive old data after 6 months (but keep accessible).

### Exclusions / Out of Scope
- Don't report on HDB-only content (focus is condo-owning families)
- Don't include outdated price data (must be within scan window)
- Don't speculate about policy changes (only report confirmed announcements)
- Don't repeat angles that Edmund has already published recently

### Tool/Connector Limitations & Fallbacks
- **YouTube RSS feeds:** Often unavailable → fallback to web search + channel page scrape
- **Google Trends API:** May rate-limit → fallback to manual Google Trends search
- **Telegram:** Requires manual monitoring (no API) → check Telegram channels weekly
- **EdgeProp:** Popularity sort may show old articles → always date-verify individually

---

## SECTION 10: HANDOFF & APPROVAL WORKFLOW

### Who Reviews & Approves
**Primary Reviewer:** Edmund Tan (strategy + angle selection)  
**Secondary Reviewer:** Cindior Ho (execution readiness + feasibility)  
**Final Approver:** Edmund Tan

### Review Checklist
- [ ] Quality: Output meets expected standard (writing, data accuracy, frameworks applied)
- [ ] Completeness: All 5 angles present, all scripts present, library updates logged
- [ ] Accuracy: All dates verified, all URLs tested, all data correct
- [ ] Consistency: Format matches prior week, tone consistent, no deviations
- [ ] Actionability: Team can execute immediately (scripts are production-ready, not outlines)
- [ ] Compliance: All hard boundaries met (no X-Singapore files, all Google Drive, WhatsApp segmented)
- [ ] Deliverability: File in correct location with correct naming

### Approval Decision Options
✅ **APPROVE** — Brief goes live. Content team begins production. Publish to team channel.  
⚠️ **REQUEST CHANGES** — Specify which angle needs adjustment. Resubmit within 2 hours.  
❌ **REJECT** — Rare. Explain why. Brief redone next week (emergency brief if time-sensitive).

### Timeline
- Task completes: Monday 9-11 AM
- Review begins: Immediately after completion
- Approval window: 1-2 hours for feedback
- Approval deadline: By Monday 12 PM (3 hours after completion)
- Publishing/Go-live: Monday 12 PM (same day)
- Content team begins production: Monday afternoon

### Escalation
- **Technical issues:** Contact [IT/Cloud support]
- **Content issues:** Contact Edmund immediately
- **Approval delays:** Contact both Edmund + Cindior
- **Missing deadline:** Notify both before 9:30 AM Monday

---

## SECTION 11: CHANGE LOG & VERSION CONTROL

### Version History

**v1.0** — 2026-06-20
- Initial version created, filled-in from Master Template
- Key sections: All 11 sections complete
- Created by: Edmund Tan
- Status: ACTIVE

**v1.1** — [PLANNED]
- Add video format variations (currently testing Formats A, B, C)
- Expand library structure based on first 4 weeks of data
- Refine keyword demand methodology

### Update Authority & Process
**Who can update:** Edmund Tan, Cindior Ho  
**Process:**
1. Identify needed change (from test run learnings)
2. Update prompt → test next run
3. Review results
4. Approval → apply to live task
5. Document in Change Log

**Communication:** Updated prompt shared with content team via Google Drive link

### Master Template & Prompt Access & Distribution
- **Master Template:** Google Drive `/Templates/MASTER_SCHEDULED_TASK_TEMPLATE_v1.0`
- **This filled-in prompt:** Google Drive `/Templates/rei-weekly-content-brief_PROMPT_v1.0`
- **Read access:** Edmund, Cindior, Content team leads
- **Edit access:** Edmund, Cindior only
- **Version notifications:** Updated version shared via email + team Slack

---

## SECTION 12: APPENDICES & REFERENCE MATERIALS

### Appendix A: Script Format Decision Matrix
| Format | Best For | Triggers | Example |
|--------|----------|----------|---------|
| **A: Fast-Paced, Data-Driven** | Rank 1, high urgency | Time-sensitive signals, market shock | Newton GLS $1,865 psf |
| **B: Narrative + Story/Case Study** | Evergreen, structural | Timeless problems, deep psychology | Idle equity risk |
| **C: Authority Breakdown (Myth-Bust)** | Contrarian, white-space | Everyone says X, we say Y | "Market crashing (it's not)" |

### Appendix B: Belief Block Reframe Examples
- **"Property appreciating so fine to stay"** → Counter: Window closing on entry prices, equity alone doesn't maximize wealth
- **"Not the right time to buy"** → Counter: Quiet markets = less competition, better negotiating position
- **"Child cannot afford it"** → Counter: Family structure + parental equity = access now
- **"Maxed out on names"** → Counter: Decoupling + adult child = new entry path
- **"Fully paid condo means safe"** → Counter: Idle equity risk, SORA near 1% = leverage opportunity

### Appendix C: Related Processes
- Bi-weekly Rollup (Sunday 11 PM) — synthesizes 2 weeks of brief data
- Content Research Resources Library — grows with each brief
- Social Media Calendar — pulls angles from brief for weekly scheduling
- Video Production Pipeline — consumes YouTube scripts for production

### Appendix D: Glossary
- **SI-05:** Strategic Intent 05 = Legacy Launch (existing condo → first portfolio move)
- **SI-06:** Strategic Intent 06 = Family Legacy (parent + adult child co-purchase)
- **Mash-up:** Both SI-05 + SI-06 running simultaneously
- **REI Method:** R (Review Real Position) → E (Evaluate Market Rewards) → I (Identify Next Moves)
- **CTA:** Call-to-Action (POSITION, LEGACY, UNLOCK, AUDIT codes)
- **TDSR:** Total Debt Service Ratio (affordability metric)
- **MOP:** Minimum Occupation Period (HDB/EC restriction)
- **SORA:** Singapore Overnight Rate Average (floating interest rate benchmark)

### Further Reading & Links
- REI Content Research Resources: Google Drive `/REI_Content_Research_Resources/INDEX.md`
- Prior briefs: Google Drive `/Weekly Contents/` (last 4 weeks)
- Master Template: Google Drive `/Templates/MASTER_SCHEDULED_TASK_TEMPLATE_v1.0`
- MAS frameworks: 00_CLIENT BRAIN, 01_MAS_CLIENT_OS (in referenced folder)

---

## SECTION 13: NOTES FOR TEMPLATE EVOLUTION

This filled-in example will evolve based on test run results.

**First 4 weeks will reveal:**
- Which script formats (A, B, C) drive highest engagement
- Which CTA codes (POSITION/LEGACY/UNLOCK/AUDIT) convert best
- Which segments (L2/L3/L4) respond to which angles
- Which Tier 2 sources are actually valuable vs noise

**Quarterly improvements planned:**
- Refine scoring system based on performance data
- Lock in proven script formats
- Optimize Tier 2 source list (remove non-performers)
- Automate keyword trend pulling (currently manual)

---

## END REI WEEKLY CONTENT INTELLIGENCE BRIEF — FILLED-IN EXAMPLE v1.0