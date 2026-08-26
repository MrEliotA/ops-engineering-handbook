---
title: "Filesystem Capacity"
category: "linux"
tags:
  - filesystem-capacity
  - linux
  - production
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Filesystem Capacity

## Investigation focus
Establish baseline, scope and time window before tuning. Correlate host pressure with service latency and recent changes.

```bash
date -u +%FT%TZ
uptime
vmstat -w 1 5
cat /proc/pressure/cpu /proc/pressure/memory /proc/pressure/io
```

## Decision rule
Prefer the check that can falsify the leading hypothesis. Do not change kernel or service limits just because a counter is high; compare to workload, saturation and failure symptoms.
