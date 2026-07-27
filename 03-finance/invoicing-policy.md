# Invoicing Policy

**Owner:** Joel (Principal) · **Trigger:** A billing event occurs (see triggers below) · **Cadence:** Event-driven, plus the 1st for retainers · **Last reviewed:** 2026-07-26

## Purpose

Invoices go out the day the triggering event happens, not when someone remembers.
This is the source of truth for payment terms; every other document defers to it.

What breaks without it: work gets delivered and invoiced late, which pushes cash
out by weeks and makes chasing awkward — hard to be firm about a payment when the
invoice itself arrived eleven days after the milestone.

The observed cost of not having this: **$12,000 across two milestones, aged 11 and
18 days, with no chase having fired.**

## Billing triggers

An invoice is issued **the same business day** the trigger fires. No batching.

| Trigger | Invoice |
|---|---|
| SOW signed | Deposit — 40% of fixed-scope value |
| Midpoint milestone accepted | 30% |
| Final deliverable approved | 30% |
| Retainer month begins | Full monthly fee, on the 1st, in advance |
| Change order signed | 100% of the change order, immediately |
| Milestone-based engagement | Per the milestone schedule in the SOW |

**Deposit before work.** Stage 1 of `../01-delivery/project-lifecycle.md` requires
the deposit received, not merely invoiced.

## Terms

**These numbers are the source of truth. Any other document that disagrees is wrong.**

**Every engagement is fixed-price.** Alivio does not bill hourly — see
`../01-delivery/scope-change-protocol.md`. The price is agreed before work starts
and does not move without a signed change order. What varies is the *schedule*
the fixed price is drawn down on, not the price.

- **Payment terms: Net 7** from invoice date
- **Deposit: 40%**, non-refundable once discovery begins
- **Default structure: 40 / 30 / 30** for fixed-scope
- **A different schedule is allowed when it is written into the SOW.** The total
  stays fixed; only the timing changes. See the RLTRS example below.
- **Retainers: monthly in advance**, due on the 1st, 3-month minimum term
- **Late fee: 2% per month** on balances over 30 days, stated in the SOW —
  unstated, it is unenforceable and merely annoying
- **Currency:** USD unless the SOW says otherwise
- **Client pays transfer fees** on international payments

### Custom schedules — the RLTRS pattern

RLTRS runs **$4,000 up front, then $500 every Friday until completion** (agreed
at the Jul 16 meeting; the transcript is the authoritative record). That is a
fixed-price engagement on a weekly draw, not a different pricing model.

**The risk this shape carries, named because it is not obvious.** A fixed total
paid weekly "until completed" means *Alivio absorbs every week of overrun at
zero marginal revenue*. On 40/30/30 an overrun costs Alivio time; here it costs
time and delays the remaining draws. The protections are the ones already in the
OS and they matter more on this shape than on any other:

- The **delay clause** — client-caused delay moves the end date rather than being
  absorbed
- The **scope change protocol** — every extra is a change order, priced
  separately from the weekly draw
- The **RED trigger at 5 days' milestone slip** — on a weekly-draw engagement,
  slippage compounds

Before agreeing a weekly draw again, decide the **end date or the cap**. "Until
we're completed" is only safe when what "completed" means is written down and
countable, which is what the SOW deliverables list is for.

**Why Net 7 rather than Net 30:** Alivio is a solo operator with a contractor bench
to pay. Net 30 on a 6-week project means being paid after the work and the
contractors are done. Net 7 is normal for small agencies and is rarely objected to
when it is in the SOW from the start.

## Every invoice contains

- [ ] Invoice number, sequential, never reused
- [ ] Issue date and **due date as an explicit calendar date** — never "Net 7"
      alone, which invites arithmetic in Alivio's disfavour
- [ ] What it is for, referencing the SOW milestone by name
- [ ] Amount, currency, and tax treatment
- [ ] Payment methods and full details
- [ ] Late fee terms
- [ ] The PM's and Joel's contact for questions

## Rules

- **Nothing sends automatically.** Drafted automatically, reviewed and sent by
  Joel. A wrong invoice costs more credibility than a late one.
- **Never hold an invoice** because the relationship feels delicate. That is
  precisely when clarity helps most.
- **Never invoice for disputed work** without resolving the dispute first —
  invoicing into a disagreement converts a scope conversation into a payment fight.
- **Log every invoice** with issue date, due date, and amount, so AR aging is
  computable rather than remembered.

## Decision rights

- **Joel decides alone:** issuing, amounts, terms, write-offs, payment plans.
- **PM decides alone:** nothing. The PM flags that a trigger has fired.
- **Escalate when:** a client disputes an invoice — immediately, to Joel, and the
  chase sequence pauses until it is resolved.

## Definition of done

Every billing trigger produces an invoice the same business day, and every invoice
is logged with its due date.

## Related

- [AR chase sequence](ar-chase-sequence.md)
- [Cash flow review](cash-flow-review.md)
- [Scoping and SOW](../01-delivery/scoping-and-sow.md)
- [Delivery and handoff](../01-delivery/delivery-and-handoff.md)
- [Month-end close](month-end-close.md)

## Assumptions

- **Confirmed 2026-07-27:** every engagement is fixed-price. 40/30/30 is the
  default schedule; a different one is permitted when written into the SOW, and
  RLTRS is the live example. The price is fixed either way — only the timing of
  the draw changes.
- The 2%/month late fee is common practice; enforceability varies by jurisdiction
  and it has not been reviewed by a lawyer.
- AR aging is computed by `../08-automation/lib/ledger.py`, built 2026-07-26.
  It is only as current as what Joel records — the ledger cannot observe a bank
  account, and it reports "no balances recorded" rather than assuming zero.
