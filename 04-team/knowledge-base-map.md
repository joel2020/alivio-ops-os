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
| Decisions and reasoning | **Obsidian** — `Alivio Operations OS/02 - Decisions Log.md` for company-wide, the engagement folder for client-specific | PM | Chat, transcripts alone |
| Meeting transcripts | **Granola** | — | — |
| Code, deploys, environments | **GitHub + Vercel** | Build | — |
| Credentials | **Password manager** | Joel | Chat, email, code, notes |
| Client conversations | **Channel of record** per client | PM | Anywhere else |
| Financial records | **The ledger** (`08-automation/lib/ledger.py`) | Joel | Spreadsheets |
| Contractor register and payments | **The ledger** `contractor` commands | Joel | Spreadsheets |
| Signed agreements, W-9/W-8BEN | **Joel's records** | Joel | — |

## The Obsidian structure

**This describes the vault as it actually is**, verified 2026-07-27. An earlier
draft of this file proposed a different shape — one that had never existed. A map
that describes an imagined structure is worse than no map, because people follow
it and create a second convention alongside the first.

```
Clients/
  _Client Registry.md        the MOC — every client, repo, Vercel, Supabase, Linear
  <Client>.md                one dossier per client

<Engagement or Project>/     one folder per body of work
  00 - Index.md              start here; links the numbered notes
  01 - ...                   numbered, in reading order
  NN - Decision Log.md       where the engagement has one

Alivio Operations OS/        the OS itself
  00 - Index.md
  01 - What Was Built.md
  02 - Decisions Log.md
  03 - Open Decisions.md
  04 - Operating Numbers.md
```

**Conventions that already exist and should be followed:**

- YAML frontmatter with `type`, `tags`, `updated`
- Numbered filenames, `NN - Title.md`, in reading order
- `[[Wikilinks]]`, never bare paths
- `_`-prefixed files are indexes (MOCs)

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

1. Any active client missing a dossier in `Clients/`?
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

Every active client has a dossier in `Clients/`, every engagement with decisions
has a log, and every category in the table has exactly one home.

## Related

- [Decision log](decision-log.md)
- [SOP writing standard](sop-writing-standard.md)
- [Client communication standard](../01-delivery/client-communication-standard.md)
- [Operating charter](../00-charter/operating-charter.md)

## Assumptions

- **The structure above was corrected on 2026-07-27 to match the real vault.**
  The original draft invented a `Clients/<Name>/00-context.md` layout that did not
  exist. Anyone following it would have created a second convention alongside the
  one already in use — which is exactly the "two homes for one fact" failure this
  document exists to prevent.
- Assumes Obsidian and Linear stay as-is. Consistent with the stated constraint not
  to propose replacements.
- **Assumes a password manager exists.** None was named in the stack — if there is
  not one, that is a gap worth closing before the next credential handoff.
- The accounting tool is the ledger, built 2026-07-26. It is operational rather
  than double-entry and exports CSV for an accountant.
