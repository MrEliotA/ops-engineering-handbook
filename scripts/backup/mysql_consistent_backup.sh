#!/usr/bin/env bash
set -euo pipefail
: "${MYSQL_DATABASE:?set MYSQL_DATABASE}"
out=${1:-"backup-${MYSQL_DATABASE}-$(date -u +%Y%m%dT%H%M%SZ).sql.gz"}
# For transactional workloads. Review options for routines/events/GTID and non-InnoDB tables.
mysqldump --single-transaction --quick --routines --events --triggers --hex-blob --databases "$MYSQL_DATABASE" | gzip -1 > "$out"
gzip -t "$out"
sha256sum "$out" > "$out.sha256"
echo "$out"
