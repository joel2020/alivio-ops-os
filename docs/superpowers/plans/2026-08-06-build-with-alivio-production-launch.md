# Build With Alivio Production Launch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Instrument, verify, launch, and operate `buildwithalivio.com` as a measurable acquisition system with trustworthy reporting, safe rollback, and a disciplined 12-week improvement cycle.

**Architecture:** Search Console measures organic discovery. Consent-aware GA4 measures anonymous site behavior and named funnel events. Linear remains the source of truth for lead, review, opportunity, and deal outcomes. A weekly scorecard joins only aggregate counts and values—never prospect PII—with explicit definitions and owners. Production launches first to a controlled audience, then organic/outbound volume grows only after the operational and compliance gates stay healthy.

**Tech Stack:** Google Search Console, GA4 with consent controls, Vercel deployments/logs, Linear, static ES modules, Node.js tests, Chrome Lighthouse/accessibility tools, Alivio OS Markdown scorecards and runbooks.

## Global Constraints

- Execute after the infrastructure, conversion-site, and initial organic/outbound deliverables are complete.
- Do not make `buildwithalivio.com` canonical until the production deployment, form, email, legal, and rollback checks pass.
- Linear is authoritative for pipeline stage and commercial outcome. GA4 is diagnostic, not the revenue source of truth.
- Never send email addresses, phone numbers, names, free-text form responses, client inputs, or Linear IDs to analytics.
- Analytics loads only under the consent behavior stated in the final privacy policy. The cookie interface must make rejecting optional analytics as easy as accepting it.
- Do not record calculator input values as analytics parameters; record only the event that a calculation occurred and a coarse page context.
- Every metric has a definition, owner, cadence, data source, and known limitation.
- No public client claim launches without its evidence-register approval.
- Do not delete or overwrite a known-good Vercel deployment. Keep its URL and rollback instructions until the new release is stable.
- A launch is blocked by any false-success form behavior, missing legal identity/address, broken opt-out, mail authentication failure, certificate error, critical accessibility issue, material unsupported claim, or unverified rollback.

---

### Task 1: Define the funnel measurement contract

**Files:**
- Create: `06-metrics/build-with-alivio-funnel.md`
- Modify: `06-metrics/definitions.md`
- Modify: `06-metrics/scorecard.md`
- Create: `/Users/joel/alivio-studio/tests/analytics-contract.test.js`

- [ ] **Step 1: Define the lifecycle and source of truth**

Use:

```text
Organic impression/click/query: Search Console
Landing page/session/action: GA4
Lead submitted and persisted: Linear issue with website source
Review booked/completed: Linear stage plus calendar evidence
Qualified opportunity/proposal/won/lost: Linear pipeline stage
Deal value and weighted pipeline: Linear using existing OS definitions
```

- [ ] **Step 2: Define the exact events**

Create a data dictionary for:

```text
roi_calculation_completed
roi_review_cta_clicked
lead_form_started
lead_form_validation_failed
lead_form_persisted
booking_link_opened
resource_cta_clicked
email_link_landed
call_followup_landed
```

Allowed parameters are `page_type`, `trade`, `cta_location`, `source_class`, and non-identifying UTM values. Disallow user-entered numeric values, personal data, submission/lead IDs, and free text.

- [ ] **Step 3: Define funnel KPIs**

At minimum:

```text
Organic clicks = Search Console clicks to canonical site
Qualified website leads = persisted Linear leads that pass ICP review
Review booking rate = booked reviews / persisted review-form leads
Review show rate = completed reviews / booked reviews
Opportunity rate = qualified opportunities / completed reviews
Proposal rate = proposals / qualified opportunities
Win rate = won deals / decided proposals
Sales-cycle days = won date - persisted lead date
Source-to-won value = fixed-price value of won deals by original source
Email positive reply rate = positive human replies / delivered emails
Call meaningful-conversation rate = meaningful conversations / connected calls
```

Do not use page views or raw lead volume as primary business outcomes.

- [ ] **Step 4: Write failing analytics-contract tests**

