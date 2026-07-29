# 02_SCRIPTS — _INDEX
Version: v2.0
Status: ACTIVE REGISTRY
Date: 2026-07-20

This branch indexes operational script assets retained from the pre-cleanup structure.

## Ruling

- The live v8.43 Apps Script remains the system of record.
- The v9 folder is a future improvement asset, not a released replacement.
- Do not promote v9 without a separate build, test, rollback and release decision.
- Source-of-truth runtime/code should live in local runtime/private Git where applicable; Drive copies are controlled operational or recovery artifacts.

Read `SCRIPTS_README.md` and the relevant script-specific record before use. Confirm the deployed runtime version directly; filenames alone are not deployment evidence.

