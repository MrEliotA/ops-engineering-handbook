---
title: "Pam Analysis"
category: "engineering"
tags:
  - pam-analysis
  - engineering
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

# Pam Analysis

This note captures production-oriented operating guidance for **Pam Analysis**. Start from evidence, make hypotheses explicit, bound risky changes, and verify from the user/service perspective after intervention.

## Review prompts
- What signal proves this failure mode?
- Which adjacent failure mode can look similar?
- What is the lowest-risk discriminating check?
- What rollback and post-change validation are required?
