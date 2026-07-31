# Legacy Launch V2 — GHL Build Guide

A precise, paste-in-order guide to stand up the two-step funnel in GoHighLevel
(whitelabel: **app.theintellia.com**, Location ID **cyeYxFVQE1l73kO6S6Lx**).

> **Do NOT touch** the existing funnel "Legacy Launch" (`4W2JREPZkCv6GQknDUOQ`).
> Everything below creates a brand-new funnel.

---

## ✅ Already done for you (July 9, 2026)

| Item | Status |
|---|---|
| New funnel **Legacy Launch V2** created | ✅ (`ILuFW2Qv6l9UIXk6lUIM`) — skip §1.1 |
| Step 1 **Strategy Call Opt-in** (path `/strategy-call`) | ✅ created, blank page started (page `4JECqA37xZnvFFNi3DTa`) — skip §1.2 |
| Step 2 **Book Your Strategy Call** (path `/schedule-call`) | ✅ created — skip §1.3 (note: `/book-call` is a reserved GHL path, hence `/schedule-call`) |
| Opt-in form shell created | ✅ **"Form 18"**, ID `cw6XigpSZy8OCZgtDC34` (Sites → Forms) — still needs §4 config: rename to `Legacy Launch V2 — Qualify`, add the two dropdowns, swap consent checkbox, button text, redirect, custom CSS |
| Booking calendar identified | ✅ "New Launch/Family Legacy Ladder" `34KkdVJncaYiuAOjE0FP` — pre-wired in `page2-block-01.html` |
| Mobile sticky-bar overlap fix | ✅ already applied in `page1-custom-css.css` (slim button-only bar <520px) |

**Why the rest is manual (or one setting away from automated):** GHL renders the page/form
builders inside a cross-origin iframe (`*.leadconnectorhq.com`), which the Claude Chrome
extension currently isn't allowed to control. To let Claude finish the paste-in for you,
add **`leadconnectorhq.com`** to the Claude extension's allowed sites (extension icon →
site access) and ask Claude to continue. Otherwise the paste-in below takes ~20 minutes by hand.

Also: the funnel has **no domain attached** yet — Funnel → Settings → Domain (e.g.
`legacylaunch.com.sg`) before the form redirect URL (§4.8) will resolve.

---

## 0. File map (what you're pasting from)

```
dist/
├─ optin-preview.html                         ← QA only. Open in a browser to see Step 1.
├─ booking-preview.html                        ← QA only. Open in a browser to see Step 2.
└─ ghl/
   ├─ page1-custom-css.css                      → Step 1 · Page Settings → Custom CSS
   ├─ page1-block-01-hero.html                  → Step 1 · Custom Code element #1
   ├─ page1-block-02-problem-mechanism.html     → Step 1 · Custom Code element #2
   ├─ page1-block-03-cases-testimonials.html    → Step 1 · Custom Code element #3
   ├─ page1-block-04a-call-qualify.html         → Step 1 · Custom Code element #4
   ├─ page1-block-04b-faq.html                  → Step 1 · Custom Code element #5
   ├─ page1-block-05-form-finalcta-footer.html  → Step 1 · Custom Code element #6 (edit {{FORM_EMBED_SRC}})
   ├─ page1-block-06-sticky-scripts.html        → Step 1 · Custom Code element #7 (LAST)
   ├─ page2-custom-css.css                       → Step 2 · Page Settings → Custom CSS
   ├─ page2-block-01.html                        → Step 2 · Custom Code element #1
   └─ form-builder-custom-css.css                → Sites → Forms → your form → Styles → Advanced → Custom CSS
```

