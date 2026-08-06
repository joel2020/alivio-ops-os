# Build With Alivio Organic and Outbound Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a repeatable, no-paid-ads acquisition system that earns relevant organic traffic, supports Joel’s manual cold calls, sends small personalized email campaigns, and converts interested US home-service operators into an ROI Systems Review.

**Architecture:** One research theme becomes a search-focused resource, three founder-led LinkedIn posts, a call insight, and—only where lawful and relevant—a personalized email angle. Public content lives on `buildwithalivio.com`. Campaign procedures and reusable assets live in the Alivio operating-system repository. Prospect personally identifiable information and suppression records live in access-controlled operational systems, not Git. Linear becomes the deal record once contact or meaningful engagement occurs.

**Tech Stack:** Static HTML resources on Vercel, Google Search Console, LinkedIn, manual telephone, authenticated domain email, Linear, Google Slides/Drive for client presentations, existing Alivio operating-system templates.

## Global Constraints

- No paid advertising in this phase.
- Target US home-service companies nationwide; use Northeast HVAC and adjacent trades as the first outbound concentration because the strongest relevant proof is Bravo Mechanical.
- Calls are placed manually by Joel. Do not use prerecorded, AI-generated, predictive-dialer, or ringless-voicemail voice.
- Email volume starts at 10 carefully researched messages per business day, not a bulk blast.
- Call volume starts at 15 selected calls per day, four days per week.
- Use Day 1, 3, 7, and 14 touches, then stop unless the prospect engages.
- Do not buy scraped lists or commit prospect names, phone numbers, email addresses, suppression data, or private research to Git.
- The email sending-readiness gate in `02-sales/campaigns/build-with-alivio/sending-readiness.md` must be `READY` before sending any commercial campaign.
- Commercial email must use accurate sender and subject information, a valid physical postal address, a clear opt-out, and an enforced suppression list. Refer to the FTC’s official CAN-SPAM compliance guide and the selected providers’ current sender requirements during execution.
- Verify calling rules for the business type, number, state, and method before dialing; federal rules are not the only rules that may apply.
- No guaranteed ROI. Use conservative, expected, and upside scenarios tied to prospect-provided inputs.
- Any client name, logo, quote, screenshot, or outcome requires written permission and source evidence.
- This plan follows conversion-site Tasks 1–7. Its public resource pages must be complete before the conversion-site sitemap/security task is finalized.

---

### Task 1: Create the campaign operating system

**Files:**
- Create: `02-sales/campaigns/build-with-alivio/README.md`
- Create: `02-sales/campaigns/build-with-alivio/prospect-research-standard.md`
- Create: `02-sales/campaigns/build-with-alivio/campaign-qa.md`
- Modify: `02-sales/crm-hygiene.md`
- Modify: `02-sales/follow-up-cadence.md`

- [ ] **Step 1: Define the campaign’s audience and exclusions**

The campaign README must specify:

```text
Priority trades: HVAC first; plumbing, electrical, roofing second
Geography: US nationwide; first list concentrated in Northeast markets
Company size: 5–100 employees
Buyer: owner, operator, GM, sales/marketing/operations leader
Signals: active demand generation, missed-call risk, slow response, weak estimate
follow-up, disconnected CRM/phone/scheduling stack, unclear source-to-profit reporting
Commercial fit: credible path to an $8K+ implementation or $2K+/month retainer
Exclusions: residential consumers, one-person startups without budget, agencies,
direct competitors, existing opt-outs, active clients unless the contact is relevant
```

- [ ] **Step 2: Define the research standard**

Require one operational observation and one evidence URL for each prospect before contact. Allowed public evidence includes the company website, Google Business Profile, public reviews, public job openings, and public technology/contact flows. Do not infer private revenue, lead count, margins, or performance.

- [ ] **Step 3: Define the data boundary**

Store operational prospect data in the selected access-controlled system. A contacted or engaged account becomes a Linear issue with source, owner, next step, due date, and suppression status. Git contains only the schema and procedures.

- [ ] **Step 4: Align follow-up and hygiene**

