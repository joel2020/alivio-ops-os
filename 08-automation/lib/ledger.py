"""The books. Invoices, payments, expenses, contractors, cash.

Why this exists: Alivio's stack named no accounting tool, which blocked the AR
chase sweep, the 13-week cash model, month-end close, and five of the eleven
scorecard metrics. Every one of those needs the same thing — a queryable record
of money owed and money spent.

WHAT THIS IS: an operational ledger. It answers "who owes me, how late are they,
and can I cover the contractor run." That is the question the OS actually needs
answered weekly.

WHAT THIS IS NOT: double-entry bookkeeping, and not a substitute for what an
accountant needs at year end. There is no chart of accounts, no journal, no
trial balance. It exports CSV so a bookkeeper can work from it. If Alivio later
buys QuickBooks or Xero, this becomes the operational layer in front of it or
gets retired — either is fine, and nothing else in the OS has to change because
everything reads through this module rather than the files.

STORAGE: append-only JSONL under books/. Append-only because a ledger you can
silently rewrite is a ledger nobody should trust, and because it makes every
change visible in git. Corrections are new entries, never edits.

MONEY IS NEVER MOVED. Nothing here pays, sends, or charges anything. It records
what a human did.
"""

import argparse
import csv
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "books")

INVOICES = os.path.join(BOOKS, "invoices.jsonl")
PAYMENTS = os.path.join(BOOKS, "payments.jsonl")
EXPENSES = os.path.join(BOOKS, "expenses.jsonl")
CONTRACTORS = os.path.join(BOOKS, "contractors.jsonl")
CONTRACTOR_PAY = os.path.join(BOOKS, "contractor-payments.jsonl")
ACCOUNTS = os.path.join(BOOKS, "accounts.jsonl")

# 03-finance/invoicing-policy.md — the source of truth. Mirrored, not invented.
NET_DAYS = 7
LATE_FEE_MONTHLY = 0.02
LATE_FEE_AFTER_DAYS = 30

# 03-finance/ar-chase-sequence.md
CHASE_TIERS = [
    (1,  1, "PM",   "friendly reminder"),
    (7,  2, "PM",   "firm, Joel cc'd"),
    (14, 3, "Joel", "Joel direct + payment plan offer"),
    (21, 4, "Joel", "stop-work notice"),
    (30, 5, "Joel", "work stops, late fee applies"),
    (45, 6, "Joel", "DECISION: collections / write-off"),
]

AR_BUCKETS = [("current", 0), ("1-30", 30), ("31-60", 60), ("60+", 10 ** 6)]

EXPENSE_CATEGORIES = [
    "software", "contractor", "hosting", "hardware", "travel",
    "professional-services", "marketing", "bank-fees", "tax", "other",
]

RECEIPT_REQUIRED_OVER = 75          # 03-finance/month-end-close.md


# ── storage ──────────────────────────────────────────────────────────────

def _read(path):
    """Every record. A malformed line is skipped, never guessed at."""
    if not os.path.exists(path):
        return []
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def _append(path, rec):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def _today(today=None):
    return today or datetime.date.today()


def _d(s):
    return datetime.date.fromisoformat(str(s)[:10])


def _plus(date, days):
    return (_d(date) + datetime.timedelta(days=days)).isoformat()


# ── invoices ─────────────────────────────────────────────────────────────

def issue_invoice(number, client, amount, issued=None, due=None, project="",
                  note="", path=None):
    """Record an invoice. Due date defaults to Net 7 from issue."""
    issued = issued or _today().isoformat()
    return _append(path or INVOICES, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "invoice", "number": number, "client": client,
        "project": project, "amount": round(float(amount), 2),
        "issued": issued, "due": due or _plus(issued, NET_DAYS),
        "note": note, "disputed": False, "void": False,
    })


def record_payment(number, amount, received=None, method="", path=None):
    """Record money actually arriving. Partial payments are allowed."""
    return _append(path or PAYMENTS, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "payment", "number": number,
        "amount": round(float(amount), 2),
        "received": received or _today().isoformat(), "method": method,
    })


def mark(number, field, value, path=None):
    """Amend an invoice by appending a correction, never by editing."""
    return _append(path or INVOICES, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "amend", "number": number, "field": field, "value": value,
    })


