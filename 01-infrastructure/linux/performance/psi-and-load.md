---
title: "Pressure Stall Information and Load"
category: "linux"
tags:
  - linux
  - psi
  - load-average
  - capacity
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# PSI and Load Average

Load average counts runnable tasks and tasks in uninterruptible sleep; it is not a CPU-percent metric. Diagnose it with run queue, PSI, latency and device evidence.

```bash
uptime
cat /proc/loadavg
vmstat -w 1 10
cat /proc/pressure/{cpu,memory,io}
iostat -xmdz 1 10
```

### Patterns
- High load + high CPU PSI + low I/O PSI: CPU scheduling contention.
- High load + high I/O PSI + elevated device await: storage path bottleneck.
- High memory PSI + major faults/reclaim + swap activity: memory pressure.
- High load with low PSI can indicate short bursts or many tasks that still make progress.

Correlate with application latency before remediation; an overloaded batch node and a latency-critical API have different acceptable pressure profiles.
