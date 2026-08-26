---
title: "PostgreSQL Lock and Query Triage"
category: "database"
tags:
  - postgresql
  - locks
  - pg_stat_activity
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# PostgreSQL Lock and Query Triage

```sql
SELECT pid, usename, application_name, state, wait_event_type, wait_event,
       now()-query_start AS query_age, now()-xact_start AS xact_age,
       left(query, 240) AS query
FROM pg_stat_activity
WHERE pid <> pg_backend_pid()
ORDER BY xact_start NULLS LAST;
```

Use `pg_blocking_pids(pid)` to identify blockers. Prefer cancelling a statement before terminating a backend when that is sufficient, and consider rollback cost of long write transactions.
