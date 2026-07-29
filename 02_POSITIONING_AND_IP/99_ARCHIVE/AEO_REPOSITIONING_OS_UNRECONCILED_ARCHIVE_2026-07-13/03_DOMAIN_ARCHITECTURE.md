# 03 — DOMAIN ARCHITECTURE
**Phase 3 · AEO Repositioning OS · Client Edition (Singapore property advisory)**
**Owner:** Domain Architecture builder · **Date:** 9 July 2026 · **Status:** Built on LOCKED decisions D2–D4. Every quantitative claim and traffic/backlink assumption is marked [VERIFY].

---

## Executive summary

This phase turns six owned domains into one clean authority-and-funnel architecture. The ruling: **one authority domain earns everything** (`thereimethod.com`, per LOCKED D2), **two vanity domains host funnels** (`secondpropertyladder.com` for the diagnostic, `legacylaunch.com.sg` for Legacy Launch V2 — the latter currently has no domain attached and must be connected now), **two domains fold into the authority via 301** (`singaporerealestateinsider.com`, `6figurepropertyprofits.com`), and **one is parked** (`familylegacy.com.sg`). The design deliberately consolidates link equity and entity signals on a single host to avoid authority-splitting, AI/LLM entity confusion, and duplicate-content dilution, while keeping conversion funnels off the authority domain's index so they never compete for or pollute organic real estate. Funnel steps are noindexed; a single indexable **bridge page** per vanity domain carries a canonical to its `thereimethod.com` equivalent so the vanity URL can be shared and verified without creating a doorway. All 301s are gated behind three preconditions — Search Console verification, a backlink export, and a live-traffic check — because a redirect executed before those checks can silently discard ranking pages and inbound links. Email trust is anchored to `admin@thereimethod.com` with SPF/DKIM/DMARC on the authority domain only; vanity domains never send cold. The companion `Domain_Redirect_Map.csv` lists every actionable redirect, canonical, noindex, park and DNS task with preconditions and priority.

---

## 1. Evaluation criteria (how each verdict was reached)

Every domain is scored against nine criteria drawn from D2, D8 (no-spam doctrine) and Google Search Central guidance on site moves, canonicalisation and doorway pages:

1. **Authority strengthening vs splitting** — does the domain concentrate link equity/entity signals on `thereimethod.com`, or fragment them across hosts?
2. **AI / LLM entity confusion** — will answer engines (Google AI Overviews, ChatGPT, Perplexity) struggle to bind the entity "The REI Method / The Second Property Ladder™ / Coach Edmund Tan & Cindior Ho" to one canonical home if multiple domains present overlapping brand claims?
3. **Duplicate content** — does the domain risk publishing the same category/founder content on two hosts?
4. **Doorway-site risk** — is the domain a thin gateway whose only purpose is to funnel to another destination (a Google spam-policy violation)?
5. **Active traffic [VERIFY]** — does the domain currently receive organic/direct/paid traffic that a redirect must preserve?
6. **Backlinks [VERIFY]** — does the domain hold inbound links whose equity must be forwarded, not dropped?
7. **Tracking** — can pixels, GA4 and GHL attribution be cleanly attached and kept consistent across ad click-through?
8. **Clear role** — does the domain have exactly one job a human and a crawler can both understand?
9. **Future-architecture fit** — does keeping it serve the end-state (authority hub + campaign funnels + parked reserve), or is it legacy baggage?

---

## 2. Domain Decision Table

