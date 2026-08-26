---
title: "systemd Service Forensics"
category: "systemd"
tags:
  - systemd
  - journal
  - service
  - cgroup
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# systemd Service Forensics

```bash
unit=nginx.service
systemctl show "$unit" -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus \
  -p NRestarts -p Restart -p MemoryCurrent -p TasksCurrent -p ControlGroup
journalctl -u "$unit" --since '-30 min' --no-pager -o short-iso-precise
systemctl cat "$unit"
systemd-analyze critical-chain "$unit"
```

Repeated restarts can erase the original failure signal. Capture `Result`, exit status, previous logs, dependency failures and overrides before restarting manually.
