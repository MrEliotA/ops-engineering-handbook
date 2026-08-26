---
title: "Command Library: MySQL"
category: "command-library"
tags:
  - mysql
  - sql
  - commands
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# MySQL Commands

```sql
SELECT SCHEMA_NAME,DIGEST,COUNT_STAR,
ROUND(SUM_TIMER_WAIT/1e12,2) total_s,
ROUND(AVG_TIMER_WAIT/1e9,2) avg_ms,
SUM_ROWS_EXAMINED,SUM_ROWS_SENT,LEFT(DIGEST_TEXT,220) digest_text
FROM performance_schema.events_statements_summary_by_digest
WHERE DIGEST IS NOT NULL
ORDER BY SUM_TIMER_WAIT DESC LIMIT 30;
```

```bash
mysqlcheck -u username -p --check --databases database_name
```

Do not routinely combine repair/optimize across all engines/databases without understanding engine semantics, lock/space impact and maintenance window.
