# ABOUTME: Tests for DocParser — verifies paragraph splitting, metadata tagging, and figure markers.
# ABOUTME: Uses the 7-page fixture covering TOC + PDF pages 35-40 (paragraphs 1-1 through 1-8).

import pytest
import pdfplumber
from pdfindexer.toc_parser import parse_toc
from pdfindexer.doc_parser import parse_document, _join_hyphens

FIXTURE = "tests/fixtures/ac_43_13_excerpt.pdf"


@pytest.fixture(scope="module")
def paragraphs():
    with pdfplumber.open(FIXTURE) as pdf:
        toc = parse_toc([pdf.pages[0]])
        # Content pages start at fixture page index 1 (PDF page 35)
        result = parse_document(pdf, toc, content_start_page=1)
    return result


def test_returns_list_of_paragraphs(paragraphs):
    assert isinstance(paragraphs, list)
    assert len(paragraphs) >= 7  # fixture covers 1-1 through at least 1-7


def test_first_paragraph_is_1_1(paragraphs):
    assert paragraphs[0]["number"] == "1-1"


def test_paragraphs_in_order(paragraphs):
    numbers = [p["number"] for p in paragraphs]
    assert numbers.index("1-1") < numbers.index("1-2")
    assert numbers.index("1-2") < numbers.index("1-3")


def test_paragraph_has_chapter_metadata(paragraphs):
    p = paragraphs[0]
    assert p["chapter"] == 1
    assert p["chapter_title"] == "WOOD STRUCTURE"


def test_paragraph_has_section_metadata(paragraphs):
    p = paragraphs[0]
    assert p["section"] == 1
    assert p["section_title"] == "MATERIALS AND PRACTICES"


def test_paragraph_has_title(paragraphs):
    assert paragraphs[0]["title"] == "General"


def test_paragraph_1_1_content(paragraphs):
    p = next(p for p in paragraphs if p["number"] == "1-1")
    assert "GENERAL" in p["text"]
    assert "aircraft" in p["text"]


def test_paragraph_1_2_content(paragraphs):
    p = next(p for p in paragraphs if p["number"] == "1-2")
    assert "WOODS" in p["text"]
    assert "Quality of Wood" in p["text"]


def test_figure_marker_inserted(paragraphs):
    # Figure 1-1 appears within paragraph 1-2 (about woods)
    p = next(p for p in paragraphs if p["number"] == "1-2")
    assert "[FIG 1-1" in p["text"]


def test_table_marker_inserted(paragraphs):
    # Table 1-1 appears within paragraph 1-2 (about woods)
    p = next(p for p in paragraphs if p["number"] == "1-2")
    assert "[TABLE 1-1" in p["text"]


def test_paragraph_text_does_not_bleed_into_next(paragraphs):
    p1 = next(p for p in paragraphs if p["number"] == "1-1")
    # 1-2 starts with "WOODS" — that should not be in 1-1's text
    assert "1-2." not in p1["text"]


def test_hyphenated_words_joined(paragraphs):
    p = next(p for p in paragraphs if p["number"] == "1-1")
    # "construc-\ntion" should be joined to "construction"
    assert "construction" in p["text"]
    assert "construc-" not in p["text"]


# ---------------------------------------------------------------------------
# CHG 1 Tests — CHG 1 body format uses no period after paragraph number
# ---------------------------------------------------------------------------

CHG1_FIXTURE = "tests/fixtures/ac_43_13_chg1_excerpt.pdf"


def _make_chg1_toc():
    """Build a minimal synthetic TOC covering paragraphs in the CHG 1 body fixture."""
    return [
        {
            "number": 12,
            "title": "HYDRAULIC AND PNEUMATIC SYSTEMS",
            "sections": [
                {
                    "number": 5,
                    "title": "AVIONICS TEST EQUIPMENT",
                    "paragraphs": [
                        {"number": "12-70", "title": "General", "page_ref": "12-25"},
                        {"number": "12-71", "title": "Test Equipment Calibration Standards", "page_ref": "12-25"},
                        {"number": "12-72", "title": "Test Equipment Calibration", "page_ref": "12-25"},
                    ],
                }
            ],
        },
        {
            "number": 13,
            "title": "HUMAN FACTORS",
            "sections": [
                {
                    "number": 0,
                    "title": "",
                    "paragraphs": [
                        {"number": "13-1", "title": "Human Factors Influence on Mechanic's Performance", "page_ref": "13-1"},
                        {"number": "13-2", "title": "The FAA Aviation Safety Program", "page_ref": "13-1"},
                    ],
                }
            ],
        },
    ]


@pytest.fixture(scope="module")
def chg1_paragraphs():
    toc = _make_chg1_toc()
    with pdfplumber.open(CHG1_FIXTURE) as pdf:
        # Page 0 is TOC page 34; pages 1-2 are CHG 1 body content (PDF pp.631-632)
        result = parse_document(pdf, toc, content_start_page=1)
    return result


def test_chg1_para_12_70_detected(chg1_paragraphs):
    """Paragraph 12-70 is detected from CHG 1 body text (no period after number)."""
    numbers = [p["number"] for p in chg1_paragraphs]
    assert "12-70" in numbers


def test_chg1_para_13_1_detected(chg1_paragraphs):
    """Paragraph 13-1 is detected from CHG 1 body text (no period after number)."""
    numbers = [p["number"] for p in chg1_paragraphs]
    assert "13-1" in numbers


def test_chg1_para_13_1_has_chapter_metadata(chg1_paragraphs):
    """Paragraph 13-1 carries correct chapter metadata."""
    p = next((p for p in chg1_paragraphs if p["number"] == "13-1"), None)
    assert p is not None
    assert p["chapter"] == 13


