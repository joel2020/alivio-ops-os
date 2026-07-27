# Client Communication Standard

**Owner:** PM · **Trigger:** Every client interaction · **Cadence:** Continuous · **Last reviewed:** 2026-07-26

## Purpose

Alivio's stated pain: *client comms scattered across channels*. Today a client
conversation might live in WhatsApp, a second thread in email on a different
account, and the work in Linear — so nobody can reconstruct what was agreed
without asking Joel, and a decision made on a call exists only in someone's memory.

What breaks without it: the same argument as scope creep, but worse, because there
is no artifact at all. A phone call is fine; a phone call that is the *only* record
of a decision is not.

## The rule

**Every client has exactly one channel of record, declared at kickoff.**

Everything that matters lands there. Other channels may exist for convenience —
the client will text, and that is fine — but anything decided elsewhere gets
**echoed into the channel of record within one business day**, by the PM, in
writing.

The echo is not bureaucracy. It is the difference between "we agreed on the call"
and a link to the message where it was agreed.

## Choosing the channel of record

Pick one at kickoff and write it in the kickoff notes:

| Channel | Use when | Watch out for |
|---|---|---|
| **Email thread** | Default. Client is not technical, or is enterprise. | Threads fork; always reply-all on the original |
| **Shared Slack/Teams channel** | Client already lives there and will add us | Retention limits on free plans — export at close |
| **WhatsApp group** | Client's actual habit, common with LatAm clients | Not searchable by anyone but the account holder; **highest echo discipline required** |
| **Linear** | Technical clients comfortable in the tracker | Non-technical stakeholders will not read it |

**If the client's real habit is WhatsApp, use WhatsApp** — a channel of record the
client ignores is not a record. But WhatsApp raises the echo requirement, because
one logged-out phone makes the whole history unreadable to the business. Decisions
from WhatsApp get promoted to Obsidian weekly, not eventually.

## Response SLAs

| Situation | Response within |
|---|---|
| Client asks a question, business hours | 1 business day |
| Client reports something broken in production | 4 business hours, acknowledged even if unsolved |
| Client asks for a scope change | 1 business day to acknowledge, 3 to price |
| Client goes quiet on a blocker | PM chases at day 2, day 5, escalates to Joel at day 7 |

**Acknowledged is not solved, and acknowledging counts.** "Got it, looking at this,
answer by Thursday" inside a day beats a complete answer in four.

## Who talks to whom

- **PM is the client's primary contact** from kickoff to offboarding.
- **Build, Design, Marketing** may answer technical or craft questions directly in
  the channel. They never discuss scope, dates, or money — those route to the PM,
  who routes money to Joel.
- **Joel** owns the account relationship: commercial conversations, escalations,
  and anything about the relationship itself.
- **The client names one decision-maker at kickoff.** Feedback from anyone else is
  logged but not acted on until the decision-maker confirms. This single rule
  prevents most revision-round inflation.

## Weekly status report

Every active project gets one, every Wednesday, in the channel of record, using
`../05-templates/weekly-status-report.md`. Sent even when the news is "no change" —
especially then. Silence is the thing clients escalate about.

## What never happens in a client channel

- Disagreements between Alivio people. Resolve internally, respond with one voice.
- Blaming a contractor by name.
- Committing to a date the PM has not confirmed with whoever will do the work.
- Quoting a price. Ever, by anyone but Joel.
- Speculating about a cause before it is known. "We're investigating" is complete.

## Decision rights

- **PM decides alone:** tone, timing inside SLA, what to escalate.
- **Joel decides alone:** anything commercial, and any message where the
  relationship itself is at stake.
- **Escalate when:** the client is unhappy about something other than the work
  itself.

## Definition of done

Anyone can reconstruct what was agreed with a client, and when, without asking a
person.

## Related

- [Kickoff](kickoff.md)
- [Weekly status report](../05-templates/weekly-status-report.md)
- [Scope change protocol](scope-change-protocol.md)
- [Project red escalation](project-red-escalation.md)
- [Decision log](../04-team/decision-log.md)

## Assumptions

- SLAs (1 business day, 4 hours for production) are best-practice guesses. They
  should appear in the SOW so they are a mutual commitment rather than a private
  standard — a client who does not know the SLA cannot be satisfied by it.
- **The WhatsApp risk is live, not hypothetical:** the RLTRS client group currently
  sits in an account that is logged out, meaning the business cannot read its own
  client history. The weekly promotion to Obsidian is the mitigation.
- Assumes one decision-maker per client. Committees need a different rule and are
  a disqualifier in `../02-sales/icp-and-disqualifiers.md` for exactly this reason.
