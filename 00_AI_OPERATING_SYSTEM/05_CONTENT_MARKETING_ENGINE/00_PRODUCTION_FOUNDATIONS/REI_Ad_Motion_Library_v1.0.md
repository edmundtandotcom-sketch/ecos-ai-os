# REI Ad Motion Library — transitions, moves, type motion, and the anti-tell rules
Version: v1.0
Status: CANDIDATE (first use: Thomson Reserve × Daughter EDB, 2026-10-04)
Date: 2026-10-04
Sources: `E:\REMOTION\ADS_PLAYBOOK.md` norms as surfaced in `/rei-ad-build` (171 vertical ads measured); `render_ad_v4.py` (`motion()`, `build_shots()` zoom ladder and whip/punch/push assignment); `REI_Ad_Reel_Edit_Style_Bible_v1.0.md` §4; the professionally cut S&P reference edit (2026-08-26); the Thomson Reserve styleframes and motion previews rendered 2026-10-04.
Companion: Style Bible (look, type, colour) · ADS_PLAYBOOK (measured norms) · DEVICE_LIBRARY (graphic devices). This file owns **how things move and how shots join**.

**Why it exists.** Static ads died; "dynamic" ads made by a script now die for a different reason: they look assembled. The difference between the two is not the number of effects, it is whether each move is *motivated* by what is being said and whether anything repeats. This library gives every move a name, a trigger, a duration, and a budget, so a variation spec can call them by name and the QC gate can count them.

---

## 1. Camera moves — one on every shot, no exceptions

| Name | What | Trigger | Spec | Notes |
|---|---|---|---|---|
| `push` | slow zoom in | default narration shot | 1.00→1.05 over the shot, linear | the resting move; invisible, but a static frame reads dead |
| `pull` | slow zoom out | after a punch, or on a reveal ("a forever view") | 1.08→1.00 | pairs with a dip-to-white |
| `punch` | fast zoom in, eased | any number, price, %, "not", "never", a name | 1.00→1.13 in 8–10 frames, ease-out ⁴, then hold/push | the emphasis move; max 1 per 2s |
| `slam` | punch + rotation + darken | the single pivot word of the ad ("Not yet.", "Gone.") | 1.08→1.20, −3°/+3°, 40% darken on the plate | once or twice per ad, never in the hook *and* the CTA |
| `whip` | horizontal (or vertical) directional blur out → in | section change, every b-roll entry | 3 frames out, 3–4 frames in, blur 60→160 px, +8% brightness at the peak | always with a whoosh; never on consecutive shots |
| `drift` | sub-pixel pan | long device holds (bar growth, dot grid) | 6–10 px over 3s | keeps a hold alive without calling attention |
| `parallax` | background and foreground at different rates | render walk-throughs (interiors, aerials) | bg 1.00→1.04, fg layer 1.00→1.08 | needs a cut-out or a device layer; otherwise use `push` |
| `handheld` | 1–2 px micro-shake, 2–4 Hz, random phase | UGC-genre shots that have been stabilised too clean | amplitude ≤2 px, never on text | the imperfection that reads human |
| `ramp` | speed change | into a slam or a list run ("Gone. Gone.") | 1.0×→1.2× over 0.4s, or 0.6× slow-mo for a 0.8s beat | audio pitch-corrected; never on a number read |

**Zoom ladder.** Consecutive speaker shots never share a scale: 1.00 → 1.10 → 1.20 → 1.10 → 1.00 (standard) or 1.00 → 1.06 → 1.12 (tight selfie footage). The composer assigns these; a human cut should still obey it.

## 2. Cuts — how one shot ends and the next begins

| Name | Spec | Use |
|---|---|---|
| hard cut | 0 frames, on a consonant or a breath | 70% of all joins |
| jump cut | hard cut on the same framing, scale stepped by the ladder | UGC genre; removes dead air honestly |
| cut-on-action | cut on a hand gesture, a head turn, a blink | whenever the take offers one; it hides the join |
| J-cut | audio of the next shot leads by 4–8 frames | into b-roll — the viewer hears the next thought before seeing it |
| L-cut | audio of the current shot trails 4–8 frames | out of a device hold back to the speaker |
| match cut | cut on a shape that continues (a window → a floor plan, a hand → a map pin) | once per ad, where it exists; never forced |
| smash cut | hard cut from quiet to loud, or dark to light | the slam |

## 3. Transitions — the joins that are visible (budgeted)

| Name | Spec | Budget | Trigger |
|---|---|---|---|
| white flash | 3–4 frames to `#FFFAF0`, exponential decay | ≤1 per 6s | section seams, the slam, hook open |
| dip-to-white | 2 frames | — | a soft landing ("a forever view") |
| dip-to-ink | 4 frames to the card colour | 1 | into the end card |
| whip pan | see §1 | ≤1 per 6s | section change, b-roll entry |
| slide / wipe | new picture pushes the old 14 frames, ease-in-out; left for doubts, right for likes | — | list structures |
| split-slide | the two halves of a split swap | — | VS genre |
| torn split | b-roll tears in from the top over 6 frames to a 52/48 split with a jagged seam | ≤4 per ad | an insert where the speaker must stay visible |
| zoom-through | push into a device until it fills the frame, cut inside the move | 1 | into an interstitial |
| speed-ramp cut | cut at the peak of a 1.2× ramp | — | list runs |
| light leak / lens flare / glitch / film burn | **not in the library** | 0 | these are the tells |

**The rule that matters most:** the same transition never appears twice in a row, and a whip is never followed by a flash. Rotate: whip → cut → cut → flash → cut → slide → cut → whip. The composer's `transition_rotation` seed is the written order above; a human edit reads it off this table.

## 4. Type motion — how captions and devices arrive

