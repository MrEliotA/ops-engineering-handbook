#!/usr/bin/env bash
set -euo pipefail
out=${1:-"evidence/firewall-$(date -u +%Y%m%dT%H%M%SZ)"}
mkdir -p "$out"
nft -a list ruleset > "$out/nft.txt" 2>&1 || true
nft -j list ruleset > "$out/nft.json" 2>&1 || true
sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_max > "$out/conntrack-sysctl.txt" 2>&1 || true
conntrack -S > "$out/conntrack-stats.txt" 2>&1 || true
ss -s > "$out/ss-summary.txt" 2>&1 || true
printf '%s\n' "$out"
