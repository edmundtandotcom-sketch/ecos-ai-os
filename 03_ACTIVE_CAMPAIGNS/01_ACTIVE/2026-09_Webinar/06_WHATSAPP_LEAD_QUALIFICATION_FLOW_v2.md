# Thomson Reserve Webinar — WhatsApp Lead Qualification & Booking Flow (v3)
Pre/post-registration WhatsApp conversation flow: qualifies a webinar lead
through Messages 2–5, then transitions into a phone-call booking with
Coach Edmund (Messages 6 onward). v3 fixes a voice inconsistency and
switches Message 7 from an open question to a proactive time offer — see
changelog at the bottom for exactly what changed and why.

Status: v3 — ready to load into whatever CRM/chat tool runs this flow.

## MESSAGE 1 (for reference — establishes the voice everything else must match)

"Hey *{{1}}*, Coach Edmund here.

I've received your interest in joining me for *{{2}} on {{3}}*, so you never buy based on hype, emotion, or pressure.

Did I get the right person?"

**This is first person, personal — Edmund texting directly.** Every message
below is written to match that voice. If a real person other than Edmund
(a team member/assistant) is actually the one sending Messages 2 onward,
that should be disclosed rather than left implicit — see the highlight at
the bottom.

They reply "yes, that's me" → triggers Message 2.

---

MESSAGE 2 OBJECTIVE = PERMISSION + ENGAGEMENT

Get permission to ask quick questions — tied explicitly to giving
relevant insights during the webinar, not just general guidance.

Use one natural variant:

Variant A:
"Is it okay if I ask a couple of quick questions so I can share more relevant insights with you during the webinar?"

Variant B:
"Mind if I ask a couple of quick questions first, so the webinar can be more relevant to your situation?"

Variant C:
"Can I ask a couple of quick questions first, so what you get from the webinar is tailored to you?"

If affirmative → Message 3.

If unclear → repeat Message 2 using another variant.

If they ask a question → answer briefly, then return to Message 2.

If hostile → remain calm and ask what they need directly.

----------------------------------------

MESSAGE 3 OBJECTIVE = BUYER TYPE

Understand buyer stage, tied to why they joined the webinar.

Use one:

Variant A:
"Which best describes why you joined the webinar — buying your first property, upgrading, planning your next move after a sale, or something else?"

Variant B:
"So I can guide you properly — are you buying your first property, upgrading, planning your next move after a sale, or something else?"

Variant C:
"Just so I place you correctly — is this about your first property, an upgrade, your next move after a sale, or something else?"

If answer is vague:

"Got it. Just to place you correctly, which one is closest — first property, upgrading, or after sale, or something else?"

or

Is this mainly for own stay, upgrading, or investment, or something else?

or

Just so I guide you properly — is this for own stay, next move, or investment, or something else?

If FACEBOOK LEAD FORM SUBMITTED TRIGGER already captured this, skip Message 3.

----------------------------------------

MESSAGE 4 OBJECTIVE = MAIN INTEREST DRIVER

Find what they specifically want help with on the webinar. **First person
— matches Message 1's voice** (was incorrectly third person, "Coach
Edmund," in the prior version).

Use one:

Variant A:
"What would you like me to help you solve during the Live Webinar that can benefit you?"

Variant B:
"What's the one thing you're hoping I can help you figure out during the Live Webinar?"

Variant C:
"If I could help you solve one thing on this Live Webinar, what would it be?"

If answer is vague:

"No worries — even a rough idea helps. Is it more about timing, budget, or picking the right move?"

----------------------------------------

MESSAGE 5 OBJECTIVE = PURPOSE OF THE MOVE

Understand what this next move is actually for.

Use one:

Variant A:
"Is this next move mainly for own stay, investment, or for your kids, or something else?"

Variant B:
"Just so I understand — is this for own stay, investment, or planning ahead for your kids, or something else?"

Variant C:
"Would you say this is more for your own stay, an investment, or for your kids' future, or something else?"

If answer is vague:

"No worries — would you say it's more for staying yourself, investing, or planning ahead for your kids?"

----------------------------------------

MESSAGE 6 OBJECTIVE = BOOKING TRANSITION

Invite a phone call. **First person — matches Message 1's voice** (was
incorrectly third person, "with Coach Edmund," in the prior version).

Use only if user shows genuine interest, urgency, confusion, or active timeline.

Use one:

Variant A:
"Based on what you shared, would you like a short phone call with me? You can ask me directly about your situation and plans, and I can help you work through it right away. That could save you a lot of guesswork — sound good?"

Variant B:
"From what you've told me, I think a quick phone call could really help — you can run your situation and plans by me directly, and get my take on the spot. Could save you a lot of guesswork. Sound good?"

