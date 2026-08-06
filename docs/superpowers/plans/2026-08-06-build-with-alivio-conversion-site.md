# Build With Alivio Conversion Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing Alivio Studio Vercel mock-up into a credible, ROI-first home-services funnel that captures qualified leads durably, shows transparent financial scenarios, and is safe to launch on `buildwithalivio.com`.

**Architecture:** Keep the current dependency-light static HTML/CSS/JavaScript site and visual identity. Add small browser ES modules for the ROI calculator and lead form, testable pure modules for business logic, and Vercel Functions for configuration, Turnstile verification, Linear persistence, and notifications. The browser never receives private credentials. The primary journey is homepage or HVAC landing page → ROI calculator → Systems Review form → booking page.

**Tech Stack:** Static HTML5/CSS, browser ES modules, Node.js 24, `node:test`, Vercel Functions, Linear GraphQL API, Cloudflare Turnstile, Resend transactional email, Schema.org JSON-LD.

## Global Constraints

- Work in `/Users/joel/alivio-studio`; do not move the site into the operations-system repository.
- Preserve the current design language, media, and useful motion while replacing unsupported claims and dead interactions.
- Use the company name “Alivio Studio.” “Build With Alivio” is the domain/campaign CTA, not a new legal entity.
- Do not publish client revenue, lead, conversion, time-saving, testimonial, or attribution claims without written evidence.
- The Bravo Mechanical case study may describe the verified website, CRM, intake, and workflow build; quantified results remain absent until documented.
- Use the approved offer ladder: free 30-minute review, `$3,000` fixed roadmap, `$8,000–$30,000` typical implementation, and `$2,000–$5,000/month` managed optimization with a three-month minimum.
- Do not say “cancel anytime,” “45-minute call,” “four specialists on every engagement,” or imply guaranteed ROI.
- All calculations must expose their inputs and label results as scenarios, not promises.
- A lead is successful only after Linear returns an issue ID. Email notification is secondary and must not be the sole record.
- No secrets or private client information in source, browser bundles, logs, analytics events, or test fixtures.
- Use test-driven development for validation, ROI math, Linear mapping, endpoint behavior, and internal-link checks.
- Do not deploy production until the infrastructure plan passes.
- Source design: `/Users/joel/alivio-ops-os/docs/superpowers/specs/2026-08-06-build-with-alivio-launch-design.md`.

---

### Task 1: Establish a zero-dependency test and configuration baseline

**Files:**
- Create: `/Users/joel/alivio-studio/package.json`
- Create: `/Users/joel/alivio-studio/.env.example`
- Create: `/Users/joel/alivio-studio/tests/site-baseline.test.js`
- Create: `/Users/joel/alivio-studio/scripts/check-site.mjs`
- Modify: `/Users/joel/alivio-studio/.gitignore`

- [ ] **Step 1: Write a green test for the blocker-detection engine**

Test the audit engine against temporary HTML fixtures: one clean page must return no findings, and one intentionally invalid fixture must report missing title/description/canonical/H1/skip link, broken local navigation, duplicate IDs, and the known placeholder patterns. The test suite verifies detection behavior without treating the current production mock-up as a passing fixture.

The production-site audit checks that every public HTML page has one title, one meta description, one canonical URL on `https://buildwithalivio.com`, one H1, a skip link, valid local navigation targets, and no known placeholders:

```js
const forbidden = [
  /\+1\s*\(?(?:555)/i,
  /hello@alivio\.studio/i,
  /href=["']#["']/i,
  /class=["'][^"']*pending/i,
  /cancel anytime/i,
  /45-minute/i,
];
```

Expected fixture-test result: PASS. Expected production audit result: FAIL on placeholder contact/legal links and missing canonical metadata.

- [ ] **Step 2: Add the test runner**

Create `package.json`:

```json
{
  "name": "alivio-studio",
  "private": true,
  "type": "module",
  "engines": { "node": "24.x" },
  "scripts": {
    "test": "node --test tests/*.test.js",
    "check:site": "node scripts/check-site.mjs"
  }
}
```

- [ ] **Step 3: Define the environment contract without values**

Create `.env.example` with names and comments only:

