# wikiCheck Programmer Todo

## Phases 1–8 — [x] Complete

---

## Phase 9 — Fix `Pending` status case mismatch

**Bug:** wikiCheck reports `Pending pages: 0` and lists the 7 pending pages under
"Pages missing from log". The review log uses lowercase `pending`; the implementation
expects capitalized `Pending`.

**Required behavior (from design.md):**
- `Pending` recognized as valid status alongside `Approved` and `unreviewed`
- Pending count correct in summary line
- Pending pages excluded from "Pages missing from log"
- `--detail` "Pending pages" section lists them by name (currently shows `(none)`)

### Tasks

- [x] 9.1 — In `review_log.py`, normalize status to title-case on read (or use
  case-insensitive comparison). Verify `pending` → treated as `Pending`.

- [x] 9.2 — Run `wiki_check.py --detail` against live data and verify:
  - `Pending pages: 7` (not 0)
  - Those 7 pages absent from "Pages missing from log"
  - `--detail` "Pending pages" section lists them by name

- [x] 9.3 — Confirm tests pass (`pytest`) with pristine output. Add/update test
  coverage for lowercase `pending` input if not already present.

- [x] 9.4 — Commit with updated programmer_todo.md