Update the existing OS documents so the Day 1/3/7/14 acquisition cadence is distinct from proposal follow-up. A reply, booked call, explicit no, hard bounce, or opt-out ends the automated cadence immediately. Every live conversation has a next step in Linear.

- [ ] **Step 5: Create preflight QA**

`campaign-qa.md` must fail a send or call batch if audience fit, source evidence, sender authentication, postal address, suppression check, personalization, truthful subject, monitored replies, or next-step tracking is missing.

- [ ] **Step 6: Commit the campaign foundation**

```bash
git add 02-sales/campaigns/build-with-alivio 02-sales/crm-hygiene.md 02-sales/follow-up-cadence.md
git commit -m "docs: add Build With Alivio campaign operating system"
```

### Task 2: Create the ROI-first cold-call playbook

**Files:**
- Create: `02-sales/campaigns/build-with-alivio/cold-call-playbook.md`
- Create: `02-sales/campaigns/build-with-alivio/call-review-scorecard.md`
- Modify: `02-sales/pipeline-stages.md`

- [ ] **Step 1: Write the permission-based opener**

Use a short, truthful pattern:

```text
“Hi [first name], Joel from Alivio Studio. I noticed [specific public observation].
We help home-service operators find where calls, web leads, and estimates fall out
before they become booked gross profit. This is a cold call—can I take 30 seconds
to explain why I called, and you can tell me if it is irrelevant?”
```

The final script uses merge fields in the calling workspace; it does not save personal data in the repository.

- [ ] **Step 2: Add four diagnostic questions**

Ask only enough to identify a measurable gap:

1. How are missed calls and after-hours leads handled now?
2. How quickly does a new web lead receive a human or automated response?
3. What happens to an estimate that does not close on the first follow-up?
4. Can the operator trace a lead source through booking, closed job, and gross margin?

- [ ] **Step 3: Add the ROI bridge**

If there is a gap, use the prospect’s own approximate inputs in the site calculator. State that the output is a scenario and that the review will validate the baseline before Alivio recommends an investment.

- [ ] **Step 4: Add outcome branches**

Define exact next actions for:

```text
No permission / not interested: thank them, record “no,” stop cadence
Wrong person: ask who owns lead handling or operations; do not pressure
Mild interest: email the relevant resource and agree on a specific follow-up
Qualified pain: book the 30-minute ROI Systems Review
No measurable problem: say so and close without pitching
Do-not-call request: confirm, suppress immediately, do not call again
```

- [ ] **Step 5: Add objection handling**

Cover “we already have a CRM,” “we tried automation,” “send information,” “AI is risky,” “we need more leads, not systems,” and “what does it cost?” Every response returns to current leakage, measurable baseline, and fixed-price options rather than arguing about tools.

- [ ] **Step 6: Create the call scorecard**

Score permission, relevance, discovery quality, use of prospect inputs, truthfulness, concise CTA, compliance, next step, and CRM hygiene. Do not score a call primarily on whether a meeting was booked.

- [ ] **Step 7: Define the weekly operating target**

Use 15 researched calls per day on four days each week. Friday reviews connection rate, decision-maker conversations, identified measurable problems, reviews booked, opt-outs, and language learned.

- [ ] **Step 8: Commit the call system**

```bash
git add 02-sales/campaigns/build-with-alivio/cold-call-playbook.md 02-sales/campaigns/build-with-alivio/call-review-scorecard.md 02-sales/pipeline-stages.md
git commit -m "docs: add ROI-first home-service call playbook"
```

### Task 3: Build the personalized email sequence and suppression workflow

**Files:**
- Create: `02-sales/campaigns/build-with-alivio/email-sequence.md`
- Create: `02-sales/campaigns/build-with-alivio/suppression-workflow.md`
- Create: `02-sales/campaigns/build-with-alivio/email-reply-routing.md`

- [ ] **Step 1: Define required merge fields and validation**

Each email requires `first_name`, `company`, `public_observation`, `observation_url`, `relevant_problem`, `resource_url`, `sender_name`, `reply_address`, `business_postal_address`, and `unsubscribe_action`. The campaign QA gate blocks sending if any required value or source evidence is absent.

