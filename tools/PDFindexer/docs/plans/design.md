# PDFindexer Design

## Purpose

Extract the content of FAA AC 43.13-1B ("Acceptable Methods, Techniques, and Practices -
Aircraft Inspection and Repair") into a structured set of plain text files consumable by
CMW (claude-maintenance-writer) — the Claude instance that writes aircraft-specific
maintenance procedures for the Cozy Mark IV ea_mxmanual project.

CMW workflow: read index.txt to identify relevant paragraphs by title, open only those
paragraph files, incorporate FAA guidance into the specific aircraft procedure.

## Source Document

- File: `docs/references/ac_43.13.pdf`
- Type: Born-digital PDF (real selectable text, no OCR needed)
- Size: 646 pages, 13 chapters, variable sections per chapter
- Layout: Two-column body text with embedded figures (images) and tables (PDF table objects)
- Page numbering: Chapter-relative format (e.g., Page 1-1, Page 1-2)
- Paragraph numbering: Chapter-relative format (e.g., 1-1, 1-2, 2-1, 2-2)
- TOC: Pages 2 through 34
- Note: Later sections (Ch.12 Section 5, Ch.13, Appendices) are Change 1 additions
  dated 9/27/01 vs. the original 9/8/98 date. Change 1 body pages use a different
  paragraph marker format (no period after number: "12-70 GENERAL." vs "12-70. GENERAL.")

## Output Location

`data/` within the PDFindexer repo. Tom will copy the output to the ea_mxmanual project
(`docs/references/FAA43_13/`) manually after the program runs successfully.

## Output Structure

```
data/
  index.txt                  <- master index; CMW reads this first
  ch01_p001.txt              <- paragraph 1-1
  ch01_p002.txt              <- paragraph 1-2
  ...
  ch13_p001.txt              <- paragraph 13-1
  ch13_p002.txt              <- paragraph 13-2
  appendix_1_glossary.txt    <- Appendix 1: Glossary (PDF pages 633-641)
  appendix_2_acronyms.txt    <- Appendix 2: Acronyms and Abbreviations (PDF pages 642-645)
  appendix_3_metric.txt      <- Appendix 3: Metric-Based Prefixes and Powers of 10 (PDF page 646)
```

### index.txt Format

Plain text. Optimized for CMW to scan quickly and identify relevant paragraphs without
opening any content files.

```
AC 43.13-1B — Acceptable Methods, Techniques, and Practices

CHAPTER 1: WOOD STRUCTURE

  SECTION 1: MATERIALS AND PRACTICES
    1-1  General [ch01_p001.txt]
    1-2  Woods [ch01_p002.txt]
    ...

  SECTION 2: HEALTH AND SAFETY
    1-18  General [ch01_p018.txt]
    ...

CHAPTER 13: HUMAN FACTORS
  13-1  Human Factors Influence on Mechanic's Performance [ch13_p001.txt]
  13-2  The FAA Aviation Safety Program [ch13_p002.txt]

APPENDICES
  Appendix 1: Glossary [appendix_1_glossary.txt]
  Appendix 2: Acronyms and Abbreviations [appendix_2_acronyms.txt]
  Appendix 3: Metric-Based Prefixes and Powers of 10 [appendix_3_metric.txt]
```

Note: Chapter 13 has no sections in the TOC — paragraphs listed directly under chapter.

### Paragraph File Format

Plain text (`.txt`). No markdown syntax. Optimized to minimize tokens while preserving
all content CMW needs.

```
AC 43.13-1B  Chapter 1: Wood Structure  Section 1: Materials and Practices

1-2. WOODS.

  a. Quality of Wood.  All wood and plywood used in the repair of aircraft structures
  should be of aircraft quality...

  [TABLE 1-1]

  b. Substitution of Original Wood.  The wood species used to repair a part should
  be the same as that of the original whenever possible...

  [FIG 1-1]
```

### Appendix File Format

Plain text, extracted as-is from the PDF pages without paragraph splitting. Header
line identifies the appendix.

```
AC 43.13-1B  Appendix 1: Glossary

abrasion resistant PTFE  a solid insulation wall of PTFE with hard, nonconductive
grit positioned midway in the wall thickness...

acetylene  gas composed of two parts of carbon and two parts of hydrogen...
```

## Token Optimization Decisions

1. Plain text files, not markdown — no syntax overhead
2. Page headers/footers stripped — repeat on every page, pure noise
3. Compact figure/table markers — [FIG 1-1] and [TABLE 1-1]
4. Paragraph titles in index — CMW determines relevance from index alone without
   opening content files; typical query reads index once + 1-3 paragraph files
5. Short filenames — ch01_p001.txt; titles are already in the index
6. Paragraph-level granularity — CMW reads only the specific paragraphs it needs
7. Hyphenated line-break words joined throughout — original pages use regular hyphens
   (U+002D); CHG 1 pages use soft hyphens (U+00AD, \xad). Both are stripped and the
   word joined: "recom\xad\nended" → "recommended", "construc-\ntion" → "construction"

## Processing Pipeline

### Phase 1: TOC Extraction (pages 2-34)

Parse the TOC to build the complete expected structure:
- Chapter numbers and titles
- Section numbers and titles per chapter (some chapters have no sections — Ch.13)
- Paragraph numbers and titles per section (or directly under chapter if no sections)
- Page numbers (used for validation and index)

### Phase 2: Content Extraction (pages 35-632)

Walk pages sequentially. For each page:
1. Strip header and footer
2. Extract text with column awareness
3. Detect paragraph boundaries using TWO patterns:
   - Original format: `^(\d+-\d+)\.` (number + period)
   - CHG 1 format: `^(\d+-\d+)\s+[A-Z]` (number + space + capital, no period)
4. Detect figures; insert [FIG X-X] marker
5. Detect tables; insert [TABLE X-X] marker

Join hyphenated line-break words throughout. Two hyphen types used in this document:
- Regular hyphen U+002D (`-`): original pages
- Soft hyphen U+00AD (`\xad`): CHG 1 pages
Strip \xad first, then apply: `r"(\w+)-\s*\n\s*(\w+)"`. Or match both in one pass:
`r"(\w+)[\-\xad]\s*\n\s*(\w+)"`

### Phase 3: Appendix Extraction (pages 633-646)

Extract plain text from appendix pages without paragraph splitting:
- Appendix 1 (Glossary): PDF pages 633-641
- Appendix 2 (Acronyms): PDF pages 642-645
- Appendix 3 (Metric): PDF page 646

Apply same column-aware extraction and header/footer stripping as Phase 2.
Join hyphenated line-break words.

### Phase 4: Output Writing

- Write paragraph files (ch##_p###.txt)
- Write appendix files
- Write index.txt including appendices section

## Two-Column Handling

The body text uses a two-column layout. Naive pdfplumber extraction interleaves columns.

Approach: Use pdfplumber `extract_words()` to get words with bounding boxes. For each
page, determine the column midpoint (approximately x=306 for a standard letter page).
Classify lines as full-width (centered headers: spans midpoint AND min_x > 150),
left-column (x < 306), or right-column (x >= 306). Reconstruct left column first,
then right column. Full-width lines merged into left by y-position.

## Library

**pdfplumber** — column-aware extraction via `extract_words()`, table detection,
image/figure detection via `page.images`.

## Figure Handling

When pdfplumber detects an image on a page, insert [FIG X-X] at the appropriate
point in the text flow. The caption text follows the image in the PDF and is
extracted as normal text.

## Table Handling

Tables extracted as plain text with [TABLE X-X] marker. Table title appears above
the table in the PDF and is extracted as normal text.

## Paragraph Numbering

Chapter-relative (1-1 through 1-N, etc.). Filenames zero-padded to 3 digits using
the paragraph's own number: ch01_p036.txt for paragraph 1-36.

## CHG 1 Format (Change 1, dated 9/27/01)

Sections affected: Chapter 12 Section 5 (paragraphs 12-70 to 12-72), Chapter 13.

Body text paragraphs use no period after the number:
  `12-70 GENERAL.` (CHG 1) vs `12-70. GENERAL.` (original)

TOC entries for these paragraphs DO have periods (same as original format).

TOC structural difference: Chapter 13 has no section headers — paragraphs listed
directly under the chapter. TOC parser must handle chapters with no sections.

## Known Challenges

- Reserved paragraph ranges (e.g., "1-12. 1-17. [RESERVED.]") — treated as a single
  short paragraph
- Sub-paragraphs (a., b., c.) are part of the parent paragraph content
- Some paragraphs span multiple pages
- Cross-column duplicate paragraph numbers — merged into original paragraph

## Out of Scope

- Image extraction (figures noted with markers only)
- Hyperlinks or cross-references
- Any output format other than plain text