| Domain | Role | Verdict | Rationale (against criteria) | Key risks | Sequencing — check BEFORE acting |
|---|---|---|---|---|---|
| **thereimethod.com** | Authority hub: founder profiles (Edmund Tan, Cindior Ho), The Second Property Ladder™ category hub, 5-Steps pages, Exit Before Entry™ page, case studies, guides, FAQ, tools. | **Keep — authority** (LOCKED D2) | Concentrates all link equity + entity signals on one host (crit 1). Single canonical home removes AI entity confusion (crit 2). Only domain permitted to publish evergreen content (crit 3 — no duplication). Clear role, perfect future fit (crit 4,8,9). Email identity already `admin@thereimethod.com` (crit 7). | Platform choice still open (see §7). Must be live before any 301 points at it, or redirects land on a dead/placeholder host. | Confirm host is live and serving a real homepage + category hub URL. Stand up `/second-property-ladder` and `/legacy-launch` targets before pointing canonicals/301s at them. |
| **secondpropertyladder.com** | Vanity funnel host for the "Which Step of The Second Property Ladder Are You On?" 14-question diagnostic. | **Keep — vanity** (LOCKED D3) | Exact-match to the category — high ad-trust and click-through consistency (crit 7). Funnel lives off the authority index so it never competes with the hub (crit 1,3). One indexable bridge page canonical to hub prevents doorway/duplicate (crit 3,4). Clear single role (crit 8). | Doorway/duplicate risk IF the whole funnel is indexed — mitigated by noindex + single canonical bridge (see §4–5). Exact-match domain can look thin if it hosts nothing but a redirect — the bridge page must carry real, answer-complete intro content. | Confirm domain resolves and is attachable to GHL. Do NOT let GHL auto-index every funnel step. Build bridge page content before publishing. |
| **legacylaunch.com.sg** | Vanity funnel host for the **Legacy Launch V2** funnel (`ILuFW2Qv6l9UIXk6lUIM`) — currently **NO domain attached**. | **Keep — vanity; ATTACH NOW** (LOCKED D3) | Campaign-specific host for the new-launch line; `.com.sg` signals local Singapore trust (crit 7,8). Keeps the campaign funnel off the authority index (crit 1,3). Bridge page canonical to a `thereimethod.com/legacy-launch` campaign page (crit 3,4). | Funnel is live in GHL with no domain — it is currently reachable only via the GHL preview/whitelabel URL, which is not ad-safe or brand-safe. Footer currently reads "© Singapore Real Estate Insider" and carries no CEA licence line (compliance gap, D7). | Attach domain in GHL (add domain → DNS records). Fix footer entity block + add CEA compliance line BEFORE running paid traffic. Verify domain in Meta before ads. |
| **singaporerealestateinsider.com** | Legacy domain matching the YouTube media brand. The media brand lives on YouTube, not on its own site (LOCKED D1, D4). | **301 → thereimethod.com** (LOCKED D4) | Keeping it as a live site would split authority and create AI entity confusion between "Singapore Real Estate Insider" (media sub-brand) and "The REI Method" (business) (crit 1,2). A separate site duplicates founder/category content (crit 3). 301 forwards any equity to the hub (crit 1,6). | If the domain ever hosted pages with backlinks/traffic, a blind catch-all 301 to the homepage discards page-level equity and rankings. Brand token "Singapore Real Estate Insider" must stay valid on YouTube — do not retire the *name*, only the *website*. | **Before 301:** verify property in Search Console; export backlink profile [VERIFY]; export top pages + traffic [VERIFY]; map any high-value old paths to closest hub equivalents; then implement 301 and, if a full site existed, submit Change of Address in GSC. Keep redirect ≥12 months. |
| **6figurepropertyprofits.com** | Legacy income-claim domain. | **Retire + 301 → thereimethod.com** (LOCKED D4) | Name is an income claim — reputational and CEA-advertising compliance liability (D7). No place in a private-wealth-advisory positioning (crit 8,9). 301 preserves any residual equity while removing the brand from public use (crit 1,6). | Compliance risk if it stays reachable with any income-claim content. Possible spammy backlink profile from an income-claim era — audit before forwarding equity. | **Before 301:** GSC verify; **audit backlinks for toxic/spam links** (do not forward a poisoned profile — disavow if needed) [VERIFY]; export any traffic [VERIFY]; then 301 catch-all to hub homepage. Never reuse the name in ads/social. |
| **familylegacy.com.sg** | Reserve domain; possible future campaign host. | **Park (renew, no content)** (LOCKED D4) | No current role; building on it would create a doorway/thin site and split authority (crit 1,4). Reserving it protects a future `.com.sg` campaign option and blocks squatters (crit 9). | Parking pages from some registrars serve ad-laden placeholder content — that can index as thin/spam. Must serve a minimal branded holding page with `noindex`, or a blank/registrar-park with no ads. | Renew registration. Point to a `noindex` holding page (or leave unresolved). Do NOT build, do NOT link from authority. Revisit only if a future campaign claims it. |

---

