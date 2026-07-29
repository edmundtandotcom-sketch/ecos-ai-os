# LOST — routing
Version: v0.1 · Status: DRAFT · Date: 2026-07-11 · Supersedes: none
Sources: OUTCOME_CODES.md (branch 12); LOST_REASON_REGISTRY.csv (this branch); CRM SOP 01 §5–§6

## Purpose
Captures and classifies leads that ended without a viable path forward — with a controlled lost-reason so patterns are learnable (feeds content + conversation intelligence). `[T5]`

## Play
1. Stamp the OUTCOME_CODE (branch 12) — only `lost-to-competitor` / `chose-no-action` (and genuinely-dead NO-FIT states) route here.
2. Assign ONE controlled `lost_reason_code` (LOST_REASON_REGISTRY.csv).
3. Log root cause (anonymised) + the gap that was never closed (branch 13).
4. If any future trigger exists → REVIVAL, not permanent close.

## Rules
- `recommended-not-to-transact` and `not-suitable` are advisory outcomes, NOT losses — do not log them as competitive losses. `[T5]`
- No PII in lost records held in this OS. `[HARD RULE 5]`
- Lost-reason patterns hand off to branch 21 (conversation intelligence) + content (objection pre-emption).

READS FROM: branch 12 OUTCOME_CODES; branch 13 (unclosed gap). FEEDS INTO: REVIVAL, branch 21, branch 15.
