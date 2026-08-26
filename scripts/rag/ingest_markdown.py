#!/usr/bin/env python3
"""Reference heading-aware ingestion for OpenAI embeddings + Qdrant.
Install optional dependencies: pip install '.[rag]'.
"""
import argparse, hashlib, os, re
from pathlib import Path

def chunks(text, max_chars=6000):
    parts=re.split(r'(?=^#{1,4} )', text, flags=re.M)
    buf=''
    for part in parts:
        if len(buf)+len(part)>max_chars and buf.strip(): yield buf.strip(); buf=''
        buf+=part
    if buf.strip(): yield buf.strip()

def main():
    from openai import OpenAI
    from qdrant_client import QdrantClient, models
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--collection',default=os.getenv('QDRANT_COLLECTION','engineering_handbook')); a=ap.parse_args()
    oc=OpenAI(); qc=QdrantClient(url=os.getenv('QDRANT_URL','http://127.0.0.1:6333'), api_key=os.getenv('QDRANT_API_KEY') or None)
    model=os.getenv('EMBEDDING_MODEL','text-embedding-3-small'); dim=1536
    if not qc.collection_exists(a.collection): qc.create_collection(a.collection, vectors_config=models.VectorParams(size=dim,distance=models.Distance.COSINE))
    pts=[]
    for p in Path(a.root).rglob('*.md'):
        if '.github' in p.parts: continue
        text=p.read_text(encoding='utf-8'); rel=str(p.relative_to(a.root))
        for i,c in enumerate(chunks(text)):
            vec=oc.embeddings.create(model=model,input=c).data[0].embedding
            pid=int(hashlib.sha256(f'{rel}:{i}:{c}'.encode()).hexdigest()[:15],16)
            pts.append(models.PointStruct(id=pid,vector=vec,payload={'path':rel,'chunk':i,'text':c}))
            if len(pts)>=32: qc.upsert(a.collection,points=pts); pts=[]
    if pts: qc.upsert(a.collection,points=pts)
if __name__=='__main__': main()
