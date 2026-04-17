# wikiCheck Spec

## Purpose

Command-line script that reports wiki integrity status. Designed to be run at the start of a Reviewer session and output a compact summary suitable for pasting into a Claude conversation.

## Inputs

- **WR path:** `/home/tom/projects/N657CZDashTwo`
- **AR review log path:** `docs/notes/review_log.md` (relative to AR root)

## Checks

### Broken Link Check

Scan all WR `.md` files for DokuWiki internal links:
- `[[page-slug]]`
- `[[page-slug|Display Text]]`

Extract target slugs. Check which slugs have no corresponding `.md` file in the WR. Report count and list.

### Review Log Check

- Read datestamp from `docs/notes/review_log.md`
- Glob all WR `.md` pages
- Grep review log for page entries
- Identify WR pages missing from the log entirely
- Count entries with status `unreviewed`

## Output

Compact plain-text summary (default):

```
Wiki Integrity Report — YYYY-MM-DD
Broken links:            12  (pages referenced but not yet written)
Unreviewed pages:         8  (in log, never reviewed)
Pages missing from log:   3  (in WR, not in log)
Review log last updated: YYYY-MM-DD (N days ago)
```

With `--detail` flag: full lists of broken links, unreviewed pages, and pages missing from log.

## Flags

- `--detail` — print full lists in addition to summary counts
- `--seed` — write all WR pages to review log with status `unreviewed`; asks confirmation before writing

## Review Log Format

File: `docs/notes/review_log.md` in AR.

```
# Review Log
Last updated: YYYY-MM-DD

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| manual-standards | unreviewed | — |
```
