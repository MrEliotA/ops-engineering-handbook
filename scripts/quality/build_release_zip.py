#!/usr/bin/env python3
import argparse, hashlib, zipfile
from pathlib import Path
EXCLUDE={'.git','.venv','__pycache__','.pytest_cache','.ruff_cache'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--output',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); out=Path(a.output).resolve()
    files=[p for p in root.rglob('*') if p.is_file() and not any(x in p.parts for x in EXCLUDE) and p.resolve()!=out]
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(files):
            zi=zipfile.ZipInfo(str(Path(root.name)/p.relative_to(root))); zi.date_time=(2026,8,24,0,0,0); zi.external_attr=(p.stat().st_mode & 0xFFFF)<<16
            z.writestr(zi,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    print(out); print(hashlib.sha256(out.read_bytes()).hexdigest())
if __name__=='__main__': main()
