# GHL Implementation Rules (for Legacy Launch v2 build)

## Architecture
- Page = a few modular Custom Code blocks (one per major section group, keep each roughly under ~8k chars) + Page Settings → Custom CSS for shared styles. Never one giant block.
- ALL CSS rules must be scoped under a wrapper class we own: `.llv2` (GHL styles are global; bare-tag selectors bleed into GHL chrome). Give sections the class, prefix every selector.
- `<script>` tags MUST be siblings AFTER wrapper divs, never nested inside a `<div>` — nested scripts silently fail in GHL.
- Don't add a `<meta viewport>` (GHL sets its own). Handle responsive via scoped @media.
- GHL wraps custom code in its own container — design each block to be self-contained, full-width friendly.
- Full-bleed trick if needed: `width:100vw; position:relative; left:50%; margin-left:-50vw;`
- Debug: append `?customCode=false` to published URL to isolate custom-code failures.

## Fonts
- Google Fonts `<link>` once (page tracking-code/header or first custom block), not repeated per block. For custom-code content, fonts inside blocks work if loaded on the page.

## Forms & calendar
- Page-level CSS CANNOT style GHL form/calendar iframes (cross-origin). Style forms inside the Form Builder's own Styles → Advanced → Custom CSS field. Useful selectors: `input, textarea, select`, `button[type="submit"]`, `label`, `.hl-error`, `.ghl-footer-preview .ghl-submit-btn`.
- Calendar embed pattern (Step 2):
```html
<div style="min-height:700px;">
  <iframe src="https://api.leadconnectorhq.com/widget/booking/34KkdVJncaYiuAOjE0FP"
    style="width:100%;height:100%;min-height:700px;border:none;overflow:hidden" scrolling="no"></iframe>
</div>
<script src="https://link.msgsndr.com/js/form_embed.js" type="text/javascript"></script>
```
- Always reserve min-height on iframe wrappers (late-loading iframes = #1 CLS cause).
- Form embed: create form in Sites → Forms, get embed code via Share → Embed, same form_embed.js pattern. Form's own settings control the on-submit redirect (→ Step 2 URL).

## Sticky mobile CTA
- Fixed-position div in its own custom-code block near page end; hide ≥768px; add body bottom padding = bar height; must not overlap final CTA/footer.

## Buttons/anchors
- In-page smooth scroll: native GHL buttons have "Scroll to Element" action; in custom code use anchors + CSS `scroll-behavior:smooth` on the scoped container (html-level is fine too but scope it via JS if needed).

## Import/replication paths
- New funnel: Sites → Funnels → + New funnel; steps via "+ Add new step or import".
- "+ Add New Step" accepts a LIVE URL (ClickFunnels-style importer) and converts it to native editable elements — once our custom-code page is published, it can be re-imported from its own URL to get a native-element version. Forms/calendars must be re-connected manually after import.
- Clone funnel step: step ⋮ → Create Variation (A/B) or funnel ⋮ → Clone.

## Account facts
- Whitelabel app: app.theintellia.com. Location ID: cyeYxFVQE1l73kO6S6Lx.
- Target calendar: "New Launch/Family Legacy Ladder", ID 34KkdVJncaYiuAOjE0FP (1hr, Active).
- Existing funnel "Legacy Launch" (4W2JREPZkCv6GQknDUOQ) must NOT be modified. We create a NEW funnel.
