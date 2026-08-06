# Build With Alivio Infrastructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Put `buildwithalivio.com` on the existing Alivio Studio Vercel project, establish trustworthy domain email, and create the external accounts and configuration required by the conversion funnel without interrupting `aliviosearch.cloud`.

**Architecture:** Hostinger remains the registrar, DNS host, and mail provider. Vercel continues to host the static website. The apex domain is canonical, `www` redirects to the apex, mail records stay independent from web records, and Linear is the durable lead system. Secrets live only in Vercel environment variables or the owning provider, never in Git.

**Tech Stack:** Hostinger Domains/DNS/Email, Vercel project `alivio-studio`, Linear GraphQL API, Gmail-compatible mail client, Google Calendar appointment schedules or equivalent booking page, DNS verification tools.

## Global Constraints

- Execute this plan before the conversion-site plan's production deployment.
- Do not change, forward, cancel, or let lapse `aliviosearch.cloud`; it remains intact until a later explicit retirement decision.
- Do not purchase a domain until the checkout page shows the exact registration term, taxes, ICANN fees, renewal price, and total, and Joel confirms that exact total.
- Do not create multiple consumer Gmail accounts. Use domain mailboxes and aliases under `buildwithalivio.com`.
- Preserve Hostinger MX records when changing web DNS records.
- Never commit API keys, verification tokens, DNS secrets, mailbox passwords, or client information.
- Do not start email campaigns until SPF, DKIM, DMARC, TLS, a monitored reply address, a physical postal address, and an unsubscribe process all pass verification.
- Make every DNS change recoverable: capture the current zone before edits and record the exact old and new values in the runbook.
- Use production and preview Vercel environment scopes deliberately; do not expose server-only variables to browser JavaScript.
- The source design is `docs/superpowers/specs/2026-08-06-build-with-alivio-launch-design.md`.

---

### Task 1: Create the infrastructure runbook and evidence log

**Files:**
- Create: `docs/runbooks/build-with-alivio-infrastructure.md`
- Reference: `docs/superpowers/specs/2026-08-06-build-with-alivio-launch-design.md`

- [ ] **Step 1: Add the runbook skeleton**

Create sections for ownership, account identifiers, pre-change DNS snapshot, purchase evidence, DNS records, mail records, Vercel domains, booking link, Linear configuration, environment variables, verification evidence, rollback, and final sign-off.

Record only non-secret identifiers. Represent every secret by its provider location, such as “Vercel production environment,” not by its value.

- [ ] **Step 2: Record the known baseline**

Include:

```text
Registrar/DNS/mail: Hostinger
Target domain: buildwithalivio.com
Existing domain to preserve: aliviosearch.cloud
Vercel project: alivio-studio
Vercel project ID: prj_ccWNwP7bm9Ici4zlgYg5jwhiGw5i
Canonical URL: https://buildwithalivio.com
Redirect URL: https://www.buildwithalivio.com -> https://buildwithalivio.com
Primary mailbox: joel@buildwithalivio.com
Inbound alias: hello@buildwithalivio.com
Campaign sender: updates@buildwithalivio.com
```

- [ ] **Step 3: Add pass/fail evidence fields**

For every verification, require timestamp, tool/provider page, observed result, pass/fail, and remediation. Screenshots must exclude passwords, recovery codes, tokens, and billing information.

- [ ] **Step 4: Review the runbook for secret leakage**

Run:

```bash
rg -n '(api[_-]?key|password|secret|token).*[=:].+|BEGIN [A-Z ]*PRIVATE KEY' docs/runbooks/build-with-alivio-infrastructure.md
```

Expected: no secret values; only descriptions of where secrets are stored.

- [ ] **Step 5: Commit the runbook baseline**

```bash
git add docs/runbooks/build-with-alivio-infrastructure.md
git commit -m "docs: add Build With Alivio infrastructure runbook"
```

### Task 2: Confirm and purchase `buildwithalivio.com`