```dotenv
LINEAR_API_KEY=
LINEAR_TEAM_ID=
LINEAR_PROJECT_ID=
LINEAR_WEBSITE_LABEL_ID=
RESEND_API_KEY=
LEAD_NOTIFY_TO=
BOOKING_URL=
TURNSTILE_SECRET_KEY=
TURNSTILE_SITE_KEY=
ALLOWED_ORIGINS=https://buildwithalivio.com,https://www.buildwithalivio.com
INTEGRATION_MODE=production
```

- [ ] **Step 4: Protect local secrets**

Add `.env`, `.env.local`, and `.env.*.local` to `.gitignore`, while keeping `.env.example` tracked.

- [ ] **Step 5: Implement the site scanner**

`check-site.mjs` exports the pure audit helpers used by the tests and, when executed directly, recursively scans public `.html`, `.xml`, `.txt`, `.js`, and `.css` files while excluding `.git`, `.vercel`, `.worktrees`, `node_modules`, and `tests`. It exits nonzero for broken local links, forbidden placeholder strings, duplicate page IDs, missing canonical metadata, or a sitemap URL without a corresponding page.

- [ ] **Step 6: Confirm the baseline fails for real blockers**

Run:

```bash
npm test
npm run check:site
```

Expected: `npm test` passes the audit-engine fixture tests. `npm run check:site` fails with named current-site blockers, not syntax or test-discovery errors.

- [ ] **Step 7: Commit the test harness**

```bash
git add package.json .env.example .gitignore tests/site-baseline.test.js scripts/check-site.mjs
git commit -m "test: add Alivio site launch checks"
```

### Task 2: Implement and test the ROI model

**Files:**
- Create: `/Users/joel/alivio-studio/lib/roi.js`
- Create: `/Users/joel/alivio-studio/tests/roi.test.js`
- Create: `/Users/joel/alivio-studio/assets/roi-calculator.js`

- [ ] **Step 1: Write failing unit tests for the financial model**

Test input normalization, percentage bounds, zero values, invalid numbers, scenario ordering, monthly benefit, and payback. Use this public contract:

```ts
type RoiInput = {
  monthlyLeads: number;
  missedOpportunityRatePct: number;
  recoveryRatePct: number;
  bookingRatePct: number;
  closeRatePct: number;
  averageJobValue: number;
  grossMarginPct: number;
  adminHoursSaved: number;
  loadedHourlyCost: number;
  implementationInvestment: number;
};

type RoiScenario = {
  recoveredOpportunities: number;
  additionalBookedJobs: number;
  additionalRevenue: number;
  additionalGrossProfit: number;
  monthlyLaborSavings: number;
  monthlyBenefit: number;
  paybackMonths: number | null;
};

calculateRoi(input: RoiInput): {
  conservative: RoiScenario;
  expected: RoiScenario;
  upside: RoiScenario;
};
```

Use recovery multipliers `0.60`, `1.00`, and `1.25`, capping the effective recovery rate at 100%.

- [ ] **Step 2: Confirm the ROI tests fail**

```bash
node --test tests/roi.test.js
```

Expected: FAIL because `lib/roi.js` does not yet export the contract.

- [ ] **Step 3: Implement the minimum pure calculation**

Use these formulas:

```text
recoverable opportunities = monthly leads × missed opportunity rate
recovered opportunities = recoverable opportunities × scenario recovery rate
additional booked jobs = recovered opportunities × booking rate × close rate
additional revenue = additional booked jobs × average job value
additional gross profit = additional revenue × gross margin
monthly labor savings = admin hours saved × loaded hourly cost
monthly benefit = additional gross profit + monthly labor savings
payback months = implementation investment ÷ monthly benefit
```

Return `null` payback when monthly benefit is zero. Reject non-finite, negative, or out-of-range inputs with field-specific messages.

- [ ] **Step 4: Run the ROI tests**

```bash
node --test tests/roi.test.js
```

Expected: PASS.

- [ ] **Step 5: Build an accessible browser controller**

`assets/roi-calculator.js` imports the pure function, updates all three scenarios on input, uses `Intl.NumberFormat`, announces recalculation through a polite live region, and never stores inputs remotely. Provide a “Review these numbers with Alivio” button that copies the calculator values into matching hidden form fields, scrolls to the qualification form, and moves focus to its heading.

- [ ] **Step 6: Commit the ROI model**

```bash
git add lib/roi.js tests/roi.test.js assets/roi-calculator.js
git commit -m "feat: add transparent home-service ROI calculator"
```

### Task 3: Define lead validation and Linear persistence

