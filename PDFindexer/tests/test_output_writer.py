# ABOUTME: Tests for OutputWriter — verifies paragraph file format, index format, and filenames.
# ABOUTME: Uses a small set of synthetic paragraph dicts to test output independently of extraction.

import os
import pytest
import tempfile
from pdfindexer.output_writer import write_output

SAMPLE_TOC = [
    {
        "number": 1,
        "title": "WOOD STRUCTURE",
        "sections": [
            {
                "number": 1,
                "title": "MATERIALS AND PRACTICES",
                "paragraphs": [
                    {"number": "1-1", "title": "General",        "page_ref": "1-1"},
                    {"number": "1-2", "title": "Woods",          "page_ref": "1-1"},
                    {"number": "1-3", "title": "Modified Wood",  "page_ref": "1-3"},
                ],
            },
            {
                "number": 2,
                "title": "HEALTH AND SAFETY",
                "paragraphs": [
                    {"number": "1-18", "title": "General", "page_ref": "1-9"},
                ],
            },
        ],
    },
]

SAMPLE_PARAGRAPHS = [
    {
        "number": "1-1",
        "title": "General",
        "chapter": 1,
        "chapter_title": "WOOD STRUCTURE",
        "section": 1,
        "section_title": "MATERIALS AND PRACTICES",
        "text": "1-1. GENERAL. Wood aircraft construction dates back to the early days.",
    },
    {
        "number": "1-2",
        "title": "Woods",
        "chapter": 1,
        "chapter_title": "WOOD STRUCTURE",
        "section": 1,
        "section_title": "MATERIALS AND PRACTICES",
        "text": "1-2. WOODS.\na. Quality of Wood. All wood and plywood...\n[FIG 1-1] Relative shrinkage.",
    },
    {
        "number": "1-18",
        "title": "General",
        "chapter": 1,
        "chapter_title": "WOOD STRUCTURE",
        "section": 2,
        "section_title": "HEALTH AND SAFETY",
        "text": "1-18. GENERAL. Sanding generates fine dust.",
    },
]


@pytest.fixture
def output_dir():
    with tempfile.TemporaryDirectory() as d:
        write_output(SAMPLE_PARAGRAPHS, SAMPLE_TOC, d)
        yield d


def test_creates_paragraph_files(output_dir):
    files = os.listdir(output_dir)
    assert "ch01_p001.txt" in files
    assert "ch01_p002.txt" in files
    assert "ch01_p018.txt" in files


def test_paragraph_file_has_header_line(output_dir):
    with open(os.path.join(output_dir, "ch01_p001.txt")) as f:
        first_line = f.readline().strip()
    assert "Chapter 1" in first_line
    assert "WOOD STRUCTURE" in first_line
    assert "Section 1" in first_line
    assert "MATERIALS AND PRACTICES" in first_line


def test_paragraph_file_contains_text(output_dir):
    with open(os.path.join(output_dir, "ch01_p001.txt")) as f:
        content = f.read()
    assert "GENERAL" in content
    assert "Wood aircraft construction" in content


def test_paragraph_file_no_markdown(output_dir):
    with open(os.path.join(output_dir, "ch01_p001.txt")) as f:
        content = f.read()
    assert "##" not in content
    assert "**" not in content


def test_creates_index_file(output_dir):
    assert "index.txt" in os.listdir(output_dir)


def test_index_contains_chapter(output_dir):
    with open(os.path.join(output_dir, "index.txt")) as f:
        content = f.read()
    assert "CHAPTER 1" in content
    assert "WOOD STRUCTURE" in content


def test_index_contains_section(output_dir):
    with open(os.path.join(output_dir, "index.txt")) as f:
        content = f.read()
    assert "SECTION 1" in content
    assert "MATERIALS AND PRACTICES" in content


def test_index_contains_paragraph_entries(output_dir):
    with open(os.path.join(output_dir, "index.txt")) as f:
        content = f.read()
    assert "1-1" in content
    assert "General" in content
    assert "ch01_p001.txt" in content


def test_index_lists_all_paragraphs(output_dir):
    with open(os.path.join(output_dir, "index.txt")) as f:
        content = f.read()
    assert "1-2" in content
    assert "1-18" in content


def test_filename_zero_padded(output_dir):
    # paragraph 1-18 should be ch01_p018.txt not ch01_p18.txt
    files = os.listdir(output_dir)
    assert "ch01_p018.txt" in files
    assert "ch01_p18.txt" not in files
