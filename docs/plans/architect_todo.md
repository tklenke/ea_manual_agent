# Architect Todo

## In Progress

## Backlog

### [ ] Design input file archiving for writer_todo and feedback drop zones (flagged by Writer 2026-04-17)

Currently, the Writer deletes input files from `input/writer_todo/` and `input/feedback/` after consuming them. Tom wants consumed files retained. Design an archiving approach — likely an `input/archive/` directory or per-subdirectory archive folders. Update the Writer role instructions and content_development_overview.md to reflect the new behavior.

---

### [ ] Verify wikiCheck "pending" status fix (flagged 2026-04-17)

Task written to `tools/docs/plans/architect_todo.md` for tools architect to implement.
When complete: run `wiki_check.py --detail` and verify:
- Pending pages show under "Pending pages" summary line with correct count
- Pending pages do NOT appear under "Pages missing from log"
- `--detail` output includes a "Pending pages" section listing them

Currently pending pages: `home`, `panels-canopy`, `readme`.

---

### [ ] OtterWiki navigation sidebar strategy — confirm final decision

Options evaluated 2026-04-16:
- **Option A:** Hand-maintained `_sidebar.md`
- **Option B:** Derived from `toc_structure.md`
- **Option C:** OtterWiki built-in auto-generated index

**Current decision: Option C.** Auto-generated sidebar reviewed with initial content (2026-04-16) — acceptable so far. Revisit as content volume grows. Do not close until Tom confirms Option C is the permanent approach.

---

## Completed

### [x] Update TDS citation format in docs/plans/formatting.md (2026-04-17)

AR source already had the correct filename format. No change needed.

### [x] Add AR-update flow to Reviewer role instructions (2026-04-17)

Added "When AR Sources Need Updates" section to `claude/roles/reviewer.md`. Reviewer fixes wiki page, logs task in architect_todo.md, does not touch AR sources directly.

### [x] Verify wikiCheck output and integrate into Reviewer role (2026-04-17)

Ran `wiki_check.py --detail` against WR — output accurate. 82 broken links expected (TOC pages not yet written). 4 false-positive slugs from templates.md documented in `docs/notes/wikicheck_ignored_links.md`. Updated `claude/roles/reviewer.md` with wikiCheck startup sequence. Created `docs/notes/review_log.md`. Updated `claude/project_status.md`.

### [x] Review wikiCheck orphan detection (2026-04-17)

Output correct and useful. No orphans currently — expected at this stage. Integrated into Reviewer role startup. Orphan design: wikiCheck live scan is authoritative; Writer resolves by finding a valid link target; escalates to Architect if none exists.
