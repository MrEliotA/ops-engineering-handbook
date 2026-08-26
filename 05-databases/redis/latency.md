---
title: "Redis Latency Triage"
category: "database"
tags:
  - redis
  - latency
  - memory
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Redis Latency Triage

```bash
redis-cli --latency-history
redis-cli INFO commandstats
redis-cli INFO memory
redis-cli SLOWLOG GET 32
redis-cli LATENCY DOCTOR
```

Correlate server-side latency with fork/persistence, memory fragmentation, eviction, large commands and network RTT. Avoid `KEYS *` in production; use cursor-based `SCAN` with a bounded `COUNT` when keyspace inspection is necessary.