The test scans `assets/analytics.js` and HTML data attributes. It fails if an unknown event or parameter is emitted, if forbidden names such as `email`, `phone`, `name`, `leadId`, `submissionId`, `revenueLeak`, or `calculatorValue` appear in event payload construction, or if analytics can load before consent resolution.

- [ ] **Step 5: Align the OS scorecard**

Add a compact Build With Alivio acquisition section without replacing existing cash, delivery, and weighted-pipeline metrics. Document weekly owner Joel, Friday cadence, and source limitations.

- [ ] **Step 6: Commit the measurement contract**

```bash
git add 06-metrics/build-with-alivio-funnel.md 06-metrics/definitions.md 06-metrics/scorecard.md
git commit -m "docs: define Build With Alivio funnel metrics"

cd /Users/joel/alivio-studio
git add tests/analytics-contract.test.js
git commit -m "test: define privacy-safe analytics contract"
```

### Task 2: Implement consent-aware analytics

**Files:**
- Create: `/Users/joel/alivio-studio/assets/consent.js`
- Create: `/Users/joel/alivio-studio/assets/analytics.js`
- Modify: `/Users/joel/alivio-studio/api/config.js`
- Modify: `/Users/joel/alivio-studio/.env.example`
- Modify: `/Users/joel/alivio-studio/assets/style.css`
- Modify: all public `/Users/joel/alivio-studio/*.html`
- Modify: `/Users/joel/alivio-studio/tests/analytics-contract.test.js`

- [ ] **Step 1: Confirm the contract test fails**

```bash
cd /Users/joel/alivio-studio
node --test tests/analytics-contract.test.js
```

Expected: FAIL because consent and analytics modules do not exist.

- [ ] **Step 2: Add public GA configuration**

Add `GA_MEASUREMENT_ID` to `.env.example`. Return it from `/api/config` as a public value only when configured. Never expose any Google API secret.

- [ ] **Step 3: Implement consent state**

Use one first-party consent key with version and timestamp. Initial optional analytics state is denied. Render a keyboard-accessible banner with equally prominent “Reject optional analytics” and “Accept analytics” actions plus a persistent footer link to reopen settings. Core forms, calculator, booking, and navigation work when analytics is rejected.

- [ ] **Step 4: Implement the analytics adapter**

Export:

```js
track(eventName, allowedParameters)
setAnalyticsConsent('granted' | 'denied')
```

Queue allowed events until consent is granted, discard them on denial, load Google’s tag only once, and enforce the event/parameter allowlists from the measurement contract. Sanitize UTM values to bounded alphanumeric/hyphen strings.

- [ ] **Step 5: Instrument the funnel**

Add declarative `data-analytics-event`, `data-page-type`, and `data-cta-location` attributes to relevant controls. Form persistence is tracked only after the API returns success; validation failure includes no field name or value.

- [ ] **Step 6: Update privacy disclosure and CSP**

Describe GA4, consent storage, data purpose, and how to withdraw consent. Permit only the exact Google tag/collection origins required by current official GA4 documentation. Keep all other existing CSP restrictions.

- [ ] **Step 7: Run tests and browser verification**

```bash
npm test
npm run check:site
```

In Chrome verify: no Google request before consent; none after rejection; one loader after acceptance; withdrawal stops optional collection; permitted events contain no PII.

- [ ] **Step 8: Commit analytics**

```bash
git add assets/consent.js assets/analytics.js assets/style.css api/config.js .env.example privacy.html vercel.json *.html tests/analytics-contract.test.js
git commit -m "feat: add consent-aware funnel analytics"
```

### Task 3: Configure Search Console and production measurement accounts

**External systems:**
- Google Search Console
- Google Analytics 4
- Hostinger DNS
- Vercel environment variables

**Files:**
- Create: `docs/runbooks/build-with-alivio-measurement.md`

- [ ] **Step 1: Create the GA4 property and web stream**

Name the property for Build With Alivio under the Alivio-owned Google account. Set the correct reporting time zone and currency. Disable advertising personalization/signals unless a later approved use requires them. Record the non-secret Measurement ID and ownership details.

- [ ] **Step 2: Add the Measurement ID to Vercel**

