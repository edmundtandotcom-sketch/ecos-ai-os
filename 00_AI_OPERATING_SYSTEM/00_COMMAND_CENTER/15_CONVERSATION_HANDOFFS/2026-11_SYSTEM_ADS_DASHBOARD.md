# Handoff — System Ads Dashboard
Conversation: "System Ads Dashboard"
Period: 2026-11-03 → 2026-11-15
Transcript: 63.6 MB, 447 turns (desktop only)
Recorded: 2026-11-17

---

## 1. What this thread is

Two pieces of work that grew out of one another:

1. **REI Performance OS v9/v10** — the Meta + Google + GHL ads dashboard, a Google
   Apps Script web app reading a master sheet.
2. **The USD 68k mentorship decision pack** — a slide deck built to decide whether to
   buy a mastermind/mentorship place, argued from 15 months of real ad results.

## 2. Standing rules established here

**Tabulate from GHL, not from Meta directly.** Edmund reports off GHL, so the
dashboard must agree with GHL rather than with Meta's own attribution. Meta supplies
spend; GHL supplies the funnel.

**Two pipelines, never blended.** The 1-To-1 pipeline is high-ticket. The Webinar
pipeline is its own ladder. A webinar signup and a 1-to-1 lead are not the same
commitment and must not be summed into one funnel.

**The 30 October cutoff.** One ad ("9 Oct–30 Oct–4 Nov–Webinar + HT") ran both
objectives. The ruling: **anything before 30 Oct counts as webinar, anything from
31 Oct counts as high-ticket.** This is a manual rule, not something the data states.

**Won deals are only those explicitly marked won, with a figure.** A contact can
appear in both pipelines; that must not double-count. One deal was present as closed
in 1-To-1 while actually belonging to the 1-to-many pipeline.

**Guru stays out of the dashboard.** Tracked separately, by decision.

## 3. Metrics required per segment

| High-ticket | Webinar |
|---|---|
| Spend | Spend |
| Leads | Leads (opt-ins) |
| Responded | Attended |
| Booked call | Booked call |
| Appointments | Appointments |
| Strategy sessions | Strategy sessions |
| Closed won | Closed won |
| Cost per lead / booked call / appointment / close | same |

Edmund's stated purpose is to see where each stage leaks, per campaign, so ads can be
improved stage by stage — not a single blended scoreboard.

## 4. Where the dashboard stands

- **v10.6.0** adds a badge on every card (`ALL`, `HIGH-TICKET`, `WEBINAR`) plus two
  split lines under each combined number, so the All view reads unambiguously.
- Attended cards carry the WEBINAR badge; Responded carries HIGH-TICKET, because each
  belongs to exactly one segment.
- Source of truth for the code is
  `00_AI_OPERATING_SYSTEM/08_OPERATIONS/02_SCRIPTS/REI_PERFORMANCE_OS_V9/01_SOURCE_CODE/`,
  which **is** in this repository and readable from a cloud session.
- Deployment details, including the live URL, are in
  `../../08_OPERATIONS/02_SCRIPTS/REI_PERFORMANCE_OS_V9/02_DEPLOYMENT_AND_GUIDES/DEPLOYMENT_RECORD_v9.0.md`.

**Known trap, cost four days in August 2026:** the live project is **standalone**, so
the spreadsheet's own menu belongs to a different, retired bound project. Credentials
entered through that menu land in the wrong place and the dashboard returns HTTP 401.
Store credentials in the **live project's Script Properties** only.

**Blended cost per lead is not like-for-like.** Combined CPL was SGD 78 on
SGD 10,952 ÷ 141 leads, but webinar supplied 135 of those 141, so the blend sits
almost on the webinar figure. The high-ticket SGD 171 rested on 6 leads and about
SGD 1,029 of spend and will swing hard week to week. Use each segment's own CPL for
decisions; compare segments on cost per booked call or cost per close.

## 5. The USD 68k decision pack

Deck: <https://claude.ai/artifact/5ZxB2Qh5xVgN9a3qqvmUR5> — 27 slides, a 19-slide main
pack plus an 8-slide appendix, rebuilt around one chart per slide.

**Baseline from 15 months:** cost was 44% of commission at SGD 40k a case, 32% at
SGD 55k. Only the webinar channel came near the 20% target (webinar 19%, high-ticket
64%, total 44%).

**Funnels measured:** webinar 339 → 198 attended → 15 applications → 3 closes;
high-ticket 412 → 69 → 6.

**Scenario set** (setter fixed at 1–3 extra appointments per webinar, not scaling with
spend):

| | Before (15 mo) | Best | Normal | Worst |
|---|---|---|---|---|
| Closes | 10 | 39 | 15 | 6 |
| Commission at 40k / 55k (SGD k) | 400 / 550 | 1,575 / 2,165 | 610 / 838 | 253 / 347 |
| Cost % without the 68k | 44% / 32% | 19% / 14% | 44% / 32% | 103% / 75% |
| Cost % with the 68k | – | 24% / 18% | 59% / 43% | 138% / 100% |

- The 68k needs roughly **3.4 extra closes (22%)** to beat putting the same money into ads.
- Ads per close: SGD 5.1k Best, 13.1k Normal, 31.7k Worst.

**The improvement ladder** — how Normal's SGD 13.1k ads-per-close comes down, stacked
in order. The 20% allowance is SGD 9.2k at 55k cases and SGD 6.4k at 40k:

| Step | Ads per close | Closes/yr |
|---|---|---|
| Normal today | 13.1k | 15 |
| 1. Cost per opt-in 75 → 60 | 11.2k | 18 |
| 2. Attend 40% → 50% | 9.5k | 21 |
| 3. Application 6.4% → 7.6% | 8.3k | 24 |
| 4. Close rate 15% → 18% | 7.2k | 28 |
| 5. Setter 2 → 3 appts | 6.6k | 30 |
| 6. 20 free opt-ins per webinar | 5.4k | 37 |

At SGD 55k cases, steps 1–3 suffice. At SGD 40k, steps 1–5 get close. Free opt-ins are
the single largest lever but no lever is sufficient alone.

**Volume is the binding constraint.** Current run rate is about 38 opt-ins a week;
SGD 2m needs 81 (at 55k cases) to 119 (at 40k), and SGD 3m needs 132 to 190 — two to
five times current volume, with cost per opt-in *holding* at SGD 60 while spend rises.

**Benchmark search outcome:** there is **no authoritative benchmark** for agent
marketing spend as a share of commission, in Singapore or globally. CEA publishes
none; NAR's agent profile does not break it out. Vendor blogs cluster around 10% of
gross commission (range 5–25%), 8–12% for established agents, 15–30% for new ones.
Treat all of it as rough, and note one source argues the denominator should be
commission retained *after* the agency split.

## 6. Open items

- **Meta access token is not stored.** Needs `META_ACCESS_TOKEN`, `META_APP_ID` and
  `META_APP_SECRET` in the live project's Script Properties. Without the app id and
  secret, the weekly auto-renew cannot run and the 60-day expiry bites.
- **`installV9Triggers` has never been confirmed as run.** This is why nothing
  reconciles nightly and why the token lapsed.
- **v10.6.0 was built but not deployed** as of 2026-11-11, blocked on the browser pane
  losing its Google sign-in. Deployment needs Edmund signed in; a password cannot be
  typed on his behalf.
- **Deck layout was never visually verified** in the live viewer — charts were checked
  in a local render only.
- Google campaigns genuinely stopped spending on 2026-07-12; that is real, not a sync gap.
