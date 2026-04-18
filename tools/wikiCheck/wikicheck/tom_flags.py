# ABOUTME: Finds @@TOM flags in WR markdown files.
# ABOUTME: Returns pages containing flags and total flag count.

import re
from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages

_TOM_FLAG = re.compile(r'@@TOM\b')


def find_tom_flags(wr_dir: Path) -> list[str]:
    pages = []
    for slug in glob_wr_pages(wr_dir):
        text = (wr_dir / f"{slug}.md").read_text()
        if _TOM_FLAG.search(text):
            pages.append(slug)
    return sorted(pages)


def count_tom_flags(wr_dir: Path) -> int:
    total = 0
    for slug in glob_wr_pages(wr_dir):
        text = (wr_dir / f"{slug}.md").read_text()
        total += len(_TOM_FLAG.findall(text))
    return total
