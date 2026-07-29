# REI Creative Intelligence System — SOP v1 (Model Version)
**Owner:** Coach Edmund Tan | **Date:** 2026-06-13 | **Status:** Master SOP — model this for every campaign
**Scope:** One platform to plan, deploy, track, and optimize all ad creative across campaigns (images, videos, carousels) with auto-pulled Meta + Google data, lead-quality tracking, and advisory recommendations.

> HOW TO USE THIS SOP: This is the standard. Each new campaign reuses this exact structure — only the campaign tag and creative change. Build once, repeat forever. Sections marked **[SETUP — desktop]** require desktop + credentials and are done after this doc is approved.

---

## 0. CORE PRINCIPLE — ONE PLATFORM, NEVER MANY

Never build a dashboard per campaign. Build ONE data store + ONE dashboard where every variable is a *filter*, not a separate file. A new campaign = new rows tagged with a new campaign name. Nothing gets rebuilt.

Filter dimensions on every creative:
**Campaign · Angle (01–10, expandable) · System (1–10) · Hook Psychology · Format (image / 9:16 video / 16:9 video / carousel) · Offer/Lead Magnet · Funnel Track (A/B/Retarget) · Status (Built / Testing / Validated / Kill / Scaling)**

---

## 1. ASSET FRAMEWORK — ANGLE × SYSTEM × HOOK

Every creative needs all three layers:
`ANGLE (what story) + SYSTEM (how it's shown) + HOOK PSYCHOLOGY (why it clicks)`

