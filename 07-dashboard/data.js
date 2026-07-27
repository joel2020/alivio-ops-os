/* Alivio Studios — dashboard data
 *
 * EDIT THIS FILE. It is the only file you need to touch.
 *
 * It is plain JSON wrapped in one assignment, because a browser opening
 * dashboard.html from your filesystem is not allowed to fetch("data.json") —
 * it blocks that as a cross-origin request. Assigning to a variable and loading
 * it with <script src> sidesteps that entirely and needs no server.
 *
 * Rules: quote every key, use "YYYY-MM-DD" for dates, no trailing commas.
 * If the page shows a parse error, it will tell you the line.
 *
 * Every stage name, weight, and threshold below comes from the written OS.
 * Change them there first — the dashboard reads the definitions, it does not
 * invent them.
 */

window.ALIVIO_DATA = {

  /* When this data was last updated by hand. The page shows its age and turns
     amber past 3 days, because a stale dashboard that renders as current is
     worse than no dashboard. */
  "updated": "2026-07-26",

  /* ── CASH ─────────────────────────────────────────────────────────────
     monthly_operating_cost drives the trigger levels in
     03-finance/cash-flow-review.md. It is currently a PLACEHOLDER — Joel has
     not provided it, so the cash panel says so instead of guessing. Set it and
     the trigger levels start working. */
  "cash": {
    "on_hand": null,
    "tax_set_aside": null,
    "monthly_operating_cost": null,

    /* 13 weeks forward. Rebuild every Monday.
       "in" = money agreed and expected. Never weighted pipeline. */
    "projection": [
      { "week": "2026-07-27", "in": 0, "out": 0 },
      { "week": "2026-08-03", "in": 0, "out": 0 },
      { "week": "2026-08-10", "in": 0, "out": 0 },
      { "week": "2026-08-17", "in": 0, "out": 0 },
      { "week": "2026-08-24", "in": 0, "out": 0 },
      { "week": "2026-08-31", "in": 0, "out": 0 },
      { "week": "2026-09-07", "in": 0, "out": 0 },
      { "week": "2026-09-14", "in": 0, "out": 0 },
      { "week": "2026-09-21", "in": 0, "out": 0 },
      { "week": "2026-09-28", "in": 0, "out": 0 },
      { "week": "2026-10-05", "in": 0, "out": 0 },
      { "week": "2026-10-12", "in": 0, "out": 0 },
      { "week": "2026-10-19", "in": 0, "out": 0 }
    ]
  },

  /* ── INVOICES ─────────────────────────────────────────────────────────
     Everything issued and not yet paid. Chase tier is computed from due_date
     per 03-finance/ar-chase-sequence.md — you do not set it.
     Set "disputed": true to pause the chase sequence (see the SOP). */
  "invoices": [
    {
      "number": "ALI-2026-018",
      "client": "RLTRS",
      "project": "RLTRS — Colombia real estate suite",
      "amount": 10000,
      "issued": "2026-07-01",
      "due_date": "2026-07-08",
      "paid": false,
      "disputed": false,
      "note": "Week 1 milestone — ALI-28. $4,000 paid + $6,000 on signing."
    },
    {
      "number": "ALI-2026-019",
      "client": "RLTRS",
      "project": "RLTRS — Colombia real estate suite",
      "amount": 2000,
      "issued": "2026-07-08",
      "due_date": "2026-07-15",
      "paid": false,
      "disputed": false,
      "note": "Week 2 milestone — ALI-32. Trust layer, monetization, scraper."
    }
  ],

  /* ── PROJECTS ─────────────────────────────────────────────────────────
     stage must be one of: Scoped, Kickoff, Build, QA, Client review,
     Delivered, Closed  (01-delivery/project-lifecycle.md)

     Health is COMPUTED from the rules in that document. You do not set a
     colour. What you set is the facts the rules read:
       stage_since        when it entered its current stage
       next_milestone     name + date
       blocker_since      null, or when the current blocker started
       budget_consumed    0..1
       delivered          0..1
       missed_checkpoints integer
       scope_disputed     true/false  */
  "projects": [
    {
      "client": "RLTRS",
      "name": "RLTRS — Colombia real estate suite",
      "owner": "Joel",
      "value": 29000,
      "started": "2026-06-01",
      "target_delivery": "2026-09-09",
      "stage": "Build",
      "stage_since": "2026-06-15",
      "next_milestone": { "name": "Week 1 acceptance (ALI-28)", "date": "2026-07-08" },
      "blocker_since": null,
      "budget_consumed": 0.55,
      "delivered": 0.5,
      "missed_checkpoints": 1,
      "scope_disputed": false,
      "scope_changes": { "count": 0, "hours": 0, "charged": 0 }
    },
    {
      "client": "itslitneon",
      "name": "itslitneon storefront + ad creative",
      "owner": "Joel",
      "value": 8000,
      "started": "2026-07-01",
      "target_delivery": "2026-08-15",
      "stage": "Build",
      "stage_since": "2026-07-10",
      "next_milestone": { "name": "Checkout restored", "date": "2026-08-01" },
      "blocker_since": "2026-07-24",
      "budget_consumed": 0.4,
      "delivered": 0.6,
      "missed_checkpoints": 0,
      "scope_disputed": false,
      "scope_changes": { "count": 0, "hours": 0, "charged": 0 }
    },
    {
      "client": "Bravo Mechanical",
      "name": "Bravo Mechanical — website + CRM",
      "owner": "Joel",
      "value": 6000,
      "started": "2026-06-20",
      "target_delivery": "2026-08-01",
      "stage": "Client review",
      "stage_since": "2026-07-14",
      "next_milestone": { "name": "Client approves audit fixes", "date": "2026-07-21" },
      "blocker_since": "2026-07-14",
      "budget_consumed": 0.3,
      "delivered": 0.35,
      "missed_checkpoints": 2,
      "scope_disputed": false,
      "scope_changes": { "count": 0, "hours": 0, "charged": 0 }
    }
  ],

  /* ── PIPELINE ─────────────────────────────────────────────────────────
     stage must be one of: New, Qualified, Discovery, Proposal, Verbal
     (02-sales/pipeline-stages.md). Weighted value is computed from the stage
     weight — never set it by hand, and never adjust a weight per deal.

     next_step is REQUIRED. A deal without one is not being worked, and the
     page will flag it. */
  "pipeline": [],

  /* Revenue target for the next 90 days. Drives pipeline coverage
     (02-sales/forecast-method.md). PLACEHOLDER — not set by Joel. */
  "revenue_target_90d": null,

  /* ── THIS WEEK ────────────────────────────────────────────────────────
     Commitments due, from 00-charter/cadence-calendar.md plus anything you
     have promised. "done": true drops it off the list. */
  "commitments": [
    { "what": "Weekly status report — RLTRS", "owner": "Joel", "due": "2026-07-29", "done": false },
    { "what": "Weekly status report — itslitneon", "owner": "Joel", "due": "2026-07-29", "done": false },
    { "what": "Weekly status report — Bravo Mechanical", "owner": "Joel", "due": "2026-07-29", "done": false },
    { "what": "Pipeline review + forecast recorded", "owner": "Joel", "due": "2026-07-31", "done": false },
    { "what": "Invoice chase sweep", "owner": "Joel", "due": "2026-07-28", "done": false }
  ]
};
