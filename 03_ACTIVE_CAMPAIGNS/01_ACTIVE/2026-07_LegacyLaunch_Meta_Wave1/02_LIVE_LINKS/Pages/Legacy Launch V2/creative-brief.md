# Legacy Launch — New Funnel Creative Brief (v2 page)

## Business context
- Brand: **Legacy Launch** (legacylaunch.com.sg) — Singapore new-launch property advisory run by **Edmund Tan & Cindior Ho** ("Coach Edmund & Cindior").
- Framework/IP: **New Launch Ladder™**, "Buy-Not-to-Stay", "Exit-First Strategy".
- Offer: free **New Launch Strategy Call** (1 hr) — only for buyers actively planning a purchase in the next 3–6 months.
- Positioning: serious advisory for buyers planning their NEXT property move (exit-first, data-driven, portfolio thinking) — explicitly NOT a typical property-agent page. Anti-hype, anti-pressure, disqualification-led.
- Audience: Singapore private-property owners / HDB upgraders with ~$1M+ budgets, skeptical of agents, planning within 3–6 months. Sophisticated, numbers-driven.

## Funnel architecture (2 steps, NEW funnel — never touch existing)
1. **Step 1 — Opt-in landing page** (the main build). All CTAs open/scroll to a short qualifying opt-in form (name, email, phone, buying timeline, current property status). Submit → Step 2.
2. **Step 2 — Booking page**: brief reinforcement header + embedded GHL calendar (ID `34KkdVJncaYiuAOjE0FP`, widget URL `https://app.theintellia.com/widget/booking/34KkdVJncaYiuAOjE0FP`) + "what happens on the call" recap.
- Location ID: `cyeYxFVQE1l73kO6S6Lx`. Whitelabel domain: `app.theintellia.com`.

## Design direction — "private-wealth advisory"
- Deep navy/charcoal base (#0B1D33-ish), warm off-white/ivory sections, champagne-gold accents (#C6A35D-ish). NO red urgency bars.
- Elegant serif for headlines (e.g., Playfair Display / Cormorant Garamond via Google Fonts), clean humanist sans for body (e.g., Inter / Source Sans 3).
- Generous whitespace, editorial layout, thin gold rules/dividers, data presented like a fund factsheet (stat blocks, fine lines), muted photography treatment.
- Feels like: boutique private bank / family office memo. NOT: ClickFunnels gold-button hype.
- Mobile-first: sticky bottom CTA bar on mobile, short sections, readable at 16px+.

## Approved claims & proof (use verbatim/sharpened, all approved by owner)
- We disqualify 90% of projects. Map your next 2–3 property moves before you buy.
- $160,014,029 collectively invested in exit-ready new launch units. 100+ buyers guided. 2,000+ YouTube subscribers, 600+ videos.
- Case studies:
  1. **Edmund Tan & Cindior Ho** — own portfolio: 10+ yrs in <$600K HDB → Tre Ver 2BR $1.05M→sold $1.28M → $3M property (<4 yrs); Parc Clematis 2BR $1.15M→sold $1.525M (3 yrs); portfolio $5M+. "This is our own portfolio."
  2. **Edward & Rose** — >$500K gains in 4 years, crossed $3.5M NAV by skipping the "comfort upgrade".
  3. **MoK & Jine** — 15 yrs in ~$600K 4-room HDB → split into 2×3BR (stay ~$1.2M + rental ~$1M), rental offsets loans, 8 yrs reserves kept, >$235K gains, >$3M portfolio.
  4. **Win/Esther & Family** — fearful/lost → 1-on-1 plan → data-driven filtering → confidently bought $1.8M unit aligned with future plans.
- 8 testimonial headlines (guesswork→framework, $1.5m purchase clarity, exit path, total clarity, real numbers not sales talk, math over hype, which launches to avoid, growth not guesswork).
- What happens on the call: map current position (equity/timeline/constraints) → which launches to avoid immediately → 1–2 strategic entry options → exit plan before commitment. "You'll leave knowing what to do next even if we don't work together."
- Disqualification: NOT for browsers / not buying in 3–6 months / opinion shoppers. FOR: shortlisted buyers, avoiding $200K+ mistakes, serious about next move.
- Compliance footer: results-vary disclaimer + PDPA 2012 notice + © 2026 Singapore Real Estate Insider.

## Copy principles
- Lead with the buyer's fear: buying a unit you can't exit ("dead-end property", "forever home by accident").
- Advisory voice: calm, precise, numbers-first. No exclamation marks, no scarcity timers. Authority through specificity.
- Disqualification as status: the reader must qualify, we're not chasing them.
- CTA language for a 2-step form flow, e.g. "Check If You Qualify →" / "Request Your Strategy Call" (button opens form), never "Submit".

## Deliverables
1. `copy-deck.md` — final copy, section by section.
2. `legacy-launch-v2-optin.html` — self-contained (inline CSS/JS, Google Fonts <link> ok) landing page, wrapped in scoped class `.llv2` to survive GHL. No external images required (use CSS/SVG treatments and initials-avatars; image slots marked with placeholder swap instructions).
3. `legacy-launch-v2-booking.html` — Step 2 with calendar iframe embed.
4. `ghl-build-guide.md` — exact steps to create new funnel + paste custom code + wire form submit → step 2, plus native-rebuild notes for replication.
