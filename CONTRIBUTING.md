---
title: "Contributing"
category: "meta"
tags:
  - contributing
  - review
  - quality
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Contributing

## Acceptance criteria

A production document should answer: **when to use it, what evidence it collects, how results change the hypothesis, what can go wrong, and how to verify recovery**.

Avoid beginner-only command dumps. Prefer commands with explicit output fields, time bounds, sorting, filters, and correlation keys.

Before opening a PR:

```bash
python3 scripts/rag/validate_frontmatter.py .
python3 scripts/quality/check_links.py .
pytest -q
```
