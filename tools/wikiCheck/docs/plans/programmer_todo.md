# wikiCheck Programmer Todo

## Phases 1–7 — [x] Complete

---

## Phase 8 — Pending status support

**Goal:** Recognize `Pending` as a valid review log status. Count pending pages separately
in the summary and in `--detail`. Pending pages are in the log; they must NOT appear in
"Pages missing from log".

### 8.1 — `review_log.py`: parse `Pending` status

`_ROW_RE` currently matches `(Approved|unreviewed)`. Add `Pending` to the alternation:

```python
_ROW_RE = re.compile(r'^\|\s*([^|]+?)\s*\|\s*(Approved|Pending|unreviewed)\s*\|', re.MULTILINE)
```

**Tests to write in `test_review_log.py`:**
- `test_reads_pending_entry`: log with a `Pending` row parses correctly; `entry.status == "Pending"`
- `test_entry_count_includes_pending`: a log with Approved + Pending + unreviewed yields 3 entries

TDD: write failing tests first, then make the one-line regex change.

---

### 8.2 — `stats.py`: count pending pages

Add `pending_count: int` to the `Stats` dataclass (after `approved_count`).

In `compute_stats()`, add:
```python
pending = sum(1 for e in log.entries if e.status == "Pending")
```
Include `pending_count=pending` in the returned `Stats`.

Note: pending pages are already in `log_slugs` (they have log entries), so
`missing_from_log_count` is automatically correct once the regex fix in 8.1 is in place.
No special handling needed.

**Tests to write in `test_stats.py`:**
- `test_pending_count`: log with one `Pending` entry → `stats.pending_count == 1`
- `test_pending_not_in_missing_from_log`: a WR page whose log entry has status `Pending`
  does NOT appear in `missing_from_log_count`

All existing `test_stats.py` tests pass through `compute_stats()` which returns a `Stats`.
Adding the new field may break any test that constructs `Stats` directly. Check — and fix
if needed.

TDD: write failing tests, then add the field and the count line.

---

### 8.3 — `report.py`: add Pending line to summary; add Pending section to detail

#### `format_report()`

Insert a Pending line between "Approved pages" and "Unreviewed pages":

```python
f"Pending pages:           {stats.pending_count:>2}  (reviewed, awaiting resolution)",
```

Column alignment: "Pending pages:" (14 chars) + 11 spaces = 25 chars before the `:>2`
field, matching the column position of all other numeric fields.

#### `format_detail()`

Add `pending: list` parameter. Insert a "Pending pages:" section between the structural
section and "Unreviewed pages:":

```python
section("Pending pages:", pending),
section("Unreviewed pages:", unreviewed),
```

**Tests to write in `test_report.py`:**
- Update `_stats()` helper: add `pending_count=0` to the defaults dict.
- Update `test_format_normal_report`: add the Pending line to the expected string:
  ```
  "Approved pages:          36  (of 47 in log)\n"
  "Pending pages:            0  (reviewed, awaiting resolution)\n"
  "Unreviewed pages:         8  (in log, never reviewed)\n"
  ```
- `test_pending_line_in_report`: stats with `pending_count=3`, verify
  `"Pending pages:            3  (reviewed, awaiting resolution)"` in output.
- `test_pending_line_between_approved_and_unreviewed`: verify ordering via index positions.

**Tests to write in `test_detail.py`:**
- Update ALL existing `format_detail()` calls to add `pending=[]`.
- `test_detail_includes_pending`: `pending=["home", "panels-canopy"]` → "Pending pages:"
  and both slugs appear in detail.
- `test_pending_section_before_unreviewed`: verify `detail.index("Pending pages:") <
  detail.index("Unreviewed pages:")`.

TDD order: fix the `_stats()` helper first (that's not a test, it's scaffolding), then
write each failing test and implement to pass before moving to the next.

---

### 8.4 — `wiki_check.py`: pass pending to `format_detail()`

Two call sites need updating:

**Normal log branch** (around line 72): extract pending slugs and pass to `format_detail()`:
```python
pending = sorted(e.slug for e in log.entries if e.status == "Pending")
```
Add `pending=pending` to the `format_detail()` call.

**Missing log branch** (around line 50): add `pending=[]` to the `format_detail()` call.

**Tests to write in `test_e2e.py`:**
- Update `_run_with_fixtures()` to extract and pass `pending` (same pattern as `unreviewed`).
- Update `_run_missing_log_detail()` to pass `pending=[]`.
- Add `test_e2e_pending_count_in_summary`: use a new fixture log
  `tests/fixtures/review_log_with_pending.md` that adds a `Pending` entry for `page-a`.
  Verify `"Pending pages:            1"` appears in the summary.
- Add `test_e2e_pending_slug_in_detail`: same fixture, verify `"page-a"` appears in the
  detail under the pending section.
- Add `test_e2e_pending_not_in_missing`: same fixture, verify `page-a` does NOT cause
  an increase in "Pages missing from log".

**Fixture to create:** `tests/fixtures/review_log_with_pending.md`:
```
# Review Log
Last updated: 2026-04-10

| Page | Status | Last Reviewed |
|------|--------|---------------|
| page-a | Pending | 2026-04-10 |
| page-b | unreviewed | — |
```

(page-c remains absent from log — tests can still check missing_from_log == 1.)

---

### Commit checklist

- [ ] All tests pass with pristine output
- [ ] `test_format_normal_report` updated with Pending line in expected string
- [ ] All `format_detail()` call sites in tests have `pending=` parameter
- [ ] `programmer_todo.md` updated before committing
