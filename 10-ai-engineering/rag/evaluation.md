---
title: "RAG Evaluation"
category: "ai"
tags:
  - rag
  - evaluation
  - retrieval
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# RAG Evaluation

Build a sanitized benchmark from real incident questions. Measure:
- recall@K for required evidence chunks,
- rank quality,
- metadata/environment filter correctness,
- citation correctness,
- unsupported recommendation rate,
- latency and cost.

Include adversarial cases where similar procedures exist for different platforms. A confident answer grounded in the wrong environment is a more serious failure than returning no answer.
