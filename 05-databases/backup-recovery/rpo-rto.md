---
title: "Rpo Rto"
category: "database"
tags:
  - rpo-rto
  - database
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

# Rpo Rto

## Investigation focus
Correlate workload class, latency, locks/transactions, I/O and connection pressure. Prefer aggregate/query-digest evidence to isolated snapshots.

## Change safety
Before terminating sessions or changing durability/concurrency settings, estimate rollback cost and verify the application impact. Recovery is complete only after application-level read/write checks.