**Files:**
- Create: `/Users/joel/alivio-studio/lib/lead-validation.js`
- Create: `/Users/joel/alivio-studio/lib/linear.js`
- Create: `/Users/joel/alivio-studio/tests/lead-validation.test.js`
- Create: `/Users/joel/alivio-studio/tests/linear.test.js`

- [ ] **Step 1: Write failing validation tests**

Define and test this request:

```ts
type LeadSubmission = {
  submissionId: string;
  name: string;
  business: string;
  email: string;
  phone: string;
  website?: string;
  trade: 'hvac' | 'plumbing' | 'electrical' | 'roofing' | 'other';
  serviceArea: string;
  teamSize: '1-4' | '5-19' | '20-49' | '50-100' | '100+';
  monthlyLeadVolume: 'under-50' | '50-149' | '150-499' | '500+' | 'unknown';
  crm?: string;
  phoneSystem?: string;
  schedulingTool?: string;
  biggestRevenueLeak: string;
  decisionMaker: 'yes' | 'with-partner' | 'no';
  timeline: '0-30-days' | '31-90-days' | 'later' | 'exploring';
  investmentRange: 'under-8k' | '8k-15k' | '15k-30k' | '30k+' | 'unknown';
  contactConsent: true;
  source: string;
  utm: { source?: string; medium?: string; campaign?: string; content?: string };
  roi?: Partial<RoiInput>;
  turnstileToken: string;
  companyFax?: string;
};
```

Require a valid UUID submission ID, human-readable field errors, trimmed strings, maximum lengths, a valid email, HTTPS-normalized optional website, checked contact consent, empty honeypot `companyFax`, and a bounded JSON body. Label the field “Business email” in the UI but do not reject a valid free-mail address; owner-operators may legitimately use one.

- [ ] **Step 2: Write failing Linear mapping tests**

Test that a validated submission becomes exactly one deterministic issue payload, escaping Markdown and excluding secrets and the Turnstile token. The title is `<Business> — Home Service ROI Review`. The description includes source/UTM, contact consent timestamp, ROI inputs as estimates, and all qualification fields.

- [ ] **Step 3: Run tests and observe failure**

```bash
node --test tests/lead-validation.test.js tests/linear.test.js
```

Expected: FAIL because the modules do not exist.

- [ ] **Step 4: Implement validation and normalization**

Export:

```js
validateLeadSubmission(raw) // => { ok: true, value } | { ok: false, errors }
normalizeWebsite(value)     // => normalized URL or null
```

Do not accept arbitrary enum strings or silently coerce invalid numeric ROI fields.

- [ ] **Step 5: Implement the Linear client contract**

Export:

```js
buildLinearIssueInput(lead, config)
findRecentOpenLead({ email, businessDomain }, config, fetchImpl)
createLinearLead(lead, config, fetchImpl)
```

Use the GraphQL endpoint `https://api.linear.app/graphql`, an abort timeout, explicit handling for HTTP failure and GraphQL `errors`, and a submission-ID plus recent-open-lead lookup before creation. If a duplicate exists, add a comment only when the same submission has not already been attached, then return the existing issue ID.

- [ ] **Step 6: Run focused tests**

```bash
node --test tests/lead-validation.test.js tests/linear.test.js
```

Expected: PASS.

- [ ] **Step 7: Commit the persistence contract**

```bash
git add lib/lead-validation.js lib/linear.js tests/lead-validation.test.js tests/linear.test.js
git commit -m "feat: validate and persist qualified leads in Linear"
```

### Task 4: Build the secure lead endpoint and client form controller

**Files:**
- Create: `/Users/joel/alivio-studio/api/config.js`
- Create: `/Users/joel/alivio-studio/api/leads.js`
- Create: `/Users/joel/alivio-studio/lib/turnstile.js`
- Create: `/Users/joel/alivio-studio/lib/notification.js`
- Create: `/Users/joel/alivio-studio/assets/lead-form.js`
- Create: `/Users/joel/alivio-studio/tests/leads-api.test.js`

- [ ] **Step 1: Write failing endpoint tests**

Use mocked request/response objects and injected `fetch` to test:

