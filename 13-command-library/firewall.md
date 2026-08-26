---
title: "Command Library: Firewall"
category: "command-library"
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

# Firewall Commands

```bash
nft -a list ruleset
nft -j list ruleset > /var/tmp/nft-ruleset.json
sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_max
conntrack -S
```
