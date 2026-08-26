---
title: "Linux I/O Forensics"
category: "storage"
tags:
  - linux
  - io
  - storage
  - iostat
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Linux I/O Forensics

```bash
iostat -xmdz 1 10
pidstat -d -h -p ALL 2 5
cat /proc/pressure/io
lsblk -o NAME,KNAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,ROTA,DISC-MAX,DISC-GRAN
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Do not diagnose from `%util` alone on modern parallel devices. Compare `await`, queue depth, throughput, service concurrency, PSI, and application latency. For device-mapper/LVM stacks inspect both logical and physical devices.

For filesystem saturation capture inode and block availability separately:

```bash
df -hT
df -ih
```
