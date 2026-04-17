# wikiCheck Programmer Todo

## Phase 1: Core data collection

### [x] 1.1 Glob WR pages
- Write failing test: given a directory of .md files, returns list of slugs
- Implement
- Tests pass, commit

### [x] 1.2 Parse Otterwiki links from a page
- Write failing test: extracts slugs from `[[Display Text|slug]]` and `[[slug]]` forms
- Write failing test: ignores non-link content
- Implement regex extraction
- Tests pass, commit

### [x] 1.3 Collect all broken links across WR
- Write failing test: cross-references extracted slugs against known WR slugs
- Write failing test: deduplicates repeated broken links
- Implement
- Tests pass, commit

### [x] 1.4 Parse review log
- Write failing test: reads `Last updated:` datestamp
- Write failing test: reads page entries and their status (`Approved`, `unreviewed`)
- Implement
- Tests pass, commit

### [x] 1.5 Handle missing review log
- Write failing test: when log missing, generates seeded review_log.md in data/
- Write failing test: seeded log contains all WR slugs with status `unreviewed` and today's date
- Write failing test: summary output includes NOT FOUND message with expected destination path
- Implement
- Tests pass, commit

## Phase 2: Statistics

### [x] 2.1 Compute all statistics
- Write failing tests for each stat:
  - Total WR page count
  - Broken link count
  - Approved page count
  - Unreviewed page count
  - Pages missing from log count
  - Log age in days
- Implement
- Tests pass, commit

## Phase 3: Output

### [x] 3.1 Format summary report
- Write failing test: output matches expected format exactly (see design.md)
- Implement
- Tests pass, commit

### [x] 3.2 --detail flag
- Write failing test: appends sorted lists of broken links, unreviewed pages, missing pages
- Write failing test: omitted when flag not passed
- Implement
- Tests pass, commit

## Phase 4: CLI and integration

### [x] 4.1 Wire up argparse CLI (--detail)
- Write failing test: correct behavior for each flag combination
- Implement
- Tests pass, commit

### [x] 4.2 End-to-end test against fixture WR and log
- Create fixture directory with a small WR and review log
- Write E2E test covering: broken links, unreviewed, missing pages, missing log
- Tests pass, commit

## Phase 5: AR integration

### [ ] 5.1 Create `docs/notes/review_log.md` in ea_mxmanual project
- Run `wiki_check.py`, take the generated template from `data/`, move to `docs/notes/`
- Commit in ea_mxmanual repo

### [ ] 5.2 Update `claude/roles/reviewer.md` in ea_mxmanual project
- Add wikiCheck startup sequence per design.md spec
- Add post-review log update step
- Commit in ea_mxmanual repo

### [ ] 5.3 Update `claude/project_status.md` in ea_mxmanual project
- Document `docs/notes/` directory and `review_log.md`
- Commit in ea_mxmanual repo