Store `GA_MEASUREMENT_ID` in Production and a separate test stream in Preview. Deploy preview and verify only the test property receives test events.

- [ ] **Step 3: Create a domain Search Console property**

Verify `buildwithalivio.com` with the exact DNS TXT record Google supplies. Preserve all web and mail records. Submit `https://buildwithalivio.com/sitemap.xml` only after the production domain is live and canonical.

- [ ] **Step 4: Configure conversion reporting carefully**

Mark only `lead_form_persisted` and the validated booking-completion event—if the booking provider supplies a reliable non-PII signal—as key events. Do not count CTA clicks as leads.

- [ ] **Step 5: Verify data flow**

Use GA DebugView/Realtime and Search Console URL Inspection. Confirm canonical URLs, no preview-host indexing, event allowlists, correct stream, and sitemap acceptance.

- [ ] **Step 6: Document access and recovery**

Record owners, backup owner, account names, property/stream IDs, verification method, and recovery procedure. Store no password or token.

- [ ] **Step 7: Commit the measurement runbook**

```bash
git add docs/runbooks/build-with-alivio-measurement.md
git commit -m "docs: add Build With Alivio measurement runbook"
```

### Task 4: Build a repeatable release verification suite

**Files:**
- Create: `/Users/joel/alivio-studio/scripts/check-production.mjs`
- Create: `/Users/joel/alivio-studio/tests/production-check.test.js`
- Create: `docs/runbooks/build-with-alivio-release-checklist.md`

- [ ] **Step 1: Write failing production-check tests**

Mock network responses and require the checker to detect certificate/HTTP failure, incorrect canonical, `www` redirect loop, missing security headers, missing sitemap page, indexable preview host, API config leakage, and form false success.

- [ ] **Step 2: Implement a read-only production checker**

`check-production.mjs --base-url https://preview-deployment.vercel.app` verifies:

```text
HTTPS and final host
www -> apex redirect
status for every sitemap URL
canonical and robots directives
security headers
robots and sitemap consistency
/api/config contains only allowlisted public keys
/api/leads rejects GET and malformed POST safely
no known placeholder contact/legal/claim strings
```

It must never submit a valid production lead.

- [ ] **Step 3: Run focused tests**

```bash
cd /Users/joel/alivio-studio
node --test tests/production-check.test.js
```

Expected: PASS after the checker is implemented.

- [ ] **Step 4: Create the human release checklist**

Cover visual/browser review, keyboard/screen reader, responsive layouts, reduced motion, real test lead with `[TEST]` source, Linear dedupe, notification, booking, mail authentication, analytics consent, legal identity/address, client evidence, performance, security headers, DNS, rollback, and owner sign-off.

- [ ] **Step 5: Commit the release suite**

```bash
cd /Users/joel/alivio-studio
git add scripts/check-production.mjs tests/production-check.test.js
git commit -m "test: add production release checker"

cd /Users/joel/alivio-ops-os
git add docs/runbooks/build-with-alivio-release-checklist.md
git commit -m "docs: add Build With Alivio release checklist"
```

### Task 5: Conduct the pre-production audit

**Files:**
- Modify: `docs/runbooks/build-with-alivio-release-checklist.md`
- Reference: `docs/runbooks/build-with-alivio-infrastructure.md`
- Reference: `docs/runbooks/build-with-alivio-site-verification.md`
- Reference: `docs/runbooks/build-with-alivio-measurement.md`

- [ ] **Step 1: Freeze a release candidate**

Record the exact Git commit and Vercel preview deployment URL. Make only blocker fixes after the freeze; each fix gets its own commit and retest.

- [ ] **Step 2: Run repository checks**

```bash
cd /Users/joel/alivio-studio
npm test
npm run check:site
git status --short
git log -1 --oneline
```

Expected: all tests pass, no unintended files, known commit recorded.

- [ ] **Step 3: Verify content and commercial truth**

Review every page, email, call script, slide, and downloadable against the offer ladder and evidence register. Prices, call duration, retainer minimum, client proof, and ROI disclaimers must match.

- [ ] **Step 4: Verify legal and outreach readiness**

