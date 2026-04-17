# ABOUTME: Detects orphan pages in the WR — pages that exist but are never linked to.
# ABOUTME: A page is an orphan if its slug appears in known pages but not in any link target.

from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages
from wikicheck.broken_links import collect_referenced_slugs

STRUCTURAL_PAGES = ["home", "readme"]


def find_orphan_pages(wr_dir: Path) -> list[str]:
    known = set(glob_wr_pages(wr_dir))
    referenced = collect_referenced_slugs(wr_dir)
    structural = {s.lower() for s in STRUCTURAL_PAGES}
    return sorted(slug for slug in known - referenced if slug.lower() not in structural)


def check_structural_pages(wr_dir: Path) -> tuple[list[str], list[str]]:
    known_lower = {slug.lower() for slug in glob_wr_pages(wr_dir)}
    found = sorted(s for s in STRUCTURAL_PAGES if s in known_lower)
    missing = sorted(s for s in STRUCTURAL_PAGES if s not in known_lower)
    return found, missing
