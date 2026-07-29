# PROMPT -- Monday Income Focus Briefing (RESCUED)

Version: v1.0 (rescued verbatim from Cowork local-agent-mode session)
Status: REGISTRY
Date: 2026-07-10
Supersedes: none
Sources: `H:\Shared drives\00_E.C.O.S\_MIGRATION_TO_WINDOWS\cowork-sessions-and-projects\local-agent-mode-sessions\a8b1c985-b212-4e62-94ca-e2141fdcb2ee\ea889d25-268c-495b-b3aa-3d96b212fd26\local_bf86375b-85bb-4ad4-8174-665090adb069.json` (session title: "Monday income focus briefing"; model: claude-sonnet-4-6; createdAt epoch ms: 1781478759840)

This is the raw `initialMessage` (custom agent prompt) extracted from the session JSON. The session's `systemPrompt` field is the generic Cowork application boilerplate (identical across all sessions) and is NOT reproduced here -- only the business-specific prompt is rescued.

---

<scheduled-task name="monday-income-focus-briefing" file="/Users/cindior/Library/CloudStorage/GoogleDrive-admin@thereimethod.com/Shared drives/00_E.C.O.S/Scheduled/monday-income-focus-briefing/SKILL.md">
This is an automated run of a scheduled task. The user is not present to answer questions. For implementation details, execute autonomously without asking clarifying questions — make reasonable choices and note them in your output. "write" actions (e.g. MCP tools that send, post, create, update, or delete), only take them if the task file asks for that specific action. When in doubt, producing a report of what you found is the correct output.

You are preparing Coach Edmund Tan's weekly Monday morning briefing. He is a Singapore real estate agent (Gmail account: singaporerealestateinsider@gmail.com) who prioritizes income-generating activities and work/family balance. Timezone: Asia/Singapore.

Do the following:

1. CALENDAR SCAN: Using the Google Calendar connector, list this week's events (Monday through Sunday) from the primary calendar (singaporerealestateinsider@gmail.com), the Family calendar, and the "6. PlayBigger Mentoring" and "1CallClose™ Fast Track" calendars.

2. EMAIL SCAN: Using the Gmail connector, search the last 7 days of inbox (query: "in:inbox newer_than:7d") and flag threads needing a reply or action — especially anything from clients, buyers, tenants, agents, lawyers, or banks about deals, viewings, handovers, rentals, or payments.

3. TABULATE BY IMPORTANCE, in this order:
   - A. INCOME-GENERATING (do first): viewings, listings, handovers, rental/sale completions, client calls, marketing of units, lead follow-ups.
   - B. INCOME-SUPPORTING ADMIN: invoices, tax filing, bank matters, paperwork with deadlines.
   - C. FAMILY (protected — flag if the week looks one-sided toward work or has zero family time).
   - D. SECONDARY / DO-LATER: anything that does not contribute to income — list at the bottom as "later" items, do not mix them into the priority list. Personal reminders found on the calendar (e.g. wash hair, social notes) should be flagged as "move to tasks, not calendar."

4. BALANCE CHECK: One short paragraph — is work vs family balanced this week? Note any conflicts/double-bookings.

5. OUTPUT: A single concise briefing with a table (Priority | Item | Day/Time | Action needed) followed by the top 3 things to clear first this week. Keep it to one page.
</scheduled-task>
