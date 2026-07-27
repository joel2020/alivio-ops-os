---
name: alivio-chase
description: Draft the right accounts-receivable chase email for an overdue Alivio invoice, at the correct escalation tier for its age. Use when Joel says an invoice is late or unpaid, asks who owes money, asks to chase or follow up on payment, mentions AR or receivables, asks what to send a client about an invoice, or asks how overdue something is. Never sends — drafts only.
---

# Draft an AR chase

Tiers, timing, and copy are defined in the OS. This skill computes which tier an
invoice has reached and produces the matching draft. **It never sends.**

## Run it

```bash
cd ~/alivio-ops-os/08-automation
python3 lib/drafts.py                       # every chase due, worst first
python3 lib/ops.py invoice-chase-sweep      # the structured sweep
```

For one invoice:

```bash
python3 -c "
import sys; sys.path.insert(0,'lib')
import ledger, drafts, json
inv = [i for i in ledger.invoices() if i['number']=='ALI-2026-018'][0]
print(json.dumps(drafts.draft(inv), indent=2))"
```

If the invoice is not in the books yet, add it first — do not draft from memory:

```bash
python3 lib/ledger.py invoice new --number X --client Y --amount 1000 \
  --project "..." --issued 2026-07-01
```

## Then

1. **Show Joel the draft, the tier, and the reason for that tier.** The age
   determines the tier; it is not a judgment call.
2. **Surface every warning the draft carries.** They are real:
   - Tier 4 must not be sent unless Alivio will actually stop work. An
     unenforced stop-work notice teaches the client that Alivio's deadlines are
     decorative.
   - Tier 5 references the 2% late fee, which must be in the signed SOW to be
     referenced at all.
   - Tier 6 is a decision, not a message — collections, write-off, or a
     documented exception.
3. **Fill the placeholders** — `[NAME]`, `[PROJECT]`, `[PM NAME]` — from what
   Joel tells you. Never invent a contact name.
4. **Joel sends it.** Not you. There is no send path in this codebase and that
   is deliberate.
5. When payment arrives: `python3 lib/ledger.py invoice pay --number X --amount N`

## Hard rules

- **Never send anything.** Draft, show, stop.
- **Never move money.**
- **A disputed invoice is not chased.** The sequence pauses — chasing into a
  dispute converts a scope conversation into a payment fight. If Joel says a
  client is disputing: `python3 lib/ledger.py invoice dispute --number X`
- **Never soften a tier because the client is nice.** The schedule running
  regardless is what makes it routine rather than a confrontation. Skipping a
  tier is how day 45 arrives.
- **Tell the PM before any tier 3+ message** on a project they are mid-delivery
  with. Walking in blind damages the relationship they are holding.

## Reference

- `03-finance/ar-chase-sequence.md` — the sequence and its reasoning
- `05-templates/invoice-chase-emails.md` — the copy per tier
- `03-finance/invoicing-policy.md` — terms, late fee, what an invoice contains
