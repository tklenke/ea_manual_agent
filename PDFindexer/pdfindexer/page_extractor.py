# ABOUTME: Extracts text from a single AC 43.13-1B content page with column-aware reconstruction.
# ABOUTME: Handles two-column body text, strips headers/footers, and detects embedded figures.

import re


# Page boundaries (points from top of page)
_HEADER_CUTOFF = 65    # skip date/doc-number line at top
_FOOTER_CUTOFF = 745   # skip Par/Page line at bottom

# Column midpoint for standard letter page (width=612)
_COL_MIDPOINT = 306

# Full-width lines (centered headers, captions) have no words near left margin
_FULL_WIDTH_MIN_X = 150

# Y-grouping tolerance for words on the same line (points)
_LINE_TOLERANCE = 2


def extract_page(page):
    """Extract text and figure metadata from a single content page.

    Args:
        page: pdfplumber page object

    Returns:
        dict with keys:
          "text"        - reconstructed plain text, left column before right column
          "page_label"  - page reference string from footer (e.g. "1-1"), or ""
          "figures"     - list of dicts: {"top": float, "bottom": float, "page_label": str}
    """
    words = page.extract_words()
    page_label = _extract_page_label(words)
    content_words = _strip_header_footer(words)
    text = _reconstruct_text(content_words)
    figures = _extract_figures(page, page_label)
    return {"text": text, "page_label": page_label, "figures": figures}


def _extract_page_label(words):
    """Find the page label from the footer (e.g. 'Page 1-1' → '1-1')."""
    footer_words = [w for w in words if w["top"] > _FOOTER_CUTOFF]
    for i, w in enumerate(footer_words):
        if w["text"] == "Page" and i + 1 < len(footer_words):
            return footer_words[i + 1]["text"]
    return ""


def _strip_header_footer(words):
    """Remove header and footer words, keeping only body content."""
    return [w for w in words if _HEADER_CUTOFF <= w["top"] <= _FOOTER_CUTOFF]


def _group_into_lines(words):
    """Group words into lines by y-position within tolerance."""
    buckets = {}
    for w in words:
        y_key = round(w["top"] / _LINE_TOLERANCE) * _LINE_TOLERANCE
        buckets.setdefault(y_key, []).append(w)
    lines = []
    for y_key in sorted(buckets):
        row = sorted(buckets[y_key], key=lambda w: w["x0"])
        lines.append(row)
    return lines


def _reconstruct_text(words):
    """Reconstruct text with left column before right column.

    Full-width lines (centered headers, captions) where no word starts
    near the left margin are kept together and merged into the left-column
    pass at their natural y-position.
    """
    lines = _group_into_lines(words)

    full_width_lines = []  # (y, text)
    left_lines = []        # (y, text)
    right_lines = []       # (y, text)

    for row in lines:
        min_x = row[0]["x0"]
        y = row[0]["top"]
        has_left = any(w["x0"] < _COL_MIDPOINT for w in row)
        has_right = any(w["x0"] >= _COL_MIDPOINT for w in row)

        if has_left and has_right and min_x > _FULL_WIDTH_MIN_X:
            # Centered header or caption — spans both sides but not anchored at left margin
            full_width_lines.append((y, " ".join(w["text"] for w in row)))
        else:
            # Split into left and right column parts
            left_words = [w for w in row if w["x0"] < _COL_MIDPOINT]
            right_words = [w for w in row if w["x0"] >= _COL_MIDPOINT]
            if left_words:
                left_lines.append((y, " ".join(w["text"] for w in left_words)))
            if right_words:
                right_lines.append((y, " ".join(w["text"] for w in right_words)))

    # Merge full-width into left by y-position, then append right column
    merged = sorted(full_width_lines + left_lines, key=lambda t: t[0])
    all_lines = merged + right_lines

    return "\n".join(text for _, text in all_lines)


def _extract_figures(page, page_label):
    """Return metadata for each image found on the page."""
    figures = []
    for img in page.images:
        figures.append({
            "top": img["top"],
            "bottom": img["bottom"],
            "page_label": page_label,
        })
    return figures
