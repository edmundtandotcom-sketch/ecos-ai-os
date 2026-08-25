---
name: desk
description: Route the current task to the right AI TEAM desk and work as that desk. Use when Edmund types /desk, names a desk (advisory, content, ads, recruitment, research, ops, strategy), or gives any substantial business task without naming one.
---

# /desk — AI TEAM Desk Routing

You are inside the AI Operating System (`00_AI_OPERATING_SYSTEM\`). Run the task as the correct specialist desk.

## Steps

1. Read `00_AI_OPERATING_SYSTEM\01_E.C.O.S\00_TEAM_ROSTER.md` and pick the single highest-leverage desk for the task in `$ARGUMENTS` (or the current conversation task if no arguments). Do not run multiple desks at once; lead with one and note hand-offs.
2. Read that desk's charter file in `01_E.C.O.S\` fully. Follow its READS list — load those files before producing anything.
3. Check `00_COMMAND_CENTER\03_CURRENT_PRIORITIES.md`: if the task doesn't support current priorities, say so and recommend the Parking Lot before proceeding.
4. Execute per the desk's SOP, quality bar, and output format. Tight Ship Mode always.
5. Save outputs where the desk's PRODUCES table says — never to ad-hoc locations.
6. If the work created a decision, new direction, or reusable lesson, route it per `00_COMMAND_CENTER\05_EVOLUTION_PROTOCOL.md` before ending.

## Rules
- Old folders outside `00_AI_OPERATING_SYSTEM\` are read-only reference.
- If the task spans two desks, finish as the lead desk and end with: "Hand-off: run /desk <other> for <sub-task>."
