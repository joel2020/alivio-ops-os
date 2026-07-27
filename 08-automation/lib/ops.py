"""The six scheduled tasks, computed.

Each returns structured data with its sources named. The skills and slash
commands render it; nothing here writes prose, and nothing here sends anything.

Four rules from the Phase 3 brief, enforced structurally rather than by
instruction:

  1. Nothing sends externally. There is no send path in this module.
  2. No money moves. Ever. There is no payment path either.
  3. Every output cites where its numbers came from — the `sources` key.
  4. Each task degrades when a source is down: it says what is missing and
     delivers the rest, rather than failing whole or, worse, reporting a
     confident zero.

Rule 4 is the one that matters most in practice. A Monday brief that silently
omits cash because the books could not be read is worse than no brief, because
it looks complete.
"""

import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger  # noqa: E402
from sync_dashboard import read_existing  # noqa: E402

AUTOMATION = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OS_ROOT = os.path.dirname(AUTOMATION)

# 01-delivery/project-lifecycle.md
STAGE_DWELL = {"Scoped": 5, "Kickoff": 5, "QA": 3, "Client review": 7,
               "Delivered": 10}
BUILD_FRACTION = 0.60
RED = {"milestone_slip_days": 5, "blocker_days": 7, "missed_checkpoints": 2,
       "invoice_overdue_days": 30}
AMBER = {"blocker_min": 2, "blocker_max": 5, "milestone_within": 3,
         "budget_consumed": 0.80, "delivered_below": 0.60,
         "missed_checkpoints": 1}

# 02-sales/pipeline-stages.md
PIPELINE_WEIGHTS = {"New": .05, "Qualified": .15, "Discovery": .30,
                    "Proposal": .50, "Verbal": .80}
PIPELINE_DWELL = {"New": 5, "Qualified": 10, "Discovery": 10,
                  "Proposal": 15, "Verbal": 15}
UNTOUCHED_DAYS = 5                       # 02-sales/crm-hygiene.md
COVERAGE_TARGET, COVERAGE_ALARM = 3, 2   # 02-sales/forecast-method.md


def _today(t=None):
    return t or datetime.date.today()


def _d(s):
    return datetime.date.fromisoformat(str(s)[:10]) if s else None


def _since(s, today=None):
    return (_today(today) - _d(s)).days if s else None


def _until(s, today=None):
    return (_d(s) - _today(today)).days if s else None


def load_board():
    """Projects, pipeline, commitments. Reports failure rather than empty."""
    try:
        d = read_existing()
    except SystemExit as e:
        return {"available": False, "reason": str(e), "projects": [],
                "pipeline": [], "commitments": []}
    if not d:
        return {"available": False,
                "reason": "07-dashboard/data.js not found or unreadable",
                "projects": [], "pipeline": [], "commitments": []}
    return {"available": True, "reason": None,
            "projects": d.get("projects", []), "pipeline": d.get("pipeline", []),
            "commitments": d.get("commitments", []),
            "revenue_target_90d": d.get("revenue_target_90d"),
            "monthly_operating_cost": (d.get("cash") or {}).get("monthly_operating_cost")}


# ── project health (must agree with the dashboard; a test enforces it) ────

def stage_limit(p):
    if p.get("stage") in STAGE_DWELL:
        return STAGE_DWELL[p["stage"]]
    if p.get("stage") == "Build" and p.get("started") and p.get("target_delivery"):
        total = (_d(p["target_delivery"]) - _d(p["started"])).days
        if total > 0:
            return round(total * BUILD_FRACTION)
    return None


def project_health(p, today=None, overdue_projects=()):
    red, amber = [], []
    in_stage = _since(p.get("stage_since"), today)
    blocked = _since(p.get("blocker_since"), today)
    to_ms = _until((p.get("next_milestone") or {}).get("date"), today)

    if to_ms is not None and to_ms < -RED["milestone_slip_days"]:
        red.append(f"milestone slipped {-to_ms}d")
    if blocked is not None and blocked > RED["blocker_days"]:
        red.append(f"blocked {blocked}d")
    if (p.get("missed_checkpoints") or 0) >= RED["missed_checkpoints"]:
        red.append(f"{p['missed_checkpoints']} missed checkpoints")
    if p.get("scope_disputed"):
        red.append("scope disputed")
    if p.get("name") in overdue_projects:
        red.append("invoice >30d overdue")

    lim = stage_limit(p)
    if lim is not None and in_stage is not None and in_stage > lim:
        amber.append(f"{in_stage}d in {p['stage']} (limit {lim})")
    if to_ms is not None and 0 <= to_ms <= AMBER["milestone_within"]:
        amber.append(f"milestone in {to_ms}d")
    if blocked is not None and AMBER["blocker_min"] <= blocked <= AMBER["blocker_max"]:
        amber.append(f"blocked {blocked}d")
    bc, dv = p.get("budget_consumed"), p.get("delivered")
    if isinstance(bc, (int, float)) and isinstance(dv, (int, float)) \
            and bc > AMBER["budget_consumed"] and dv < AMBER["delivered_below"]:
        amber.append(f"{round(bc*100)}% budget, {round(dv*100)}% delivered")
    if (p.get("missed_checkpoints") or 0) == AMBER["missed_checkpoints"]:
        amber.append("1 missed checkpoint")

    if red:
        return {"level": "red", "reasons": red}
    if amber:
        return {"level": "amber", "reasons": amber}
    return {"level": "green", "reasons": []}


