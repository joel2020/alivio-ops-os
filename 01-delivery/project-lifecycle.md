# Project Lifecycle

**Owner:** PM · **Trigger:** SOW signed and deposit received · **Cadence:** Continuous; stage reviewed every Wednesday · **Last reviewed:** 2026-07-26

## Purpose

Seven stages with **entry and exit criteria you can check without judgment**. A
stage you can argue about is a stage that projects sit in for three weeks while
everyone assumes someone else is unblocking it.

What breaks without it: "what's the status of X" requires asking Joel, which is
the pain this OS is built to remove.

Stage lives in **Linear**. Nowhere else. If Linear says Build and the status
report says QA, Linear is right and the report is wrong.

## The stages

### 1. Scoped

**Enter when:** SOW signed **and** deposit received. Both. A signed SOW with an
unpaid deposit is not a project, it is a hope.

**Exit when:**
- [ ] Linear project created, milestones entered with dates
- [ ] PM assigned and named to the client
- [ ] Contractors booked with committed dates
- [ ] Channel of record agreed and created
- [ ] Kickoff scheduled

**Max dwell: 5 business days.** Longer means the resourcing wasn't real when the
SOW was signed.

### 2. Kickoff

**Enter when:** kickoff meeting is on the calendar.

**Exit when:**
- [ ] Kickoff held, `05-templates/kickoff-agenda.md` followed
- [ ] Client has confirmed their decision-maker and their SLA for feedback
- [ ] All client-supplied inputs received, or listed with dates and an owner
- [ ] Success criteria written down in one sentence the client agreed to
- [ ] Notes in Obsidian, decisions promoted to the decision log

**Max dwell: 5 business days.**

### 3. Build

**Enter when:** kickoff exit criteria are met.

**Exit when:**
- [ ] Every SOW deliverable exists in a reviewable state
- [ ] Self-review done by whoever built it
- [ ] No known defect that the client would call a defect

**Max dwell: 60% of total engagement duration.** On a 6-week project that is
about 3.5 weeks. Crossing it without a corresponding milestone completion is an
**amber** flag; see health rules below.

### 4. QA

**Enter when:** Build exit criteria met.

**Exit when:** the QA gate passes — see `qa-gate.md`. Not "mostly passes."

**Max dwell: 3 business days.** QA is a gate, not a phase; if it takes longer the
work wasn't finished, and the project belongs back in Build, honestly labelled.

### 5. Client review

**Enter when:** QA passed and the deliverable is with the client.

**Exit when:**
- [ ] Client has approved, **or**
- [ ] Client feedback received and inside the two included rounds, **or**
- [ ] A change order is signed for anything beyond scope

**Max dwell: 7 calendar days per round.** Beyond that the PM escalates — a client
sitting on feedback is the most common way a fixed-scope project loses its margin,
and it is invisible unless it is a tracked stage.

### 6. Delivered

**Enter when:** client has approved the final deliverable.

**Exit when:**
- [ ] Handoff complete per `delivery-and-handoff.md`
- [ ] Final invoice issued
- [ ] Access and credentials transferred or documented
- [ ] Client confirmed receipt in writing

**Max dwell: 10 business days.**

### 7. Closed

**Enter when:** final invoice **paid** and offboarding checklist complete.

A project is not closed when the work is done. It is closed when the money has
arrived. Anything else lets a "finished" project hide unpaid invoices — which is
exactly how $12,000 aged 11 and 18 days unnoticed.

**Exit:** none. Terminal.

## Health rules

Computed, not opinion. The dashboard uses exactly these.

| Health | Rule |
|---|---|
| 🟢 **Green** | Inside stage dwell limit, next milestone in the future, no blockers older than 2 business days |
| 🟡 **Amber** | Any one of: stage dwell exceeded; next milestone within 3 days with work outstanding; a blocker aged 2–5 business days; budget over 80% consumed with under 60% delivered; one missed checkpoint |
| 🔴 **Red** | Any one of: milestone slipped over 5 business days; client unresponsive over 7 days on a blocker; two consecutive missed checkpoints; scope disputed; invoice for this project over 30 days late |

Amber is a PM problem. **Red is a Joel problem, same day** — see
`project-red-escalation.md`.

## Decision rights

- **PM decides alone:** moving a project between stages, declaring amber,
  sequencing inside a stage.
- **Escalate when:** any red criterion is met, or a stage exceeds its dwell limit
  by more than 50%.

## Definition of done

Every active project has a stage in Linear, a next milestone with a date, and a
health colour derived from the rules above rather than from how it feels.

## Related

- [Kickoff](kickoff.md)
- [QA gate](qa-gate.md)
- [Delivery and handoff](delivery-and-handoff.md)
- [Scope change protocol](scope-change-protocol.md)
- [Project red escalation](project-red-escalation.md)
- [Weekly status report](../05-templates/weekly-status-report.md)

## Assumptions

- **Dwell limits are calibrated for 4–8 week engagements.** A 3-month build needs
  them scaled or it shows amber permanently, which trains everyone to ignore amber.
- The 60% Build / 80% budget thresholds are best-practice guesses. They need one
  quarter of real data to confirm — track them before trusting them.
- Assumes Linear projects map one-to-one with client engagements. If one client has
  several parallel workstreams, stage becomes ambiguous and they should be separate
  Linear projects.
