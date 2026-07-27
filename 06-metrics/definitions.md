# Metric Definitions

**Owner:** Joel (Principal) · **Trigger:** A metric is disputed, or a new one is added · **Cadence:** Quarterly · **Last reviewed:** 2026-07-26

## Purpose

Exactly how each scorecard number is calculated. A metric two people compute
differently is not a metric — it is a source of argument that looks like data.

What breaks without it: "win rate" quietly means three different things depending
on who is asked and what month it is, and the trend becomes meaningless.

## Definitions

### 1. Cash on hand
Sum of all business account balances **minus** the tax set-aside balance.

The set-aside is excluded because it is not Alivio's money — it is collected on
behalf of a government and happens to be in Alivio's account.

### 2. 13-week projected low point
The lowest projected closing balance across the next 13 weeks, per
`../03-finance/cash-flow-review.md`.

- Inflows: invoices issued and unpaid at their due date; scheduled but unissued
  invoices from SOW milestone schedules; retainers at their billing date
- **Overdue invoices are dated realistically, not at their original due date**
- **Weighted pipeline is excluded entirely** — cash planning uses agreed money, not
  forecast money
- Outflows: contractor run, recurring tools, tax set-aside, known one-offs

Expressed as **weeks of operating cost**, so it is comparable across months.

### 3. AR over 30 days
Sum of unpaid invoices where **today − due date > 30 days**. Due date, never
invoice date.

Excludes invoices under formal dispute — those are tracked separately, because a
dispute is a delivery problem wearing a finance problem's clothes.

### 4. AR over 45 days
Same, at 45 days. Tracked separately because it means the chase sequence never
ran, rather than ran late.

### 5. Weighted pipeline
**Σ (deal value × stage weight)**, weights fixed in
`../02-sales/pipeline-stages.md`:

| Stage | Weight |
|---|---|
| New | 5% |
| Qualified | 15% |
| Discovery | 30% |
| Proposal | 50% |
| Verbal | 80% |

**Weights are never adjusted per deal.** Marking one "90% because I can feel it" is
what makes forecasts useless.

Excludes retainer renewals — those are recurring revenue, tracked separately.

### 6. Pipeline coverage
**Weighted pipeline ÷ revenue target for the next 90 days.**

Revenue target is **$100,000/year → $25,000 per 90 days** (set 2026-07-27), so
3× coverage means **$75,000 of weighted pipeline**.

Target 3×, alarm below 2×. Assumes roughly a 30% close rate.

### 7. Win rate
**Deals Won ÷ (deals Won + deals Lost)**, over a rolling 90 days.

- Counted at close, by close date
- **Excludes deals Alivio declined** — refusing a bad fit is not a loss, and
  counting it as one punishes good qualification
- Includes deals lost to silence; those are losses

### 8. Projects red
Count of active projects meeting any RED trigger in
`../01-delivery/project-red-escalation.md`. Point-in-time, checked weekly.

### 9. On-time milestone rate
**Milestones delivered on or before their committed date ÷ total milestones due**,
over a rolling 90 days.

- The **committed** date is the one in the SOW or the most recent signed change
  order — not a date that was informally moved
- A milestone delayed by documented client-caused delay under the delay clause is
  **excluded**, not counted as a miss
- Delivered means passed the QA gate and sent to the client

That exclusion matters. Counting client-caused delay as an Alivio miss makes the
metric measure the wrong thing and encourages hiding it.

### 10. Average revision rounds
**Total revision rounds ÷ total deliverables**, over a rolling 90 days.

A round is one consolidated set of feedback, per
`../01-delivery/scope-change-protocol.md`.

- Clarifying questions are not a round
- Fixing something that does not match the SOW is not a round
- A change of direction is a round

**Above 2.5 is a scoping problem, not a client problem.** The rounds are a symptom;
the cause is upstream in discovery.

### 11. Gross margin per project
**(Project revenue − direct contractor cost) ÷ project revenue**, computed at
close.

- Revenue includes change orders
- Direct contractor cost is only contractor payments and expenses booked to this project
- **Excludes Joel's own time** — Alivio has no internal cost rate for Joel, so
  including it would require inventing one
- Excludes overhead and tools

Because Joel's time is excluded, this measures contractor leverage rather than true
profitability. **Named explicitly so the number is not over-read.**

## Rules

- **A metric is computed the same way every period**, or the trend is fiction
- **Changing a definition means restating history**, or noting the break clearly
- **When a number looks wrong, check the definition before the data.** It is
  usually the definition

## Decision rights

- **Joel decides alone:** every definition here.
- **Escalate when:** a metric cannot be computed as defined. That is a data or
  tooling gap and it gets named rather than approximated.

## Definition of done

Every scorecard metric has a definition here precise enough that two people
computing it independently get the same number.

## Related

- [Scorecard](scorecard.md)
- [Cash flow review](../03-finance/cash-flow-review.md)
- [Forecast method](../02-sales/forecast-method.md)
- [Pipeline stages](../02-sales/pipeline-stages.md)
- [Project red escalation](../01-delivery/project-red-escalation.md)
- [Scope change protocol](../01-delivery/scope-change-protocol.md)

## Assumptions

- **Metric 6 is computable as of 2026-07-27** ($25,000 per 90 days). **Metric 2
  still is not** — it needs a monthly operating cost figure, without which the
  cash trigger levels stay switched off rather than guessed.
- **Metric 11 excluding Joel's time is a deliberate simplification.** Once Joel sets
  a notional internal rate, this should be revisited — it currently flatters every
  project Joel worked on personally.
- Metrics 1–4 and 11 are computed from the ledger
  (`../08-automation/lib/ledger.py`), built 2026-07-26. They are only as current
  as what Joel has recorded — the ledger cannot observe a bank account, and it
  reports "no balances recorded" rather than assuming zero.
