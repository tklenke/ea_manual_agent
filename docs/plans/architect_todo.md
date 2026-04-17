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

### [ ] Review wikiCheck orphan detection once implemented (2026-04-16)
Tools architect_todo has the task. Once the programmer builds it, verify output is correct
and useful, then ensure it's reflected in the Reviewer integration.

**Orphan page design decisions (2026-04-16):**
- No separate tracking file — wikiCheck live scan is authoritative; list shrinks as Writer fixes
- Orphan count in summary report; full list under `--detail`
- Reviewer startup: run wikiCheck, hand orphan list to Writer as actionable items
- Writer resolves by finding the right page to link from and adding the link
- If no valid link target exists, Writer escalates to Architect
- No valid use case for intentionally unlinked pages in this manual

---

### [ ] Verify wikiCheck output and integrate into Reviewer role (2026-04-16)

**Context:** `tools/wikiCheck/wiki_check.py` is built by the tools Claude per `tools/wikiCheck/docs/plans/architect_todo.md`. Once built, verify the output is correct and useful, then integrate into the Reviewer role startup sequence.

**Steps:**
1. Run `tools/wikiCheck/wiki_check.py` against the WR; verify output is accurate
2. Update `claude/roles/reviewer.md` — add wikiCheck to startup sequence and post-review workflow
3. Create `docs/notes/review_log.md` (seeded via `--seed` flag)
4. Update `claude/project_status.md` — add `docs/notes/` directory entry

---

## Completed
