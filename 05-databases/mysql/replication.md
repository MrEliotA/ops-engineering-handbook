---
title: "MySQL Replication Triage"
category: "database"
tags:
  - mysql
  - replication
  - gtid
  - recovery
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# MySQL Replication Triage

Inspect source/replica coordinates or GTID state, I/O/SQL/applier errors, lag semantics, relay logs and replication filters. Do not equate a single lag counter with data freshness when parallel appliers or delayed replication are in use.

For modern MySQL:

```sql
SHOW REPLICA STATUS\G
SELECT * FROM performance_schema.replication_connection_status\G
SELECT * FROM performance_schema.replication_applier_status_by_worker\G
```

Avoid `RESET REPLICA` or skipping transactions until root cause and consistency implications are understood.
