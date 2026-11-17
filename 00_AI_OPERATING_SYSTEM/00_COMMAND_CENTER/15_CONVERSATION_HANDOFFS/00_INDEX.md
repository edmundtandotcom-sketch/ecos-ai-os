# 15_CONVERSATION_HANDOFFS — Index
Version: v1.0
Status: LIVE
Created: 2026-11-17
Owner: Edmund Tan

---

## 1. Why this folder exists

Claude Code session transcripts and Claude's own memory files live **only on the
desktop machine**, under `C:\Users\Admin\.claude\projects\`. They are not in this
repository and cannot be, because they sit outside the Drive root that Git tracks.

That has one consequence worth stating plainly: **a cloud session, or any session on
another machine, starts blind.** It clones this repository and sees nothing of what
was decided in conversation.

This folder is the fix. Each file distils one working conversation down to the part
that matters later: what was decided, where the work currently stands, and what is
still open. The raw transcripts stay on the desktop; the decisions travel here.

## 2. Scope of this first batch

Five conversations were nominated on 2026-11-17. Four produced a handoff.

| Conversation | Handoff | Raw transcript | Status |
|---|---|---|---|
| System Ads Dashboard | [2026-11_SYSTEM_ADS_DASHBOARD.md](2026-11_SYSTEM_ADS_DASHBOARD.md) | 63.6 MB, 447 turns | Active |
| 2027 Webinar Launch Calendar | [2026-11_WEBINAR_LAUNCH_CONTROL_2027.md](2026-11_WEBINAR_LAUNCH_CONTROL_2027.md) | 13.8 MB, 64 turns | Active |
| One Chuan Grove video script | [2026-11_ONE_CHUAN_GROVE_VIDEO.md](2026-11_ONE_CHUAN_GROVE_VIDEO.md) | 3.0 MB | Draft, awaiting verification |
| `-->RANDOM` (ad-hoc research) | [2026-11_AD_HOC_RESEARCH.md](2026-11_AD_HOC_RESEARCH.md) | 8.8 MB | Partial — see exclusion below |
| Korean trip AI building | none | 0.8 MB | **Empty — nothing to record** |

**"Korean trip AI building"** contains 46 transcript lines, one human prompt (the
title) and a single clarifying question that was never answered. There is no work in
it. No handoff was written rather than inventing one.

## 3. Deliberate exclusion — IRAS audit material

The `-->RANDOM` conversation is a grab-bag spanning 2026-09-29 to 2026-11-15. Its most
recent thread is **IRAS audit correspondence**: named individuals, a commission-sharing
arrangement, income figures and a statutory submission deadline.

**That thread is excluded from this repository on purpose.** Constitution §2 restricts
the AI OS to material with no raw PII, and routes client and contact data to
`00_E.C.O.S_CLIENTS_PRIVATE`, which is not version-controlled. A private GitHub
repository is still a third-party service, and tax-audit material naming third parties
does not belong in one.

The IRAS workstream has its own tracker in the restricted private drive. Nothing in
this folder should be read as a record of it.

## 4. How to use this folder from a cloud session

1. Read this index.
2. Read the handoff for the thread you are picking up.
3. Treat every figure marked **unverified** as unverified. Several of these documents
   record numbers that were never traced to source.
4. Where a handoff says an asset is desktop-only, it is genuinely unreachable from a
   cloud session. Do not assume a clone contains it.

## 5. Maintenance

Each handoff is a point-in-time record, dated at the top. When a thread moves on
materially, update its handoff rather than adding a second file for the same thread
(Constitution §6, one file one home).

These documents do not replace `04_DECISION_MEMORY.md` for formal decisions, or
`08_SESSION_LOG.md` for the session record. They carry working context between
machines, which neither of those files was built to do.
