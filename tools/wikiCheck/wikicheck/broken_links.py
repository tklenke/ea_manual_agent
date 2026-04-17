# ABOUTME: Detects broken internal links across the WR by cross-referencing slugs against .md files.
# ABOUTME: Returns a sorted, deduplicated list of slugs that have no corresponding page.

from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages
from wikicheck.link_parser import extract_links


def collect_referenced_slugs(wr_dir: Path) -> set[str]:
    referenced = set()
    for md_file in Path(wr_dir).glob("*.md"):
        for slug in extract_links(md_file.read_text()):
            referenced.add(slug)
    return referenced


def find_broken_links(wr_dir: Path) -> list[str]:
    known = set(glob_wr_pages(wr_dir))
    referenced = {s for s in collect_referenced_slugs(wr_dir) if not s.startswith("/-/")}
    return sorted(referenced - known)