## 3. Redirect Map (precise, host + path level)

All redirects are permanent (**301**), implemented at both apex and `www`, forcing **HTTPS**. Destinations are absolute `https://` URLs. Where an old path's equivalent is unknown, the default is a catch-all to the hub homepage, with a [VERIFY] task to map real historical paths from Search Console before go-live (a catch-all-to-homepage move loses page-level ranking signals and should be the fallback, not the plan).

| # | Source (host + path) | → Destination | Type | Notes |
|---|---|---|---|---|
| R1 | `singaporerealestateinsider.com/*` (apex, catch-all) | `https://thereimethod.com/` | 301 | Fallback only. Replace with path-level rules once GSC top-pages export exists [VERIFY]. |
| R2 | `www.singaporerealestateinsider.com/*` | `https://thereimethod.com/` | 301 | www → apex → authority, single hop preferred (avoid chained redirects). |
| R3 | `singaporerealestateinsider.com/<old-path>` (per real historical URL) | `https://thereimethod.com/<closest-equivalent>` | 301 | [VERIFY] whether this site ever hosted content. If yes, map each high-traffic/high-backlink path individually before R1 catch-all applies. |
| R4 | `6figurepropertyprofits.com/*` (apex, catch-all) | `https://thereimethod.com/` | 301 | After backlink toxicity audit. Disavow spam links rather than forward them [VERIFY]. |
| R5 | `www.6figurepropertyprofits.com/*` | `https://thereimethod.com/` | 301 | Single hop. |
| R6 | `6figurepropertyprofits.com/<old-path>` | `https://thereimethod.com/<closest-equivalent>` | 301 | Only if legitimate historical pages with equity exist [VERIFY]; otherwise R4 catch-all. |
| R7 | Any `http://` on both retired domains | `https://` equivalent then to hub | 301 | Enforce HTTPS at the edge (registrar/Cloudflare) so there is one redirect hop, not two. |

**Redirect hygiene rules:** one hop only (avoid `http→https→apex→destination` chains — collapse at the edge); keep 301s live a minimum of 12 months (Google Search Central — "Redirects and Google Search" recommends ≥1 year for a site move to fully transfer signals); do not chain a retired domain through another retired domain.

---

## 4. Canonical Map (vanity funnel → authority equivalent)

Each vanity domain exposes **exactly one** indexable page — the **bridge page** — which is genuinely answer-complete (real intro content about the diagnostic or the campaign, not a bare redirect) and carries a `rel="canonical"` pointing to its evergreen equivalent on `thereimethod.com`. Every other funnel step is `noindex` (see §5). This gives the vanity URL a shareable, ad-verifiable, non-thin front door while the authority page remains the single canonical home for the topic — satisfying D8 (no doorway sites) and Google's canonicalisation guidance.

| Vanity domain | Indexable bridge page | Canonical target (self-referencing? No — cross-domain) | Rationale |
|---|---|---|---|
| `secondpropertyladder.com` | `secondpropertyladder.com/` (home/bridge) | `https://thereimethod.com/second-property-ladder` (category hub) | The hub is the citable answer for "what is the Second Property Ladder". The bridge introduces the diagnostic and points equity to the hub. |
| `legacylaunch.com.sg` | `legacylaunch.com.sg/` (home/bridge) | `https://thereimethod.com/legacy-launch` (campaign page under the hub) | Campaign page on the authority domain is canonical; the vanity bridge is the ad landing entry. |

**GHL mechanics (practical level).** GHL funnel pages expose per-page **SEO / Meta Data** settings and a per-page **head/custom-code** slot; there is no first-class "canonical URL" field reliable across all GHL versions, so implement the canonical explicitly:

1. In the GHL **Funnel → Page → Settings → SEO Meta Data**, set the bridge page's title/description (answer-complete, LOCKED vocabulary — "Step", "Position Map", never banned words).
2. In the bridge page **Tracking Code → Head**, inject: `<link rel="canonical" href="https://thereimethod.com/second-property-ladder">` (or the `/legacy-launch` target). This is the authoritative signal; GHL will otherwise self-canonicalise the vanity URL.
3. Leave the bridge page **indexable** (do NOT add a noindex meta on the bridge).
4. On every other step (`/strategy-call`, `/schedule-call`, quiz question screens), inject `<meta name="robots" content="noindex, nofollow">` in the page head, or toggle the page's SEO/index setting off where the version exposes it. Robots meta in the page head is the reliable cross-version method.
5. Confirm the funnel's global setting does not force a sitemap listing of every step; if GHL auto-generates a funnel sitemap, ensure only the bridge appears (or submit only the authority sitemap to Search Console and let noindex handle the rest).