**External systems:**
- Hostinger domain search and checkout
- Hostinger account ownership and billing profile

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`

- [ ] **Step 1: Recheck exact domain availability**

In the signed-in Hostinger account, search for the exact ASCII domain `buildwithalivio.com`. Confirm the spelling in the cart and confirm that it is a new registration, not a brokered or premium transfer.

Expected: Hostinger reports the exact domain available for direct registration.

- [ ] **Step 2: Inspect the complete checkout terms**

Record the selected registration term, first-term subtotal, taxes/fees, total charged today, renewal date, and renewal price. Do not rely on the search-result promotional price because the observed `$0.01` offer was conditional on a three-or-more-year term.

- [ ] **Step 3: Obtain transaction confirmation**

Show Joel the exact item, purpose, term, amount charged today, and renewal price. Continue only after he confirms that exact transaction.

- [ ] **Step 4: Complete the purchase and security setup**

Purchase only `buildwithalivio.com`. Enable registrar lock, auto-renew, contact privacy where offered, and two-factor authentication on the Hostinger account. Store recovery material in Joel’s password manager, not in the runbook.

- [ ] **Step 5: Verify ownership and record evidence**

Confirm the Hostinger domain dashboard shows the correct registration and expiration dates. Add the non-sensitive dates and transaction reference to the runbook.

- [ ] **Step 6: Commit the evidence update**

```bash
git add docs/runbooks/build-with-alivio-infrastructure.md
git commit -m "docs: record Build With Alivio domain registration"
```

### Task 3: Stage the domain in Vercel without exposing the unfinished site

**External systems:**
- Vercel project `alivio-studio`
- Hostinger DNS zone for `buildwithalivio.com`

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`

- [ ] **Step 1: Capture the untouched DNS zone**

Before editing, record every DNS record by type, name, value, TTL, and provider purpose. Explicitly identify MX, SPF, DKIM, and DMARC records as protected mail records.

- [ ] **Step 2: Add both domains in Vercel**

Attach `buildwithalivio.com` and `www.buildwithalivio.com` to project `alivio-studio`. Configure the intended apex canonical and `www` redirect in Vercel, but do not change the Hostinger apex or `www` web records yet. The unfinished site must not become public under the new domain before the production launch gate.

- [ ] **Step 3: Verify ownership without cutting over web traffic**

If Vercel requests ownership verification, add only its exact TXT verification record at Hostinger and wait for Vercel to confirm ownership. Preserve all mail records. Do not add the apex A/ALIAS or `www` CNAME web targets during this infrastructure phase.

- [ ] **Step 4: Record the exact cutover records**

Run `vercel domains inspect` for the apex and `www`. Record the exact current web targets Vercel displays; project-specific targets take precedence over general-purpose examples.

The expected shape is:

```text
@     A or ALIAS   value shown by Vercel at cutover
www   CNAME        value shown by Vercel at cutover
```

- [ ] **Step 5: Verify mail DNS remains intact**

Run:

```bash
dig +short buildwithalivio.com MX
dig +short buildwithalivio.com TXT
```

Expected: Hostinger mail MX records remain present; any Vercel ownership TXT is visible. It is acceptable and intended that the web records do not yet point to Vercel.

- [ ] **Step 6: Add the production cutover procedure**

Record the precise Hostinger steps that the production-launch plan will use to apply the staged apex and `www` records. The launch procedure will then verify:

```bash
curl -sSIL https://buildwithalivio.com | sed -n '1,20p'
curl -sSIL https://www.buildwithalivio.com | sed -n '1,30p'
```

Required launch result: the apex returns a valid HTTPS response; `www` redirects once to `https://buildwithalivio.com/`; there is no certificate warning or redirect loop.

- [ ] **Step 7: Record rollback values**

Document the old web records and the precise Hostinger steps that restore them. Do not include protected credentials.

- [ ] **Step 8: Commit staged domain evidence**

```bash
git add docs/runbooks/build-with-alivio-infrastructure.md
git commit -m "docs: stage Build With Alivio domain routing"
```

