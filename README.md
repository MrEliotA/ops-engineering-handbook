---
title: "Production Engineering Handbook"
category: "meta"
tags:
  - handbook
  - operations
  - sre
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Production Engineering Handbook

A production-first knowledge system for senior Linux/hosting/DevOps/SRE operations. Git is the source of truth; RAG indexes, agent memory, and runtime state are derived.

## Design rules

1. **Evidence first, mutation second.** Gather timestamps, scope, resource pressure, logs, and service state before changing production.
2. **Prefer discriminating checks.** Every command should narrow hypotheses, not merely print data.
3. **Bound blast radius.** Read-only by default; mutations need preconditions, rollback, and post-change verification.
4. **Preserve provenance.** Incident evidence and handbook changes should be reviewable in Git.
5. **Keep runtime secrets out of this repository.** Store credentials and production inventory in dedicated systems.

## Fast entry points

- [`12-runbooks/`](12-runbooks/) — incident procedures.
- [`13-command-library/`](13-command-library/) — advanced command recipes.
- [`01-infrastructure/`](01-infrastructure/) — Linux, networking, hosting and web-stack internals.
- [`05-databases/`](05-databases/) — database diagnostics and recovery.
- [`06-security/`](06-security/) — hardening and incident response.
- [`07-sre/`](07-sre/) — SLI/SLO, incident command, capacity and DR.
- [`10-ai-engineering/`](10-ai-engineering/) — RAG and evaluation.
- [`11-ai-ops-assistant/`](11-ai-ops-assistant/) — safe AI-assisted operations architecture.

## Local validation

```bash
python3 scripts/rag/validate_frontmatter.py .
python3 -m compileall -q scripts
bash -n scripts/**/*.sh 2>/dev/null || true
pytest -q
```

## Package

```bash
python3 scripts/quality/build_release_zip.py --root . --output ../engineering-handbook-ready-to-push.zip
```

See [`ARCHITECTURE.md`](ARCHITECTURE.md), [`WORKFLOW.md`](WORKFLOW.md), and [`SECURITY.md`](SECURITY.md).
