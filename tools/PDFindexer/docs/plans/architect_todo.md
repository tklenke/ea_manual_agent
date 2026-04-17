# Architect Todo

## Completed Work (as of 2026-04-15)

Initial design, library selection, output format, pipeline design, token optimization,
all documented in design.md. CMW (claude-maintenance-writer) defined as the consumer.

Design revisions after implementation review:
- CHG 1 format: body text uses no period after paragraph number; Chapter 13 has no
  section headers in TOC. Both documented in design.md "CHG 1 Format" section.
- Three appendices confirmed (Glossary p.633-641, Acronyms p.642-645, Metric p.646).
  Extraction approach and filenames documented in design.md.
- Soft hyphen (U+00AD) found in CHG 1 pages — fix must strip \xad before joining,
  not just handle whitespace around regular hyphens.

## Open Items

- [ ] Validate index.txt and spot-check output files once Phases 8-10 are complete
- [ ] Confirm output is usable by CMW after full pipeline re-run
- [ ] README.md review once Programmer drafts it (Phase 10)
