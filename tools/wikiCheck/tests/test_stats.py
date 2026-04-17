# ABOUTME: Tests for wikiCheck statistics computation.
# ABOUTME: Covers all six stats: page count, broken links, approved, unreviewed, missing, log age.

from pathlib import Path
from wikicheck.stats import compute_stats

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
