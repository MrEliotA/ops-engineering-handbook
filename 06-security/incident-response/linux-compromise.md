---
title: "Linux Compromise Triage"
category: "security"
tags:
  - incident-response
  - linux
  - forensics
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Linux Compromise Triage

Prioritize evidence preservation and containment decisions. Avoid destructive cleanup before collecting volatile state.

```bash
date -u +%FT%TZ
uname -a
who -a
ss -plantu
ps -eo pid,ppid,user,lstart,etimes,stat,cgroup:60,args --sort=etimes
systemctl list-units --type=service --state=running --no-pager
journalctl --since '-2h' -o short-iso-precise --no-pager > /var/tmp/journal-2h.txt
```

Capture hashes and metadata of suspicious artifacts. If credential theft is plausible, rotate secrets from a trusted system after containment, not from the suspected host.
