#!/usr/bin/env python3
import argparse, json, urllib.parse, urllib.request
p=argparse.ArgumentParser(); p.add_argument('--url',required=True); p.add_argument('--query',action='append',required=True); a=p.parse_args()
out={}
for q in a.query:
    u=a.url.rstrip('/')+'/api/v1/query?'+urllib.parse.urlencode({'query':q})
    with urllib.request.urlopen(u, timeout=15) as r: out[q]=json.load(r)
print(json.dumps(out,indent=2))
