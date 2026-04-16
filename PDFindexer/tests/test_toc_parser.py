# ABOUTME: Tests for TocParser — verifies extraction of chapter/section/paragraph structure from TOC pages.
# ABOUTME: Uses the 7-page fixture (PDF pages 2 and 35-40); fixture page 1 is the TOC page.

import pytest
import pdfplumber
from pdfindexer.toc_parser import parse_toc

FIXTURE = "tests/fixtures/ac_43_13_excerpt.pdf"


@pytest.fixture
def toc_page():
    with pdfplumber.open(FIXTURE) as pdf:
        yield pdf.pages[0]  # fixture page 1 = PDF page 2 = TOC (Chapter 1 entries)


def test_parse_toc_returns_chapters(toc_page):
    result = parse_toc([toc_page])
    assert len(result) >= 1
    assert result[0]["title"] == "WOOD STRUCTURE"
    assert result[0]["number"] == 1


def test_parse_toc_chapters_have_sections(toc_page):
    result = parse_toc([toc_page])
    ch1 = result[0]
    assert len(ch1["sections"]) >= 1
    assert ch1["sections"][0]["title"] == "MATERIALS AND PRACTICES"
    assert ch1["sections"][0]["number"] == 1


def test_parse_toc_sections_have_paragraphs(toc_page):
    result = parse_toc([toc_page])
    ch1 = result[0]
    s1 = ch1["sections"][0]
    assert len(s1["paragraphs"]) >= 1
    # First paragraph in section 1
    assert s1["paragraphs"][0]["number"] == "1-1"
    assert s1["paragraphs"][0]["title"] == "General"


def test_parse_toc_paragraph_has_page_ref(toc_page):
    result = parse_toc([toc_page])
    para = result[0]["sections"][0]["paragraphs"][0]
    assert "page_ref" in para
    assert para["page_ref"] == "1-1"


def test_parse_toc_all_chapter1_sections_present(toc_page):
    result = parse_toc([toc_page])
    ch1 = result[0]
    section_titles = [s["title"] for s in ch1["sections"]]
    assert "MATERIALS AND PRACTICES" in section_titles
    assert "HEALTH AND SAFETY" in section_titles
    assert "INSPECTION" in section_titles
    assert "REPAIRS" in section_titles