Every block is already wrapped in `<div class="llv2">…</div>` and each is < 8,000
characters (GHL's practical Custom Code ceiling). Paste them **in the order listed**.

---

## 1. Create the funnel + two steps

1. **Sites → Funnels → + New Funnel.** Name it **`Legacy Launch V2`**.
2. Add **Step 1**, name it `Opt-In` (path e.g. `/new-launch-strategy-call`). Choose a **blank** template.
3. Add **Step 2**, name it `Booking` (path e.g. `/you-qualify`). Blank template.
4. Note the **published URL of Step 2** — you'll wire the form's redirect to it in §4.

---

## 2. Load the fonts once per page (recommended)

The CSS files already `@import` Google Fonts, so you can skip this. But `<link>`
loads faster and avoids an occasional FOUT. For **each** step:

- **Funnel → Settings → (or the page's) Tracking Code → Header**, paste:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

If you add the `<link>`, delete the `@import url(...)` first line from the matching
`*-custom-css.css` before pasting (avoids loading fonts twice). Optional, not required.

---

## 3. Build Step 1 (Opt-In)

### 3a. Page CSS
- Open Step 1 in the builder → **Page Settings (gear) → Custom CSS**.
- Paste the entire contents of **`page1-custom-css.css`**. Save.

### 3b. Page body — drop 7 Custom Code elements top-to-bottom
For each: drag a **Custom Code / Custom HTML** element onto the page (one per row,
full width), open it, and paste the whole file. Keep this exact order:

| # | Paste this file | Contains |
|---|-----------------|----------|
| 1 | `page1-block-01-hero.html` | audience bar + hero + trust stats |
| 2 | `page1-block-02-problem-mechanism.html` | dead-end property + New Launch Ladder |
| 3 | `page1-block-03-cases-testimonials.html` | 4 case studies + testimonial wall |
| 4 | `page1-block-04a-call-qualify.html` | the 60 minutes + qualification columns |
| 5 | `page1-block-04b-faq.html` | FAQ accordions |
| 6 | `page1-block-05-form-finalcta-footer.html` | **opt-in form** + final CTA + footer |
| 7 | `page1-block-06-sticky-scripts.html` | sticky mobile bar + all scripts (**must be last**) |

> **Why the split & order matters:** every "Check If You Qualify" button is an
> anchor to `#llv2-apply`, which lives in block #6. The scripts in block #7 wire
> the smooth-scroll, the scroll-reveal, and the sticky bar — they are **siblings
> after** the wrapper div (GHL silently drops `<script>` nested inside a div), so
> block #7 has to be the final element on the page.

### 3c. Insert the opt-in form (do §4 first to have the embed src)
- In **block #6** replace the placeholder `{{FORM_EMBED_SRC}}` inside the `<iframe src="…">`
  with your form's real embed src (see §4). Leave everything else as-is — the
  `<script src="…/form_embed.js">` sibling that makes the iframe auto-resize is
  already there.

---

## 4. Create the opt-in form (Sites → Forms)

1. **Sites → Forms → + Build Form → Start from scratch.** Name it
   `Legacy Launch V2 — Qualify`.
2. Add these fields **in this order** (copy from copy-deck §13):

   | Field | Type | Required | Notes |
   |-------|------|----------|-------|
   | Full name | Standard `Full Name` (or First+Last) | yes | label: **Full name** |
   | Email | Standard `Email` | yes | label: **Email** |
   | Mobile | Standard `Phone` | yes | label: **Mobile** |
   | When are you planning to buy? | Dropdown (single select) | yes | options below |
   | Your current property | Dropdown (single select) | yes | options below |
   | Consent | Checkbox / Terms | yes | text below |

3. **Dropdown "When are you planning to buy?"** options (exact):
   - `Within 3 months`
   - `3–6 months`
   - `6–12 months`
   - `Just exploring for now`

4. **Dropdown "Your current property"** options (exact):
   - `HDB — planning to upgrade`
   - `Private — planning my next move`
   - `Own both HDB and private`
   - `First-time buyer`

5. **Consent checkbox** text:
   > I agree to be contacted about my New Launch Strategy Call. My details are held under Singapore's PDPA (2012) and never sold or shared.

6. **Submit button text:** `Request My Strategy Call`.

7. **Styles → Advanced → Custom CSS:** paste **`form-builder-custom-css.css`**.
   (Page CSS can't reach inside the form iframe — this is the only place these
   styles apply.) Save.

8. **On-submit action → Redirect / "On submit go to URL":** set to the **Step 2
   published URL** from §1.4. (This is what advances a qualified lead to the calendar.)
   *Optional gating:* if you want to send "not-a-fit" answers elsewhere, use a
   Workflow trigger on the form submission instead of a hard redirect.

9. **Share → Embed → copy the embed code.** From it grab the iframe **`src`** URL
   (looks like `https://link.msgsndr.com/widget/form/XXXXXXXX` or an
   `api.leadconnectorhq.com/widget/form/…` URL). Paste that into `{{FORM_EMBED_SRC}}`
   in block #6 (§3c).

---

## 5. Build Step 2 (Booking)

1. Open Step 2 → **Page Settings → Custom CSS** → paste **`page2-custom-css.css`**. Save.
2. Drop **one** Custom Code element and paste **`page2-block-01.html`**.
   - The calendar iframe is pre-wired to **New Launch/Family Legacy Ladder**
     (`https://api.leadconnectorhq.com/widget/booking/34KkdVJncaYiuAOjE0FP`) with the
     `form_embed.js` resizer sibling. No edit needed unless the calendar ID changes.
   - If the calendar shows a domain error, swap the host to your whitelabel:
     `https://app.theintellia.com/widget/booking/34KkdVJncaYiuAOjE0FP`.

---

## 6. SEO / meta (per step)

**Step 1 → Page Settings → General / SEO:**
- **Title:** `New Launch Strategy Call | Legacy Launch — Exit-First Property Advisory Singapore`
- **Description:** `We disqualify 90% of new launch projects and map your next 2–3 property moves before you buy. A calm, numbers-first strategy call for Singapore buyers moving in 3–6 months. Not an agent pitch.`

**Step 2 → Page Settings → General / SEO:**
- **Title:** `You Qualify — Book Your New Launch Strategy Call | Legacy Launch`
- **Description:** `Choose a time for your 1-hour New Launch Strategy Call. Bring your shortlist. Leave with an exit-first plan for your next property move.`

Set a favicon and social share image in Funnel Settings if desired. **Do not** add a
`<meta viewport>` — GHL manages it.

---

## 7. Publish & QA checklist

Publish both steps, then on a **real phone** and a **desktop**:

- [ ] Fonts render (Playfair headlines, Inter body) — no system-serif fallback flash.
- [ ] Dark→light section rhythm looks intentional (navy hero → ivory → white → navy cases → ivory → white → ivory → white → navy form/CTA → dark footer).
- [ ] Every **Check If You Qualify** button smooth-scrolls to the form.
- [ ] Form submits → lands on Step 2 calendar.
- [ ] Calendar loads and lets you pick a slot; no layout shift after it loads (min-heights reserved).
- [ ] **Mobile:** sticky bottom bar appears < 768px, the ✕ dismisses it, and the footer isn't covered (body gets bottom padding while the bar is visible).
- [ ] Scroll-reveal: sections fade in; if you disable JS the page is still fully visible.
- [ ] No red anywhere; buttons are gold with navy text; form submit reads clearly.
- [ ] Debug tip: append **`?customCode=false`** to the published URL to confirm whether an issue is from a custom-code block or the GHL page itself.

---

## 8. Convert to native GHL elements later (optional)

The custom-code build is production-ready, but if you want fully native, editable
elements (so non-devs can tweak copy in the builder):

1. Publish Step 1 as above.
2. In the funnel, **+ Add New Step → Import from URL** and paste Step 1's **live
   published URL**. GHL's ClickFunnels-style importer converts the rendered page
   into native sections/rows/elements.
3. **Re-connect the form and calendar by hand** — importers turn embeds into static
   markup. Drop a native **Form** element (pick `Legacy Launch V2 — Qualify`) and a
   native **Calendar** element (`New Launch/Family Legacy Ladder`).
4. Re-apply brand styling: the imported page keeps most inline CSS, but move the
   shared rules from `page1-custom-css.css` into the new page's Custom CSS so future
   edits stay consistent.
5. Keep the custom-code version as an A/B variation (step ⋮ → **Create Variation**)
   until the native rebuild matches.

---

## 9. Replicate this design for other pages

Everything is a self-contained kit keyed to the `.llv2` namespace. To spin up a new
advisory page in the same skin:

1. **Copy `page1-custom-css.css` verbatim** into the new page's Custom CSS. It's the
   entire design system (tokens, type scale, components, responsive). Nothing to change.
2. **Reuse the block scaffolding** — copy any `page1-block-*.html` and swap only the
   copy inside. Keep the class names; they carry all the styling.
3. **Swap these per page:**
   - Copy (headlines, body, stats, cases, FAQ) — from a new copy deck.
   - `{{FORM_EMBED_SRC}}` → the new page's form embed src.
   - Calendar iframe `src` → the new calendar ID (Step 2 only).
   - SEO title/description.
   - The `#llv2-apply` anchor id if you run more than one form on a page (rename in
     both the form section and the CTA `href`s so they stay matched).
4. **Keep the rules that make it survive GHL:** every selector stays scoped under
   `.llv2`; `<script>` stays a sibling after the wrapper div; no `<meta viewport>`;
   each block under ~8k chars.
5. **Change the accent by editing one line** — the tokens block at the top of the CSS
   (`--gold`, `--navy`, `--ivory`, `--ink`). Recolor the whole system from there.
