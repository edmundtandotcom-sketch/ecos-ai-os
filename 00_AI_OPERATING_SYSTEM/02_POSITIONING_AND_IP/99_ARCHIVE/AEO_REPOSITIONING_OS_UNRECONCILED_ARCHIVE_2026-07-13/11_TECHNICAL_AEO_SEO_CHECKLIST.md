# 11 — TECHNICAL AEO/SEO READINESS CHECKLIST
**Phase 11 · AEO Repositioning OS · Singapore property advisory**
**Owner:** Technical AEO/SEO Auditor (Sonnet) · **Date:** 9 July 2026 · **Status:** Build-ready; inherits all LOCKED decisions from `_MASTER_CONTEXT_BRIEF.md`
**Ecosystem in scope:** `thereimethod.com` (authority site, platform decided below) · GHL funnels on vanity domains (`secondpropertyladder.com`, `legacylaunch.com.sg`) · YouTube (`@singaporerealestateinsider`) · Google Business Profile (`share.google/bpyWTGgjlyNxt8Xiz`)

---

## Executive Summary

This phase audits and specs the plumbing that decides whether the entity/content work in docs 01–10 is actually crawlable, indexable, fast, and citable by both Google and AI answer engines. The single highest-leverage decision is the **authority-site platform**: this doc recommends **GHL Websites**, not WordPress or static/headless, because the operating team is two non-technical founders who already live inside GHL daily — the cost of a second CMS (updates, plugins, a second login, a webmaster dependency) outweighs GHL's real weaknesses in native schema/blog tooling, which are solvable with a disciplined custom-code SOP given here. The second-highest-leverage item is **domain hygiene**: `03_DOMAIN_ARCHITECTURE.md` does not yet exist, so this doc implements D2–D4 directly from the Master Brief — two domains retire via 301, one parks, two vanity domains stay live as noindexed bridge funnels canonical to the authority hub. Everything downstream (schema injection, redirects, tracking) is scoped to GHL's real constraints: an 8,000-character custom-code limit per page/site, uncertain native robots.txt control [VERIFY], and no plugin ecosystem — so every schema block, tracking script, and noindex tag competes for the same character budget and must be audited together, not bolted on ad hoc. This doc also makes the deliberate **AEO call to allow AI crawlers** (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) in robots.txt — the whole project's goal is to be the cited answer, and blocking the crawlers that read for citation contradicts that goal. Everything below is sequenced into a P0→P2 priority list with owners and done-criteria, because a checklist without sequencing is a wish list.

---

## 1. CRITICAL DECISION — Authority Site Platform

### 1.1 The options, weighed against the real constraint

The real constraint is not "what's the best CMS" in the abstract — it's **who operates it**. Edmund and Cindior are a two-person, non-technical team who already run their entire funnel, CRM, calendar, and attribution stack inside one GHL sub-account (`cyeYxFVQE1l73kO6S6Lx`). Any platform choice that adds a second system they must personally learn, patch, or pay someone else to run is a real ongoing cost, not a one-time setup cost.

| Option | Strength | Weakness for this team | Verdict |
|---|---|---|---|
| **(a) GHL Websites** | Same login/CRM/attribution as everything else they already run; native form + calendar embeds (zero integration work — the objects already exist: form `cw6XigpSZy8OCZgtDC34`, calendar `34KkdVJncaYiuAOjE0FP`); custom-code injection per page and site-wide covers schema + tracking; no plugin updates, no security-patch cadence, no separate hosting bill | Weaker native on-page SEO tooling (no Yoast/RankMath-style auto-schema, meta editing is manual per page); blog feature is basic (enabled, unused); page-builder elements can bloat Core Web Vitals if used carelessly; custom-code budget is capped at ~8,000 characters per block; robots.txt customisation depth is [VERIFY] | **Recommended** |
| **(b) WordPress** | Mature SEO plugin ecosystem (RankMath/Yoast auto-schema, XML sitemaps, redirect managers, image optimisation); best-in-class blog authoring UX; huge template/theme flexibility | A second platform entirely: separate login, separate hosting, plugin/core updates, security patching, backups, potential plugin-conflict debugging — none of which this team can self-serve; requires either a technical co-founder or an ongoing webmaster retainer, which does not currently exist | Viable **only** with a funded webmaster retainer — not now |
| **(c) Static/headless (Next.js, Astro, Cloudflare Pages, etc.)** | Fastest possible Core Web Vitals; full schema/markup control in code | Founders cannot self-serve a single blog post, FAQ edit, or founder-bio update without a developer touching a git repo — this fails the core Content Engine SOP requirement (doc 10) that the team publishes consistently | **Disqualified** for this team's operating model |

**Recommendation: GHL Websites**, with the weaknesses actively mitigated rather than ignored (§1.2). Revisit WordPress only if/when the business funds a part-time technical retainer — at that point the SEO-plugin advantage becomes worth the maintenance cost. Static/headless is not viable while the team is two non-technical people; do not reconsider until there is a technical hire.

### 1.2 Implementation checklist for GHL Websites as the authority-site platform