def invoices(inv_path=None, pay_path=None):
    """Current state of every invoice, with amendments and payments applied."""
    state = {}
    for r in _read(inv_path or INVOICES):
        if r.get("type") == "invoice":
            state[r["number"]] = dict(r, paid=0.0)
        elif r.get("type") == "amend" and r["number"] in state:
            state[r["number"]][r["field"]] = r["value"]
    for p in _read(pay_path or PAYMENTS):
        if p["number"] in state:
            state[p["number"]]["paid"] += p["amount"]
    for v in state.values():
        v["outstanding"] = round(v["amount"] - v["paid"], 2)
        v["settled"] = v["outstanding"] <= 0.005 or v.get("void")
    return list(state.values())


def chase_tier(inv, today=None):
    """Which chase tier an invoice has reached. None if not yet due or settled.

    A disputed invoice returns None — the sequence pauses, per the SOP. That is
    deliberate: chasing into a dispute converts a scope conversation into a
    payment fight.
    """
    if inv.get("settled") or inv.get("disputed") or inv.get("void"):
        return None
    over = (_today(today) - _d(inv["due"])).days
    if over < 1:
        return None
    hit = None
    for day, tier, who, label in CHASE_TIERS:
        if over >= day:
            hit = {"tier": tier, "who": who, "label": label, "day": day}
    if hit:
        hit["overdue_days"] = over
    return hit


def late_fee(inv, today=None):
    """Accrued late fee. Only past 30 days, per the invoicing policy."""
    if inv.get("settled") or inv.get("disputed"):
        return 0.0
    over = (_today(today) - _d(inv["due"])).days
    if over <= LATE_FEE_AFTER_DAYS:
        return 0.0
    months = (over - LATE_FEE_AFTER_DAYS) / 30.0
    return round(inv["outstanding"] * LATE_FEE_MONTHLY * months, 2)


def ar_aging(today=None, **kw):
    """AR split into the buckets the dashboard and scorecard both use."""
    today = _today(today)
    open_inv = [i for i in invoices(**kw) if not i["settled"]]
    buckets = {name: {"total": 0.0, "count": 0, "invoices": []}
               for name, _ in AR_BUCKETS}
    for i in open_inv:
        over = (today - _d(i["due"])).days
        name = "current" if over < 1 else next(
            n for n, mx in AR_BUCKETS[1:] if over <= mx)
        b = buckets[name]
        b["total"] = round(b["total"] + i["outstanding"], 2)
        b["count"] += 1
        b["invoices"].append(i["number"])
    total = round(sum(i["outstanding"] for i in open_inv), 2)
    over30 = round(sum(i["outstanding"] for i in open_inv
                       if (today - _d(i["due"])).days > 30), 2)
    over45 = round(sum(i["outstanding"] for i in open_inv
                       if (today - _d(i["due"])).days > 45), 2)
    return {"available": True, "as_of": today.isoformat(), "buckets": buckets,
            "total_outstanding": total, "over_30": over30, "over_45": over45,
            "open_count": len(open_inv)}


def chase_list(today=None, **kw):
    """Every invoice that has reached a tier, worst first. Drives the sweep."""
    out = []
    for i in invoices(**kw):
        t = chase_tier(i, today)
        if t:
            out.append({**i, "chase": t, "late_fee": late_fee(i, today)})
    out.sort(key=lambda x: (-x["chase"]["tier"], -x["outstanding"]))
    return out


# ── expenses ─────────────────────────────────────────────────────────────

def add_expense(amount, category, description, date=None, receipt=False,
                project="", path=None):
    if category not in EXPENSE_CATEGORIES:
        raise ValueError(f"category must be one of {EXPENSE_CATEGORIES}")
    amount = round(float(amount), 2)
    return _append(path or EXPENSES, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "expense", "amount": amount, "category": category,
        "description": description, "date": date or _today().isoformat(),
        "receipt": bool(receipt), "project": project,
        "receipt_required": amount > RECEIPT_REQUIRED_OVER,
    })


def expenses(since=None, path=None):
    rows = _read(path or EXPENSES)
    if since:
        rows = [r for r in rows if r["date"] >= since]
    return rows


def missing_receipts(path=None):
    """Month-end blocker: anything over the threshold without a receipt."""
    return [e for e in expenses(path=path)
            if e.get("receipt_required") and not e.get("receipt")]


