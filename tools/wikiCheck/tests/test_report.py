# ABOUTME: Tests for summary report formatting — both normal and missing-log cases.
# ABOUTME: Validates exact output format matching the design spec.

from wikicheck.report import format_report, format_missing_log_report
from wikicheck.stats import Stats


def _stats(**kwargs):
    defaults = dict(
        total_pages=10,
        broken_link_count=0,
        system_link_count=0,
        system_links=[],
        orphan_count=0,
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
        approved_count=5,
        pending_count=0,
        unreviewed_count=0,
        missing_from_log_count=0,
        log_age_days=0,
        tom_flag_count=0,
        tom_flag_pages=[],
    )
    defaults.update(kwargs)
    return Stats(**defaults)


def test_format_normal_report():
    stats = _stats(
        total_pages=47,
        broken_link_count=12,
        system_link_count=2,
        system_links=["/-/changelog", "/-/history"],
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
        "System links:             2  (Otterwiki system calls, not checked)\n"
        "Orphan pages:             5  (exist in WR, never linked to)\n"
        "@@TOM flags:              0  (pages flagged for Tom's input)\n"
        "Structural pages:         2  (home, readme — excluded from orphans)\n"
        "Approved pages:          36  (of 47 in log)\n"
        "Pending pages:            0  (reviewed, awaiting resolution)\n"
        "Unreviewed pages:         8  (in log, never reviewed)\n"
        "Pages missing from log:   3  (in WR, not in log)\n"
        "Review log last updated: 2026-04-10 (6 days ago)"
    )


def test_orphan_line_appears_between_broken_links_and_approved():
    stats = _stats(broken_link_count=1, orphan_count=2, structural_pages_missing=["readme"])
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    broken_pos = output.index("Broken links:")
    orphan_pos = output.index("Orphan pages:")
    approved_pos = output.index("Approved pages:")
    assert broken_pos < orphan_pos < approved_pos


def test_system_links_line_in_report():
    stats = _stats(system_link_count=1, system_links=["/-/changelog"])
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "System links:             1  (Otterwiki system calls, not checked)" in output


def test_system_links_line_between_broken_and_orphan():
    stats = _stats(broken_link_count=1, system_link_count=1, system_links=["/-/changelog"], orphan_count=1)
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    broken_pos = output.index("Broken links:")
    system_pos = output.index("System links:")
    orphan_pos = output.index("Orphan pages:")
    assert broken_pos < system_pos < orphan_pos


def test_structural_pages_line_in_report():
    stats = _stats(structural_pages_found=["home", "readme"])
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "Structural pages:         2  (home, readme — excluded from orphans)" in output


def test_structural_pages_error_line_in_report():
    stats = _stats(structural_pages_found=["home"], structural_pages_missing=["readme"])
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "ERROR: Structural page not in WR: readme" in output


def test_no_structural_error_line_when_all_found():
    stats = _stats()
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "ERROR:" not in output


def test_format_missing_log_report():
    output = format_missing_log_report(
        total_pages=47,
        broken_link_count=12,
        system_link_count=2,
        system_links=["/-/changelog", "/-/history"],
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
        today="2026-04-16",
        seed_path="tools/wikiCheck/data/review_log.md",
    )
    assert output == (
        "Wiki Integrity Report — 2026-04-16\n"
        "Total WR pages:          47\n"
        "Broken links:            12  (pages referenced but not yet written)\n"
        "System links:             2  (Otterwiki system calls, not checked)\n"
        "Structural pages:         2  (home, readme — excluded from orphans)\n"
        "Review log:              NOT FOUND — seeded template written to\n"
        "                         tools/wikiCheck/data/review_log.md\n"
        "                         move to: docs/notes/review_log.md"
    )


def test_pending_line_in_report():
    stats = _stats(pending_count=3)
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "Pending pages:            3  (reviewed, awaiting resolution)" in output


def test_tom_flags_line_in_report():
    stats = _stats(tom_flag_count=5)
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    assert "@@TOM flags:              5  (pages flagged for Tom's input)" in output


def test_tom_flags_line_position():
    stats = _stats(orphan_count=2, tom_flag_count=3)
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    orphan_pos = output.index("Orphan pages:")
    tom_pos = output.index("@@TOM flags:")
    structural_pos = output.index("Structural pages:")
    assert orphan_pos < tom_pos < structural_pos


def test_pending_line_between_approved_and_unreviewed():
    stats = _stats(approved_count=5, pending_count=2, unreviewed_count=3)
    output = format_report(stats, today="2026-04-16", log_last_updated="2026-04-16")
    approved_pos = output.index("Approved pages:")
    pending_pos = output.index("Pending pages:")
    unreviewed_pos = output.index("Unreviewed pages:")
    assert approved_pos < pending_pos < unreviewed_pos


def test_tom_flags_detail_section():
    stats = _stats(tom_flag_pages=["avionics", "fuel-system"])
    from wikicheck.report import format_detail
    detail = format_detail(
        broken_links=[],
        pending=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=[],
        structural_pages_found=[],
        structural_pages_missing=[],
        system_links=[],
        tom_flag_pages=["avionics", "fuel-system"],
    )
    assert "Pages with @@TOM flags:" in detail
    assert "  avionics" in detail
    assert "  fuel-system" in detail


def test_tom_flags_detail_section_position():
    from wikicheck.report import format_detail
    detail = format_detail(
        broken_links=[],
        pending=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=["orphan-page"],
        structural_pages_found=["home"],
        structural_pages_missing=[],
        system_links=[],
        tom_flag_pages=["flagged-page"],
    )
    orphan_pos = detail.index("Orphan pages:")
    tom_pos = detail.index("Pages with @@TOM flags:")
    structural_pos = detail.index("Structural pages (excluded from orphans):")
    assert orphan_pos < tom_pos < structural_pos


def test_missing_log_report_structural_error_line():
    output = format_missing_log_report(
        total_pages=10,
        broken_link_count=0,
        system_link_count=0,
        system_links=[],
        structural_pages_found=["home"],
        structural_pages_missing=["readme"],
        today="2026-04-16",
        seed_path="tools/wikiCheck/data/review_log.md",
    )
    structural_pos = output.index("Structural pages:")
    error_pos = output.index("ERROR: Structural page not in WR: readme")
    review_log_pos = output.index("Review log:")
    assert structural_pos < error_pos < review_log_pos
