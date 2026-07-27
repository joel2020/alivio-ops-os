# Scope Change Protocol

**Owner:** PM · **Trigger:** Anyone asks for something not in the SOW · **Cadence:** As it happens · **Last reviewed:** 2026-07-26

## Purpose

Fixed-scope work loses its margin one small favour at a time. Nobody ever approved
the erosion; each individual "sure, quick thing" was reasonable. This document
makes the accumulation visible while each request is still small enough to price.

What breaks without it: the fourth week of a six-week project contains two weeks
of unbilled work, and the argument about who agreed to what happens with money on
the table. This is Alivio's stated pain — *scope and payment terms go fuzzy* — and
this file is the direct answer to it.

## The rule

**Two revision rounds are included per deliverable.** A round is one consolidated
set of feedback, delivered at once. Feedback arriving in six messages over four
days is still one round — but see the counting rules, because that behaviour has
its own cost.

Round three onward is a change order, priced as a fixed amount. Every time. The
moment this is negotiated once, it is no longer a policy.

**Alivio does not bill hourly.** Every client-facing number is a fixed price for
a defined piece of work, including change orders. Hours are still estimated
internally — they are how effort is costed and capacity is planned — but the
client never sees an hourly rate and never receives a variable invoice. That is
deliberate: an hourly change order invites a conversation about how long
something *should* have taken, which is the least productive argument available
and one Alivio cannot win.

## Steps

1. **Catch it.** A scope change is anything not written in the SOW deliverables
   list. Including things that are "obviously implied." Especially those.

2. **Do not start it.** Not even the small ones. Starting work is the approval,
   whatever was said.

3. **Size it.** PM estimates the effort in hours *internally*, converts it to a
   fixed price, and quotes only the price. If unsure, size it high — a price
   that turns out generous is a good outcome; one that turns out short is
   unrecoverable, because there is no hourly true-up to fall back on.

4. **Route it by the thresholds.** These are the same numbers as
   `../00-charter/roles-and-decision-rights.md`.

   | Size | Route |
   |---|---|
   | Under $500 **and** under 2 hours of effort | PM approves, logs in Linear with the `scope-change` label. No client paperwork. |
   | $500–$2,500 | PM writes it up → Joel approves → PM confirms **in writing** in the channel of record → logged |
   | Over $2,500 **or** any client-visible date moves | Change order. Client signs. Work does not start before the signature. |

5. **Write it down regardless of size.** Every change gets a Linear comment on the
   project: what, why, who asked, internal effort, price, and which tier. The under-$500 ones matter
   most here — they are individually trivial and collectively how a project bleeds.

6. **Reconcile at the weekly status report.** The report shows cumulative scope
   changes to date, in changes and dollars — **never in hours**. The client
   seeing "3 changes absorbed, no charge" is worth more than the goodwill of
   hiding it, and it makes the fourth request land differently. Showing hours
   would invite exactly the how-long-should-this-take argument that fixed
   pricing exists to avoid.

## Counting revision rounds

- A round is **one consolidated set of feedback**.
- Feedback trickling in across several days is still one round, but the PM
  consolidates it and replies once with the full list. Trickle-feedback is a
  symptom of an unclear decision-maker — fix that, don't police the count.
- **Clarifying questions are not a round.**
- **Our defects are not a round.** If it does not match the SOW, fixing it is
  finishing the work, not revising it.
- **A change of mind is a round**, even if the client calls it a correction.

## What is never in scope without a signed change order

- New deliverables of any size
- Anything that moves a client-visible date
- Work for a stakeholder who is not the named decision-maker
- Migrating, integrating with, or supporting a system not named in the SOW
- Ongoing maintenance after handoff — that is a retainer, quoted separately

## Decision rights

- **PM decides alone:** anything under $500 and 2 hours; whether something counts
  as a defect or a revision.
- **Joel decides alone:** everything $500 and above; whether to waive a charge.
- **Escalate immediately when:** the client disputes that something is out of
  scope. Do not argue it in the channel — that is a Joel conversation.

## Definition of done

Every change is either in the SOW, logged under $500, approved by Joel, or on a
signed change order. There is no fifth category.

## Related

- [Scoping and SOW](scoping-and-sow.md)
- [Project lifecycle](project-lifecycle.md)
- [Change order template](../05-templates/change-order.md)
- [Roles and decision rights](../00-charter/roles-and-decision-rights.md)
- [Client communication standard](client-communication-standard.md)

## Assumptions

- **Two rounds is the number used everywhere in this OS** — SOW template, QA gate,
  change order. Joel must confirm; if it becomes three, three files change together
  or the OS contradicts itself.
- **Alivio does not bill hourly** (confirmed by Joel 2026-07-27). Change orders
  are fixed-price. The 2-hour figure in the threshold table is an *internal
  effort* measure for deciding who approves, never a billing unit, and it never
  appears in a client document.
- Assumes fixed-scope work. **Retainers need a different mechanism and it is not
  yet written.** Since Alivio does not bill hourly, a retainer cannot be an hour
  pool — it has to be a defined monthly scope, or a capacity commitment with an
  explicit list of what is in and out. That is a real gap, and the wrong answer
  is letting a retainer quietly become unlimited requests.
