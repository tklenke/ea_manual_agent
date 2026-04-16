# Programmer Todo

Read docs/plans/design.md fully before starting any task.

## Phase 1: Project Setup

- [x] Create requirements.txt with pdfplumber and pytest
- [x] Set up venv and install dependencies
- [x] Create pdfindexer/ package directory with __init__.py
- [x] Create tests/ directory with conftest.py
- [x] Verify pdfplumber can open and read the source PDF

## Phase 2: TOC Parser

- [x] Write failing test for TOC extraction using tests/fixtures/ac_43_13_excerpt.pdf
- [x] Implement toc_parser.py — extracts chapter/section/paragraph structure from TOC pages
      Output: list of chapter dicts with nested sections and paragraphs
- [x] Verify parser produces correct structure for Chapter 1 (all 4 sections, all paragraphs)
      Note: reserved paragraph ranges (1-12 to 1-17 etc.) are absent from TOC — handled correctly

## Phase 3: Page Text Extractor

- [ ] Write failing test for two-column extraction using tests/fixtures/ac_43_13_excerpt.pdf
      (pages 2-7 of fixture = PDF pages 35-40 = Chapter 1 Section 1 content)
- [ ] Implement page_extractor.py — extracts text from a single page with column awareness
      - Uses extract_words() with bounding boxes
      - Splits at page midpoint, sorts left then right column by y-coordinate
      - Strips page header (top ~50pt) and footer (bottom ~50pt)
- [ ] Implement figure detection — returns list of (y_position, page_label) for images on page
- [ ] Implement table detection — returns table text with [TABLE X-X, p.X-X] marker

## Phase 4: Document Parser

- [ ] Write failing tests for paragraph boundary detection
- [ ] Implement doc_parser.py — walks all content pages (35+), splits text into paragraphs
      - Detects paragraph boundaries by matching pattern "N-N." at start of text block
      - Associates each paragraph with its chapter/section from TOC structure
      - Inserts figure and table markers at correct positions in text flow
- [ ] Handle paragraphs that span multiple pages
- [ ] Handle sub-paragraphs (a., b., c.) as part of parent paragraph content

## Phase 5: Output Writer

- [ ] Write failing tests for output format
- [ ] Implement output_writer.py — writes paragraph files and index
      - Paragraph files: ch##_p###.txt with single header line + content
      - index.txt: full TOC with filenames, plain text format per design.md
- [ ] Verify filenames sort correctly (zero-padded paragraph numbers)

## Phase 6: Main Entry Point

- [ ] Implement main.py (or __main__.py) — orchestrates full pipeline
      - Accepts PDF path and output directory as arguments
      - Runs TOC parser, doc parser, output writer in sequence
      - Prints progress summary on completion
- [ ] Write integration test against a small page range of the real PDF

## Phase 7: Full Run and Validation

- [ ] Run against full ac_43.13.pdf, writing output to data/
- [ ] Verify output file count matches expected paragraph count from TOC
- [ ] Spot-check 5-10 paragraph files for content accuracy
- [ ] Confirm index.txt lists all chapters, sections, paragraphs with correct filenames
- [ ] Report any extraction quality issues to Architect
