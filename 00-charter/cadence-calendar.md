# Cadence Calendar

**Owner:** Joel (Principal) · **Trigger:** Standing rhythm · **Cadence:** This *is* the cadence · **Last reviewed:** 2026-07-26

## Purpose

The rhythm that makes the rest of the OS actually happen. Every ritual here
produces an **artifact** — a meeting that produces nothing is a meeting that gets
skipped as soon as things get busy, and things are always about to get busy.

What breaks without it: the SOPs exist and nothing triggers them. This is the
clock.

Total standing time: **about 2.5 hours a week** for Joel, most of it Monday and
Friday. That budget is deliberate — a solo operator cannot afford an OS that costs
five hours a week to run.

## Daily

| When | Who | What | Artifact | Time |
|---|---|---|---|---|
| Morning | PM | Scan client channels, clear anything inside SLA | Replies sent, blockers raised in Linear | 15m |
| Morning | Joel | Read the Monday-brief-style digest; act on anything red | — | 5m |

Nothing else is daily. A daily standup at 4–6 concurrent clients is theatre.

## Weekly

| When | Who | What | Artifact |
|---|---|---|---|
| **Mon 7:00** | Automated | Monday brief generated | Cash, pipeline movement, week's commitments, top 3 priorities |
| **Mon 9:00** | Joel | Week planning off the brief | Top 3 priorities committed in Linear |
| **Tue** | Automated | Invoice chase sweep | Overdue list + drafted chase emails, unsent |
| **Wed** | PM | Project status roll-up | Per-project stage, blockers, anything aging in stage |
| **Wed** | PM → clients | Weekly status report per active project | Status report sent in channel of record |
| **Fri** | Automated | Pipeline hygiene sweep | Stale deals, missing fields, deals with no next step |
| **Fri** | Automated | Invoice chase sweep (second pass) | Drafted chase emails, unsent |
| **Fri 15:30** | Joel | Pipeline review | CRM clean, next step on every open deal |
| **Fri 16:00** | Automated | Friday close-out | What shipped, what slipped, what carries over |

**Why Tuesday and Friday for AR:** invoices are chased twice a week rather than
once because the observed failure was $12,000 aging 11 and 18 days with nothing
firing at all. Two passes make a slip visible within three business days.

## Monthly

| When | Who | What | Artifact |
|---|---|---|---|
| **1st** | Joel | Retainer invoices issue | Invoices sent |
| **1st** | Joel | Contractor payment run | Contractors paid |
| **25th** | Automated | Month-end prep | Reconciliation gaps, uncategorized items, checklist status |
| **Last business day** | Joel | Month-end close | Books closed, scorecard updated |
| **Monthly** | Joel + PM | Scorecard review | The 8–12 numbers, with a written note on any that moved badly |
| **Monthly** | PM | Knowledge base review | Stale docs flagged, one fixed |

## Quarterly

| When | Who | What | Artifact |
|---|---|---|---|
| Quarter start | Joel | Tax set-aside transferred | Money moved to the tax account |
| Quarter start | Joel | OS review — charter, roles, RACI, thresholds | Updated docs, `Last reviewed` bumped |
| Quarter start | Joel | Pricing review against actual margin | Confirmed or revised price bands |
| Quarter end | Joel + PM | Win/loss themes | Written summary, 1–2 changes committed |

## Annual

| When | Who | What |
|---|---|---|
| January | Joel | 1099s issued to contractors |
| January | Joel | Insurance, contracts, and tool subscriptions reviewed |

## The rule that keeps this honest

**If a ritual is skipped twice in a row, it is either wrong or unowned — fix it or
delete it.** A calendar full of ceremonies nobody performs is worse than a short
one that runs, because it teaches you to ignore the calendar.

## Decision rights

- **Joel decides alone:** what is on this calendar and when.
- **PM decides alone:** moving an internal checkpoint inside the same week.
- **Escalate when:** a client-visible ritual (status report, invoice) will be
  missed.

## Definition of done

Every automated row has a corresponding scheduled task in
`../06-metrics/scorecard.md`'s cadence and in the Phase 3 automation layer. Every
manual row has a named owner above.

## Related

- [Operating charter](operating-charter.md)
- [RACI matrix](raci-matrix.md)
- [Meeting standards](../04-team/meeting-standards.md)
- [Weekly review agenda](../05-templates/weekly-review-agenda.md)
- [Scorecard](../06-metrics/scorecard.md)

## Assumptions

- Times (Mon 7:00, Fri 15:30/16:00) are guesses at Joel's working rhythm and
  should be moved to whatever he actually does. The *sequence* matters more than
  the clock: brief before planning, hygiene before pipeline review, close-out last.
- Assumes Joel works Monday–Friday. If work is spread across weekends, the Friday
  close-out is the ritual that needs moving.
- **Past ~8 people:** add a Monday delivery stand-up across PMs. At 4–6 clients
  with one PM archetype it is unnecessary overhead.
