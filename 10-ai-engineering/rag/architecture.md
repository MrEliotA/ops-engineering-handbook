---
title: "RAG Architecture for Operations"
category: "ai"
tags:
  - rag
  - hybrid-search
  - retrieval
  - operations
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# RAG Architecture for Operations

Use Git-reviewed Markdown as source of truth. Build stable, heading-aware chunks; store path, section, status, category, risk and review date as metadata.

For operational corpora, hybrid retrieval is useful because exact tokens such as `nf_conntrack_max`, `pm.max_children`, SQL error codes and service unit names matter alongside semantic similarity.

Pipeline:

```text
validate -> chunk -> dense embedding + lexical index -> metadata filter -> rerank -> cited context
```

Never let conversational memory silently become an authoritative runbook source.