### Task 4: Create the domain email architecture

**External systems:**
- Hostinger Email for `buildwithalivio.com`
- Joel’s selected Gmail-compatible client

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`

- [ ] **Step 1: Create one primary mailbox**

Create `joel@buildwithalivio.com` as the authenticated primary mailbox. Use a unique password and two-factor authentication where Hostinger supports it.

- [ ] **Step 2: Create role addresses**

Configure `hello@buildwithalivio.com` to deliver to Joel’s monitored inbox. Configure `updates@buildwithalivio.com` as the campaign From address, with replies delivered to the monitored inbox. Prefer aliases if Hostinger’s plan supports authenticated sending correctly; create separate mailboxes only when necessary for provider authentication.

- [ ] **Step 3: Connect the mail client**

Add the domain mailbox to the selected Gmail-compatible interface using Hostinger’s current IMAP/SMTP settings. Send test messages in both directions with a non-Alivio address and verify that replies use the intended domain From address.

- [ ] **Step 4: Define visible sender identities**

Use these identities consistently:

```text
Joel Carias — Alivio Studio <joel@buildwithalivio.com>
Alivio Studio <hello@buildwithalivio.com>
Build With Alivio Updates <updates@buildwithalivio.com>
```

Do not present Build With Alivio as a separate legal entity; it is the domain and campaign identity for Alivio Studio.

- [ ] **Step 5: Verify mailbox operations**

Pass: inbound mail arrives, outbound mail arrives, replies thread correctly, From alignment is correct, and no message exposes a Hostinger or consumer Gmail address as the visible sender.

### Task 5: Authenticate email and establish campaign compliance gates

**External systems:**
- Hostinger DNS and Email
- Google Admin Toolbox CheckMX or equivalent independent DNS checker
- Campaign sending provider selected during execution

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`
- Create: `02-sales/campaigns/build-with-alivio/sending-readiness.md`

- [ ] **Step 1: Publish and verify SPF**

Use one SPF TXT record for the apex and include only Hostinger plus the selected campaign sender. Merge mechanisms into the existing SPF record; never publish multiple apex SPF records.

- [ ] **Step 2: Publish and verify DKIM**

Enable Hostinger DKIM and the campaign sender’s DKIM. Add the exact selectors each provider supplies. Verify a test message’s authentication results show DKIM pass and domain alignment.

- [ ] **Step 3: Publish DMARC in monitoring mode**

Start with a single DMARC record using `p=none`, aggregate reporting to a monitored address, and alignment settings compatible with both senders. Move to quarantine/reject only after at least two weeks of clean aligned traffic and an explicit review.

- [ ] **Step 4: Authenticate a separate transactional subdomain**

In Resend, verify `notify.buildwithalivio.com` for website lead notifications using the exact SPF/MX return-path and DKIM records Resend supplies. Send notifications from `Alivio Website <notifications@notify.buildwithalivio.com>` with `Reply-To: hello@buildwithalivio.com`. Keep campaign sending on the primary domain addresses so transactional reputation and campaign reputation are isolated.

- [ ] **Step 5: Verify TLS and message authentication**

Send test mail to Gmail and another major provider. Capture only the non-sensitive authentication result:

```text
SPF: PASS and aligned
DKIM: PASS and aligned
DMARC: PASS
Transport: TLS
```

- [ ] **Step 6: Add the legal sending prerequisites**

In `sending-readiness.md`, require all of the following before the first campaign:

- Alivio Studio’s valid physical postal address in every commercial email.
- Accurate From, Reply-To, and subject lines.
- Clear commercial identity and a working unsubscribe mechanism.
- A suppression list checked before every send.
- Opt-outs honored across every sender within 10 business days, with an internal target of one business day.
- No purchased lists, deceptive personalization, or prerecorded/AI-generated cold-call voice.
- Manual review of state-specific calling and email rules for the chosen prospect geography.

