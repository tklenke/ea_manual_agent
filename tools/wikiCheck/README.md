# wikiCheck

Checks the integrity of the wiki reference (WR) and the AR review log.
Produces a compact plain-text summary for pasting into a Claude Reviewer session.

## Background

The WR (`/home/tom/projects/N657CZDashTwo`) is a flat directory of Otterwiki `.md`
files. Pages link to each other using `[[slug]]` or `[[Display Text|slug]]` syntax.
As the manual grows, pages get referenced before they are written — wikiCheck
counts those broken links. The AR review log (`ea_mxmanual/docs/notes/review_log.md`)
tracks which WR pages have been reviewed and approved. wikiCheck reports how stale
the log is and how many pages have never been reviewed.

## Setup

```
cd wikiCheck
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to run

```
python3 wiki_check.py
```

With detail lists appended:

```
python3 wiki_check.py --detail
```

## Normal output

When the review log exists:

```
Wiki Integrity Report — 2026-04-16
Total WR pages:          10
Broken links:             3  (pages referenced but not yet written)
System links:             1  (Otterwiki system calls, not checked)
Orphan pages:             2  (exist in WR, never linked to)
@@TOM flags:              4  (pages flagged for Tom's input)
Structural pages:         2  (home, readme — excluded from orphans)
Approved pages:           7  (of 10 in log)
Pending pages:            0  (reviewed, awaiting resolution)
Unreviewed pages:         2  (in log, never reviewed)
Pages missing from log:   1  (in WR, not in log)
Review log last updated: 2026-04-10 (6 days ago)
```

If a structural page (`home` or `readme`) is missing from the WR entirely, an
error line appears after the structural pages line:

```
ERROR: Structural page not in WR: home
```

With `--detail`, sorted lists are appended after a blank line:

```
Broken links:
  engine-mount
  fuel-system
  ...

Orphan pages:
  some-unreferenced-page
  ...

Pages with @@TOM flags:
  avionics
  fuel-system
  ...

Structural pages (excluded from orphans):
  home
  readme

Unreviewed pages:
  manual-standards-formatting
  record-of-revisions

Pages missing from log:
  panels-canopy-cleaning
```

If a section has no entries, it shows `(none)`.

## Missing review log output

If `docs/notes/review_log.md` does not exist, wikiCheck seeds a template and
reports where it was written:

```
Wiki Integrity Report — 2026-04-16
Total WR pages:          10
Broken links:             3  (pages referenced but not yet written)
Structural pages:         2  (home, readme — excluded from orphans)
Review log:              NOT FOUND — seeded template written to
                         /path/to/tools/wikiCheck/data/review_log.md
                         move to: docs/notes/review_log.md
```

Move the generated file to `ea_mxmanual/docs/notes/review_log.md` before the
next run. All entries start as `unreviewed`; update them as pages are reviewed.

## Output files

| Path | Description |
|------|-------------|
| stdout | Summary report (always printed) |
| `tools/wikiCheck/data/review_log.md` | Seeded template written on first run only, when log is missing |

The `data/` directory is gitignored. The real review log lives in the
`ea_mxmanual` project at `docs/notes/review_log.md`.

## Review log format

```
# Review Log
Last updated: YYYY-MM-DD

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| manual-standards | unreviewed | — |
```

Valid status values: `Approved`, `unreviewed`.

Update `Last updated:` and the relevant row after each review session, then commit.

## Development

```
python3 -m pytest         # run all tests
python3 -m pytest -v      # verbose
```

Tests use small fixtures in `tests/fixtures/` rather than the real WR.
See `docs/plans/design.md` for architecture details.
