# ABOUTME: CLI entry point for wikiCheck — checks WR integrity and AR review log status.
# ABOUTME: Prints a compact summary report; use --detail for full broken/unreviewed/missing lists.

import argparse
from datetime import date
from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages
from wikicheck.broken_links import find_broken_links
from wikicheck.orphan_pages import find_orphan_pages, check_structural_pages
from wikicheck.review_log import parse_review_log
from wikicheck.seed_log import seed_review_log
from wikicheck.stats import compute_stats
from wikicheck.report import format_report, format_missing_log_report, format_detail

WR_DIR = Path("/home/tom/projects/N657CZDashTwo")
_SCRIPT_DIR = Path(__file__).parent
LOG_PATH = _SCRIPT_DIR / "../../docs/notes/review_log.md"
DATA_DIR = _SCRIPT_DIR / "data"


def main():
    parser = argparse.ArgumentParser(description="Check WR integrity and AR review log.")
    parser.add_argument("--detail", action="store_true", help="Show full lists of broken links, unreviewed, and missing pages.")
    args = parser.parse_args()

    today = date.today().isoformat()
    log_path = LOG_PATH.resolve()

    if not log_path.exists():
        DATA_DIR.mkdir(exist_ok=True)
        broken = find_broken_links(WR_DIR)
        total = len(glob_wr_pages(WR_DIR))
        structural_found, structural_missing = check_structural_pages(WR_DIR)
        seed_path = DATA_DIR / "review_log.md"
        seed_review_log(WR_DIR, DATA_DIR, today=today)
        print(format_missing_log_report(
            total_pages=total,
            broken_link_count=len(broken),
            structural_pages_found=structural_found,
            structural_pages_missing=structural_missing,
            today=today,
            seed_path=str(seed_path),
        ))
        if args.detail:
            orphans = find_orphan_pages(WR_DIR)
            print()
            print(format_detail(
                broken_links=broken,
                unreviewed=[],
                missing_from_log=[],
                orphan_pages=orphans,
                structural_pages_found=structural_found,
                structural_pages_missing=structural_missing,
            ))
        return

    stats = compute_stats(WR_DIR, log_path, today=today)
    log = parse_review_log(log_path)
    print(format_report(stats, today=today, log_last_updated=log.last_updated))

    if args.detail:
        broken = find_broken_links(WR_DIR)
        orphans = find_orphan_pages(WR_DIR)
        structural_found, structural_missing = check_structural_pages(WR_DIR)
        wr_slugs = set(glob_wr_pages(WR_DIR))
        log_slugs = {e.slug for e in log.entries}
        unreviewed = sorted(e.slug for e in log.entries if e.status == "unreviewed")
        missing = sorted(wr_slugs - log_slugs)
        print()
        print(format_detail(
            broken_links=broken,
            unreviewed=unreviewed,
            missing_from_log=missing,
            orphan_pages=orphans,
            structural_pages_found=structural_found,
            structural_pages_missing=structural_missing,
        ))


if __name__ == "__main__":
    main()
