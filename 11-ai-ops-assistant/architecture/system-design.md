---
title: "AI Ops Assistant System Design"
category: "ai-ops"
tags:
  - agent
  - operations
  - safety
  - architecture
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# AI Ops Assistant System Design

Recommended maturity path:

```text
L0 handbook search
L1 monitoring/log read
L2 bounded evidence collection
L3 change-plan generation
L4 human-approved mutation
L5 verified rollback automation
```

Keep tools typed and narrow. A `restart_service(host, unit)` tool is safer than an unrestricted remote shell. Re-read current state immediately before mutation and verify service health plus user-facing indicators afterward.