---

## 5. Noindex Map (every known funnel path + embed widget)

Booking widgets and funnel steps must never be indexed. The rule: **only bridge pages are indexable; everything transactional is `noindex, nofollow`.** Widget/booking URLs on `app.theintellia.com` (GHL whitelabel) and `api.leadconnectorhq.com` are third-party embed hosts we do not fully control, but we (a) embed them via iframe on noindexed steps and (b) never expose their standalone URLs as landing pages or links.

| Host | Path / asset | Index directive | Method | Notes |
|---|---|---|---|---|
| `secondpropertyladder.com` | `/` (bridge) | **index, follow** | Leave default + canonical | Only indexable page on this domain. |
| `secondpropertyladder.com` | `/quiz`, `/start`, quiz question steps, `/result` | noindex, nofollow | Robots meta in page head | 14-question diagnostic screens (Checkpoints/Gates). Never index. |
| `secondpropertyladder.com` | `/strategy-call`, `/schedule-call`, `/thank-you` | noindex, nofollow | Robots meta in page head | Opt-in + booking + confirmation. |
| `legacylaunch.com.sg` | `/` (bridge) | **index, follow** | Leave default + canonical | Only indexable page on this domain. |
| `legacylaunch.com.sg` | `/strategy-call` (page `4JECqA37xZnvFFNi3DTa`) | noindex, nofollow | Robots meta in page head | Legacy Launch V2 Step 1 opt-in. |
| `legacylaunch.com.sg` | `/schedule-call` | noindex, nofollow | Robots meta in page head | Legacy Launch V2 Step 2 booking. |
| `legacylaunch.com.sg` | `/thank-you` / confirmation | noindex, nofollow | Robots meta in page head | Post-booking. |
| `app.theintellia.com` | Calendar widget `34KkdVJncaYiuAOjE0FP` ("New Launch/Family Legacy Ladder") standalone URL | noindex (do not expose) | Embed via iframe only; never link the standalone widget URL | GHL whitelabel booking host. Widget carried inside a noindexed `/schedule-call` step. |
| `app.theintellia.com` | Diagnostic/other whitelabel funnel preview URLs | noindex (do not expose) | Never use whitelabel preview URL as an ad landing page | Ads point only at the vanity bridge/opt-in, not the whitelabel host. |
| `api.leadconnectorhq.com` | Booking/form widget embed URLs (LeadConnector) | noindex (do not expose) | Iframe embed only; no standalone linking; no sitemap entry | LeadConnector widget backend; not a landing surface. |
| `familylegacy.com.sg` | `/` holding page | noindex, nofollow | Robots meta on park page | Parked; branded holding or registrar park with no ads. |

**Verification step (post-implementation):** after publishing, fetch each URL and confirm the `robots` meta and canonical resolve as intended (view-source or Search Console URL Inspection). Do this once per funnel before ad spend.

---

## 6. Campaign Domain Usage Rules

**When a future campaign earns a vanity domain vs a path on the authority domain:**

- **Default to a path on the authority domain.** New evergreen content (a guide, a case study, a founder page, the category hub) always lives on `thereimethod.com/<path>` so it compounds authority. This is the D2/D8 default.
- **A vanity domain is justified only when ALL of the following hold:** (a) it is a *paid-traffic funnel*, not evergreen content; (b) it needs to stay off the authority index so it never competes with or dilutes organic pages; (c) exact-match or campaign-match naming measurably lifts ad trust/click-through (e.g. `secondpropertyladder.com` matching the diagnostic, `legacylaunch.com.sg` matching the campaign); and (d) it will carry a proper bridge + noindex + footer entity block. If a campaign does not meet all four, it becomes a noindexed funnel *path* under a subdomain of the authority (e.g. `go.thereimethod.com/...`) or a folder, not a new domain.
- **Do not mint new domains per campaign.** Two vanity domains is the ceiling for now. More domains = more authority splitting, more AI entity confusion, more compliance surfaces. `familylegacy.com.sg` is the only reserve; a new campaign should claim it before any brand-new registration is considered.