- [ ] **Step 7: Add a launch-blocking checklist**

The document must explicitly output `READY` only if every identity, authentication, address, opt-out, suppression, and reply-monitoring field is complete. Otherwise it outputs `BLOCKED` with the failed requirement.

- [ ] **Step 8: Commit the email readiness controls**

```bash
git add docs/runbooks/build-with-alivio-infrastructure.md 02-sales/campaigns/build-with-alivio/sending-readiness.md
git commit -m "docs: add Build With Alivio email readiness controls"
```

### Task 6: Create the booking experience

**External systems:**
- Google Calendar appointment schedules or the selected booking provider

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`

- [ ] **Step 1: Create the event type**

Create “Home Service ROI Systems Review” with a 30-minute duration, US-friendly availability, a 15-minute buffer, a minimum notice period of 24 hours, and a reasonable daily cap. Do not call it a 45-minute consultation.

- [ ] **Step 2: Add qualification questions**

Collect business name, website, home-service trade, service area, approximate monthly lead volume, current CRM/phone/scheduling tools, biggest revenue leak, decision-maker attendance, implementation timing, and investment range.

- [ ] **Step 3: Add truthful confirmation copy**

Promise a focused review of lead handling, booking, follow-up, and operating bottlenecks. Do not promise a guaranteed revenue result. State that the call may conclude with no-fit guidance, the `$3,000` fixed Systems Roadmap, or a later implementation conversation.

- [ ] **Step 4: Configure notifications and time zones**

Verify invite creation, Joel notification, prospect confirmation, reminder timing, rescheduling, cancellation, and correct display in Eastern Time plus the prospect’s local time.

- [ ] **Step 5: Test the complete booking journey**

Book, reschedule, and cancel a test appointment from a non-Alivio email address. Pass only if both parties receive accurate calendar events and the questions appear in the event record.

- [ ] **Step 6: Record the production booking URL**

Store the public URL in the runbook and later in Vercel as `BOOKING_URL`. Do not hard-code it into multiple HTML files.

### Task 7: Prepare Linear as the durable lead system

**External systems:**
- Linear workspace

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`
- Modify: `02-sales/crm-hygiene.md`
- Modify: `02-sales/pipeline-stages.md`

- [ ] **Step 1: Create or verify the sales project**

Use a dedicated Linear project for Alivio pipeline items. One qualified or inbound submission becomes one issue. Record the non-secret team, project, and label identifiers in the runbook.

- [ ] **Step 2: Define labels and deduplication**

Create labels for `source: website`, `source: organic`, `source: cold call`, `source: email`, `trade: hvac`, `offer: roi review`, and `status: needs review`. The website integration uses normalized email plus business domain to find a recent open issue before creating a duplicate.

- [ ] **Step 3: Define the issue contract**

Require:

```text
Title: <Business> — Home Service ROI Review
Description: contact, trade, service area, lead volume, tools, problem, authority,
timeline, investment range, source/UTM, consent timestamp, and submission ID
Initial stage: Lead
Owner: Joel
Review SLA: one business day
```

- [ ] **Step 4: Align the operating-system docs**

Update `crm-hygiene.md` and `pipeline-stages.md` to state how website submissions enter Linear, when duplicates are merged, and when unqualified submissions are closed. Preserve the existing buyer-action stage philosophy.

- [ ] **Step 5: Create a scoped API credential**

Create the minimum-access Linear credential supported for the workspace and store it in the password manager and later Vercel. Do not paste it in chat, docs, shell history, or Git.

- [ ] **Step 6: Commit the pipeline integration contract**

```bash
git add docs/runbooks/build-with-alivio-infrastructure.md 02-sales/crm-hygiene.md 02-sales/pipeline-stages.md
git commit -m "docs: define website lead intake in Linear"
```

### Task 8: Populate Vercel environment variables and close the infrastructure gate

**External systems:**
- Vercel project `alivio-studio`

**Files:**
- Modify: `docs/runbooks/build-with-alivio-infrastructure.md`

