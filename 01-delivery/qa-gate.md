# QA Gate

**Owner:** PM · **Trigger:** A deliverable is claimed complete · **Cadence:** Every deliverable, no exceptions · **Last reviewed:** 2026-07-26

## Purpose

One checkpoint between "the person who built it thinks it's done" and the client
seeing it. Every defect the client finds costs a revision round, some credibility,
and — because rounds are capped at two — real money.

What breaks without it: the client becomes the QA process. That is the most
expensive QA available, and it is charged in trust.

**This gate applies to work from Joel too.** A gate with an exception for the
principal is not a gate.

## Steps

1. **Builder self-reviews first.** The gate is not where you find out whether it
   works. Anything that fails the checklist below on first pass goes back without
   further review — QA is not a debugging service.

2. **PM runs the gate**, against the SOW deliverables list rather than memory.

3. **Universal checks** — every deliverable, every service line:
   - [ ] Matches what the SOW actually says, read fresh, not recalled
   - [ ] Every acceptance criterion in the SOW is demonstrably met
   - [ ] Client's name, product names, and key terms spelled correctly throughout
   - [ ] No placeholder text, lorem ipsum, TODO, or test data anywhere
   - [ ] No Alivio-internal comments, URLs, or credentials visible
   - [ ] Works for someone who has never seen it — opened cold, without a walkthrough

4. **Service-line checks** — run the ones that apply:

   **AI builds**
   - [ ] Behaves correctly on a deliberately bad input, not only the happy path
   - [ ] Failure mode is graceful and legible — says what went wrong
   - [ ] No API key, secret, or credential in code, logs, or client-visible output
   - [ ] Cost per run measured and documented; client knows what it will cost them
   - [ ] Prompt and model choices documented so someone else can maintain it
   - [ ] Rate limits and quotas identified

   **Web development**
   - [ ] Renders correctly on mobile, tablet, desktop
   - [ ] Lighthouse run; scores recorded in the handoff, and no red
   - [ ] Every link resolves, including footer and nav
   - [ ] Forms submit, and the submission arrives somewhere a human will see
   - [ ] No console errors on any page
   - [ ] Basic accessibility: alt text, focus states, keyboard navigation, contrast
   - [ ] Deploys reproducibly from a clean checkout — no undocumented local state

   **Design**
   - [ ] Source files organised and named so someone else can open them
   - [ ] Fonts either licensed for the client's use or substituted, with licences noted
   - [ ] Exports in the formats the SOW promised, at the sizes promised
   - [ ] Design system tokens documented if one was part of scope

   **Marketing**
   - [ ] Every factual claim traceable to a source
   - [ ] No claim about client results that is not substantiated in writing
   - [ ] Links and UTMs correct and tested
   - [ ] Approved by the client's named decision-maker before anything publishes

5. **Record the outcome.** Pass or fail, in Linear, with the date. A gate with no
   record cannot be improved and cannot be shown to have happened.

6. **On fail:** back to Build. The project stage changes back too — a project
   sitting in QA that is actually being rebuilt is a project lying about its stage.

## Definition of done

The PM would be comfortable if the client opened this without warning, with no
walkthrough, on their phone, in front of their own boss.

## Decision rights

- **PM decides alone:** pass or fail.
- **Joel decides alone:** shipping something that failed the gate. This is
  sometimes correct — a deadline may be worth a known rough edge — but it is
  Joel's call, it is written down, and the client is told what is rough.
- **Escalate when:** the same check fails twice on one project. That is a
  capability or briefing problem, not a QA problem.

## Related

- [Project lifecycle](project-lifecycle.md)
- [Delivery and handoff](delivery-and-handoff.md)
- [Scoping and SOW](scoping-and-sow.md)
- [Scope change protocol](scope-change-protocol.md)

## Assumptions

- Assumes the PM is competent to judge across all four service lines. At current
  scale that is Joel, so it holds. **Past ~8 people this breaks** and each line
  needs a peer reviewer instead.
- Lighthouse "no red" is a guess at Alivio's bar. Worth setting a real number —
  observed on the Bravo Mechanical audit, a mobile LCP of 14.8s shipped to a live
  client site, which suggests the bar needs to be explicit rather than assumed.
- Assumes deliverables are reviewable in a staging environment. Where they are not,
  QA happens in production and the risk should be named in the SOW.
