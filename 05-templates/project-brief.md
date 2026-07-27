# Project Brief

**Owner:** PM · **Trigger:** Project enters Scoped · **Cadence:** Once per project · **Last reviewed:** 2026-07-26

## Purpose

The internal counterpart to the SOW. The SOW is what the client signed; this is
what the team needs to know to build it — including the things you would never put
in a client document.

A contractor should be able to read this plus the SOW and start work without a
call. That is the test.

---

## Template

# [PROJECT NAME] — Project Brief

**Client:** [NAME] · **PM:** [NAME] · **Started:** [DATE] · **Target delivery:** [DATE]
**Value:** [$] · **SOW:** [link] · **Linear:** [link] · **Channel of record:** [where]

## The client in three lines

- **Who they are:** [business, size, what they sell]
- **Who we deal with:** [decision-maker name, role, how they like to work]
- **What they actually care about:** [the thing behind the brief]

## Why they hired us

[2–3 sentences. The real reason, which is often not the stated one. A client
buying a website may be buying credibility for a funding round.]

## What we're building

[Link to SOW section 2. Do not restate it — one source of truth.]

## What we're deliberately not building

[Link to SOW section 3, plus anything discussed internally and ruled out, with the
reason. This is where "we considered X, it's not worth it" gets recorded.]

## Technical context

- **Stack:** [what we're working in]
- **Access needed:** [repos, hosting, accounts, and who has it]
- **Constraints:** [anything that limits how we build]
- **Existing systems:** [what we integrate with, and what condition it's in]

## Team

| Role | Who | Committed dates | Budget (hours) |
|---|---|---|---|
| PM | | | |
| Build | | | |
| Design | | | |

## Watch out for

**The internal-only section.** Anything the team should know that would never go
in a client document:

- [Client is slow to respond — build buffer into review cycles]
- [Previous agency left the codebase in poor shape — see audit]
- [Decision-maker's boss has opinions and appears late]
- [Payment history: notes]

**This section is the most valuable part of the brief.** It is the institutional
memory that otherwise lives only in Joel's head, which is exactly what this OS
exists to fix.

## Success criteria

[The one sentence agreed at kickoff, in the client's words.]

## Risks

| Risk | Likelihood | If it happens |
|---|---|---|
| [thing] | H/M/L | [what we do] |

## Key dates

| What | When |
|---|---|
| Kickoff | |
| Client input deadline | |
| Midpoint checkpoint | |
| QA | |
| Client review | |
| Delivery | |

---

## Rules

- **Written by the PM before Build starts.** Not during.
- **Lives in Obsidian**, in the client folder. Linked from Linear.
- **Updated when reality changes**, particularly "watch out for."
- **Never shared with the client.** It contains internal judgments and should.

## Decision rights

- **PM decides alone:** everything in it.
- **Escalate when:** writing it reveals the SOW is not buildable as scoped. Better
  now than in week three.

## Definition of done

A contractor who has never met this client can read this and the SOW and start
work without asking a question.

## Related

- [Scoping and SOW](../01-delivery/scoping-and-sow.md)
- [SOW template](sow-template.md)
- [Project lifecycle](../01-delivery/project-lifecycle.md)
- [Knowledge base map](../04-team/knowledge-base-map.md)

## Assumptions

- Assumes a PM distinct from Joel. Where Joel is the PM, the brief still gets
  written — writing it is how the knowledge leaves his head, which is the point.
- Assumes contractors read it. Confirmed by the three questions in
  `../04-team/onboarding-path.md`.
