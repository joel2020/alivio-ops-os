# Knowledge Base Map

**Owner:** PM · Joel accountable · **Trigger:** New client, new tool, or the monthly review · **Cadence:** Monthly review · **Last reviewed:** 2026-07-26

## Purpose

Say where each kind of information lives, so nobody has to guess and nothing gets
written in two places. Two copies of a fact means one of them is wrong and you
cannot tell which.

What breaks without it: knowledge scatters across Obsidian, Linear, chat threads,
and Joel's head — which is the state this OS exists to end.

## Where everything lives

| Information | Lives in | Owner | Never in |
|---|---|---|---|
| Policy, process, definitions | **This OS** (`alivio-ops-os/`) | Joel | Obsidian, chat |
| Active work, issues, milestones, stage | **Linear** | PM | Obsidian |
| Pipeline and deals | **Linear** (pipeline project) | Joel | Spreadsheets |
| Client knowledge, meeting notes, context | **Obsidian**, per-client folder | PM | Linear |
| Decisions and reasoning | **Obsidian** decision log | PM | Chat, transcripts alone |
| Meeting transcripts | **Granola** | — | — |
| Code, deploys, environments | **GitHub + Vercel** | Build | — |
| Credentials | **Password manager** | Joel | Chat, email, code, notes |
| Client conversations | **Channel of record** per client | PM | Anywhere else |
| Financial records | **Accounting tool** *(not yet chosen)* | Joel | Spreadsheets |
| Contractor register, agreements, tax forms | **Joel's records** | Joel | — |

## The Obsidian structure

```
Clients/
  [Client Name]/
    00-context.md          who they are, what they care about, how they work
    01-decisions.md        the decision log for this client
    02-meetings/           notes, newest first
    03-deliverables/       what was delivered, when
    99-postmortem.md       written at Delivered
Company/
  decisions.md             company-wide decision log
  win-loss-log.md          every deal post-mortem
  contractor-register.md   who, archetype, rate, dates
```

Four files per client. Enough to hold context, few enough that nobody has to decide
where something goes.

## The rules

- **One home per fact.** Anything that would naturally live in two places gets a
  link from the second to the first.
- **Client context is written at kickoff**, not accumulated. Fifteen minutes then
  beats an archaeology exercise later.
- **Transcripts are raw material.** A Granola transcript is not a decision record —
  the decision gets promoted to the log by a human, or it is not findable.
- **Credentials never appear in notes.** Password manager, always, no exceptions.
- **If it is only in Joel's head, it is not in the knowledge base.** That is the
  whole point.

## The monthly review — 15 minutes

With the month-end close:

1. Any client folder missing `00-context.md`?
2. Any decisions from this month not logged?
3. Any OS document whose `Last reviewed` is over a quarter old?
4. Anything written in two places?
5. Fix **one** thing. Not all of it — one. A review that requires an afternoon
   gets skipped, and a review that fixes one thing a month fixes twelve a year.

## Decision rights

- **PM decides alone:** structure inside a client folder, what context to capture.
- **Joel decides alone:** what tool holds what, and any change to this map.
- **Escalate when:** something has no obvious home. It gets added to the table
  above so it is only ambiguous once.

## Definition of done

Every active client has a folder with context and a decision log, and every
category in the table has exactly one home.

## Related

- [Decision log](decision-log.md)
- [SOP writing standard](sop-writing-standard.md)
- [Client communication standard](../01-delivery/client-communication-standard.md)
- [Operating charter](../00-charter/operating-charter.md)

## Assumptions

- Assumes Obsidian and Linear stay as-is. Consistent with the stated constraint not
  to propose replacements.
- **Assumes a password manager exists.** None was named in the stack — if there is
  not one, that is a gap worth closing before the next credential handoff.
- **Assumes an accounting tool will be chosen.** The table has a row for it with
  nothing in it, which is honest rather than aspirational.
