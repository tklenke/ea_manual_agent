# ABOUTME: Tests for @@TOM flag detection in WR markdown files.
# ABOUTME: Covers count, page list, empty dir, and partial match exclusion.

import pytest
from pathlib import Path
from wikicheck.tom_flags import find_tom_flags, count_tom_flags


@pytest.fixture
def wr_with_flags(tmp_path):
    wr = tmp_path / "wr"
    wr.mkdir()
    (wr / "page-a.md").write_text("Some text @@TOM check this and @@TOM again")
    (wr / "page-b.md").write_text("No flags here")
    return wr


def test_count_is_total_occurrences(wr_with_flags):
    assert count_tom_flags(wr_with_flags) == 2


def test_pages_with_tom_flags(wr_with_flags):
    assert find_tom_flags(wr_with_flags) == ["page-a"]


def test_no_tom_flags(tmp_path):
    wr = tmp_path / "wr"
    wr.mkdir()
    assert count_tom_flags(wr) == 0
    assert find_tom_flags(wr) == []


def test_partial_match_not_counted(tmp_path):
    wr = tmp_path / "wr"
    wr.mkdir()
    (wr / "page-a.md").write_text("@@TOMMY is not a flag")
    assert count_tom_flags(wr) == 0
    assert find_tom_flags(wr) == []
