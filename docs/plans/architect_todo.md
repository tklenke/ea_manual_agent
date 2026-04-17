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

### [x] Review wikiCheck orphan detection once implemented (2026-04-16)
Verified 2026-04-17. Output is correct and useful. Orphan detection working (no orphans
currently — expected). Integrated into Reviewer role startup.

**Orphan page design decisions (2026-04-16):**
- No separate tracking file — wikiCheck live scan is authoritative; list shrinks as Writer fixes
- Orphan count in summary report; full list under `--detail`
- Reviewer startup: run wikiCheck, hand orphan list to Writer as actionable items
- Writer resolves by finding the right page to link from and adding the link
- If no valid link target exists, Writer escalates to Architect
- No valid use case for intentionally unlinked pages in this manual

---

### [x] Verify wikiCheck output and integrate into Reviewer role (2026-04-16)

Completed 2026-04-17.

1. Ran `wiki_check.py --detail` against WR — output accurate; 82 broken links expected (TOC pages not yet written); 4 false-positive slugs from templates.md documented in `docs/notes/wikicheck_ignored_links.md`
2. Updated `claude/roles/reviewer.md` — wikiCheck added to startup sequence with guidance on interpreting output and handling orphans
3. Created `docs/notes/review_log.md` (seeded by wikiCheck, moved from `tools/wikiCheck/data/`)
4. Updated `claude/project_status.md` — `docs/notes/` directory documented

---

## Completed