- [ ] **Step 2: Draft Day 1 as an observation, not a pitch dump**

Structure:

```text
Subject: question about [company]’s [calls/estimates/lead follow-up]
1 sentence: specific public observation
1 sentence: plausible operational question, explicitly framed as a question
1 sentence: what Alivio measures from lead to booked gross profit
CTA: worth comparing the current process for 15–30 minutes?
Signature, postal address, and plain-language opt-out
```

- [ ] **Step 3: Draft Day 3, 7, and 14**

Day 3 adds a relevant checklist or resource. Day 7 introduces the transparent ROI inputs. Day 14 is a concise close-the-loop message. Do not fake a prior relationship, thread, referral, or manual reply.

- [ ] **Step 4: Build reply routing**

Define responses for interested, referral, timing later, not a fit, unsubscribe, and out-of-office. Interested replies receive a human response and Linear next step within one business day. Opt-outs update suppression before any other action.

- [ ] **Step 5: Build the suppression workflow**

The operational suppression store uses normalized email plus domain, reason, source, timestamp, and scope. It is checked before every send and import. The Git document contains the schema only. Hard bounce, abuse complaint, explicit opt-out, or do-not-contact request suppresses immediately across `joel@`, `hello@`, and `updates@` campaigns.

- [ ] **Step 6: Run a non-sending QA test**

Render the sequence for three invented companies using example.invalid addresses. Verify merge failures block output, opt-out is visible, physical-address enforcement works, links use `buildwithalivio.com`, and no live email is sent.

- [ ] **Step 7: Commit the email system**

```bash
git add 02-sales/campaigns/build-with-alivio/email-sequence.md 02-sales/campaigns/build-with-alivio/suppression-workflow.md 02-sales/campaigns/build-with-alivio/email-reply-routing.md
git commit -m "docs: add compliant personalized email sequence"
```

### Task 4: Publish the resource hub and first four organic resources

**Files:**
- Create: `/Users/joel/alivio-studio/resources/index.html`
- Create: `/Users/joel/alivio-studio/resources/home-service-revenue-leak-checklist.html`
- Create: `/Users/joel/alivio-studio/resources/speed-to-lead-home-services.html`
- Create: `/Users/joel/alivio-studio/resources/hvac-estimate-follow-up.html`
- Create: `/Users/joel/alivio-studio/resources/home-service-roi-calculator-guide.html`
- Modify: `/Users/joel/alivio-studio/assets/style.css`
- Modify: `/Users/joel/alivio-studio/sitemap.xml`
- Modify: `/Users/joel/alivio-studio/tests/site-baseline.test.js`

- [ ] **Step 1: Write failing resource-page tests**

Require unique intent, title, description, canonical, visible author/date/last-reviewed date, breadcrumbs, cited primary sources where factual benchmarks appear, internal links, one review CTA, and inclusion in the sitemap.

- [ ] **Step 2: Build the resource hub**

Group content by missed opportunity, lead response, estimate follow-up, CRM/reporting, and ROI planning. Explain that resources help operators diagnose a constraint; the CTA is the 30-minute Systems Review.

- [ ] **Step 3: Publish the revenue-leak checklist**

Create an actionable self-audit across phone coverage, form delivery, response time, booking ownership, estimate follow-up, membership reminders, source tracking, closed-job value, gross margin, and weekly review. Link each failure to a measurable input, not a software product.

- [ ] **Step 4: Publish the speed-to-lead guide**

Explain how to measure lead-created time, first automated acknowledgement, first meaningful human response, contact attempts, booking, and disqualification. Do not cite an uncited universal “five-minute” conversion claim; use the operator’s baseline and clearly sourced current research only.

- [ ] **Step 5: Publish the HVAC estimate-follow-up guide**

Map estimate created → delivery → questions → financing/option clarification → scheduled follow-up → won/lost reason. Include automation boundaries and human review points.

- [ ] **Step 6: Publish the ROI calculator guide**

Explain each calculator input, gross profit versus revenue, labor savings, payback, scenario ranges, double counting, and why Alivio validates inputs before a proposal.

