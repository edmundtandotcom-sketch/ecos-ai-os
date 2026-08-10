# Competitive Pattern Report — 21 SG Property YouTube Videos
Date: 2026-08-10 · Method: metadata + transcripts (all 21), frame-study +
scene-detect cut analysis (7 representative). Study set curated by Edmund.

## 1. The headline finding
**In this niche, outlier performance is script-led, not edit-led.**
The biggest outlier (11× channel size) is visually near-static; the losers
include polished, graphics-heavy productions. Editing quality is table stakes;
hook psychology + packaging is the multiplier.

## 2. Outlier scoreboard (views ÷ channel subs)
| × | Channel | Video | Views | Cuts/min |
|---|---|---|---|---|
| 11.0 | Joy Shi Property | The HDB Boom Might Be Ending | 38,418 | **0.8** (single-take) |
| 8.7 | Shelby Lai | HDB DECLINING? Condo STUCK? Landed KING? | 6,805 | 5.6 |
| 4.8 | DF Property | 4 Reasons People Never Get Rich from SG Property | 11,657 | 7.9 |
| ~1 | Marcus Luah | UNBIASED Thoughts series | 2–13k | 5.7 |
| brand | CNA | wait-out rule explainer | 24.5k | 5.9 |
(Our HDB v14 long-form: visual change every ~3–4s ≈ 15–18/min — denser than
every winner studied.)

## 3. The winning hook anatomy (all 3 outliers, first 20s)
1. **Speak to the viewer's inner state first, news second.**
   "I know you're sitting on the fence… thinking maybe prices will drop" /
   "If you clicked this, you probably know someone who got rich from property."
2. **Contrarian information gap.** "Everyone talks about X — NOBODY talks
   about Y" / "secretly doing behind the scenes".
3. **Insider authority in one line.** "On the ground as a salesperson, I'm
   already seeing the impact."
4. **One hyper-specific curiosity number.** "6 years to recoup your reno cost."
5. **Personal stakes/threat.** "Before you regret later" / "could cost you
   hundreds of thousands."
6. **Roadmap with named curiosity gaps.** "We'll reveal WHO you're actually
   competing against."

### Title formulas that outperformed
- Tension question stack: "HDB DECLINING? Condo STUCK? Landed still KING?"
- Ending/threat frame: "The HDB Boom Might Be **Ending**"
- Negative-promise listicle: "4 Reasons People **Never** Get Rich…"
- (Underperformers used news-summary or generic-guide titles.)

## 4. Visual mechanics worth keeping vs adding
- Keep our density for REELS (short-form norms differ) and keep: cutout
  articles, data boards, subtitles, punch-ins — they match CNA/Luah polish.
- ADD Style Variant E "Outlier Minimal" for long-form A/B: clean set feel,
  punch-ins only, sparse graphics at data moments, script carries it.
- CNA pattern worth copying: b-roll ~40% of runtime but SLOW cuts (5.9/min),
  every graphic dwells long enough to read.

