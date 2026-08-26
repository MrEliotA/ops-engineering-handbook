---
title: "DirectAdmin dataskq and Task Queue"
category: "hosting"
tags:
  - directadmin
  - dataskq
  - hosting
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# DirectAdmin `dataskq`

The task queue is operational state. Inspect it before deleting queue items or forcing rebuilds.

```bash
ls -l /usr/local/directadmin/data/task.queue*
/usr/local/directadmin/dataskq d80
```

When working with CustomBuild, understand the distinction between the ordinary task queue and CustomBuild queue processing. Do not assume a CustomBuild invocation drains all DirectAdmin tasks.
