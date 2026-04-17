# ABOUTME: Tests for orphan page detection across the WR directory.
# ABOUTME: Covers pages that exist as .md files but are never linked to from other pages.

from pathlib import Path
from wikicheck.orphan_pages import find_orphan_pages, check_structural_pages


def test_unlinked_page_is_orphan(tmp_path):
    (tmp_path / "page-a.md").write_text("No links here.")
    assert find_orphan_pages(tmp_path) == ["page-a"]


def test_linked_page_is_not_orphan(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]].")
    (tmp_path / "page-b.md").write_text("Content.")
    assert find_orphan_pages(tmp_path) == ["page-a"]


def test_all_pages_linked_returns_empty(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]].")
    (tmp_path / "page-b.md").write_text("See [[page-a]].")
    assert find_orphan_pages(tmp_path) == []


def test_empty_wr_dir_returns_empty(tmp_path):
    assert find_orphan_pages(tmp_path) == []


def test_orphan_pages_sorted(tmp_path):
    (tmp_path / "zebra.md").write_text("No links.")
    (tmp_path / "alpha.md").write_text("No links.")
    assert find_orphan_pages(tmp_path) == ["alpha", "zebra"]


def test_structural_page_excluded_from_orphans(tmp_path):
    (tmp_path / "home.md").write_text("No links.")
    assert find_orphan_pages(tmp_path) == []


def test_structural_page_case_insensitive_excluded(tmp_path):
    (tmp_path / "Home.md").write_text("No links.")
    assert find_orphan_pages(tmp_path) == []


def test_check_structural_pages_both_found(tmp_path):
    (tmp_path / "home.md").write_text("Home.")
    (tmp_path / "readme.md").write_text("Readme.")
    found, missing = check_structural_pages(tmp_path)
    assert sorted(found) == ["home", "readme"]
    assert missing == []


def test_check_structural_pages_one_missing(tmp_path):
    (tmp_path / "home.md").write_text("Home.")
    found, missing = check_structural_pages(tmp_path)
    assert found == ["home"]
    assert missing == ["readme"]


def test_check_structural_pages_case_insensitive(tmp_path):
    (tmp_path / "README.md").write_text("Readme.")
    (tmp_path / "home.md").write_text("Home.")
    found, missing = check_structural_pages(tmp_path)
    assert sorted(found) == ["home", "readme"]
    assert missing == []
