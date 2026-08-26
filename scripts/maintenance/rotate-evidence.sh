#!/usr/bin/env bash
set -euo pipefail
dir=${1:-evidence}
days=${RETENTION_DAYS:-14}
[ -d "$dir" ] || exit 0
find "$dir" -xdev -type f -mtime "+$days" -print -delete
find "$dir" -xdev -type d -empty -delete