- only `POST` is accepted by `/api/leads`;
- `Content-Type: application/json` and an allowed Origin are required;
- bodies above 32 KB return `413`;
- invalid fields return `400` with safe field errors;
- failed Turnstile returns `400` without contacting Linear;
- Linear failure returns `503` and never reports success;
- Linear success returns `{ ok: true, submissionId, leadId, bookingUrl }`;
- notification failure after Linear success returns success and logs only the submission ID;
- preview mode marks issues `[TEST]` and uses the test label;
- no response or log contains API keys, the Turnstile token, or the full lead body.
- a retry with the same submission ID returns the same Linear issue and does not append duplicate content.

- [ ] **Step 2: Confirm endpoint tests fail**

```bash
node --test tests/leads-api.test.js
```

Expected: FAIL because the endpoint modules do not exist.

- [ ] **Step 3: Implement public configuration**

`GET /api/config` returns only:

```json
{
  "bookingUrl": "<configured public URL>",
  "turnstileSiteKey": "<configured public site key>"
}
```

Return `503` if either required value is absent. Add `Cache-Control: public, max-age=300, stale-while-revalidate=3600` and restrict CORS to configured origins.

- [ ] **Step 4: Implement Turnstile verification**

Server-side verification sends the token, secret, request IP, and submission UUID as Turnstile’s idempotency key to Cloudflare’s Siteverify endpoint with a timeout. Require `success`, expected hostname in production, and expected action `systems_review`. Treat tokens as single-use and five-minute-lived: a recoverable retry resets the widget and obtains a new token while keeping the same lead submission ID.

- [ ] **Step 5: Implement notification as a secondary side effect**

After Linear persistence, send a plain-text and escaped-HTML notification through Resend. The message contains the Linear issue URL and the minimum contact/qualification data needed for response. Never send the Turnstile token, raw request, or secret configuration.

- [ ] **Step 6: Implement the endpoint**

Use explicit dependency injection so tests do not contact external services. Require and validate the browser-generated cryptographically random submission ID. Response rules:

```text
400 invalid JSON, validation, honeypot, or Turnstile
403 origin not allowed
405 wrong method
413 oversized body
503 Linear unavailable or required server configuration missing
200 Linear lead persisted, even if the notification subsequently fails
```

- [ ] **Step 7: Implement the browser form controller**

`lead-form.js` loads `/api/config`, renders Turnstile, creates a submission UUID with `crypto.randomUUID()`, submits JSON once, prevents double submission, keeps entered values on recoverable errors, resets Turnstile before a retry, moves focus to an error summary, and redirects to the configured booking URL only after the API returns `ok: true`. Keep the same submission ID for retries of unchanged form data within the browser session; create a new ID after a successful submission or material edit.

- [ ] **Step 8: Run endpoint tests**

```bash
node --test tests/leads-api.test.js
```

Expected: PASS.

- [ ] **Step 9: Commit the lead flow**

```bash
git add api/config.js api/leads.js lib/turnstile.js lib/notification.js assets/lead-form.js tests/leads-api.test.js
git commit -m "feat: add secure ROI review lead flow"
```

### Task 5: Rewrite the homepage around immediate measurable ROI

**Files:**
- Modify: `/Users/joel/alivio-studio/index.html`
- Modify: `/Users/joel/alivio-studio/assets/style.css`
- Modify: `/Users/joel/alivio-studio/assets/site.js`

- [ ] **Step 1: Add a failing homepage content test**

Extend `site-baseline.test.js` to require the approved homepage sections in order: ROI-first hero, revenue leaks, transparent ROI calculator, First 30 Days, offer ladder, proof, process, FAQ, final review CTA.

Expected: FAIL against the existing homepage.

- [ ] **Step 2: Replace the hero and primary CTA**

Use this message hierarchy:

```text
Eyebrow: AI systems and websites for US home-service companies
H1: Turn missed leads and slow follow-up into measurable gross profit.
Support: Alivio Studio builds the intake, follow-up, CRM, website, and reporting
systems that help home-service operators book more of the demand they already earn.
Primary CTA: Calculate your opportunity
Secondary CTA: Book a 30-minute ROI review
Trust note: Conservative scenarios. Transparent inputs. No guaranteed outcomes.
```

- [ ] **Step 3: Remove unsupported figures**

Delete or replace every current placeholder statistic, testimonial, fake logo attribution, and outcome claim. Use factual capability statements and the transparent calculator until written evidence exists.

- [ ] **Step 4: Add the revenue-leak section**

