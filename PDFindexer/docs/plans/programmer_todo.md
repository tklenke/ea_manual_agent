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

## Phase 8: CHG 1 Format Support (AWAITING ARCHITECT DECISIONS)

See architect_todo.md Phase 4 Issue A for full context. Do not start until Architect
has marked the decision items complete.

- [ ] Update toc_parser.py to handle CHG 1 paragraph entries (no period after number)
      Verify pages 33-34 of PDF to understand exact TOC format for Ch.13 entries
- [ ] Update doc_parser.py paragraph boundary regex to also match `^(\d+-\d+)\s+[A-Z]`
      for CHG 1 body text format
- [ ] Add test fixture pages covering a CHG 1 section (e.g. PDF page 631) to
      tests/fixtures/ and write tests for CHG 1 extraction
- [ ] Re-run full PDF and verify 12-70/71/72 and Ch.13 paragraphs now extracted

## Phase 9: Appendix Extraction (AWAITING ARCHITECT DECISIONS)

See architect_todo.md Phase 4 Issue B for full context. Do not start until Architect
has marked the decision items complete.

- [ ] Implement appendix extraction in a new module or extend output_writer.py
      - Extract pages 633-641 as appendix_1_glossary.txt (plain text, no paragraph splitting)
      - Extract pages 642-end as appendix_2_acronyms.txt
- [ ] Add appendix entries to index.txt (separate section at bottom of index)
- [ ] Write tests for appendix extraction
- [ ] Re-run full pipeline and verify appendix files are present and readable

## Phase 10: Documentation and CMW References (AWAITING ARCHITECT DECISIONS)

See architect_todo.md Phase 4 Issue C for full context.

- [ ] Create README.md for PDFindexer repo (usage instructions, output description,
      CMW usage pattern)
- [ ] Tighten hyphenation regex if Architect decides to (Issue D in architect_todo.md)
