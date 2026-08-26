---
title: "Production Packet Capture"
category: "network"
tags:
  - tcpdump
  - pcap
  - network
  - tcp
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Production Packet Capture

Prefer bounded captures to open-ended packet collection.

```bash
sudo timeout 60 tcpdump -ni any -s 0 -B 4096 -w /var/tmp/incident.pcap \
  'host 203.0.113.10 and (tcp port 443 or icmp)'

sudo tcpdump -nn -tttt -r /var/tmp/incident.pcap 'tcp[tcpflags] & (tcp-syn|tcp-rst|tcp-fin) != 0'
```

For TLS/application incidents capture metadata rather than payload where possible. Define retention and access controls for PCAPs because they may contain credentials or personal data.
