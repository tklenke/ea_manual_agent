# PDFindexer

Extracts FAA AC 43.13-1B ("Acceptable Methods, Techniques, and Practices —
Aircraft Inspection and Repair") into a structured set of plain text files
for use by CMW (claude-maintenance-writer).

## Background

CMW is the Claude instance that writes aircraft-specific maintenance procedures
for the Cozy Mark IV ea_mxmanual project. It reads `index.txt` to find relevant
FAA paragraphs by title, then opens only those files to incorporate guidance
into specific procedures. The output is optimized for token efficiency: plain
text, no markdown, compact figure/table markers, paragraph-level granularity.

## How to run

```
python -m pdfindexer <pdf_path> <output_dir>
```

Example:

```
python -m pdfindexer docs/references/ac_43.13.pdf data/
```

The source PDF (`ac_43.13.pdf`) is not included in this repo. Place it at
`docs/references/ac_43.13.pdf` before running.

## Output structure

```
data/
  index.txt                       ← master index; CMW reads this first
  ch01_p001.txt                   ← paragraph 1-1
  ch01_p002.txt                   ← paragraph 1-2
  ...
  ch13_p001.txt                   ← paragraph 13-1
  ch13_p002.txt                   ← paragraph 13-2
  appendix_1_glossary.txt
  appendix_2_acronyms.txt
  appendix_3_metric.txt
```

`index.txt` lists every chapter, section, and paragraph title with its
filename. CMW scans the index to decide which files to open — typically
one index read plus 1–3 paragraph files per query.

Paragraph files begin with a breadcrumb header line:

```
AC 43.13-1B  Chapter 1: WOOD STRUCTURE  Section 1: MATERIALS AND PRACTICES

1-2. WOODS.

  a. Quality of Wood.  All wood and plywood used in the repair of aircraft
  structures should be of aircraft quality...

  [TABLE 1-1]

  b. Substitution of Original Wood.  ...

  [FIG 1-1]
```

Appendix files begin with a matching header and contain plain extracted text
with terms and definitions separated by two spaces (converted from the PDF's
dot leaders):

```
AC 43.13-1B  Appendix 1: Glossary

abrasion resistant PTFE  a solid insulation wall of PTFE with hard,
nonconductive grit positioned midway in the wall thickness...

acetylene—gas composed of two parts of carbon and two parts of hydrogen...
```

## Pipeline

| Phase | What it does |
|-------|-------------|
| TOC parse (pp. 2–34) | Builds chapter/section/paragraph structure from the table of contents |
| Content extract (pp. 35–632) | Walks body pages; splits on paragraph numbers; inserts [FIG] / [TABLE] markers |
| Appendix extract (pp. 633–646) | Extracts Glossary, Acronyms, and Metric appendices as plain text |
| Output write | Writes `ch##_p###.txt`, appendix files, and `index.txt` |

## Known gaps

662 of 666 TOC paragraphs are extracted. The 4 unextracted paragraphs have
root causes that cannot be addressed with pattern changes alone:

- 10-17  Weight and Balance Extreme Conditions — paragraph marker sits at
  y=64.3, just below the HEADER_CUTOFF=65 filter; the word is stripped as
  a page header before extraction reaches the splitter.
- 11-54  Relays
- 11-55  Load Considerations
- 11-56  Operating Conditions for Switches and Relays — the body text uses
  paragraph numbers 11-48/49/50 for the same content; the TOC numbers and
  body numbers diverge due to an inconsistency in the source PDF.

These paragraphs appear in `index.txt` without a filename. CMW will not be
able to open them directly but can still see their titles in the index.

## Development

```
python -m pytest          # run all tests (64 tests)
```

Tests use small PDF fixtures in `tests/fixtures/` rather than the full PDF.
See `docs/plans/design.md` for architecture details.
