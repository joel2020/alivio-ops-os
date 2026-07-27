"""Generate the dashboard's money from the books.

Before this, dashboard/data.js was hand-maintained in full — including AR, which
is exactly the number nobody should be retyping. A dashboard whose cash figures
are transcribed by hand is a dashboard that is wrong in a way nobody notices.

This rewrites ONLY the money: invoices and cash come from the ledger. Projects,
pipeline, and commitments stay hand-edited, because no system here knows them
and inventing them would be worse than typing them.

    python3 lib/sync_dashboard.py            # write it
    python3 lib/sync_dashboard.py --check    # is it stale? exit 1 if so

The `--check` mode is what the Monday brief runs, so a stale dashboard is
reported rather than silently believed.
"""

import argparse
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger  # noqa: E402

# lib/ -> 08-automation/ -> alivio-ops-os/. The dashboard is a sibling of
# 08-automation, not a child of it — getting this wrong silently writes a stray
# data.js one level too deep and leaves the real one untouched.
AUTOMATION = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OS_ROOT = os.path.dirname(AUTOMATION)
DATA_JS = os.path.join(OS_ROOT, "07-dashboard", "data.js")

HEADER = """/* Alivio Studios — dashboard data
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
 * Generated %s
 */

window.ALIVIO_DATA = %s;
"""


def strip_js_comments(src):
    """Comments out, so the object can be read as JSON.

    String-aware: a // inside "https://..." is not a comment, and getting that
    wrong silently truncates a URL in the middle of the data.
    """
    out, i, n = [], 0, len(src)
    in_str = None
    while i < n:
        c = src[i]
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(src[i + 1]); i += 2; continue
            if c == in_str:
                in_str = None
            i += 1; continue
        if c in "\"'":
            in_str = c; out.append(c); i += 1; continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            i = n if j == -1 else j + 2
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            i = n if j == -1 else j
            continue
        out.append(c); i += 1
    return "".join(out)


def read_existing(path=None):
    """Load the current data.js so hand-maintained sections survive."""
    path = path or DATA_JS
    if not os.path.exists(path):
        return {}
    raw = open(path).read()
    m = re.search(r"window\.ALIVIO_DATA\s*=\s*(\{.*\})\s*;", raw, re.S)
    if not m:
        return {}
    body = strip_js_comments(m.group(1))
    body = re.sub(r",(\s*[}\]])", r"\1", body)     # tolerate trailing commas
    try:
        return json.loads(body)
    except json.JSONDecodeError as e:
        raise SystemExit(f"data.js is not readable as JSON: {e}\n"
                         "Fix it by hand, or delete it and re-run to start fresh.")


def build(today=None):
    """The money sections, from the books."""
    today = today or datetime.date.today()
    invs = []
    for i in ledger.invoices():
        if i.get("void"):
            continue
        note = i.get("note", "")
        # A partly-paid invoice must not read as if the full amount is owed.
        if 0 < i["paid"] < i["amount"]:
            note = (note + "  " if note else "") + \
                   f"[${i['outstanding']:,.0f} outstanding of ${i['amount']:,.0f}]"
        invs.append({
            "number": i["number"], "client": i.get("client", ""),
            "project": i.get("project", ""),
            # The dashboard should chase what is still owed, not the original
            # face value.
            "amount": i["outstanding"] if not i["settled"] else i["amount"],
            "issued": i.get("issued"), "due_date": i["due"],
            "paid": bool(i["settled"]), "disputed": bool(i.get("disputed")),
            "note": note,
        })
    pos = ledger.cash_position()
    proj = ledger.projection(weeks=13, today=today)
    cash = {
        "on_hand": pos["total"] if pos["available"] else None,
        "tax_set_aside": pos.get("tax_set_aside") if pos["available"] else None,
        # Still Joel's to provide — the ledger cannot infer it, and guessing
        # would switch the cash trigger levels on with a fabricated number.
        "monthly_operating_cost": None,
        "projection": ([{"week": w["week"], "in": w["in"], "out": w["out"]}
                        for w in proj["weeks"]] if proj["available"] else []),
    }
    return invs, cash


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report staleness instead of writing; exit 1 if stale")
    ap.add_argument("--out", default=DATA_JS)
    a = ap.parse_args(argv)

    existing = read_existing(a.out)
    invs, cash = build()

    if a.check:
        stale = []
        if existing.get("invoices") != invs:
            stale.append(f"invoices ({len(existing.get('invoices', []))} in "
                         f"data.js vs {len(invs)} in the books)")
        if (existing.get("cash") or {}).get("on_hand") != cash["on_hand"]:
            stale.append("cash position")
        if stale:
            print("data.js is STALE: " + "; ".join(stale))
            print("  fix: python3 08-automation/lib/sync_dashboard.py")
            return 1
        print("data.js money is current with the books.")
        return 0

    merged = {
        "updated": datetime.date.today().isoformat(),
        "cash": cash,
        "invoices": invs,
        # preserved, never generated
        "projects": existing.get("projects", []),
        "pipeline": existing.get("pipeline", []),
        "revenue_target_90d": existing.get("revenue_target_90d"),
        "commitments": existing.get("commitments", []),
    }
    body = json.dumps(merged, indent=2, ensure_ascii=False)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as f:
        f.write(HEADER % (datetime.date.today().isoformat(), body))

    print(f"wrote {a.out}")
    print(f"  generated : {len(invs)} invoice(s), cash "
          f"{'from books' if cash['on_hand'] is not None else 'UNSET — no balances recorded'}")
    print(f"  preserved : {len(merged['projects'])} project(s), "
          f"{len(merged['pipeline'])} deal(s), "
          f"{len(merged['commitments'])} commitment(s)")
    if cash["monthly_operating_cost"] is None:
        print("  note      : monthly_operating_cost is still unset, so cash "
              "trigger levels stay off. Set it in data.js by hand.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
