---
title: "MySQL Performance Schema Triage"
category: "database"
tags:
  - mysql
  - performance-schema
  - sql
  - latency
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# MySQL Performance Schema Triage

Aggregate statement classes before reacting to one active query.

```sql
SELECT
    SCHEMA_NAME,
    DIGEST,
    COUNT_STAR,
    ROUND(SUM_TIMER_WAIT/1e12, 2) AS total_s,
    ROUND(AVG_TIMER_WAIT/1e9, 2) AS avg_ms,
    SUM_ROWS_EXAMINED,
    SUM_ROWS_SENT,
    SUM_CREATED_TMP_DISK_TABLES,
    LEFT(DIGEST_TEXT, 240) AS digest_text
FROM performance_schema.events_statements_summary_by_digest
WHERE DIGEST IS NOT NULL
ORDER BY SUM_TIMER_WAIT DESC
LIMIT 30;
```

Correlate high total time with call count, rows examined/sent, temp-disk tables and schema. A query with high average latency but tiny call volume may matter less than a moderately slow query executed millions of times.
