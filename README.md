# Alivio Studios — Operations OS

The documented system that runs the agency without depending on any one person's
memory.

**Status:** All three phases complete and running.
Phase 1 — 41 documents · Phase 2 — dashboard · Phase 3 — 6 scheduled agents,
5 skills, and the ledger. 42 tests, integrity-gated on commit.

**Last reviewed:** 2026-07-26

---

## Start here

**New contractor?** Read these five, in order, then answer the three questions in
[onboarding path](04-team/onboarding-path.md). About an hour.

1. [Operating charter](00-charter/operating-charter.md) — what Alivio does and refuses
2. [Roles and decision rights](00-charter/roles-and-decision-rights.md) — your role's section
3. [Project lifecycle](01-delivery/project-lifecycle.md) — the stages and what "done" means
4. [QA gate](01-delivery/qa-gate.md) — the bar your work is measured against
5. [Client communication standard](01-delivery/client-communication-standard.md) — especially what you never say to a client

**Looking for a specific answer?** The four questions that come up most:

| Question | Answer lives in |
|---|---|
| Can I agree to this change? | [Roles and decision rights](00-charter/roles-and-decision-rights.md) — the thresholds table |
| What are our payment terms? | [Invoicing policy](03-finance/invoicing-policy.md) — the source of truth |
| How many revisions are included? | Two. [Scope change protocol](01-delivery/scope-change-protocol.md) |
| This project is in trouble — now what? | [Project red escalation](01-delivery/project-red-escalation.md) |

---

## The full index

### 00 — Charter
The layer everything else defers to.

- [Operating charter](00-charter/operating-charter.md) — services, commitments, refusals, tool ownership
- [Roles and decision rights](00-charter/roles-and-decision-rights.md) — who decides what, and the escalation thresholds
- [RACI matrix](00-charter/raci-matrix.md) — one accountable person per workflow
- [Cadence calendar](00-charter/cadence-calendar.md) — the daily/weekly/monthly/quarterly rhythm

### 01 — Delivery
- [Intake and qualification](01-delivery/intake-and-qualification.md)
- [Scoping and SOW](01-delivery/scoping-and-sow.md)
- [Project lifecycle](01-delivery/project-lifecycle.md) — 7 stages, entry/exit criteria, health rules
- [Kickoff](01-delivery/kickoff.md)
- [QA gate](01-delivery/qa-gate.md)
- [Delivery and handoff](01-delivery/delivery-and-handoff.md)
- [Client communication standard](01-delivery/client-communication-standard.md)
- [Scope change protocol](01-delivery/scope-change-protocol.md)
- [Project red escalation](01-delivery/project-red-escalation.md)

### 02 — Sales
- [ICP and disqualifiers](02-sales/icp-and-disqualifiers.md)
- [Pipeline stages](02-sales/pipeline-stages.md)
- [Proposal and pricing](02-sales/proposal-and-pricing.md)
- [Follow-up cadence](02-sales/follow-up-cadence.md)
- [CRM hygiene](02-sales/crm-hygiene.md)
- [Forecast method](02-sales/forecast-method.md)
- [Win/loss capture](02-sales/win-loss-capture.md)

### 03 — Finance
- [Invoicing policy](03-finance/invoicing-policy.md) — **source of truth for payment terms**
- [AR chase sequence](03-finance/ar-chase-sequence.md)
- [Contractor payments](03-finance/contractor-payments.md)
- [Cash flow review](03-finance/cash-flow-review.md)
- [Month-end close](03-finance/month-end-close.md)
- [Tax and compliance calendar](03-finance/tax-and-compliance-calendar.md)

### 04 — Team
- [Onboarding path](04-team/onboarding-path.md)
- [Meeting standards](04-team/meeting-standards.md)
- [Decision log](04-team/decision-log.md)
- [SOP writing standard](04-team/sop-writing-standard.md)
- [Knowledge base map](04-team/knowledge-base-map.md)

### 05 — Templates
- [Project brief](05-templates/project-brief.md)
- [SOW template](05-templates/sow-template.md)
- [Kickoff agenda](05-templates/kickoff-agenda.md)
- [Weekly status report](05-templates/weekly-status-report.md)
- [Change order](05-templates/change-order.md)
- [Offboarding checklist](05-templates/offboarding-checklist.md)
- [Invoice chase emails](05-templates/invoice-chase-emails.md) — the actual copy, per tier
- [Weekly review agenda](05-templates/weekly-review-agenda.md)

### 06 — Metrics
- [Scorecard](06-metrics/scorecard.md) — the 11 numbers
- [Definitions](06-metrics/definitions.md) — exactly how each is calculated

### 07 — Dashboard *(Phase 2)*
- [Dashboard README](07-dashboard/README.md) — how to use it, what it computes
- `07-dashboard/dashboard.html` — open it directly, no server needed
- `07-dashboard/data.js` — the only file you edit

Health colours, chase tiers, weighted pipeline, and cash trigger levels are all
**computed from the documents above**. The dashboard reads the definitions; it
does not hold its own.

### 08 — Automation *(Phase 3)*
- [Automation README](08-automation/README.md) — the ledger, the six tasks, the five skills
- `08-automation/lib/ledger.py` — the accounting tool: invoices, AR, expenses, contractors, cash
- `08-automation/scheduler/install.sh --load` — start or stop the six agents
- `.claude/skills/` — alivio-intake · alivio-scope · alivio-status · alivio-chase · alivio-postmortem

