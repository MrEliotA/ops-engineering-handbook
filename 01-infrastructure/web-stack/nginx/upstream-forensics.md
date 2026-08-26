---
title: "Nginx Upstream Forensics"
category: "web"
tags:
  - nginx
  - upstream
  - latency
  - http
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Nginx Upstream Forensics

Separate client/network latency from upstream application latency. Log upstream timing fields temporarily if absent: `$request_time`, `$upstream_connect_time`, `$upstream_header_time`, `$upstream_response_time`, upstream address/status and request ID.

```bash
nginx -T >/var/tmp/nginx-config.txt 2>&1
ss -lntp | grep -E ':80|:443'
journalctl -u nginx --since '-30 min' -o short-iso-precise --no-pager
```

A fast upstream response with large total request time suggests client transfer or buffering effects; a slow upstream header time points closer to application or database execution.
