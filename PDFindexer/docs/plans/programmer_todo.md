# Programmer Todo

Read docs/plans/design.md fully before starting any task.

## Completed (Phases 1-7)

Project setup, TOC parser, page extractor, doc parser, output writer, main entry point,
and full pipeline run are all complete. 37 tests passing. 648/656 paragraphs extracted.
See git log for details.

## Phase 8: CHG 1 Format Support — COMPLETE

- [x] Extract PDF pages 631-632 as tests/fixtures/ac_43_13_chg1_excerpt.pdf
- [x] Update toc_parser.py — handle chapters with no section headers (Ch.13 has none);
      synthetic section {number: 0, title: "", paragraphs: []} created on demand;
      also made trailing period optional in TOC para entry (some CHG 1 entries omit it)
- [x] Write tests: 13-1 and 13-2 appear in TOC parse with correct chapter metadata
- [x] Update doc_parser.py — paragraph boundary also matches CHG 1 format `^(\d+-\d+)\s+[A-Z]`
- [x] Write tests: 12-70 and 13-1 detected from CHG 1 body text
- [x] Re-run full PDF — 12-70/71/72 and 13-1/13-2 now in output; 661/666 paragraphs
- [x] output_writer.py updated to omit SECTION line for synthetic sections (Ch.13)

## Phase 9: Appendix Extraction

See design.md "Phase 3: Appendix Extraction" section.

Page ranges (1-indexed PDF page numbers):
  Appendix 1 Glossary:  pages 633-641
  Appendix 2 Acronyms:  pages 642-645
  Appendix 3 Metric:    page  646

- [ ] Extract PDF pages 633-634 as tests/fixtures/ac_43_13_appendix_excerpt.pdf
- [ ] Implement pdfindexer/appendix_extractor.py
      extract_appendix(pdf, start_page, end_page, title) → plain text string
      Uses page_extractor.extract_page() for column-aware text; joins pages;
      applies hyphen joining; strips headers/footers
- [ ] Write tests for appendix_extractor.py
- [ ] Update output_writer.py — write appendix files and APPENDICES section in index.txt
- [ ] Update __main__.py — run appendix extraction after main content pass
- [ ] Re-run full pipeline — verify 3 appendix files present and readable

## Phase 10: Hyphenation Fix and README

- [ ] Fix hyphenation in doc_parser.py and appendix_extractor.py:
      CHG 1 pages use soft hyphens (U+00AD, \xad) instead of regular hyphens for
      line breaks. Current regex only matches regular hyphens and misses these.
      Fix: strip \xad characters first, then apply hyphen-join regex.
      Specifically in _join_hyphens(): text = text.replace('\xad', '') before the re.sub,
      OR use regex pattern r"(\w+)[\-\xad]\s*\n\s*(\w+)" to match both in one pass.
- [ ] Write test: soft-hyphenated word (e.g. "recom\xad\nmended") → "recommended"
- [ ] Create README.md:
      - What PDFindexer does and who uses it (CMW)
      - How to run: python -m pdfindexer <pdf_path> <output_dir>
      - Output structure
      - Known gaps (8 paragraphs not detected, reason)
