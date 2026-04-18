# Programmer Todo

## Phases 1–9 — [x] Complete

---

## Phase 10: @@TOM flag count

Count occurrences of `@@TOM` across all WR `.md` files and report in the summary.
In `--detail` mode, list the pages that contain at least one `@@TOM`.

### Implementation steps

- [x] Create `wikicheck/tom_flags.py`
  - `find_tom_flags(wr_dir: Path) -> list[str]` — returns sorted list of page slugs
    that contain at least one `@@TOM` occurrence (one entry per page, not per occurrence)
  - `count_tom_flags(wr_dir: Path) -> int` — total count of all `@@TOM` occurrences
    (sum across all files, not unique pages)

- [x] Write tests for `tom_flags.py`
  - Fixture: create temp dir with two .md files; one has two `@@TOM`, one has none
  - `test_count_is_total_occurrences` — count = 2
  - `test_pages_with_tom_flags` — list contains only the page with @@TOM
  - `test_no_tom_flags` — empty WR returns count=0 and empty list
  - `test_partial_match_not_counted` — `@@TOMMY` does not match (whole-token check)

- [x] Add `tom_flag_count: int` and `tom_flag_pages: list[str]` to `Stats` dataclass
      in `stats.py`

- [x] Wire into `compute_stats()` in `stats.py`

- [x] Add summary line to `format_report()` in `report.py`, between Orphan pages and
      Structural pages:
      `f"@@TOM flags:             {stats.tom_flag_count:>2}  (pages flagged for Tom's input)"`

- [x] Add `--detail` section to `format_detail()` in `report.py`:
      `section("Pages with @@TOM flags:", tom_flag_pages)`
      — place between Orphan pages and Structural pages sections

- [x] Write tests for report output
  - `test_tom_flags_line_in_report` — summary line present with correct count
  - `test_tom_flags_line_position` — appears between orphan and structural lines
  - `test_tom_flags_detail_section` — detail section lists correct pages
  - `test_tom_flags_detail_section_position` — detail section between orphan and structural
