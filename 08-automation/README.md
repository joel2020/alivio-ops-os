# Automation

**Owner:** Joel (Principal) · **Trigger:** Scheduled, or invoked by name · **Cadence:** See below · **Last reviewed:** 2026-07-26

## Purpose

Phase 1 defined the cadences. This runs them. Six scheduled tasks and five
skills, plus the ledger everything reads from.

What breaks without it: the SOPs exist and nothing triggers them, so they get
followed in a good week and dropped in a busy one — which is precisely backwards.

## The four rules, enforced structurally

The Phase 3 brief set four rules. Three are enforced by capability rather than
by remembering:

| Rule | How it is enforced |
|---|---|
| Nothing sends externally | There is no send path anywhere in `lib/`. A test greps for one and fails if it appears. |
| No money moves, ever | Same test. No payment library, no transfer call. |
| Every output cites its sources | Every task returns a `sources` array; the commands render it. |
| Degrade gracefully | Each task reports what it could not read and delivers the rest. |

The fourth is the one that matters most day to day. A Monday brief that silently
omits cash because the books could not be read is worse than no brief, because
it looks complete.

## The ledger

The accounting tool the OS was missing. See `lib/ledger.py`.

```bash
python3 lib/ledger.py chase      # who to chase, at which tier
python3 lib/ledger.py aging      # AR buckets, over-30, over-45
python3 lib/ledger.py cash --monthly-cost 9000
python3 lib/ledger.py pnl --project "..."
python3 lib/ledger.py export     # CSV for a bookkeeper
```

**What it is:** an operational ledger. Who owes money, how late, can Alivio cover
the contractor run.

**What it is not:** double-entry bookkeeping. No chart of accounts, no trial
balance. It does not replace what an accountant needs at year end — it exports to
them. If Alivio later buys QuickBooks, this becomes the layer in front of it or
gets retired, and nothing else changes, because everything reads through
`ledger.py` rather than the files.

Storage is append-only JSONL under `books/`. Corrections are new records, never
edits — a ledger you can silently rewrite is one nobody should trust, and
append-only makes every change visible in git.

## The six scheduled tasks

Installed as launchd agents, `com.alivio.ops.*`.

| Task | When | Output |
|---|---|---|
| `monday-brief` | Mon 07:00 | Cash, AR, pipeline, red projects, commitments, proposed top 3 |
| `invoice-chase-sweep` | Tue + Fri 09:00 | Overdue list and drafted emails at the right tier |
| `project-status-rollup` | Wed 09:00 | Stage, blockers, aging, health per project |
| `pipeline-hygiene` | Fri 15:00 | Stale deals, missing fields, no next step |
| `friday-closeout` | Fri 16:00 | Shipped, slipped, carrying over, the four questions |
| `month-end-prep` | 25th 09:00 | Reconciliation gaps while there is time to fix them |

```bash
scheduler/install.sh --load       # start
scheduler/install.sh --unload     # stop, fully reversible
launchctl list | grep com.alivio.ops
tail -5 runs/run-log.jsonl
```

**Chase is twice weekly, not weekly**, because tier boundaries are days 1 and 7
and a weekly sweep can miss one by six days.

Each run does two things: the **engine** computes the numbers deterministically,
then **Claude** renders them. The engine runs even when the CLI is unavailable —
the numbers are the point, and a missing CLI must not mean a missing sweep. The
run log records both outcomes separately.

## The five skills

Triggered by natural language, not a magic command. In `.claude/skills/`.

| Skill | Fires when |
|---|---|
| `alivio-intake` | A new lead arrives; "should we take this?" |
| `alivio-scope` | Discovery notes exist; "write the SOW" |
| `alivio-status` | "What do I tell the client this week?" |
| `alivio-chase` | "Who owes me?"; "chase that invoice" |
| `alivio-postmortem` | A deal closes or a project delivers |

They are project-scoped, so they activate when working inside `~/alivio-ops-os`.
To have them available anywhere:

```bash
ln -s ~/alivio-ops-os/.claude/skills/alivio-* ~/.claude/skills/
```

## Anti-drift

The rules live in three places: the markdown, a `RULES` block in
`dashboard.html`, and Python constants here. Three copies is a design smell and
it is deliberate — the dashboard must run from `file://` with no server, so it
cannot import Python, and Python cannot import JavaScript.

Given that constraint the choice is between duplication that is tested and
duplication that is hoped for. `lib/tests/test_no_drift.py` is the test. Change
a chase tier in one place and it fails there, rather than six weeks later when
an invoice is chased at the wrong tier — or when the dashboard and the Monday
brief quietly disagree about which projects are red and nobody can tell which is
lying.

Proven to work: changing day 14 to day 13 in the dashboard fails the test with a
readable diff.

```bash
python3 lib/tests/run_all.py
```

## Decision rights

- **Joel decides alone:** every threshold, every send, every payment, what is
  scheduled.
- **Escalate when:** the engine and the dashboard disagree. The markdown wins and
  one of the other two is the bug.

## Definition of done

Every cadence in `00-charter/cadence-calendar.md` either fires on a schedule or
is explicitly listed as manual, and no output states a number it cannot source.

## Related

- [Cadence calendar](../00-charter/cadence-calendar.md)
- [AR chase sequence](../03-finance/ar-chase-sequence.md)
- [Invoicing policy](../03-finance/invoicing-policy.md)
- [Dashboard](../07-dashboard/README.md)
- [Scorecard](../06-metrics/scorecard.md)

## Assumptions

- Assumes `python3` (system Python is fine — there are no dependencies) and,
  optionally, the `claude` CLI. Everything degrades without the latter.
- **Assumes Joel records balances and payments.** The ledger cannot observe a
  bank account. Nothing here is true unless someone types it, and the tasks say
  so rather than assuming zero.
- **`monthly_operating_cost` and `revenue_target_90d` are still unset**, so cash
  trigger levels and pipeline coverage stay switched off rather than fabricated.
- Assumes macOS launchd. On Linux these become systemd timers; the runner is
  unchanged.
