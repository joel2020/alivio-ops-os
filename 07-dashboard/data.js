/* Alivio Studios — dashboard data
 *
 * MONEY IS GENERATED. invoices + cash come from the ledger:
 *     08-automation/lib/ledger.py
 * Regenerate with:
 *     python3 08-automation/lib/sync_dashboard.py
 * Editing those sections by hand will be overwritten, and would be wrong
 * anyway — the books are the source of truth for money.
 *
 * EVERYTHING ELSE IS YOURS. projects, pipeline, and commitments are hand-
 * maintained and preserved across regeneration. Nothing here knows them.
 *
 * Generated 2026-07-26
 */

window.ALIVIO_DATA = {
  "updated": "2026-07-26",
  "cash": {
    "on_hand": null,
    "tax_set_aside": null,
    "monthly_operating_cost": null,
    "projection": []
  },
  "invoices": [
    {
      "number": "ALI-2026-018",
      "client": "RLTRS",
      "project": "RLTRS — Colombia real estate suite",
      "amount": 10000.0,
      "issued": "2026-07-01",
      "due_date": "2026-07-08",
      "paid": false,
      "disputed": false,
      "note": "Week 1 milestone ALI-28"
    },
    {
      "number": "ALI-2026-019",
      "client": "RLTRS",
      "project": "RLTRS — Colombia real estate suite",
      "amount": 2000.0,
      "issued": "2026-07-08",
      "due_date": "2026-07-15",
      "paid": false,
      "disputed": false,
      "note": "Week 2 milestone ALI-32"
    }
  ],
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
      "next_milestone": {
        "name": "Week 1 acceptance (ALI-28)",
        "date": "2026-07-08"
      },
      "blocker_since": null,
      "budget_consumed": 0.55,
      "delivered": 0.5,
      "missed_checkpoints": 1,
      "scope_disputed": false,
      "scope_changes": {
        "count": 0,
        "hours": 0,
        "charged": 0
      }
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
      "next_milestone": {
        "name": "Checkout restored",
        "date": "2026-08-01"
      },
      "blocker_since": "2026-07-24",
      "budget_consumed": 0.4,
      "delivered": 0.6,
      "missed_checkpoints": 0,
      "scope_disputed": false,
      "scope_changes": {
        "count": 0,
        "hours": 0,
        "charged": 0
      }
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
      "next_milestone": {
        "name": "Client approves audit fixes",
        "date": "2026-07-21"
      },
      "blocker_since": "2026-07-14",
      "budget_consumed": 0.3,
      "delivered": 0.35,
      "missed_checkpoints": 2,
      "scope_disputed": false,
      "scope_changes": {
        "count": 0,
        "hours": 0,
        "charged": 0
      }
    }
  ],
  "pipeline": [],
  "revenue_target_90d": null,
  "commitments": [
    {
      "what": "Weekly status report — RLTRS",
      "owner": "Joel",
      "due": "2026-07-29",
      "done": false
    },
    {
      "what": "Weekly status report — itslitneon",
      "owner": "Joel",
      "due": "2026-07-29",
      "done": false
    },
    {
      "what": "Weekly status report — Bravo Mechanical",
      "owner": "Joel",
      "due": "2026-07-29",
      "done": false
    },
    {
      "what": "Pipeline review + forecast recorded",
      "owner": "Joel",
      "due": "2026-07-31",
      "done": false
    },
    {
      "what": "Invoice chase sweep",
      "owner": "Joel",
      "due": "2026-07-28",
      "done": false
    }
  ]
};
