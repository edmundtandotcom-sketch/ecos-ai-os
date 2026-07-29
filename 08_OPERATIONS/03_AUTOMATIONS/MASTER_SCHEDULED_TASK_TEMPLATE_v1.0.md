# MASTER SCHEDULED TASK TEMPLATE

Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-10
Supersedes: none — copied as-is
Sources: `H:\Shared drives\00_E.C.O.S\01_PROPERTY_BUSINESS\Templates\MASTER_SCHEDULED_TASK_TEMPLATE_v1.0` (no file extension in legacy Drive; saved here as `.md`)

**Last Updated:** 2026-06-20  
**Owner:** Edmund Tan  
**Scope:** All recurring scheduled tasks (content briefs, reports, research, monitoring, etc.)

---

## INSTRUCTIONS FOR USE

1. **Copy this entire template** for any new recurring task
2. **Fill in all [BRACKETS]** with task-specific information
3. **Delete sections marked [OPTIONAL]** if not applicable
4. **Keep structure consistent** — do not reorder sections
5. **Save filled-in version** to `Templates/[Task ID]_PROMPT.md`
6. **Create Google Doc version** for team sharing/approval
7. **Version control:** Update this master template quarterly; track all changes in Section 10

---

## SECTION 1: TASK HEADER

**Task ID:** [kebab-case, e.g., rei-weekly-content-brief]  
**Task Name:** [Human-readable, e.g., REI Weekly Content Intelligence Brief]  
**Owner:** [Primary owner name]  
**Created:** [YYYY-MM-DD]  
**Last Updated:** [YYYY-MM-DD]  
**Status:** [DRAFT / ACTIVE / ARCHIVED]  
**Version:** [e.g., 1.0]  
**Scheduler Type:** Cowork Scheduled Task / Automation Tool / Manual (if applicable)

---

## SECTION 2: TASK OVERVIEW & PURPOSE

### Business Objective
[One clear sentence: What does this task do? What problem does it solve? Why does it matter?]

### Key Benefits
- [Benefit 1: specific outcome]
- [Benefit 2: specific outcome]
- [Benefit 3: specific outcome]

### Stakeholders
**Reviews:** [Who reviews the output? (e.g., Edmund, Cindior, Team Lead)]  
**Acts On:** [Who takes action based on output? (e.g., Content team, Sales team)]  
**Consumes:** [Who uses the output as input for other work?]

### Success Metric
[How do you measure if this task is working? Examples:]
- Content engagement rate > X%
- Output completed within 2 hours
- Team acts on recommendations within 24 hours
- Library grows by Y new entries per run

---

## SECTION 3: EXECUTION SCHEDULE

**Frequency:** [Daily / Weekly / Bi-weekly / Monthly / Quarterly / Ad-hoc]  
**Day & Time:** [e.g., Every Monday at 9:00 AM Singapore time]  
**Cron Expression:** [e.g., "0 9 * * 1" (five fields: minute hour dayOfMonth month dayOfWeek)]  
**Timezone:** [Singapore (UTC+8) / Other]  
**Estimated Duration:** [e.g., 2-3 hours per run]

### Run Requirements
- **App State:** [Open / Can be closed / Specific state needed]
- **Network:** [Internet required / Offline capable / Specific connectivity]
- **Tools/Connectors Needed:** [List any MCPs, APIs, databases to access]
- **Authentication:** [Any credentials or approvals needed?]

### If Schedule Changes
[Document how/when schedule was updated, by whom, for what reason]

---

## SECTION 4: INPUT DATA SOURCES

### Tier 1 Sources (Must-Scan Weekly)
- [Source 1: Full URL/access path, why essential, how often refreshes]
- [Source 2: Full URL/access path, refresh rate]
- [Source 3, 4, 5, etc.]

### Tier 2 Sources (Situational/Seasonal)
- [Source A: URL, when used, priority level]
- [Source B: URL, when used]
- [Source C, D, etc.]

### Tier 3 Sources (Exploratory/Ad-hoc)
- [Source X: URL, for deep dives, frequency]
- [Source Y: URL, exploratory]

### External Reference Materials
- [Template/playbook name: location, how to use]
- [Format guide: location]
- [Prior task runs: where to find examples]

### Data Quality Rules
- [Rule 1: e.g., "Only accept signals verified to exact day/hour"]
- [Rule 2: e.g., "Must be from Tier 1 or Tier 2 sources only"]
- [Rule 3: e.g., "Scan window: last 7 days only"]
- [Rule 4: e.g., "All URLs must be active/verified"]

---

## SECTION 5: PROCESSING & ANALYSIS

### Step 1: Data Collection
[What to gather? How to verify it? What to exclude?]
- Collection method: [How will data be gathered?]
- Verification process: [How to ensure data quality?]
- Exclusion criteria: [What gets filtered out?]

