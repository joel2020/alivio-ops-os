# Forecast Method

**Owner:** Joel (Principal) · **Trigger:** Friday pipeline review · **Cadence:** Weekly · **Last reviewed:** 2026-07-26

## Purpose

One number that says whether Alivio will have enough work in 60 days, computed the
same way every week so the trend means something. The trend matters more than the
number — a weighted pipeline falling three weeks running is a signal well before
it becomes a cash problem.

What breaks without it: capacity and cash get planned on the feeling that things
seem busy, which is at its most wrong exactly when delivery is heaviest and
prospecting has stopped.

## The calculation

**Weighted pipeline = Σ (deal value × stage weight)**

Weights are in `pipeline-stages.md` and are not adjusted per deal. The temptation
to mark one "90% because I can feel it" is exactly what makes forecasts useless.

| Stage | Weight |
|---|---|
| New | 5% |
| Qualified | 15% |
| Discovery | 30% |
| Proposal | 50% |
| Verbal | 80% |

## Coverage target

**Coverage = weighted pipeline ÷ revenue target for the period.**

**Revenue target: $100,000 for the year** (Joel, 2026-07-27) — **$25,000 per
rolling 90 days**.

Target: **3× coverage**, so the pipeline needs **$75,000 weighted** at any time.

Why 3×: at a roughly 30% close rate — which the stage weights imply — three
dollars of weighted pipeline are needed for every dollar of revenue. Below 3× the
problem is already two months old, because that is how long it takes a new lead to
become cash.

| Coverage | Means | Do this |
|---|---|---|
| **Above 3×** | Healthy | Protect delivery capacity; consider raising prices |
| **2–3×** | Thin | Prospecting becomes a scheduled weekly block |
| **Below 2×** | Problem | Prospecting is the top priority above all non-client work |
| **Below 1×** | Serious | Cash planning changes; see `../03-finance/cash-flow-review.md` |

## What the forecast does not do

- **It does not predict individual deals.** It predicts the aggregate, and only
  above about 8 open deals. Below that it is arithmetic, not a forecast.
- **It does not include retainer renewals** — those are recurring revenue and
  belong in the cash view, not the pipeline.
- **It does not get adjusted to look better.** Ever.

## Retainers

Tracked separately: **monthly recurring revenue** = sum of active retainers. New
retainer deals appear in the pipeline at annual value for weighting, but only the
committed term counts as recurring.

## The weekly ritual

Fifteen minutes, Friday, after the hygiene sweep:

1. Recompute the weighted total
2. Compare to last week — the delta is the signal
3. Compute coverage against the 90-day target
4. If coverage dropped two weeks running, write down why
5. Record the number so the trend exists

**Recording it is the point.** A forecast computed and not written down cannot show
a trend, and the trend is the only genuinely useful part.

## Decision rights

- **Joel decides alone:** revenue targets, the coverage threshold, whether to act.
- **Escalate when:** n/a.

## Definition of done

A weighted number and a coverage ratio are recorded every Friday, with a written
note whenever coverage falls below 3×.

## Related

- [Pipeline stages](pipeline-stages.md)
- [CRM hygiene](crm-hygiene.md)
- [Cash flow review](../03-finance/cash-flow-review.md)
- [Scorecard](../06-metrics/scorecard.md)
- [Definitions](../06-metrics/definitions.md)

## Assumptions

- **Revenue target set 2026-07-27: $100,000/year, $25,000 per 90 days.** Coverage
  is now computable. The $75,000 weighted-pipeline figure follows from the 3×
  target.
- **The target and the stated capacity do not agree, and that is worth
  resolving.** 4–6 concurrent clients on 4–8 week engagements implies roughly
  25–35 engagements a year; at the $8,000 web floor that would be $200K+. Either
  the concurrency figure counts small and dormant work, or $100K is a
  deliberately conservative floor, or the price bands are set too high for the
  volume actually being run. Whichever it is, it changes what "healthy" means on
  this page — a business tracking to $100K does not need 4–6 concurrent clients,
  and one running 4–6 should not be at $100K.
- The 3× target assumes a ~30% close rate. Alivio's actual rate is unknown; after
  ~20 closed deals, replace both the weights and the target with measured values.
- Assumes the pipeline is large enough for weighting to be meaningful. At 4–6
  concurrent clients the pipeline may be small enough that Joel should read the
  individual deals and treat the weighted number as secondary.