- **10 Angles** = content direction (the tension/story).
- **10 Systems** = visual format/architecture (HOW it's produced).
- **10 Hook Psychologies** = the emotional trigger driving the click (guides the copy).

Production sequence for any ad: pick Angle → choose best-fit System → apply matching Hook → produce creative + write copy.

### Matrix states (corrected labels)
The Angle × System matrix uses THREE states — not "tested vs try":
- **BUILT** — creative exists in the asset bank but has no live results yet (was mislabeled "tested" in v1).
- **TRY** — recommended combination, derived from matching the angle's psychological driver to the system that amplifies it (this reasoning = the Hook Psychology).
- **VALIDATED** — proven by live data (hits target cost-per-qualified-lead). A cell turns green ONLY here.

A combo's journey: TRY → BUILT → (run it) → VALIDATED or KILL.

---

## 2. CAMPAIGN STRUCTURE & FUNNEL TRACKS

### Tracks
- **Track A — Quality:** Video (or strong image) cold → **Landing Page** → book Strategy Session. High intent, lower volume.
- **Track B — Volume:** Checklist ad → **Lead Form** → GHL nurture → session. Higher volume, longer cycle.
- **Retargeting:** warm audiences (25%+ video viewers, engagers, LP non-bookers) → Practitioner/Authority creative + checklist.

### Capture rule (fixed)
- **Checklist / lead magnet → Lead Form** (low-commitment; instant; 2 qualifying questions).
- **Strategy Session → Landing Page** (high-ticket; needs belief shift + proof before booking).

### Checklist 2-Version Quality Test (active experiment)
Goal: which placement yields better-QUALITY leads (cost per *qualified* lead + qualified-appointment rate). Hold capture constant, vary only audience:
| | Version A — Retargeting | Version B — Cold Main |
|---|---|---|
| Campaign | `LL_LGR_CHECKLIST_RETARGET` | `LL_LGR_CHECKLIST_COLD` |
| Audience | Warm (viewers + engagers) | Cold (Advantage+, SG, 30–55) |
| Offer / Capture | Checklist / Lead Form | Same checklist / identical Lead Form |
| Qualifiers (identical) | Own condo/HDB? · Timeline? | same |
| Primary metric | Cost per qualified lead | Cost per qualified lead |
Scale the winner; optional Version C later (cold → LP framing → form).

### Budget guides
- Default launch: 80% Track A (cold video) / 20% Retarget checklist.
- If promoting checklist to cold Track B: 60% video / 30% checklist cold / 10% retarget.

---

## 3. NAMING CONVENTIONS (ENFORCE — the dashboard parses these)
- **Video:** `LL_LGR_[ANGLE]_[HOOK]_v#` → e.g. `LL_LGR_AGENTMYTH_PitchVsReality_v1`
- **Image:** `A[ANGLE#]_SYS[SYSTEM#]_[TYPE]_v#` → e.g. `A02_SYS02_IMG_v1`
- One mistyped name = a row that won't roll up. Lock it.

---

## 4. DATA LAYER & AUTOMATION (no paid app)

```
Meta Ads  ─┐
            ├─►  Google Apps Script (free, daily timer)  ─►  Google Sheet (master data)  ─►  Dashboard (reads + scores)
Google Ads ─┘
GHL (leads + appt status) ─────────────────────────────────►  Google Sheet (Lead Log)
```

- **No Supermetrics / no paid SaaS.** Google Apps Script is built into Google Sheets at $0.
- The Sheet is the single source of truth for ad metrics; GHL is source of truth for lead status (synced one way into the Lead Log).

### [SETUP — desktop] What to connect
- **Meta Marketing API:** Meta Developer App (App ID + Secret) + System-User token with `ads_read`; Ad Account `act_1467621970951606`. For offline optimization: Conversions API access token + dataset/pixel ID.
- **Google Ads API:** Developer token (apply in API Center — Google approval, allow a few days) + OAuth client ID/secret + refresh token; Customer ID `185-178-8166`.
- Credentials live in Apps Script's secure Script Properties in your account — never in chat or in the Sheet body.

---

## 5. TRACKING SCHEMA (the Sheet tabs)

### Tab 1 — Creative Inventory
Creative ID (named per convention) · Campaign · Angle · System · Hook · Format · Offer · Track · Status · Launch date · Drive link.

### Tab 2 — Ad Performance (auto-pulled daily)
Date · Creative ID · Campaign · Spend (SGD) · Impressions · 3-sec views · ThruPlay · Link clicks · Leads · Hook rate · Hold rate · CTR · CPC · CPL. Formulas auto-calc the rates.

### Tab 3 — Lead Log (your manual + synced fields)
**Lead name · Email · Mobile · Ad Campaign · Group · Ad Source (specific ad) · Date in · Qualified? (Y/N) · Appointment booked? (Y/N) · Appointment date · Appointment qualified? (Y/N) · Outcome (showed/no-show/closed) · Lead-quality score (1–5) · Source platform (Meta/Google).**
Cost roll-ups derived: **Cost per Lead · Cost per Qualified Lead · Cost per Appointment · Cost per Qualified Appointment** (spend joined by Campaign/Group/Ad Source).

### Tab 4 — Leaderboards
Angle leaderboard · System leaderboard · Hook leaderboard — ranked by cost per qualified lead. Drives the next production decisions.

### Tab 5 — Targets / Benchmarks
Target CPL · target cost per qualified lead · target cost per qualified appointment · max frequency. The dashboard flags actuals against these.

---

## 6. RECOMMENDATION ENGINE (advisory — you activate)

The system NEVER auto-kills or auto-scales. It surfaces a prompt; you approve and act.
Examples it surfaces:
- "Ad A02_SYS02: hook 18% (<25%), CPL 2.3× avg → **Recommend KILL**."
- "Video PitchVsReality: cost/qualified-lead 30% under target, frequency 1.4 → **Recommend SCALE +20%/day**."
- "Group 3 mid-tier: CTR fine, CPL high → **Recommend ITERATE headline/thumbnail**."

### Checkpoint cadence
- **Day 0–3 Learning:** don't touch unless catastrophic. Wait for ~1–2k impressions / ~50+ clicks per creative (significance > calendar).
- **Day 3 Kill check:** flag hook <25% OR CPL >2× ad-set avg.
- **Day 5 Iterate:** one change to mid-tier (hook/headline/thumbnail or image↔video swap).
- **Day 7 Scale check:** duplicate winners / raise budget ~20–30%/day; retire losers; introduce next group.
- **Ongoing Fatigue:** frequency >2.5 + rising CPL → refresh.

---

## 7. OFFLINE CONVERSION FEEDBACK (the biggest lever) [SETUP — desktop]

Send real outcomes back so the algorithms optimize toward people who QUALIFY, not cheap form-fills.

### Meta
1. **Measurement (manual, easy):** Events Manager → create Offline Event Set → import CSV of events (Lead, AppointmentBooked, AppointmentQualified) with hashed email/phone + event time. Do periodically.
2. **Optimization (automated, powerful):** send a live custom event (e.g. `QualifiedAppointment`) via the Conversions API, then set campaigns to optimize for it. I automate this push from the Lead Log/GHL — no manual upload. Requires CAPI token + dataset/pixel.

### Google Ads
- Use **Offline Conversion Import (OCI)** keyed to **GCLID**. Runs as a **free scheduled import from a Google Sheet** — no manual uploads.
- **Requirement:** the GCLID must be captured at lead time (on the LP) and stored with the lead. Meta-form leads have no GCLID, so Google OCI only covers Google-Ads-driven leads.
- Setup: Google Ads → Goals/Conversions → create conversion actions (AppointmentBooked, AppointmentQualified) → Uploads → schedule from Sheet.

---

## 8. ATTRIBUTION, DE-DUP, PDPA

### UTM / naming
- **Meta:** UTMs work — keep campaign/group/ad in the URL template. (Already tracking well.)
- **Google Ads:** uses GCLID auto-tagging, not UTMs, so names don't appear in the URL — this is expected, not a bug. **Fix:** pull campaign/ad-group/ad names directly from the Google Ads API (joined by ID). No extra UTM work needed on Google. Keep GCLID for conversions.

### Lead de-duplication
The same person can enter more than once (sees Meta video AND clicks Google ad; submits checklist twice; already in GHL). De-dup = treat them as ONE person (match on normalized email + mobile, keep first-touch attribution, merge in GHL). Without it, cost-per-qualified-lead is inflated by counting one human as 2–3 leads and they get double-nurtured.

### PDPA (Singapore)
A Meta/Google opt-in covers the submission, but PDPA wants explicit consent for *your* collection/use of personal data. Ensure each lead form has a consent line + privacy-policy link + a way to withdraw. (Not legal advice — confirm with whoever handles compliance.)

---

## 9. BUILD & SETUP SEQUENCE

| # | Step | Needs | Where |
|---|---|---|---|
| 1 | v2 master tracker (this schema: Inventory, Performance, Lead Log, Leaderboards, Targets) | none | now |
| 2 | v2 dashboard (reads Sheet; Built/Try/Validated matrix; recommendation prompts) | none | now |
| 3 | Create native Google Sheet matching schema | Google acct | desktop |
| 4 | Apps Script: pull Meta + Google daily into Sheet | Meta App + token; Google dev token + OAuth | desktop |
| 5 | GHL → Lead Log sync + GCLID capture on LP | GHL access | desktop |
| 6 | Offline conversions: Meta CAPI + Google OCI | tokens + conversion actions | desktop |
| 7 | Targets/benchmarks + fatigue + de-dup rules | your numbers | now/desktop |

Steps 1, 2, 7 need no credentials and can be built from mobile now. Steps 3–6 are desktop + credentials, done after this SOP is approved.

---

## 10. CONFIG BLOCK
- **Google Ads Customer ID:** 185-178-8166
- **Meta Ad Account ID:** act_1467621970951606
- **CRM:** GoHighLevel (GHL) — connected
- **Data store:** Google Sheet (to be created) | **Automation:** Google Apps Script (free)
- **Connected now:** Google Drive, Gmail, Calendar, GHL
- **Needed for automation (desktop):** Meta Developer App + token; Google Ads developer token + OAuth
- **Note:** Chrome extension is desktop-only — not available on mobile.

---
*This SOP supersedes scattered notes. Companion files in this folder: Build Spec, Ad Deployment Plan, Checklist Test + Setup Notes, Tracker, Dashboard.*
