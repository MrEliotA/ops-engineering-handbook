---
title: "PHP-FPM Pool Saturation"
category: "web"
tags:
  - php-fpm
  - hosting
  - latency
  - capacity
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# PHP-FPM Pool Saturation

Symptoms such as `server reached pm.max_children`, rising request latency and a full listen queue indicate capacity pressure, but increasing `pm.max_children` without memory math can convert queueing into host-wide OOM pressure.

```bash
systemctl status php-fpm --no-pager
journalctl -u php-fpm --since '-20 min' --no-pager
grep -R "^pm\.\|^request_slowlog_timeout\|^slowlog" /etc/php-fpm.d /etc/php/*/fpm/pool.d 2>/dev/null
ps -C php-fpm -o pid,ppid,rss,%mem,%cpu,etimes,args --sort=-rss
```

Estimate realistic worker RSS distribution, account for shared memory carefully, leave headroom for kernel/cache/database, then test queue and latency under load. Enable slow logs for attribution rather than only enlarging pools.
