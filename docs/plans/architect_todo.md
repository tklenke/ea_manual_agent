# Architect Todo

## In Progress

## Backlog

### [x] Design input file archiving for writer_todo and feedback drop zones (2026-04-17)

Files are renamed in place with a `_pending` suffix after being consumed (e.g.,
`task.md` → `task_pending.md`). Deleted after work is approved. No archive directories
needed — drop zones are gitignored. Updated `claude/roles/writer.md` and
`claude/roles/architect.md`.

---

### [x] Verify wikiCheck "pending" status fix (2026-04-17)

Verified 2026-04-17. All three criteria met:
- Pending pages show under "Pending pages" summary line with correct count (7)
- Pending pages do NOT appear under "Pages missing from log"
- `--detail` output includes a "Pending pages" section listing them

---

### [ ] Writer todo update workflow — add to Writer role (NOTE FROM REVIEWER 2026-04-17)

Tom has asked that the Writer update writer_todo.md after Tom explicitly approves a reviewed page — not during the review session itself. Update `claude/roles/writer.md` to reflect this: Writer marks tasks `[x]` complete after Tom's sign-off, not before.

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
