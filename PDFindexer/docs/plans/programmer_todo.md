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

- [x] Write failing tests for output format
- [x] Implement output_writer.py — writes ch##_p###.txt paragraph files and index.txt
      - Paragraph files: plain text, header line + content, no markdown
      - index.txt: chapter/section/paragraph listing with filenames
      - Filenames zero-padded to 3 digits using paragraph number within chapter
- [x] 10 tests passing; 37 total

## Phase 6: Main Entry Point

- [x] Implement __main__.py — orchestrates full pipeline with CLI args (pdf_path, output_dir, --toc-end)
- [x] Ran against full ac_43.13.pdf: 648/656 paragraphs extracted (98.8%), 649 files written
      Known gaps (8 paragraphs not found in body text): 9-17, 10-17, 11-54/55/56, 12-70/71/72
      Chapter 13 (Human Factors) has no body content in this PDF edition
      Fixed duplicate paragraph detection bug — merged cross-column re-occurrences correctly

## Phase 7: Full Run and Validation

- [x] Run against full ac_43.13.pdf, writing output to data/
- [x] Verified file count: 648 paragraph files + index.txt = 649 total
- [x] Spot-checked paragraph files — content accurate, headers correct, markers working
- [x] index.txt confirmed: 13 chapters, all sections, 648/656 paragraphs with filenames
- [x] 8 paragraphs listed in index without filenames (not detectable from body text layout)
- [x] Reported known gaps to Architect — see architect_todo.md Phase 4

## Phase 8: CHG 1 Format Support

Architect decisions complete. See design.md "CHG 1 Format" section.

- [ ] Extend test fixture: extract PDF pages 631 and 632 into a new fixture file
      tests/fixtures/ac_43_13_chg1_excerpt.pdf (Ch.12 Section 5 + Ch.13)
- [ ] Update toc_parser.py to handle chapters with no section headers
      — paragraphs listed directly under chapter must still be captured
      — simplest approach: if no current_section when paragraph found, create a
        synthetic section {number: 0, title: "", paragraphs: []} on demand
- [ ] Write tests for CHG 1 TOC parsing (13-1 and 13-2 present, correct metadata)
- [ ] Update doc_parser.py paragraph boundary detection to also match CHG 1 format:
      `^(\d+-\d+)\s+[A-Z]` in addition to existing `^(\d+-\d+)\.`
- [ ] Write tests for CHG 1 body text extraction (12-70 detected, 13-1 detected)
- [ ] Re-run full PDF — verify 12-70/71/72 and 13-1/13-2 now appear in output

## Phase 9: Appendix Extraction

Architect decisions complete. See design.md "Phase 3: Appendix Extraction" section.
Three appendices, all plain text extraction (column-aware, no paragraph splitting).

Page ranges (PDF page numbers, 1-indexed):
  Appendix 1 Glossary:    pages 633-641  (10 pages per TOC, two-column dictionary)
  Appendix 2 Acronyms:    pages 642-645  (4 pages per TOC)
  Appendix 3 Metric:      page  646      (1 page per TOC)

- [ ] Implement pdfindexer/appendix_extractor.py
      - extract_appendix(pdf, start_page, end_page, title) → plain text string
      - Uses existing page_extractor.extract_page() for column-aware text
      - Joins pages, applies hyphen joining, strips headers/footers
- [ ] Write tests for appendix_extractor.py using a fixture of appendix pages
      (extract PDF pages 633-634 as tests/fixtures/ac_43_13_appendix_excerpt.pdf)
- [ ] Update output_writer.py to write appendix files and add APPENDICES section
      to index.txt
- [ ] Update __main__.py to run appendix extraction after main content pass
- [ ] Re-run full pipeline — verify 3 appendix files present and readable

## Phase 10: Hyphenation and README

- [ ] Tighten hyphenation regex in doc_parser.py:
      change r"(\w)-\n(\w)" to r"(\w+)-\s*\n\s*(\w+)"
      also apply same fix in appendix_extractor.py
- [ ] Create README.md documenting:
      - What PDFindexer does
      - How to run it (python -m pdfindexer <pdf> <output_dir>)
      - Output structure and what CMW does with it
      - Known gaps (8 paragraphs, reason)
