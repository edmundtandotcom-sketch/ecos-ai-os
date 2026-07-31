# 10 — CONTENT ENGINE SOP
**Phase owner:** Sonnet agent · **Companion file:** `Content_Calendar_12_Months.csv` · **Status:** DRAFT for orchestrator QA pass (built on LOCKED decisions in `_MASTER_CONTEXT_BRIEF.md`)

## Executive Summary

This SOP turns one weekly long-form YouTube video into twelve downstream assets (article, shorts, carousel, FB, LinkedIn, GBP, email, funnel follow-up, sales objection asset, FAQ addition, case study reference) using tools the business already has — GHL Social Planner, Descript/CapCut, Canva, Google Drive — none of them yet configured for this purpose. The realistic team is Edmund Tan and Cindior Ho on camera plus one assistant on execution; the weekly hour budget below is roughly 11.5 assistant-hours and 3.5 combined founder-hours, which is achievable without hiring. Two structural gaps must close before Week 1 can run as designed: no social accounts are connected in GHL (Phase 07 dependency) and no blog exists on `thereimethod.com` (Phase 04/11 dependency) — both are called out as hard blockers, not assumptions. A separate, lower-cadence workstream mines the 600+ existing YouTube back-catalogue (re-cut, not re-uploaded, with freshly written companion articles) and a bridge rule lets the 33 existing "New Launch Ladder™" reel scripts fill early social-calendar weeks as-is, per the Master Brief's no-big-bang-rename ruling (D5). The companion CSV lays out 52 weekly rows (13 Jul 2026 – 5 Jul 2027) mapped to the 6 content pillars and Singapore seasonal moments (CNY, National Day, BTO windows, cooling-measure anniversaries), all title/slug/copy fields screened against the banned-word list and the "lead with the climb, not 'safe'" hook rule. Every dollar figure, stat, and case-study name in the calendar is a placeholder sourced from existing reel/funnel copy and is flagged `[VERIFY]` pending Phase 09 Proof Library sign-off — nothing here should publish unverified.

---

## 1. Reality Constraints This SOP Is Built Around

- **Team:** 2 founders (Edmund Tan, Cindior Ho) + presumably 1 assistant. No videographer, no dedicated editor, no copywriter on staff assumed.
- **Existing assets:** 600+ YouTube videos on `youtube.com/@singaporerealestateinsider` (repurposing goldmine, largely untagged to the new pillar structure); 33 drafted reel scripts built on "New Launch Ladder™" vocabulary (not SPL vocabulary — do not rename per D5).
- **Tech available but unused:** GHL Social Planner (zero social accounts connected as of this brief); GHL Blogging module (no blog configured on any domain); GHL email/newsletter tool.
- **Authority domain for all new publishing:** `thereimethod.com` (D2). Campaign vanity domains (`secondpropertyladder.com`, `legacylaunch.com.sg`) stay funnel-only, noindexed, per D3.
- **Vocabulary discipline:** all new content uses The Second Property Ladder™ / Exit Before Entry™ vocabulary from day 1 (D5). The 33 reels and Legacy Launch V2 funnel keep New Launch Ladder™ vocabulary until the scheduled full rename pass (Phase 13/14) — this SOP does not touch that copy, it only bridges to it.

## 2. The Atomisation Chain — One Weekly Pillar Asset → 12 Downstream Assets

Worked against a single example thread: **Week 1 pillar video — "Position Map: How to Get Your Real Numbers Before You Plan a Second Property Move."**

