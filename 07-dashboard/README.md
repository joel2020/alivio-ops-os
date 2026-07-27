# Dashboard

**Owner:** Joel (Principal) · **Trigger:** Monday planning, Friday review, or any time · **Cadence:** Data updated weekly · **Last reviewed:** 2026-07-26

## Purpose

One page that answers "how is the business actually doing" without asking anyone.
It renders the operating picture defined in Phase 1 — it does not invent
definitions, it reads them.

What breaks without it: the answer to "what's the status of X" lives in Joel's
head, which is one of Alivio's four stated pains.

## Using it

```
open dashboard.html
```

That is the whole setup. No server, no build step, no install.

**Edit `data.js`.** It is the only file to touch. Plain JSON wrapped in one
assignment, with comments explaining every field.

## Why data.js and not data.json

A browser opening `dashboard.html` from your filesystem is **not permitted to
`fetch("data.json")`** — it treats a local file read as a cross-origin request and
blocks it. That is a browser security rule, not something the page can work around.

`data.js` assigns one variable and loads via `<script src>`, which has no such
restriction. It edits exactly like JSON.

The page still prefers `data.json` when served over HTTP, so pointing it at a live
feed later requires no change to the page:

```
python3 -m http.server 8080     # then open http://localhost:8080/dashboard.html
```

## What is computed, and what you set

**You never set a health colour or a chase tier.** You set facts; the page applies
the rules from Phase 1.

| You set | Page computes | Rule from |
|---|---|---|
| `stage`, `stage_since`, `blocker_since`, `missed_checkpoints`, `budget_consumed`, `delivered` | project health, days in stage, dwell limit | `01-delivery/project-lifecycle.md` |
| `due_date`, `paid`, `disputed` | chase tier, who owns it, AR aging bucket | `03-finance/ar-chase-sequence.md` |
| deal `stage`, `value` | weight, weighted value, coverage, stale flags | `02-sales/pipeline-stages.md`, `forecast-method.md` |
| `on_hand`, `projection`, `monthly_operating_cost` | 13-week low point, weeks of cover, trigger level | `03-finance/cash-flow-review.md` |

This is the point of building Phase 1 first. Changing a threshold in the markdown
and in the `RULES` block at the top of `dashboard.html` keeps them honest; changing
it only in the dashboard is a bug.

## What it will not do

- **It will not guess.** Where a figure is missing it says "not set" and names the
  field, rather than showing a zero that looks like an answer. `monthly_operating_cost`
  and `revenue_target_90d` are unset today, so cash trigger levels and pipeline
  coverage are switched off rather than fabricated.
- **It will not hide staleness.** The header shows the data's age and turns amber
  past 3 days.
- **It will not sort a problem out of view.** Attention Required is ranked worst-
  first and cannot be filtered.

## Panels

1. **Attention required** — every red item, ranked: AR over 45 days, AR over 30
   days, red projects, other overdue invoices, deals with no next step
2. **Cash** — on hand, 13-week low point, weeks of cover against the trigger
   levels, AR outstanding, AR over 30 and over 45 tracked separately, aging
   buckets, and the 13-week chart
3. **Active projects** — client, stage, owner, next milestone, days in stage
   against its limit, computed health. Filter by health; the choice persists
4. **Pipeline** — open deals, raw and weighted value, coverage, days in stage,
   days untouched, next step
5. **This week** — commitments from the cadence calendar, overdue in red

Every table sorts on any column, and both the sort and the filter persist across
reloads via localStorage.

## Dependencies

Chart.js from a CDN, for the cash projection only. **If it fails to load the page
still works** — the projection renders as a table and says why. Everything else is
inline.

## Decision rights

- **Joel decides alone:** what is in `data.js`, and any change to the `RULES` block.
- **Escalate when:** the dashboard disagrees with the markdown. The markdown wins
  and the dashboard is the bug.

## Definition of done

Joel can answer "how is the business doing" in under a minute without opening
anything else.

## Related

- [Project lifecycle](../01-delivery/project-lifecycle.md) — stages, dwell limits, health rules
- [Pipeline stages](../02-sales/pipeline-stages.md) — weights and dwell limits
- [Forecast method](../02-sales/forecast-method.md) — coverage
- [AR chase sequence](../03-finance/ar-chase-sequence.md) — tiers
- [Cash flow review](../03-finance/cash-flow-review.md) — trigger levels
- [Scorecard](../06-metrics/scorecard.md) — the numbers this renders

## Assumptions

- **Seed data in `data.js` is real but partial.** Projects, invoices, and
  commitments reflect Alivio's actual position as at 2026-07-26. Cash figures and
  the pipeline are empty because Joel has not provided them.
- **No live connectors are wired.** The Phase 2 brief permits probing authorized
  tools first; none were authorized, so the page is manual-entry only. The
  `data.json` path over HTTP is the seam where a connector would attach.
- Assumes weekly data updates. The staleness warning fires at 3 days, which suits a
  Monday rebuild.
