# ABOUTME: Tests for review log parsing — datestamp and page entry extraction.
# ABOUTME: Covers Last updated header and table rows with Approved/unreviewed status.

import pytest
from pathlib import Path
from wikicheck.review_log import parse_review_log, ReviewLogEntry

LOG_CONTENT = """\
# Review Log
Last updated: 2026-04-10

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| manual-standards | unreviewed | — |
"""


def test_reads_last_updated(tmp_path):
    log = tmp_path / "review_log.md"
    log.write_text(LOG_CONTENT)
    result = parse_review_log(log)
    assert result.last_updated == "2026-04-10"


def test_reads_approved_entry(tmp_path):
    log = tmp_path / "review_log.md"
    log.write_text(LOG_CONTENT)
    result = parse_review_log(log)
    approved = [e for e in result.entries if e.slug == "panels-canopy"]
    assert len(approved) == 1
    assert approved[0].status == "Approved"


def test_reads_unreviewed_entry(tmp_path):
    log = tmp_path / "review_log.md"
    log.write_text(LOG_CONTENT)
    result = parse_review_log(log)
    unreviewed = [e for e in result.entries if e.slug == "manual-standards"]
    assert len(unreviewed) == 1
    assert unreviewed[0].status == "unreviewed"


def test_entry_count(tmp_path):
    log = tmp_path / "review_log.md"
    log.write_text(LOG_CONTENT)
    result = parse_review_log(log)
    assert len(result.entries) == 2


PENDING_LOG_CONTENT = """\
# Review Log
Last updated: 2026-04-10

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| home | Pending | 2026-04-10 |
| manual-standards | unreviewed | — |
"""


def test_reads_pending_entry(tmp_path):
    log = tmp_path / "review_log.md"
    log.write_text(PENDING_LOG_CONTENT)
    result = parse_review_log(log)
    pending = [e for e in result.entries if e.slug == "home"]
    assert len(pending) == 1
    assert pending[0].status == "Pending"


def test_entry_count_includes_pending(tmp_path):
    log = tmp_path / "review_log.md"
    log.write_text(PENDING_LOG_CONTENT)
    result = parse_review_log(log)
    assert len(result.entries) == 3
