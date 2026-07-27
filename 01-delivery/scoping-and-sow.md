# Scoping and SOW

**Owner:** Joel (Principal) · **Trigger:** Discovery complete, deal moving to Proposal · **Cadence:** Per deal · **Last reviewed:** 2026-07-26

## Purpose

Turn a conversation into a document that can be argued from months later. The SOW
is the contract that every downstream dispute resolves against — QA checks against
it, scope changes are measured from it, and the final invoice is justified by it.

What breaks without it: *scope and payment terms go fuzzy*, Alivio's stated pain.
The observed instance is instructive — a $4,000 payment basis that required
retrieving a meeting transcript to settle. That is what an under-specified
agreement costs, and it is cheap only because it was recoverable.

## Steps

1. **Run discovery before scoping.** 60–90 minutes. Output is written notes in
   Obsidian, not a proposal. Scoping from a qualification call is guessing.

2. **Write the deliverables list first, and make it countable.** Not "a marketing
   site" but "5 pages: home, services, about, careers, contact — responsive,
   CMS-editable." If you cannot count it, you cannot tell when it is done, and
   neither can the client.

3. **Write the exclusions list.** This matters more than the deliverables list. It
   is where "obviously implied" goes to be made explicit. Standard exclusions:
   - Content and copy, unless named as a deliverable
   - Photography, illustration, licensed assets
   - Hosting, domains, and third-party subscription costs
   - Integrations with systems not named here
   - Maintenance or support after handoff
   - Training beyond the handoff session
   - Work for stakeholders other than the named decision-maker

4. **Write acceptance criteria per deliverable.** One sentence each, checkable.
   "Done when the form submits and the lead appears in the client's CRM" is
   checkable. "Done when the site looks professional" is a future argument.

5. **Set the payment structure** — see `../03-finance/invoicing-policy.md`, which
   is the source of truth. Fixed-scope default: **40% deposit / 30% midpoint /
   30% on delivery**, Net 7.

6. **State the revision policy explicitly: two rounds per deliverable.** Same
   number as `scope-change-protocol.md` and the change-order template. It appears
   in the SOW so it is a mutual agreement rather than an internal rule the client
   discovers when it is enforced.

7. **State the client's obligations, with dates.** Most slipped projects are
   waiting on something the client owes: content, access, a decision, a review.
   List them, name the owner, give each a date, and state what happens when one
   slips — see the delay clause below.

8. **Name the decision-maker.** One person. Written in the SOW.

9. **State the SLAs** from `client-communication-standard.md`, so response times
   are a commitment both ways.

10. **Price it** using `../02-sales/proposal-and-pricing.md`. Joel only.

11. **Send for signature. Do not start.** Work begins when the SOW is signed *and*
    the deposit has landed — see `project-lifecycle.md`, stage 1.

## The delay clause

Every SOW contains it, because client-caused delay is the most common way a
fixed-price project loses money and the most awkward to raise once it is happening:

> Alivio's timeline assumes client inputs and approvals arrive by the dates listed.
> Where a client input is more than 5 business days late, Alivio may reschedule
> remaining milestones to the next available capacity, and the engagement end date
> moves accordingly. Delays beyond 20 business days may require re-scoping at
> then-current rates.

Say it at kickoff too, warmly, once. A clause the client meets for the first time
when it is invoked reads as a trap.

## Decision rights

- **Joel decides alone:** price, terms, what is in and out, whether to write a SOW
  at all.
- **PM decides alone:** nothing here. The PM may draft; Joel owns.
- **Escalate when:** n/a — Joel is the owner.

## Definition of done

A contractor who has never met the client can read the SOW and know exactly what
to build, what not to build, when it is due, and what "finished" means.

## Related

- [SOW template](../05-templates/sow-template.md)
- [Project brief](../05-templates/project-brief.md)
- [Scope change protocol](scope-change-protocol.md)
- [Invoicing policy](../03-finance/invoicing-policy.md)
- [Proposal and pricing](../02-sales/proposal-and-pricing.md)
- [QA gate](qa-gate.md)

## Assumptions

- **The 40/30/30 structure is a best-practice guess.** The one observed Alivio
  engagement (RLTRS) ran $4,000 up front plus $500 weekly, which is a different
  shape entirely. Joel must decide whether 40/30/30 is the standard and weekly
  draws are the exception, or the reverse.
- Assumes SOWs are signed electronically and the countersigned copy is filed.
  Where it is filed is not yet defined — a gap.
- **No legal review has happened.** The delay clause and the terms are operational
  drafting, not legal advice, and should be reviewed by a lawyer before they
  appear in a contract that matters.
