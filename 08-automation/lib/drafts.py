"""Draft the correct chase email for an invoice. Never sends it.

Copy comes from 05-templates/invoice-chase-emails.md. Tone escalates by tier,
deliberately — skipping a tier's register is how day 45 arrives.

There is no send function in this module, and there is no send function anywhere
in 08-automation. That is structural, not a convention: 03-finance/
ar-chase-sequence.md says nothing sends without Joel's approval, and the safest
way to honour that is for the capability not to exist.
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger  # noqa: E402

SIGN_PM = "[PM NAME]"
SIGN_JOEL = "Joel"


def _money(n):
    return f"${n:,.2f}"


def draft(invoice, today=None, pm_name=None, contact=None):
    """Return {subject, body, tier, send_as, warnings} for one invoice.

    `warnings` carries anything Joel must decide before sending. They are
    returned rather than resolved, because each is a judgment call the SOP
    reserves for him.
    """
    today = today or datetime.date.today()
    t = ledger.chase_tier(invoice, today)
    if not t:
        return None

    pm = pm_name or SIGN_PM
    name = contact or "[NAME]"
    num = invoice["number"]
    amt = _money(invoice["outstanding"])
    due = invoice["due"]
    over = t["overdue_days"]
    client = invoice.get("client", "[CLIENT]")
    warnings = []

    if invoice.get("disputed"):
        return None  # sequence paused; chase_tier already returns None

    if t["tier"] == 1:
        subject = f"Invoice {num} — {client} — due {due}"
        body = (
            f"Hi {name},\n\n"
            f"Quick one — invoice {num} for {amt} was due {due}. Attaching it "
            f"again here in case it needs re-sending to anyone on your side.\n\n"
            f"If it's already in motion, ignore me entirely.\n\n{pm}"
        )
        send_as = "PM"

    elif t["tier"] == 2:
        subject = f"Re: Invoice {num} — {client} — now {over} days overdue"
        body = (
            f"Hi {name},\n\n"
            f"Following up on invoice {num} for {amt}, which was due {due} and "
            f"is now {over} days past.\n\n"
            f"Could you let me know when it's scheduled for payment? If there's "
            f"a problem with the invoice itself, or something you need from us "
            f"to process it, tell me and I'll fix it today.\n\n{pm}"
        )
        send_as = "PM, Joel cc'd"

    elif t["tier"] == 3:
        subject = f"Invoice {num} — can we sort this out?"
        body = (
            f"Hi {name},\n\n"
            f"Invoice {num} for {amt} is now {over} days past due and I haven't "
            f"been able to get a date from your team.\n\n"
            f"I'd rather have a straight conversation than keep sending "
            f"reminders. If cash flow is tight, say so and we'll work out a "
            f"schedule that fits — I'd much prefer that to silence. If "
            f"something about the work isn't right, I want to hear it.\n\n"
            f"Can you reply today or tomorrow with either a payment date or "
            f"what's in the way?\n\n{SIGN_JOEL}"
        )
        send_as = "Joel, directly"
        warnings.append("Offers a payment plan. Joel decides the terms, and a "
                        "plan resets the clock only once, in writing.")

    elif t["tier"] == 4:
        stop = (ledger._d(due) + datetime.timedelta(days=30)).isoformat()
        subject = f"Invoice {num} — work pausing {stop}"
        body = (
            f"{name},\n\n"
            f"Invoice {num} for {amt} is now {over} days past due, and I "
            f"haven't had a response to my last message.\n\n"
            f"I need to let you know that work on [PROJECT] will pause on "
            f"{stop} unless payment is received or we've agreed a schedule "
            f"before then. That's not a position I want to be in, and I'd still "
            f"much rather resolve this.\n\n"
            f"Please reply with a payment date, or let me know a time to talk "
            f"this week.\n\n{SIGN_JOEL}"
        )
        send_as = "Joel, formal"
        warnings.append("DO NOT SEND unless Alivio will actually stop work. An "
                        "unenforced stop-work notice teaches the client that "
                        "Alivio's deadlines are decorative.")

    elif t["tier"] == 5:
        fee = ledger.late_fee(invoice, today)
        subject = f"[PROJECT] — work paused, invoice {num}"
        body = (
            f"{name},\n\n"
            f"As set out previously, work on [PROJECT] is paused as of today. "
            f"Invoice {num} for {amt} is {over} days past due.\n\n"
            f"Per our agreement, a late fee of 2% per month now applies to the "
            f"outstanding balance"
            + (f" — currently {_money(fee)}." if fee else ".") + "\n\n"
            f"Everything completed to date is safe and will be handed over as "
            f"soon as the account is settled. We can resume within [N] business "
            f"days of payment, though the timeline will need re-planning "
            f"against current capacity.\n\n"
            f"I'd like to resolve this. Please reply with a payment date or a "
            f"time to talk.\n\n{SIGN_JOEL}"
        )
        send_as = "Joel, formal"
        warnings.append("The 2% late fee must be in the signed SOW to be "
                        "referenced. Referencing a term that is not in the "
                        "contract is worse than not referencing one.")

    else:  # tier 6
        return {
            "number": num, "tier": 6, "send_as": "—",
            "subject": None, "body": None,
            "warnings": [f"Day {over}. This is a DECISION, not a message: "
                         f"collections, write-off, or a documented exception. "
                         f"{amt} outstanding. Log whichever it is."],
        }

    if not invoice.get("project"):
        warnings.append("No project on the invoice — [PROJECT] needs filling in.")

    return {"number": num, "client": client, "tier": t["tier"],
            "overdue_days": over, "outstanding": invoice["outstanding"],
            "send_as": send_as, "subject": subject, "body": body,
            "warnings": warnings,
            "source": "05-templates/invoice-chase-emails.md"}


def draft_all(today=None, pm_name=None):
    """Every chase due, worst first. Drafts only."""
    out = []
    for i in ledger.chase_list(today):
        d = draft(i, today, pm_name)
        if d:
            out.append(d)
    return out


if __name__ == "__main__":
    for d in draft_all():
        print("=" * 72)
        print(f"TIER {d['tier']}  {d['number']}  {d.get('client','')}  "
              f"${d['outstanding']:,.2f}  {d.get('overdue_days','')}d overdue")
        print(f"send as: {d['send_as']}")
        if d["subject"]:
            print(f"\nSubject: {d['subject']}\n\n{d['body']}")
        for w in d["warnings"]:
            print(f"\n  !! {w}")
    print("=" * 72)
    print("DRAFTS ONLY — nothing here can send. Joel reviews and sends.")
