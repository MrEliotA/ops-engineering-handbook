---
title: "Handbook Architecture"
category: "meta"
tags:
  - architecture
  - knowledge-management
  - rag
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Architecture

## Trust boundaries

```text
Git-reviewed Markdown (authoritative)
        |\
        | +--> local search / Obsidian
        +----> validated chunks --> hybrid retrieval index --> assistant
                                                       |
Monitoring / logs / CMDB ------------------------------+
                                                       |
                                                       v
                                             evidence + hypotheses
                                                       |
                                                approval gate
                                                       |
                                             bounded automation
```

The handbook remains useful when AI, vector databases, or external APIs are unavailable. Runtime agents may propose handbook updates, but they do not directly rewrite approved procedures.

## Documentation layers

| Layer | Purpose | Paths |
|---|---|---|
| Quick response | incident triage and command recipes | `12-runbooks`, `13-command-library` |
| Deep knowledge | internals, failure modes, tuning | `01`–`07` |
| Machine-readable | schemas, ingestion, evaluation | `schemas`, `10`, `11`, `scripts/rag` |

## Change safety model

Each operational procedure should state scope, risk, expected evidence, rollback, and verification. Commands that mutate state are separated from diagnostic commands whenever possible.
