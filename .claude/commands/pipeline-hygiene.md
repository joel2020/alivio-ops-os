---
description: Friday — stale deals, missing fields, deals with no next step
---

```bash
cd ~/alivio-ops-os/08-automation && python3 lib/ops.py pipeline-hygiene
```

Work the `issues` array with Joel. Every one resolves to: add a next step,
advance the stage, fill the field, or mark Lost. **There is no fifth option, and
"leave it" is not one of them.**

- A deal without a next step is not being worked.
- Deals go Lost, not stale. A pipeline that only grows is one nobody believes.
- If `empty_pipeline_is_the_finding` is true, say so directly — an empty pipeline
  is the most important thing on the page, not a blank section.
- If coverage cannot be computed, say why rather than skipping it.

Then record the weighted number. **Writing it down is the point** — a forecast
that is computed and not recorded cannot show a trend, and the trend is the
useful part.