def _overdue_project_names(today=None):
    return {i.get("project") for i in ledger.chase_list(today)
            if i["chase"]["overdue_days"] > RED["invoice_overdue_days"]
            and i.get("project")}


def orphaned_invoices(today=None):
    """Invoices whose `project` matches no project on the board.

    Invoices link to projects by exact string match, so a typo in either place
    silently detaches money from the project it belongs to — the invoice stops
    contributing to that project's health, and the >30-day RED trigger never
    fires for it. Nothing else would ever notice, which is why this is checked
    rather than assumed.
    """
    board = load_board()
    if not board["available"]:
        return {"available": False, "reason": board["reason"], "orphans": []}
    names = {p.get("name") for p in board["projects"]}
    orphans = []
    for i in ledger.invoices():
        proj = i.get("project")
        if proj and proj not in names:
            orphans.append({"number": i["number"], "project": proj,
                            "outstanding": i["outstanding"],
                            "fix": "make the invoice's project match a name in "
                                   "07-dashboard/data.js exactly, or correct the "
                                   "project name there"})
    return {"available": True, "reason": None, "orphans": orphans}


def projects_with_health(today=None):
    board = load_board()
    od = _overdue_project_names(today)
    out = []
    for p in board["projects"]:
        if p.get("stage") == "Closed":
            continue
        out.append({**p, "health": project_health(p, today, od),
                    "in_stage": _since(p.get("stage_since"), today),
                    "limit": stage_limit(p)})
    return board, out


# ── the six tasks ────────────────────────────────────────────────────────

def invoice_chase_sweep(today=None):
    """Tue + Fri. Overdue list at the right tier. Drafts are in drafts.py."""
    today = _today(today)
    rows = ledger.chase_list(today)
    aging = ledger.ar_aging(today)
    return {
        "task": "invoice-chase-sweep", "as_of": today.isoformat(),
        "available": True,
        "sources": ["08-automation/books/invoices.jsonl",
                    "03-finance/ar-chase-sequence.md"],
        "to_chase": [{
            "number": r["number"], "client": r.get("client"),
            "project": r.get("project"), "outstanding": r["outstanding"],
            "due": r["due"], "overdue_days": r["chase"]["overdue_days"],
            "tier": r["chase"]["tier"], "owner": r["chase"]["who"],
            "action": r["chase"]["label"], "late_fee": r["late_fee"],
            "disputed": r.get("disputed", False),
        } for r in rows],
        "total_overdue": round(sum(r["outstanding"] for r in rows), 2),
        "aging": aging,
        "escalations": [r["number"] for r in rows if r["chase"]["tier"] >= 4],
        "orphaned_invoices": orphaned_invoices(today),
        "reminder": "Drafts only. Joel reviews and sends. Nothing goes out from here.",
    }


def project_status_rollup(today=None):
    """Wednesday. Stage, blockers, anything aging."""
    today = _today(today)
    board, projs = projects_with_health(today)
    return {
        "task": "project-status-rollup", "as_of": today.isoformat(),
        "available": board["available"],
        "reason": board["reason"],
        "sources": ["07-dashboard/data.js", "01-delivery/project-lifecycle.md"],
        "projects": [{
            "client": p.get("client"), "name": p.get("name"),
            "owner": p.get("owner"), "stage": p.get("stage"),
            "in_stage": p["in_stage"], "limit": p["limit"],
            "aging": bool(p["limit"] and p["in_stage"] and p["in_stage"] > p["limit"]),
            "health": p["health"]["level"], "why": p["health"]["reasons"],
            "next_milestone": p.get("next_milestone"),
        } for p in projs],
        "red": [p["name"] for p in projs if p["health"]["level"] == "red"],
        "amber": [p["name"] for p in projs if p["health"]["level"] == "amber"],
        "status_reports_due": [p.get("client") for p in projs],
    }


