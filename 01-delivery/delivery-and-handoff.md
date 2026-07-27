# Delivery and Handoff

**Owner:** PM · **Trigger:** Client approves the final deliverable · **Cadence:** Once per project · **Last reviewed:** 2026-07-26

## Purpose

Get the work into the client's hands so completely that they never need Alivio to
use it — and get the final invoice out while goodwill is at its peak.

What breaks without it: a "finished" project that quietly still depends on Alivio,
generating unpaid support requests for months, with the final invoice unsent
because the work "wrapped up" informally.

**The single most expensive mistake in delivery is a late final invoice.** Approval
day is the best collection day Alivio will ever have. It gets worse every day
after.

## Steps

1. **Confirm approval in writing** in the channel of record. A verbal yes on a
   call is echoed and confirmed before anything else proceeds.

2. **Issue the final invoice the same day.** Not at month end, not at the next
   billing run. The same day. See `../03-finance/invoicing-policy.md`.

3. **Transfer everything.** Nothing stays only in an Alivio account:
   - [ ] Repositories transferred or client added as owner
   - [ ] Hosting, domains, DNS moved to client accounts
   - [ ] Third-party services (analytics, CMS, email, AI provider keys) on client
         billing, in client accounts
   - [ ] Design source files delivered, organised, in the promised formats
   - [ ] Credentials handed over via a password manager, never in chat or email
   - [ ] Any Alivio-owned key that stays live is documented with its cost and an
         end date

4. **Write the handoff document.** This is the deliverable clients remember. What
   it contains:
   - What was built, in plain language, one paragraph
   - How to run, edit, or deploy it
   - Where everything lives — repos, hosting, accounts
   - Known limitations, stated plainly
   - Recurring costs the client now owns, with amounts
   - What to do when something breaks, and who to call
   - What is explicitly *not* covered

5. **Run the handoff session.** 30–45 minutes, recorded. Walk the document, watch
   them do the two things they will actually need to do. If they cannot do it while
   you watch, the document is wrong.

6. **Offer what comes next, once.** A retainer, a phase two, or nothing. Said once,
   clearly, at the moment of maximum goodwill — then dropped. Repeatedly pitching a
   client who just paid you is how a good delivery becomes a bad memory.

7. **Complete the offboarding checklist** —
   `../05-templates/offboarding-checklist.md`.

8. **Run the post-mortem** within 5 business days —
   `../02-sales/win-loss-capture.md`. Including on projects that went well;
   especially those, because nobody ever asks why something worked.

9. **Move to Closed only when the final invoice is paid.** Delivered and Closed are
   different stages for exactly this reason.

## Decision rights

- **PM decides alone:** handoff format, session scheduling, what goes in the doc.
- **Joel decides alone:** issuing the final invoice, any discount or write-off,
  whether to offer a retainer.
- **Escalate when:** the client will not confirm approval in writing, or asks for
  "one more small thing" before signing off. The second is a scope change and goes
  through the protocol, not through goodwill.

## Definition of done

The client can operate what was built without Alivio, the final invoice is issued,
and every credential and account is in the client's name or documented with an end
date.

## Related

- [Offboarding checklist](../05-templates/offboarding-checklist.md)
- [Project lifecycle](project-lifecycle.md)
- [Invoicing policy](../03-finance/invoicing-policy.md)
- [QA gate](qa-gate.md)
- [Win/loss capture](../02-sales/win-loss-capture.md)

## Assumptions

- Assumes clients want full ownership. Some prefer Alivio to keep hosting — that is
  a retainer with its own SOW, not an informal arrangement, and it must never be
  the default that happens by neglect.
- **The "same day" final invoice is a policy choice, not current practice.** It is
  the single highest-leverage change in this document given that $12,000 was
  observed aging 11 and 18 days.
- Assumes a password manager exists for credential transfer. If not, that is a tool
  gap worth closing before the next handoff.