**A — Schema JSON-LD injection**
1. Site-wide `Organization` + `ProfessionalService` block (doc 02 §6b) goes in **GHL Websites → Settings → Custom Code → Header** (site-level, applies to every page) so the `@id="https://thereimethod.com/#organization"` node is defined once and referenced by every other page's `Person`/`Service`/`Article` blocks via `"@id"` reference rather than re-declaring the org each time (keeps per-page character budget free).
2. Page-specific schema (`Person`, `Article` + `DefinedTerm`, `Service`, `FAQPage`, `VideoObject`, `Review`) goes in that page's **individual page settings → Tracking Code / Custom Code → Header**, as a single `<script type="application/ld+json">` block.
3. **Budget discipline (8,000-character limit applies per custom-code block on GHL page-builder pages, confirmed for funnel HTML/CSS blocks; treat as the working assumption for Websites pages too until [VERIFY]):** every page's header custom-code field will likely carry schema **and** tracking pixels **and** any noindex meta tag together. Before publishing any page, total the characters of: JSON-LD + GA4/Meta Pixel snippets + any meta robots tag. If a page is schema-heavy (e.g. the category hub with `Article`+`DefinedTerm`+`FAQPage`), strip whitespace/minify the JSON-LD and move non-essential tracking (e.g. secondary retargeting pixels) to a Google Tag Manager container loaded once, so only one short GTM snippet — not five separate pixel scripts — competes for the budget.
4. [VERIFY before build]: confirm GHL Websites (as distinct from GHL Funnels) exposes the same per-page header custom-code field and the same character ceiling. If Websites has a materially different (larger) limit, this constraint eases; do not assume — check in the live builder.

**B — Blog workflow (non-technical, repeatable)**
1. Draft in Google Docs (per Content Engine SOP, doc 10) → internal review/approval → paste into **GHL Blogs** post editor.
2. Set per-post: URL slug (short, matches target keyword/topic per doc 05 clusters), meta title (≤60 characters), meta description (≤155 characters, contains the category term where natural), featured image (WebP, descriptive alt text — §12 below), author (Edmund Tan or Cindior Ho, linked to their `/about/` page — §15).
3. Add post-specific JSON-LD (`Article`, `author` referencing the `Person` `@id`, `datePublished`/`dateModified`) via the post's custom-code field if GHL Blogs exposes one [VERIFY]; if it does not, fall back to the site-wide header block covering only the `Organization`/`WebSite` node and accept that individual blog posts inherit generic schema until a workaround is found (e.g. embedding the JSON-LD as a visible `<script>` inside the post body itself, which GHL's rich-text/HTML block does support).
4. On publish, confirm the post appears in the auto-generated XML sitemap (§3) and manually submit the URL in Search Console (**URL Inspection → Request Indexing**) rather than waiting for organic crawl — critical in the first 90 days while domain authority is near zero.

**C — GHL form/calendar embeds on the authority site**
Because the form (`cw6XigpSZy8OCZgtDC34`) and calendar (`34KkdVJncaYiuAOjE0FP`) already exist in the same GHL location, embedding on `thereimethod.com` is a native "Add Element → Form/Calendar" action inside the page builder — no API keys, no iframe hacks, no cross-domain auth. This is the concrete, day-to-day payoff of keeping the authority site inside GHL: every CTA on the site (Position Map session booking, Blueprint enquiry) reuses the exact same GHL objects the funnels use, so attribution fields (`utm_source`, `ad_id`, `campaign_id` — §6.5) populate identically regardless of whether the visitor arrived via the authority site or a vanity funnel.

---

## 2. THE 20-AREA TECHNICAL AUDIT + SPEC

### 1. Crawlability
**Current state:** `thereimethod.com` content status is [VERIFY — Q3 in Master Brief]; assume greenfield build. **Spec:** ensure GHL Websites does not gate the site behind a password/staging flag before launch (common cause of accidental "noindex everything"); confirm no `Disallow: /` left over from a builder default; test with **Google Search Console URL Inspection** ("Live Test") on the homepage and category hub before any link-building or ad spend points at the domain.

