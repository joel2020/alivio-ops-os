---
description: Tuesday + Friday — overdue list and drafted chase emails, unsent
---

```bash
cd ~/alivio-ops-os/08-automation
python3 lib/ops.py invoice-chase-sweep
python3 lib/drafts.py
```

Present as a list: invoice, client, amount outstanding, days overdue, tier, who
owns it, and the draft.

**Surface every warning.** They are real:
- Tier 4 must not be sent unless Alivio will actually stop work
- Tier 5 references the 2% late fee, which must be in the signed SOW
- Tier 6 is a decision, not a message

Fill `[NAME]` and `[PROJECT]` from what Joel provides. Never invent a contact.

Check `orphaned_invoices` — an invoice pointing at a project name that does not
exist means that money is invisible to the project's health and the 30-day RED
trigger will never fire for it. Report it and name the fix.

**Nothing sends. Joel reviews and sends.** Twice weekly, because a weekly sweep
lets a tier slip by up to six days and the boundaries are days 1 and 7.