| Task | When |
|---|---|
| Monday brief | Mon 07:00 |
| Invoice chase sweep | Tue + Fri 09:00 |
| Project status roll-up | Wed 09:00 |
| Pipeline hygiene | Fri 15:00 |
| Friday close-out | Fri 16:00 |
| Month-end prep | 25th 09:00 |

**Nothing sends. No money moves.** Both are enforced by the capability not
existing — a test greps for a send or payment path and fails if one appears.

---

## The numbers that appear in more than one document

Each has **one** source of truth. Change it there; everything else links.

| Number | Value | Source of truth |
|---|---|---|
| Revision rounds included | **2** per deliverable | [Scope change protocol](01-delivery/scope-change-protocol.md) |
| Payment terms | **Net 7** | [Invoicing policy](03-finance/invoicing-policy.md) |
| Payment structure | **40 / 30 / 30** | [Invoicing policy](03-finance/invoicing-policy.md) |
| Late fee | **2%/month** after 30 days | [Invoicing policy](03-finance/invoicing-policy.md) |
| Scope change: PM decides alone | **< $500 and < 2 hours** | [Roles and decision rights](00-charter/roles-and-decision-rights.md) |
| Scope change: Joel approves | **$500–$2,500** | [Roles and decision rights](00-charter/roles-and-decision-rights.md) |
| Scope change: change order | **> $2,500** or any date change | [Roles and decision rights](00-charter/roles-and-decision-rights.md) |
| Chase tiers | **Days 1 / 7 / 14 / 21 / 30 / 45** | [AR chase sequence](03-finance/ar-chase-sequence.md) |
| Pipeline coverage target | **3×** | [Forecast method](02-sales/forecast-method.md) |

---

## How to change the OS

1. Change it in its **source of truth** file, never in a document that references it
2. Update every document that restates it — the table above says which
3. **If it is a threshold, update all three copies**: the markdown, the `RULES`
   block in `07-dashboard/dashboard.html`, and the constants in
   `08-automation/lib/`. The test suite fails if they disagree, so you will know.
4. Bump `Last reviewed`
5. If it is a policy change, log it in the [decision log](04-team/decision-log.md)
6. Follow the [SOP writing standard](04-team/sop-writing-standard.md)

**An SOP not followed twice is wrong.** Fix the SOP, not the person.

```bash
python3 08-automation/lib/tests/run_all.py     # 42 tests
```

A pre-commit hook runs them. It blocks a commit that breaks the OS, because six
launchd agents execute this code unattended.

---

## What this OS is for

Five tests. If a document does not move one of these, it should not exist.

1. A new PM can run a project end-to-end using only these files
2. A new contractor is productive on day one without a synchronous walkthrough
3. Nobody asks "what's the status of X" — they read the status report
4. No invoice ages past 45 days without someone having been told
5. **Joel can be off for two weeks and the agency runs**

---

## What still needs Joel

Phase 1 is written but **not yet fully true**. These are the decisions the OS is
still guessing at, ranked by how much damage a wrong guess does.

1. **Pricing floors** — every band is inferred from two observed data points
   (RLTRS at $29,000, a published $5–10K install figure). Quoting from an
   invented floor either loses winnable work or wins unprofitable work, and both
   are invisible until the quarter closes.
2. **Monthly operating cost — partial.** $320/month of software is known
   (ChatGPT $20, Claude $200, Higgsfield $100). Still missing: tax set-aside,
   recurring contractors, and personal draw. Cash trigger levels stay OFF until
   the total exists — computing them from $320 would show green at $591 of cash.
3. **Retainer mechanism** — Alivio does not bill hourly, so a retainer cannot be
   an hour pool. It needs a defined monthly scope, or a capacity commitment with
   an explicit in/out list, or it quietly becomes unlimited requests.
4. **The Deputy is defined but vacant** — a named person holding Joel's
   decisions while he is away, with written limits. See
   `00-charter/roles-and-decision-rights.md`. Until it is filled, RED projects
   pause during an absence rather than being decided, and "Joel can be off for
   two weeks" is not achievable.

### Settled 2026-07-27

- **Revenue target: $100,000/year → $25,000 per 90 days.** At 3× coverage the
  pipeline needs $75,000 weighted. Currently $0 — the alarm is firing, correctly.
- **Every engagement is fixed-price.** No hourly billing anywhere, including
  change orders. Hours are an internal costing input and never appear in a
  client document.
- **40/30/30 is the default payment schedule**, with a custom schedule permitted
  when written into the SOW. RLTRS runs $4,000 up front plus $500 weekly — a
  fixed price on a weekly draw, not a different pricing model. The risk that
  shape carries is documented in `03-finance/invoicing-policy.md`.
- **The accounting tool exists** — `08-automation/lib/ledger.py`.

### One tension worth resolving

The revenue target and the stated capacity do not agree. 4–6 concurrent clients
on 4–8 week engagements implies roughly 25–35 engagements a year, which at the
$8,000 web floor would be $200K+. Either the concurrency figure counts small and
dormant work, or $100K is deliberately conservative, or the price bands are too
high for the volume actually being run. It changes what "healthy" means on the
dashboard, so it is worth settling. See `02-sales/forecast-method.md`.