Variant C:
"Seems like this is worth a proper conversation. Would you be open to a short phone call with me, so you can ask me about your situation and plans and get help sorting it out right away? Sound good?"

Once Message 6 is sent:

Disable nudges.

Disable timeout follow-ups.

If yes → Message 7.

If no → Message 6A.

----------------------------------------

MESSAGE 6A OBJECTIVE = GRACEFUL EXIT TO WEBINAR

Use only if the reply to Message 6 is "no" or otherwise declines the call.

Use one:

Variant A:
"Sure, no worries — sounds like you're still in the exploring stage for now. I look forward to seeing you at the Live Webinar!"

Variant B:
"No problem at all — totally fine to just explore for now. See you at the Live Webinar!"

Variant C:
"All good — sounds like you're not quite there yet, and that's fine. I'll see you at the Live Webinar!"

Then stop.

----------------------------------------

MESSAGE 7 OBJECTIVE = OFFER TIME SLOTS
*(was TIME CAPTURE — changed from an open question to a proactive offer,
per Edmund's direction: lower friction, and it reads as more prepared/
in-demand than asking the lead to name a time themselves.)*

**Internal check — do this BEFORE sending Message 7, not after:**
Select 2 real available slots, both within the next 2 days, **spaced
apart with a genuine gap between them** (e.g. a morning slot vs. an
evening slot, or a day-1 slot vs. a day-2 slot) — not two options 1–2
hours apart, which isn't really a choice. This replaces the old flow's
"capture a time, then validate availability afterward" step — availability
is now confirmed before the message goes out.

Use one:

Variant A:
"I've got two slots open — [Slot 1] or [Slot 2]. Which works better for you?"

Variant B:
"I have two openings coming up — [Slot 1] or [Slot 2]. Would either of these suit you?"

Variant C:
"Here are two times that could work — [Slot 1] or [Slot 2]. Let me know which one's better for you."

If either slot works → Message 8A.

If neither works → Message 7B.

----------------------------------------

MESSAGE 7B — ALTERNATIVE TIME SLOTS

Use only if neither slot offered in Message 7 works. Offer exactly 2
alternative slots — same rule as Message 7: real availability, spaced
apart, confirmed before sending.

Use:

"No worries, here are a couple more options:

[Alt Slot 1]

[Alt Slot 2]

Let me know if either of these works for you."

If one of these works → Message 8A.

If neither works → end scheduling attempt for now, using:

"No worries, let's leave it for now. Just message me here whenever a time works better for you, and we'll sort it out."

Then stop.

----------------------------------------

MESSAGE 8A OBJECTIVE = CONFIRMATION

Use:

"That works.

I've locked this in for you. You'll receive a calendar invite with the details shortly."

Then stop.

---

## CHANGELOG — v2 → v3 (2026-09-09)

1. **Voice consistency fix.** Message 1 is first-person ("Coach Edmund
   here... I've received your interest"). Messages 4 and 6 had drifted
   into third person ("Coach Edmund," "with Coach Edmund") — both
   rewritten to first person to match. Message 6A's "we" softened to "I"
   in variants A/C for the same reason (B's "See you at the Live Webinar"
   was already person-neutral, left as is).
2. **Message 7 changed from an open question to a proactive 2-slot
   offer**, both slots within the next 2 days and deliberately spaced
   apart so the choice is real, not two near-identical times. 3 new
   variants (previously had none).
3. **The old capture → check-availability sequence is gone.** Availability
   is now confirmed *before* Message 7 is sent, not checked afterward —
   the "Internal check" note moved from after the question to before it.
4. **Old Messages 8B/8C (the "locked, here are 2 alternatives" /
   "second round of alternatives" chain) are replaced by a single new
   Message 7B**, since Message 7 already front-loads the first offer —
   there's no separate "user proposed a time, it didn't work" step to
   react to anymore. This takes the flow from 3 rounds of back-and-forth
   down to 2 (Message 7's offer, then 7B's alternates) before gracefully
   ending the scheduling attempt. Message 8A (confirmation) is unchanged.

## HIGHLIGHT — worth a decision before this goes live

If Messages 2 onward are actually sent by a team member or an automated
assistant rather than Edmund himself, first-person phrasing across the
whole thread ("I," "me," "with me") will read as Edmund personally
texting when he isn't — which could land badly if the lead later realizes
otherwise (e.g. on the actual phone call, when a different name shows up).
Two honest options: (a) it genuinely is Edmund's own number/inbox running
this flow, in which case first person is correct and nothing further is
needed, or (b) a team member sends it, in which case either Message 1
should briefly disclose that ("Coach Edmund here — well, technically his
team, helping set this up!") or the voice should shift to a clearly
labeled assistant persona rather than impersonating Edmund directly. Not
a copy question — a decision about who's actually operating this number.