| Name | Spec | Where |
|---|---|---|
| caption pop | line scales 1.15→1.00 in 4 frames, ease-out | every caption cue |
| box pop | the orange box scales 0→1.0 with overshoot 1.6 over 6 frames, the word appears at 60% | the boxed word, when the cue is a number or the pivot |
| roll-up | digits count from 0 to value over 0.6–0.9s, ease-out ³ | prices, %, counts in cards |
| rise-in | card translates +260px→0 over 10 frames with a soft shadow | bottom-third cards |
| slide-in | bars/pills enter from the right, staggered 1 per spoken item | stacks, lists |
| fill | grid/meter fills over 1.2s, ease-in-out, glow on the lit set | dot grid, price rail |
| stamp | word scales 1.8→1.0 in 6 frames, rotated −12°/+9°, red | GONE |
| strike | a gold line draws left→right through a question over 8 frames | the wrong question |
| tick | checkmark draws in 5 frames after the line is spoken, pill goes green | checklists |
| typewriter | **not in the library** | the single most recognisable machine tell |

Every arrival has a matching exit: cards drop out the way they came in (−260px, 6 frames), captions cut (never fade), interstitials cut on a J-cut.

## 5. Sound — motion the viewer hears

- Whoosh on every whip (−18 dBFS, 180ms, low-passed for vertical whips).
- Soft hit on every punch landing on a number; a deeper hit on the slam; a tick on each roll-up step and each checklist tick.
- Bed at 9% under VO; ducks 3 dB for 300ms on every hit; drops out entirely for the 8-frame silence before a slam.
- All SFX and beds from the owned set. Nothing claimable.

## 6. The anti-tell rules — why an edit reads "AI-made", and the fix

| Tell | Why it reads machine | Fix (and where it is enforced) |
|---|---|---|
| The same b-roll clip twice | humans remember pictures | `used_broll` set in the composer; QC item |
| Metronomic shot lengths | every shot 1.10s exactly | cuts land on word gaps, which jitter naturally; the composer snaps to `cue` boundaries, never to a grid; if a human cut is too even, offset three cuts by ±6 frames |
| Captions that drift from speech | the eye reads ahead of the ear | word-level timings; fix the transcript before splitting cues |
| Caption on top of a card that already has copy | two voices at once | "device owns the frame" rule |
| Transitions as decoration | a whip where nothing changed | every whip needs a section change or a new picture under it |
| Light leaks, lens flares, glitch | they come from packs | not in the library |
| Typewriter text | it is the default effect of every tool | not in the library |
| Static holds | the frame stops breathing | `drift` on every hold |
| Stock that is not Singapore | the audience lives here | the SG allowlist; deck renders for the project |
| Gradient-blob or neon backgrounds under captions | there is no room in a real ad | captions sit on the footage with a shadow, or on a scrim over b-roll |
| Perfect stabilisation on a selfie | phones shake | `handheld` on UGC shots |
| Every number the same size and colour | nothing is important | gold in cards, orange box in captions, the pivot number gets the slam |
| The same end card on every ad | the account looks templated | three card styles rotate |

**The three-tell test** (ship gate): watch the final once at 1.5×. If you notice (a) a picture you have seen before in the ad, (b) a cut rhythm you could tap along to, or (c) a caption arriving before or after the word, it is not done.

## 7. Variation seeds — eight families, so no two ads cut the same

| Family | Dominant join | Secondary | Caption arrival | Device motion | Feel |
|---|---|---|---|---|---|
| Whip-led | whip | hard cut | pop | rise-in | reportage |
| Flash + punch | white flash | punch, slam | box pop | slam, stamp | aggressive |
| Slide/wipe | slide | speed-ramp cut | pop | slide-in | editorial |
| Match / split | match cut, split-slide | hard cut | pop | fill | analytical |
| Jump-cut UGC | jump cut | punch 1.06 | wordPop | tick | raw |
| Parallax walk | parallax push | dip-to-white | strike | roll-up | cinematic |
| Torn-insert | torn split | J/L cut | pop | rise-in | documentary |
| Hold-and-build | drift | zoom-through | box pop | fill, roll-up | explanatory |

A campaign's Variation Register records which family each ad used (axis 7). Adjacent ads in one ad set never share a family.

## 8. Implementation notes

- All of §1 maps to `effects.move(kind, nframes)` in `E:\REMOTION\ads\effects.py` (`push`, `punch`, `whip` exist; `pull`, `slam`, `drift`, `parallax`, `handheld`, `ramp` are to add).
- §4 devices are frame generators: a function of `t∈[0,1]` that returns the frame. Reference PIL implementations for receipt_card, dot_grid, bar_pair, price_gap, vs_split, interstitial, same_stack, price_line, ballot_tiles, two_three_split, checklist and end_card are in `03_ACTIVE_CAMPAIGNS/01_ACTIVE/2026-08-Thomson Reserve/02_AD_EDIT_DIRECTION/styleframes/styleframes.py`. Loop the PNG sequence at `-framerate 30`; never fade a single PNG (it holds invisible — `/rei-ad-build` §5).
- Whip blur is a horizontal box average of shifted copies (`whip_blur()` in the same file) — cheap, and it matches what a real pan does to a sensor.
- Caption plates: Anton 92px (Punch 150px), white, one orange rounded box, shadow blur 10 / offset 6 / α190; emoji 0.7× cap height under the line.

## 9. Open items
- Edmund to approve as v1.0 and, if agreed, retire Style Bible §4.6 (yellow karaoke) for paid ads in favour of the boxed-word plate.
- Measure the eight families against the next batch of finals (cuts/min, transition counts) and write the numbers back here.
- `exit_funnel`, `plan_abc`, `strike_through`, `ten_year_rail` are specified in the Thomson EDB but not yet drawn.
