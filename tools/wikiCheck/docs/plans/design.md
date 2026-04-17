# wikiCheck Design

## Purpose

Check the integrity of the wiki reference (WR) and the AR review log. Produces a
compact summary suitable for pasting into a Claude session at the start of a Reviewer
session.

## Inputs

- **WR (wiki reference):** `/home/tom/projects/N657CZDashTwo` — directory of `.md` files
- **AR review log:** `<ea_mxmanual>/docs/notes/review_log.md`

## Output

Compact plain-text summary printed to stdout:

```
Wiki Integrity Report — YYYY-MM-DD
Broken links:            12  (pages referenced but not yet written)
Unreviewed pages:         8  (in log, never reviewed)
Pages missing from log:   3  (in WR, not in log)
Review log last updated: 2026-04-10 (6 days ago)
```

## Flags

- `--detail` — append full lists of broken links, unreviewed pages, and missing pages
- `--seed` — write all WR pages to review log with status `unreviewed`; prompts Tom
  for confirmation before writing

## Checks

### Broken link check

Scan all WR `.md` files for DokuWiki internal links in these formats:
- `[[page-slug]]`
- `[[page-slug|Display Text]]`

Extract target slugs. A broken link is a slug with no corresponding `.md` file in the
WR. Report count (and list under `--detail`).

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

### Seeding

First Reviewer session runs `wiki_check.py --seed`. The script:
1. Globs all WR `.md` pages
2. Prints the list and asks Tom to confirm before writing
3. Writes `review_log.md` with all pages marked `unreviewed` and today's date as
   `Last updated:`

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
