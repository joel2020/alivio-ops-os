# Invoice Chase Emails

**Owner:** Joel (Principal) · **Trigger:** AR sweep, Tuesday and Friday · **Cadence:** Per the tier schedule · **Last reviewed:** 2026-07-26

## Purpose

The actual copy for each escalation tier, so chasing is a send rather than a
writing task. Most invoices go unchased because writing the message is
uncomfortable — pre-written copy removes the discomfort and the delay together.

Tiers and timing are defined in `../03-finance/ar-chase-sequence.md`. **Nothing
here sends without Joel's approval.**

Replace `[BRACKETS]`. Keep the tone — it escalates deliberately, and skipping a
tier's tone is how day 45 arrives.

---

## Tier 1 — Day 1 after due date

**From:** PM · **Assume it is an oversight, because it usually is.**

> **Subject:** Invoice [NUMBER] — [CLIENT] — due [DATE]
>
> Hi [NAME],
>
> Quick one — invoice [NUMBER] for [AMOUNT] was due [DATE]. Attaching it again
> here in case it needs re-sending to anyone on your side.
>
> If it's already in motion, ignore me entirely.
>
> [PM NAME]

Short, warm, no friction. Most invoices are paid at this tier.

---

## Tier 2 — Day 7

**From:** PM, **Joel cc'd.** The cc is the escalation; it is never mentioned.

> **Subject:** Re: Invoice [NUMBER] — [CLIENT] — now 7 days overdue
>
> Hi [NAME],
>
> Following up on invoice [NUMBER] for [AMOUNT], which was due [DATE] and is now
> 7 days past.
>
> Could you let me know when it's scheduled for payment? If there's a problem
> with the invoice itself, or something you need from us to process it, tell me
> and I'll fix it today.
>
> [PM NAME]

Factual, no apology, one clear question. Offering to fix a problem gives an easy
route to the real reason.

---

## Tier 3 — Day 14

**From:** Joel, directly. Personal, not procedural.

> **Subject:** Invoice [NUMBER] — can we sort this out?
>
> Hi [NAME],
>
> Invoice [NUMBER] for [AMOUNT] is now two weeks past due and I haven't been able
> to get a date from your team.
>
> I'd rather have a straight conversation than keep sending reminders. If cash
> flow is tight, say so and we'll work out a schedule that fits — I'd much prefer
> that to silence. If something about the work isn't right, I want to hear it.
>
> Can you reply today or tomorrow with either a payment date or what's in the way?
>
> [JOEL]

**The offer of a payment plan is what makes this work.** A client avoiding you
because they cannot pay will engage with an offer to solve it.

---

## Tier 4 — Day 21 — stop-work notice

**From:** Joel. Formal. Only send if Alivio will actually stop.

> **Subject:** Invoice [NUMBER] — work pausing [DATE]
>
> [NAME],
>
> Invoice [NUMBER] for [AMOUNT] is now 21 days past due, and I haven't had a
> response to my last message.
>
> I need to let you know that work on [PROJECT] will pause on [DATE — day 30]
> unless payment is received or we've agreed a schedule before then. That's not a
> position I want to be in, and I'd still much rather resolve this.
>
> Please reply with a payment date, or let me know a time to talk this week.
>
> [JOEL]

A stop-work notice that does not result in stopped work teaches the client that
Alivio's deadlines are decorative. **If Joel will not stop, do not send this.**

---

## Tier 5 — Day 30 — work stopped

**From:** Joel. Formal. State facts, no anger.

> **Subject:** [PROJECT] — work paused, invoice [NUMBER]
>
> [NAME],
>
> As set out on [DATE], work on [PROJECT] is paused as of today. Invoice [NUMBER]
> for [AMOUNT] is 30 days past due.
>
> Per our agreement, a late fee of 2% per month now applies to the outstanding
> balance.
>
> Everything completed to date is safe and will be handed over as soon as the
> account is settled. We can resume within [N] business days of payment, though
> the timeline will need re-planning against current capacity.
>
> I'd like to resolve this. Please reply with a payment date or a time to talk.
>
> [JOEL]

Note the deliberate absence of threat. The facts are severe enough.

---

## Tier 6 — Day 45 — decision required

No template. Day 45 is a **decision**, not a message: collections, write-off, or a
documented exception with a reason. Log whichever it is.

---

## Special cases

**Client disputes the work** → stop the sequence. This is now a delivery
conversation, per `../01-delivery/project-red-escalation.md`. Resume only when
resolved.

**Client asks for a payment plan** → Joel only. In writing, with dates. Resets the
clock **once**.

**Client goes completely silent through tier 3** → do not keep emailing. Change
channel: phone the decision-maker.

**Client is mid-delivery with the PM** → tell the PM before any tier 3+ message.
Walking into that conversation blind damages the relationship the PM is holding.

## Decision rights

- **PM decides alone:** sending tiers 1–2 once Joel has approved the draft.
- **Joel decides alone:** tiers 3–6, stop-work, plans, write-offs, and any
  exception.

## Definition of done

Every overdue invoice has had the correct tier sent on schedule, or a logged reason
it did not.

## Related

- [AR chase sequence](../03-finance/ar-chase-sequence.md)
- [Invoicing policy](../03-finance/invoicing-policy.md)
- [Project red escalation](../01-delivery/project-red-escalation.md)

## Assumptions

- Tone assumes Alivio's clients are small operator-led businesses where the
  decision-maker reads their own email. Enterprise AP departments need a different,
  more procedural register.
- **The 2% late fee must be in the signed SOW** to be referenced at tier 5.
  Referencing a term that is not in the contract is worse than not referencing one.
- Assumes Joel will enforce stop-work. If not, delete tiers 4–5 rather than bluff.
