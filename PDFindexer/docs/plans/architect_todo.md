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

## Phase 4: Design Revisions Required (discovered during implementation 2026-04-15)

### Issue A: CHG 1 Format Paragraphs

Pages 629-631 and Chapter 13 (p.632) are part of **Change 1** (dated 9/27/01 vs
original 9/8/98). CHG 1 paragraphs use a different format: no period after the
paragraph number (e.g. `12-70 GENERAL.` instead of `12-70. GENERAL.`).

Affected paragraphs not currently extracted:
- 12-70, 12-71, 12-72 (Section 5: Avionics Test Equipment, p.631)
- Chapter 13: 13-1, 13-2 (Human Factors, p.632) — content has periods so body
  extraction would work once TOC entries are found
- Chapter 13 TOC entries likely in CHG 1 format on the last TOC pages (need to check)

Decisions needed:
- [ ] Update paragraph boundary detection regex to also match `^(\d+-\d+)\s+[A-Z]`
      (number + space + capital, no period) for CHG 1 format
- [ ] Update TOC parser to handle CHG 1 format paragraph entries
- [ ] Verify pages 33-34 of PDF for Chapter 13 TOC entries and their format

### Issue B: Appendices

The PDF contains two appendices after Chapter 13:
- **Appendix 1: Glossary** (starts p.633, runs through ~p.641) — two-column
  dictionary format, terms in bold followed by definitions. No paragraph numbers.
- **Appendix 2: Acronyms** (starts p.642) — list format. No paragraph numbers.

These are valuable reference material for CMW (claude-maintenance-writer, the
Claude instance that writes the ea_mxmanual procedures) but do not follow the
paragraph structure of the main body.

Decisions needed:
- [ ] Determine output filenames: `appendix_1_glossary.txt` and `appendix_2_acronyms.txt`
- [ ] Decide how appendices are referenced in index.txt (separate section at bottom?)
- [ ] Determine page range for Appendix 2 (need to read p.642 to see format/end)
- [ ] Design extraction approach: plain text pass of those pages, no paragraph splitting

### Issue C: CMW References in Documentation

Tom confirmed the consumer of the output is **CMW (claude-maintenance-writer)** —
the Claude instance writing maintenance procedures for the Cozy Mark IV.

- [ ] Add CMW definition and usage pattern to design.md
- [ ] Create README.md for the PDFindexer repo documenting usage and output
- [ ] Update index.txt format to mention CMW usage context

### Issue D: Hyphenation Robustness

Current regex `r"(\w)-\n(\w)"` handles most line-break hyphenation. Edge case:
hyphens followed by optional whitespace before newline may be missed.

- [ ] Decide whether to tighten regex to `r"(\w+)-\s*\n\s*(\w+)"` for robustness
- [ ] Confirm with Tom whether any specific words in output are not being joined
