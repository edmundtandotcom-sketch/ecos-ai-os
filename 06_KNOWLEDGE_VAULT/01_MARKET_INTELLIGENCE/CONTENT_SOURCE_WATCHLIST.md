# CONTENT_SOURCE_WATCHLIST
Version: v1.1
Status: APPROVED MASTER
Date: 2026-07-30
Source of truth for: the weekly organic content engine — currently being rebuilt as the Cloud "Weekly Content Intelligence" routine (claude.ai/code/routines); `08_OPERATIONS/03_AUTOMATIONS/rei-weekly-content-brief_SKILL.md` and its Claude Code scheduled task are retired (disabled 2026-07-30, kept for history, not the active spec). Also read by the on-demand `.claude/skills/rei-video-routine/SKILL.md` for its competitor-channel roster.

> This is a **seed list, not a ceiling.** Whatever runs this scan must not limit itself to only what's listed here — scan more broadly for Singapore property articles, news, and YouTube content each run. When a source outside this list turns up repeatedly with strong signal (a new outlet, a new creator gaining traction), add it here with a one-line rationale and the date added. Do not invent or guess a source's existence — only add sources actually found live during a run. Mirrors the same discipline as `COMPETITOR_WATCHLIST.md` in the sibling ads-intelligence routine.

---

## Article sources (seed)

| Source | URL | Why it's here |
|---|---|---|
| StackedHomes | stackedhomes.com | Data-driven SG property analysis, closest direct content competitor |
| EdgeProp | edgeprop.sg | New launch coverage, market commentary |
| URA | ura.gov.sg | Official transaction data, GLS tenders, stats |
| 99.co | 99.co/blog/singapore | Resale data, transaction analysis |
| PropNex | propnex.com | Market reports |
| MoneySmart | blog.moneysmart.sg/property | Mortgage/finance angle |

## YouTube channels (seed)

| Channel | Why it's here |
|---|---|
| Marcus Luah ("Keep It Real Estate") | Established SG property YouTube creator, format/pacing reference |
| JNA Real Estate ("JNA News Dash") | News-recap format, weekly cadence |
| StackedHomes YouTube | Same outlet as the article source, video-specific angle worth tracking separately |

### Competitor channel roster (merged 2026-07-30 from `Competitor_Channel_Roster_v1.0.md`, retired to a pointer — this is now the one home for the list)

**Own channel — baseline for comparison only, never scan as a competitor source:** Singapore Property–The REI Method | Edmund Cindior (`@SingaporeRealEstateInsider`).

**Update discipline:** when a `TBD` handle gets resolved, write the resolved handle/ID back into this row so the next run doesn't re-resolve it. Re-verify the whole roster roughly quarterly, or immediately if a scan starts returning 0 results for a channel that should have content — that usually means a stale/wrong ID, not an empty channel. To add a new channel: append with `TBD`, note who found it and why, let the next run resolve the handle — never hand-guess a channel ID, a wrong one silently returns zero/wrong-channel results with no error.

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

**Excluded:** Sarah X. Miracle (channel/UCEmTUviyTG5Ssnki8ons1nA) — flagged 2026-07-28 as likely off-niche (Music/Hobby topics) or a wrong link. Do not scan until confirmed as actually SG-property content.

## Signal sources (seed, exploratory tier)

Google Trends (SG property keywords) · Reddit r/singapore + r/singaporefi · HardwareZone property forums · relevant Telegram/FB groups · YouTube comments on tracked channels' videos · Google News alerts.

---

## Additions log

*(New rows added here as discovered — source, date added, one-line rationale. Empty as of 2026-07-30, the list's creation date.)*
