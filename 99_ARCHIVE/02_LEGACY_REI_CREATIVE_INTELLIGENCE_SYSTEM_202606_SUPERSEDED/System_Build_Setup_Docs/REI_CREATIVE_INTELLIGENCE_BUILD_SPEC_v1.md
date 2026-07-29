# REI Creative Intelligence — Build Spec v1
**Owner:** Coach Edmund Tan | **Date:** 2026-06-13
**Purpose:** Evolve the single-campaign Legacy Launch dashboard into ONE scalable platform that monitors every campaign and auto-pulls data from Meta + Google — no manual input, no separate dashboards per campaign.

---

## PART A — THE ARCHITECTURE PRINCIPLE (read this first)

The mistake to avoid: one dashboard per campaign. That forces you to open many files and re-instruct each time.

The fix: **one data store + one dashboard**, where every variable is a *column/filter*, not a separate file.

Dimensions (filters) on every creative row:
- **Campaign** (Legacy Launch, Family Legacy, future…)
- **Angle** (01–10, expandable — not capped)
- **System** (1–10, the visual format)
- **Hook Psychology** (the why-it-clicks)
- **Format** (image / 9:16 video / 16:9 video / carousel)
- **Offer / Lead Magnet** (session, checklist, ebook, report — what the ad points to)
- **Funnel Track** (A quality / B volume / retarget)
- **Status** (testing / winner / kill / scaling)

With these as filters, a NEW campaign = new rows tagged with a new campaign name. Nothing gets rebuilt. The matrix and angle list just grow.

---

## PART B — MEDIA TYPES & ASSETS: combine or separate?

**Combine into one platform; separate by FIELD, not by file.**

- Images, 9:16 videos, 16:9 videos, carousels are all **creatives** → one table, tagged by `Format`. The dashboard is NOT image-only; it tracks any creative.
- PDFs, checklists, reports, ebooks are **offers / lead magnets** — i.e. *what the ad drives to*, not ads themselves. They live as an `Offer` dimension linked to the creative. Track which offer each ad points to and which offer converts best — but don't list them as if they were ad creatives.

Result: one dashboard, every asset type visible, filter to whatever you want.

---

## PART C — DATA LAYER: how auto-pull actually works

