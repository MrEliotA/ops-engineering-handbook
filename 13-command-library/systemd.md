---
title: "Command Library: systemd"
category: "command-library"
tags:
  - systemd
  - journalctl
  - commands
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# systemd Commands

```bash
systemctl show nginx.service -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts -p ControlGroup
journalctl -u nginx.service --since '-30 min' -o short-iso-precise --no-pager
systemd-analyze critical-chain nginx.service
```