| # | Asset | Trigger / When | Owner | Tool | Time Budget | Drive Subfolder | QA Gate |
|---|---|---|---|---|---|---|---|
| 1 | Long-form pillar video (source asset) | Shoot Mon → rough cut Tue → publish Wed | Edmund/Cindior (on camera) + Assistant (camera, audio, edit) | Camera/mic rig; Descript for rough cut | 2.5 hrs shoot + 2.5 hrs edit | `00_RAW_FOOTAGE/`, `02_EDIT_PROJECT/`, `03_EXPORTS/` | Founder approves final cut for vocabulary, claims, CEA line before publish |
| 2 | Website guide article (AEO answer-first) | Drafted Tue PM from transcript; published Wed | Assistant drafts; founder approves | Descript transcript export → Google Doc → CMS (thereimethod.com blog) | 1.5 hrs draft + 0.75 hrs founder review | `04_ARTICLE/` | Full Content QA Checklist (Section 9) — **article is not a transcript** |
| 3 | 2–3 Shorts | Cut Wed PM from long-form + extra hook takes shot Monday | Assistant | CapCut | 2.0 hrs | `03_EXPORTS/shorts/` | Caption-burn accuracy; hook leads with climb/missed window, never "safe"/"truth" |
| 4 | IG carousel | Built Thu PM from article's answer-first block | Assistant | Canva (brand template: navy/ivory/gold, Fraunces/Playfair headline + Inter body) | 1.0 hr | `05_SOCIAL_COPY/carousel/` | Banned-word scan; vocabulary check |
| 5 | FB post | Drafted alongside carousel, Thu | Assistant | GHL Social Planner composer | 0.25 hr | `05_SOCIAL_COPY/` | Banned-word scan |
| 6 | LinkedIn post (founder voice) | Assistant drafts skeleton Thu AM; founder rewrites first-person | Edmund or Cindior | GHL Social Planner or native LinkedIn | 0.3 hr founder | `05_SOCIAL_COPY/` | Must read as the founder's own words, not marketing copy — reject if it sounds ghostwritten |
| 7 | GBP post | Drafted Fri AM | Assistant | GHL Social Planner (if GBP supported) or native GBP dashboard | 0.3 hr | `05_SOCIAL_COPY/` | Local-intent relevance; CTA present; matches Phase 08 GBP plan |
| 8 | Email newsletter | Drafted Fri AM, sent Fri | Assistant drafts; founder approves | GHL email builder | 0.5 hr + 0.2 hr approval | `05_SOCIAL_COPY/email/` | PDPA footer + unsubscribe present |
| 9 | Funnel follow-up asset | Added Fri into the *existing* nurture sequence (not a new funnel) | Assistant | GHL workflow builder | 0.3 hr | `05_SOCIAL_COPY/funnel-tiein/` | Confirm correct funnel: Position Map universal CTA vs. Legacy Launch V2 for new-launch weeks |
| 10 | Sales objection asset | Extracted Fri from the article's core objection-and-answer | Assistant drafts; founder finalises | Google Doc (internal, not published) | 0.3 hr | `06_QA_SIGNOFF/sales-enablement/` | Founder sign-off only — for use live in Position Map sessions |
| 11 | FAQ page addition | Merged Fri once the article's FAQ block passes QA | Assistant | CMS FAQ page module | 0.3 hr | `04_ARTICLE/faq-merge/` | No duplicate FAQPage schema on two URLs; canonical checked |
| 12 | Case study reference | Added Fri only if that week's `case_study_ref` is populated | Assistant | CMS link/card component | 0.2 hr | `04_ARTICLE/` | Must match a verified entry in the Phase 09 Proof Library Inventory — never an invented name or figure |

**Total weekly time:** ~11.5 assistant-hours + ~3.5 combined founder-hours (shoot + review + LinkedIn voice pass + GBP/newsletter approval). See Section 5 for the day-by-day layout.

## 3. Transcription → Article Workflow (thin-content rule)