# ---------------------------------------------------------------------------
# Soft Hyphen Tests — CHG 1 pages use U+00AD (\xad) instead of U+002D for
# line-break hyphens. These must be joined just like regular hyphens.
# Fixture page 1 = PDF page 611 (paragraph 12-8, Section 2 of Ch.12)
# ---------------------------------------------------------------------------

def test_join_hyphens_strips_soft_hyphen():
    """_join_hyphens must join words broken by a soft hyphen (U+00AD)."""
    text = "is strongly recom\xad\nmended. An operation"
    result = _join_hyphens(text)
    assert "recommended" in result
    assert "\xad" not in result


def test_join_hyphens_regular_hyphen_still_works():
    """_join_hyphens must still join regular hyphens after the soft-hyphen fix."""
    text = "construc-\ntion"
    result = _join_hyphens(text)
    assert "construction" in result
    assert "-\n" not in result


def _make_chg1_toc_with_12_8():
    """Synthetic TOC covering paragraph 12-8 (PDF page 611) plus CHG 1 paragraphs."""
    return [
        {
            "number": 12,
            "title": "AIRCRAFT AVIONICS SYSTEMS",
            "sections": [
                {
                    "number": 2,
                    "title": "GROUND OPERATIONAL CHECKS FOR AVIONICS EQUIPMENT (ELECTRICAL)",
                    "paragraphs": [
                        {"number": "12-8", "title": "General", "page_ref": "12-5"},
                    ],
                },
                {
                    "number": 5,
                    "title": "AVIONICS TEST EQUIPMENT",
                    "paragraphs": [
                        {"number": "12-70", "title": "General", "page_ref": "12-25"},
                        {"number": "12-71", "title": "Test Equipment Calibration Standards", "page_ref": "12-25"},
                        {"number": "12-72", "title": "Test Equipment Calibration", "page_ref": "12-25"},
                    ],
                },
            ],
        },
        {
            "number": 13,
            "title": "HUMAN FACTORS",
            "sections": [
                {
                    "number": 0,
                    "title": "",
                    "paragraphs": [
                        {"number": "13-1", "title": "Human Factors Influence on Mechanic's Performance", "page_ref": "13-1"},
                        {"number": "13-2", "title": "The FAA Aviation Safety Program", "page_ref": "13-1"},
                    ],
                }
            ],
        },
    ]


@pytest.fixture(scope="module")
def para_12_8():
    """Parse paragraph 12-8 from the CHG 1 fixture (fixture page 1 = PDF page 611)."""
    toc = _make_chg1_toc_with_12_8()
    with pdfplumber.open(CHG1_FIXTURE) as pdf:
        # content_start_page=1: fixture pages 1-3 (PDF pp.611, 631, 632)
        paragraphs = parse_document(pdf, toc, content_start_page=1)
    return next((p for p in paragraphs if p["number"] == "12-8"), None)


def test_para_12_8_detected(para_12_8):
    """Paragraph 12-8 is found in the CHG 1 fixture."""
    assert para_12_8 is not None


def test_para_12_8_soft_hyphens_joined(para_12_8):
    """Soft-hyphen line breaks in paragraph 12-8 are joined (e.g. recom­+mended → recommended)."""
    assert para_12_8 is not None
    assert "recommended" in para_12_8["text"]
    assert "\xad" not in para_12_8["text"]


def test_para_12_8_no_broken_word_recom(para_12_8):
    """'recom' does not appear as a fragment (line break was at 'recom­\\nmended')."""
    assert para_12_8 is not None
    # After joining, "recom" should only appear as part of "recommended"
    text = para_12_8["text"]
    assert "recom\xad" not in text
    # The word "recommended" appears whole, not as a bare fragment
    assert "recom\n" not in text


# ---------------------------------------------------------------------------
# Mid-line paragraph marker — fixture page 1 (PDF page 431)
# Paragraph 9-17 marker appears on the same line as a figure label:
# "TIRE DANGER 9-17. DISASSEMBLE THE WHEEL in"
# The primary ^(\d+-\d+) pattern cannot match; a secondary search is required.
# ---------------------------------------------------------------------------

def _make_toc_with_9_17():
    """Minimal synthetic TOC containing only paragraph 9-17."""
    return [
        {
            "number": 9,
            "title": "AIRCRAFT LANDING GEAR SYSTEMS",
            "sections": [
                {
                    "number": 1,
                    "title": "INSPECTION AND MAINTENANCE OF LANDING GEAR",
                    "paragraphs": [
                        {"number": "9-17", "title": "Disassemble the Wheel", "page_ref": "9-7"},
                    ],
                }
            ],
        }
    ]


@pytest.fixture(scope="module")
def para_9_17():
    """Parse paragraph 9-17 from the CHG 1 fixture (fixture page 1 = PDF page 431)."""
    toc = _make_toc_with_9_17()
    with pdfplumber.open(CHG1_FIXTURE) as pdf:
        paragraphs = parse_document(pdf, toc, content_start_page=1)
    return next((p for p in paragraphs if p["number"] == "9-17"), None)


def test_para_9_17_detected(para_9_17):
    """Paragraph 9-17 is detected even though its marker appears mid-line after a figure label."""
    assert para_9_17 is not None


def test_para_9_17_has_chapter_metadata(para_9_17):
    """Paragraph 9-17 carries correct chapter metadata."""
    assert para_9_17 is not None
    assert para_9_17["chapter"] == 9


def test_para_9_17_text_starts_at_marker(para_9_17):
    """Paragraph 9-17 text begins at the paragraph marker, not the figure label."""
    assert para_9_17 is not None
    assert para_9_17["text"].startswith("9-17.")
    assert "TIRE DANGER" not in para_9_17["text"]
