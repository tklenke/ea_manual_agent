# ABOUTME: Tests for summary report formatting — both normal and missing-log cases.
# ABOUTME: Validates exact output format matching the design spec.

from wikicheck.report import format_report, format_missing_log_report
from wikicheck.stats import Stats


def test_format_normal_report():
    stats = Stats(
        total_pages=47,
        broken_link_count=12,
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
        "Approved pages:          36  (of 47 in log)\n"
        "Unreviewed pages:         8  (in log, never reviewed)\n"
        "Pages missing from log:   3  (in WR, not in log)\n"
        "Review log last updated: 2026-04-10 (6 days ago)"
    )


def test_format_missing_log_report():
    output = format_missing_log_report(
        total_pages=47,
        broken_link_count=12,
        today="2026-04-16",
        seed_path="tools/wikiCheck/data/review_log.md",
    )
    assert output == (
        "Wiki Integrity Report — 2026-04-16\n"
        "Total WR pages:          47\n"
        "Broken links:            12  (pages referenced but not yet written)\n"
        "Review log:              NOT FOUND — seeded template written to\n"
        "                         tools/wikiCheck/data/review_log.md\n"
        "                         move to: docs/notes/review_log.md"
    )
