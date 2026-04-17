# wikiCheck Programmer Todo

## Phase 1: Core data collection

### [ ] 1.1 Glob WR pages
- Write failing test: given a directory of .md files, returns list of slugs
- Implement
- Tests pass, commit

### [ ] 1.2 Parse Otterwiki links from a page
- Write failing test: extracts slugs from `[[Display Text|slug]]` and `[[slug]]` forms
- Write failing test: ignores non-link content
- Implement regex extraction
- Tests pass, commit

### [ ] 1.3 Collect all broken links across WR
- Write failing test: cross-references extracted slugs against known WR slugs
- Write failing test: deduplicates repeated broken links
- Implement
- Tests pass, commit

### [ ] 1.4 Parse review log
- Write failing test: reads `Last updated:` datestamp
- Write failing test: reads page entries and their status (`Approved`, `unreviewed`)
- Write failing test: handles missing log file gracefully (report N/A)
- Implement
- Tests pass, commit

## Phase 2: Statistics

### [ ] 2.1 Compute all statistics
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

### [ ] 3.1 Format summary report
- Write failing test: output matches expected format exactly (see design.md)
- Implement
- Tests pass, commit

### [ ] 3.2 --detail flag
- Write failing test: appends sorted lists of broken links, unreviewed pages, missing pages
- Write failing test: omitted when flag not passed
- Implement
- Tests pass, commit

## Phase 4: --seed flag

### [ ] 4.1 Generate seed content
- Write failing test: produces correct review_log.md content for a given set of slugs
- Implement
- Tests pass, commit

### [ ] 4.2 Confirmation prompt and write
- Write failing test: prints slug list and prompts before writing
- Write failing test: aborts cleanly on non-yes response
- Write failing test: writes review_log.md on confirmation
- Implement
- Tests pass, commit

## Phase 5: CLI and integration

### [ ] 5.1 Wire up argparse CLI (--detail, --seed)
- Write failing test: correct behavior for each flag combination
- Implement
- Tests pass, commit

### [ ] 5.2 End-to-end test against fixture WR and log
- Create fixture directory with a small WR and review log
- Write E2E test covering: broken links, unreviewed, missing, seed
- Tests pass, commit

## Phase 6: AR integration

### [ ] 6.1 Create `docs/notes/review_log.md` in ea_mxmanual project
- Run `wiki_check.py --seed` or create manually from WR page list
- Commit in ea_mxmanual repo

### [ ] 6.2 Update `claude/roles/reviewer.md` in ea_mxmanual project
- Add wikiCheck startup sequence per design.md spec
- Add post-review log update step
- Commit in ea_mxmanual repo

### [ ] 6.3 Update `claude/project_status.md` in ea_mxmanual project
- Document `docs/notes/` directory and `review_log.md`
- Commit in ea_mxmanual repo
