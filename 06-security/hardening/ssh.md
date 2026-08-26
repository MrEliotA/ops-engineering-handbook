---
title: "SSH Hardening"
category: "security"
tags:
  - ssh
  - hardening
  - authentication
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: true
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# SSH Hardening

Treat SSH configuration as policy: strong key-based auth, explicit user/group access, controlled forwarding, audited privilege escalation, and emergency access procedures.

Validate before reload:

```bash
sshd -T > /var/tmp/sshd-effective.txt
sshd -t
systemctl reload sshd
```

Keep an existing authenticated session open while validating a remote change. Test the exact intended authentication path before closing fallback access.
