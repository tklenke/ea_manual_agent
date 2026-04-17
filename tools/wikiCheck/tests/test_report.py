# ABOUTME: Tests for summary report formatting — both normal and missing-log cases.
# ABOUTME: Validates exact output format matching the design spec.

from wikicheck.report import format_report, format_missing_log_report
from wikicheck.stats import Stats


def test_format_normal_report():
    stats = Stats(
        total_pages=47,
        broken_link_count=12,
        orphan_count=5,
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
        approved_count=36,
        unreviewed_count=8,
        missing_from_log_count=3,
        log_age_days=6,
    )
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-10")
    assert output == (
        "Wiki Integrity Report — 2026-04-16\n"
        "Total WR pages:          47\n"
        "Broken links:            12  (pages referenced but not yet written)\n"
        "Orphan pages:             5  (exist in WR, never linked to)\n"
        "Structural pages:         2  (home, readme — excluded from orphans)\n"
        "Approved pages:          36  (of 47 in log)\n"
        "Unreviewed pages:         8  (in log, never reviewed)\n"
        "Pages missing from log:   3  (in WR, not in log)\n"
        "Review log last updated: 2026-04-10 (6 days ago)"
    )


def test_orphan_line_appears_between_broken_links_and_approved():
    stats = Stats(
        total_pages=10,
        broken_link_count=1,
        orphan_count=2,
        structural_pages_found=["home"],
        structural_pages_missing=["readme"],
        approved_count=5,
        unreviewed_count=0,
        missing_from_log_count=0,
        log_age_days=0,
    )
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    broken_pos = output.index("Broken links:")
    orphan_pos = output.index("Orphan pages:")
    approved_pos = output.index("Approved pages:")
    assert broken_pos < orphan_pos < approved_pos


def test_structural_pages_line_in_report():
    stats = Stats(
        total_pages=10,
        broken_link_count=0,
        orphan_count=0,
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
        approved_count=5,
        unreviewed_count=0,
        missing_from_log_count=0,
        log_age_days=0,
    )
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "Structural pages:         2  (home, readme — excluded from orphans)" in output


def test_structural_pages_error_line_in_report():
    stats = Stats(
        total_pages=10,
        broken_link_count=0,
        orphan_count=0,
        structural_pages_found=["home"],
        structural_pages_missing=["readme"],
        approved_count=5,
        unreviewed_count=0,
        missing_from_log_count=0,
        log_age_days=0,
    )
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "ERROR: Structural page not in WR: readme" in output


def test_no_structural_error_line_when_all_found():
    stats = Stats(
        total_pages=10,
        broken_link_count=0,
        orphan_count=0,
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
        approved_count=5,
        unreviewed_count=0,
        missing_from_log_count=0,
        log_age_days=0,
    )
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "ERROR:" not in output


def test_format_missing_log_report():
    output = format_missing_log_report(
        total_pages=47,
        broken_link_count=12,
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
        today="2026-04-16",
        seed_path="tools/wikiCheck/data/review_log.md",
    )
    assert output == (
        "Wiki Integrity Report — 2026-04-16\n"
        "Total WR pages:          47\n"
        "Broken links:            12  (pages referenced but not yet written)\n"
        "Structural pages:         2  (home, readme — excluded from orphans)\n"
        "Review log:              NOT FOUND — seeded template written to\n"
        "                         tools/wikiCheck/data/review_log.md\n"
        "                         move to: docs/notes/review_log.md"
    )


def test_missing_log_report_structural_error_line():
    output = format_missing_log_report(
        total_pages=10,
        broken_link_count=0,
        structural_pages_found=["home"],
        structural_pages_missing=["readme"],
        today="2026-04-16",
        seed_path="tools/wikiCheck/data/review_log.md",
    )
    structural_pos = output.index("Structural pages:")
    error_pos = output.index("ERROR: Structural page not in WR: readme")
    review_log_pos = output.index("Review log:")
    assert structural_pos < error_pos < review_log_pos
