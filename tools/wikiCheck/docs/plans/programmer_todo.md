# wikiCheck Programmer Todo

## Phases 1–6 — [x] Complete

## Phase 7: Structural page exclusion + orphan detection bug fix

See design.md "Structural page exclusion" section for full spec.

### [ ] 7.1 Extend `orphan_pages.py`

- Add `STRUCTURAL_PAGES = ["home", "readme"]` constant
- Update `find_orphan_pages(wr_dir)` to exclude structural pages (case-insensitive slug
  comparison); signature unchanged
- Add `check_structural_pages(wr_dir) -> tuple[list[str], list[str]]`: returns
  `(found, missing)` — structural pages that exist vs. are absent from WR; comparison
  is case-insensitive against `STRUCTURAL_PAGES`
- TDD: update `test_orphan_pages.py`
  - Add test: structural page slug excluded from `find_orphan_pages()` result
  - Add test: case-insensitive exclusion (e.g., `Home.md` excluded)
  - Add test: `check_structural_pages()` returns both in `found` when both exist
  - Add test: `check_structural_pages()` returns missing page in `missing` when absent
  - Add test: case-insensitive detection in `check_structural_pages()` (e.g., `README.md` → found)
  - Existing tests must still pass (none use structural slugs)

### [ ] 7.2 Update `Stats` and `compute_stats()`

- Add `structural_pages_found: list[str]` and `structural_pages_missing: list[str]`
  to `Stats` dataclass
- Call `check_structural_pages(wr_dir)` in `compute_stats()` and populate new fields
- `orphan_count` is now `len(find_orphan_pages(wr_dir))` — structural pages already
  excluded, no other changes needed
- TDD: update `test_stats.py`
  - Add test: `structural_pages_found` populated when structural pages exist in WR
  - Add test: `structural_pages_missing` populated when a structural page is absent
  - Add test: `orphan_count` does not include structural pages

### [ ] 7.3 Update `format_report()` in `report.py`

- Add `structural_pages_found` and `structural_pages_missing` parameters
- Insert structural pages line after "Orphan pages":
  `Structural pages:         N  (slug, slug — excluded from orphans)`
- Append one `ERROR: Structural page not in WR: slug` line per missing page
- TDD: update `test_report.py`
  - Add test: structural pages line present with correct count and slug list
  - Add test: ERROR line appears when a structural page is missing
  - Add test: no ERROR line when all structural pages found

### [ ] 7.4 Update `format_missing_log_report()` in `report.py`

- Add `structural_pages_found` and `structural_pages_missing` parameters
- Insert structural pages line (and any ERROR lines) between broken links and the
  "Review log: NOT FOUND" block
- TDD: update `test_report.py` (missing-log cases)

### [ ] 7.5 Update `format_detail()` in `report.py`

- Add `structural_pages_found` and `structural_pages_missing` parameters
- Add section "Structural pages (excluded from orphans):" listing `found` slugs
- If any `missing`, append `  ERROR: not in WR: slug` lines in that section
- TDD: update `test_detail.py`
  - Add test: structural section present with correct slugs
  - Add test: error lines present for missing structural pages

### [ ] 7.6 Fix bug + update `wiki_check.py`

- **Bug fix**: missing-log `--detail` branch (line 43) passes `orphan_pages=[]`
  hardcoded; replace with `find_orphan_pages(WR_DIR)`
- Add `check_structural_pages(WR_DIR)` call in both branches (log-exists and
  missing-log)
- Pass `structural_pages_found` and `structural_pages_missing` to `format_report()`,
  `format_missing_log_report()`, and `format_detail()` in all call sites
- TDD: update `test_cli.py` and `test_e2e.py`
  - Add test: `--detail` with missing log now shows real orphan list (bug fix)
  - Add test: structural pages line appears in normal run output
  - Add test: structural pages line appears in missing-log run output
