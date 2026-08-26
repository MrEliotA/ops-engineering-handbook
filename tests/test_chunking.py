from scripts.rag.ingest_markdown import chunks

def test_chunks_preserve_content():
    text='# A\n'+'x'*80+'\n## B\n'+'y'*80
    out=list(chunks(text,max_chars=100))
    assert len(out)>=2
    assert '## B' in '\n'.join(out)
