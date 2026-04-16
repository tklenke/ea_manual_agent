# ABOUTME: Walks AC 43.13-1B content pages and splits extracted text into paragraph-level dicts.
# ABOUTME: Detects paragraph boundaries, inserts figure/table markers, and joins hyphenated words.

import re
from pdfindexer.page_extractor import extract_page


def parse_document(pdf, toc, content_start_page=1):
    """Walk content pages and return a list of paragraph dicts.

    Args:
        pdf: open pdfplumber PDF object
        toc: chapter/section/paragraph structure from parse_toc()
        content_start_page: 0-indexed page number where body content begins

    Returns:
        list of paragraph dicts:
        {
            "number":        "1-1",
            "title":         "General",
            "chapter":       1,
            "chapter_title": "WOOD STRUCTURE",
            "section":       1,
            "section_title": "MATERIALS AND PRACTICES",
            "text":          "1-1. GENERAL. Wood aircraft construction...",
        }
    """
    para_lookup = _build_para_lookup(toc)
    full_text = _extract_all_pages(pdf, content_start_page)
    full_text = _join_hyphens(full_text)
    full_text = _insert_markers(full_text)
    return _split_paragraphs(full_text, para_lookup)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _build_para_lookup(toc):
    """Build a flat dict mapping paragraph number → metadata."""
    lookup = {}
    for ch in toc:
        for sec in ch["sections"]:
            for para in sec["paragraphs"]:
                lookup[para["number"]] = {
                    "title":         para["title"],
                    "chapter":       ch["number"],
                    "chapter_title": ch["title"],
                    "section":       sec["number"],
                    "section_title": sec["title"],
                }
    return lookup


def _extract_all_pages(pdf, content_start_page):
    """Extract and concatenate text from all content pages."""
    parts = []
    for page in pdf.pages[content_start_page:]:
        result = extract_page(page)
        parts.append(result["text"])
    return "\n".join(parts)


def _join_hyphens(text):
    """Join words hyphenated across line breaks (e.g. 'construc-\\ntion' → 'construction')."""
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def _insert_markers(text):
    """Replace 'FIGURE N-N.' and 'TABLE N-N.' with compact markers, keeping caption text."""
    # "FIGURE 1-1. Some caption text" → "[FIG 1-1, p.??] Some caption text"
    # Page label is not available at this point; it gets embedded by page_extractor already
    # in the surrounding text, so we just compact the keyword.
    text = re.sub(
        r"\bFIGURE\s+(\d+-\d+)\.",
        r"[FIG \1]",
        text,
    )
    text = re.sub(
        r"\bTABLE\s+(\d+-\d+)\.",
        r"[TABLE \1]",
        text,
    )
    return text


def _split_paragraphs(text, para_lookup):
    """Split full document text into paragraph dicts using paragraph number markers.

    If a paragraph number is encountered again (can happen due to cross-column layout),
    the extra content is appended to the original paragraph rather than creating a duplicate.
    """
    # Match original format "1-1. TITLE" OR CHG 1 format "12-70 TITLE" (no period)
    para_pattern = re.compile(r"^(\d+-\d+)(?:\.|\s+[A-Z])")

    paragraphs = []
    seen_nums = {}   # para number → index in paragraphs list
    current_num = None
    current_lines = []

    def _flush():
        """Commit the accumulated paragraph if it hasn't been stored yet."""
        nonlocal current_num, current_lines
        if current_num is None:
            return
        if current_num not in seen_nums:
            para = _make_para(current_num, current_lines, para_lookup)
            seen_nums[current_num] = len(paragraphs)
            paragraphs.append(para)
        current_num = None
        current_lines = []

    for line in text.split("\n"):
        m = para_pattern.match(line)
        if m and m.group(1) in para_lookup:
            candidate = m.group(1)
            _flush()
            if candidate in seen_nums:
                # Duplicate occurrence — append content to existing paragraph
                paragraphs[seen_nums[candidate]]["text"] += "\n" + line
                current_num = candidate   # track so subsequent lines append too
            else:
                current_num = candidate
                current_lines = [line]
        else:
            if current_num is not None:
                if current_num in seen_nums:
                    paragraphs[seen_nums[current_num]]["text"] += "\n" + line
                else:
                    current_lines.append(line)

    _flush()
    return paragraphs


def _make_para(number, lines, para_lookup):
    """Assemble a paragraph dict from accumulated lines."""
    meta = para_lookup[number]
    return {
        "number":        number,
        "title":         meta["title"],
        "chapter":       meta["chapter"],
        "chapter_title": meta["chapter_title"],
        "section":       meta["section"],
        "section_title": meta["section_title"],
        "text":          "\n".join(lines).strip(),
    }
