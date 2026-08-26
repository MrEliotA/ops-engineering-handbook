---
title: "SLI, SLO and Error Budgets"
category: "sre"
tags:
  - slo
  - sli
  - error-budget
  - reliability
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# SLI/SLO and Error Budgets

An SLO should be tied to user-observable reliability, not server health alone. Typical request SLIs include successful request ratio and latency distribution; batch SLIs include completion freshness and correctness.

Use multi-window burn-rate alerting so both fast catastrophic failures and slower sustained budget consumption are visible. Operational policy should specify what release/feature decisions change when budget is exhausted.
