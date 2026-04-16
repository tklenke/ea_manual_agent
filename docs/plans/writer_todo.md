# Writer Todo

## In Progress

## Backlog

### [ ] Configure OtterWiki print footer and write Record of Revisions page

**Prerequisite:** OtterWiki instance must be running (Tom's architect task — see architect_todo).

This task has two parts that must be done in order.

#### Part 1: Configure OtterWiki print footer

Set up the OtterWiki instance to display version metadata on printed pages.

**Goal:** Every printed page automatically shows a footer with last-edited timestamp and short git commit hash, so a printed copy can be traced back to an exact version in git.

**Steps:**
1. Test whether `page.updated` is available in the OtterWiki Jinja2 template context for the installed version
2. Create `customBody.html` injecting a print-only footer div:
   ```html
   <div class="print-only-metadata">
       Last edited: {{ page.updated.strftime('%Y-%m-%d %H:%M') }} (short-hash)
   </div>
   ```
3. If `page.updated` is unavailable, use JavaScript against the history endpoint to retrieve the timestamp
4. For the git short hash: investigate whether OtterWiki exposes commit hash in template context; if not, use JavaScript
5. Create `custom.css` with print-only display rules (hide on screen, show fixed footer on print)
6. Test by printing a page from the browser — verify timestamp and hash appear correctly
7. Target format: `Last edited: YYYY-MM-DD HH:MM (short-hash)`

**Reference:** `docs/plans/architecture_decisions.md` — Version and Revision Information section.

#### Part 2: Write the Record of Revisions page (Section 1)

Once the print footer is working, write the `Record of Revisions` page for Section 1. Note: the `[[/?do=recent|Record of Revisions]]` TOC entry links to OtterWiki's built-in recent changes view. This page is a companion that explains how to interpret and use that revision history.

**This page explains to a maintainer:**
- All changes to this manual are tracked in git — every edit has a timestamp and commit hash
- The print footer on each page shows when the page was last edited and the short git commit hash
- How to use that information to identify the exact version of a printed page (e.g., `git show <hash>` or `git log --all -- <page-file>`)
- The Record of Revisions link in the TOC shows the full change history across all pages

**Tone:** Written for a maintainer who may not be a git expert. Practical — focus on "how do I verify which version I have" not git internals.

**Sources:** No AC 43.13 or TDS citations needed. This is procedural documentation about the manual itself.

---

## Completed

### [x] Write home.md and update README for WR (2026-04-16)
- home.md: OtterWiki landing page with full 18-section TOC, committed to WR.
- readme.md: Added disclaimer text to README.
- Corrected wiki link format throughout (OtterWiki uses `[[Display Text|page-name]]`). Updated formatting.md and templates.md in AR to match.

### [x] FIRST TASK: Write pilot pages — Canopy and Canopy Cleaning (2026-04-16)
- panels-canopy.md: description (hinge right, electric actuator, manual latch bar, access door), specifications, inspection criteria. Committed to WR.
- panels-canopy-cleaning.md: full Type 2 procedure — pre-rinse, Plexus, optional Pledge wax, solvents-to-avoid list per AC 43.13 ch03_p025. Committed to WR.
- One @@TOM flag remains open: canopy seal type and inspection criteria.
- Review checkpoint complete (2026-04-16): pages render correctly in OtterWiki, cross-link resolves, [TOC] renders. Templates and standards confirmed good — proceed with content development.
