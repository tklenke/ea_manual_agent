# ABOUTME: Extracts appendix content from AC 43.13-1B into plain text strings.
# ABOUTME: Each appendix is extracted as-is (no paragraph splitting) with a standard header line.

import re

# Match page_extractor's cutoffs and column constants
_HEADER_CUTOFF = 65
_FOOTER_CUTOFF = 745
_COL_MIDPOINT = 306
_FULL_WIDTH_MIN_X = 150

# Appendix pages use a wider y-grouping tolerance than body pages.
# Leader-dot words (U+F8E7) sit ~2pt above their visual line due to PDF encoding;
# 4pt threshold merges them with adjacent text while staying well below the 11pt
# minimum line spacing in the glossary.
_LINE_TOLERANCE = 4


def extract_appendix(pdf, start_page, end_page, title):
    """Extract appendix pages from the PDF and return a cleaned plain text string.

    Args:
        pdf: open pdfplumber PDF object
        start_page: 1-indexed first page number of the appendix
        end_page: 1-indexed last page number of the appendix (inclusive)
        title: full appendix title for the header line (e.g., "Appendix 1: Glossary")

    Returns:
        Plain text string: standardized header line, blank line, then appendix body.
    """
    parts = []
    for page in pdf.pages[start_page - 1 : end_page]:
        text = _extract_page_text(page)
        parts.append(text)

    text = "\n".join(parts)
    text = _replace_leaders(text)
    text = _join_hyphens(text)
    text = _strip_appendix_title_lines(text)

    return f"AC 43.13-1B  {title}\n\n" + text.strip() + "\n"


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _extract_page_text(page):
    """Column-aware text extraction for appendix pages.

    Identical logic to page_extractor._reconstruct_text() but uses a wider
    y-grouping tolerance (4pt vs 2pt).  The wider tolerance is needed because
    leader-dot words (U+F8E7) are encoded in the PDF with a top position ~2pt
    above the rest of the words on the same visual line.  With a 2pt bucket
    they fall into a separate line; with 4pt they merge correctly.

    Normal line spacing in the appendices is ~11pt, so 4pt is safe.
    """
    words = page.extract_words()
    words = [w for w in words if _HEADER_CUTOFF <= w["top"] <= _FOOTER_CUTOFF]
    if not words:
        return ""

    lines = _group_into_lines(words)

    full_width_lines = []
    left_lines = []
    right_lines = []

    for row in lines:
        min_x = row[0]["x0"]
        y = row[0]["top"]
        has_left = any(w["x0"] < _COL_MIDPOINT for w in row)
        has_right = any(w["x0"] >= _COL_MIDPOINT for w in row)

        if has_left and has_right and min_x > _FULL_WIDTH_MIN_X:
            full_width_lines.append((y, " ".join(w["text"] for w in row)))
        else:
            left_words = [w for w in row if w["x0"] < _COL_MIDPOINT]
            right_words = [w for w in row if w["x0"] >= _COL_MIDPOINT]
            if left_words:
                left_lines.append((y, " ".join(w["text"] for w in left_words)))
            if right_words:
                right_lines.append((y, " ".join(w["text"] for w in right_words)))

    merged = sorted(full_width_lines + left_lines, key=lambda t: t[0])
    all_lines = merged + right_lines
    return "\n".join(text for _, text in all_lines)


def _group_into_lines(words):
    """Group words into visual lines using greedy y-proximity.

    Words sorted by top position are grouped together as long as each word's
    top is within _LINE_TOLERANCE of the group's first word's top.  This is
    more robust than fixed-size buckets when a word's top sits just across a
    bucket boundary (as the U+F8E7 leader words do).
    """
    sorted_words = sorted(words, key=lambda w: w["top"])
    groups = []
    current_group = []
    group_anchor = None

    for w in sorted_words:
        if group_anchor is None or w["top"] - group_anchor <= _LINE_TOLERANCE:
            current_group.append(w)
            if group_anchor is None:
                group_anchor = w["top"]
        else:
            groups.append(sorted(current_group, key=lambda w: w["x0"]))
            current_group = [w]
            group_anchor = w["top"]

    if current_group:
        groups.append(sorted(current_group, key=lambda w: w["x0"]))
    return groups


def _replace_leaders(text):
    """Replace runs of leader-dot characters (U+F8E7) with two spaces.

    In the PDF, U+F8E7 encodes dot leaders that separate a term from its
    definition (glossary) or an acronym from its expansion (acronym list).
    Replacing the run with two spaces preserves the term  definition structure.
    """
    return re.sub(r'\uf8e7+', '  ', text)


def _join_hyphens(text):
    """Join words hyphenated across line breaks (regular and soft hyphens)."""
    text = re.sub(r'\xad\n\s*', '', text)    # soft-hyphen line breaks (U+00AD)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)  # regular-hyphen line breaks
    text = text.replace('\xad', '')           # strip any residual soft hyphens
    return text


def _strip_appendix_title_lines(text):
    """Remove in-PDF appendix title lines (e.g., 'APPENDIX 1. GLOSSARY', 'Appendix 1').

    The standardized header is added separately by extract_appendix().
    """
    lines = text.split("\n")
    cleaned = [
        line for line in lines
        if not re.match(r'^APPENDIX\s+\d+[\.\s]', line)
        and not re.match(r'^Appendix\s+\d+\s*$', line)
    ]
    return "\n".join(cleaned)
