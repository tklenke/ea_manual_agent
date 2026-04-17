# wikiCheck Architect Todo

## Backlog

### [ ] Write `wiki_check.py`

Script operates on the WR at `/home/tom/projects/N657CZDashTwo` and the AR review log at `docs/notes/review_log.md`.

**Broken link check:** Scan all WR `.md` files for DokuWiki internal links (`[[page-slug]]` and `[[page-slug|Display Text]]`). Extract target slugs. Check which slugs have no corresponding `.md` file in the WR. Report count and list.

**Review log check:**
- Read datestamp from `docs/notes/review_log.md` (AR)
- Glob all WR `.md` pages
- Grep review log for page entries; identify WR pages missing from the log
- Report: log age, count of unreviewed pages (status = `unreviewed`), count of WR pages missing from log entirely

**Output format:** Compact plain-text summary, suitable for pasting into a Claude session:
```
Wiki Integrity Report — 2026-04-16
Broken links:            12  (pages referenced but not yet written)
Unreviewed pages:         8  (in log, never reviewed)
Pages missing from log:   3  (in WR, not in log)
Review log last updated: 2026-04-10 (6 days ago)
```

**Flags:**
- `--detail` — print full lists of broken links, unreviewed pages, and missing pages
- `--seed` — write all WR pages to review log with status `unreviewed`; asks confirmation before writing

---

### [ ] Create `docs/notes/review_log.md` (in AR)

Format:
```
# Review Log
Last updated: YYYY-MM-DD

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | Approved | 2026-04-10 |
| manual-standards | unreviewed | — |
```

- **Seeding:** First Reviewer session runs `wiki_check.py --seed`, which identifies all WR pages and writes them to the log marked `unreviewed`. Asks Tom to confirm before writing.
- **Updating:** After reviewing a page, Reviewer updates the entry with date and outcome.
- **Log datestamp** (`Last updated:`) updated whenever Reviewer modifies the log.

---

### [ ] Update `claude/roles/reviewer.md` (in AR)

Add to Reviewer startup sequence (after reading standard files):

1. Run `tools/wikiCheck/wiki_check.py` (or ask Tom to run it and paste the output)
2. Report summary to Tom
3. Ask: "The review log has N unreviewed pages and N pages missing from the log. Want me to update the log? Do you want to run a link check this session?"
4. If log needs seeding (first run, no log exists): walk Tom through the seeding step

Add to Reviewer workflow: after completing a page review, update `docs/notes/review_log.md` entry and commit.

---

### [ ] Document `docs/notes/` in `claude/project_status.md` (in AR)

Add `docs/notes/` to the directory structure with entries for `review_log.md`.

---

**Implementation order:** `wiki_check.py` → review log → reviewer.md → project_status.md