Add a cited implementation-pattern section using the approved home-services AI evidence register. Distinguish measured customer stories from product use-case descriptions; identify vendor-reported evidence in the visible copy; explain what each source does not prove; and never transfer an external percentage or dollar result into the visitor's calculator defaults.

- [ ] **Step 7: Add contextual conversion paths**

Every resource links to the relevant homepage/HVAC section, calculator, and Systems Review. Do not interrupt the article with multiple popups or a forced email gate.

- [ ] **Step 8: Run all site checks**

```bash
cd /Users/joel/alivio-studio
npm test
npm run check:site
```

Expected: PASS, including sitemap and internal links.

- [ ] **Step 9: Commit the initial organic library**

```bash
git add resources assets/style.css sitemap.xml tests/site-baseline.test.js
git commit -m "content: publish initial home-service ROI resources"
```

### Task 5: Create the 12-week editorial and repurposing system

**Files:**
- Create: `03-marketing/build-with-alivio/editorial-calendar.md`
- Create: `03-marketing/build-with-alivio/content-brief-template.md`
- Create: `03-marketing/build-with-alivio/content-qa.md`
- Create: `03-marketing/build-with-alivio/linkedin-repurposing.md`
- Create: `03-marketing/build-with-alivio/opted-in-monthly-email.md`

- [ ] **Step 1: Define the weekly cadence**

One substantial resource per week, three LinkedIn posts derived from it, one outbound observation angle, and one internal-link update. One verified client/build breakdown is published monthly. One opted-in email summarizes the month.

- [ ] **Step 2: Schedule 12 intent-led topics**

Cover HVAC first, then plumbing/electrical/roofing variations. Balance diagnosis, measurement, implementation, change management, and proof. Each brief defines primary question, audience, evidence sources, unique insight, CTA, internal links, and claims requiring proof.

- [ ] **Step 3: Define three LinkedIn transformations**

For each resource produce:

1. operator problem and contrarian insight;
2. short numbered diagnostic;
3. build/process lesson with transparent limitation.

Posts must sound like Joel, link only when useful, and avoid invented client dialogue or engagement bait.

- [ ] **Step 4: Define the monthly opted-in email**

Send only to subscribers or contacts with the appropriate relationship/permission. Include one operating insight, one practical diagnostic, one new resource, and one reply CTA. Apply the same authentication, postal-address, and opt-out controls as outbound email.

- [ ] **Step 5: Add content QA**

Check primary-source support, date sensitivity, client permission, search intent, non-duplication, useful examples, accessible headings, metadata, internal links, and whether the CTA naturally follows the content. For external case studies, also check evidence classification, visible vendor-reporting labels, baseline/measurement-period fidelity, limitation language, primary-source links, and separation from Alivio client proof.

- [ ] **Step 6: Commit the editorial system**

```bash
git add 03-marketing/build-with-alivio
git commit -m "docs: add Build With Alivio 12-week content system"
```

### Task 6: Create the client ROI presentation and roadmap deliverable

**Files:**
- Create: `05-templates/build-with-alivio-roi-presentation.md`
- Create: `05-templates/home-service-systems-roadmap.md`
- Create: `05-templates/client-evidence-register.md`
- Modify: `05-templates/sow-template.md`
- External artifact: Google Slides deck “Build With Alivio — Home Service ROI Review”

- [ ] **Step 1: Define the evidence register**

For every client claim require claim text, source, client approval status, permitted channel, expiration/review date, and owner. A blank or unapproved field means the claim cannot appear publicly or in a reusable sales deck. Maintain a separate external-evidence section for industry examples with operator, trade, implemented workflow, exact source wording, baseline and measurement period when supplied, evidence classification, original URL, last-verified date, caveat, permitted paraphrase, and owner. External evidence may support relevance or implementation patterns; it cannot be presented as Alivio performance evidence or as a forecast for a prospect.

- [ ] **Step 2: Write the 10-slide narrative**

Use:

```text
1. Prospect-specific operating goal
2. Current lead-to-cash flow
3. Where opportunities leak
4. Baseline inputs and evidence quality
5. Conservative / expected / upside monthly gross-profit scenario
6. First 30-day measurement and recovery plan
7. Recommended system architecture
8. Relevant Alivio proof and its limitations
9. Offer: $3K roadmap or scoped $8K–$30K implementation
10. Decision, owners, timeline, and next step
```

