---
description: Monday 7am — cash, pipeline movement, week's commitments, top 3
---

Run the Monday brief.

```bash
cd ~/alivio-ops-os/08-automation
python3 lib/sync_dashboard.py --check   # is the dashboard's money current?
python3 lib/ops.py monday-brief
```

Render it for Joel, in this order — money first, because it is the only thing
that can end the business quickly:

1. **Missing inputs.** Report the `missing` array FIRST, plainly. A brief that
   silently omits cash because the books could not be read is worse than no
   brief, because it looks complete.
2. **Cash** — position, 13-week low point, weeks of cover, which trigger level.
   If `monthly_operating_cost` is unset, say the trigger levels are off. Do not
   estimate it.
3. **AR** — total overdue, count, over-30, over-45. Over-45 means the chase
   sequence never ran.
4. **Projects** — red first, then amber, with the computed reason.
5. **Pipeline** — open, weighted, coverage. If `revenue_target_90d` is unset,
   say coverage cannot be computed.
6. **Commitments due this week** — `commitments.items`. If
   `commitments.available` is false, say the file could not be read rather than
   reporting an empty week.
7. **Proposed top 3** — say plainly that these are proposed from the numbers and
   Joel decides.

If `available` is false, **lead with that**. A partial brief is useful; a partial
brief presented as complete is not.

Cite the sources listed in the output. Never invent a number that came back null.
