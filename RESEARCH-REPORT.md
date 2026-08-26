---
title: "Repository Research and Design Report"
category: "meta"
tags:
  - research
  - architecture
  - rag
  - hermes
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Repository Research and Design Report

This repository implements the production-engineering handbook described in the supplied project report as actual files, scripts, CI, schemas and tests rather than external placeholder download links.

## Key decisions implemented
- Git-reviewed Markdown is authoritative; retrieval indexes and agent memory are derived.
- Runbooks and command libraries are optimized for evidence collection and discrimination, not beginner command lists.
- GitHub Actions uses least-privilege permissions and full commit SHA pins for the core official actions.
- RAG uses heading-aware chunks and is designed for hybrid retrieval and metadata filtering.
- The AI Ops/Hermes boundary keeps runtime automation separate from handbook governance.
- Mutating production automation follows approval and verification gates.

## Recommended repository split
Keep `engineering-handbook` as the reviewed knowledge repository. Place Hermes runtime plugins, production tool adapters, secrets bindings and schedules in a separate `hermes-ops-automation` repository. The shared interface is versioned document metadata/retrieval plus narrow tool contracts.
