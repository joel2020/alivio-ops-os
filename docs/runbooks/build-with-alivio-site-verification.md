# Build With Alivio — Preview Verification and Launch Gates

**Verification date:** 2026-08-06/07 EDT  
**Status:** Protected preview verified; production launch is intentionally blocked  
**Preview:** https://buildwithalivio-preview.vercel.app  
**Vercel deployment:** `dpl_ELMDL199ng3TLrWEKsBASiAex6ni`  
**Site branch:** `codex/buildwithalivio-conversion`

## Verified build

- Final privacy commits: `d804101` (prevent no-script form data leakage) and `555aa76` (make the no-script email action visibly interactive).
- Automated suite: 100/100 tests passing.
- Static site audit: passed.
- Diff check: passed; site worktree clean.
- Independent review: passed after one accessibility finding was fixed and re-reviewed.
- Linear request timeout: an intentionally hung request aborted with `TimeoutError` in 22 ms against a 20 ms test limit.

## Lighthouse evidence

| Page | Performance | Accessibility | Best practices | SEO | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|---:|---:|
| Home | 95 | 100 | 100 | 100 | 2.4 s | 0 | 150 ms |
| HVAC | 100 | 100 | 100 | 100 | 1.5 s | 0 | 0 ms |
| Systems Review | 98 | 100 | 100 | 100 | 2.2 s | 0 | 0 ms |

The HVAC run initially found low CTA-link contrast. Commit `59e424b` changed the link color; the rerun scored 100 for accessibility and all other categories.

## Manual conversion checks

- ROI calculator sample inputs produced conservative `$4,782/month` and `2.5 months`, expected `$7,504` and `1.6 months`, and upside `$9,205` and `1.3 months`.
- The calculator CTA copied all values into the review form and focused the qualification heading.
- Blank submission focused a useful summary and identified 13 invalid fields without contacting `/api/leads`.
- A recoverable submission failure retained the prospect's values, focused the error, reset Turnstile, and did not redirect.
- Offline and missing-configuration paths produced clear messages and no false success.
- A failing Turnstile token returned 400 locally.
- Without JavaScript, the form stays hidden to prevent browser GET/query-string leakage and exposes a visibly interactive `hello@buildwithalivio.com` email fallback.

## Protected preview checks

- Preview alias resolves to deployment `dpl_ELMDL199ng3TLrWEKsBASiAex6ni`, status Ready.
- `/api/config` returned 200 with only the preview booking URL and public Cloudflare test site key.
- Homepage returned 200 with strict CSP, HSTS, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, Referrer Policy, and Permissions Policy.
- Origin mismatch returned 403; wrong content type returned 400; a request over 32 KB returned 413.
- A structurally valid synthetic submission passed the official dummy Turnstile check, reached the intentionally invalid Linear credential, and returned 503 `service_unavailable`. It did not report success or create a lead.
- Preview-only Turnstile behavior requires all three conditions: preview integration mode, the explicit test flag, and Cloudflare's official always-pass dummy secret. Production ignores the test flag.
- Cloudflare testing reference: https://developers.cloudflare.com/turnstile/troubleshooting/testing/

## Claims and case-study audit

The homepage presents industry evidence as third-party, vendor-reported examples—not Alivio client results—and states the limitations beside each claim.

- Peaden/Hatch: https://www.usehatchapp.com/case-studies/peaden-voice
- Preferred Home Services/Rilla: https://www.rilla.com/customer-stories/prefered-home-services
- Air Design/Podium: https://homeservices.podium.com/resources/case-study/air-design-ai-membership-coordinator
- Harley's/ServiceTitan research source: https://www.servicetitan.com/blog/success-story-max-harleys-heating-air

The calculator labels outputs as scenarios rather than forecasts, uses prospect-controlled inputs, and does not present revenue as profit. A targeted claim scan found only qualified vendor-reported metrics and explicit no-guarantee language.

## Production launch gates

Do not promote this deployment or connect the public domain until every gate below is complete:

1. Create a least-privilege Linear personal API key, store it only as a Vercel production secret, and run exactly one `[TEST]` issue plus an identical replay to prove deduplication.
2. Confirm the real 30-minute booking URL, timezone, availability, intake behavior, and cancellation/rescheduling rules.
3. Purchase or confirm control of `buildwithalivio.com`; connect apex and `www` to Vercel, set apex as canonical, verify SSL, and keep `aliviosearch.cloud` separate.
4. Provision `hello@buildwithalivio.com` and required aliases; publish SPF, DKIM, and DMARC; verify sending and replies before an email campaign.
5. Create a production Cloudflare Turnstile widget for `buildwithalivio.com` and `www.buildwithalivio.com`; replace all dummy keys and set `TURNSTILE_TEST_MODE=false`.
6. Approve the legal entity name, postal/contact details, governing law/jurisdiction, privacy retention details, processors, and final Terms/Privacy text. Remove draft/noindex treatment only after review.
7. Configure production-only Vercel variables, lead notification recipient, privacy-conscious analytics, uptime checks, and alert ownership.
8. Capture the current production deployment ID before promotion. Roll back by reassigning the production domains to that prior known-good deployment if smoke tests fail.
9. After promotion, run desktop/mobile smoke tests, submit one real production test lead, verify its Linear issue, notification, booking redirect, canonical URLs, robots, sitemap, and analytics events, then delete or close the test lead.
10. Build the organic launch assets: HVAC pillar/supporting pages, Google Business Profile plan, call script, email sequence, lead list workflow, editorial calendar, and weekly KPI scorecard. Paid ads remain out of scope.

## Launch decision

The site is **preview-ready, not production-ready**. The remaining gates require owner credentials, domain/email configuration, real booking details, and legal approval; none should be inferred or replaced with placeholders.
