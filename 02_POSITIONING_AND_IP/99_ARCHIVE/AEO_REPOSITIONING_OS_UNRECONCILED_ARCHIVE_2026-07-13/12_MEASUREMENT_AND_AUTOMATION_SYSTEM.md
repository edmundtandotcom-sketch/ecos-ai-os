# 12 — MEASUREMENT AND AUTOMATION SYSTEM
**Phase 12 · Proving the Repositioning Is Working**
**Project:** AEO Repositioning OS — Singapore Property Advisory
**Owner:** Measurement and Automation (Sonnet builder)
**Date:** 9 July 2026 · **Status:** Built on LOCKED decisions in `_MASTER_CONTEXT_BRIEF.md`. Nothing here overrides the contract; conflicts are flagged in "Concerns."
**Companion file:** `AEO_Visibility_Test_Bank.csv` (62 rows, columns `test_id,engine,category,prompt,target_entity_or_page,success_criterion,frequency`)

---

## EXECUTIVE SUMMARY

This phase turns the other eleven phases into numbers a sceptical founder can check monthly, and it does so honestly: today, most of the instrumentation this business needs does not exist. GA4 is unconfirmed on any domain, Search Console verification is unconfirmed, no social account is connected to GHL, and the GHL sub-account that will carry every advisory KPI also carries 180+ `cg_*` Changi Green tenancy fields and a "Changi Green-Tenant Cycle" pipeline that will silently pollute every count until it is tagged out. There is also no `spl_*` field set yet, because the "Which Step Are You On?" diagnostic referenced throughout the strategy docs has not been built.

The system below is deliberately two-track. Track one is a **Google Sheets KPI Dashboard** buildable this week with what already exists (GHL pipeline data, manual AI-visibility testing, manual SERP checks) — because waiting for GA4/GSC verification before measuring anything would mean measuring nothing for months. Track two is the **migration path to Looker Studio** once GA4 and Search Console are confirmed and connected, at which point ranking and traffic KPIs stop being manual.

The centrepiece is the **AI Visibility Test Bank** — 62 fixed prompts across six engines (ChatGPT, Perplexity, Gemini, Google AI Overview, Google SERP, YouTube search) and eight buyer-language categories, scored 0–3 (not mentioned / mentioned / cited / recommended) every month, logged out, screenshotted. Because "The Second Property Ladder" and "Exit Before Entry" currently have **zero public footprint** (Report 1, Section I), most of these tests should score 0 at baseline — that 0 is the point. It is the number every later phase is judged against.

This file also delivers the Monthly Reporting Template (10 fixed questions), the Weekly Action Review (30-minute founder ritual), a prioritised Automation Backlog (lead-grade routing, review requests, no-show recovery, quiz field-mapping, stale-opportunity alerts, KPI auto-pull, AI-visibility reminders), a Data Source Map naming every gap, and a Baseline Capture Plan that must run **before** Phases 3, 4, 7, and 8 change anything public-facing — otherwise there is no "before" to compare the "after" against.

**Headline rulings:** recommend Google Sheets now, Looker Studio once GA4+GSC verified; segment Changi Green contacts out of all reporting immediately via tags, not later; treat every AI-visibility score of 0 at baseline as expected and correct, not as a failure to fix before measuring.

---

## 1. KPI DASHBOARD SPEC

### 1.1 Platform recommendation

**Google Sheets now. Migrate to Looker Studio once GA4 + Search Console are verified (target: month 3).**

Reasoning: Looker Studio's main advantage — native GA4/GSC connectors that auto-refresh — is worthless while those two properties are unconfirmed [VERIFY, per Master Context Brief Q3]. Building a Looker Studio dashboard today would mean wiring most tiles to manual-entry ranges anyway, which is exactly what a Sheet does natively, with none of the sharing/permission overhead. Sheets also match the manual nature of the AI Visibility Test Bank (a human runs 62 prompts and types in a score — there is no API for "did ChatGPT cite us"). Once GA4 and GSC are installed and have 60–90 days of data, migrate the ranking/traffic tiles to Looker Studio and keep the manual tiles (AI visibility, lead quality, CRM velocity) as linked Sheets — Looker Studio can blend a live GA4 connector with a manual Sheet in the same report.

