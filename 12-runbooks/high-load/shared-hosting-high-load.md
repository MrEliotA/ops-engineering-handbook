---
title: "Shared Hosting High Load Runbook"
category: "runbook"
tags:
  - hosting
  - high-load
  - cpanel
  - directadmin
  - mysql
  - php-fpm
status: "approved"
audience: "senior"
risk: "medium"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Shared Hosting High Load Runbook

## 1. Freeze the timeline

```bash
date -u +%FT%TZ
uptime
cat /proc/loadavg
cat /proc/pressure/{cpu,memory,io}
vmstat -w 1 10
iostat -xmdz 1 10
```

## 2. Attribute work

```bash
ps -eo pid,ppid,user,uid,stat,cls,pri,ni,%cpu,%mem,rss,etimes,wchan:28,cgroup:55,args --sort=-%cpu | head -80
ps -eLo pid,lwp,ppid,user,psr,stat,%cpu,wchan:28,comm --sort=-%cpu | head -120
```

Correlate UID/account with web requests, PHP-FPM pools, cron jobs, mail and MySQL sessions/digests. Do not kill the top process solely because it is top.

## 3. Determine the pressure class
- CPU: CPU PSI/run queue/per-core saturation.
- Memory: memory PSI, reclaim, swap, OOM events.
- I/O: I/O PSI, device latency, blocked tasks.
- Database: statement digests, locks, transaction age.
- Web/PHP: request latency, pool queues, slow logs.

## 4. Remediation hierarchy
1. stop or rate-limit the identified abusive/accidental workload,
2. fix pathological query/request/job,
3. adjust concurrency only after capacity math,
4. scale resources when sustained legitimate demand exceeds capacity.

## 5. Verify
Repeat the exact evidence set and confirm user-facing latency/error recovery, not only reduced load average.
