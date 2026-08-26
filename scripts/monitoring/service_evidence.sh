#!/usr/bin/env bash
set -euo pipefail
unit=${1:?usage: service_evidence.sh UNIT [OUTDIR]}
out=${2:-"evidence/${unit//\//_}-$(date -u +%Y%m%dT%H%M%SZ)"}
mkdir -p "$out"
systemctl show "$unit" -p Id -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus -p NRestarts -p ControlGroup -p MemoryCurrent -p TasksCurrent > "$out/systemctl-show.txt" || true
systemctl cat "$unit" > "$out/unit.txt" 2>&1 || true
journalctl -u "$unit" --since '-30 min' -o short-iso-precise --no-pager > "$out/journal.txt" 2>&1 || true
printf '%s\n' "$out"