1. Descript auto-transcribes the long-form video (Tuesday morning, ~15 min machine time).
2. Assistant reads the raw transcript once and extracts: (a) the single question the video actually answers, (b) 3–4 sub-questions it touches, (c) any numbers/claims mentioned (each gets a `[VERIFY]` flag until confirmed).
3. Assistant drafts the article using the **Video-to-Article Template** (Section 7) — this is a fresh, restructured, answer-first piece of writing, not a cleaned-up transcript. Concretely: no verbal filler ("so", "right", "you know"), no timestamp-order narrative, no second-person "as I said in the video," a direct 40–60-word answer under the H2 before any supporting narrative appears.
4. **Rule: if a paragraph in the draft could be produced by deleting filler words from the transcript alone, rewrite it.** This is the thin-content gate — Google's people-first content guidance treats auto-generated-from-transcript pages as a quality risk, and duplicate video/article content earns no separate citation value for AEO.
5. Founder review (Wednesday) checks vocabulary, claims, and that the piece reads as genuinely written, not transcribed.
6. Publish with full schema block (Section 7).

## 4. Back-Catalogue Mining Workstream (600+ existing videos)

This is a **separate, lower-cadence workstream** layered onto the weekly new-production cadence above — it does not replace Monday's shoot day.

1. **Pull analytics.** Export YouTube Studio data (views, average view duration, watch time, traffic source) for the full channel. `[VERIFY — requires YouTube Studio access; not available to this SOP author]`.
2. **Shortlist.** Rank by (top 20% by watch time) × (relevance to the 6 pillars, especially Founder Proof and The 5 Steps, since old videos are most likely to already contain founder-journey and process material). Target: a running shortlist of 20–30 candidate videos.
3. **Vocabulary screen.** Old videos almost certainly use pre-repositioning language ("New Launch Ladder", "agent", "unit", "good buy"). **Do not republish or re-upload raw.** Every back-catalogue asset gets re-cut and re-captioned before it touches a channel under the new vocabulary.
4. **Re-cut.** Pull the single best 60–90 second segment; cut a new Short with a new hook and new caption in SPL vocabulary. Treat it exactly like a Step 3 short in the weekly chain (Section 2, row 3) — same QA gate.
5. **Companion article.** Write a fresh guide article inspired by the old video's topic (not a transcript of it), embedding the old video as supporting media, dated with today's `datePublished`. This is new AEO-eligible content, not a repost.
6. **Cadence.** Realistic pace for a lean team: **one back-catalogue mining asset every 2 weeks**, run in whichever week has slack (do not let it displace the primary weekly pillar asset). Week 51 in the calendar is built as a visible showcase of this workstream ("What 600+ Videos Taught Us"). If bandwidth allows, a freelance editor engaged specifically for back-catalogue re-cuts (outside the core weekly loop) would let this run weekly instead of bi-weekly — flagged as a Month 2–3 hiring decision, not a Week 1 requirement.

## 5. The 33 Reel Scripts — Bridge Rule (do not rename, do use)

Per Master Brief D5, the 33 existing reels use "New Launch Ladder™" and the Legacy Launch brand — **they are not renamed to SPL vocabulary now.** They remain a live, separate content stream tied to the Legacy Launch V2 funnel. Two ways this SOP touches them without violating that ruling:

1. **Fallback filler, not primary content.** In the first 4–6 weeks of this engine (while the new SPL-vocabulary shorts library is still thin), the assistant may schedule an existing reel script as-is into the IG/FB/YouTube Shorts calendar on a week that has no back-catalogue or weekly-pillar short ready, tagged internally "Legacy Launch stream — NLL vocabulary, do not edit for SPL terms." This is explicitly called out in the CSV `notes` column wherever it applies (see Week 12/W12).
2. **Funnel bridge tie-in.** Any calendar week whose theme is new-launch-specific (buyer mistakes / exit-before-entry applied to launches) sets `funnel_tiein` to **Legacy Launch V2** rather than the Position Map universal CTA, since that funnel already exists and is the correct destination for that audience segment.
3. **Do not** insert "Second Property Ladder™" or "Exit Before Entry™" trademark language into the 33 reels' existing scripts before the scheduled full rename pass (Phase 13/14 owns that).

