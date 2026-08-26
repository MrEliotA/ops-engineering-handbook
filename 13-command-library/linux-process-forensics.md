---
title: "Command Library: Linux Process Forensics"
category: "command-library"
tags:
  - linux
  - process
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

# Linux Process Forensics

```bash
ps -eo pid,ppid,user,uid,stat,cls,rtprio,pri,ni,psr,%cpu,%mem,rss,vsz,etimes,wchan:32,cgroup:60,args --sort=-%cpu | sed -n '1,80p'
ps -eLo pid,lwp,ppid,user,psr,stat,pri,ni,%cpu,wchan:32,comm --sort=-%cpu | sed -n '1,120p'
pidstat -urdwt -h -p ALL 2 5
```
