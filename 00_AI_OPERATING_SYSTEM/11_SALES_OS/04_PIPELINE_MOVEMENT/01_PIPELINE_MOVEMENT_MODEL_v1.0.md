# Pipeline Movement Model
Version: v1.0
Status: APPROVED DECISION ARCHITECTURE — VERIFY LIVE BEFORE USE
Date: 2026-07-20
Source: Decision 071.

## Ten-stage architecture

1. `New Lead`
2. `Responded`
3. `Booked Call`
4. `Appointment`
5. `Strategy Session`
6. `Close`
7. `Nurture`
8. `Unqualified`
9. `Won`
10. `Lost`

These names record the approved architecture, not evidence that the live GHL configuration currently matches it.

## Movement rules

- Every move requires an observable event or controlled outcome.
- Entry and exit criteria must be distinct.
- Stage and A–D lead grade remain separate.
- `Strategy Session` tracks progression; Client Advisory governs the session itself.
- `Nurture`, `Unqualified`, `Won` and `Lost` require reason, owner and date.
- Use outcomes `Proceed`, `Prepare`, `Nurture`, `No Fit` where applicable.
- Never move a record solely to make a dashboard look cleaner.

Operations implements only after confirming live objects and approved criteria.