**Ad-platform considerations:**

- **Meta domain verification per domain.** Verify each domain that appears as a click-through destination in Business Manager (DNS TXT or meta-tag). `secondpropertyladder.com` and `legacylaunch.com.sg` must each be verified before running Advantage+/conversion campaigns, so Aggregated Event Measurement and domain-level controls work. The authority domain should also be verified if any ad ever links to it.
- **Click-through consistency.** The domain a user sees in the ad's display/destination URL must match the landing host (no cross-domain bounce between click and page). Ad → `secondpropertyladder.com` bridge/opt-in → GHL steps on the same host → booking widget embedded (not navigated to). No mid-funnel host switch that breaks pixel continuity or trust.
- **Tracking parity.** The Meta pixel + GHL attribution fields (`ad_id`, `ad_name`, `campaign_id`, `campaign_name`, `utm_source`, `click_id` — already present in the sub-account) must fire on the vanity host. Set the pixel per vanity domain; confirm events (`quiz_start … capture_submitted` for the diagnostic; opt-in/booking for Legacy Launch V2) are received before scaling.

**Mandatory vanity-funnel footer rule (every vanity funnel page, including noindexed steps):** each vanity funnel footer MUST carry:
1. **The REI Method entity block** — business name "The REI Method", founders "Coach Edmund Tan & Cindior Ho", and a link to the authority domain (`https://thereimethod.com`) and to the founder pages. This binds the vanity funnel to the canonical entity for both humans and answer engines and replaces the current, incorrect "© Singapore Real Estate Insider" footer.
2. **CEA/PropNex compliance line** — registered names + CEA registration numbers + PropNex agency name and licence number, per CEA advertising guidelines. **[VERIFY numbers — CEA reg nos for Edmund and Cindior + PropNex licence no. are not yet on file].** Until supplied, ship a placeholder block flagged for PropNex compliance review — do not run paid traffic without it.
3. Replace the compliance-risk line **"This is advisory, not agency"** with **"Advisory-first. We plan the sequence before any transaction."** (per D7).

---

## 7. Final Domain Architecture (end-state)

```
                         ┌─────────────────────────────────────────────┐
                         │            thereimethod.com                  │
                         │        AUTHORITY HUB (indexable)             │
                         │  /  · /about (Edmund Tan) · /cindior-ho      │
                         │  /second-property-ladder  (category hub)     │
                         │  /the-5-steps · /exit-before-entry           │
                         │  /case-studies · /guides · /faq · /tools     │
                         │  /legacy-launch  (campaign page)             │
                         │  Email identity: admin@thereimethod.com      │
                         └───────▲───────────────▲──────────▲──────────┘
                                 │ 301           │ 301      │ canonical + footer link
              ┌──────────────────┘               │          └────────────────────┐
              │                                   │                               │
  singaporerealestateinsider.com      6figurepropertyprofits.com                  │
   (301 → hub; name stays on          (RETIRE + 301 → hub;                        │
    YouTube only, not a website)       income-claim liability)                    │
                                                                                  │
        ┌─────────────────────────────────────────────┬───────────────────────────┘
        │ VANITY FUNNEL (canonical → hub)              │ VANITY FUNNEL (canonical → hub)
        ▼                                               ▼
  secondpropertyladder.com                        legacylaunch.com.sg
   /            (bridge, INDEX, canonical→hub)      /            (bridge, INDEX, canonical→hub)
   /quiz…       (noindex)                           /strategy-call (noindex, page 4JECqA37…)
   /strategy-call /schedule-call (noindex)          /schedule-call (noindex)
   Diagnostic "Which Step Are You On?"              Legacy Launch V2  (ILuFW2Qv6l9UIXk6lUIM)
        │  embeds ▼                                        │  embeds ▼
        └────────────── app.theintellia.com / api.leadconnectorhq.com ──────────────┘
                        (GHL whitelabel booking + form widgets — iframe only, noindex, never linked standalone)

  familylegacy.com.sg  →  PARKED (renew, noindex holding page, no content, no links)
```

