# Architect Todo

## In Progress

## Backlog

### [x] Set up OtterWiki instance on local machine (2026-04-16)

Instance running. Pilot pages (panels-canopy, panels-canopy-cleaning) and home.md TOC reviewed and look good. Auto-generated sidebar acceptable so far.

### [ ] OtterWiki navigation sidebar strategy — confirm final decision

Options evaluated 2026-04-16:
- **Option A:** Hand-maintained `_sidebar.md`
- **Option B:** Derived from `toc_structure.md`
- **Option C:** OtterWiki built-in auto-generated index

**Current decision: Option C.** Auto-generated sidebar reviewed with initial content (2026-04-16) — acceptable so far. Revisit as content volume grows. Do not close until Tom confirms Option C is the permanent approach.

### [x] Migrate architecture_decisions.md to Otterwiki as Manual Standards page (2026-04-16)

Writer task created in writer_todo.md. See "Publish Manual Standards page (Section 1)".

### [x] Audit and revise toc_structure.md

Completed 2026-04-16. Full restructure: 18 sections, all pages defined, all content decisions documented in architecture_decisions.md.

The current TOC has significant problems identified on 2026-04-15. Do not begin writing content until this is resolved.

**Problems to address:**

1. **Section 16 (Avionics) is generic commercial-aircraft boilerplate.** The following items almost certainly don't exist on the Cozy Mark IV and should be removed or verified:
   - HF Communication
   - Instrument Landing System (ILS)
   - Fly-by-Wire Technology
   - Terrain Awareness and Warning Systems (TAWS)
   - Ground Proximity Warning Systems (GPWS)
   - Traffic Alert and Collision Avoidance System (TCAS)

2. **Section 14 (Electrical) is also suspiciously generic.** Needs to be audited against what is actually installed on the aircraft.

3. **Wildly inconsistent depth.** Sections 14 and 16 have elaborate sub-page trees; Sections 2, 6, 15, 17, 18 are completely empty. Section 6 (Inspection) should be one of the most developed sections for a maintenance manual — it is currently a skeleton.

4. **Duplicate section number.** Two entries labeled 7.2 in Section 7 (Structures).

5. **Section 1 meta-content.** "Instructions for development of Design and Troubleshooting Documentation" is a guidance doc for Claude/Tom, not content for a maintainer. Remove from the manual TOC.

6. **Missing weight and balance section.** Standard and important for a maintenance manual.

7. **Scope question to resolve with Tom.** Pages like `flight-controls-fabrication-notes` and `flipping-fuselage` — are we writing a maintenance manual, a build manual, or both? This needs an explicit decision before content is written.

**Plan to resolve:**
- Interview Tom: get an inventory of what avionics and electrical systems are actually installed on the aircraft
- Audit Sections 14 and 16 against that inventory — remove or stub pages for systems not present
- Fill in empty section skeletons (especially Section 6 Inspection)
- Fix duplicate 7.2
- Remove meta-content from Section 1
- Add weight and balance section
- Get explicit scope decision from Tom on fabrication content

## Backlog

### [x] Consider retiring standards files from docs/plans/ (NOTE FROM WRITER 2026-04-16) — resolved 2026-04-16

**Decision:** Keep AR copies. AR is the working copy; WR is the published snapshot — same pattern as `architecture_decisions.md` / `manual-standards.md`. Removing the AR copies would invert this pattern and make session startup dependent on OtterWiki availability.

**Drift prevention:** Two-layer approach added to `claude/roles/architect.md`:
1. When Architect modifies a standards file, create a Writer task to re-publish the corresponding WR page immediately.
2. Pre-commit drift check: compare `git log -1` dates on AR files vs WR files; create a Writer task if AR is newer and no task already exists.

---

### [x] Define workflow for the `input/` directory (NOTE FROM WRITER 2026-04-16) — resolved 2026-04-16

**Decision:** Writer's proposed workflow adopted with one addition:

- `input/architect_todo/` — Architect checks at session startup, adds tasks to `architect_todo.md`, deletes input file
- `input/writer_todo/` — Writer checks at session startup, adds tasks to `writer_todo.md`, deletes input file
- `input/feedback/` — Writer checks at session startup, processes feedback (updates content), deletes input file; escalates to Architect if feedback has structural implications
- Processed files are deleted (not archived) — git history preserves them if needed
- `input/` documented in `claude/project_status.md` directory structure
- Role startup reads updated in `claude/roles/architect.md` and `claude/roles/writer.md`

---

### [ ] Build wiki integrity tooling and update Reviewer role (2026-04-16)

**Context:** Discussed 2026-04-16. The Reviewer needs two persistent quality tools: a broken link report and a page review log. Rather than having Claude do grep/glob work in role definition prose, we build a Python script that does the heavy lifting and outputs a compact summary. Reviewer reads the output and asks Tom what to do.

---