## 6. Weekly Operating Calendar

| Day | Block | Activity | Owner | Hours |
|---|---|---|---|---|
| Mon AM | Shoot | Film long-form pillar video; batch 2–3 extra hook takes for shorts in the same session | Edmund/Cindior on camera, Assistant on camera/audio | 2.0 hrs founders + 0.5 hrs assistant |
| Mon PM | Ingest | Upload raw footage to Drive, log clip, back up | Assistant | 0.5 hrs |
| Tue AM | Transcribe + rough cut | Auto-transcribe (Descript); rough cut long-form edit | Assistant | 2.5 hrs |
| Tue PM | Article draft | Draft companion article from transcript, Video-to-Article Template — not a transcript | Assistant | 1.5 hrs |
| Wed AM | Founder QA | Review/approve video cut + article draft: vocabulary, claims, CEA line | Edmund (lead) | 0.75 hrs |
| Wed AM | Publish | Publish long-form to YouTube; publish article to thereimethod.com with FAQ schema, author box, dateModified | Assistant | 1.0 hr |
| Wed PM | Shorts cut | Cut 2–3 vertical shorts + hook variants; burn captions | Assistant (CapCut) | 2.0 hrs |
| Thu AM | Schedule | Load shorts, carousel, FB/LinkedIn posts into GHL Social Planner for Thu–Mon | Assistant | 1.0 hr |
| Thu AM | Founder voice pass | Rewrite LinkedIn post skeleton into first-person founder voice | Edmund or Cindior | 0.3 hrs |
| Thu PM | Carousel build | Build IG carousel from article's answer-first block | Assistant (Canva) | 1.0 hr |
| Fri AM | GBP + newsletter | Publish GBP post; finalise and send email newsletter | Assistant drafts, founder approves | 1.0 hr assistant + 0.3 hrs founder |
| Fri PM | QA + file | Run Content QA Checklist; file all assets to Drive; log completion in calendar tracker | Assistant | 1.0 hr |

**Weekly totals: ~11.5 assistant-hours, ~3.35 combined founder-hours.** No day requires more than 2.5 assistant-hours or more than 2 founder-hours — deliberately sized to survive a busy sales week.

## 7. Monthly Content Themes (12 months, 6 pillars + Singapore seasonal moments)

Calendar year used below: 13 Jul 2026 (Week 1) → 5 Jul 2027 (Week 52), matching the CSV. `[VERIFY]` flags on every date-dependent claim — HDB BTO launch windows and any cooling-measure changes must be checked against current HDB InfoWEB / MAS-MND circulars before the tied GBP post publishes, since this SOP was written from July 2026 and cannot see mid-2026–2027 policy changes.

| Month | Seasonal SG moment | Primary pillar | Secondary pillar | Notes |
|---|---|---|---|---|
| Jul 2026 | Content engine launch (no major property-calendar event) | The 5 Steps | Founder Proof | Introduce SPL vocabulary fresh across every channel from Week 1 |
| Aug 2026 | National Day (9 Aug) — family/legacy framing | Founder Proof | Case Studies | Lean into "Family Options" language around National Day |
| Sep 2026 | Cooling-measure anniversary (Sep 2022 tightening round) `[VERIFY current status]` | Exit Before Entry | The One-Property Trap | Annual "Policy Clock" explainer refresh |
| Oct 2026 | Q4 new-launch season `[VERIFY 2026 launch calendar]` | Buyer Mistakes | Exit Before Entry | Bridges to Legacy Launch V2 reels for launch-specific weeks |
| Nov 2026 | BTO Nov launch window `[VERIFY]`; year-end planning opens | The 5 Steps | Case Studies | Opens the annual Climb Cadence review arc |
| Dec 2026 | Year-end NAV review / "New Year, Next Move" planning | Founder Proof | The One-Property Trap | Highest-scrutiny week: founder's own NAV figures — verify before publish |
| Jan 2027 | CNY prep (CNY 2027 date `[VERIFY exact date]`); family conversations about property | The One-Property Trap | Buyer Mistakes | Warm, family-forward tone; CNY table-talk content |
| Feb 2027 | CNY week; BTO Feb launch `[VERIFY]` | Case Studies | Founder Proof | Family-centred case studies; Cindior Ho on-camera week (D6 open item) |
| Mar 2027 | Q1 new-launch season | Exit Before Entry | Buyer Mistakes | Selection Research / exit-math focus for launch buyers |
| Apr 2027 | Cooling-measure anniversary (Apr 2023 ABSD hike) `[VERIFY current rates]` | The One-Property Trap | Exit Before Entry | Annual ABSD/LTV explainer refresh |
| May 2027 | BTO May launch `[VERIFY]`; mid-year checkpoint | The 5 Steps | Case Studies | Possible "Which Step Are You On?" diagnostic promotion, if built by then |
| Jun 2027 | Mid-year Climb Cadence review; school holidays (family decision season) | Founder Proof | The One-Property Trap | Closes the year; Week 52 doubles as engine-anniversary review |

