# Architect Todo

## Active: Consolidate tools/ shared structure (2026-04-16)

**Goal:** As tools/ grows beyond PDFindexer to include wikiCheck and future tools, lift
shared concerns (acronyms, style guide, architect oversight) to tools/docs/ so they
don't drift per-tool. Keep per-tool plans/design/programmer_todo where they belong.

### Target structure

```
tools/
  docs/
    acronyms.md              <- lifted from PDFindexer/docs/; shared across all tools
    style-guide.md           <- lifted from PDFindexer/docs/; shared across all tools
    plans/
      architect_todo.md      <- this file; single view of all cross-tool architect work
  PDFindexer/
    docs/
      plans/
        design.md            <- keep (tool-specific)
        programmer_todo.md   <- keep (tool-specific)
        required_from_tom.md <- keep (tool-specific)
      references/            <- keep (tool-specific, READ ONLY)
      # acronyms.md REMOVED (moved to tools/docs/)
      # style-guide.md REMOVED (moved to tools/docs/)
      # plans/architect_todo.md REMOVED (merged here)
  wikiCheck/
    docs/
      plans/
        design.md            <- to be created (wikiCheck spec)
        programmer_todo.md   <- to be created
        # plans/architect_todo.md REMOVED (merged here)
  claude/
    roles/
      architect.md           <- update path references
      programmer.md          <- update path references
      code_reviewer.md       <- update path references
    project_status.md        <- update to multi-tool scope + new paths
  CLAUDE.md                  <- update path references
```

### Implementation steps

- [x] Create tools/docs/plans/ directory
- [x] Write this architect_todo.md
- [x] git mv PDFindexer/docs/acronyms.md → tools/docs/acronyms.md
- [x] git mv PDFindexer/docs/style-guide.md → tools/docs/style-guide.md
- [x] Merge PDFindexer architect_todo content into this file (PDFindexer section below)
- [x] Remove tools/PDFindexer/docs/plans/architect_todo.md (content merged here)
- [x] Merge wikiCheck architect_todo content into this file (wikiCheck section below)
- [x] Remove tools/wikiCheck/docs/plans/architect_todo.md (content merged here)
- [x] Update claude/roles/architect.md path references
- [x] Update claude/roles/programmer.md path references
- [x] Update claude/roles/code_reviewer.md path references
- [x] Update claude/project_status.md — multi-tool scope, new shared paths
- [x] Update tools/CLAUDE.md if it references old paths
- [x] Commit

---

## PDFindexer

### Completed (as of 2026-04-15)

Initial design, library selection, output format, pipeline design, token optimization,
all documented in design.md. CMW (claude-maintenance-writer) defined as consumer.

Design revisions after implementation review:
- CHG 1 format: body text uses no period after paragraph number; Chapter 13 has no
  section headers in TOC. Both documented in design.md "CHG 1 Format" section.
- Three appendices confirmed (Glossary p.633-641, Acronyms p.642-645, Metric p.646).
  Extraction approach and filenames documented in design.md.
- Soft hyphen (U+00AD) found in CHG 1 pages — fix must strip \xad before joining.

### Open

- [ ] Validate index.txt and spot-check output files once Phases 8-10 are complete
- [ ] Confirm output is usable by CMW after full pipeline re-run
- [ ] README.md review once Programmer drafts it (Phase 10)

---

## wikiCheck

### Open

- [x] Promote spec from architect_todo to a proper design.md in wikiCheck/docs/plans/
- [x] Write `wiki_check.py` (see spec below)
- [ ] Add orphan page detection to wikiCheck — pages that exist in WR but are never linked
      to from any other WR page. Include count in summary report and list under `--detail`.
      Logic is the inverse of broken links: build set of all link targets across WR, flag
      any existing page not in that set. No separate tracking file — live scan is
      authoritative. No valid use case for intentionally unlinked pages in this manual.
      (Requested 2026-04-16)
- [ ] Create `docs/notes/review_log.md` format spec (in AR — ea_mxmanual project)
- [ ] Update `claude/roles/reviewer.md` (in AR — ea_mxmanual project)
- [ ] Document `docs/notes/` in `claude/project_status.md` (in AR)

### Spec (from original wikiCheck architect_todo)

Script operates on the WR at `/home/tom/projects/N657CZDashTwo` and the AR review log
at `docs/notes/review_log.md`.

**Broken link check:** Scan all WR `.md` files for DokuWiki internal links
(`[[page-slug]]` and `[[page-slug|Display Text]]`). Extract target slugs. Check which
slugs have no corresponding `.md` file in the WR. Report count and list.

**Review log check:**
- Read datestamp from `docs/notes/review_log.md` (AR)
- Glob all WR `.md` pages
- Grep review log for page entries; identify WR pages missing from the log
- Report: log age, count of unreviewed pages (status = `unreviewed`), count of WR pages
  missing from log entirely

**Output format:** Compact plain-text summary:
```
Wiki Integrity Report — 2026-04-16
Broken links:            12  (pages referenced but not yet written)
Unreviewed pages:         8  (in log, never reviewed)
Pages missing from log:   3  (in WR, not in log)
Review log last updated: 2026-04-10 (6 days ago)
```

**Flags:**
- `--detail` — print full lists of broken links, unreviewed pages, and missing pages
- `--seed` — write all WR pages to review log with status `unreviewed`; asks
  confirmation before writing

**review_log.md format:**
```
# Review Log
Last updated: YYYY-MM-DD

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| manual-standards | unreviewed | — |
```

**Reviewer startup integration:**
1. Run `tools/wikiCheck/wiki_check.py` (or ask Tom to run it and paste output)
2. Report summary to Tom
3. Ask about log updates and link check scope
4. If log needs seeding: walk Tom through seeding step
5. After each page review: update review_log.md entry and commit

**Implementation order:** wiki_check.py → review_log format → reviewer.md → project_status.md
