# Scorecard

**Owner:** Joel (Principal) · **Trigger:** Weekly and monthly review · **Cadence:** Per row · **Last reviewed:** 2026-07-26

## Purpose

Eleven numbers that say whether Alivio is healthy. Few enough to actually be
maintained, spread across all four pillars so a problem in one shows up before it
becomes a problem in cash.

What breaks without it: the business is judged by how busy it feels, which is
uncorrelated with whether it is working.

Calculations are in `definitions.md`. No metric here is ambiguous about how it is
computed — a number two people compute differently is not a metric.

## The numbers

### Cash — the ones that end the business if ignored

| # | Metric | Owner | Cadence | Target | Alarm |
|---|---|---|---|---|---|
| 1 | **Cash on hand** | Joel | Weekly | — | — |
| 2 | **13-week projected low point** | Joel | Weekly | > 8 weeks of operating cost | < 4 weeks |
| 3 | **AR over 30 days** | Joel | Weekly | $0 | Anything above $0 |
| 4 | **AR over 45 days** | Joel | Weekly | $0 | Anything above $0 — a process failure, not a client problem |

Metrics 3 and 4 are separate deliberately. Over 30 days means the chase sequence
is running late; over 45 days means it never ran at all — the observed failure.

### Pipeline — the ones that predict cash

| # | Metric | Owner | Cadence | Target | Alarm |
|---|---|---|---|---|---|
| 5 | **Weighted pipeline** | Joel | Weekly | — | Falling 3 weeks running |
| 6 | **Pipeline coverage** | Joel | Weekly | > 3× | < 2× |
| 7 | **Win rate** | Joel | Monthly | — | Falling trend over a quarter |

### Delivery — the ones that predict pipeline

| # | Metric | Owner | Cadence | Target | Alarm |
|---|---|---|---|---|---|
| 8 | **Projects red** | PM | Weekly | 0 | Any project red 2 weeks running |
| 9 | **On-time milestone rate** | PM | Monthly | > 85% | < 70% |
| 10 | **Average revision rounds** | PM | Monthly | ≤ 2 | > 2.5 — a scoping problem, not a client problem |

### Margin — the one that says whether any of it was worth doing

| # | Metric | Owner | Cadence | Target | Alarm |
|---|---|---|---|---|---|
| 11 | **Gross margin per project** | Joel | Per project, at close | — | Any project below 40% |

**Metric 11 is the one most agencies never compute**, and it is the one that
determines whether growth helps. Revenue without margin is just more work.

## How to read it

- **A single bad number is noise. A trend is signal.** Record every week; conclude
  monthly.
- **Cash metrics are checked weekly regardless.** They are the only ones that can
  end the business quickly.
- **When two conflict, cash wins.** A pipeline that looks great while AR is at 45
  days is a business about to have a bad month.
- **Write a note whenever a metric hits its alarm.** The note is what makes the
  quarterly review useful — the number alone does not say what was happening.

## What is deliberately not measured

Named so nobody adds them back:

- **Utilisation.** Encourages busywork over outcomes at this size.
- **Hours logged per person.** Alivio buys deliverables from contractors, not time.
- **Revenue alone**, without margin. See metric 11.
- **Number of leads.** Volume without qualification is a vanity number; coverage
  (metric 6) captures what matters.

## Decision rights

- **Joel decides alone:** what is on this list, targets, alarm thresholds.
- **PM decides alone:** nothing — but owns the accuracy of metrics 8, 9, 10.
- **Escalate when:** any alarm fires, at the next review at the latest. Cash alarms
  escalate same day.

## Definition of done

Every metric has a current value and a recorded history, updated at its stated
cadence.

## Related

- [Definitions](definitions.md)
- [Cash flow review](../03-finance/cash-flow-review.md)
- [Forecast method](../02-sales/forecast-method.md)
- [Month-end close](../03-finance/month-end-close.md)
- [Weekly review agenda](../05-templates/weekly-review-agenda.md)

## Assumptions

- **Targets for metrics 2, 6, 9, 10, and 11 are industry defaults, not Alivio's
  history.** They are a starting point. After one quarter of real data they should
  be replaced with values grounded in what Alivio actually does.
- **Metric 2 cannot be computed until Joel provides a monthly operating cost
  figure.** Blocking.
- **Metric 6 cannot be computed until Joel sets a revenue target.** Blocking.
- Assumes 11 metrics is maintainable for a solo operator. If it is not, cut to
  metrics 2, 3, 6, 8, and 11 — those five cover the business.
