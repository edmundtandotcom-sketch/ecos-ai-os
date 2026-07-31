# Migration and QA Plan

## Phase 1 — Parallel build

- Keep v8.43 live.
- Deploy v9 against the copied v9 master sheet.
- Run Meta, GHL and Google syncs manually.
- Compare 7-day and 30-day totals by platform.

## Phase 2 — Reconciliation checks

For each period, compare:

- Spend
- Leads
- Responded
- Booked calls
- Appointments
- Qualified appointments
- Closed transactions
- Revenue

Allow timing differences only when a platform has not completed attribution or the scheduled sync has not yet run.

## Phase 3 — Forecast calibration

Do not use the Base forecast as a target until there are at least:

- 30 leads
- 10 completed appointments
- 5 closed transactions
- 90 days of stable daily data

Until then, mark the forecast as directional.

## Phase 4 — Cutover

Cut over only after:

- Three consecutive days without failed scheduled syncs
- Chrome desktop and mobile access works without Google account selection
- Meta and Google spend reconcile within an agreed tolerance
- GHL stage totals reconcile
- Error_Log has no unresolved high-severity entries

## Phase 5 — Retire old deployment

Do not delete v8.43. Rename the deployment and retain it as emergency rollback for at least 30 days.