## 5. Actions taken
- Hook formulas + title formulas added to VIDEO_BRIEF_TEMPLATE (script section).
- Style Variant E added to the variant table for A/B testing.
- Next script (video #2): draft the hook in outlier anatomy, keep reels dense.
- Validation loop: publish → compare YouTube Studio retention curves →
  double down on whichever style wins OUR audience.

## 6. Channel-scan offer (standing)
Give any channel URL → full video list + baseline views → study only the
3–10× outliers. Sharper than hand-picked single videos.

---

## 7. VISUAL GRAMMAR CATALOG (full-duration frame study, added same day)

### Marcus Luah (review format — the richest display vocabulary)
| Format observed | What it is | Our equivalent |
|---|---|---|
| Map callout | Rounded map screenshot, animated RED circle + arrows, big outlined location labels, often TWO maps side-by-side (THE VALES vs WATERBAY) | NEW: MapCallout component |
| Sidebar reason panel | Dark rounded panel L/R ~40%: colored semantic title (RED "WHY PEOPLE WON'T BUY" / GREEN "3 REASONS PEOPLE WILL BUY"), numbered reasons, arrow bullets | UPGRADE: StatCard semantic variant |
| Price-table reveal | Spreadsheet screenshot top-half, RED cell highlight, gold caption banner below | NEW: TableReveal |
| Circle-zoom callout | Portal screenshot + magnifier bubble on a price + red arrow | NEW: CircleZoom |
| Project VS cards | Two rendering-image cards stacked with names | UPGRADE: DuoTags w/ images |
| Doodle emphasis | Hand-drawn ?? around head, sketch LIKE button | NEW: DoodleEmphasis (small) |
| Cross-promo thumbs | His other-video thumbnails inserted at related claims | LATER (needs our channel thumbs) |
| Chart w/ circled point | Colorful bar/line chart, one value circled + called out | UPGRADE: BarChart annotate mode |

### How to Singapore (faceless format)
- Stock-prop b-roll narration (miniature houses, hands, coins) between graphics
- White document-style COMPARISON TABLES (Feature | Premium | Standard tiers)
- Annotated data timelines (Year | number | context-note rows)
- Report-summary cards (bold-keyword bullets citing PropNex/EdgeProp/URA)
- Playful outlined caption font (their brand voice)
→ Adopt: CompareTable + AnnotatedTimeline components; faceless b-roll
  narration segments as an option inside Variant E.

### CNA (podcast format)
- Multi-angle switching carries pace; name lower-third once; minimal graphics.
→ Lesson: angle-switching (or punch-in alternation, our equivalent) can
  replace graphic density in interview/conversation formats.

### Build priority (next production or on request)
1. MapCallout  2. SidebarList semantic variant  3. TableReveal  4. CircleZoom
5. CompareTable  6. AnnotatedTimeline  7. DoodleEmphasis  8. VS image cards
All re-skinned to navy/gold brand; mechanics mirrored, identity ours.

---

## 8. DEEP MINE OF THE TOP CHANNEL-SWEEP OUTLIERS (2026-08-10, second pass)
Studied at last: the biggest performers, which the first pass never opened.

### The Right Move (94x / 98x) — "DATA-SHEET CAST" — the niche's #1 format
The entire 40-60 min video is a LIVE SPREADSHEET screencast:
- Full-screen Google-Sheets analysis (their own exit-strategy framework),
  scrolled and cell-highlighted live while he narrates.
- Talking head reduced to a SMALL ROUNDED PIP, bottom-left, over a branded
  teal grid backdrop; head returns full-frame only for commentary beats.
- Persistent lower caption bar on every shot (small, centered, dark plate).
- Animated channel-name badge (glowing brand tag) top-left.
- "Video Outline" icon-map card near the start (3 chapters w/ icons).
- Cross-promo grid card: 6 video thumbnails of his other reviews.
- Head-vs-sheet alternates every few seconds — that IS his pacing engine.
→ BUILD: **ScreenCastLayout** (full-doc + head PIP corner, doc scroll +
  cell highlight), **OutlineCard** (icon chapter map), **PromoGrid**
  (thumbnail wall), **BrandTag** (animated corner badge).

### The Real Collective (107x — highest in the sweep) — HOME TOUR grammar
- Persistent burned caption bar, EVERY shot, bottom-center.
- Location title card: big name ("BLOCK 274A") over a white 3D city render.
- Animated MAP: route line drawing between pins + big script-font label
  ("1-2 Mins Walk") — used as a transition between areas.
- Gimbal walk-and-talk, room-by-room, wide interior framing.
- Channel logo watermark top-right throughout.
→ BUILD: **TourCaptionBar**, **LocationTitleCard**, **RouteMap** (animated
  path + walk-time label), **RoomLabel**.

### Confirmed reusable for our format
- Sheet-cast pacing (head PIP ↔ full doc) is the strongest attention device
  for long data segments — better than our static boards for dense numbers.
- Outline card at the start = the "roadmap" hook step, visualised.
- Cross-promo thumbnail grid is a proven retention/loop device.

### v3 BUILD LIST (priority order)
1. ScreenCastLayout (+ doc scroll & cell highlight) — biggest single win
2. OutlineCard (icon chapter map)
3. RouteMap (animated path + time label)
4. LocationTitleCard
5. PromoGrid (cross-promo thumbnails)
6. TourCaptionBar + RoomLabel (needed only when tour series starts)
7. BrandTag (animated corner badge)
8. BarChart annotate-mode (circled point) — carried over from v2 spec
