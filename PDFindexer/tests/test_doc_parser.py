# ABOUTME: Tests for DocParser — verifies paragraph splitting, metadata tagging, and figure markers.
# ABOUTME: Uses the 7-page fixture covering TOC + PDF pages 35-40 (paragraphs 1-1 through 1-8).

import pytest
import pdfplumber
from pdfindexer.toc_parser import parse_toc
from pdfindexer.doc_parser import parse_document

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
