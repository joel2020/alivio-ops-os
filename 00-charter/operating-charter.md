# Operating Charter

**Owner:** Joel (Principal) · **Trigger:** Quarterly review, or any change to services/pricing · **Cadence:** Quarterly · **Last reviewed:** 2026-07-26

## Purpose

This is the document every other file in the OS defers to. If two documents
disagree, this one wins and the other gets fixed. If a decision isn't covered
anywhere, it gets decided here and written down, so it is decided once.

What breaks without it: every new contractor re-learns Alivio by asking Joel,
which is the exact dependency the OS exists to remove.

## What Alivio Studios does

A four-service agency run by one operator and a contractor bench.

| Service line | What it is | Typical range |
|---|---|---|
| **AI builds** | Agents, automations, RAG systems, LLM integrations | $12K–$30K+ |
| **Web development** | Product builds, marketing sites, platform work | $8K–$30K |
| **Design** | Brand, UI, design systems | $5K–$15K |
| **Marketing** | Content, campaigns, ad creative | $3K–$10K, or retainer |

Engagements run **4–8 weeks** typically, with **4–6 clients concurrent**. Revenue
is an even mix of fixed-scope projects and monthly retainers.

Alivio Search Partners is Alivio Studios' own product, not a client. It competes
for the same contractor hours as client work and is scheduled the same way — the
only difference is that it has no external deadline, which means it is always the
thing that slips. That is a deliberate choice, not an accident.

## Who we work for

See `02-sales/icp-and-disqualifiers.md` for the enforceable version. In short:
operators who own their outcome and can make a decision in one meeting.

## How we work

**Six commitments that constrain what we will agree to.**

1. **One owner per project.** A named PM owns delivery and client communication.
   Joel is not the default PM; when Joel is the PM, that is written down as an
   exception with an end date.
2. **Scope is written before work starts.** No build begins without a signed SOW.
   The cost of skipping this is not "some rework" — it is an unwinnable argument
   about what was promised, months later, with money attached.
3. **Two revision rounds per deliverable.** Defined in
   `01-delivery/scope-change-protocol.md`. This number appears in the SOW, the
   change-order template, and the QA gate, and it is the same number in all three.
4. **Nothing goes to a client without passing the QA gate.** Including from Joel.
5. **Money is never automatic.** No invoice sends, no payment runs, no refunds
   happen without a human approving that specific transaction.
6. **Client communication happens in the client's channel of record**, declared at
   kickoff, and nowhere else. See `01-delivery/client-communication-standard.md`.

## What we refuse

Stated plainly so a contractor can say no without checking:

- **No work without a signed SOW and deposit received.** Not "signed and the
  deposit is coming." Received.
- **No unbounded revision cycles.** Round three is a change order, every time.
- **No spec work or paid-in-exposure arrangements.**
- **No taking over a build we cannot inspect first.** Rescue work requires a paid
  audit before a fixed-price quote.
- **No accepting a deadline set by someone who is not resourcing it.**
- **No discount without a scope reduction attached.** Price flexes when scope
  flexes; a bare discount teaches the client the first number was invented.
- **No client contact in a channel that leaves no record.** A phone call is fine;
  a phone call that is the only artifact of a decision is not.

## Tool stack, and what each is the source of truth for

The OS fits these tools. Nothing here proposes replacing them.

| Tool | Source of truth for | Not for |
|---|---|---|
| **Linear** | All work: issues, milestones, project stage, due dates | Knowledge, decisions |
| **Obsidian** | Client knowledge, meeting notes, decision log | Task tracking |
| **GitHub + Vercel** | Code, deploys, environments | Anything a client reads |
| **Granola** | Meeting transcripts | Decisions — those get promoted to the decision log |
| **Claude / ChatGPT** | Leverage on drafting, review, analysis | Anything that sends externally unreviewed |
| **This OS** | Policy, process, and definitions | Live data |

The rule that keeps this from rotting: **a fact lives in exactly one of these.**
If a project's stage is in both Linear and a Notion page, one of them is lying and
you can't tell which.

## Decision rights

- **Joel decides alone:** pricing, discount authority, who we take on, who we
  refuse, contractor rates, anything that moves money, final QA sign-off on first
  delivery to a new client.
- **PM decides alone:** sequencing within an agreed scope, which contractor does
  what, scope changes under $500 and 2 hours, client comms inside the standard.
- **Escalate to Joel when:** scope change exceeds $500 or touches the timeline; a
  project meets any RED criterion; a client disputes an invoice; a contractor is
  not going to hit a committed date.

Full matrix in `roles-and-decision-rights.md`.

## Definition of done

This charter is working when a contractor can answer "can we agree to this?"
without messaging Joel, and is right.

## Related

- [Roles and decision rights](roles-and-decision-rights.md)
- [RACI matrix](raci-matrix.md)
- [Cadence calendar](cadence-calendar.md)
- [ICP and disqualifiers](../02-sales/icp-and-disqualifiers.md)
- [Scope change protocol](../01-delivery/scope-change-protocol.md)

## Assumptions

- **Alivio Studios is the agency; Alivio Search Partners is its own product, not a
  client.** Inferred from the `alivio.studio.ops@` operations address and from the
  live client set (RLTRS, Bravo Mechanical, itslitneon) sitting alongside
  `alivio-platform` as an owned asset. If ASP is actually a separate company,
  several finance documents need splitting.
- Service-line price bands are inferred from observed deals: RLTRS at $29,000
  fixed-scope, and Alivio's own published $5–10K install / $2–3K retainer. **Joel
  must confirm these before they are quoted from.**
- The four contractor archetypes (Build, Design, PM, Marketing) are treated as
  roles rather than named people, so one person can hold several.
