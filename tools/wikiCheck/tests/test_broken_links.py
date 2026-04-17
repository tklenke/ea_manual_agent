# ABOUTME: Tests for broken link detection across the WR directory.
# ABOUTME: Covers cross-referencing extracted slugs against known pages, and deduplication.

from pathlib import Path
from wikicheck.broken_links import find_broken_links, collect_referenced_slugs


def test_collect_referenced_slugs_returns_all_linked_slugs(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]] and [[page-c]].")
    assert collect_referenced_slugs(tmp_path) == {"page-b", "page-c"}


def test_collect_referenced_slugs_deduplicates(tmp_path):
    (tmp_path / "page-a.md").write_text("[[dup]] and [[dup]]")
    (tmp_path / "page-b.md").write_text("[[dup]]")
    assert collect_referenced_slugs(tmp_path) == {"dup"}


def test_collect_referenced_slugs_empty_dir(tmp_path):
    assert collect_referenced_slugs(tmp_path) == set()


def test_detects_broken_link(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]] for info.")
    # page-b.md does not exist
    broken = find_broken_links(tmp_path)
    assert broken == ["page-b"]


def test_no_broken_links(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]].")
    (tmp_path / "page-b.md").write_text("Content.")
    assert find_broken_links(tmp_path) == []


def test_deduplicates_broken_links(tmp_path):
    (tmp_path / "page-a.md").write_text("[[missing]] and [[missing]] again.")
    (tmp_path / "page-b.md").write_text("Also [[missing]].")
    broken = find_broken_links(tmp_path)
    assert broken == ["missing"]


def test_broken_links_sorted(tmp_path):
    (tmp_path / "page-a.md").write_text("[[zebra]] and [[alpha]]")
    broken = find_broken_links(tmp_path)
    assert broken == ["alpha", "zebra"]


def test_system_links_excluded_from_broken_links(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[/-/changelog]] for history.")
    assert find_broken_links(tmp_path) == []


def test_system_link_prefix_excluded(tmp_path):
    (tmp_path / "page-a.md").write_text("[[/-/history]] and [[/-/edit/page-a]]")
    assert find_broken_links(tmp_path) == []


def test_non_system_broken_link_still_detected(tmp_path):
    (tmp_path / "page-a.md").write_text("[[/-/changelog]] and [[real-missing]]")
    assert find_broken_links(tmp_path) == ["real-missing"]
