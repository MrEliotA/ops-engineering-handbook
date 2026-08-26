---
title: "Service Down Runbook"
category: "runbook"
tags:
  - service
  - systemd
  - incident
status: "approved"
audience: "senior"
risk: "medium"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Service Down Runbook

```bash
unit="$1"
systemctl show "$unit" -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts
journalctl -u "$unit" --since '-30 min' -o short-iso-precise --no-pager
systemctl list-dependencies --reverse "$unit" --no-pager
```

Determine whether failure is local process crash, dependency failure, port conflict, resource exhaustion, configuration error or external dependency. Validate configuration before restart when the service supports it. Verify from a client path after recovery.
