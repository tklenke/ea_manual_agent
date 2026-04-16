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

- [x] Write failing test for two-column extraction using tests/fixtures/ac_43_13_excerpt.pdf
- [x] Implement page_extractor.py — extracts text with column awareness, strips header/footer,
      detects figures; classifies lines as full-width, left-col, or right-col based on x position
- [x] 10 tests passing
      Note: table detection deferred to doc_parser phase; tables appear across pages 36+ in fixture

## Phase 4: Document Parser

- [x] Write failing tests for paragraph boundary detection
- [x] Implement doc_parser.py — walks content pages, splits text into paragraphs,
      attaches chapter/section metadata, inserts [FIG] and [TABLE] markers,
      joins hyphenated line-break words
- [x] 12 tests passing; multi-page paragraphs and sub-paragraphs handled correctly

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
