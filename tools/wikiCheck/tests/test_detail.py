# ABOUTME: Tests for --detail flag output — sorted lists of broken links, unreviewed, missing pages.
# ABOUTME: Also verifies detail is absent when flag not passed.

from wikicheck.report import format_detail


def test_detail_includes_broken_links():
    detail = format_detail(
        broken_links=["page-x", "page-y"],
        unreviewed=["manual-standards"],
        missing_from_log=["page-z"],
        orphan_pages=[],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    assert "Broken links:" in detail
    assert "  page-x" in detail
    assert "  page-y" in detail


def test_detail_includes_unreviewed():
    detail = format_detail(
        broken_links=[],
        unreviewed=["manual-standards", "record-of-revisions"],
        missing_from_log=[],
        orphan_pages=[],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    assert "Unreviewed pages:" in detail
    assert "  manual-standards" in detail
    assert "  record-of-revisions" in detail


def test_detail_includes_missing_from_log():
    detail = format_detail(
        broken_links=[],
        unreviewed=[],
        missing_from_log=["new-page"],
        orphan_pages=[],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    assert "Pages missing from log:" in detail
    assert "  new-page" in detail


def test_detail_empty_sections_show_none():
    detail = format_detail(
        broken_links=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=[],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    assert "  (none)" in detail


def test_detail_sorted():
    detail = format_detail(
        broken_links=["zebra", "alpha"],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=[],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    alpha_pos = detail.index("  alpha")
    zebra_pos = detail.index("  zebra")
    assert alpha_pos < zebra_pos


def test_detail_includes_orphan_pages():
    detail = format_detail(
        broken_links=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=["lonely-page", "another-orphan"],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    assert "Orphan pages:" in detail
    assert "  lonely-page" in detail
    assert "  another-orphan" in detail


def test_orphan_section_between_broken_links_and_unreviewed():
    detail = format_detail(
        broken_links=["bad-link"],
        unreviewed=["unreviewed-page"],
        missing_from_log=[],
        orphan_pages=["orphan-page"],
        structural_pages_found=[],
        structural_pages_missing=[],
    )
    broken_pos = detail.index("Broken links:")
    orphan_pos = detail.index("Orphan pages:")
    unreviewed_pos = detail.index("Unreviewed pages:")
    assert broken_pos < orphan_pos < unreviewed_pos


def test_detail_structural_section_present():
    detail = format_detail(
        broken_links=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=[],
        structural_pages_found=["home", "readme"],
        structural_pages_missing=[],
    )
    assert "Structural pages (excluded from orphans):" in detail
    assert "  home" in detail
    assert "  readme" in detail


def test_detail_structural_error_lines():
    detail = format_detail(
        broken_links=[],
        unreviewed=[],
        missing_from_log=[],
        orphan_pages=[],
        structural_pages_found=["home"],
        structural_pages_missing=["readme"],
    )
    assert "  ERROR: not in WR: readme" in detail
