# Decision Log

**Owner:** PM (maintains) · Joel accountable · **Trigger:** Any decision that would be expensive to relitigate · **Cadence:** As decisions happen; reviewed monthly · **Last reviewed:** 2026-07-26

## Purpose

Record decisions with their **reasoning**, so they are not relitigated in six
months by people who have forgotten why. The reasoning is the valuable part —
anyone can see what was decided; almost nobody remembers what was known at the
time.

What breaks without it: the same debate recurs quarterly, and decisions get
silently reversed by people who never knew they were decisions.

The live example: an Alivio payment basis that required retrieving a meeting
transcript to settle months later. The decision had been made; it simply had not
been recorded anywhere findable.

## What gets logged

- Anything a client and Alivio agreed that is not in the SOW
- Any scope change over $500
- Any architectural or tooling choice that constrains later work
- Any pricing exception
- Any decision made on a call rather than in writing
- Any decision that reverses an earlier one
- Every RED project decision

**Not logged:** routine task-level choices. If it would not be surprising to
revisit it, it does not need a record.

## The format

Five lines. Long enough to be useful, short enough to actually get written.

```
## [YYYY-MM-DD] Short title

**Decided:** what was decided, one sentence
**By:** who decided
**Because:** the reasoning, and what was known at the time
**Alternatives:** what else was considered and why not
**Revisit if:** the condition that would make this worth reopening
```

`Revisit if` is what stops a log becoming a graveyard. A decision made under
constraints that no longer hold *should* be reopened, and naming the condition
makes that legitimate rather than a reversal.

### Example

```
## [2026-07-16] RLTRS payment basis

**Decided:** $4,000 for the week of Jul 16, then $500 every Friday until completion.
**By:** Joel and Jason, on the Jul 16 call.
**Because:** Client cash flow could not support the original milestone schedule.
  Weekly draws keep the engagement funded without a large single payment.
**Alternatives:** Original milestone schedule — rejected, client could not fund it.
  Pausing the engagement — rejected, momentum was worth more.
**Revisit if:** Weekly payments are missed twice, or scope expands past the
  original estimate.
```

## Where it lives

**Obsidian**, one note per client plus one for company-wide decisions. Not Linear
— Linear tracks work, Obsidian holds knowledge, and a decision is knowledge.

Client-specific decisions go in the client folder. Anything about how Alivio
operates goes in the company log and usually implies an OS change.

## The rules

- **Written within one business day** of the decision. Memory degrades faster than
  anyone expects, especially the reasoning.
- **Whoever made the decision writes it**, or the PM writes it and they confirm.
- **Never edited to look better.** A decision that turned out wrong stays as it
  was, with an outcome note appended. That is the entire value — a log of only
  good decisions teaches nothing.
- **Superseding, not deleting.** A reversal is a new entry linking to the old one.

## Monthly review

Fifteen minutes with the month-end close:

- Any decision whose `Revisit if` condition has been met?
- Any that turned out badly — what was the signal that was missed?
- Any that should become policy in this OS rather than staying a one-off?

That last question is how the OS improves. **A decision made three times is a
policy that has not been written down yet.**

## Decision rights

- **PM decides alone:** what goes in, format compliance.
- **Joel decides alone:** whether a decision becomes OS policy.
- **Escalate when:** a decision is being relitigated without its `Revisit if`
  condition being met. Point at the log rather than re-arguing it.

## Definition of done

Every qualifying decision is logged within one business day, with reasoning and a
revisit condition.

## Related

- [Knowledge base map](knowledge-base-map.md)
- [Project red escalation](../01-delivery/project-red-escalation.md)
- [Scope change protocol](../01-delivery/scope-change-protocol.md)
- [Win/loss capture](../02-sales/win-loss-capture.md)
- [SOP writing standard](sop-writing-standard.md)

## Assumptions

- Assumes Obsidian is where knowledge lives. Consistent with the stated stack.
- **Assumes decisions are made in identifiable moments.** Many drift into existence
  without ever being decided — the monthly review is the mechanism for catching
  those and making them explicit.
- Assumes Granola transcripts are available for meeting decisions. **A transcript
  is not a log** — the transcript is the raw material, the log entry is the
  artifact, and one of them is findable in six months.
