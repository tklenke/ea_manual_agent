# Architect Todo

## In Progress

## Backlog

### [ ] OtterWiki navigation sidebar strategy — confirm final decision

Options evaluated 2026-04-16:
- **Option A:** Hand-maintained `_sidebar.md`
- **Option B:** Derived from `toc_structure.md`
- **Option C:** OtterWiki built-in auto-generated index

**Current decision: Option C.** Auto-generated sidebar reviewed with initial content (2026-04-16) — acceptable so far. Revisit as content volume grows. Do not close until Tom confirms Option C is the permanent approach.

---

## Completed

### [x] Verify wikiCheck output and integrate into Reviewer role (2026-04-17)

Ran `wiki_check.py --detail` against WR — output accurate. 82 broken links expected (TOC pages not yet written). 4 false-positive slugs from templates.md documented in `docs/notes/wikicheck_ignored_links.md`. Updated `claude/roles/reviewer.md` with wikiCheck startup sequence. Created `docs/notes/review_log.md`. Updated `claude/project_status.md`.

### [x] Review wikiCheck orphan detection (2026-04-17)

Output correct and useful. No orphans currently — expected at this stage. Integrated into Reviewer role startup. Orphan design: wikiCheck live scan is authoritative; Writer resolves by finding a valid link target; escalates to Architect if none exists.
