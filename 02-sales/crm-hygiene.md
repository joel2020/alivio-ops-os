# CRM Hygiene

**Owner:** Joel (Principal) · **Trigger:** Friday pipeline sweep · **Cadence:** Weekly · **Last reviewed:** 2026-07-26

## Purpose

A pipeline you do not trust is worse than no pipeline, because you act on it
anyway. Fifteen minutes on Friday keeps the forecast honest and stops deals dying
of neglect rather than of a decision.

What breaks without it: the forecast becomes fiction, and deals go quiet without
anyone noticing until the month closes light.

## The record

Pipeline lives in **Linear**, as a dedicated project, one issue per deal.

**Required on every deal:**

- [ ] Company and contact name
- [ ] Source — referral, inbound, outbound, network
- [ ] Service line — AI / web / design / marketing
- [ ] Stage, per `pipeline-stages.md`
- [ ] Estimated value
- [ ] **Next step, with a date** — the one field that is never optional
- [ ] Last touch date
- [ ] Decision-maker name

**Required on close:** win/loss reason, from the standard list in
`win-loss-capture.md`.

## The Friday sweep — 15 minutes

Automated in Phase 3; the checks are the same either way.

1. **Deals with no next step** → add one or mark Lost. No third option.
2. **Deals past their stage dwell limit** → advance, or Lost.
3. **Deals not touched in 5 business days** → follow up per the cadence.
4. **Missing required fields** → fill them.
5. **Stale stages** → does the stage still reflect what the client actually did?
6. **Won deals** → confirm deposit received; a Won with no deposit is Verbal.
7. **Update the forecast** per `forecast-method.md`.

## The rules that keep it honest

- **Next step is mandatory.** A deal without one is not being worked.
- **Stage reflects the client's last action, not Alivio's.** See
  `pipeline-stages.md`.
- **Lost is a normal outcome.** Marking Lost is hygiene, not failure. The pipeline
  that only grows is the one nobody believes.
- **One deal per opportunity.** A client discussing two projects is two deals.
- **Never inflate value to make the pipeline look healthy.** The only person misled
  is Joel, three weeks later, planning cash against it.

## Decision rights

- **Joel decides alone:** everything here.
- **Escalate when:** n/a.

## Definition of done

Every open deal has all required fields, a dated next step, and a stage no older
than its dwell limit.

## Related

- [Pipeline stages](pipeline-stages.md)
- [Forecast method](forecast-method.md)
- [Follow-up cadence](follow-up-cadence.md)
- [Win/loss capture](win-loss-capture.md)
- [Weekly review agenda](../05-templates/weekly-review-agenda.md)

## Assumptions

- Assumes Linear is adequate as a CRM at this volume. It is, at 4–6 concurrent
  clients. **Past roughly 15–20 open deals the lack of a pipeline view becomes the
  binding constraint**, and a real CRM is worth the switching cost — not before.
- Assumes Joel does the sweep himself. It is highly automatable and is a Phase 3
  scheduled task.
