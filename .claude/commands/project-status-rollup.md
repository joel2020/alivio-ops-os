---
description: Wednesday — per-project stage, blockers, anything aging in stage
---

```bash
cd ~/alivio-ops-os/08-automation && python3 lib/ops.py project-status-rollup
```

Render per project: client, stage, days in stage against the limit, health and
the computed reason, next milestone.

Then, for each active project, draft the weekly status report using the
**alivio-status** skill. Wednesday is when they go out.

- Health is computed from `01-delivery/project-lifecycle.md`. Do not override it
  because a project "feels" fine.
- Anything red goes to Joel the same day, not into the report.
- Drafts only. The PM or Joel sends.
