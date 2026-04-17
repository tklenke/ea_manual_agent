# ABOUTME: Tests for --detail flag output — sorted lists of broken links, unreviewed, missing pages.
# ABOUTME: Also verifies detail is absent when flag not passed.

from wikicheck.report import format_detail


def test_detail_includes_broken_links():
    detail = format_detail(
        broken_links=["page-x", "page-y"],
        unreviewed=["manual-standards"],
        missing_from_log=["page-z"],
    )
    assert "Broken links:" in detail
    assert "  page-x" in detail
    assert "  page-y" in detail


def test_detail_includes_unreviewed():
    detail = format_detail(
        broken_links=[],
        unreviewed=["manual-standards", "record-of-revisions"],
        missing_from_log=[],
    )
    assert "Unreviewed pages:" in detail
    assert "  manual-standards" in detail
    assert "  record-of-revisions" in detail


def test_detail_includes_missing_from_log():
    detail = format_detail(
        broken_links=[],
        unreviewed=[],
        missing_from_log=["new-page"],
    )
    assert "Pages missing from log:" in detail
    assert "  new-page" in detail


def test_detail_empty_sections_show_none():
    detail = format_detail(broken_links=[], unreviewed=[], missing_from_log=[])
    assert "  (none)" in detail


def test_detail_sorted():
    detail = format_detail(
        broken_links=["zebra", "alpha"],
        unreviewed=[],
        missing_from_log=[],
    )
    alpha_pos = detail.index("  alpha")
    zebra_pos = detail.index("  zebra")
    assert alpha_pos < zebra_pos