### Step 2: Filtering & Scoring
[What makes data qualify for output? How is it ranked?]
- Selection criteria: [Pass/fail criteria]
- Scoring system: [If scored, how? (e.g., 6-step filter, 10-point scale)]
- Ranking logic: [How to rank top findings?]

### Step 3: Synthesis & Analysis
[How to combine/analyze data? What frameworks/methodologies apply?]
- Analysis frameworks: [e.g., REI Method (R-E-I), MAS hierarchy, etc.]
- Cross-referencing: [Any dependencies with other data sources?]
- Insights to extract: [What patterns/conclusions to look for?]

### Step 4: Output Generation
[Build what outputs? In what order?]
- Primary output: [e.g., Weekly brief document]
- Secondary outputs: [e.g., WhatsApp scripts, YouTube scripts]
- Format: [Structure, sections, tone]

### Step 5: Quality Check (Before Delivery)
[What must be verified?]
- [ ] All sources verified/live
- [ ] All dates correct and in-window
- [ ] All URLs active and on separate lines
- [ ] Tone consistent with brand voice
- [ ] No repeats from prior runs
- [ ] All sections complete
- [ ] Ready for immediate action/publication

---

## SECTION 6: OUTPUT FORMAT & STRUCTURE

### File Naming Convention
[Exact pattern, e.g., "[YYYY-MM-DD] REI Content Brief.md"]

### Output Locations
**Primary:** [Full path where main output saves]  
**Library/Resources:** [If feeding library updates, where does that go?]  
**Backup/Archive:** [If older files archived, path and retention policy?]

### File Format(s)
- [Format 1: e.g., Markdown (.md)]
- [Format 2: e.g., Google Doc (.gdoc)]
- [Format 3: e.g., PDF (optional)]

### Document Structure (Sections In Order)
1. [Section name: description]
2. [Section name: description]
3. [Section name: description]
4. [Section name: description]
5. [etc.]

### Appearance & Tone
- Tone: [e.g., Direct, data-driven, actionable]
- Audience level: [e.g., Executive summary for Edmund, detail for team]
- Visual formatting: [e.g., Headers, bullet points, tables as needed]

### [OPTIONAL] Backup & Archive Policy
[When/how to archive old files? Where? How long to keep?]

---

## SECTION 7: METRICS & KPIs TO TRACK

### Output Metrics (Task Quality)
- [Metric 1: e.g., "Number of signals extracted per run"]
  - Target: [e.g., 5-8 signals]
  - Tracking location: [Where logged?]
- [Metric 2: e.g., "Quality score (1-10)"]
  - Target: [e.g., 8+ = good, 6-7 = acceptable, <6 = needs review]
- [Metric 3: e.g., "Time to completion"]
  - Target: [e.g., 2-3 hours]

### Downstream Performance Metrics (Impact)
[Optional — track if output drives real results]
- [Metric A: e.g., "Content engagement rate on published material"]
  - Target: [e.g., >10% engagement]
  - How measured: [YouTube views, WhatsApp reply rate, etc.]
- [Metric B: e.g., "CTA conversion rate (POSITION/LEGACY/UNLOCK/AUDIT)"]
  - Target: [e.g., POSITION >15%, LEGACY >10%]

### Tracking Location
[Where are metrics logged/reviewed?]
- Output metrics: [e.g., "Library/CaseStudyRegistry/"]
- Performance data: [e.g., "Bi-weekly Rollup Summary"]
- Historical data: [e.g., "Library archives"]

### Success Thresholds
- ✅ If [Metric X] > [Threshold], task is on track
- ⚠️ If [Metric X] between [Threshold A] and [Threshold B], review needed
- 🔴 If [Metric X] < [Threshold C], escalate for adjustment

---

## SECTION 8: UPDATE CADENCE & DEPENDENCIES

### Primary Update Schedule
- [Section A of output]: Updates every [frequency, e.g., weekly]
- [Section B of output]: Updates every [frequency, e.g., monthly]
- [Library/Resources]: Updated after each run? Or batch updated?

### Upstream Dependencies
[What must happen BEFORE this task runs?]
- [Task/Data 1]: Due by [date/time], provides [what]
- [Task/Data 2]: Due by [date/time], provides [what]
- [Manual input 1]: [What human input is needed?]

### Downstream Outputs
[What uses the output of this task?]
- [Task A]: Consumes [which section/output] by [date]
- [Team B]: Uses [output] for [what decision/action]
- [Resource C]: Updated with [learnings] from [output]