Explain four concrete leaks: missed calls/slow response, inconsistent booking and routing, estimates without follow-up, and fragmented reporting. Connect each to a metric Alivio can baseline in the first week.

- [ ] **Step 5: Mount the ROI calculator**

Add labeled inputs, explanations, conservative/expected/upside cards, the formula disclosure, a disclaimer, and the form-prefill CTA. Do not pre-populate results in a way that looks like a client outcome.

- [ ] **Step 6: Add the First 30 Days plan**

Present:

```text
Days 1–5: baseline leads, missed calls, speed-to-lead, booking, close, and margin
Days 6–12: install end-to-end tracking and ownership
Days 13–21: fix routing, missed-call response, lead response, and estimate follow-up
Days 22–30: compare baseline to live results and prioritize the next constraint
```

- [ ] **Step 7: Add the approved offers and truthful proof**

List the exact offer ladder and explain fixed-price scoping. Use Bravo Mechanical as a factual build example with no quantified result. Use RLTRS and one of It’s Lit Neon/Elite Funding only for relevant delivery breadth, not home-service ROI proof.

Add a visually separate “How home-service operators are using AI” evidence section based on the approved research register. Each item must identify the operator/trade, implemented workflow, original source, evidence classification, publication or review date, reported outcome only when the source provides one, and a concise limitation. Label vendor customer stories as “vendor-reported industry example.” Never imply that an external result belongs to Alivio, that Alivio implemented it, or that the same result is expected for the visitor. Link to the primary source, avoid third-party logos unless permission is documented, and omit any figure whose baseline, period, or wording cannot be verified.

- [ ] **Step 8: Replace the global CTA and contact details**

Use `hello@buildwithalivio.com`; remove the fake phone number until a real business line is supplied. Remove the demo form handlers from `assets/site.js` and load the new ES modules only where needed.

- [ ] **Step 9: Make the responsive and reduced-motion states complete**

Verify calculator tables/cards, range/input controls, CTA groups, live messages, and proof cards at 320, 768, 1024, and 1440 CSS pixels. Respect `prefers-reduced-motion` and preserve visible focus indicators.

- [ ] **Step 10: Run homepage checks**

```bash
npm test
npm run check:site
```

Expected: homepage-specific tests PASS; other not-yet-fixed pages may still fail and must be named.

- [ ] **Step 11: Commit the homepage conversion rewrite**

```bash
git add index.html assets/style.css assets/site.js tests/site-baseline.test.js
git commit -m "feat: reposition homepage around home-service ROI"
```

### Task 6: Create the primary funnel landing pages

**Files:**
- Create: `/Users/joel/alivio-studio/hvac.html`
- Create: `/Users/joel/alivio-studio/systems-review.html`
- Modify: `/Users/joel/alivio-studio/contact.html`
- Modify: `/Users/joel/alivio-studio/assets/style.css`
- Modify: `/Users/joel/alivio-studio/tests/site-baseline.test.js`

- [ ] **Step 1: Write failing page-structure tests**

Require unique title/description/H1, canonical URL, one primary intent, breadcrumbs, truthful pricing, form labels, consent copy, success/error regions, and links between HVAC → calculator/review → booking.

- [ ] **Step 2: Build the HVAC landing page**

Structure it around HVAC-specific operational leaks: after-hours/missed calls, seasonal lead spikes, dispatch/routing, replacement-estimate follow-up, membership/service reminders, and source-to-gross-profit reporting. Avoid promises that AI replaces dispatchers or guarantees bookings.

- [ ] **Step 3: Build the Systems Review page**

Explain who the review is for, what Joel will inspect, what inputs the prospect should bring, what they receive, the no-fit/roadmap/implementation outcomes, and the exact offer prices. Embed the complete qualified-lead form and Turnstile container.

- [ ] **Step 4: Refactor the contact page**

Make general contact secondary. Route sales intent to `systems-review.html`; provide the monitored email for partnerships or existing clients. Remove fake phone, demo behavior, and unsupported FAQ claims.

- [ ] **Step 5: Add form privacy and consent language**

The unchecked consent must say Alivio may contact the submitter about the requested review by email or phone, standard carrier rates may apply, consent is not a purchase condition, and Privacy/Terms links are available. Do not add SMS consent until an SMS program exists.

- [ ] **Step 6: Run the focused checks**

```bash
node --test tests/site-baseline.test.js
npm run check:site
```

Expected: PASS for the new funnel pages and their internal links.

