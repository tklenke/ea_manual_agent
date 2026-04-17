# ABOUTME: End-to-end tests using fixture WR directory and review log.
# ABOUTME: Covers broken links, unreviewed, missing pages, and missing log scenarios.

import subprocess
from pathlib import Path

VENV_PYTHON = Path(__file__).parent.parent / "venv" / "bin" / "python3"
SCRIPT = Path(__file__).parent.parent / "wiki_check.py"

FIXTURE_WR = Path(__file__).parent / "fixtures" / "wr"
FIXTURE_LOG = Path(__file__).parent / "fixtures" / "review_log.md"


def _run_with_fixtures(log_path, *extra_args):
    """Run wiki_check.py with patched paths via env override — not possible without modifying the script.
    Instead, import the modules directly and test the pipeline end-to-end."""
    from wikicheck.wr_pages import glob_wr_pages
    from wikicheck.broken_links import find_broken_links
    from wikicheck.review_log import parse_review_log
    from wikicheck.stats import compute_stats
    from wikicheck.report import format_report, format_detail

    stats = compute_stats(FIXTURE_WR, log_path, today="2026-04-16")
    log = parse_review_log(log_path)
    summary = format_report(stats, today="2026-04-16", log_last_updated=log.last_updated)
    broken = find_broken_links(FIXTURE_WR)
    wr_slugs = set(glob_wr_pages(FIXTURE_WR))
    log_slugs = {e.slug for e in log.entries}
    unreviewed = sorted(e.slug for e in log.entries if e.status == "unreviewed")
    missing = sorted(wr_slugs - log_slugs)
    detail = format_detail(broken_links=broken, unreviewed=unreviewed, missing_from_log=missing)
    return summary, detail


def test_e2e_broken_links_detected():
    summary, detail = _run_with_fixtures(FIXTURE_LOG)
    # fixture has one broken link: ghost-page
    assert "Broken links:            1" in summary


def test_e2e_unreviewed_detected():
    summary, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "Unreviewed pages:         1" in summary


def test_e2e_missing_from_log_detected():
    summary, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "Pages missing from log:   1" in summary


def test_e2e_detail_shows_broken_link_slug():
    _, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "ghost-page" in detail


def test_e2e_detail_shows_unreviewed_slug():
    _, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "page-b" in detail


def test_e2e_detail_shows_missing_slug():
    _, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "page-c" in detail


def test_e2e_missing_log_seeds_file(tmp_path):
    from wikicheck.seed_log import seed_review_log
    seed_review_log(FIXTURE_WR, tmp_path, today="2026-04-16")
    out = tmp_path / "review_log.md"
    assert out.exists()
    content = out.read_text()
    assert "page-a" in content
    assert "page-b" in content
    assert "page-c" in content
    assert "unreviewed" in content
