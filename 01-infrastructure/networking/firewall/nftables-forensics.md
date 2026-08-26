---
title: "nftables and Conntrack Forensics"
category: "network"
tags:
  - nftables
  - conntrack
  - firewall
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# nftables and Conntrack Forensics

```bash
nft -a list ruleset
nft -j list ruleset > /var/tmp/nft-ruleset.json
sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_max
conntrack -S
ss -s
```

If conntrack is near capacity, determine table composition and traffic pattern before raising the limit. Increasing capacity consumes memory and may only postpone an abusive-flow problem.

Use rule handles (`nft -a`) when preparing a surgical rollbackable change; take a complete ruleset snapshot first.
