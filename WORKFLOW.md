---
title: "Handbook Workflow"
category: "meta"
tags:
  - workflow
  - git
  - review
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Workflow

## Daily use

1. Search the runbooks or command library.
2. Capture evidence with UTC timestamps and host/service identity.
3. Correlate pressure, logs, service state, and recent changes.
4. Form ranked hypotheses and run the cheapest discriminating checks.
5. If change is required, record preconditions, rollback and verification.
6. Promote reusable lessons through a pull request.

## Content lifecycle

`draft -> reviewed -> approved -> deprecated`

Use small PRs. A runbook change caused by an incident should link the incident/ticket in the PR description, but not embed private customer data in Markdown.
