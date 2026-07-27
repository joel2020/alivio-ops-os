---
description: 25th — reconciliation gaps, uncategorized items, close checklist
---

```bash
cd ~/alivio-ops-os/08-automation && python3 lib/ops.py month-end-prep
```

Report every gap with what closes it. Run on the 25th so there is still time to
fix things before the close.

Gap kinds and their fixes:
- **missing receipt** → attach it, or record why it does not exist
- **1099 blocked** → collect the W-9/W-8BEN before the next payment run. This is
  the rule that prevents the January scramble
- **invoice over 30 days** → this is also a RED trigger on its project
- **delivered but not closed** → usually an unpaid final invoice
- **no balances recorded** → `python3 lib/ledger.py balance set`

Then walk `03-finance/month-end-close.md`. Compute gross margin per delivered
project — it is the number that determines whether growth helps, and the one
most agencies never compute.
