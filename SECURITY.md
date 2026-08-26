---
title: "Repository Security"
category: "security"
tags:
  - security
  - secrets
  - supply-chain
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Security

Never commit credentials, private keys, customer data, production inventory exports, or full incident logs containing secrets/PII.

## GitHub controls
- Protect `main` with review and required checks.
- Use least-privilege `GITHUB_TOKEN` permissions.
- Pin third-party GitHub Actions to immutable full commit SHAs.
- Enable secret scanning/code scanning where available.

## Agent controls
- Separate read-only evidence tools from mutating tools.
- Require explicit approval for production mutation.
- Enforce allowlists, argument validation, timeouts and audit logs.
- Re-fetch state immediately before a mutation to avoid acting on stale evidence.