## 8. Video-to-Article Template

```
TITLE: [Specific Singapore search/AEO angle — question or comparison form]
URL SLUG: /guides|mistakes|compare|case-studies|proof/[slug]
  (slug taxonomy proposed here — reconcile against Phase 05 AEO Topic Clusters before final publish)
META DESCRIPTION: [140–155 characters, no banned words]
H1: [same as title, adjusted for readability]
BYLINE: [Edmund Tan | Cindior Ho] · Published [date] · Updated [dateModified]

[AEO ANSWER-FIRST BLOCK — required, appears before any other body content]
H2: [The exact question this article answers, phrased as a real search query]
[Direct-answer paragraph, 40–60 words. Plain language. Must be a complete,
citable answer on its own — this is the paragraph an AI Overview or featured
snippet would lift. No hedging, no banned words.]

[BODY — 2–4 sections]
H2: [Sub-question or expansion #1]
[2–4 paragraphs; Singapore-specific detail — HDB/EC/private, ABSD/MOP/SSD/
CPF/TDSR/IPA as relevant; any figure not yet confirmed carries [VERIFY].]
H2: [Sub-question or expansion #2]
H2: [Sub-question or expansion #3 — tie to a Step/artefact of the 5 Steps if relevant]

[CASE STUDY CALLOUT — only if this week's case_study_ref is populated]
[Short named reference, [VERIFY], links to the full case study page.]

[FAQ BLOCK — required, 3–5 pairs, marked up as FAQPage schema]
Q: [question]
A: [40–60 word direct answer]
(repeat)

[INTERNAL LINKS — required, minimum 3]
- The Second Property Ladder™ category hub
- One other pillar article
- The relevant offer page (Position Map session, or Legacy Launch V2 for
  new-launch-themed pieces) with compliant CTA copy

[COMPLIANCE BLOCK — required, footer]
[CEA registered name] · CEA Reg No. [VERIFY] · PropNex Licence No. [VERIFY]
"Advisory-first. We plan the sequence before any transaction."
[PDPA line if any form is embedded on this page]

[AUTHOR BOX — required]
Photo · Name (Edmund Tan or Cindior Ho) · CEA Reg No. [VERIFY] ·
2–3 line bio anchored to "We built it before we advised it" ·
link to founder profile page

[SCHEMA — required, technical]
Article (headline, author, datePublished, dateModified, publisher = The REI Method)
FAQPage (only if the FAQ block above is genuinely visible on-page)
BreadcrumbList
```

## 9. Article-to-Social Template

