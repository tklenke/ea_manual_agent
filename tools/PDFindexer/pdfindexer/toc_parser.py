# ABOUTME: Parses the Table of Contents pages of AC 43.13-1B to extract document structure.
# ABOUTME: Returns a list of chapters, each containing sections, each containing paragraphs.

import re


def parse_toc(pages):
    """Parse TOC pages and return structured chapter/section/paragraph list.

    Args:
        pages: list of pdfplumber page objects covering the TOC

    Returns:
        list of chapter dicts:
        [
          {
            "number": 1,
            "title": "WOOD STRUCTURE",
            "sections": [
              {
                "number": 1,
                "title": "MATERIALS AND PRACTICES",
                "paragraphs": [
                  {"number": "1-1", "title": "General", "page_ref": "1-1"},
                  ...
                ]
              },
              ...
            ]
          },
          ...
        ]
    """
    lines = _extract_lines(pages)
    return _parse_structure(lines)


def _extract_lines(pages):
    """Extract text lines from pages, grouping words by y-position."""
    lines = []
    for page in pages:
        words = page.extract_words()
        if not words:
            continue
        # Group words into lines by y-position (within 2pt tolerance)
        buckets = {}
        for w in words:
            y_key = round(w["top"] / 2) * 2
            buckets.setdefault(y_key, []).append(w)
        for y_key in sorted(buckets):
            row = sorted(buckets[y_key], key=lambda w: w["x0"])
            lines.append(row)
    return lines


def _parse_structure(lines):
    """Walk lines and build chapter/section/paragraph hierarchy."""
    chapters = []
    current_chapter = None
    current_section = None

    for row in lines:
        texts = [w["text"] for w in row]
        x0s = [w["x0"] for w in row]
        line_text = " ".join(texts)

        # Chapter header: "CHAPTER N. TITLE WORDS"
        ch_match = re.match(r"CHAPTER\s+(\d+)\.", line_text)
        if ch_match:
            title = _chapter_section_title(texts)
            current_chapter = {
                "number": int(ch_match.group(1)),
                "title": title,
                "sections": [],
            }
            chapters.append(current_chapter)
            current_section = None
            continue

        # Section header: "SECTION N. TITLE WORDS"
        sec_match = re.match(r"SECTION\s+(\d+)\.", line_text)
        if sec_match and current_chapter is not None:
            title = _chapter_section_title(texts)
            current_section = {
                "number": int(sec_match.group(1)),
                "title": title,
                "paragraphs": [],
            }
            current_chapter["sections"].append(current_section)
            continue

        # Paragraph entry: first word at x<115 matches "N-N." pattern
        if x0s and x0s[0] < 115 and current_chapter is not None:
            para_match = re.match(r"^(\d+-\d+)\.?$", texts[0])
            if para_match:
                para_num = para_match.group(1)
                title, page_ref = _para_title_and_page(texts[1:])
                if title:
                    # Chapters with no section headers (e.g., Ch.13): create a
                    # synthetic section on demand so paragraphs have a home.
                    if current_section is None:
                        current_section = {
                            "number": 0,
                            "title": "",
                            "paragraphs": [],
                        }
                        current_chapter["sections"].append(current_section)
                    current_section["paragraphs"].append({
                        "number": para_num,
                        "title": title,
                        "page_ref": page_ref,
                    })
                continue

    return chapters


def _chapter_section_title(texts):
    """Extract title words after 'CHAPTER N.' or 'SECTION N.' tokens."""
    # Skip tokens until past the "N." token, then collect remaining words
    past_number = False
    title_words = []
    for t in texts:
        if not past_number:
            if re.match(r"^\d+\.$", t):
                past_number = True
        else:
            title_words.append(t)
    return " ".join(title_words)


def _para_title_and_page(texts):
    """Extract paragraph title and page reference from the title tokens.

    The last token typically contains 'TitleWord.....N-N' with the page ref
    embedded after dot leaders.
    """
    if not texts:
        return "", ""

    # Join all tokens; last token may contain "...page_ref" at end
    last = texts[-1]
    page_ref = ""
    page_match = re.search(r"[.\s]*([\d]+-[\d]+)\s*$", last)
    if page_match:
        page_ref = page_match.group(1)
        # Strip the dots and page ref from the last token to get clean title word
        clean_last = re.sub(r"\.+[\d]+-[\d]+\s*$", "", last).rstrip(".")
    else:
        clean_last = last

    title_parts = texts[:-1] + ([clean_last] if clean_last else [])
    title = " ".join(t for t in title_parts if t)
    return title, page_ref
