#!/usr/bin/env bash
set -euo pipefail
hosts=${1:?hosts file}
shift
(( $# )) || { echo "command required" >&2; exit 2; }
max=${MAX_PARALLEL:-5}
# Designed for read-only evidence commands. Host keys and auth policy remain external.
xargs -r -P "$max" -I{} sh -c 'h="$1"; shift; echo "### $h"; timeout 30 ssh -o BatchMode=yes -- "$h" "$@"' _ {} "$@" < "$hosts"