Confirm privacy/terms reflect the live tools, valid physical postal address is published where required, sending-readiness is `READY`, suppression works, and the first campaign has passed QA. If legal review is pending, launch may proceed without outbound campaigns only if the public site itself is approved and compliant; outbound remains blocked.

- [ ] **Step 5: Verify real integration paths**

Using an approved test identity, complete one preview form and booking. Confirm one `[TEST]` Linear issue, correct qualification data, no duplicate, notification delivery, calendar event, cancellation, and clean deletion/closure of the test record under the retention policy.

- [ ] **Step 6: Verify accessibility, performance, and security**

Run Lighthouse on homepage, HVAC, Systems Review, and the longest resource. Manually verify keyboard order, focus, form errors, zoom, contrast, mobile navigation, reduced motion, and no horizontal scroll. Review response headers and browser console/network errors.

- [ ] **Step 7: Test rollback**

Promote and then roll back a harmless preview-to-preview test, or document an equivalent verified Vercel rollback without touching production. Confirm the prior deployment URL is retained.

- [ ] **Step 8: Record the launch decision**

Every line is `PASS`, `BLOCKED`, or `NOT APPLICABLE` with evidence. Production can launch only with zero `BLOCKED` items in domain, forms, legal identity, claims, accessibility-critical, security-critical, email authentication, or rollback categories.

- [ ] **Step 9: Commit the signed audit**

```bash
git add docs/runbooks/build-with-alivio-release-checklist.md
git commit -m "docs: approve Build With Alivio release candidate"
```

### Task 6: Launch production with a controlled rollback window

**External systems:**
- Vercel project `alivio-studio`
- Hostinger DNS
- Search Console and GA4
- Linear and booking provider

**Files:**
- Modify: `docs/runbooks/build-with-alivio-release-checklist.md`

- [ ] **Step 1: Deploy the approved commit to Vercel production**

Confirm the deployment’s source commit matches the signed release candidate. Do not deploy uncommitted local files.

- [ ] **Step 2: Apply the staged domain cutover and confirm the certificate**

Use the exact apex and `www` web records captured in the infrastructure runbook and apply them at Hostinger. Preserve MX, SPF, DKIM, DMARC, Turnstile verification, Search Console verification, and every unrelated DNS record. Set `buildwithalivio.com` as the production domain, confirm Vercel provisions the certificate, confirm `www` redirects once to the apex, and keep the Vercel preview domain non-canonical and out of the sitemap.

- [ ] **Step 3: Run immediate read-only checks**

```bash
cd /Users/joel/alivio-studio
node scripts/check-production.mjs --base-url https://buildwithalivio.com
```

Expected: PASS.

- [ ] **Step 4: Complete one controlled production conversion**

Submit using an approved Alivio test identity and source `production-smoke-test`. Confirm Linear persistence, dedupe, notification, booking link, consent behavior, and that analytics contains no PII. Mark and close the test issue.

- [ ] **Step 5: Submit the sitemap and request indexing**

Submit the production sitemap in Search Console. Inspect the homepage, HVAC, Systems Review, and resource hub. Do not request indexing for preview or legal pages unless intended.

- [ ] **Step 6: Monitor the rollback window**

For the first two hours, inspect Vercel function errors, form persistence, domain/certificate, mail delivery, consent/analytics, and layout at mobile/desktop. For the first 72 hours, check at least morning and afternoon. Roll back on false-success submissions, sustained server errors, security regression, certificate/redirect failure, or material broken conversion path.

- [ ] **Step 7: Record production evidence**

Capture final domain, deployment, commit, smoke-test Linear issue, sitemap status, analytics stream, time of launch, and owner. Exclude secrets and PII.

- [ ] **Step 8: Commit the launch record**

```bash
git add docs/runbooks/build-with-alivio-release-checklist.md
git commit -m "docs: record Build With Alivio production launch"
```

### Task 7: Start the four-week soft-launch operating rhythm

**Files:**
- Create: `05-templates/build-with-alivio-weekly-review.md`
- Create: `06-metrics/build-with-alivio-weekly-log.md`
- Modify: `00-charter/cadence-calendar.md`

