#!/usr/bin/env python3
import argparse, hashlib
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('file'); p.add_argument('--sha256'); a=p.parse_args()
f=Path(a.file); h=hashlib.sha256(f.read_bytes()).hexdigest(); print(h)
if a.sha256 and h.lower()!=a.sha256.lower(): raise SystemExit('checksum mismatch')