### Triggers for Running Early/Late
[Under what conditions can schedule change?]
- Can task run early? [If yes, what condition triggers it?]
- Can task be delayed? [If yes, what's latest acceptable time?]
- Manual override? [Who can trigger manual run, and when?]

---

## SECTION 9: CONSTRAINTS & RULES

### Hard Boundaries (Cannot Break)
- [ ] [Rule 1: e.g., "NEVER use data outside 7-day scan window"]
- [ ] [Rule 2: e.g., "MUST segment WhatsApp broadcasts, never mass-blast"]
- [ ] [Rule 3: e.g., "All URLs on separate lines"]
- [ ] [Rule 4: e.g., "Only date-verified signals"]

### Soft Guidelines (Should Follow)
- [ ] [Guideline A: e.g., "Prefer Tier 1 sources, use Tier 2 as secondary"]
- [ ] [Guideline B: e.g., "Aim for 3-5 findings; 2-8 acceptable"]
- [ ] [Guideline C: e.g., "Archive old data after 6 months"]

### Exclusions / Out of Scope
- Don't [action 1]
- Don't [action 2]
- Don't [action 3]

### Tool/Connector Limitations & Fallbacks
- [Tool 1]: May fail with [issue]. Fallback: [alternate method]
- [Connector A]: Requires [authentication]. If unavailable: [workaround]
- [Data source B]: RSS feeds down? Use [web search alternative]

---

## SECTION 10: HANDOFF & APPROVAL WORKFLOW

### Who Reviews & Approves
**Primary Reviewer:** [Name/role]  
**Secondary Reviewer:** [Optional, name/role]  
**Final Approver:** [Name/role]

### Review Checklist
- [ ] Quality: Output meets expected standard
- [ ] Completeness: All sections filled, no gaps
- [ ] Accuracy: Data is correct, URLs verified
- [ ] Consistency: Format matches prior runs, no deviations
- [ ] Actionability: Output is ready for immediate use/publication
- [ ] Compliance: All hard boundaries respected, soft guidelines followed
- [ ] Deliverability: File saved to correct location, correctly named

### Approval Decision Options
✅ **APPROVE** — Goes live as-is. [Timeline]  
⚠️ **REQUEST CHANGES** — Specify what needs adjustment. [Resubmit by: date]  
❌ **REJECT** — Explain why. Task redone next cycle. [Escalation notes]

### Timeline
- Task completes: [Day/time]
- Review begins: [Immediately / next morning / specific time]
- Approval window: [Hours available for review]
- Approval deadline: [Must decide by: date/time]
- Publishing/Go-live: [When does output go to audience?]

### Escalation
[If issues arise during run, who do we contact?]
- Technical issues: Contact [name/email]
- Content issues: Contact [name/email]
- Approval delays: Contact [name/email]

---

## SECTION 11: CHANGE LOG & VERSION CONTROL

### Version History

**v1.0** — [YYYY-MM-DD]
- [Initial version created]
- [Key sections: list main sections]
- Created by: [Name]
- Status: [DRAFT / ACTIVE]

**v1.1** — [YYYY-MM-DD] [PLANNED or COMPLETED]
- [Planned/Completed update: describe change]
- Reason: [Why this change?]
- Impact: [What changes in execution?]

[Continue for each version...]

### Update Authority & Process
**Who can update this template?**
- [Edmund / Cindior / [others]]

**Update process:**
1. Identify needed change
2. Update template → create test version
3. Test run with new version
4. Review results
5. Approval → apply to live task
6. Document in Change Log

**Communication:**
- All task owners notified of template updates: [How? Email/meeting/doc link?]
- Training provided: [If major changes, how to train users?]

### Master Template Access & Distribution
- **Master location:** `Templates/MASTER_SCHEDULED_TASK_TEMPLATE_v1.0`
- **Google Doc version:** [Link to shared Google Doc]
- **Read access:** [Edmund, Cindior, Team leads, All staff]
- **Edit access:** [Edmund, Cindior only]
- **Version notification:** [All task owners notified of major updates]

---

## SECTION 12: APPENDICES & REFERENCE MATERIALS [OPTIONAL]

### Appendix A: [e.g., Scoring Matrix]
[If task uses specific scoring/ranking system, document it here]

### Appendix B: [e.g., Format Examples]
[Show examples of good output, bad output, edge cases]

### Appendix C: [e.g., Related Processes]
[Link to related workflows, upstream/downstream tasks]

### Appendix D: [e.g., Glossary]
[Define task-specific terms, acronyms, jargon]

### Further Reading & Links
- [Link to resource library (if applicable)]
- [Link to prior task runs (for reference)]
- [Link to related documentation]
- [Link to team playbook (if applicable)]

---

## SECTION 13: NOTES FOR TEMPLATE EVOLUTION

This template is designed to be **living** — it will evolve as we learn what works.

**How to suggest improvements:**
1. Note the gap/issue you found
2. Suggest specific change (add section? Reword guidance? Remove?)
3. Document in Change Log (Section 11)
4. Test change in next task run
5. Incorporate into master if successful

**Review Cadence for Master Template:**
- Monthly: Quick scan for needed updates
- Quarterly: Full review + updates
- Annually: Major review + version increment

---

## END MASTER SCHEDULED TASK TEMPLATE v1.0