# ── contractors ──────────────────────────────────────────────────────────

def add_contractor(name, archetype, rate, tax_form=False, start=None, path=None):
    return _append(path or CONTRACTORS, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "contractor", "name": name, "archetype": archetype,
        "rate": rate, "tax_form_on_file": bool(tax_form),
        "start": start or _today().isoformat(), "end": None,
    })


def pay_contractor(name, amount, project="", date=None, path=None):
    return _append(path or CONTRACTOR_PAY, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "contractor_payment", "name": name,
        "amount": round(float(amount), 2), "project": project,
        "date": date or _today().isoformat(),
    })


def contractors(path=None):
    state = {}
    for r in _read(path or CONTRACTORS):
        state[r["name"]] = r
    return list(state.values())


def contractor_totals(year=None, c_path=None, p_path=None):
    """Annual totals per contractor. Drives 1099 issuance in January.

    Flags anyone paid without a tax form on file — the single rule that
    prevents the January scramble.
    """
    year = year or _today().year
    reg = {c["name"]: c for c in contractors(c_path)}
    totals = {}
    for p in _read(p_path or CONTRACTOR_PAY):
        if _d(p["date"]).year != year:
            continue
        totals[p["name"]] = round(totals.get(p["name"], 0.0) + p["amount"], 2)
    out = []
    for name, total in sorted(totals.items(), key=lambda x: -x[1]):
        c = reg.get(name, {})
        out.append({"name": name, "total": total, "year": year,
                    "tax_form_on_file": bool(c.get("tax_form_on_file")),
                    "needs_1099": total >= 600,
                    "blocker": total >= 600 and not c.get("tax_form_on_file")})
    return out


# ── cash ─────────────────────────────────────────────────────────────────

def set_balance(account, balance, date=None, path=None):
    return _append(path or ACCOUNTS, {
        "ts": datetime.datetime.now().astimezone().isoformat(),
        "type": "balance", "account": account,
        "balance": round(float(balance), 2),
        "date": date or _today().isoformat(),
    })


def balances(path=None):
    """Latest recorded balance per account."""
    state = {}
    for r in sorted(_read(path or ACCOUNTS), key=lambda x: x["date"]):
        state[r["account"]] = r
    return state


def cash_position(path=None):
    b = balances(path)
    if not b:
        return {"available": False,
                "reason": "no balances recorded — run: ledger.py balance set",
                "total": None}
    # A 'tax' account is money held for a government, not Alivio's money.
    operating = sum(v["balance"] for k, v in b.items() if "tax" not in k.lower())
    tax = sum(v["balance"] for k, v in b.items() if "tax" in k.lower())
    oldest = min(v["date"] for v in b.values())
    return {"available": True, "total": round(operating, 2),
            "tax_set_aside": round(tax, 2),
            "accounts": {k: v["balance"] for k, v in b.items()},
            "as_of": oldest}


def projection(weeks=13, monthly_operating_cost=None, today=None, **kw):
    """13-week cash view, built from real invoice due dates.

    Overdue invoices are dated at TODAY + 7, not at their original due date.
    An invoice 20 days late does not arrive tomorrow because it was supposed
    to, and a model that assumes otherwise is reassuring and useless — the one
    place cash projections most often lie.

    Weighted pipeline is deliberately excluded. Cash planning uses money that
    has been agreed, never money that has been forecast.
    """
    today = _today(today)
    pos = cash_position()
    if not pos["available"]:
        return {"available": False, "reason": pos["reason"], "weeks": []}

    inflow = {}
    for i in invoices(**kw):
        if i["settled"]:
            continue
        due = _d(i["due"])
        if due < today:
            due = today + datetime.timedelta(days=7)
        wk = (due - today).days // 7
        if 0 <= wk < weeks:
            inflow[wk] = round(inflow.get(wk, 0.0) + i["outstanding"], 2)

    weekly_out = (monthly_operating_cost / 4.33) if monthly_operating_cost else 0.0

    running, rows, low = pos["total"], [], None
    for w in range(weeks):
        i_ = inflow.get(w, 0.0)
        running = round(running + i_ - weekly_out, 2)
        rows.append({
            "week": (today + datetime.timedelta(days=7 * w)).isoformat(),
            "in": i_, "out": round(weekly_out, 2), "balance": running})
        low = running if low is None else min(low, running)

    weeks_cover = (low / weekly_out) if weekly_out else None
    return {"available": True, "opening": pos["total"], "weeks": rows,
            "low_point": low, "weeks_of_cover": weeks_cover,
            "operating_cost_known": monthly_operating_cost is not None}


