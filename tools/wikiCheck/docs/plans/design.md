# wikiCheck Design

## Design Revision History

- **2026-04-17**: Added structural page exclusion to orphan detection. `home` and `readme`
  are expected orphans (nothing links to them by design); they are excluded from the
  orphan count and reported separately. Case-insensitive matching. Missing structural
  pages are errors. Phase 5 (AR integration) removed — handled outside this repo.

## Purpose

Check the integrity of the wiki reference (WR) and the AR review log. Produces a
compact summary suitable for pasting into a Claude session at the start of a Reviewer
session.

## Inputs

- **WR (wiki reference):** `/home/tom/projects/N657CZDashTwo` — directory of `.md` files
- **AR review log:** `<ea_mxmanual>/docs/notes/review_log.md`

## Output

**[REVISED - 2026-04-17]**

Compact plain-text summary printed to stdout:

```
Wiki Integrity Report — YYYY-MM-DD
Total WR pages:          47
Broken links:            12  (pages referenced but not yet written)
Orphan pages:             3  (exist in WR, never linked to)
Structural pages:         2  (home, readme — excluded from orphans)
Approved pages:          36  (of 47 in log)
Unreviewed pages:         8  (in log, never reviewed)
Pages missing from log:   3  (in WR, not in log)
Review log last updated: 2026-04-10 (6 days ago)
```

If a structural page is missing from WR entirely, append after the structural pages line:

```
ERROR: Structural page not in WR: home
```

If the review log is missing:

```
Wiki Integrity Report — YYYY-MM-DD
Total WR pages:          47
Broken links:            12  (pages referenced but not yet written)
Structural pages:         2  (home, readme — excluded from orphans)
Review log:              NOT FOUND — seeded template written to
                         tools/wikiCheck/data/review_log.md
                         move to: docs/notes/review_log.md
```

(ERROR lines appear after the structural pages line here too, if applicable.)

## Flags

- `--detail` — append full lists of broken links, orphan pages, unreviewed pages, and missing pages

## Checks

### Orphan page detection

**[REVISED - 2026-04-17]**

Scan all WR `.md` files for internal links using the same regex as broken link check.
Build a set of all referenced slugs. Any existing WR page whose slug does not appear in
that set is an orphan — it exists but is never linked to.

A helper `collect_referenced_slugs(wr_dir)` should be extracted from `broken_links.py`
so both checks share the same scan loop. `find_orphan_pages(wr_dir)` returns
`sorted(known - referenced)`, excluding structural pages (see below).

No separate tracking file — live scan is authoritative.

#### Structural page exclusion

`home` and `readme` are structural pages: they exist in the WR but are never linked to
by design (`home` is the Otterwiki entry point; `readme` is GitHub-facing). They are
excluded from the orphan count and reported on their own line.

Matching is **case-insensitive**: `Home.md`, `README.md`, etc. are all recognized.

**`STRUCTURAL_PAGES = ["home", "readme"]`** — hardcoded constant in `orphan_pages.py`.

Two functions handle structural pages:

- **`find_orphan_pages(wr_dir)`** — returns orphan slugs with structural pages removed.
  Signature unchanged.

- **`check_structural_pages(wr_dir)`** → `tuple[list[str], list[str]]`  
  Returns `(found, missing)` where:
  - `found` — structural pages that exist as `.md` files in WR (expected state)
  - `missing` — structural pages with no `.md` file in WR (error condition)  
  A structural page that exists and is linked to (not an orphan) is still "found" — not
  an error. Only absence from WR is an error.

The `Stats` dataclass carries `structural_pages_found: list[str]` and
`structural_pages_missing: list[str]`. `compute_stats()` calls
`check_structural_pages()`.

The `format_report()` and `format_missing_log_report()` functions add a structural
pages line and, if `structural_pages_missing` is non-empty, one ERROR line per missing
page. The `format_detail()` function adds a "Structural pages (excluded from orphans):"
section listing found pages, followed by any ERROR lines for missing ones.

### Broken link check

Scan all WR `.md` files for Otterwiki internal links in these formats:
- `[[Display Text|page-slug]]` — display text before the pipe, slug after
- `[[page-slug]]` — slug only, no display text

Regex: `\[\[(?:[^\]|]+\|)?([^\]|]+)\]\]` (capturing group = slug)

The WR is flat: slug `page-slug` maps to `page-slug.md` in the WR root.
A broken link is a slug with no corresponding `.md` file. Report count (and list under
`--detail`).

### Review log check

- Read `Last updated:` datestamp from `docs/notes/review_log.md`
- Glob all WR `.md` pages
- Parse review log for page entries
- **Unreviewed pages:** entries in the log with status `unreviewed`
- **Pages missing from log:** WR pages with no entry in the log at all
- Report: log age in days, unreviewed count, missing count

## review_log.md Format (in AR)

```
# Review Log
Last updated: YYYY-MM-DD

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| manual-standards | unreviewed | — |
```

Valid status values: `Approved`, `unreviewed`

### Missing review log

If `docs/notes/review_log.md` does not exist, the script:
1. Generates a seeded `review_log.md` (all WR pages, status `unreviewed`, today's date)
2. Writes it to `tools/wikiCheck/data/review_log.md`
3. Reports it in the summary with the expected destination path

Tom moves the file to `docs/notes/review_log.md` manually.

## Reviewer Integration

Add to Reviewer startup sequence (after reading standard files):

1. Run `tools/wikiCheck/wiki_check.py` (or ask Tom to run it and paste output)
2. Report summary to Tom
3. Ask: "The review log has N unreviewed pages and N pages missing from the log.
   Want me to update the log? Do you want to run a link check this session?"
4. If log needs seeding (first run, no log exists): walk Tom through seeding step

After completing each page review: update the `review_log.md` entry and commit.

## Implementation Notes

- Single script: `wiki_check.py` at `tools/wikiCheck/wiki_check.py`
- No dependencies beyond Python standard library (pathlib, re, datetime, argparse)
- AR path resolved relative to script location: `../../docs/notes/review_log.md`
- WR path hardcoded: `/home/tom/projects/N657CZDashTwo`
