# Architect Todo

## Phase 1: Design

- [x] Gather requirements from Tom
- [x] Evaluate PDF characteristics (born-digital, two-column layout, figure/table types)
- [x] Decide output granularity (paragraph-level files)
- [x] Design token-optimized output format (plain text, compact markers, rich index)
- [x] Design processing pipeline (TOC pass, content pass, output writing)
- [x] Document two-column extraction approach
- [x] Select library (pdfplumber)
- [x] Write design.md
- [x] Update claude/project_status.md
- [x] Create docs/plans/ structure

## Phase 2: Implementation Support

- [x] Review programmer_todo.md tasks once Programmer begins
- [x] Review sample output from early implementation runs for quality
- [x] Address architectural questions that arose during implementation (see Phase 4 below)

## Phase 3: Validation

- [ ] Validate index.txt structure and completeness against TOC
- [ ] Spot-check several paragraph files for content accuracy
- [ ] Confirm output is usable by mxmanual Claude instance (CMW — see Phase 4)

## Phase 4: Design Revisions (completed 2026-04-15)

### Issue A: CHG 1 Format Paragraphs — RESOLVED

Inspected TOC pages 33-34. Findings:
- TOC entries for 12-70/71/72 and Ch.13 DO have periods (same format as original)
- Root cause for missing paragraphs: TWO separate bugs
  1. Body text uses no period: `12-70 GENERAL.` — regex must also match this format
  2. Chapter 13 has NO section headers in the TOC — parser required a section before
     accepting paragraph entries, so 13-1 and 13-2 were silently dropped

- [x] Decision: update paragraph boundary regex to also match `^(\d+-\d+)\s+[A-Z]`
- [x] Decision: update TOC parser to accept paragraphs directly under chapter (no section)
      — represent as chapter with section number=0 and title="" in the data structure,
      OR handle at the chapter level directly; Programmer to choose simpler approach
- [x] Documented in design.md under "CHG 1 Format"

### Issue B: Appendices — RESOLVED

TOC page 34 reveals THREE appendices (not two):
- Appendix 1: Glossary — 10 pages, PDF pages 633-641
- Appendix 2: Acronyms and Abbreviations — 4 pages, PDF pages 642-645
- Appendix 3: Metric-Based Prefixes and Powers of 10 — 1 page, PDF page 646

- [x] Decision: extract all three as plain text files (column-aware, no paragraph splitting)
- [x] Decision: filenames: appendix_1_glossary.txt, appendix_2_acronyms.txt, appendix_3_metric.txt
- [x] Decision: add APPENDICES section at bottom of index.txt
- [x] Decision: page ranges hardcoded in __main__.py (known from TOC)
- [x] Documented in design.md

### Issue C: CMW References — RESOLVED

- [x] CMW (claude-maintenance-writer) defined and documented in design.md
- [ ] Create README.md for PDFindexer repo — delegate to Programmer (Phase 10)

### Issue D: Hyphenation — RESOLVED

- [x] Decision: tighten regex to `r"(\w+)-\s*\n\s*(\w+)"` — handles edge cases,
      no downside, Programmer to implement in Phase 10