**DNS / hosting notes.**

- **Funnels (both vanity domains) → GHL.** Attach `secondpropertyladder.com` and `legacylaunch.com.sg` inside GHL (Sites → Domains → add domain → apply the DNS records GHL issues: typically a CNAME/A record at the registrar). `legacylaunch.com.sg` has NO domain attached today — this is the highest-priority connection task so the live V2 funnel stops depending on the whitelabel preview URL.
- **Retired domains → registrar/edge 301.** Implement R1–R7 at the registrar or a Cloudflare zone (edge redirect rules) so the redirect works without hosting a site. Force HTTPS and apex+www at the edge to keep to one hop.
- **Parked domain → minimal holding.** `familylegacy.com.sg`: registrar park with ads OFF, or a one-page `noindex` holding page. No build.
- **Authority site platform — recommendation (final decision deferred to doc 11 per brief).** The team lives in GHL, but the authority domain's job is AEO/SEO: granular JSON-LD (Person, Organization, Article, FAQPage, BreadcrumbList), a real blog taxonomy, fast Core Web Vitals, and citable, answer-complete pages. Options and my recommendation:
  - **GHL Websites/Blogs** — lowest friction (team already there), but limited/awkward JSON-LD control, weaker blog taxonomy and schema flexibility, and it co-mingles the authority site with the same sub-account that runs Changi Green (mitigate via the sub-account split recommended in docs 06/12).
  - **WordPress (managed hosting)** — full schema control (RankMath/Yoast + custom JSON-LD), mature blog/taxonomy, non-developer editability. Cost: security/maintenance overhead a 2-person non-technical team must carry.
  - **Astro / static** — best performance and total schema control, but needs a developer for every content change; only viable if a developer owns the site.
  - **ORCHESTRATOR RULING (reconciled with doc 11, which owns this decision):** authority hub launches on **GHL Websites** — the team's ability to actually operate the site outweighs WordPress's schema flexibility, and doc 11 provides the GHL implementation checklist (schema via per-page head injection, blog workflow, embeds). **Migration triggers to WordPress are documented:** if GHL's custom-code limits block required JSON-LD, if blog scale (>100 posts) makes taxonomy unmanageable, or if Core Web Vitals stay in "poor" after optimisation, migrate — URL structure in doc 04 is platform-neutral to keep that door open. Funnels stay in **GHL**; retired domains on **edge 301s**. This section's original WordPress preference is preserved above as the documented trade-off, not the decision.

---

## 8. Email / domain trust note