def pipeline_hygiene(today=None):
    """Friday. Stale deals, missing fields, deals with no next step."""
    today = _today(today)
    board = load_board()
    deals = board["pipeline"]
    issues, weighted = [], 0.0
    for x in deals:
        w = PIPELINE_WEIGHTS.get(x.get("stage"), 0)
        weighted += (x.get("value") or 0) * w
        if not x.get("next_step"):
            issues.append({"company": x.get("company"), "problem": "no next step",
                           "fix": "add one with a date, or mark Lost"})
        in_stage = _since(x.get("stage_since"), today)
        lim = PIPELINE_DWELL.get(x.get("stage"))
        if in_stage is not None and lim and in_stage > lim:
            issues.append({"company": x.get("company"),
                           "problem": f"{in_stage}d in {x['stage']} (limit {lim})",
                           "fix": "advance or mark Lost"})
        untouched = _since(x.get("last_touch"), today)
        if untouched is not None and untouched > UNTOUCHED_DAYS:
            issues.append({"company": x.get("company"),
                           "problem": f"untouched {untouched}d",
                           "fix": "follow up per 02-sales/follow-up-cadence.md"})
        for field in ("company", "stage", "value", "decision_maker", "source"):
            if not x.get(field):
                issues.append({"company": x.get("company", "(unnamed)"),
                               "problem": f"missing {field}", "fix": "fill it in"})

    target = board.get("revenue_target_90d")
    coverage = (weighted / target) if target else None
    return {
        "task": "pipeline-hygiene", "as_of": today.isoformat(),
        "available": board["available"], "reason": board["reason"],
        "sources": ["07-dashboard/data.js", "02-sales/crm-hygiene.md",
                    "02-sales/forecast-method.md"],
        "open_deals": len(deals),
        "weighted": round(weighted, 2),
        "coverage": round(coverage, 2) if coverage is not None else None,
        "coverage_note": (None if coverage is not None else
                          "revenue_target_90d is unset — coverage cannot be computed, "
                          "and will not be guessed"),
        "below_target": coverage is not None and coverage < COVERAGE_TARGET,
        "alarm": coverage is not None and coverage < COVERAGE_ALARM,
        "issues": issues,
        "empty_pipeline_is_the_finding": len(deals) == 0,
    }


def monday_brief(today=None):
    """Monday 7am. Cash, pipeline movement, commitments, top 3."""
    today = _today(today)
    board, projs = projects_with_health(today)
    cash = ledger.cash_position()
    moc = board.get("monthly_operating_cost")
    proj = ledger.projection(weeks=13, monthly_operating_cost=moc, today=today)
    chase = invoice_chase_sweep(today)
    pipe = pipeline_hygiene(today)

    missing = []
    if not cash["available"]:
        missing.append("cash position — no balances recorded (ledger.py balance set)")
    if moc is None:
        missing.append("monthly_operating_cost — cash trigger levels stay off")
    if board.get("revenue_target_90d") is None:
        missing.append("revenue_target_90d — pipeline coverage cannot be computed")
    if not board["available"]:
        missing.append(board["reason"])

    # Top 3, proposed not decided: money first, then red projects, then commitments.
    top = []
    for r in chase["to_chase"][:2]:
        top.append(f"Chase {r['client']} {r['number']} — ${r['outstanding']:,.0f}, "
                   f"{r['overdue_days']}d overdue, tier {r['tier']} ({r['owner']})")
    for p in projs:
        if p["health"]["level"] == "red" and len(top) < 3:
            top.append(f"{p.get('name')} is RED — {', '.join(p['health']['reasons'])}")

    due = [c for c in board["commitments"] if not c.get("done")]
    due.sort(key=lambda c: c.get("due") or "9999")

    return {
        "task": "monday-brief", "as_of": today.isoformat(),
        # False when any source failed. A brief that reads "available" while
        # silently missing projects looks complete, which is worse than a brief
        # that says it is partial.
        "available": board["available"],
        "partial": bool(missing),
        "sources": ["08-automation/books/", "07-dashboard/data.js",
                    "00-charter/cadence-calendar.md"],
        "missing": missing,
        "cash": {"position": cash, "projection": proj},
        "ar": {"total_overdue": chase["total_overdue"],
               "count": len(chase["to_chase"]),
               "over_30": chase["aging"]["over_30"],
               "over_45": chase["aging"]["over_45"]},
        "pipeline": {"open": pipe["open_deals"], "weighted": pipe["weighted"],
                     "coverage": pipe["coverage"]},
        # Each section carries its own availability. A section that reports
        # zero red projects when it could not read the file at all is the
        # single failure this OS is built to avoid — "nothing to do" and "I
        # couldn't look" must never render the same.
        "projects": {"available": board["available"], "reason": board["reason"],
                     "red": [p.get("name") for p in projs if p["health"]["level"] == "red"],
                     "amber": [p.get("name") for p in projs if p["health"]["level"] == "amber"],
                     "total": len(projs)},
        "commitments": {"available": board["available"], "reason": board["reason"],
                        "items": due},
        "proposed_top_3": top[:3],
        "note": "Top 3 are proposed from the numbers. Joel decides.",
    }


