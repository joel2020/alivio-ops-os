# AR Chase Sequence

**Owner:** Joel (Principal) · **Trigger:** An invoice passes its due date · **Cadence:** Swept Tuesday and Friday · **Last reviewed:** 2026-07-26

## Purpose

Chase every overdue invoice on a fixed schedule so that no invoice ages past 45
days without someone having deliberately decided not to chase it.

This is Alivio's most expensive stated pain, and it is measurable: **$12,000 across
two RLTRS milestones aged 11 and 18 days with no chase having fired at all.** Not
a judgment failure — there was no sequence to fire.

The whole point is removing the decision. Chasing is uncomfortable, so it gets
deferred; a schedule that runs regardless makes it routine rather than a
confrontation someone has to choose to start.

## The sequence

Day 0 is the **due date**, not the invoice date.

| Tier | Day | From | Tone | Intent |
|---|---|---|---|---|
| **1** | Day 1 | PM | Friendly, assumes an oversight | "This is due — here it is again" |
| **2** | Day 7 | PM, Joel cc'd | Firm, factual | Escalation is visible without being stated |
| **3** | Day 14 | Joel direct | Direct, personal | Ask what is actually going on; offer a payment plan |
| **4** | Day 21 | Joel | Formal | Stop-work notice: work pauses at day 30 |
| **5** | Day 30 | Joel | Formal | Work stops. Late fee applies. Final notice before escalation |
| **6** | Day 45 | Joel | — | Decision required: collections, write-off, or a documented exception |

Copy for tiers 1–5 is in `../05-templates/invoice-chase-emails.md`.

## Rules

- **Every tier fires on schedule.** Skipping a tier because the client is nice is
  how day 45 arrives. The sequence being automatic is what makes it not personal.
- **Nothing sends without Joel's approval.** Drafted automatically, reviewed, sent
  by a human. Money is never automatic.
- **Pause on genuine dispute.** If the client disputes the work, the sequence stops
  and it becomes a delivery conversation. Resume when resolved. "I'll look into it"
  is not a dispute — that is silence with better manners.
- **A payment plan resets the clock**, but only once, and only in writing with
  dates.
- **Stop-work is real.** A stop-work notice that does not result in stopped work
  teaches the client that Alivio's deadlines are decorative. If Joel will not stop,
  do not send tier 4.
- **Never chase a client the PM is mid-delivery with, without telling the PM.**
  Walking into that conversation blind damages the relationship the PM is holding.

## The twice-weekly sweep

Tuesday and Friday. Automated in Phase 3.

1. Pull every unpaid invoice past its due date
2. Bucket by age: 1–7, 8–14, 15–30, 31–45, 45+
3. Match each to its tier
4. Draft the appropriate email, using client history and prior tone
5. Present to Joel as a list with drafts attached, unsent
6. Joel reviews, edits, sends
7. Log every touch against the invoice

**Twice weekly, not weekly**, because a weekly sweep can let a tier slip by up to
six days, and tier boundaries are days 1 and 7.

## AR aging buckets

Reported on the dashboard and at every cash review:

| Bucket | Meaning |
|---|---|
| Current | Not yet due |
| 1–30 days | Normal friction |
| 31–60 days | Problem — Joel personally involved |
| 60+ days | Assume it will not be paid without escalation; provision accordingly |

**Anything over 30 days is a RED trigger on its project** — see
`../01-delivery/project-red-escalation.md`.

## Decision rights

- **PM decides alone:** sending tiers 1–2 after Joel's approval; flagging a dispute.
- **Joel decides alone:** all of tiers 3–6, stop-work, payment plans, write-offs,
  collections, and any exception.
- **Escalate when:** a client disputes, asks for a plan, or goes silent through
  tier 3.

## Definition of done

No invoice ages past 45 days without a logged decision. Every overdue invoice has
had every tier fire on schedule, or a written reason it did not.

## Related

- [Invoicing policy](invoicing-policy.md)
- [Invoice chase emails](../05-templates/invoice-chase-emails.md)
- [Cash flow review](cash-flow-review.md)
- [Project red escalation](../01-delivery/project-red-escalation.md)
- [Scorecard](../06-metrics/scorecard.md)

## Assumptions

- **The tier days (1/7/14/21/30/45) are best-practice defaults**, calibrated to
  Net 7. On Net 30 they would shift. They are aggressive by design because the
  observed failure was total absence of chasing, not chasing too gently.
- Assumes Joel is willing to enforce stop-work. **If not, tier 4 should be removed
  rather than bluffed** — an unenforced threat is worse than no threat.
- AR data is queryable from `../08-automation/lib/ledger.py`, and the sweep runs
  Tuesday and Friday via launchd. It is only as complete as the invoices Joel has
  recorded.
