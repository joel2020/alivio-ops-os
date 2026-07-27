# Roles and Decision Rights

**Owner:** Joel (Principal) · **Trigger:** New role added, or a decision gets escalated that shouldn't have been · **Cadence:** Quarterly · **Last reviewed:** 2026-07-26

## Purpose

Most agency bottlenecks are not capacity problems, they are permission problems —
work stops while someone waits to be told they may proceed. This file removes the
waiting by naming, for every recurring decision, who decides alone.

What breaks without it: everything routes to Joel, which makes the 90-day goal
(Joel off for two weeks) arithmetically impossible.

## Roles

Roles, not people. One person may hold several; at current headcount Joel holds
Principal and often PM.

### Principal (Joel)

**Outcomes owned:** revenue, margin, client relationships at the account level,
who Alivio works with, final quality bar.

**Decides alone:**
- Pricing, discounts, payment terms
- Which clients to take and which to refuse
- Contractor rates and who is on the bench
- Anything that moves money, without exception
- Whether a project is stopped or a client fired

**Must be consulted on:** any scope change over $500, any timeline change
communicated to a client, any project entering RED.

**Cannot delegate:** money movement, pricing, final sign-off on first delivery to
a new client.

### PM

**Outcomes owned:** on-time delivery, client comms, project health, status
reporting. The PM is the client's primary contact from kickoff to offboarding.

**Decides alone:**
- Sequencing and assignment inside an agreed scope
- Scope changes **under $500 and under 2 hours** — logged, not approved
- Which contractor works which task
- When a deliverable is ready for the QA gate
- Rescheduling an internal checkpoint

**Must escalate:**
- Scope change **$500–$2,500** → propose to Joel, Joel approves
- Scope change **over $2,500, or any change to a client-visible date** → change
  order, client signature required
- Any RED trigger (see `01-delivery/project-red-escalation.md`)
- Client disputes an invoice or asks for a payment plan
- A contractor will miss a committed date

**Never does:** quote a price, offer a discount, promise a date not already in the
SOW, or send an invoice.

### Build (engineering contractor)

**Outcomes owned:** working software that passes the QA gate, on the committed
date.

**Decides alone:** implementation approach, libraries, architecture within the
agreed stack, refactors that don't change scope or timeline.

**Must escalate:** anything that changes the stack, adds a paid service, extends
the timeline, or touches client production data.

**Never does:** communicate directly with the client about scope, dates, or money.
Technical clarification in the client channel is fine and encouraged.

### Design

**Outcomes owned:** design deliverables that pass the QA gate and match the brief.

**Decides alone:** visual direction inside an approved brief, component and system
choices, which concepts to show.

**Must escalate:** more than two revision rounds requested; a brief that has
materially changed; anything requiring new brand decisions from the client.

### Marketing

**Outcomes owned:** content and campaign deliverables, on schedule.

**Decides alone:** channel tactics inside an agreed strategy, creative variations,
posting schedule.

**Must escalate:** spend changes, any claim about a client's results that isn't
already substantiated, anything published under the client's name that hasn't been
approved.

## The escalation thresholds, in one place

These three numbers appear in several documents. **This is the source of truth.**
If another file disagrees, that file is wrong.

| Situation | Who decides |
|---|---|
| Scope change < $500 **and** < 2 hours | PM decides alone, logs in Linear |
| Scope change $500–$2,500 | PM proposes → Joel approves → logged |
| Scope change > $2,500 **or** any client-visible date change | Change order, client signs, see `01-delivery/scope-change-protocol.md` |
| Discount of any size | Joel only, and only with a scope reduction attached |
| Anything that moves money | Joel only, always |

## Decision rights

- **Joel decides alone:** who holds which role, and every threshold on this page.
- **Escalate when:** a decision doesn't obviously belong to anyone. Then it gets
  added to this file, so it is only ambiguous once.

## Definition of done

A contractor facing a decision can find it on this page in under thirty seconds,
or knows immediately that it escalates.

## Related

- [Operating charter](operating-charter.md)
- [RACI matrix](raci-matrix.md)
- [Scope change protocol](../01-delivery/scope-change-protocol.md)
- [Project red escalation](../01-delivery/project-red-escalation.md)
- [Onboarding path](../04-team/onboarding-path.md)

## Assumptions

- **The $500 / $2,500 thresholds are a best-practice guess, not Alivio policy.**
  They are calibrated so roughly 80% of small changes clear without Joel on a
  $5K–$30K engagement. Joel must confirm — set too low, everything escalates and
  the OS fails its own goal; set too high, margin leaks silently.
- Assumes the PM archetype is trusted with client communication. If Joel wants to
  keep all client contact, say so — it is a defensible choice, but it makes "Joel
  off for two weeks" impossible and several documents change.
- **Past ~8 people:** split PM into Delivery Lead (owns the portfolio) and PM
  (owns one project). Not needed at 4–6 concurrent clients.
