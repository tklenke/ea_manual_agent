# ABOUTME: Tests for wikiCheck statistics computation.
# ABOUTME: Covers all six stats: page count, broken links, approved, unreviewed, missing, log age.

from pathlib import Path
from wikicheck.stats import compute_stats, Stats

LOG_CONTENT = """\
# Review Log
Last updated: 2026-04-10

| Page | Status | Last Reviewed |
|------|--------|---------------|
| page-a | Approved | 2026-04-10 |
| page-b | unreviewed | — |
"""


def _make_wr(tmp_path, pages):
    wr = tmp_path / "wr"
    wr.mkdir()
    for name in pages:
        (wr / f"{name}.md").write_text("")
    return wr


def _make_log(tmp_path, content):
    log = tmp_path / "review_log.md"
    log.write_text(content)
    return log


def test_total_wr_page_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b", "page-c"])
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.total_pages == 3


def test_broken_link_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b"])
    (wr / "page-a.md").write_text("[[missing-page]]")
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.broken_link_count == 1


def test_approved_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b"])
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.approved_count == 1


def test_unreviewed_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b"])
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.unreviewed_count == 1


def test_missing_from_log_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b", "page-c"])
    log = _make_log(tmp_path, LOG_CONTENT)  # only has page-a and page-b
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.missing_from_log_count == 1


def test_log_age_in_days(tmp_path):
    wr = _make_wr(tmp_path, ["page-a"])
    log = _make_log(tmp_path, LOG_CONTENT)  # Last updated: 2026-04-10
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.log_age_days == 6


def test_orphan_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b", "page-c"])
    (wr / "page-a.md").write_text("[[page-b]]")  # page-b is linked; page-c is orphan
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.orphan_count == 2  # page-a and page-c are orphans


def test_structural_pages_found(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "home", "readme"])
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert sorted(stats.structural_pages_found) == ["home", "readme"]
    assert stats.structural_pages_missing == []


def test_structural_pages_missing(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "home"])
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.structural_pages_found == ["home"]
    assert stats.structural_pages_missing == ["readme"]


def test_system_link_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a"])
    (wr / "page-a.md").write_text("[[/-/changelog]] and [[/-/history]]")
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.system_link_count == 2
    assert sorted(stats.system_links) == ["/-/changelog", "/-/history"]


def test_orphan_count_excludes_structural(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "home"])
    log = _make_log(tmp_path, LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.orphan_count == 1  # page-a is orphan; home is structural, not counted


PENDING_LOG_CONTENT = """\
# Review Log
Last updated: 2026-04-10

| Page | Status | Last Reviewed |
|------|--------|---------------|
| page-a | Approved | 2026-04-10 |
| page-b | Pending | 2026-04-10 |
"""


def test_pending_count(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b"])
    log = _make_log(tmp_path, PENDING_LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.pending_count == 1


def test_pending_not_in_missing_from_log(tmp_path):
    wr = _make_wr(tmp_path, ["page-a", "page-b"])
    log = _make_log(tmp_path, PENDING_LOG_CONTENT)
    stats = compute_stats(wr, log, today="2026-04-16")
    assert stats.missing_from_log_count == 0