- [ ] **Step 1: Add the weekly review to the OS cadence**

Friday review covers data quality, organic queries/pages, call/email activity, meaningful engagement, reviews, opportunities, pipeline value, opt-outs/complaints, content shipped, site failures, and one improvement decision.

- [ ] **Step 2: Create the weekly log schema**

Record week ending, activity, outcomes, rates, weighted pipeline, won value, source, data completeness, anomalies, learning, decision, owner, and due date. Store aggregates only; prospect details remain in Linear.

- [ ] **Step 3: Set initial operating limits**

Weeks 1–2 after launch:

```text
Calls: up to 60/week
Personalized emails: up to 50/week, only after sending gate READY
Resources: 1/week
LinkedIn posts: 3/week
Client/build breakdown: 1/month
Opted-in email: 1/month
```

- [ ] **Step 4: Define scale/hold rules**

Scale one channel only when its data is trustworthy, compliance is clean, reply/conversation quality is acceptable, reviews are attended, and Joel has capacity to follow up within one business day. Hold or reduce on complaints, bounces, low relevance, missed follow-ups, weak show rate, or delivery overload.

- [ ] **Step 5: Commit the operating cadence**

```bash
git add 05-templates/build-with-alivio-weekly-review.md 06-metrics/build-with-alivio-weekly-log.md 00-charter/cadence-calendar.md
git commit -m "docs: add Build With Alivio weekly operating cadence"
```

### Task 8: Run the 30/60/90-day optimization reviews

**Files:**
- Create: `03-marketing/build-with-alivio/30-60-90-review.md`
- Modify per review: `06-metrics/build-with-alivio-weekly-log.md`
- Modify per decision: relevant site/campaign/OS files

- [ ] **Step 1: Complete Day 30 review**

Audit tracking accuracy, query/index coverage, resource engagement, outbound list quality, call/email language, review booking/show rate, qualification, and response SLA. Fix measurement or process defects before optimizing conversion copy.

- [ ] **Step 2: Complete Day 60 review**

Compare trades, source paths, problems, and offers. Decide whether HVAC remains the sole landing-page priority or whether one proven adjacent trade merits its own page. Require enough observed conversations/leads to justify segmentation.

- [ ] **Step 3: Complete Day 90 review**

Assess qualified pipeline, wins/losses, sales cycle, offer uptake, delivery capacity, content compounding, and whether Linear remains adequate. Decide continue, narrow, expand, or pause each channel.

- [ ] **Step 4: Apply evidence to public proof**

Only after signed client permission and verified baseline/outcome data, update the evidence register and create a quantified case study. Show measurement window, starting point, intervention, result, attribution limits, and client approval.

- [ ] **Step 5: Update the next 12-week plan**

Choose topics and experiments from actual queries, calls, emails, objections, and pipeline—not generic content volume. Keep one primary hypothesis per experiment.

- [ ] **Step 6: Commit each review**

Use the matching command for the completed review:

```bash
git add 03-marketing/build-with-alivio/30-60-90-review.md 06-metrics/build-with-alivio-weekly-log.md
git commit -m "docs: record Build With Alivio day 30 review"
git commit -m "docs: record Build With Alivio day 60 review"
git commit -m "docs: record Build With Alivio day 90 review"
```

Run only one of the three commit commands for that review.

## Completion Criteria

- Search Console, privacy-safe analytics, Linear, and the weekly scorecard agree on their respective parts of the funnel.
- The production release passes automated and human checks and has a tested rollback.
- The site’s real form, booking, email, and domain paths work without false success or PII leakage.
- The launch starts with controlled organic/call/email activity and clear scale/hold rules.
- Day 30/60/90 decisions use observed pipeline and operational evidence, not vanity traffic.

## Implementation References

- [Vercel: Setting up a custom domain](https://vercel.com/docs/domains/set-up-custom-domain)
- [Vercel: Firewall overview](https://vercel.com/docs/vercel-firewall)
- [Google Search Console Help](https://support.google.com/webmasters/)
- [Google Analytics Help](https://support.google.com/analytics/)