- [ ] **Step 7: Commit the funnel pages**

```bash
git add hvac.html systems-review.html contact.html assets/style.css tests/site-baseline.test.js
git commit -m "feat: add HVAC and ROI review funnel pages"
```

### Task 7: Convert the remaining site into a consistent sales narrative

**Files:**
- Modify: `/Users/joel/alivio-studio/services.html`
- Modify: `/Users/joel/alivio-studio/approach.html`
- Modify: `/Users/joel/alivio-studio/work.html`
- Modify: `/Users/joel/alivio-studio/about.html`
- Modify: `/Users/joel/alivio-studio/index.html`
- Modify: `/Users/joel/alivio-studio/assets/style.css`

- [ ] **Step 1: Add failing assertions for shared claims and navigation**

Require the same company identity, contact address, offer names, price facts, 30-minute review wording, and CTA across every page. Require real links for every social icon or remove the icon.

- [ ] **Step 2: Rewrite Services**

Organize capabilities around measurable systems: lead capture and response, sales/estimate follow-up, CRM and workflow automation, conversion websites, operations/reporting, and managed optimization. Map each to inputs, deliverables, KPI, and likely project range.

- [ ] **Step 3: Rewrite Approach**

Use baseline → roadmap → fixed-price implementation → 30-day validation → optional managed optimization. Remove unsupported staffing promises and reconcile the copy with Alivio’s fixed-price operating charter.

- [ ] **Step 4: Rewrite Work**

Separate verified delivery facts from outcomes. Bravo gets the anchor home-service build story. RLTRS and the selected supporting client demonstrate technical/platform and web/campaign range. Label outcome fields “measurement pending” internally; do not render them publicly.

- [ ] **Step 5: Rewrite About**

Position Joel and Alivio Studio credibly for US home-service operators without inventing headcount, offices, awards, partnerships, or years of experience. Keep Brussels origin only if it helps the story; make US client service hours and remote delivery explicit.

- [ ] **Step 6: Standardize global navigation and footer**

Primary navigation: Services, HVAC, Work, Approach, About, Resources, Systems Review. Footer: `hello@buildwithalivio.com`, no fake phone, real legal links, and only verified social profiles.

- [ ] **Step 7: Run the full checks**

```bash
npm test
npm run check:site
```

Expected: no copy-contract or broken-link failures.

- [ ] **Step 8: Commit the narrative alignment**

```bash
git add index.html services.html approach.html work.html about.html assets/style.css tests/site-baseline.test.js
git commit -m "content: align Alivio site with the approved offer"
```

### Task 8: Add legal, SEO, social, and security foundations

**Files:**
- Create: `/Users/joel/alivio-studio/privacy.html`
- Create: `/Users/joel/alivio-studio/terms.html`
- Create: `/Users/joel/alivio-studio/robots.txt`
- Create: `/Users/joel/alivio-studio/sitemap.xml`
- Create: `/Users/joel/alivio-studio/vercel.json`
- Create: `/Users/joel/alivio-studio/assets/social/build-with-alivio-og.jpg`
- Modify: all public `/Users/joel/alivio-studio/*.html`
- Modify: `/Users/joel/alivio-studio/tests/site-baseline.test.js`

- [ ] **Step 1: Write failing metadata, legal, and header tests**

Require canonical URLs, Open Graph/Twitter metadata, valid social image paths and dimensions, JSON-LD, legal links, robots sitemap declaration, every public URL in the sitemap, and the intended security headers in `vercel.json`.

- [ ] **Step 2: Draft legal pages for attorney review**

Privacy must accurately describe form data, calculator data, Linear, email notifications, Turnstile, hosting, analytics if enabled, retention, contact rights, and US audience. Terms must cover informational ROI scenarios, no guaranteed result, acceptable site use, IP, external services, limitations, and governing-law fields. Do not invent a postal address, legal registration, or governing jurisdiction; keep the production gate blocked until Joel supplies and counsel/business review confirms them.

- [ ] **Step 3: Add complete metadata**

Each page receives a unique title, description, canonical, Open Graph title/description/URL/image, Twitter card, and appropriate JSON-LD. Use `Organization`, `ProfessionalService`, `Service`, `BreadcrumbList`, and `FAQPage` only where the visible page content supports them.

- [ ] **Step 4: Create the social image**