```
SHORTS (2–3 per pillar asset) — CapCut, 30–60s, captions burned in
Hook (0–3s): [climb / missed-window / next-move angle — never "safe" or "truth"]
Payoff (3–30s): [one clear insight lifted from the article's answer block]
CTA (last 3s): [comment keyword, or "link in bio" → Position Map session]

IG CAROUSEL (6–8 slides) — Canva, brand template
Slide 1: Hook headline (question form)
Slide 2: Why it matters (the villain/problem framing)
Slides 3–6: The direct answer, broken into steps or numbers
Slide 7: Proof/case tie-in (if this week has one)
Slide 8: CTA — Position Map session, link in bio

FB POST
[Headline as question] + [2–3 sentence direct answer] + [link to article] + [CTA]
Slightly more conversational register than LinkedIn.

LINKEDIN POST (founder voice — first person, Edmund or Cindior)
[A real client moment or personal reflection tied to this week's theme]
→ [the lesson/insight] → [soft CTA: article link or Position Map session]
Must be rewritten by the founder, not posted as the assistant's draft verbatim.

GBP POST (≤1,500 characters, ~150–300 words)
[Local-intent framing, e.g. "Considering a second property move in Singapore?"]
+ [short direct answer] + [CTA button: Book / Learn more]

EMAIL NEWSLETTER
Subject: [from calendar] · Preheader: [complementary, not duplicate, of subject]
Body: 150–250 words summarising the article's answer · 1 CTA
Footer: PDPA line + unsubscribe

FUNNEL FOLLOW-UP ASSET
1–2 line nurture email/SMS added to the *existing* sequence, tying this week's
theme to the correct destination: Position Map session (default) or
Legacy Launch V2 (new-launch-themed weeks).

SALES OBJECTION ASSET (internal, not published)
1-page founder script or one-pager addressing the objection this week's article
answers — for live use in Position Map sessions.

FAQ PAGE ADDITION
Merge this week's FAQ block into the site-wide FAQ page once it has passed QA.
Dependency: FAQ page must exist (Phase 04 sitemap).

CASE STUDY REFERENCE
Only add if `case_study_ref` is populated for the week, and only if that name/
figure set already exists, verified, in the Phase 09 Proof Library Inventory.
```

## 10. Content QA Checklist (run every Friday, before anything ships)