### 2. Indexability
**Current state:** the two vanity funnel domains (`secondpropertyladder.com`, `legacylaunch.com.sg`) must NOT be indexed as standalone content per D3 — only their single bridge page each is indexable. **Spec:** every multi-step funnel page (opt-in, booking, thank-you, the diagnostic's question screens) gets `<meta name="robots" content="noindex,follow">` injected via that page's custom-code header field. Only the one designated bridge page per vanity domain is indexable, and it carries a canonical tag to the authority hub (§9). Audit quarterly via `site:secondpropertyladder.com` and `site:legacylaunch.com.sg` in Google to confirm nothing beyond the bridge page has leaked into the index.

### 3. XML sitemap
**Current state:** GHL Websites/Blogs auto-generates a sitemap for indexed pages [VERIFY exact URL pattern — typically `/sitemap.xml`]. **Spec:** confirm the auto-sitemap excludes noindexed funnel steps by default; if it does not, manually exclude via GHL's page-level sitemap toggle [VERIFY this toggle exists] or maintain a manual sitemap covering only: homepage, category hub, 5-Step pages, founder pages, offer pages, blog posts, FAQ/glossary. Submit the sitemap URL in Search Console for `thereimethod.com` on launch day, and re-submit after each redirect/domain change (§10).

### 4. robots.txt
**Current state:** GHL's native robots.txt customisation depth for Websites is [VERIFY — some page-builder SaaS platforms only expose a toggle, not a full editable file]. **Spec:** the file must (a) allow all major search engines, (b) explicitly `Disallow` any booking-widget iframe path if it generates its own crawlable URL, (c) implement the AI-crawler allow policy (§7). If GHL does not expose a fully editable robots.txt, this is a P0 escalation — file a support ticket with GHL and, if genuinely unsupported, treat it as a real limitation of the platform choice (not a reason to abandon GHL, since Google-Extended/GPTBot/ClaudeBot/PerplexityBot default to *allow* when no robots.txt rule exists — the risk is only that you cannot selectively *block* something later, not that AI visibility is blocked by default).

### 5. Page speed (Core Web Vitals) — GHL page-builder weight caveats
**Current state:** the Legacy Launch V2 funnel already respects an 8,000-character custom-code discipline (`.llv2` CSS namespace, per Report 3) — good precedent to carry to the authority site. **Risk:** GHL's drag-and-drop builder can silently add heavy default CSS/JS bundles, stock image carousels, and third-party embeds (chat widgets, review widgets) that tank Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS). **Spec:** (a) compress every image to WebP before upload (§12); (b) avoid carousel/slider elements on the category hub and founder pages — they are consistent CLS/LCP offenders; (c) load any non-essential third-party script (chat widget, review badge) via a single Google Tag Manager container with a delayed/idle trigger, not inline in every page's header; (d) test every new template with **PageSpeed Insights** and **Search Console → Core Web Vitals report** before it goes live, targeting LCP <2.5s, CLS <0.1, INP <200ms (Google's published CWV thresholds). Re-test after every redirect wave, since 301 chains add latency.

### 6. Mobile UX
**Current state:** the sticky bottom CTA bar pattern is already in use on Legacy Launch V2 (per Report 3's creative-direction notes) — mobile-first is confirmed intentional given 90%+ assumed mobile ad traffic. **Spec:** replicate the sticky CTA bar pattern on the authority site's offer pages (`/position-map-session`, `/blueprint`) and category hub — single persistent CTA button ("Book Your Position Map Session"), not competing CTAs. Test tap-target sizing (≥44px) and viewport meta tag presence on every template. Confirm the sticky bar does not cover form fields or trigger a CLS penalty on load.

### 7. Internal links
**Current state:** doc 02 §2's entity diagram is the source graph. **Spec:** every guide/blog post links to (a) the category hub, (b) the relevant one of the 5-Step pages, (c) the author's `/about/` page, (d) one offer page (Position Map session as the universal CTA). Every 5-Step page links back to the category hub and sideways to the adjacent step (sequential internal linking reinforces "the order is the product"). No orphan pages — audit via Search Console's "Pages" report (pages with 0 internal links referring) quarterly.

### 8. Duplicate content
**Current state:** two duplicate-content risks exist, and they are not the same risk. **(i) Internal/harmless:** the `.docx`/`.md` working documents in this Drive folder are not published, so they carry zero public duplicate-content risk — ignore. **(ii) Real risk:** the vanity-domain bridge pages (`secondpropertyladder.com`, `legacylaunch.com.sg`) necessarily restate category/offer language that also lives on the authority hub. **Spec:** every bridge page must (a) carry a `rel="canonical"` pointing to the relevant `thereimethod.com` page (not self-canonical), and (b) be genuinely thin/bridge-only in copy — a short framing paragraph plus links, not a re-published version of the hub's full content. This is the canonical rule D3 establishes; formalise it fully when `03_DOMAIN_ARCHITECTURE.md` is written — until then, this doc's §9 is the working canonical spec.

### 9. Canonicals
**Spec (per D2–D3, standing in for the not-yet-written doc 03):**
| Page | Canonical target |
|---|---|
| `secondpropertyladder.com` bridge page | `https://thereimethod.com/second-property-ladder` |
| `legacylaunch.com.sg` bridge page | `https://thereimethod.com/second-property-ladder` (or a Legacy Launch–specific sub-page if doc 04's sitemap creates one) |
| All noindexed funnel steps | No canonical needed (noindex already excludes them; do not canonical a noindexed page to itself) |
| Every authority-site page | Self-canonical (`https://thereimethod.com/<path>`), always the HTTPS, non-www (or www — pick one and enforce site-wide) version |

### 10. Redirects
See §4 (dedicated section) for the full domain-by-domain implementation plan.

### 11. Schema
See §3 (dedicated Schema Map). Governing rule from doc 02: Google retired `HowTo` rich results (Aug 2023) — do not use it. `FAQPage` rich-result *display* is currently limited by Google to a narrow set of well-known/authoritative sites (government, health) — `thereimethod.com` will very likely not qualify for the visible rich snippet in the near term. **Still implement `FAQPage` markup accurately on every genuine FAQ block** for two reasons that don't depend on the rich-result eligibility: (a) it is a strong, structured signal for AI answer engines parsing the page for citable Q&A (the actual AEO goal), and (b) eligibility criteria can change — accurate markup costs nothing extra and is future-proof. Never mark up FAQ content that isn't visibly on the page (D8).

### 12. Image SEO
**Spec:** convert every image to WebP before upload (smallest file size at equivalent quality; GHL should serve it as-is — confirm GHL doesn't force a re-encode to a heavier format [VERIFY]). Alt-text discipline: descriptive, keyword-natural, never keyword-stuffed — e.g. founder photos get entity-tagged alt text like `"Coach Edmund Tan, co-founder of The REI Method, Singapore property advisor"` rather than generic `"headshot.jpg"` or bare `"Edmund Tan"`. This reinforces the Person entity (doc 02 Entity 1/2) every time the image appears, including in social shares and image search. Compress via a free tool (Squoosh, TinyPNG) before upload — do not rely on GHL to compress.

### 13. Video SEO
**Spec:** every `thereimethod.com` guide/blog page that embeds a YouTube video gets a matching `VideoObject` JSON-LD block (name, description, thumbnailUrl, uploadDate, contentUrl/embedUrl, `publisher` → The REI Method `@id`, `creator` → the relevant founder `@id`) — VideoObject is eligible because the video is genuinely embedded on-page (doc 02 §4). On YouTube itself: add **chapters** (timestamps in the video description, minimum 3 chapters, first chapter must start at 0:00) to every long-form video — chapters are both a YouTube ranking/watch-time signal and a direct AEO asset (AI answer engines and Google can cite a specific chapter/timestamp as the answer to a specific question). Add **transcripts** to the corresponding article page (not just relying on YouTube's auto-captions) — a full on-page transcript is crawlable text that reinforces the article's topical relevance and gives AI engines clean text to quote instead of parsing video.

### 14. Breadcrumbs
**Spec:** implement visible on-page breadcrumbs (Home → The Second Property Ladder → [Step name]) on every hub/step/guide page, matched with `BreadcrumbList` JSON-LD. This reinforces the hierarchical entity structure (doc 02's `hasPart` relationships) and is a legitimate, still-eligible Google rich result. Do not breadcrumb the vanity-domain bridge pages (they are single standalone pages, not part of a hierarchy) — a breadcrumb there would be misleading (D8: no schema for structure that doesn't exist).

### 15. Author boxes
**Spec:** every blog post, guide, and 5-Step page carries a visible author box (name, photo, one-line bio, link to `/about/edmund-tan` or `/about/cindior-ho`) with the byline wrapped in schema `author` referencing that Person's `@id` (doc 02 §6a). This is the single most repeatable on-page action that builds the Person entities Google/AI need to recognise Edmund and Cindior as the named experts behind the category — do it on every piece of content from day one, not retroactively.

### 16. Visible dateModified
**Spec:** every guide/pillar page shows a visible, human-readable "Last updated: [date]" line near the top or byline, matched by a `dateModified` property in that page's `Article` schema. This matters doubly here because Singapore property content is regulation-sensitive (ABSD rates, MOP, SSD holding periods, loan tenure caps) — a visible last-updated date is both an E-E-A-T/trust signal and the visible proof of the regulatory update-cadence process D7 requires. Update the visible date and the schema field together whenever regulatory figures are refreshed; a stale visible date next to updated numbers (or vice versa) is worse than no date at all.

### 17. FAQ structure
**Spec:** every hub/pillar page ends with a genuine FAQ block (5–8 real questions a Property Climber would ask — sourced from the buyer-language research in `_RESEARCH_APPENDIX.md` Report 1F, e.g. "What's the difference between the Second Property Ladder and just buying a second property?", "Do I need to sell my first property before buying my next one?"). Mark up with `FAQPage` (§11). Keep answers genuinely useful and self-contained — each answer should read as a complete, quotable answer on its own, because that is exactly the unit an AI answer engine will lift and cite.

### 18. JavaScript rendering risk
**Current state:** GHL page-builder pages render mostly server-side/static HTML for text content, but interactive widgets (booking calendar, chat, the diagnostic quiz itself) are JS-rendered. **Spec:** confirm via **Search Console URL Inspection → "View Tested Page" → screenshot/HTML** that the core text content (headings, body copy, FAQ answers) renders in the initial HTML payload, not only after JS executes — this is what determines whether Google's and AI crawlers' text-based fetchers (which mostly do not execute JS) can read the content at all. The booking widget itself should be `noindex`ed at the page level where it lives standalone (it has no independently useful content for a search result) — this is distinct from noindexing the surrounding page, which should stay indexable if it has real content around the widget.

### 19. Tracking tags
See §6 (dedicated Tracking Setup Checklist).

### 20. Search Console + Bing Webmaster + GA4 setup
See §6.1–6.2 (dedicated section) — sequencing matters here specifically because Search Console verification must happen **before** the 301 redirects execute (§4), not after.

---

## 3. SCHEMA MAP (page type → JSON-LD → injection method)

This extends doc 02 §4's type/property recommendations with the GHL-specific injection mechanism.

| Page | JSON-LD type(s) | Injection method (GHL) | Notes |
|---|---|---|---|
| `thereimethod.com` (home) | `Organization` + `ProfessionalService` | **Site-wide** custom code, header (Settings → Custom Code) | Single `@id="#organization"` node; every other page references it, never re-declares it |
| `/about/edmund-tan` | `Person` | Per-page custom code, header | `worksFor` references home page's `@id` |
| `/about/cindior-ho` | `Person` | Per-page custom code, header | Publish once ≥1 real `sameAs` exists (per doc 02 Q4) |
| `/second-property-ladder` (hub) | `Article` + `DefinedTerm` + `FAQPage` | Per-page custom code, header — **audit combined char count** with any tracking pixels on this page | Highest schema density page in the ecosystem; minify JSON, route secondary pixels through GTM |
| Each 5-Step page | `Article` + `DefinedTerm` | Per-page custom code, header | `isPartOf` references hub URL |
| `/position-map-session` | `Service` | Per-page custom code, header | No `Offer`/price schema (none is public yet) |
| `/blueprint` | `Service` | Per-page custom code, header | Add `Offer` only once price is shown on-page |
| `/reviews` + testimonial blocks | `Review` (third-party only) | Per-page custom code, header | No `AggregateRating` (self-serving reviews are not rich-result eligible — Google Search Central) |
| Blog posts / guides with embedded video | `Article` + `VideoObject` | Post-level custom code if GHL Blogs exposes it [VERIFY]; else inline `<script>` in post body via rich-text/HTML block | Chapters/transcript live on-page (§13) |
| `secondpropertyladder.com` bridge page | `WebPage` + `FAQPage` | Per-page custom code on that GHL funnel page | Canonical → hub; funnel steps noindexed, not schema'd |
| `legacylaunch.com.sg` bridge page | `WebPage` + `FAQPage` | Per-page custom code on that GHL funnel page | Same rule; add CEA compliance block in visible copy, not just schema |
| Contact page | `ProfessionalService` (LocalBusiness) | Per-page or reuse site-wide org block with added `address`/`telephone` | Must match GBP NAP byte-for-byte (doc 02 §5) |

---

## 4. REDIRECT IMPLEMENTATION PLAN

`03_DOMAIN_ARCHITECTURE.md` has not been written yet — the mechanism below implements D4 directly and should be reconciled with doc 03 once it exists.

| Domain | D4 action | Mechanism | Why this mechanism | Pre-requisite | Owner |
|---|---|---|---|---|---|
| `singaporerealestateinsider.com` | 301 → `thereimethod.com` | **Registrar/DNS-level forwarding** (e.g. the registrar's built-in "Domain Forwarding" — GoDaddy/Namecheap — or a Cloudflare Page Rule if DNS is on Cloudflare) [VERIFY current registrar] | The domain is being fully retired — no content will ever be hosted on it again, so there is no reason to point its DNS at any host (GHL or otherwise). Registrar-level forwarding needs no hosting, no SSL cert management on the source domain, and has zero ongoing dependency on GHL | **Verify domain ownership in Google Search Console BEFORE executing the redirect** (see §6.1) — otherwise historical backlink/query data for this domain is unrecoverable once traffic moves | Edmund/Cindior (GHL admin) or hired web help |
| `6figurepropertyprofits.com` | Retire + 301 → `thereimethod.com` | Same: registrar/DNS-level forwarding | Same reasoning; additionally this name is a compliance liability (D4) so it should not remain resolvable to any content, even briefly, during a migration | Search Console verification first (§6.1) | Edmund/Cindior (GHL admin) |
| `familylegacy.com.sg` | Park (renew, no content) | **No redirect.** Ensure DNS does not point to any live host; either leave unresolved or point to the registrar's default parking page (which must itself be `noindex` if it has any indexable content) | D4 says do not build — a redirect implies a destination worth sending equity to, which is premature until a campaign claims this domain | None beyond renewal | Edmund/Cindior (domain renewal only) |
| `secondpropertyladder.com` | Stays live (funnel host) | **Host-level** — DNS CNAME/A record points at GHL per GHL's custom-domain connection instructions; indexing control is via page-level noindex + canonical (§8–9), not a domain redirect | This domain is not retiring — it hosts a live GHL funnel. The "redirect" concept here is page-level (canonical), not domain-level (301) | Bridge page canonical + noindex live before any ad traffic is sent | Edmund/Cindior (GHL domain settings) |
| `legacylaunch.com.sg` | Attach now (currently unattached per Master Brief) | Host-level — DNS CNAME/A → GHL, then attach to the "Legacy Launch V2" funnel (`ILuFW2Qv6l9UIXk6lUIM`) in GHL's funnel domain settings | Matches the build guide's existing suggestion; this is a new attachment, not a redirect | None — this is a net-new DNS record, no existing traffic to preserve | Edmund/Cindior (GHL domain settings) |

**Sequencing rule that overrides all of the above:** for the two retiring domains, **do not touch DNS/forwarding until Search Console properties are verified for both the source and destination domains** (§6.1). Google's **Change of Address tool** (Search Console → Settings → Change of Address) is the correct mechanism to formally tell Google `singaporerealestateinsider.com` has moved to `thereimethod.com`, and it requires both properties verified first. Skipping verification loses the ability to check what backlinks/queries existed on the old domain and loses the Change of Address signal entirely.

---

## 5. SEO PLUGIN/CMS RECOMMENDATIONS

Because the recommended platform is GHL (no plugin ecosystem), "plugins" is replaced by a lean external tool stack — all free or already-owned:

| Need | Tool | Why |
|---|---|---|
| Search visibility monitoring | **Google Search Console** (all domains — §6.1) | Non-negotiable, free, first-party Google data |
| Secondary search engine visibility | **Bing Webmaster Tools** | Also feeds Bing/Copilot/some AI answer engines that draw on Bing's index; near-zero setup cost given GSC data can be imported |
| Site audit (crawlability, broken links, redirect chains) | **Screaming Frog SEO Spider** (free tier, up to 500 URLs — sufficient at this site's scale) | Run quarterly to catch orphan pages, broken internal links, missing alt text, duplicate titles |
| Schema validation | **Google Rich Results Test** + **Schema.org Validator** | Run on every new page template before publish — catches malformed JSON-LD before it ships |
| Core Web Vitals | **PageSpeed Insights** + **Search Console Core Web Vitals report** | Free, authoritative source for the same metrics Google uses for ranking |
| Image compression | **Squoosh** or **TinyPNG** (WebP export) | Manual pre-upload step since GHL does not reliably auto-optimise [VERIFY] |
| Tag management (keeping pixel sprawl out of the 8k custom-code budget) | **Google Tag Manager** | One GTM container snippet replaces N separate pixel scripts in GHL's header field |

**If the business later funds a technical retainer and migrates the blog to WordPress:** recommend **RankMath** over Yoast — RankMath's free tier includes schema generation, redirect manager, and a built-in Core Web Vitals-adjacent readability/SEO score, which most closely replicates what this doc is manually specifying for GHL. This is a future-state note, not a current action.

---

## 6. TRACKING SETUP CHECKLIST

### 6.1 Search Console — for ALL domains, verified before redirects
Verify every domain in Google Search Console, in this order, **before** any redirect/DNS change:
1. `singaporerealestateinsider.com` (source of a 301 — verify now to preserve historical data and enable Change of Address)
2. `6figurepropertyprofits.com` (same reason)
3. `thereimethod.com` (destination of both 301s — must be verified before Change of Address tool can be used)
4. `secondpropertyladder.com` (vanity funnel — verify to monitor for accidental indexing of noindexed funnel steps)
5. `legacylaunch.com.sg` (same, once attached)

Use **Domain property** verification (DNS TXT record) where possible rather than URL-prefix, since it captures all subdomains/protocols in one property.

### 6.2 GA4
Set up a single GA4 property for `thereimethod.com` with data streams added for each vanity domain (cross-domain measurement configured in GA4's Data Streams settings so a visitor journey from `secondpropertyladder.com` → `thereimethod.com` isn't double-counted as two sessions). Bing Webmaster Tools can import GSC data directly — set that up once GSC properties exist (§6.1).

### 6.3 Meta Pixel + Conversions API (CAPI) via GHL
GHL natively supports Meta Pixel and Meta CAPI integration at the sub-account level (Settings → Integrations). Currently **no social accounts are connected** in this GHL location (Report 2) — connecting the Meta ad account here is a prerequisite not just for tracking but for `ad_id`/`campaign_id` auto-population (§6.5). Set up Pixel + CAPI together (server-side CAPI is now the more reliable half given iOS/browser tracking-prevention), test with Meta's Events Manager "Test Events" tool before the next ad spend cycle.

### 6.4 UTM conventions
Standardise before any further ad spend:
- `utm_source`: `meta` | `google` | `youtube` | `organic` | `direct`
- `utm_medium`: `paid_social` | `cpc` | `email` | `organic` | `referral`
- `utm_campaign`: campaign slug, e.g. `legacy-launch-v2`, `spl-diagnostic`, `position-map-brand`
- `utm_content`: creative/ad variant identifier (matches the ad's internal name, not a generic label)
- `utm_term`: optional, paid-search keyword only

### 6.5 GHL attribution fields — what already exists, and what it maps to
GHL already has native ad-attribution custom fields on this location (Report 2): `utm_source`, `ad_id`, `ad_name`, `campaign_id`, `campaign_name`, `click_id`. Map them as follows — do not create duplicate fields:

| GHL field | Populates from | Requires |
|---|---|---|
| `utm_source`, `utm_medium` (if added), `utm_campaign` (if added) | URL parameters on the landing page, captured automatically by GHL's tracking script | Nothing extra — works today via manual UTM tagging on every ad/link |
| `ad_id`, `ad_name`, `campaign_id`, `campaign_name` | GHL's native Facebook/Google Ads account connection (auto-attribution) | **Currently blank/unpopulated** because no ad accounts are connected (Report 2: "no social accounts connected"). Connect the Meta ad account (and Google Ads if used) in GHL Settings → Integrations to activate auto-population — this is a prerequisite, not optional, if these fields are to mean anything |
| `click_id` | Meta `fbclid` / Google `gclid` passthrough | Works once the ad account connection above is live |

### 6.6 Call tracking (+65 8786 3931)
This number is currently the single shared contact number across all campaigns and the GHL location itself. **Recommendation: do not introduce dynamic call tracking (e.g. per-channel tracking numbers) at this stage.** The funnels are form/booking-driven, not inbound-call-driven — the marginal attribution value of call tracking is low relative to the added complexity for a two-person team. Revisit only if/when paid inbound-call volume becomes a meaningful share of leads (a P2 item, not P0/P1).

---

## 7. AI CRAWLER POLICY (robots.txt)

**Decision: ALLOW GPTBot (OpenAI), ClaudeBot (Anthropic), PerplexityBot, and Google-Extended.** This is a deliberate AEO decision, not an oversight.

```
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: *
Allow: /
Disallow: /booking-widget/
Sitemap: https://thereimethod.com/sitemap.xml
```
(Path pattern above is illustrative — replace `/booking-widget/` with the actual noindexed widget path once built; this file must not block the funnel bridge pages, only the noindex meta tag does that.)

**The trade-off, stated plainly:** blocking these crawlers keeps your unique phrasing out of AI training/retrieval corpora, but this project's entire objective is AEO — being the answer ChatGPT, Claude, Perplexity, and Google's AI Overviews cite when a Property Climber asks "how do I safely buy a second property in Singapore." Blocking the crawlers that read for citation directly contradicts that goal. The actual competitive moat here is not "hiding the words" — it is the trademarked category (**The Second Property Ladder™**, **Exit Before Entry™**) and the consistent entity anchoring (doc 02) that make Edmund Tan and Cindior Ho the named, citable source, not an anonymous phrase. Allow the crawlers; protect the brand through consistent entity signals, not access restriction.

---

## 8. LLMS.TXT

**Recommendation: implement it, with the caveat stated up front — this is not a ratified standard.** `llms.txt` is a community-proposed convention (first floated 2024) for giving LLMs a clean, curated index of a site's key pages in plain Markdown. As of this writing there is no confirmed evidence that any major AI provider (OpenAI, Anthropic, Google, Perplexity) actually consumes it as a ranking or citation input — treat this as a cheap, low-risk experiment, not a dependency anything else in this project should wait on.

Suggested `https://thereimethod.com/llms.txt` content:
```
# The REI Method

> The REI Method is a Singapore property advisory founded by Coach Edmund Tan
> and Cindior Ho. It created The Second Property Ladder™, a step-by-step
> framework helping Singaporean property owners move safely from their first
> serious property to higher net asset value, more options, and long-term
> family freedom.

## Key pages
- [The Second Property Ladder™](https://thereimethod.com/second-property-ladder): the category hub and the 5-Step framework
- [About Edmund Tan](https://thereimethod.com/edmund-tan)
- [About Cindior Ho](https://thereimethod.com/cindior-ho)
- [Position Map session](https://thereimethod.com/position-map-session): free 45-minute session, the first step
- [FAQ](https://thereimethod.com/second-property-ladder#faq)
```
Keep this file manually in sync with the real sitemap; do not let it drift into an outdated page list.

---

## 9. TECHNICAL PRIORITY LIST (P0 → P2)

| Priority | Action | Owner | Done-criterion |
|---|---|---|---|
| **P0** | Verify GHL Websites' actual custom-code character limit and robots.txt editability [VERIFY items throughout this doc] | Edmund/Cindior (GHL admin, or GHL support ticket) | Written confirmation of both limits, documented back into this file |
| **P0** | Verify Search Console for `singaporerealestateinsider.com`, `6figurepropertyprofits.com`, `thereimethod.com` (§6.1) | Edmund/Cindior | All three properties show "Verified" in GSC before any redirect is touched |
| **P0** | Execute registrar-level 301s: `singaporerealestateinsider.com` and `6figurepropertyprofits.com` → `thereimethod.com`, then run Change of Address tool | Edmund/Cindior (or hired web help) | Both domains resolve to `thereimethod.com` with a 301 (test via curl/redirect-checker); Change of Address submitted in GSC |
| **P0** | Publish site-wide `Organization` + `Professional Service` JSON-LD on `thereimethod.com` home, plus both founder `Person` blocks | Edmund/Cindior (paste from doc 02 §6, with [VERIFY] fields resolved) | Google Rich Results Test shows no errors on all three pages |
| **P0** | Implement noindex + canonical on both vanity-domain bridge pages and all funnel steps | Edmund/Cindior (GHL page settings) | `site:secondpropertyladder.com` and `site:legacylaunch.com.sg` show only the one bridge page each in Google |
| **P0** | Connect Meta ad account in GHL to activate `ad_id`/`campaign_id`/`click_id` auto-population | Edmund/Cindior | Fields populate on a live test lead |
| **P1** | Attach `legacylaunch.com.sg` to Legacy Launch V2 funnel | Edmund/Cindior | Domain resolves to the funnel; SSL active |
| **P1** | Set up GA4 property + cross-domain measurement across `thereimethod.com` + both vanity domains | Edmund/Cindior (or hired help) | GA4 real-time report shows sessions from all three domains without duplicate session counting |
| **P1** | Implement `robots.txt` AI-crawler allow policy (§7) | Edmund/Cindior (or GHL support if not self-editable) | `robots.txt` live at `thereimethod.com/robots.txt` includes all four named user-agents |
| **P1** | Build breadcrumbs + `BreadcrumbList` schema on hub/step/guide templates | Web build (Edmund/Cindior or hired help) | Breadcrumbs visible and validated in Rich Results Test |
| **P1** | Author-box + `author` schema on every published page | Edmund/Cindior (content workflow step) | 100% of live pages have a visible author box linking to a founder page |
| **P2** | Publish `llms.txt` | Edmund/Cindior | File live and matches current sitemap |
| **P2** | Bing Webmaster Tools setup + GSC import | Edmund/Cindior | Bing property verified |
| **P2** | Screaming Frog quarterly audit cadence established | Edmund/Cindior | First audit run and findings logged |
| **P2** | Re-evaluate call tracking need | Edmund/Cindior | Revisit only once inbound-call lead share is measured |

---

## Questions To Clarify

1. Does GHL **Websites** (as distinct from Funnels) expose the same ~8,000-character custom-code limit, and does it expose a fully editable `robots.txt`? Both are unverified assumptions this entire doc's schema-injection and AI-crawler sections depend on.
2. Does GHL Blogs expose a post-level custom-code/header field for per-post JSON-LD, or must schema be inlined in the post body?
3. Does GHL auto-compress uploaded images to WebP, or must every image be pre-converted before upload?
4. What is the current registrar for `singaporerealestateinsider.com` and `6figurepropertyprofits.com`, and does it support native domain forwarding (vs requiring a DNS-level workaround)?
5. Is `thereimethod.com` currently live with any content, and does it already have DNS pointed anywhere (carried over from doc 02 Q3 — this doc cannot finalise the platform build sequence until answered)?

## Dependencies

- **Blocked by `03_DOMAIN_ARCHITECTURE.md` not yet existing** — this doc implements D2–D4 directly from the Master Brief as a stand-in; reconcile §4 and §8's canonical rules with doc 03 once written, and flag any conflict back to the orchestrator rather than silently deferring to either version.
- **Depends on `02_ENTITY_ARCHITECTURE.md`** — every JSON-LD block in §3 is sourced from doc 02 §4/§6 and is gated on the same [VERIFY] items (CEA numbers, GBP details) that block doc 02's Person/Organization schema from publishing.
- **Feeds `04_WEBSITE_SITEMAP_AND_PAGE_ROADMAP.md`** — the schema map (§3) assumes the page inventory doc 04 will formalise; if doc 04 adds/removes pages, update §3's table.
- **Feeds `10_CONTENT_ENGINE_SOP.md`** — the blog workflow (§1.2B) and author-box/dateModified rules (§15–16) should be folded into the content SOP's publish checklist, not run as a separate process.
- **Feeds `12_MEASUREMENT_AND_AUTOMATION_SYSTEM.md`** — the tracking setup (§6) is this doc's contribution to that phase's measurement stack.

## First 5 Actions

1. **File the two [VERIFY] platform questions with GHL support** (custom-code character limit on Websites; robots.txt editability) — every schema and AI-crawler recommendation in this doc assumes an answer.
2. **Verify Search Console for all five domains** (§6.1) before touching any DNS/redirect — this is the one irreversible-if-skipped step in the entire plan.
3. **Execute the two registrar-level 301s** (`singaporerealestateinsider.com`, `6figurepropertyprofits.com` → `thereimethod.com`) once verification is done, then submit Change of Address in GSC.
4. **Publish the site-wide Organization/Person JSON-LD** from doc 02 §6 on `thereimethod.com`'s home and founder pages, and validate with Google's Rich Results Test.
5. **Noindex every funnel step and canonical every bridge page** on `secondpropertyladder.com` and `legacylaunch.com.sg` — the fastest way to prevent duplicate-content dilution before either domain gets meaningful traffic.

---

## Concerns (flagged, not silently changed)

- This doc had to make canonical/redirect calls that were assigned to `03_DOMAIN_ARCHITECTURE.md`, which does not exist yet in this Drive folder. I've implemented D2–D4 directly rather than blocking on doc 03, but the orchestrator should treat §4 and §8/§9 here as provisional until doc 03 is written, and reconcile any divergence rather than letting two documents disagree silently.
- The GHL-platform recommendation (§1) rests on several [VERIFY] assumptions about GHL Websites' technical ceilings (custom-code limit, robots.txt editability, image auto-optimisation) that could not be checked from the research appendix alone. If any of these turn out to be more restrictive than assumed (e.g. no editable robots.txt at all), the AI-crawler-allow decision (§7) may need a workaround (e.g. a Cloudflare-proxied DNS layer in front of GHL solely to serve a custom robots.txt) — flagging this now so it isn't a surprise later.
