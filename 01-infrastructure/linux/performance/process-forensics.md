---
title: "Linux Process and Scheduler Forensics"
category: "linux"
tags:
  - linux
  - process
  - scheduler
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

# Linux Process and Scheduler Forensics

## Goal
Attribute CPU/run-queue pressure to processes, threads, cgroups, scheduling classes, and wait channels before changing priorities or killing work.

## High-value snapshots

```bash
ps -eo pid,ppid,user,uid,stat,cls,rtprio,pri,ni,psr,%cpu,%mem,rss,vsz,etimes,wchan:32,cgroup:60,args \
  --sort=-%cpu | sed -n '1,80p'

ps -eLo pid,lwp,ppid,user,psr,stat,cls,rtprio,pri,ni,%cpu,wchan:32,comm \
  --sort=-%cpu | sed -n '1,120p'

pidstat -urdwt -h -p ALL 2 5
```

Interpret `R` with run-queue saturation differently from `D`, which often points to uninterruptible waits. A single high-CPU thread inside a low-CPU process aggregate can be exposed by the LWP view.

## Scheduler and pressure context

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
vmstat -w 1 10
mpstat -P ALL 1 5
```

Use PSI `some`/`full` trends to distinguish contention from merely high utilization. `full` CPU pressure is normally absent because at least one runnable task can execute, while memory/I/O full stalls can be highly significant.

## Cgroup attribution

```bash
systemctl show php-fpm.service -p ControlGroup -p CPUUsageNSec -p MemoryCurrent -p TasksCurrent
cg=$(systemctl show php-fpm.service -p ControlGroup --value)
for f in cpu.pressure memory.pressure io.pressure cpu.stat memory.events memory.current; do
  [ -r "/sys/fs/cgroup${cg}/$f" ] && { echo "### $f"; cat "/sys/fs/cgroup${cg}/$f"; }
done
```

Do not change nice/CPU quota until you know whether the workload is CPU-bound or waiting on memory/I/O.