# ── project P&L ──────────────────────────────────────────────────────────

def project_pnl(project, e_path=None, p_path=None, **kw):
    """Revenue minus direct contractor cost. Metric 11 on the scorecard.

    Excludes Joel's time — Alivio has no internal rate for him, so including it
    would mean inventing one. This measures contractor leverage, not true
    profitability, and the scorecard says so.
    """
    rev = sum(i["amount"] for i in invoices(**kw)
              if i.get("project") == project and not i.get("void"))
    collected = sum(i["paid"] for i in invoices(**kw)
                    if i.get("project") == project)
    cost = sum(p["amount"] for p in _read(p_path or CONTRACTOR_PAY)
               if p.get("project") == project)
    cost += sum(e["amount"] for e in expenses(path=e_path)
                if e.get("project") == project)
    margin = rev - cost
    return {"project": project, "revenue": round(rev, 2),
            "collected": round(collected, 2),
            "direct_cost": round(cost, 2), "margin": round(margin, 2),
            "margin_pct": round(margin / rev, 4) if rev else None,
            "note": "excludes Joel's time — see 06-metrics/definitions.md"}


# ── export ───────────────────────────────────────────────────────────────

def export_csv(outdir, **kw):
    """Everything, as CSV, for a bookkeeper or accountant."""
    os.makedirs(outdir, exist_ok=True)
    written = []
    sets = {
        "invoices.csv": invoices(**kw),
        "payments.csv": _read(PAYMENTS),
        "expenses.csv": expenses(),
        "contractor-payments.csv": _read(CONTRACTOR_PAY),
    }
    for name, rows in sets.items():
        if not rows:
            continue
        keys = sorted({k for r in rows for k in r})
        p = os.path.join(outdir, name)
        with open(p, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            for r in rows:
                w.writerow(r)
        written.append(p)
    return written


# ── CLI ──────────────────────────────────────────────────────────────────

def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="ledger.py", description="Alivio operational ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("invoice", help="issue / pay / list")
    p.add_argument("action", choices=["new", "pay", "list", "dispute", "void"])
    p.add_argument("--number"); p.add_argument("--client", default="")
    p.add_argument("--project", default=""); p.add_argument("--amount", type=float)
    p.add_argument("--issued"); p.add_argument("--due"); p.add_argument("--note", default="")
    p.add_argument("--method", default="")

    p = sub.add_parser("expense", help="record an expense")
    p.add_argument("--amount", type=float, required=True)
    p.add_argument("--category", required=True, choices=EXPENSE_CATEGORIES)
    p.add_argument("--description", required=True)
    p.add_argument("--project", default=""); p.add_argument("--date")
    p.add_argument("--receipt", action="store_true")

    p = sub.add_parser("contractor", help="register / pay / totals")
    p.add_argument("action", choices=["add", "pay", "totals", "list"])
    p.add_argument("--name"); p.add_argument("--archetype", default="Build")
    p.add_argument("--rate", default=""); p.add_argument("--amount", type=float)
    p.add_argument("--project", default=""); p.add_argument("--tax-form", action="store_true")

    p = sub.add_parser("balance", help="record an account balance")
    p.add_argument("action", choices=["set", "show"])
    p.add_argument("--account"); p.add_argument("--amount", type=float)

    p = sub.add_parser("aging", help="AR aging report")
    p = sub.add_parser("chase", help="who needs chasing, and at which tier")
    p = sub.add_parser("cash", help="position and 13-week projection")
    p.add_argument("--monthly-cost", type=float)
    p = sub.add_parser("pnl", help="project profitability")
    p.add_argument("--project", required=True)
    p = sub.add_parser("export", help="CSV for the accountant")
    p.add_argument("--out", default=os.path.join(ROOT, "books", "export"))

    a = ap.parse_args(argv)

    if a.cmd == "invoice":
        if a.action == "new":
            r = issue_invoice(a.number, a.client, a.amount, a.issued, a.due,
                              a.project, a.note)
            print(f"issued {r['number']}  ${r['amount']:,.2f}  due {r['due']}")
        elif a.action == "pay":
            r = record_payment(a.number, a.amount, method=a.method)
            print(f"recorded ${r['amount']:,.2f} against {r['number']}")
        elif a.action in ("dispute", "void"):
            mark(a.number, "disputed" if a.action == "dispute" else "void", True)
            print(f"{a.number} marked {a.action}")
        else:
            for i in invoices():
                s = "PAID" if i["settled"] else f"owes ${i['outstanding']:,.2f}"
                print(f"  {i['number']:16} {i['client'][:18]:18} "
                      f"${i['amount']:>10,.2f}  due {i['due']}  {s}")

    elif a.cmd == "expense":
        r = add_expense(a.amount, a.category, a.description, a.date,
                        a.receipt, a.project)
        warn = "" if r["receipt"] or not r["receipt_required"] else "  ** RECEIPT NEEDED **"
        print(f"recorded ${r['amount']:,.2f} {r['category']}{warn}")

    elif a.cmd == "contractor":
        if a.action == "add":
            add_contractor(a.name, a.archetype, a.rate, a.tax_form)
            print(f"registered {a.name}" +
                  ("" if a.tax_form else "  ** NO TAX FORM — do not pay yet **"))
        elif a.action == "pay":
            pay_contractor(a.name, a.amount, a.project)
            print(f"recorded ${a.amount:,.2f} to {a.name}")
        elif a.action == "list":
            for c in contractors():
                print(f"  {c['name'][:22]:22} {c['archetype'][:10]:10} "
                      f"{str(c['rate'])[:12]:12} "
                      f"{'W-9 on file' if c['tax_form_on_file'] else 'NO TAX FORM'}")
        else:
            for t in contractor_totals():
                flag = "  ** 1099 BLOCKED: no tax form **" if t["blocker"] else ""
                print(f"  {t['name'][:22]:22} ${t['total']:>10,.2f}  "
                      f"{'1099 required' if t['needs_1099'] else ''}{flag}")

    elif a.cmd == "balance":
        if a.action == "set":
            set_balance(a.account, a.amount)
            print(f"{a.account} = ${a.amount:,.2f}")
        else:
            print(json.dumps(cash_position(), indent=2))

    elif a.cmd == "aging":
        r = ar_aging()
        print(f"AR as of {r['as_of']} — ${r['total_outstanding']:,.2f} across "
              f"{r['open_count']} invoice(s)")
        for name, b in r["buckets"].items():
            if b["count"]:
                print(f"  {name:8} ${b['total']:>11,.2f}  {b['count']} "
                      f"({', '.join(b['invoices'])})")
        print(f"  over 30: ${r['over_30']:,.2f}   over 45: ${r['over_45']:,.2f}")

    elif a.cmd == "chase":
        rows = chase_list()
        if not rows:
            print("Nothing overdue.")
        for i in rows:
            c = i["chase"]
            fee = f"  +${i['late_fee']:,.2f} late fee" if i["late_fee"] else ""
            print(f"  TIER {c['tier']}  {i['number']:16} {i['client'][:16]:16} "
                  f"${i['outstanding']:>10,.2f}  {c['overdue_days']}d overdue  "
                  f"-> {c['who']}: {c['label']}{fee}")

    elif a.cmd == "cash":
        r = projection(monthly_operating_cost=a.monthly_cost)
        if not r["available"]:
            print(r["reason"]); return 1
        print(f"opening ${r['opening']:,.2f}   low point ${r['low_point']:,.2f}")
        if r["weeks_of_cover"] is not None:
            print(f"weeks of cover at the low point: {r['weeks_of_cover']:.1f}")
        else:
            print("weeks of cover: unknown — pass --monthly-cost")
        for w in r["weeks"]:
            print(f"  {w['week']}  in ${w['in']:>10,.2f}  out ${w['out']:>9,.2f}"
                  f"  bal ${w['balance']:>11,.2f}")

    elif a.cmd == "pnl":
        print(json.dumps(project_pnl(a.project), indent=2))

    elif a.cmd == "export":
        for p in export_csv(a.out):
            print("wrote", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