- [ ] Banned-word scan clear: Homeowner, agent (except the locked "38,000 agents" market-size line and the "Agent-Led Transaction Thinking" villain name — never used to describe Edmund/Cindior), advice, consultation, project (except inside "a good project in the wrong sequence"), unit, good buy, investment property, asset progression.
- [ ] "Next Move" appears only as the CTA verb or inside a locked proof-category name (e.g. "The Exit That Unlocked the Next Move") — not as generic filler text.
- [ ] Hook rule respected: any cold/top-of-funnel hook leads with the climb, the next move, or the missed window — never with "safe" or "truth."
- [ ] Every $ figure and stat carries `[VERIFY]` until confirmed against records and signed off by name/date (Phase 09 Proof Library), or has already been confirmed with the flag removed and the sign-off logged.
- [ ] CEA registered name + CEA reg. no. + PropNex licence line present in the compliance block (or explicit `[VERIFY — pending]` placeholder if numbers haven't been supplied yet).
- [ ] PDPA consent line present on any form or CTA that captures contact details.
- [ ] Byline is Edmund Tan or Cindior Ho — never "Singapore Real Estate Insider" as author (that is the media-brand name only, D1).
- [ ] Publisher schema field = The REI Method.
- [ ] Article is not a transcript: rewritten, restructured, answer-first, no timestamps or verbal filler carried over from the raw video.
- [ ] AEO answer-first block present: question-as-H2 followed immediately by a 40–60-word direct answer.
- [ ] FAQPage schema applied only to Q&A pairs genuinely visible on the page.
- [ ] Author box present with CEA reg. no. and short bio.
- [ ] `dateModified` updated whenever a published article is edited.
- [ ] Minimum 3 internal links present (category hub + 1 pillar article + 1 offer page).
- [ ] Any `case_study_ref` matches a verified entry in the Phase 09 Proof Library Inventory — no invented names or figures.
- [ ] Compliance disclaimer present (illustrative figures, no guarantee, risk disclosure — matching the existing Legacy Launch V2 disclaimer language).
- [ ] Entity consistency: no cross-linking into Changi Green; Legacy Launch–tagged assets carry the light-touch bridge line positioning New Launch Ladder™ under The Second Property Ladder™, per D5 — not a full rename.
- [ ] GHL Social Planner schedule matches the calendar row: correct week, correct channel, correct link/UTM.

## 11. Drive Folder Convention (proposed)

No existing content-production Drive root was visible to this SOP; the convention below is proposed to mirror the numbered-folder discipline already used in `AEO_REPOSITIONING_OS/` itself. **`[PROPOSED — reconcile with the actual content Drive root if one already exists outside this shared drive before Week 1.]`**

```
03_CONTENT_ENGINE/
  YYYY/
    MM_MonthName/
      W##_YYYY-MM-DD_<pillar-code>_<slug>/
        00_RAW_FOOTAGE/
        01_TRANSCRIPT/
        02_EDIT_PROJECT/        (CapCut/Descript project files)
        03_EXPORTS/             (long-form final, shorts x2-3, captions)
          shorts/
        04_ARTICLE/             (draft doc + final HTML/schema)
          faq-merge/
        05_SOCIAL_COPY/         (carousel, FB/LinkedIn/GBP/email copy)
          carousel/
          email/
          funnel-tiein/
        06_QA_SIGNOFF/          (completed checklist, approver, date)
          sales-enablement/
```

Pillar codes for folder naming: `A` One-Property Trap · `B` Exit Before Entry · `C` The 5 Steps · `D` Founder Proof · `E` Buyer Mistakes · `F` Case Studies.

## 12. Tools Stack Summary

| Tool | Use in this SOP | Status |
|---|---|---|
| GHL Social Planner | Schedule FB/IG/LinkedIn/GBP posts | Enabled, **zero accounts connected** — Phase 07 dependency |
| Descript | Transcription + rough cut of long-form video | Assumed available, needs assistant onboarding |
| CapCut | Shorts cutdowns + caption burn-in | Assumed available |
| Canva | IG carousel, GBP graphics (brand template) | Assumed available |
| Google Drive | Asset storage per Section 11 | Available (this project lives on a shared drive already) |
| thereimethod.com CMS/blog | Article publishing, schema | **Not configured** — Phase 04/11 dependency |
| GHL email builder | Newsletter send | Available in GHL, unused for this purpose yet |
| YouTube Studio | Analytics export for back-catalogue mining; long-form upload | Assumed available, access `[VERIFY]` |

## 13. Concerns

1. This entire weekly cadence assumes social accounts are connected in GHL Social Planner by kickoff. Report 2 in the Research Appendix confirms **zero connected social accounts** today. Steps 4–7 of the atomisation chain cannot run as designed until Phase 07 closes this gap — treat Week 1–2 as a manual-posting bridge if Phase 07 hasn't landed.
2. `thereimethod.com` has no blog configured (Research Appendix, Report 2). The Wednesday article-publish step is blocked until Phase 04/11 stands up the blog with Article/FAQPage/BreadcrumbList schema support. If the blog isn't live by kickoff, bank articles in Drive rather than skip them.
3. The "Which Step of The Second Property Ladder Are You On?" diagnostic (referenced at Week 45) is spec'd but not built, and requires GHL custom fields (`spl_*`) that don't exist yet. That week's `funnel_tiein` defaults to the Position Map session unless the diagnostic ships first.
4. Cindior Ho's on-camera comfort level is an open item (D6). Week 31 assumes she leads a piece in her own voice — if that's not yet true, substitute Edmund and treat D6 resolution as a precondition, not an assumption.
5. The time budget assumes the assistant can already operate Descript, CapCut, and GHL Social Planner. If not, Month 1 should run at reduced cadence (e.g., 1 short instead of 2–3 per week) while onboarding happens, rather than silently falling behind the calendar.
6. Every case-study name and dollar figure used as calendar-row content (Tre Ver, Parc Clematis, the founders' NAV figures, "38,000 agents," the 90% disqualification stat, and the case names Edward & Rose, MoK & Jine, Win/Esther & Family, Lynn) is a placeholder pulled from existing reel/funnel copy in the Research Appendix. None of it is cleared for use — every row that touches these must pass Phase 09 Proof Library sign-off before it ships.

---

## Questions To Clarify

1. Confirm the assistant's current skill level with Descript, CapCut, and GHL Social Planner — this determines whether Month 1's cadence in Section 6 is realistic or needs to start slower.
2. Confirm the go-live date for the blog on `thereimethod.com` (blocks the Wednesday article-publish step and every Week 1+ row in the CSV).
3. Confirm whether the "Which Step Are You On?" diagnostic will be live by approximately Week 45 (mid-May 2027) — if not, that week's `funnel_tiein` reverts permanently to the Position Map session.
4. Confirm Cindior Ho's willingness and readiness for on-camera, first-person content (affects Week 31 and any future Cindior-voice weeks).
5. Confirm which of the 600+ existing YouTube videos are highest-performing — requires YouTube Studio analytics access, which this SOP did not have.
6. Confirm the exact 2026–2027 HDB BTO launch calendar and any cooling-measure changes since this brief's July 2026 date, to correct the `[VERIFY]`-flagged seasonal posts (Weeks 9, 17, 32, 39, 43 in the CSV).

## Dependencies

- **Phase 07 (Social Profile Repositioning):** social accounts must be connected in GHL before the Thursday scheduling step can run through Social Planner rather than manually.
- **Phase 04 / 11 (Website Sitemap + Technical AEO/SEO):** blog must exist on `thereimethod.com` with Article/FAQPage/BreadcrumbList schema support before the Wednesday publish step and the FAQ-page-addition step can execute.
- **Phase 09 (Proof Library System):** every `case_study_ref` and founder-figure claim in the CSV must clear Proof Library verification before publishing — this SOP's QA checklist hard-blocks on that gate.
- **Phase 05 (AEO Topic Clusters):** the slug taxonomy proposed here (`/guides/`, `/mistakes/`, `/compare/`, `/case-studies/`, `/proof/`) should be reconciled against the final cluster map; rename before publish if there's a conflict.
- **Phase 08 (Google Business Profile Plan):** GBP posting cadence here assumes the profile is claimed and verified — confirm against the Phase 08 plan before Week 1's GBP post.
- **Diagnostic build (Phase 2 lead-gen, not yet built):** affects Week 45's `funnel_tiein` only.
- **CEA reg. numbers / PropNex licence numbers** (Master Brief, open Question 1): required in the compliance block of every article template before public publish.

## First 5 Actions

1. Confirm blog live status on `thereimethod.com` and get Article/FAQPage/BreadcrumbList schema support confirmed with the Phase 11 owner — this blocks Week 1's article publish.
2. Get the assistant access to Descript and CapCut, plus a 1-hour walkthrough of the Video-to-Article and Article-to-Social templates, before Week 1's Monday shoot.
3. Connect Facebook, Instagram, LinkedIn, and GBP into GHL Social Planner (Phase 07 dependency) so the Thursday scheduling step is not fully manual from Week 1.
4. Pull a YouTube Studio analytics export for the 600+ existing videos (views, watch time, traffic source) to seed the back-catalogue mining shortlist — needed ahead of Week 51's showcase and the ongoing bi-weekly mining cadence.
5. Run Week 1's Position Map article and video through the full Content QA Checklist as a live dry run with Edmund and Cindior present, to calibrate real time-per-step before locking the weekly hour budget permanently.
