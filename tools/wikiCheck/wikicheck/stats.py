# ABOUTME: Computes wikiCheck statistics from WR directory and review log.
# ABOUTME: Returns a Stats dataclass with all seven report fields.

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages
from wikicheck.broken_links import find_broken_links
from wikicheck.orphan_pages import find_orphan_pages, check_structural_pages
from wikicheck.review_log import parse_review_log


@dataclass
class Stats:
    total_pages: int
    broken_link_count: int
    orphan_count: int
    structural_pages_found: list[str]
    structural_pages_missing: list[str]
    approved_count: int
    unreviewed_count: int
    missing_from_log_count: int
    log_age_days: int


def compute_stats(wr_dir: Path, log_path: Path, today: str) -> Stats:
    slugs = set(glob_wr_pages(wr_dir))
    broken = find_broken_links(wr_dir)
    orphans = find_orphan_pages(wr_dir)
    structural_found, structural_missing = check_structural_pages(wr_dir)
    log = parse_review_log(log_path)

    log_slugs = {e.slug for e in log.entries}
    approved = sum(1 for e in log.entries if e.status == "Approved")
    unreviewed = sum(1 for e in log.entries if e.status == "unreviewed")
    missing = len(slugs - log_slugs)

    last_updated = date.fromisoformat(log.last_updated)
    age = (date.fromisoformat(today) - last_updated).days

    return Stats(
        total_pages=len(slugs),
        broken_link_count=len(broken),
        orphan_count=len(orphans),
        structural_pages_found=structural_found,
        structural_pages_missing=structural_missing,
        approved_count=approved,
        unreviewed_count=unreviewed,
        missing_from_log_count=missing,
        log_age_days=age,
    )
