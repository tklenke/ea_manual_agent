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
    from wikicheck.orphan_pages import find_orphan_pages, check_structural_pages
    from wikicheck.broken_links import find_broken_links, find_system_links

    stats = compute_stats(FIXTURE_WR, log_path, today="2026-04-16")
    log = parse_review_log(log_path)
    summary = format_report(stats, today="2026-04-16", log_last_updated=log.last_updated)

    broken = find_broken_links(FIXTURE_WR)
    system = find_system_links(FIXTURE_WR)
    orphans = find_orphan_pages(FIXTURE_WR)
    structural_found, structural_missing = check_structural_pages(FIXTURE_WR)
    wr_slugs = set(glob_wr_pages(FIXTURE_WR))
    log_slugs = {e.slug for e in log.entries}
    pending = sorted(e.slug for e in log.entries if e.status == "Pending")
    unreviewed = sorted(e.slug for e in log.entries if e.status == "unreviewed")
    missing = sorted(wr_slugs - log_slugs)
    detail = format_detail(
        broken_links=broken,
        pending=pending,
        unreviewed=unreviewed,
        missing_from_log=missing,
        orphan_pages=orphans,
        structural_pages_found=structural_found,
        structural_pages_missing=structural_missing,
        system_links=system,
    )
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


def test_e2e_orphan_count_in_summary():
    summary, _ = _run_with_fixtures(FIXTURE_LOG)
    # fixture: page-a and page-c are orphans (page-b is linked from page-a)
    assert "Orphan pages:             2" in summary


def test_e2e_detail_shows_orphan_slugs():
    _, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "page-a" in detail
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


def test_e2e_structural_pages_in_summary():
    summary, _ = _run_with_fixtures(FIXTURE_LOG)
    assert "Structural pages:" in summary


def test_e2e_structural_pages_in_detail():
    _, detail = _run_with_fixtures(FIXTURE_LOG)
    assert "Structural pages (excluded from orphans):" in detail


def _run_missing_log_detail(fixture_wr, tmp_path):
    from wikicheck.broken_links import find_broken_links
    from wikicheck.orphan_pages import find_orphan_pages, check_structural_pages
    from wikicheck.seed_log import seed_review_log
    from wikicheck.report import format_missing_log_report, format_detail
    from wikicheck.broken_links import find_system_links

    broken = find_broken_links(fixture_wr)
    system = find_system_links(fixture_wr)
    orphans = find_orphan_pages(fixture_wr)
    structural_found, structural_missing = check_structural_pages(fixture_wr)
    seed_path = tmp_path / "review_log.md"
    seed_review_log(fixture_wr, tmp_path, today="2026-04-16")
    summary = format_missing_log_report(
        total_pages=3,
        broken_link_count=len(broken),
        system_link_count=len(system),
        system_links=system,
        structural_pages_found=structural_found,
        structural_pages_missing=structural_missing,
        today="2026-04-16",
        seed_path=str(seed_path),
    )
    detail = format_detail(
        broken_links=broken,
        pending=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=orphans,
        structural_pages_found=structural_found,
        structural_pages_missing=structural_missing,
        system_links=system,
    )
    return summary, detail


def test_e2e_missing_log_detail_shows_real_orphans(tmp_path):
    _, detail = _run_missing_log_detail(FIXTURE_WR, tmp_path)
    # fixture has page-a and page-c as orphans (page-b is linked from page-a)
    assert "page-a" in detail
    assert "page-c" in detail


FIXTURE_LOG_WITH_PENDING = Path(__file__).parent / "fixtures" / "review_log_with_pending.md"


def test_e2e_pending_count_in_summary():
    # fixture log: page-a=Pending, page-b=unreviewed; page-c missing from log
    summary, _ = _run_with_fixtures(FIXTURE_LOG_WITH_PENDING)
    assert "Pending pages:            1" in summary


def test_e2e_pending_slug_in_detail():
    _, detail = _run_with_fixtures(FIXTURE_LOG_WITH_PENDING)
    assert "Pending pages:" in detail
    assert "  page-a" in detail


def test_e2e_pending_not_in_missing_from_log():
    # page-a is Pending (in log), page-c is missing from log — missing count must be 1, not 2
    summary, _ = _run_with_fixtures(FIXTURE_LOG_WITH_PENDING)
    assert "Pages missing from log:   1" in summary