The dashboard cannot itself "log in" to Meta/Google. Data has to be pulled by something that runs on a schedule, then written to a store the dashboard reads. Recommended store: **a Google Sheet** (you already live in Drive; it's free, shareable, and both connectors and the dashboard can read/write it).

```
Meta Ads  ─┐
            ├─►  [Connector / script, runs daily]  ─►  Google Sheet (master data)  ─►  Dashboard (reads & scores)
Google Ads ─┘
```

### Can we connect directly, or is a 3rd-party app needed?
Both are possible. Honest trade-offs:

**Option 1 — Direct API (no 3rd-party fees)**
- *Meta:* Meta Marketing API. Doable and well-documented.
- *Google Ads:* Google Ads API — heavier; the developer token needs Google approval, which takes time.
- Needs code AND somewhere to run on a schedule (Google Apps Script attached to the Sheet is the cleanest "free, always-on" host).
- **I can write all of this code.** What I cannot do: be the live connection myself or hold your tokens — there's no always-on server on my side, and credentials must never be pasted into chat. The script runs in *your* account.

**Option 2 — No-code connector (fastest, small monthly fee)**
- Tools: **Supermetrics**, **Make**, or **Zapier** pull both Meta + Google into the Sheet on a schedule with no code.
- Best if you want it live this week and don't want to manage API approvals.
- You already have a Supermetrics connector available in this workspace.

**Recommendation:** Start with Option 2 (connector → Sheet) to get auto-tabulation live fast, then optionally migrate Meta to direct API later to cut cost. Either way the dashboard stays the same — it just reads the Sheet.

### What you must provide to connect
**Meta (Marketing API / connector):**
- Meta Business Manager access (admin)
- Ad Account ID (format `act_XXXXXXXXX`)
- For direct API: a Meta Developer App (App ID + App Secret) and a System User access token with `ads_read`
- For connector: just authorize Meta in Supermetrics/Make

**Google (Google Ads):**
- Google Ads Customer ID (format `XXX-XXX-XXXX`)
- For direct API: Developer token (apply in Google Ads API Center) + OAuth client ID/secret + refresh token
- For connector: just authorize Google in Supermetrics/Make
- (If you actually mean Google **Analytics/GA4** rather than Google Ads, say so — different setup: GA4 Property ID + Data API.)

> Security: never paste tokens/secrets into this chat. They go into the connector's auth screen or the Apps Script's secure properties on your side.

---

## PART D — TOP-MEDIA-BUYER ANALYTICS LAYER (what a great buyer tracks to decide spend)

The current tracker logs the basics. To make real money-allocation decisions, add these.

### 1. Funnel metrics (full path, not just clicks)
- Hook rate (3-sec views ÷ impressions)
- Hold rate (ThruPlay ÷ 3-sec views) — *video only*
- CTR (link) and CPC
- CPL (cost per lead) AND **cost per QUALIFIED lead** (your lead-quality input is what most dashboards miss)
- Landing page view rate, LP → booking rate
- **Cost per booked session** and eventually **cost per closed deal / ROAS** — the only number that truly decides spend

### 2. Decision rules built into the tool (with a clock)
You correctly flagged the tracker doesn't say *when* to act. Standard cadence:
- **Day 0–3 — Learning:** don't touch unless catastrophic. Wait for a minimum data threshold (~1,000–2,000 impressions or ~50+ link clicks per creative), because *statistical significance matters more than the calendar*.
- **Day 3 — Kill check:** kill any creative with hook rate <25% OR CPL >2× ad-set average once it has enough data.
- **Day 5 — Iterate:** mid-tier creatives get ONE change (new hook/headline/thumbnail or swap image↔video) and a second look.
- **Day 7 — Scale check:** duplicate winners into a scaling ad set (or raise budget ~20–30%/day to avoid resetting learning); retire losers.
- **Ongoing — fatigue watch:** when frequency >2.5 and CPL climbs, refresh the creative.

The dashboard should auto-flag each creative with a verdict (KEEP / KILL / ITERATE / SCALE) and show its checkpoint date — so it tells you what to do without being asked.

### 3. Budget allocation view
- Spend share vs lead share per campaign/angle/format (find where money is wasted)
- Track A / B / retarget split actual vs target (60/30/10)
- Marginal CPL as budget scales (does CPL hold when you spend more?)

### 4. Creative intelligence (ideas, copy, angles — not just numbers)
- **Angle leaderboard:** which angle produces the cheapest qualified leads → make more of it
- **System leaderboard:** which visual format wins per angle → the Angle × System matrix, updated with REAL results
- **Hook leaderboard:** which Hook Psychology converts → directs future copy
- **Winner → next-idea engine:** when a creative wins, the dashboard suggests the next variations to test (same angle, untested systems; same system, adjacent angles) so production is directed, not random
- **Copy/headline test log:** track which headline + primary-text combos win, feeding your next scripts

### 5. Lead-quality feedback loop
- A field where sales rates each lead (e.g. 1–5 or qualified/junk) flows back in, so CPL becomes **cost per QUALIFIED lead**. This is what separates real buyers from vanity dashboards — you optimize to revenue, not to cheap clicks.

---

## PART E — THE MATRIX: how "tested" vs "try" was decided (honest answer)

In the current dashboard the Angle × System matrix shows green ("tested") and gold ("try next") cells. Grounded in your master doc:

- **Green / "tested" really means "already produced"** — these are the 6 creative groups built from your existing 100+ images (Group 1 Disqualification, Group 2 Trap/Fear, Group 3 Insider/Forensic, Group 4 Practitioner, Group 5 Authority, Group 6 Checklist). They exist in the asset bank. **They were NOT yet validated by live ad performance** — so "tested" overstates it. More accurate label: **"Built."**
- **Gold / "try next" = recommended combinations** derived from the master doc's per-angle mapping (each ANGLE's *Best System Match* + *Best Hook*), e.g. ANGLE_02 Forever-Home-Trap → System 2 + System 5, Hook = Future Regret + Buyer Blindspot.
- **Yes — the reasoning is the Hook Psychology.** The recommendations come from matching each angle's psychological driver to the visual system that best amplifies it. That logic is exactly the "Hook Psychology by System" section.

**Fix in v2:** relabel green to "Built," and add a third state — true **"Validated"** (green only after live data confirms the combo wins). That way the matrix reflects reality, and gold cells graduate to validated as results come in.

---

## PART F — BUILD SEQUENCE

1. **v2 dashboard + master Google Sheet** — add Campaign/Format/Offer/Track dimensions; relabel matrix (Built / Try / Validated); add verdict + checkpoint logic.
2. **Auto-pull live** — connect Meta + Google via connector (fast) into the Sheet; dashboard reads it.
3. **Lead-quality loop** — add the sales-rating field and cost-per-qualified-lead.
4. **Creative intelligence views** — angle/system/hook leaderboards + next-idea engine.
5. **Direct API migration (optional)** — move Meta to Apps Script to cut connector cost.

Step 1 can be done now without any credentials. Steps 2 needs your Meta/Google access (connector authorize) and the desktop/Chrome reconnected for any UI work.
