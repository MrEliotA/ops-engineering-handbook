---
title: "Hypothesis Ranking"
category: "ai"
tags:
  - hypothesis-ranking
  - ai
  - production
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Hypothesis Ranking

Design the system so retrieved evidence is traceable to reviewed sources and environment metadata. Evaluate retrieval and tool execution separately.

Operational assistants should be able to return **insufficient evidence** rather than inventing a remediation. Mutating actions require typed arguments, policy checks, approval and post-action verification.
