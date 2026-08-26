---
title: "Dns Debugging"
category: "network"
tags:
  - dns-debugging
  - network
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

# Dns Debugging

## Investigation focus
Identify the failing layer: name resolution, route, neighbor discovery, stateful filtering, TCP handshake, TLS, or application response.

```bash
ip -br addr
ip route show table all
ss -s
nstat -az
```

Capture bounded packet evidence when counters cannot distinguish loss from rejection. Validate both forward and return paths for asymmetric-routing problems.