### 1.2 Sheet structure (8 tabs)

| Tab | Purpose | Update cadence | Owner |
|---|---|---|---|
| 1. Dashboard | The 15 KPI areas in one view: metric, this month, last month, target direction, RAG status | Monthly, 1st business day | Founder-designated ops owner [OPEN: Edmund, Cindior, or hire] |
| 2. AI Visibility Log | One row per test-bank run per month (62 rows × month); links to screenshot folder | Monthly | Same |
| 3. Funnel Metrics | Step-by-step conversion (visit→optin→booked→showed→Position Map→Blueprint) per funnel | Monthly | Same |
| 4. CRM Pipeline Velocity | Days-in-stage for each 1-To-1 Pipeline stage; stage-to-stage conversion % | Monthly | Same |
| 5. Lead Quality | Grade A/B/P/C distribution from diagnostic (once built) | Monthly | Same |
| 6. Content Attribution | UTM/campaign roll-up against GHL attribution fields | Monthly | Same |
| 7. Backlinks & Reviews | Backlink count/referring domains, GBP review count/rating, review velocity | Monthly | Same |
| 8. Baseline Snapshot | Frozen Week-1 numbers (Section 7) — never overwritten | Once, then read-only | Same |

### 1.3 The 15 tracked areas

| # | Area | Metric | Source | Owner | Target direction | Notes / current gap |
|---|---|---|---|---|---|---|
| 1 | Branded search volume | Search Console impressions/clicks for branded queries: "edmund tan property", "REI method", "second property ladder", "legacy launch" | Search Console (Performance report, filtered by query) | Ops owner | ↑ steadily as entity consolidates | **GAP:** GSC verification on thereimethod.com unconfirmed [VERIFY]. Cannot measure until verified. |
| 2 | Non-branded visibility | Search Console impressions for buyer-language, non-branded queries ("sell hdb buy condo", "absd second property", "decoupling singapore") | Search Console | Ops owner | ↑ from near-zero as content publishes | Same GSC dependency as #1 |
| 3 | Page rankings | Average position for target pages (category hub, founder bios, guides) for their assigned queries | Search Console Performance report, cross-checked with manual incognito search | Ops owner | ↑ (lower avg. position number = better) | GSC dependency; manual cross-check until then |
| 4 | AI answer visibility | Test Bank aggregate score (sum of 62 monthly scores, 0–186 max) | AEO_Visibility_Test_Bank.csv monthly run (Section 2) | Founder or ops owner | ↑ from baseline (expected nea-zero) | Fully manual — no API substitute exists today |
| 5 | AI Overview citations | Count of Google AI Overview appearances where thereimethod.com or a founder is cited (score 2+) | Test Bank rows tagged "Google AI Overview" (12 of 62 rows) | Ops owner | ↑ from 0 | Google does not expose an AI Overview API; manual only |
| 6 | ChatGPT/Perplexity/Gemini test results | Sub-score per engine from the Test Bank (ChatGPT 17 rows, Perplexity 12, Gemini 10) | Test Bank | Ops owner | ↑ per engine | Track per-engine, not just blended, since engines diverge |
| 7 | YouTube search visibility | Test Bank YouTube-search sub-score (8 rows) + YouTube Studio "Traffic source: YouTube search" impressions/views for the channel | Test Bank + YouTube Studio Analytics | Ops owner | ↑ | Channel stats (~600+ videos, 2,000+ subscribers) [VERIFY, per funnel copy] |
| 8 | GBP views/calls/messages | Views, calls, direction requests, messages, from GBP Insights (Business Profile Manager) | Google Business Profile Manager | Ops owner | ↑ | **GAP:** listing behind share.google/bpyWTGgjlyNxt8Xiz not confirmed claimed/verified [VERIFY name, category, review count — see Phase 8] |
| 9 | Funnel conversion rates | Step conversion: visit→optin→booked→showed→Position Map→Blueprint, per funnel (Legacy Launch V2 today; diagnostic funnel once built) | GHL funnel analytics + calendar (`34KkdVJncaYiuAOjE0FP`) + opportunity stage counts | Ops owner | ↑ at each step | See Section 1.4 for the exact GHL objects |
| 10 | Consult bookings | Count of booked "Position Map session" / "Strategy Call" appointments per month | GHL calendar + 1-To-1 Pipeline stage "Booked Call"/"Appointment" | Ops owner | ↑ | Clean of Changi Green (see Data Source Map, row 8) |
| 11 | Lead quality | % distribution of leads by grade A/B/P(Portfolio)/C, from diagnostic scoring | GHL custom fields `spl_lead_grade` (once created) | Ops owner | Shift toward A/B over time | **GAP:** `spl_*` fields do not exist yet (confirmed absent, Report 2) — this row is unmeasurable until the diagnostic ships |
| 12 | CRM stage movement (velocity) | Median days-in-stage for each 1-To-1 Pipeline stage (New Lead → Responded → Booked Call → Appointment → Strategy Session → Close → Nurture → Unqualified → Won → Lost) | GHL Opportunities report, filtered to 1-To-1 Pipeline | Ops owner | ↓ (faster movement) except intentional Nurture dwell | Must exclude Changi Green-Tenant Cycle pipeline entirely |
| 13 | Content-to-lead attribution | Lead count and grade by `utm_source`, `ad_id`, `campaign_id`, `campaign_name`, `click_id` | GHL contact custom fields (already exist) | Ops owner | Clarity on which content/campaign produces A-grade leads | Fields exist; discipline (consistent UTM tagging on every published asset) does not yet — flagged as a gap, not a field gap |
| 14 | Review velocity | New reviews per month + rating trend | Google Business Profile Manager (reviews tab) | Ops owner | ↑ count, ≥4.7 rating maintained | Depends on GBP claim status (#8) and the review-request automation (Section 5) |
| 15 | Backlinks/mentions | Referring domains count + new mentions (branded name in unlinked text) | Search Console "Links" report (free) as baseline; paid tool (Ahrefs/Semrush) if licensed | Ops owner | ↑ | **GAP:** no backlink tool confirmed licensed in this environment; GSC Links report is the free fallback and is directional only |

### 1.4 Funnel step → GHL object mapping (for KPI #9)

| Funnel step | Legacy Launch V2 object today | Diagnostic funnel (once built, per Phase 10/Master Brief offer ladder) |
|---|---|---|
| Visit | Page `4JECqA37xZnvFFNi3DTa` (`/strategy-call`) pageview | `secondpropertyladder.com` diagnostic entry page pageview |
| Opt-in | Form `cw6XigpSZy8OCZgtDC34` submission ("Legacy Launch V2 — Qualify") | Analytics event `capture_submitted` (per Report 1, Section G spec) |
| Booked | Booking step `/schedule-call` → calendar `34KkdVJncaYiuAOjE0FP` ("New Launch/Family Legacy Ladder") | Analytics event `cta_clicked` → Position Map session booking |
| Showed | 1-To-1 Pipeline stage "Appointment"/"Strategy Session" marked Showed (not No-Show) | Same GHL calendar/opportunity logic |
| Position Map | Opportunity moved to "Strategy Session" or "Close" stage with session actually delivered | Same |
| Blueprint | Opportunity moved to "Won" with Blueprint sold | Same |

---

## 2. AI VISIBILITY TEST BANK AND MONTHLY PROTOCOL

### 2.1 Scoring definition (fixed, used every month, never changed mid-series)

| Score | Meaning |
|---|---|
| **0** | Not mentioned. The engine's answer does not reference the target entity, page, or concept at all. |
| **1** | Mentioned. Named as one option among several, with no link/citation and no endorsement. |
| **2** | Cited. A specific thereimethod.com (or channel) URL is linked/footnoted, or the engine attributes a fact directly to Edmund Tan/Cindior Ho/The REI Method. |
| **3** | Recommended. The engine names the entity as its lead or sole answer to "who/what is best" — the gradual-entry endpoint for the best-top-provider category. |

### 2.2 Protocol

1. **Who runs it:** one person, every month, same person if possible (score consistency matters more than speed) — assign in First 5 Actions.
2. **Logged-out discipline:** run ChatGPT and Gemini in a private/incognito window, signed out of any Google/OpenAI account tied to the business, to avoid personalisation bias. Perplexity: use the logged-out web version. Google SERP/AI Overview: incognito, Singapore-region VPN/location if testing from outside SG, English (Singapore) if the option exists. YouTube search: signed out, incognito.
3. **Order:** run the CSV top to bottom, one prompt per fresh conversation/session (never chain prompts in one thread — that contaminates the answer with earlier context).
4. **Capture:** full-page screenshot of every answer, filename convention `AEO-0XX_YYYY-MM.png`, stored in a dated Drive subfolder (e.g. `AEO_REPOSITIONING_OS/_AI_VISIBILITY_LOG/2026-07/`).
5. **Score and log:** enter the 0–3 score, one line per prompt, into Tab 2 (AI Visibility Log) of the KPI Dashboard, with a short note on what specifically was said (e.g. "named 3 other advisories, not us" vs "cited thereimethod.com/second-property-ladder directly").
6. **Aggregate:** Tab 1 Dashboard pulls SUM and per-engine AVERAGE from Tab 2 automatically (Sheets formula, not manual re-typing).
7. **Frequency split:** 52 of 62 rows run **Monthly** (the categories most sensitive to publishing cadence: who-is, best-top-provider, how-do-i, should-i, what-is, safest-way, before-acting). The 6 **who-teaches** rows (AEO-051–056) run **Quarterly** — these are structural/definitional queries that move on a slower cycle than monthly content pushes, so monthly testing would waste effort without adding signal.
8. **Baseline expectation, stated plainly:** at month 1, expect a large majority of scores at 0. "The Second Property Ladder" and "Exit Before Entry" have zero public footprint today (Report 1, Section I) — a 0 baseline is the correct, expected reading, not a broken test. The KPI that matters is the *slope*, not the month-1 number.

---

## 3. MONTHLY REPORTING TEMPLATE

### Headings (fixed structure, same order every month)

1. **Period Covered** (calendar month, e.g. "August 2026")
2. **Executive Snapshot** (3–5 lines: what moved, what didn't, one headline number)
3. **KPI Scorecard** (the 15 areas, RAG status, vs. last month and vs. baseline)
4. **AI Visibility Results** (Test Bank scores this month vs. last month, by engine and by category, with 2–3 example screenshots of any new score-2/3 result)
5. **Funnel & CRM Performance** (conversion rates per step, pipeline velocity per stage)
6. **Content & Attribution** (which published assets drove which leads, by UTM/attribution field)
7. **Wins & Risks** (what to double down on; what's stalling and why)
8. **Next Month Focus** (the one or two KPI areas getting deliberate attention)

### The 10 questions the monthly review must answer

1. Did branded search volume for our core name-tokens (Edmund Tan, REI Method, Second Property Ladder, Legacy Launch) grow or shrink this month, and why?
2. Are we visible yet for non-branded, buyer-language queries ("sell hdb buy condo", "absd second property", "decoupling"), or still near-zero?
3. Which target pages moved in Google rankings — up or down — and which need rework this month?
4. Did any AI engine (ChatGPT, Perplexity, Gemini, Google AI Overview) mention, cite, or recommend us this month that it did not last month?
5. How many YouTube-search-driven views/impressions did the channel get, and for which queries?
6. Did GBP views/calls/messages grow, and does the current review count/rating support the authority claims we're making publicly?
7. Where in the funnel (visit→optin→booked→showed→Position Map→Blueprint) are we losing the most people, and did that leak improve or worsen?
8. How many consult bookings did we get this month, and what was the lead-grade distribution (A/B/P/C)?
9. Which specific content asset or campaign (by UTM/attribution field) produced the highest-quality leads and the fastest CRM stage movement?
10. Are Changi Green contacts fully segmented out of this report, and is the underlying data otherwise clean (no stray test/physio/CNY-survey fields bleeding in)?

---

## 4. WEEKLY ACTION REVIEW TEMPLATE (30-minute founder ritual)

Run every week, same day/time, ideally Monday morning before ad spend or content goes out for the week.

| Time | Block | What to do |
|---|---|---|
| 0–5 min | Pipeline pull | Open the 1-To-1 Pipeline board in GHL. Read off: new leads this week, bookings this week, showed vs. no-show count. |
| 5–12 min | Lead-grade check | Filter new leads by grade (once `spl_lead_grade` exists). Confirm every A-grade lead got an instant WhatsApp within the automation's SLA (Section 5, Automation 1) — if any A-grade lead sat untouched, that is this week's #1 fix, not a footnote. |
| 12–18 min | Stale-opportunity sweep | Pull the stale-opportunity list (Section 5, Automation 5 — anything untouched 5+ days in a stage). Action or explicitly park each one; don't let the list silently grow. |
| 18–23 min | AI visibility spot-check | Not the full 62-row run — spot-check the 3 highest-priority prompts (AEO-009 best-top-provider ChatGPT, AEO-035 what-is ChatGPT, AEO-045 safest-way ChatGPT). Note any change; flag anything notable for the monthly full run. |
| 23–28 min | Content ship check | Did this week's planned content (per Phase 10 content engine) actually publish? If not, why, and does it still go out this week? |
| 28–30 min | Set next week's #1 | One sentence: the single highest-leverage action for next week. Written down, not just said. |

---

## 5. AUTOMATION BACKLOG (prioritised)

| # | Automation | Trigger | Action | Tool | Effort | Impact | Priority / dependency |
|---|---|---|---|---|---|---|---|
| 1 | Quiz → field mapping (`spl_*`) | Diagnostic webhook submission from the "Which Step of The Second Property Ladder Are You On?" quiz | Make.com scenario maps payload to GHL custom fields (`spl_step_result`, `spl_total_score`, `spl_band`, `spl_lead_grade`, `spl_gate_1`–`spl_gate_4`, `spl_c1`–`spl_c10`); creates/updates contact; applies grade/step tags | Make.com + GHL API | M | Critical — foundational; automations 2 and 6 below depend on this existing first | **Do first.** Requires: (a) the 14 `spl_*` fields created in GHL (they do not exist today, Report 2), (b) the diagnostic itself built and hosted (Netlify Drop/Cloudflare Pages per Report 1, Section G) |
| 2 | Lead-grade routing | Contact field `spl_lead_grade` set/updated | If **A**: instant WhatsApp to lead + internal notification to founder + auto-offer Position Map session booking link. If **C**: add to a nurture email/SMS drip sequence, no instant contact | GHL native workflow | S (once Automation 1 exists) | High — this is the single biggest lever on "did the A-grade lead get contacted before they cooled" | Depends on Automation 1 |
| 3 | Review-request workflow | Opportunity stage moves to **Won** in 1-To-1 Pipeline (Blueprint delivered) | Automated WhatsApp/SMS/email requesting a Google review, linking the GBP listing (share.google/bpyWTGgjlyNxt8Xiz, pending Phase 8 claim) | GHL native workflow | S | High — directly feeds KPI #14 (review velocity) and #15 (mentions) | Depends on GBP listing being claimed/verified (Phase 8) |
| 4 | No-show recovery | Appointment status = "No Show" on the Strategy Session / Position Map calendar (`34KkdVJncaYiuAOjE0FP`) | Immediate (within 1 hour) WhatsApp + email with a reschedule link; a second follow-up on day 3 if unrescheduled | GHL native workflow | S | Medium–High — recovers bookings that would otherwise leak silently between "Booked Call" and "Appointment" stages | None — buildable now |
| 5 | Stale-opportunity alerts | Opportunity sits in a 1-To-1 Pipeline stage (e.g. "Responded", "Booked Call") with no activity for 5+ days | Auto-tag "stale"; internal task/notification to founder or ops owner; optional soft auto-nudge message to the lead | GHL native workflow | S | Medium — feeds directly into the Weekly Action Review (Section 4) | None — buildable now |
| 6 | Monthly KPI sheet auto-pull | Scheduled (1st of month) or GHL webhook on key events (Won, Appointment Booked) | Make.com scenario pulls GHL API data (pipeline stage counts, attribution field roll-ups) into the KPI Dashboard's Funnel Metrics and CRM Pipeline Velocity tabs | Make.com + GHL API + Google Sheets API | M | High — removes the manual CRM data entry from the monthly reporting cycle | Confirm GHL plan includes API/webhook access before building (Questions To Clarify #3) |
| 7 | AI-visibility test reminder task | Scheduled monthly (1st Monday) | Creates a recurring task/calendar reminder assigned to the Test Bank owner to run the 62-row protocol (Section 2.2) | GHL native task automation, or Make.com + Google Calendar | S | Medium — pure process discipline, but the whole Test Bank fails silently without it | None — buildable now; build alongside Automation 5 since both are process-guardrail automations |

**Build sequence:** 4 and 5 first (no dependency, immediate CRM hygiene value) → 7 alongside them (cheap, protects Section 2) → 3 once Phase 8 claims the GBP listing → 1 once the diagnostic and its `spl_*` fields exist → 2 immediately after 1 → 6 last, once GHL API/webhook access is confirmed.

---

## 6. DATA SOURCE MAP

| Metric area | System of record | Access needed | Gap today |
|---|---|---|---|
| Branded/non-branded search volume, page rankings | Google Search Console | Verify thereimethod.com (and secondpropertyladder.com, legacylaunch.com.sg once attached, per D3) in GSC; confirm ownership access | **[VERIFY]** GSC verification status unconfirmed on any domain (Master Brief Q3) |
| Organic traffic behaviour, on-site funnel steps | GA4 | Install a GA4 property + tagging on thereimethod.com, secondpropertyladder.com, legacylaunch.com.sg | **[VERIFY]** GA4 not confirmed installed anywhere |
| AI answer visibility (ChatGPT/Perplexity/Gemini/AI Overview) | Manual test log (no vendor API exists for this) | Logged-out browser access, screenshot discipline (Section 2.2) | No current process; zero baseline exists — this file establishes the first one |
| YouTube search visibility, subscriber/view stats | YouTube Studio Analytics | Studio login access (confirm who currently holds channel admin) | Subscriber/video counts (~600+ videos, 2,000+ subscribers) **[VERIFY]** per funnel copy, not yet confirmed against Studio |
| GBP views/calls/messages, reviews | Google Business Profile Manager | Claim/verify the listing behind share.google/bpyWTGgjlyNxt8Xiz; confirm admin access | **[VERIFY]** listing name, primary category, review count all unconfirmed (Master Brief Q2) |
| Funnel conversion rates, consult bookings | GHL (funnels, calendar `34KkdVJncaYiuAOjE0FP`, opportunities) | Existing access via location `cyeYxFVQE1l73kO6S6Lx` | None for Legacy Launch V2 (live); the diagnostic funnel itself does not exist yet |
| Lead quality (grade distribution) | GHL custom fields (`spl_lead_grade`, etc.) | Field creation in GHL | `spl_*` fields do not exist (confirmed absent, Report 2) |
| CRM stage movement/velocity | GHL 1-To-1 Pipeline | Existing access | **Changi Green contacts (tagged via `cg_*` fields or membership in "Changi Green-Tenant Cycle" pipeline) must be tagged and excluded from every advisory report NOW** — per D1, Changi Green is a separate business line and must never be cross-reported. Untagged, every stage count and velocity number in this system is polluted. |
| Content-to-lead attribution | GHL contact fields (`utm_source`, `ad_id`, `ad_name`, `campaign_id`, `campaign_name`, `click_id`) | Fields already exist; no new access needed | No confirmed current UTM-tagging convention or audit — fields are populated only if every ad/link is tagged consistently, which is not yet verified |
| Review velocity | Google Business Profile (reviews tab) + any secondary review sources | GBP Manager access | Same GBP claim gap as above |
| Backlinks/mentions | Search Console "Links" report (free baseline) or a paid tool (Ahrefs/Semrush) if licensed | GSC access, or tool licence | No paid backlink tool confirmed in use; GSC Links report is directional-only, not a full backlink index |
| Social visibility (secondary signal feeding AI/YouTube visibility) | Meta/IG native insights; GHL Social Planner (enabled, unused) | Connect Facebook/Instagram/YouTube accounts to GHL Social Planner | **Zero social accounts currently connected to GHL** (Report 2) — social KPIs are native-platform-only until Phase 7 connects them |

---

## 7. BASELINE CAPTURE PLAN (Week 1, before any changes go live)

This must run **before** Phases 3 (Domain Architecture), 4 (Sitemap), 7 (Social), and 8 (GBP) execute anything public-facing. Without this snapshot, no later "improvement" claim is provable — it will look like an opinion, not a result.

1. **Search Console export.** If thereimethod.com is already verified, export the last 90 days of query/impression/click data now, before any content changes. If unverified, verify it first (First 5 Actions #1), then capture whatever historical data GSC retroactively shows (GSC can show up to 16 months back once verified) — note in Tab 8 that the "before" window may be thin.
2. **Manual ranking snapshot.** For every target query in the Test Bank (especially the `what-is` and `safest-way` categories), run an incognito Google search from a Singapore location/VPN, screenshot the SERP, and log current rank (or "not found in top 50") in Tab 8.
3. **GBP Insights export.** Before Phase 8 touches the listing, export current views, calls, direction requests, messages, review count, and average rating from GBP Manager. Screenshot the live listing (name, category, photos) as it exists today.
4. **Full AI Visibility Test Bank run.** Run all 62 rows once this week, following the Section 2.2 protocol exactly, and label the output "Baseline — Week 1" in Tab 2 and in the screenshot folder. Expect mostly 0s (Section 2.2.8) — that is the number every later month is measured against.
5. **YouTube stats export.** From YouTube Studio: current subscriber count, total views, top 10 videos, and the "Traffic source: YouTube search" report as of this week. Screenshot the channel's current banner, description, and about page **before** Phase 7 rewrites them.
6. **CRM baseline.** Export current 1-To-1 Pipeline stage counts and velocity, with Changi Green contacts already tagged out (do this tagging first — see Data Source Map, row 8), into Tab 8.
7. **Social baseline.** Screenshot current follower counts and bio text for Facebook (facebook.com/coachedmundtan), Instagram (instagram.com/propertycoachedmundtan), and YouTube, before Phase 7's handle/bio changes land.
8. **Domain/backlink baseline.** Before D4's redirects execute (singaporerealestateinsider.com → thereimethod.com; 6figurepropertyprofits.com retired), run the GSC Links report (or a licensed tool) against each domain being retired, so any existing backlink equity is documented before it's redirected away.
9. **Store everything in one place.** A single dated folder, e.g. `AEO_REPOSITIONING_OS/_BASELINE_2026-07/`, with a short baseline log noting explicitly what could and could not be captured (e.g. "GA4 baseline: none — not installed as of this date").

---

## CONCERNS

1. **GA4/GSC uncertainty blocks 6 of 15 KPI areas** (branded search, non-branded visibility, page rankings, and indirectly funnel/attribution accuracy). This is the single biggest risk to this entire measurement system and should be resolved in week 1, not deferred.
2. **The diagnostic doesn't exist yet.** Lead quality (KPI #11), and Automations 1–2 in the backlog, all depend on a product (the "Which Step Are You On?" quiz) that is spec'd but unbuilt. This file treats that as a known, sequenced dependency (see Dependencies below) rather than pretending the automation can ship today.
3. **GHL location timezone is set to Asia/Kuala_Lumpur, not Asia/Singapore** (Report 2). This is a one-hour offset that will quietly skew "days-in-stage" velocity calculations and monthly cutoff boundaries (e.g. a lead logged at 11:30pm SGT on the 31st could be timestamped into the wrong month). Flagging as a fix, not assuming it will be corrected by another phase.
4. **No backlink tool is confirmed licensed.** The Data Source Map treats GSC's free Links report as the fallback, but it undercounts referring domains relative to Ahrefs/Semrush-class tools. If budget allows, recommend licensing one before Phase 12's first monthly report, so KPI #15 isn't built on a known-weak proxy from month 1.
5. **AEO test-bank target pages are marked "[pending Phase-4 slug]"** because 04_WEBSITE_SITEMAP_AND_PAGE_ROADMAP.md has not been built yet in this run. Once it exists, the CSV's `target_entity_or_page` column should be updated with exact URLs — flagged here so that update isn't missed.

---

## QUESTIONS TO CLARIFY

1. Is there any existing GA4 property or Search Console verification for thereimethod.com, secondpropertyladder.com, or legacylaunch.com.sg — under whose Google account, if so?
2. Who owns the manual monthly AI-visibility testing ritual and the weekly 30-minute review — Edmund, Cindior, or a dedicated ops hire? This system assumes one consistent owner; unassigned, it will lapse within two months.
3. Does the current GHL SaaS plan include the API/webhook access Automation 6 (KPI auto-pull) needs, or is that a paid add-on tier?
4. What WhatsApp/SMS cadence is compliant under PDPA/DNC for the lead-grade-A instant-contact and no-show-recovery automations? Needs a compliance read on message templates before Automations 2 and 4 go live (ties to D7).
5. Is a backlink monitoring tool (Ahrefs, Semrush, or similar) already licensed anywhere in the business, or should Phase 12 budget for one?
6. Who currently holds admin access to the Google Business Profile listing behind share.google/bpyWTGgjlyNxt8Xiz?

---

## DEPENDENCIES

- **Phase 3 (Domain Architecture):** final domain/redirect decisions must land before the backlink baseline (Section 7.8) and before GA4/GSC properties are finalised for secondpropertyladder.com and legacylaunch.com.sg.
- **Phase 4 (Website Sitemap and Page Roadmap):** exact page slugs are needed to replace every "[pending Phase-4 slug]" placeholder in the Test Bank's `target_entity_or_page` column.
- **The "Which Step Are You On?" diagnostic (Phase 10/offer ladder):** must be built and the 14 `spl_*` fields created in GHL before KPI #11 (lead quality) and Automations 1–2 can function.
- **Phase 7 (Social Profile Repositioning):** social accounts must be connected to GHL Social Planner before social-driven attribution can be tracked in GHL; also gates the "social baseline" step (Section 7.7) timing.
- **Phase 8 (Google Business Profile Plan):** the GBP listing must be claimed/verified before KPI #8, #14, and Automation 3 (review-request workflow) are usable.
- **GA4 + Search Console verification** (owner TBD — Questions To Clarify #1): blocks KPI areas #1, #2, #3 entirely until resolved.

---

## FIRST 5 ACTIONS

1. **Verify/install Google Search Console and GA4 on thereimethod.com this week** (extend to secondpropertyladder.com and legacylaunch.com.sg once those domains are attached per Phase 3/D3). This single action unblocks 6 of the 15 KPI areas.
2. **Tag and segment every Changi Green contact in GHL now** — bulk-tag by presence of `cg_*` fields or membership in the "Changi Green-Tenant Cycle" pipeline — before pulling any baseline CRM number. This must happen before Section 7.6, not after.
3. **Run the full 62-row AEO Visibility Test Bank once this week**, logged out, screenshotted, scored, and labelled "Baseline — Week 1" — before any Phase 3/4/7/8 content change ships.
4. **Export GBP Insights and YouTube Studio analytics now**, and screenshot both profiles as they currently exist, before Phase 7 and Phase 8 touch either.
5. **Build the 8-tab KPI Dashboard Google Sheet** per Section 1.2 and populate Tab 8 (Baseline Snapshot) with everything captured in Actions 1–4.
