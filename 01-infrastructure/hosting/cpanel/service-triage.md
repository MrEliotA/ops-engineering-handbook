---
title: "cPanel Service Triage"
category: "hosting"
tags:
  - cpanel
  - whm
  - hosting
  - service
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# cPanel Service Triage

Prefer cPanel-supported interfaces over editing generated configuration directly.

```bash
/usr/local/cpanel/bin/whmapi1 servicestatus service=exim
/usr/local/cpanel/bin/whmapi1 servicestatus service=httpd
/usr/local/cpanel/bin/whmapi1 servicestatus service=mysql
/usr/local/cpanel/scripts/restartsrv_httpd --status
/usr/local/cpanel/scripts/restartsrv_exim --status
```

Capture account/UID attribution, Apache/LiteSpeed workers, PHP-FPM pool state, MySQL workload and mail queue state before broad restarts.
