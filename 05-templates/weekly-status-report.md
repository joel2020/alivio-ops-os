# Weekly Status Report

**Owner:** PM · **Trigger:** Every Wednesday, per active project · **Cadence:** Weekly · **Last reviewed:** 2026-07-26

## Purpose

The artifact that stops anyone needing to ask "what's the status of X" — which is
one of Alivio's four stated pains and the one the 90-day goal most directly
depends on.

Sent **even when nothing changed**, especially then. Silence is what clients
escalate about; a boring report is a client who is not worried.

Ten minutes to write. If it takes longer, it is too long to read.

---

## Template

> **Subject:** [PROJECT] — status, week of [DATE]
>
> Hi [NAME],
>
> **Where we are:** [Stage] — [one sentence on what that means in plain language]
>
> **Shipped this week**
> - [Thing, and what it means for them]
>
> **In progress**
> - [Thing] — expected [DATE]
>
> **Waiting on you**
> - [Input] — needed by [DATE] to hold the [MILESTONE] date
> - *(Delete this heading entirely if nothing is outstanding. Never write "nothing
>   at this time" — it dilutes the section for the week it matters.)*
>
> **Timeline:** On track for [DATE] / Moved to [DATE] because [REASON]
>
> **Scope changes to date:** [N] changes, [N] hours, [$ charged / no charge]
>
> **Anything else:** [risks, decisions needed, or delete]
>
> [PM NAME]

---

## Rules

- **Send Wednesday**, in the channel of record. Same day every week — predictability
  is most of the value.
- **Lead with the timeline.** It is the only line some clients read.
- **Name a slip the week it happens**, not the week it becomes undeniable. Clients
  forgive slippage they hear about early and remember slippage they discover.
- **"Waiting on you" is the highest-leverage section.** Naming it weekly, with a
  date and a consequence, prevents most client-caused delay — and makes the delay
  clause fair if it is ever invoked.
- **Always show cumulative scope changes**, including unbilled ones. A client
  seeing "3 changes, 5.5 hours, no charge" values the work more, and the fourth
  request lands differently.
- **No internal detail.** Which contractor did what, tooling, and internal friction
  are not the client's business.
- **No apologising for a normal week.** A week where the plan happened is a good
  week.

## Decision rights

- **PM decides alone:** content, framing, what to include.
- **Escalate before sending when:** the report would be the first time the client
  learns of a slip they will be unhappy about. Joel hears that first.

## Definition of done

Every active project has a report sent every Wednesday, and no client has had to
ask for status.

## Related

- [Client communication standard](../01-delivery/client-communication-standard.md)
- [Project lifecycle](../01-delivery/project-lifecycle.md)
- [Scope change protocol](../01-delivery/scope-change-protocol.md)
- [Cadence calendar](../00-charter/cadence-calendar.md)

## Assumptions

- Assumes weekly is the right frequency for 4–8 week engagements. On a 3-week
  engagement, twice weekly is better.
- Assumes the client wants written status. Some prefer a call — the call still
  produces this artifact afterwards.
- **This is a strong Phase 3 candidate:** drafted automatically from Linear, edited
  and sent by the PM.
