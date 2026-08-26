---
title: "MySQL Outage Runbook"
category: "runbook"
tags:
  - mysql
  - outage
  - database
status: "approved"
audience: "senior"
risk: "high"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# MySQL Outage Runbook

Capture host pressure, disk/inodes, MySQL unit result, error log tail and port/listener state before restart. If storage is full, determine which filesystem and growth source; deleting database files is not remediation.

After service recovery, validate application read/write paths, replication and crash-recovery completion before closing the incident.