#### 1. Write `tools/wikiCheck/wiki_check.py`

Script lives in the AR at `tools/wikiCheck/wiki_check.py`. It operates on the WR at `/home/tom/projects/N657CZDashTwo`.

**What it does:**

- **Broken link check:** Scan all WR `.md` files for DokuWiki internal links (`[[page-slug]]` and `[[page-slug|Display Text]]`). Extract target slugs. Check which slugs have no corresponding `.md` file in the WR. Report count and list.

- **Review log check:**
  - Read datestamp from `docs/notes/review_log.md` (AR)
  - Glob all WR `.md` pages
  - Grep review log for page entries; identify WR pages missing from the log
  - Report: log age, count of unreviewed pages (status = `unreviewed`), count of WR pages missing from log entirely

**Output format:** Compact plain-text summary, suitable for pasting into a Claude session. Example:
```
Wiki Integrity Report — 2026-04-16
Broken links:       12  (pages referenced but not yet written)
Unreviewed pages:    8  (in log, never reviewed)
Pages missing from log: 3  (in WR, not in log)
Review log last updated: 2026-04-10 (6 days ago)
```
Optionally with `--detail` flag: full lists of broken links, unreviewed pages, missing pages.

---

#### 2. Create `docs/notes/review_log.md`

File lives in the AR. Format:

```
# Review Log
Last updated: YYYY-MM-DD

| Page | Status | Last Reviewed |
|------|--------|---------------|
| panels-canopy | 2026-04-10 | Approved |
| manual-standards | unreviewed | — |
```

- **Seeding:** First Reviewer session runs `wiki_check.py`, which identifies all WR pages. Reviewer seeds the log with every page marked `unreviewed`. Asks Tom to confirm before writing.
- **Updating:** After reviewing a page, Reviewer updates the entry with date and outcome.
- **Log datestamp** (`Last updated:`) updated whenever Reviewer modifies the log.

---

#### 3. Update `claude/roles/reviewer.md`

Add to Reviewer startup sequence (after reading standard files):

1. Run `tools/wiki_check.py` (or ask Tom to run it and paste the output if script execution isn't available)
2. Report summary to Tom
3. Ask: "The review log has N unreviewed pages and N pages missing from the log. Want me to update the log? Do you want to run a link check this session?"
4. If log needs seeding (first run, no log exists): walk Tom through the seeding step

Add to Reviewer workflow: after completing a page review, update `docs/notes/review_log.md` entry and commit.

---

#### 4. Document `docs/notes/` in `claude/project_status.md`

Add `docs/notes/` to the directory structure with entries for `review_log.md` and `link_report.md` (if we decide to persist link reports — TBD).

---

**Implementation order:** 1 → 2 → 3 → 4. Script first, then log, then role update.

---

### [x] Restructure tools/ directory and delegate wikiCheck to tools Claude (2026-04-16)

**Context:** PDFindexer has a Python-optimized CLAUDE.md and claude/ directory. These should live at the `tools/` level and cover all tools. Each tool gets its own subdirectory for code, plans, and data.

**Target structure:**
```
tools/
├── CLAUDE.md          (moved from PDFindexer/CLAUDE.md)
├── claude/            (moved from PDFindexer/claude/)
├── PDFindexer/        (code, plans, data — moved from root PDFindexer/)
└── wikiCheck/         (new — code, plans, data for wiki integrity script)
```

**Steps:**

1. `git mv PDFindexer tools/PDFindexer` — preserves history
2. `git mv PDFindexer/CLAUDE.md tools/CLAUDE.md` — move before step 1, or adjust paths accordingly
3. `git mv PDFindexer/claude tools/claude` — same
4. Create `tools/wikiCheck/` with a spec file describing what to build (see below)
5. Update `claude/project_status.md` directory structure — replace `PDFindexer/` entry with `tools/` block
6. Update the wiki integrity tooling task above — `tools/wiki_check.py` becomes `tools/wikiCheck/`
7. Update any references in role definitions that mention PDFindexer

**wikiCheck spec to seed `tools/wikiCheck/plans/spec.md`:**
- Inputs: WR path (`/home/tom/projects/N657CZDashTwo`), AR review log path (`docs/notes/review_log.md`)
- Broken link check: scan all WR `.md` files for `[[slug]]` and `[[slug|Text]]` links; report slugs with no corresponding `.md` file
- Review log check: read log datestamp; find WR pages missing from log; count entries with status `unreviewed`
- Output: compact plain-text summary (see wiki integrity task for format); `--detail` flag for full lists
- Review log seeding: `--seed` flag writes all WR pages to log with status `unreviewed` (asks confirmation before writing)

**Note:** After restructure, main roles delegate scripting work to the tools Claude by dropping a spec into `tools/wikiCheck/` or `tools/PDFindexer/` and switching Claude context to `tools/`.

---

## Completed