- [ ] **Step 3: Make the math auditable**

Every scenario slide shows monthly leads, missed-opportunity rate, recovery rate, booking rate, close rate, average job value, gross margin, labor inputs, investment, formula, and source/owner for each input. Do not show revenue as profit.

- [ ] **Step 4: Define the `$3,000` Systems Roadmap**

The template delivers current-state map, measured baseline, prioritized revenue leaks, data/integration constraints, proposed future-state workflow, ROI scenarios, fixed implementation scope options, risks, ownership, and 30/60/90-day plan. It is a paid diagnostic, not free proposal labor.

- [ ] **Step 5: Create the presentation**

During implementation, use the Presentations skill to build a polished Google Slides deck from the approved outline and existing Alivio brand assets. Include editable charts and tables, speaker notes, a confidentiality footer, and no unsupported client outcome.

- [ ] **Step 6: Align SOW language**

Update the SOW template so ROI projections are planning scenarios, measurement responsibilities are explicit, third-party costs are separated, and no business result is guaranteed.

- [ ] **Step 7: Review with three test cases**

Create invented HVAC scenarios for low, medium, and high lead volume. Verify arithmetic against the website calculator, text fit, mobile/desktop readability, PDF export, and that zero monthly benefit produces no false payback claim.

- [ ] **Step 8: Commit reusable sources**

```bash
git add 05-templates/build-with-alivio-roi-presentation.md 05-templates/home-service-systems-roadmap.md 05-templates/client-evidence-register.md 05-templates/sow-template.md
git commit -m "docs: add home-service ROI sales deliverables"
```

### Task 7: Run a controlled soft-launch cohort

**Files:**
- Create: `03-marketing/build-with-alivio/soft-launch-runbook.md`
- Create: `03-marketing/build-with-alivio/message-learning-log.md`

- [ ] **Step 1: Select a small compliant test cohort**

Choose 25–40 accounts that pass the ICP, evidence, suppression, and geographic rule checks. Include no more than two contacts per company and no suppressed contacts.

- [ ] **Step 2: Start with manual calls and individually reviewed email**

Use the approved daily limits. Joel reviews every email before it is sent. Do not automate later touches until authentication, reply routing, opt-out, suppression, and first-batch quality all pass.

- [ ] **Step 3: Capture message learning without private data**

The learning log records anonymized pattern, trade, objection/question, message used, response class, lesson, and copy/process change. Prospect PII remains in the operational system.

- [ ] **Step 4: Review after 50 calls and 25 emails**

Evaluate connection/delivery, meaningful conversations/replies, identified measurable problems, reviews booked, no-fit rate, opt-outs/complaints, and data-quality failures. Do not scale if complaint, authentication, or list-quality signals are unhealthy.

- [ ] **Step 5: Change one variable at a time**

Test audience slice, observation type, opener, resource, or CTA—not all simultaneously. Record the hypothesis before the batch and the decision afterward.

- [ ] **Step 6: Commit the non-PII learning system**

```bash
git add 03-marketing/build-with-alivio/soft-launch-runbook.md 03-marketing/build-with-alivio/message-learning-log.md
git commit -m "docs: add Build With Alivio soft-launch process"
```

## Completion Criteria

- Joel can research, call, email, qualify, and follow up using one coherent ROI narrative.
- The first four useful search resources and their internal conversion paths are live.
- A 12-week editorial system sustains one resource and three LinkedIn posts each week.
- Domain email campaigns cannot run without authentication, postal address, opt-out, suppression, and monitored replies.
- The client presentation and paid roadmap use auditable prospect inputs and never mislabel revenue as profit.
- The soft launch starts small, records learning, and scales only after quality and compliance pass.

## Implementation References

- [FTC: CAN-SPAM compliance guide for business](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- [Google: Email sender guidelines](https://support.google.com/mail/answer/81126)
- [FCC: AI-generated voices in robocalls](https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf)
