---
title: "Push to GitHub"
category: "meta"
tags:
  - git
  - github
  - release
status: "approved"
audience: "senior"
risk: "read-only"
last_reviewed: "2026-08-24"
rag:
  index: false
  chunk_strategy: "heading-aware"
  source_priority: "handbook"
---

# Push to GitHub

Create an empty GitHub repository, then from the extracted `engineering-handbook` directory:

```bash
git init
git branch -M main
git add .
git status
git diff --cached --stat
git commit -m "Initial production engineering handbook"
git remote add origin git@github.com:YOUR_USERNAME/engineering-handbook.git
git push -u origin main
```

Before the first push, review `.github/CODEOWNERS` and replace the commented example with your real GitHub username if you plan to enforce CODEOWNERS review.

Do not commit `.env`, production inventory, private keys, credentials, customer data, or raw incident evidence containing secrets/PII.
