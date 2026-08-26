#!/usr/bin/env bash
set -euo pipefail
out=${1:-"evidence/host-$(hostname -s)-$(date -u +%Y%m%dT%H%M%SZ)"}
mkdir -p "$out"
run(){ local n=$1; shift; { echo "+ $*"; "$@"; } >"$out/$n.txt" 2>&1 || true; }
run timestamp date -u +%FT%TZ
run uname uname -a
run uptime uptime
run load cat /proc/loadavg
run vmstat vmstat -w 1 10
run psi sh -c 'for f in /proc/pressure/*; do echo "### $f"; cat "$f"; done'
run processes ps -eo pid,ppid,user,uid,stat,cls,pri,ni,psr,%cpu,%mem,rss,vsz,etimes,wchan:32,cgroup:60,args --sort=-%cpu
run threads ps -eLo pid,lwp,ppid,user,psr,stat,pri,ni,%cpu,wchan:32,comm --sort=-%cpu
run sockets ss -s
run routes ip route show table all
run links ip -s link
run disk df -hT
run inodes df -ih
command -v iostat >/dev/null && run iostat iostat -xmdz 1 10
printf '%s\n' "$out"