def friday_closeout(today=None):
    """Friday 4pm. What shipped, what slipped, what carries over."""
    today = _today(today)
    board, projs = projects_with_health(today)
    done = [c for c in board["commitments"] if c.get("done")]
    carry = [c for c in board["commitments"] if not c.get("done")]
    slipped = [{"what": c.get("what"), "was_due": c.get("due"),
                "days_late": -_until(c.get("due"), today)}
               for c in carry
               if c.get("due") and _until(c.get("due"), today) < 0]
    return {
        "task": "friday-closeout", "as_of": today.isoformat(),
        "available": board["available"], "reason": board["reason"],
        "sources": ["07-dashboard/data.js", "08-automation/books/"],
        "shipped": [c.get("what") for c in done],
        "slipped": slipped,
        "carrying_over": [c.get("what") for c in carry],
        "red_into_next_week": [p.get("name") for p in projs
                               if p["health"]["level"] == "red"],
        "ar_position": ledger.ar_aging(today),
        "four_questions": [
            "What did I do this week that a contractor should have done?",
            "What am I avoiding?",
            "What would break first if I were away for two weeks?",
            "What did I learn that is not written down anywhere?",
        ],
    }


def month_end_prep(today=None):
    """25th. Reconciliation gaps while there is still time to fix them."""
    today = _today(today)
    board, projs = projects_with_health(today)
    gaps = []

    for e in ledger.missing_receipts():
        gaps.append({"kind": "missing receipt",
                     "detail": f"${e['amount']:,.2f} {e['category']} — {e['description']}",
                     "date": e["date"]})
    for t in ledger.contractor_totals(today.year):
        if t["blocker"]:
            gaps.append({"kind": "1099 blocked",
                         "detail": f"{t['name']} paid ${t['total']:,.2f} with no tax form on file",
                         "date": None})
    for i in ledger.invoices():
        if not i["settled"] and _until(i["due"], today) < -30:
            gaps.append({"kind": "invoice over 30 days",
                         "detail": f"{i['number']} {i.get('client')} ${i['outstanding']:,.2f}",
                         "date": i["due"]})
    for p in board["projects"]:
        if p.get("stage") == "Delivered":
            gaps.append({"kind": "delivered but not closed",
                         "detail": f"{p.get('name')} — usually an unpaid final invoice",
                         "date": None})

    orph = orphaned_invoices(today)
    for o in orph["orphans"]:
        gaps.append({"kind": "invoice not linked to a project",
                     "detail": f"{o['number']} points at \"{o['project']}\" which "
                               f"matches no project — ${o['outstanding']:,.2f} is "
                               f"invisible to that project's health",
                     "date": None})

    if not ledger.cash_position()["available"]:
        gaps.append({"kind": "no balances recorded",
                     "detail": "bank cannot be reconciled — ledger.py balance set",
                     "date": None})

    pnls = [ledger.project_pnl(p["name"]) for p in board["projects"]
            if p.get("stage") in ("Delivered", "Closed")]

    return {
        "task": "month-end-prep", "as_of": today.isoformat(), "available": True,
        "sources": ["08-automation/books/", "03-finance/month-end-close.md"],
        "gaps": gaps,
        "gap_count": len(gaps),
        "project_pnl": pnls,
        "checklist": "03-finance/month-end-close.md",
        "clean": len(gaps) == 0,
    }


TASKS = {
    "monday-brief": monday_brief,
    "project-status-rollup": project_status_rollup,
    "invoice-chase-sweep": invoice_chase_sweep,
    "pipeline-hygiene": pipeline_hygiene,
    "friday-closeout": friday_closeout,
    "month-end-prep": month_end_prep,
}


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv or argv[0] not in TASKS:
        print("usage: ops.py <task>\n\ntasks:")
        for t in TASKS:
            print("  " + t)
        return 1
    print(json.dumps(TASKS[argv[0]](), indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