Use the image-generation skill during implementation to create a 1200×630 Alivio-branded image with the core ROI message and safe text margins. Optimize it for web and verify it contains no unsupported metric or client logo.

- [ ] **Step 5: Add crawl files**

`robots.txt` allows public content, disallows `/api/`, and points to `https://buildwithalivio.com/sitemap.xml`. `sitemap.xml` includes only canonical, indexable production pages with valid ISO dates.

- [ ] **Step 6: Add Vercel routing and headers**

Use `cleanUrls: true`, a permanent redirect from `www` at the domain layer, and scoped headers including HSTS, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`, a CSP compatible only with self, Vercel, Turnstile, and the chosen analytics endpoint, and `frame-ancestors 'none'`. Do not enable `unsafe-eval`.

- [ ] **Step 7: Run all automated checks**

```bash
npm test
npm run check:site
```

Expected: PASS.

- [ ] **Step 8: Commit the launch foundation**

```bash
git add privacy.html terms.html robots.txt sitemap.xml vercel.json assets/social *.html tests/site-baseline.test.js
git commit -m "feat: add legal SEO and security foundations"
```

### Task 9: Verify the complete conversion journey in preview

**Files:**
- Modify as failures require: `/Users/joel/alivio-studio/index.html`
- Modify as failures require: `/Users/joel/alivio-studio/hvac.html`
- Modify as failures require: `/Users/joel/alivio-studio/systems-review.html`
- Modify as failures require: `/Users/joel/alivio-studio/assets/style.css`
- Modify as failures require: `/Users/joel/alivio-studio/assets/*.js`
- Record evidence: `/Users/joel/alivio-ops-os/docs/runbooks/build-with-alivio-site-verification.md`

- [ ] **Step 1: Run all local checks from a clean tree**

```bash
npm test
npm run check:site
git status --short
```

Expected: all tests pass; only intentional changes are present before commit.

- [ ] **Step 2: Deploy a Vercel preview with test integrations**

Use Turnstile test keys and `[TEST]` Linear labeling. Do not use production email recipients or create unmarked production pipeline issues.

- [ ] **Step 3: Test primary user stories in Chrome**

Verify at desktop and mobile sizes:

1. Homepage visitor calculates conservative/expected/upside benefit.
2. Calculator values transfer to the Systems Review form.
3. Keyboard-only visitor completes all inputs and Turnstile.
4. Invalid submission gets a focused, useful error summary.
5. Valid submission creates one `[TEST]` Linear issue.
6. Double click/retry does not create a duplicate.
7. Success opens the correct booking page.
8. Booking can be completed in the correct time zone.

- [ ] **Step 4: Test failure paths**

Simulate missing config, rejected Turnstile, Linear timeout, notification failure, JavaScript disabled, and offline submission. The site must not falsely report success. The user’s entered data remains available for retry except where the browser reloads.

- [ ] **Step 5: Run accessibility and performance checks**

Use Chrome Lighthouse plus manual keyboard, focus, contrast, reduced-motion, zoom-to-200%, and screen-reader name checks. Targets on homepage/HVAC/review pages: Accessibility ≥95, SEO ≥95, Best Practices ≥90, no critical layout shift, and no autoplay audio.

- [ ] **Step 6: Review every public claim**

Compare all rendered copy against the approved spec and evidence. Search:

```bash
rg -n '(guarantee|guaranteed|\b[0-9]+%|\$[0-9].*(revenue|saved)|testimonial|cancel anytime|45-minute|555)' --glob='*.html' .
```

Expected: every match is either approved pricing, calculator UI language, or supported copy documented in the verification record.

- [ ] **Step 7: Commit fixes and evidence**

Commit site fixes in `/Users/joel/alivio-studio`, then commit the evidence record separately in `/Users/joel/alivio-ops-os`.

## Completion Criteria

- All pages communicate a consistent ROI-first home-service offer.
- The calculator is transparent, scenario-based, tested, and accessible.
- A valid form submission persists in Linear before success and cannot silently disappear.
- Turnstile, origin checks, payload limits, validation, deduplication, and secure notifications work.
- Every placeholder contact detail, dead form, fake social link, unsupported claim, and legal placeholder is removed or resolved.
- Canonical metadata, sitemap, robots, social cards, structured data, and security headers pass checks.
- The complete preview journey passes desktop, mobile, keyboard, failure-path, accessibility, and performance verification.
