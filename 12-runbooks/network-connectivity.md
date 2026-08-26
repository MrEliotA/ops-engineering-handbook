---
title: "Network Connectivity Runbook"
category: "runbook"
tags:
  - network
  - tcp
  - dns
  - routing
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Network Connectivity Runbook

Work layer by layer and from both directions when possible:

```bash
ip -br addr
ip route get 203.0.113.10
ip neigh show
ss -s
resolvectl status 2>/dev/null || cat /etc/resolv.conf
tracepath 203.0.113.10
```

For TCP, distinguish DNS failure, route failure, SYN loss, SYN/ACK return-path filtering, TLS failure and application error. A successful ICMP echo does not prove the application path.