- **Single sending identity:** `admin@thereimethod.com` is the authority-domain mailbox and the only cold/nurture sending identity. This matches the GHL sub-account email already on file.
- **Authentication on `thereimethod.com`:** publish **SPF** (authorising GHL/LeadConnector's sending infrastructure and any other ESP used), **DKIM** (signing key for the sending platform), and **DMARC** (start `p=none` for monitoring, then move to `p=quarantine`/`p=reject` once aligned). Deliverability and answer-engine trust both benefit from a single, authenticated sending domain that matches the entity.
- **Never send cold from vanity domains.** `secondpropertyladder.com` and `legacylaunch.com.sg` are funnel hosts, not sending domains — sending from them fragments domain reputation and undermines the single-entity signal. Transactional funnel emails (booking confirmations) should send from the authenticated authority domain or a clearly-scoped subdomain of it (e.g. `mail.thereimethod.com`) with its own SPF/DKIM alignment, never from a vanity `.com`/`.com.sg`.
- **Retired domains:** once 301'd, they hold no mailboxes and send nothing. Keep an SPF `-all` (hard fail) or a null MX on retired domains so nobody can spoof mail from them.

---

## Questions To Clarify

1. **[VERIFY] Is `thereimethod.com` currently live with any content, and does a Search Console / GA4 property exist for it or any other domain?** Redirect targets and the platform decision depend on this.
2. **[VERIFY] Which domains have real backlinks and live traffic?** Specifically `singaporerealestateinsider.com` and `6figurepropertyprofits.com` — need a Search Console/Ahrefs export before any 301, plus a toxic-link audit on the income-claim domain.
3. **[VERIFY] Did `singaporerealestateinsider.com` ever host a website with real pages?** If yes, we need the top-URLs export to build path-level 301s instead of a catch-all.
4. **[VERIFY] CEA registration numbers for Edmund and Cindior + PropNex agency licence number** for the mandatory footer compliance block — blocks paid traffic on both vanity funnels.
5. Confirm registrar/DNS access (and whether a Cloudflare zone exists) to implement edge 301s and GHL domain attachment.
6. ~~Platform decision for the authority hub~~ — RESOLVED: GHL Websites for phase 1 with documented WordPress migration triggers (see §7 ruling and doc 11).
7. Does GHL currently expose a canonical-URL field on this account's funnel pages, or must canonicals be injected via head code? (Affects §4 implementation exactly.)

## Dependencies

- **Doc 02 (Entity Architecture)** — the entity block/`sameAs` set and founder-page URLs that the vanity footers and the hub must reference.
- **Doc 04 (Website Sitemap & Page Roadmap)** — the exact hub slugs (`/second-property-ladder`, `/legacy-launch`, founder pages) that canonicals and 301s point at must exist before those redirects/canonicals go live.
- **Doc 06 (Funnel Ecosystem Audit)** — full enumeration of every funnel step/URL feeds the Noindex Map; the diagnostic funnel (`spl_*` fields, not yet built) must be built before its noindex/canonical rules apply.
- **Doc 11 (Technical AEO/SEO Checklist)** — authority-site platform decision, sitemap/robots submission, schema implementation.
- **External:** registrar/DNS access; Search Console + Ahrefs (or equivalent) for the [VERIFY] backlink/traffic exports; Meta Business Manager for domain verification; PropNex compliance for CEA numbers.

## First 5 Actions

1. **Attach `legacylaunch.com.sg` to the live Legacy Launch V2 funnel in GHL** (add domain → apply DNS records), then fix the footer: swap "© Singapore Real Estate Insider" for The REI Method entity block + authority link, add the CEA compliance placeholder, and replace "This is advisory, not agency" with "Advisory-first. We plan the sequence before any transaction." (Highest priority — stops a live funnel depending on the whitelabel preview URL.)
2. **Verify all six domains in Search Console** and pull backlink + top-page + traffic exports for `singaporerealestateinsider.com` and `6figurepropertyprofits.com` [VERIFY]. Do this BEFORE any 301.
3. **Stand up the authority targets** `https://thereimethod.com/second-property-ladder` and `/legacy-launch` (at least placeholder-canonical live pages) so canonicals and 301s have real destinations.
4. **Implement the 301s** (R1–R7) at the registrar/edge once step 2 exports confirm the path map; run the toxic-link audit on `6figurepropertyprofits.com` and disavow before forwarding equity.
5. **Set noindex + canonical across both funnels** per §4–5, verify each URL's robots/canonical resolves, then **verify both vanity domains in Meta** and confirm pixel/attribution parity before ad spend. Park `familylegacy.com.sg` on a noindex holding page.

---

## Concerns (flagged, not silently changed)

- **Doorway-site line to walk carefully:** `secondpropertyladder.com` is an exact-match domain whose only content is a bridge page + noindexed funnel. That is defensible under D8 *only if* the bridge page is genuinely answer-complete (real intro to the diagnostic and the category) rather than a thin redirect shell. If it ends up as a bare gateway, it edges toward Google's doorway-page definition. Recommend the bridge carry a substantive summary of "the 5 Steps / which step are you on" with the canonical to the hub.
- **`singaporerealestateinsider.com` 301 vs the media brand:** the *name* remains valid and in active use on YouTube (`@singaporerealestateinsider`, ~600+ videos [VERIFY]). Redirecting the *website* is correct, but ensure nothing in schema/`sameAs` implies the website is the media brand's home — the YouTube channel is. Coordinate with doc 02.
- **Whitelabel host indexing:** we do not control `app.theintellia.com` / `api.leadconnectorhq.com` robots policy. The mitigation is procedural (iframe-only, never link/expose standalone widget URLs). If GHL ever exposes these as crawlable standalone pages, they could index outside our control — worth a periodic `site:` check.
- **Timezone note (not domain-scope but adjacent):** GHL sub-account timezone is `Asia/Kuala_Lumpur`; it should be `Asia/Singapore`. Flagged for the ops/funnel owner.
