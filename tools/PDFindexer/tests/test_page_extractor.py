# ABOUTME: Tests for PageExtractor — verifies two-column text extraction, header/footer stripping,
# ABOUTME: and figure detection from content pages of AC 43.13-1B.

import pytest
import pdfplumber
from pdfindexer.page_extractor import extract_page

FIXTURE = "tests/fixtures/ac_43_13_excerpt.pdf"


@pytest.fixture
def first_content_page():
    with pdfplumber.open(FIXTURE) as pdf:
        yield pdf.pages[1]  # fixture page 2 = PDF page 35


def test_strips_page_header(first_content_page):
    result = extract_page(first_content_page)
    assert "9/8/98" not in result["text"]
    assert "AC 43.13-1B" not in result["text"]


def test_strips_page_footer(first_content_page):
    result = extract_page(first_content_page)
    assert "Par 1-1" not in result["text"]
    assert "Page 1-1" not in result["text"]


def test_returns_page_label(first_content_page):
    result = extract_page(first_content_page)
    assert result["page_label"] == "1-1"


def test_chapter_header_present(first_content_page):
    result = extract_page(first_content_page)
    assert "CHAPTER 1" in result["text"]
    assert "WOOD STRUCTURE" in result["text"]


def test_section_header_present(first_content_page):
    result = extract_page(first_content_page)
    assert "SECTION 1" in result["text"]
    assert "MATERIALS AND PRACTICES" in result["text"]


def test_left_column_before_right_column(first_content_page):
    result = extract_page(first_content_page)
    text = result["text"]
    # Paragraph 1-1 is in the left column; "b. Substitution" is in the right column
    pos_para = text.find("1-1.")
    pos_right = text.find("Substitution of Original Wood")
    assert pos_para != -1
    assert pos_right != -1
    assert pos_para < pos_right


def test_left_column_content_intact(first_content_page):
    result = extract_page(first_content_page)
    text = result["text"]
    assert "1-1." in text
    assert "GENERAL" in text
    assert "Wood aircraft" in text


def test_right_column_content_intact(first_content_page):
    result = extract_page(first_content_page)
    text = result["text"]
    assert "Substitution of Original Wood" in text
    assert "Effects of Shrinkage" in text


def test_detects_figure(first_content_page):
    result = extract_page(first_content_page)
    assert len(result["figures"]) == 1
    fig = result["figures"][0]
    assert "top" in fig
    assert "bottom" in fig
    assert "page_label" in fig


def test_figure_caption_present(first_content_page):
    result = extract_page(first_content_page)
    assert "FIGURE 1-1" in result["text"]
