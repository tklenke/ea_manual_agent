# Required From Tom

Items needed before or during implementation that require Tom's input or action.

## Before Implementation

- [x] Output location: write to `data/` within PDFindexer repo; Tom copies to ea_mxmanual
      project manually after successful run (decided 2026-04-15)

## During Implementation

- [x] Test fixture: `tests/fixtures/ac_43_13_excerpt.pdf` created — contains PDF pages
      2 (TOC, Chapter 1) and 35-40 (first content pages of Chapter 1). 7 pages total.

## Decisions Made

- [x] Output granularity: paragraph-level files (decided 2026-04-15)
- [x] Output format: plain text (.txt), not markdown (decided 2026-04-15)
- [x] Figure handling: text placeholder [FIG X-X, p.X-X], no image extraction (decided 2026-04-15)
- [x] Index richness: include paragraph titles so Claude can determine relevance without
      opening content files (decided 2026-04-15)
