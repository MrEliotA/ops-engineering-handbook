---
title: "Roadmap"
category: "meta"
tags:
  - roadmap
  - platform
  - ai
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Roadmap

## Phase 1 — operational corpus
- Expand Linux, shared-hosting, database and network runbooks from real incidents.
- Add environment-specific overlays outside the public handbook.
- Build a sanitized retrieval evaluation set.

## Phase 2 — retrieval
- Heading-aware chunking with stable document IDs.
- Hybrid lexical+dense retrieval with metadata filters.
- Retrieval evaluation in CI for approved benchmark questions.

## Phase 3 — AI operations
- Read-only telemetry adapters.
- Evidence-pack generation and cited hypothesis ranking.
- Human-approved, bounded remediations with automatic verification.

## Phase 4 — controlled automation
- Canary execution, policy-as-code, rollback automation and audit trails.