- [ ] **Step 1: Create the Turnstile widget**

Create a managed Cloudflare Turnstile widget for `buildwithalivio.com` with action `systems_review`. Add only the production hostname and use Cloudflare’s published test keys for preview automation. Store the production secret only in Vercel; record the non-secret widget name and owner in the runbook.

- [ ] **Step 2: Add server-only production variables**

After the conversion-site implementation defines its exact environment contract, add these values to Production and only to Preview where a safe test value exists:

```text
LINEAR_API_KEY
LINEAR_TEAM_ID
LINEAR_PROJECT_ID
LINEAR_WEBSITE_LABEL_ID
RESEND_API_KEY
LEAD_NOTIFY_TO
BOOKING_URL
TURNSTILE_SECRET_KEY
TURNSTILE_SITE_KEY
ALLOWED_ORIGINS
```

`TURNSTILE_SITE_KEY` is public but still managed centrally. All other key/secret values remain server-only.

- [ ] **Step 3: Keep preview isolated**

Preview submissions must use Cloudflare Turnstile test keys and a separate Linear test label or disabled integration mode. A preview must never create an apparently real sales opportunity without a visible `[TEST]` marker.

- [ ] **Step 4: Configure the Vercel Firewall rule**

Create and preview a rate-limit rule scoped to `POST /api/leads`, keyed by client IP, allowing five requests per ten minutes and blocking additional requests for ten minutes. Verify the rule against the current Vercel plan and current Firewall UI/API before activating it. Exclude Vercel health checks and do not rate-limit static pages or `/api/config`.

- [ ] **Step 5: Run the infrastructure verification matrix**

Pass all of these:

```text
[ ] Domain registration and security confirmed
[ ] Apex and www are added to the Vercel project
[ ] Exact Vercel cutover and rollback records are documented
[ ] Public web DNS has not been cut over before release approval
[ ] MX records preserved
[ ] Primary mailbox plus aliases work in both directions
[ ] SPF passes and aligns
[ ] DKIM passes and aligns
[ ] DMARC passes
[ ] Booking create/reschedule/cancel passes
[ ] Linear project, labels, SLA, and credential exist
[ ] Vercel production variables exist at correct scope
[ ] Turnstile production hostname/action and preview test mode are configured
[ ] Vercel Firewall rate limit for POST /api/leads passes preview verification
[ ] No secret is present in Git or the runbook
[ ] aliviosearch.cloud remains unchanged
```

- [ ] **Step 6: Mark the infrastructure gate**

Record `PASS` only when every item is verified. A pending DNS certificate, failing mail authentication, missing postal address, or incomplete opt-out path keeps the gate `BLOCKED`.

- [ ] **Step 7: Commit final evidence**

```bash
git add docs/runbooks/build-with-alivio-infrastructure.md
git commit -m "docs: close Build With Alivio infrastructure gate"
```

## Completion Criteria

- `buildwithalivio.com` is owned by Alivio, secured, and staged on the Vercel project without exposing the unfinished site.
- The exact apex/`www` cutover and rollback records are documented, and existing mail DNS is intact.
- Domain mail sends and receives with SPF, DKIM, and DMARC passing.
- The 30-minute booking flow works end to end.
- Linear and Vercel are ready for the site’s lead endpoint.
- The campaign readiness gate remains blocked until the physical postal address and every compliance control are complete.
- `aliviosearch.cloud` is untouched.

## Implementation References

- [Vercel: Setting up a custom domain](https://vercel.com/docs/domains/set-up-custom-domain)
- [Vercel: Add rate limiting with Vercel](https://vercel.com/kb/guide/add-rate-limiting-vercel)
- [Cloudflare: Validate Turnstile tokens server-side](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)
- [Resend: Managing and verifying sending domains](https://resend.com/docs/dashboard/domains/introduction)
- [Google: Email sender guidelines](https://support.google.com/mail/answer/81126)
- [FTC: CAN-SPAM compliance guide for business](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
