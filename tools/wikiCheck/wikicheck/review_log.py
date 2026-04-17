# ABOUTME: Parses the AR review log — extracts last-updated date and per-page status entries.
# ABOUTME: Returns a ReviewLog dataclass with last_updated string and list of ReviewLogEntry.

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ReviewLogEntry:
    slug: str
    status: str


@dataclass
class ReviewLog:
    last_updated: str
    entries: list[ReviewLogEntry] = field(default_factory=list)


_LAST_UPDATED_RE = re.compile(r'^Last updated:\s*(\S+)', re.MULTILINE)
_ROW_RE = re.compile(r'^\|\s*([^|]+?)\s*\|\s*(Approved|Pending|unreviewed)\s*\|', re.MULTILINE)


def parse_review_log(log_path: Path) -> ReviewLog:
    text = Path(log_path).read_text()
    m = _LAST_UPDATED_RE.search(text)
    last_updated = m.group(1) if m else ""
    entries = [ReviewLogEntry(slug=m.group(1), status=m.group(2)) for m in _ROW_RE.finditer(text)]
    return ReviewLog(last_updated=last_updated, entries=entries)
