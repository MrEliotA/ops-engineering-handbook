---
title: "Kubernetes Pressure Lab"
category: "platform"
tags:
  - kubernetes-pressure-lab
  - platform
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

# Kubernetes Pressure Lab

Start with object events, conditions and resource pressure; then descend from workload to node/network/storage.

```bash
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.lastTimestamp | tail -80
kubectl top nodes 2>/dev/null || true
```

Avoid deleting pods as a diagnostic reflex: restarts may hide evidence and reproduce the same scheduling, image, volume or dependency failure.
