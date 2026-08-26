---
title: "MySQL Lock Attribution"
category: "database"
tags:
  - mysql
  - locks
  - innodb
  - transactions
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# MySQL Lock Attribution

```sql
SELECT * FROM performance_schema.data_lock_waits\G
SELECT * FROM information_schema.innodb_trx\G
```

Map waiting and blocking transaction/thread IDs back to statements and application identity. Before killing a blocker, establish transaction age, modified rows, rollback cost and whether it is a legitimate batch/DDL operation.
