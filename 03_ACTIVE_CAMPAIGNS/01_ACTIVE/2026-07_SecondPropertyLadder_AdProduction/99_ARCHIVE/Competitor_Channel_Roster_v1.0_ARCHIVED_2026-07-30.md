> **ARCHIVED 2026-07-30 — merged into `06_KNOWLEDGE_VAULT/01_MARKET_INTELLIGENCE/CONTENT_SOURCE_WATCHLIST.md`.** Two competing source lists for the same job (YouTube competitor tracking) is exactly the kind of drift the AI OS's "one file, one home" rule exists to prevent. The watchlist file is now the one home. Kept verbatim here for history.

---

# Competitor Channel Roster — Singapore Property YouTube
Version: v1.0
Status: APPROVED MASTER
Date: 2026-07-29
Supersedes: none (new file)
Sources: [[sg-property-youtube-competitive-landscape]] memory (2026-07-28 scan), vidiq

Fixed roster the `/yt-repurpose-scan` skill checks for recent/breakout uploads. Not a full open search — deliberately bounded to control cost and noise (Decision, 2026-07-29 in-chat: fixed roster, filtered to recent/outlier, on-demand only).

**Update discipline:** when the skill resolves a TBD handle via `vidiq_youtube_search`, it writes the resolved handle/ID back into this file so the next run doesn't re-resolve it. Re-verify the whole roster roughly quarterly, or immediately if a scan run starts returning 0 results for a channel that should have content — that's usually a stale/wrong ID, not an empty channel.

## Own channel (baseline — do not scan as a "competitor" source, comparison only)
| Channel | Handle |
|---|---|
| Singapore Property–The REI Method \| Edmund Cindior | @SingaporeRealEstateInsider |

## Competitor roster (19 channels)
| Channel | Handle / ID | Status |
|---|---|---|
| 1M65 | TBD | resolve on first run |
| Eric Chiew | @savvyericchiew | known |
| Pocket View | @pocketviewsg | known |
| Thomas Tong | @ttgx88 | known |
| LoukProp | TBD | resolve on first run |
| House Hunt with Joo | TBD | resolve on first run |
| JNA Real Estate | TBD | resolve on first run |
| The Right Move (Alvin Chin) | @TheRightMoveSG | known |
| Marcus Luah | @marcusluahsg | known |
| Property Sensei | TBD | resolve on first run |
| Alan Wee Property | TBD | resolve on first run |
| OwnThisProperty | TBD | resolve on first run |
| Cynric Ho Property | @cynricho6501 | known |
| PropertiesFreedom | TBD | resolve on first run |
| Asaphomes | @Asaphomes1000 | known |
| Matthew Lam | TBD | resolve on first run |
| Grayce Tan | @HomeswithGrayce | known |
| Invest with Pete | TBD | resolve on first run |
| Million Dollar Homes w/ Lizzy | TBD | resolve on first run |

## Excluded
- **Sarah X. Miracle** (channel/UCEmTUviyTG5Ssnki8ons1nA) — flagged 2026-07-28 as likely off-niche (Music/Hobby topics) or a wrong link. Do not scan until Edmund confirms it's actually SG-property content.

## Adding a new channel
Append it to the competitor table with `TBD`, note who found it and why (e.g. "breakout hit in a scan run, 2026-08-xx"), and let the skill resolve the handle on its next run. Don't hand-guess a channel ID — a wrong ID silently returns zero/wrong-channel results with no error.
