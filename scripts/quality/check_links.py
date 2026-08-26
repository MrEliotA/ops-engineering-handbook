#!/usr/bin/env python3
import argparse, re
from pathlib import Path
pat=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.'); a=ap.parse_args(); root=Path(a.root); bad=[]
    for p in root.rglob('*.md'):
        for link in pat.findall(p.read_text(encoding='utf-8')):
            if link.startswith(('http://','https://','mailto:','#','sandbox:')): continue
            target=(p.parent/link.split('#',1)[0]).resolve()
            if not target.exists(): bad.append((str(p.relative_to(root)),link))
    if bad:
        for f,l in bad: print(f'{f}: broken link {l}')
        raise SystemExit(1)
    print('links: ok')
if __name__=='__main__': main()
