#!/usr/bin/env python3
import argparse
from pathlib import Path
REQUIRED={'title','category','tags','status','audience','risk','last_reviewed','rag'}
IGNORED={'.github','.pytest_cache','.ruff_cache','.venv','__pycache__'}
def parse_keys(text):
    if not text.startswith('---\n'): return set()
    end=text.find('\n---\n',4)
    if end<0: return set()
    keys=set()
    for line in text[4:end].splitlines():
        if line and not line[0].isspace() and ':' in line: keys.add(line.split(':',1)[0].strip())
    return keys
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.'); a=ap.parse_args(); root=Path(a.root); bad=[]
    for p in root.rglob('*.md'):
        rel=p.relative_to(root)
        if any(part in IGNORED for part in rel.parts): continue
        keys=parse_keys(p.read_text(encoding='utf-8'))
        miss=REQUIRED-keys
        if miss: bad.append((str(rel),sorted(miss)))
    if bad:
        for f,m in bad: print(f'{f}: missing {", ".join(m)}')
        raise SystemExit(1)
    print('frontmatter: ok')
if __name__=='__main__': main()
