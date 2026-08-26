---
title: "Command Library: Networking"
category: "command-library"
tags:
  - network
  - iproute2
  - ss
  - tcpdump
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Networking Commands

```bash
ip -br link
ip -br addr
ip -s link
ip rule show
ip route show table all
ss -Htanp state established
ss -s
nstat -az
```

```bash
timeout 30 tcpdump -ni any -s 0 -B 4096 -w /var/tmp/capture.pcap 'tcp port 443'
```
