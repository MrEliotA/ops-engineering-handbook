---
title: "Hermes Integration Boundary"
category: "ai-ops"
tags:
  - hermes
  - agent
  - security
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

# Hermes Integration Boundary

Treat the handbook and agent runtime as separate repositories with an explicit interface.

```text
engineering-handbook (reviewed knowledge)
        -> validated retrieval index
        -> Hermes/agent runtime
        -> read-only adapters / approved automation
```

The agent may draft a pull request after an incident, but human review promotes knowledge. Agent memory, schedules and runtime plugins are not authoritative handbook state. Production credentials remain in a secret manager and should be scoped per tool/action.
