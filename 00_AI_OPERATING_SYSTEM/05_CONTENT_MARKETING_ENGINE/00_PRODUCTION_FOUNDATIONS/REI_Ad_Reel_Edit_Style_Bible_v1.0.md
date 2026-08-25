# REI Ad Reel — Edit Style Bible
Version: v1.0
Status: CANDIDATE (Edmund to approve; motion-frame verification pass pending — see §9)
Date: 2026-08-25
Supersedes: none (first consolidation of editing/presentation rules for paid ad reels)
Sources: 10 approved static finals read at pixel level (`01_ASSET_LIBRARY/.../08_LL_CONTENT_SERIES_16_REVIEW/03_STATIC_CREATIVES_REVIEW`, 2026-06-27 vintage); `REI_VSL_Video_Style_Rules_RESCUED.md` (Edmund's locked v5-review rules, Jun 2026); `REI_VSL_Pipeline_Recurring_Bugs_RESCUED.md`; SharpCut Studio `captionLayout.ts` (12-preset caption engine, live code); Serra `LOOK_TEST/README.md` (S5 grade + compositing chain, 2026-08-24); Amberwood `00_INDEX.md` VA1 dynamic-layer vocabulary; `REI_Video_Production_Foundation_v1.3.md` Format 1; LL post-launch hook/body export library structure; Meta ad account finals inventory (titles/durations, 3 accounts, 2026-08-25).

**What this file is:** the presentation/editing DNA for paid ad reels — look, type, color, captions, motion, pacing, and the variation engine that keeps every ad visually distinct. It deliberately contains **no script rules** (that's `LAYER_3A` + campaign angle masters). `/rei-ads-routine` executes this file.

---

## 1. The two palette families — pick ONE per ad, never mix

| Family | Base | Accent | Text | Where seen |
|---|---|---|---|---|
| **A — Campaign Luxe Dark** | Deep ink navy / near-black (#111C2E–#0D0D10) | Gold/brass (#B8894A–#C9A45C) | Warm off-white (#F4F1EA) | LL statics: One Property Trap, $1.5M Guess, Showflat, Value Up |
| **A-light — Campaign Luxe Light** | Ivory/cream (#F4F1EA) | Same gold | Near-black | "5 Showflats" static; CTA band on Paper Profit |
| **B — REI Core** | White/neutral footage | Brand blue **#005CE6** + yellow accent | White | VSL locked rules; caption system; punchline backing shapes |

Rules observed in the finals:
- Family A owns the **Legacy Launch / new-launch campaign world** (luxury, 3D metaphor renders, serif). Family B owns **REI core direct-response** (face-cam, karaoke captions, punch graphics).
- The light variant is the same system inverted — used to break feed fatigue *within* Family A without leaving the brand.
- Never gold + brand-blue in one asset.

## 2. Typography system (as shipped in the finals)

- **Editorial mode:** high-contrast serif (Playfair-class). Headline stacked 2–4 short lines. **Two-tone line pattern:** first line white/black, key line gold ("The One / **Property Trap**"; "Your Condo Went Up. / **Now What?**").
- **Punch mode:** ultra-heavy condensed sans (Archivo Black / Impact class), ALL CAPS, tight leading ("A $1.5M / GUESS IS / NOT A STRATEGY"). Single accent **word** colored, not a whole line ("Is **Not**", "You're **guessing**", "the **framework**").
- Body/support: clean grotesque (Inter/Poppins class), 70% opacity for secondary lines.
- Letterspaced caps for wordmarks/eyebrows ("LEGACY LAUNCH", "THE SHOWFLAT LOOP — SEE IT. LIKE IT. BUY IT. REGRET IT LATER.").
- **Accent-word rule:** every headline carries exactly one semantically loaded colored word — the belief pivot. This is a house signature; keep it in video punchlines too.

## 3. Composition & scene vocabulary

- **Literal metaphor renders** (the house signature): condo tower in a gold cage; condo in a glass display case; signpost with option arms (HOLD / EXIT / BUY AGAIN / DECOUPLE); crossroads floor graphic; gold arrow through skyline; five-way road split labeled with strategy options.
- **Cast:** contemplative Asian couple (thinking pose, backs/profiles), premium interiors: showflat model table, floor plans, advisory desk, window over MBS skyline. Never smiling-stock, never handshakes, never coins/keys clichés (explicitly banned in the carousel design system).
- **Layouts in rotation:** text-column-left + full-bleed scene right · diagonal split panel · half-split VS frame (lit success side vs stormy stuck side) · panel infographic (light card with 3-icon columns over scene) · full-bleed with lower text band.
- **CTA chip styles (rotate):** gold-outline pill · solid black chip with gold text · solid gold chip with black text. Always icon + verb-first label ("Find Your Next Safe Move ›", "Run The Filter", "Map Before You Buy →", "Bring Your Shortlist"). Never "Learn More".
- Footer lockup: LL or SRE monogram + campaign name + "Exit-First Property Strategy" tagline bar.

## 4. Motion rules — LOCKED by Edmund's v5 review (do not regress)

1. **3-second rotation rule:** the visual layer changes every ~3s cycling face-cam → motion graphic → B-roll, full video. Audio stays continuous face-cam. Cut boundaries snap to word gaps.
2. **Transitions:** white-flash + zoom-punch mix; zoom punch lands on emphasis/punchline cuts. (Long-form adds fade/wipe/slide rotation per scene — usable in ads as the "rotate, never repeat consecutively" rule.)
3. **Punchline overlays:** NEVER cover the face. Bottom of frame, above caption zone. Must look designed — backing shape, palette-family colors, animated in. Plain drawtext is rejected on sight.
4. **Lower thirds:** slide-in / layered reveal / branded panel only. Flat boxes rejected.
5. **B-roll:** ~50/50 stock vs pipeline-rendered motion graphics of B-roll time. Pure stock reads cheap.
6. **Caption system (locked):** yellow karaoke highlight, Impact, ALL CAPS (88px at 1080-wide reference), music bed at 4% volume.
7. **Grade:** clean + bright commercial — real black/white points, warm skin, light S-curve, micro-sharpen (Serra "S5" chain). No heavy stylized LUTs.
8. Amberwood dynamic-layer vocabulary (reusable accents): fullscreen navy question interstitials · navy data cards · info cards with real imagery · money rain · speed-line shout · animated captions · gold treatment reserved for prices/numbers.
9. **Backdrop compositing (optional look):** real room with S5 grade is the safe default; studio composite (wood-slat desk / slat-cove / lounge) allowed only with the full integration chain — eroded-then-hardened matte (gamma 1.25, no halo), wall + contact shadow, motivated rim light, light wrap sampled from plate, matched grain, depth-graded defocus.

## 5. Caption preset bank (SharpCut engine — machine-exact)

12 presets exist in the production tool; the ones fit for paid ads, mapped to genre:

| Preset | Character | Use in |
|---|---|---|
| `karaoke` (Montserrat, accent-word lights up) | The locked REI default | Face-cam hooks/bodies (Family B) |
| `wordPop` (Archivo Black, 1–2 words at a time) | Maximum aggression | Cold-open hooks, cutdowns |
| `impactPop` / `reelsPunch` (heavy/condensed pop-in) | Punch mode | UGC-selfie genre |
| `brandBanner` (left-aligned banner, accent edge) | Branded, compact | Data/proof moments |
| `highlightBar` (Oswald, bar sweeps active word) | Kinetic without shouting | Narrative genre |
| `minimalEditorial` (Playfair serif, letterspaced) | Documentary luxe | Family A editorial ads |
| `lowerThird` (broadcast panel) | Speaker ID, proof captions | Any |
| `bounceBox` / `clean` / `creatorOutline` | Softer social textures | Retargeting/warm only |

Caption geometry (from the engine): anchor top 13% / center 50% / bottom 83% of frame height; 6% horizontal safe margins; fewer words per cue as size grows (single-line rule); **money/number tokens never split across cues** (long-form locked rule, applies to ads).

## 6. Hook anatomy (0–3s) — what the finals do

- Cold open on the strongest visual contradiction available (metaphor render or mid-action scene), NOT a logo. Wordmark appears as a small eyebrow, never first.
- On-screen hook text = the thesis compressed to 2–6 words with the accent word colored, placed per §4.3.
- Hook cut density runs higher than body density; first caption cue lands ≤0.5s.
- Hook and body are separate assets (hook-swap system): 1 body × N hooks = N ads. Edit accordingly: hooks are cut to be detachable, ending on a cut boundary that any body can pick up from.
- Export set per ad: master + 1:1 + 4:5 + 9:16 crops (the account inventory shows every winner shipped as a crop family, plus 15s trims cut from the strongest 15s of the master).

## 7. QC gate — run before any ad ships (from the recurring-bugs memory)

1. No mid-word audio cuts: every cut boundary ≥80ms clear of transcript word end-times.
2. End card present: final duration = body + 3s logo card, logo visually confirmed.
3. Captions inside safe zones at ALL exported aspect ratios (re-check after each crop).
4. Punchline overlays never intersect the face bounding box at any point.
5. 3-second rotation verified across the full timeline (no static stretch >4s).
6. Number tokens unsplit; prices in gold (Family A) or yellow (Family B).
7. Music at 4%; original/licensed beds only — nothing Content-ID-claimable.
8. Grade check: skin natural, blacks not lifted, no LUT haze.

## 8. THE VARIATION ENGINE — "no two ads present the same"

Locks (never vary): §4 motion rules, §7 QC, one palette family per ad, one engine per ad (Client Advisory vs Agent Edition — never blend), accent-word rule.

Axes (vary these):

| Axis | Options |
|---|---|
| 1. Genre container | Studio hook-to-camera · UGC selfie · Narrative scenario (Dad-Daughter / Birthday Reveal class) · Split-screen VS · Infographic-led panel · Metaphor-render-led |
| 2. Palette family | A dark · A light · B (campaign decides which family; light/dark rotates within A) |
| 3. Headline type mode | Editorial serif · Punch condensed |
| 4. Caption preset | Per §5 genre mapping — rotate within the allowed set |
| 5. Backdrop/look | Real room S5 · wood-slat studio · slat-cove · lounge · location footage |
| 6. Motion-graphic accent set | Pick 2–3: data card, question interstitial, signpost, money rain, speed-line, chart/arrow, floor-plan zoom |
| 7. Transition flavor | White-flash-led · zoom-punch-led · slide/wipe-led (rotation seed) |
| 8. CTA chip style | The three chip styles + icon rotation |

**Anti-repetition rule:** every ad logs its 8-axis combo in the campaign's Variation Register (a table in the campaign `00_INDEX.md` or a sibling file). A new ad must differ from the previous ad in that campaign on **at least 3 axes**, and no combo may repeat within a campaign. Two ads in the same ad set never share axis 1 + axis 4 simultaneously.

## 9. Open items

- **Motion-frame verification — must run on DESKTOP.** Cloud capture was attempted 2026-08-25 and is confirmed impossible: Drive video finals exceed the connector's 10MB download cap, and the org egress policy 403-blocks every Facebook host in **all** cloud environments (verified in both), so the published Meta finals are unreachable too. The desktop machine sees the newest June-2026 finals directly on `H:\`. One-command recipe per video (needs ffmpeg):
  `ffmpeg -i IN.mp4 -vf "select='gt(scene,0.24)',metadata=print" -an -f null - 2>&1 | findstr pts_time > IN_cuts.txt` (cut timestamps) and
  `ffmpeg -i IN.mp4 -vf "fps=1/3,scale=640:-2" -q:v 2 frames_%03d.jpg` plus full-res frames at t=0/1/2/3/5s (hook anatomy).
  Priority set: 3–4 LL post-launch hooks + `Body1`/`Body6` + FL `Selfie Ads` + `The Birthday Reveal` + 2 verticals from `CONTENT_SERIES_16`. Drop outputs into the owning campaign folder; then verify §4/§6 against measured cuts-per-second and promote this file to v1.1.
- Palette hexes for Family A sampled visually from finals; confirm against the brand pack if a formal palette file exists.
