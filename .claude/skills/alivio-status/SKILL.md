---
name: alivio-status
description: Generate a client-facing weekly status report for an Alivio project from raw notes, commits, or Linear activity. Use when Joel asks for a status report or client update, asks what to tell a client this week, says it is time for the Wednesday reports, or asks for a project roll-up across all clients.
---

# Write a status report

Sent every Wednesday, per active project, in that client's channel of record —
**even when nothing changed, especially then.** Silence is what clients escalate
about; a boring report is a client who is not worried.

Ten minutes to write. If it takes longer it is too long to read.

## First, get the computed picture

```bash
cd ~/alivio-ops-os/08-automation
python3 lib/ops.py project-status-rollup
```

That gives stage, days in stage against the limit, computed health and why, and
which reports are due. **Use it rather than reading the stage off a note** —
Linear and the data file are the source of truth, and health is computed from
the rules, not from how the week felt.

## The template

From `05-templates/weekly-status-report.md`:

```
Subject: [PROJECT] — status, week of [DATE]

Hi [NAME],

Where we are: [Stage] — [one sentence in plain language]

Shipped this week
- [Thing, and what it means for them]

In progress
- [Thing] — expected [DATE]

Waiting on you
- [Input] — needed by [DATE] to hold the [MILESTONE] date

Timeline: On track for [DATE] / Moved to [DATE] because [REASON]

Scope changes to date: [N] changes, [N] hours, [$ charged / no charge]

Anything else: [risks, decisions needed, or delete]

[PM NAME]
```

## The rules that make it work

- **Lead with the timeline.** Some clients read only that line.
- **Name a slip the week it happens**, not the week it becomes undeniable.
  Clients forgive slippage they hear about early and remember slippage they
  discover.
- **"Waiting on you" is the highest-leverage section.** Naming it weekly, with a
  date and a consequence, prevents most client-caused delay — and makes the
  delay clause fair if it is ever invoked. **Delete the heading entirely when
  nothing is outstanding.** Never write "nothing at this time" — it dilutes the
  section for the week it matters.
- **Always show cumulative scope changes, including unbilled ones.** A client
  seeing "3 changes, 5.5 hours, no charge" values the work more, and the fourth
  request lands differently.
- **No internal detail.** Which contractor did what, tooling, internal friction —
  none of it is the client's business.
- **No apologising for a normal week.** A week where the plan happened is a good
  week.

## Before sending

**Escalate to Joel first** if the report would be the first time the client
learns of a slip they will be unhappy about. Joel hears that before the client
does.

**Never send it yourself.** Draft, show Joel or the PM, they send.

## Reference

- `05-templates/weekly-status-report.md`
- `01-delivery/client-communication-standard.md` — channel of record, SLAs
- `01-delivery/project-lifecycle.md` — stages and health rules
- `01-delivery/scope-change-protocol.md` — what counts as a revision round
