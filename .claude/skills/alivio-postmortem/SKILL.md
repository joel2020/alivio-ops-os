---
name: alivio-postmortem
description: Run a post-mortem on a closed Alivio deal or a delivered project, and append it to the win/loss log or decision log. Use when a deal is won or lost, a project is delivered or finished, Joel asks for a retro or lessons learned, asks why work was won or lost, or asks what to change after a job.
---

# Run a post-mortem

Two minutes for a deal, ten for a project. **Short by design** — a thorough
retro that never gets done is worth less than a shallow one that always does.

Within 5 business days of close. Including on things that went well; especially
those, because nobody ever asks why something worked.

## Deal post-mortem — 4 fields

1. **Outcome** — Won / Lost
2. **Primary reason** — exactly one, from the lists below. Not three.
3. **What would have changed it** — one sentence
4. **Anything to change in the OS** — usually nothing, and that is fine

**Loss reasons:** price · timing · scope fit · trust · went internal · went
silent · we declined · lost to incumbent

**Win reasons:** referral or reputation · speed of response · understood the
problem best · price · specific capability · existing relationship

**Constraining the list to one reason is what makes the data usable.** Three
reasons is a story; one is a data point that can be counted next quarter.

## Project post-mortem — 8 questions

Get the numbers first:

```bash
cd ~/alivio-ops-os/08-automation
python3 lib/ledger.py pnl --project "<exact project name>"
```

- [ ] Inside the estimated hours? By how much?
- [ ] How many revision rounds actually happened, against two included?
- [ ] How many scope changes, at what value, and how many went unbilled?
- [ ] Did any milestone slip, and what actually caused it?
- [ ] Did it go amber or red, and was it caught early?
- [ ] What would we do differently?
- [ ] What did the client say — verbatim, good or bad?
- [ ] **Would we take this client again? If no, why did we take them?**

**The last question is the valuable one.** Trace it back to the qualification
call — the signal was usually present and got rationalised away. That is a
disqualifier that needs strengthening, not bad luck.

## Where it goes

- **Deal:** a comment on the Linear issue, plus the win/loss section of
  `Alivio Operations OS/02 - Decisions Log.md` in Obsidian
- **Project:** a numbered note in that engagement's Obsidian folder —
  `NN - Post-mortem (<date>).md` — following the vault's existing convention, and
  linked from `00 - Index.md`

If it produced a decision worth not relitigating, write it into the decision log
in the five-line format, including `Revisit if`.

## The quarterly read

Individual post-mortems are anecdotes; the pattern is the product. Once a
quarter, read them together and look for:

- The most common loss reason — the biggest single lever available
- Whether estimation is systematically optimistic, and by how much
- Whether revision rounds routinely exceed two — a scoping problem, not a client
  problem
- Whether the same disqualifier keeps getting waived

**Commit to one or two changes.** A list of twelve improvements is a list nobody
executes.

## Hard rules

- **Never edit a past entry to look better.** A decision that turned out wrong
  stays as written, with an outcome note appended. A log of only good decisions
  teaches nothing.
- **One primary reason.** Enforce it.
- **Never blame a named contractor in anything client-adjacent.**

## Reference

- `02-sales/win-loss-capture.md`
- `04-team/decision-log.md`
- `04-team/knowledge-base-map.md` — where each kind of note actually lives
- `01-delivery/delivery-and-handoff.md`
- `06-metrics/definitions.md` — how margin and revision rounds are computed
