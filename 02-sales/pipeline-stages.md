# Pipeline Stages

**Owner:** Joel (Principal) · **Trigger:** Any deal movement · **Cadence:** Reviewed every Friday · **Last reviewed:** 2026-07-26

## Purpose

A pipeline stage must mean something the buyer did, not something Alivio hopes.
"They seemed keen" is not a stage. Every advance below requires an observable act
by the client — which is what makes the forecast worth reading.

What breaks without it: the pipeline inflates with dead deals nobody will admit
are dead, and the forecast becomes a mood.

## The stages

| # | Stage | Enters when — **the client did this** | Weight |
|---|---|---|---|
| 1 | **New** | Lead captured with a name and a company | 5% |
| 2 | **Qualified** | Qualification call held; ICP fit confirmed; budget range acknowledged | 15% |
| 3 | **Discovery** | Discovery session held; Alivio understands the problem well enough to scope | 30% |
| 4 | **Proposal** | SOW sent | 50% |
| 5 | **Verbal** | Client has said yes and is getting signature/procurement done | 80% |
| 6 | **Won** | SOW signed **and** deposit received | 100% |
| — | **Lost** | Declined, went elsewhere, or went quiet past the follow-up cadence | 0% |

**Won requires the deposit.** A signed SOW with no deposit is stage 5, not stage 6.
This is the same rule as `../01-delivery/project-lifecycle.md` stage 1, and it
exists because a signature is an intention and money is a decision.

## What does not move a deal forward

Named explicitly, because these are the things that feel like progress:

- A good call where nothing was decided
- "Send me something" without a scheduled follow-up
- Interest from someone who is not the decision-maker
- Alivio sending a proposal nobody asked for
- The client saying they are "definitely interested" while missing two meetings

**A deal only advances on a client action.** If the last event was Alivio doing
something, the deal has not moved.

## Stage hygiene rules

Enforced at the Friday sweep:

- **Every open deal has a next step with a date.** No exceptions. A deal without a
  next step is not a deal, it is a memory.
- **No deal sits in one stage past its limit:**

  | Stage | Max dwell | Then |
  |---|---|---|
  | New | 5 business days | Contact or mark Lost |
  | Qualified | 10 business days | Book discovery or mark Lost |
  | Discovery | 10 business days | Send proposal or mark Lost |
  | Proposal | 15 business days | Follow-up cadence; then Lost |
  | Verbal | 15 business days | Escalate — a verbal that will not close is a no |

- **Deals go Lost, not stale.** Marking Lost is not failure; carrying a dead deal
  is. A pipeline that only grows is a pipeline nobody trusts.
- **A Lost deal can be resurrected.** Reopen it — losing well costs nothing.

## Decision rights

- **Joel decides alone:** every stage change, every Lost call, the weights above.
- **Escalate when:** n/a — sales is entirely Joel's at current headcount. See the
  key-person risk noted in `../00-charter/raci-matrix.md`.

## Definition of done

Every open deal has a stage that matches a client action, a next step with a date,
and has not exceeded its dwell limit.

## Related

- [ICP and disqualifiers](icp-and-disqualifiers.md)
- [Follow-up cadence](follow-up-cadence.md)
- [Forecast method](forecast-method.md)
- [CRM hygiene](crm-hygiene.md)
- [Intake and qualification](../01-delivery/intake-and-qualification.md)

## Assumptions

- **The weights (5/15/30/50/80) are standard B2B services defaults, not Alivio's
  history.** They should be replaced with actual conversion rates once ~20 deals
  have closed. Until then the forecast is directionally useful and precisely wrong.
- Dwell limits assume a 4–8 week delivery cycle and a correspondingly short sales
  cycle. Enterprise deals would need longer limits.
- Assumes pipeline lives in Linear alongside delivery work. Workable at this
  volume; a real CRM becomes worth the switching pain somewhere past 15–20 open
  deals.
