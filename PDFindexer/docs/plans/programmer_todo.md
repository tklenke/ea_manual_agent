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

## Phase 9: Appendix Extraction — COMPLETE

See design.md "Phase 3: Appendix Extraction" section.

Page ranges (1-indexed PDF page numbers):
  Appendix 1 Glossary:  pages 633-641
  Appendix 2 Acronyms:  pages 642-645
  Appendix 3 Metric:    page  646

- [x] Extract PDF pages 633-634 as tests/fixtures/ac_43_13_appendix_excerpt.pdf
- [x] Implement pdfindexer/appendix_extractor.py (strips PUA leader chars, joins hyphens)
- [x] Write tests for appendix_extractor.py (10 tests)
- [x] Update output_writer.py — write appendix files and APPENDICES section in index.txt
- [x] Update __main__.py — run appendix extraction after main content pass
- [x] Re-run full pipeline — 3 appendix files present; 665 total files

## Phase 10: Hyphenation Fix and README — COMPLETE

- [x] Fix soft hyphens in doc_parser.py: re.sub(r'\xad\n\s*', '') + text.replace('\xad','')
- [x] Fix soft hyphens in appendix_extractor.py: same approach
- [x] Write tests: soft-hyphenated words joined in both body and appendix contexts
- [x] Create README.md: purpose, CMW consumer, how to run, output structure,
      known gaps (5 paragraphs undetected: 9-17, 10-17, 11-54, 11-55, 11-56)

## Phase 11: Mid-line Paragraph Marker Fix — COMPLETE

- [x] Rebuild CHG 1 fixture to include PDF page 431 (9-17 mid-line case) at index 1
- [x] Write failing tests: test_para_9_17_detected, test_para_9_17_has_chapter_metadata,
      test_para_9_17_text_starts_at_marker
- [x] Fix _split_paragraphs in doc_parser.py: secondary mid-line detection using
      mid_para_pattern; only triggers when no lowercase precedes the number
      (avoids false positives from body-text cross-references)
- [x] Re-run full pipeline: 662/666 paragraphs; 9-17 now in output
- [x] Update README.md known gaps: 4 remaining paragraphs with root causes documented
      (10-17: header cutoff; 11-54/55/56: TOC/body numbering inconsistency in source PDF)
