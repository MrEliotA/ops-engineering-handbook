from scripts.quality import check_links

def test_link_regex():
    assert check_links.pat.findall('[x](a.md)') == ['a.md']
