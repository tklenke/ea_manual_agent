# Writer Todo

## In Progress

## Backlog

### [ ] FIRST TASK: Configure OtterWiki print footer and write Record of Revisions page

This is the first writing task. It has two parts that must be done in order.

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

### [ ] PILOT PAGE: Write canopy component page and canopy cleaning procedure

**Purpose:** Validate that templates, formatting, cross-linking, and OtterWiki rendering all work correctly before bulk content development begins. After completion, Tom and Claude review the output together and adjust standards if needed.

**Prerequisite:** OtterWiki instance must be running (see architect_todo).

#### Page 1: `panels-canopy` — Canopy component page (Type 1b)

Write the Canopy component page for Section 9. This is a reference page — description, specifications, inspection criteria. The cleaning procedure is a cross-reference link, not inline content.

**Research needed:**
- Canopy material and construction (Cozy Mark IV uses a blown acrylic canopy)
- Location, dimensions if known
- Inspection criteria: crazing, scratches, delamination, seal condition, latch mechanism

**Cross-reference to include:**
- `See [[panels-canopy-cleaning|Canopy Cleaning]] for cleaning procedure.`

#### Page 2: `panels-canopy-cleaning` — Canopy Cleaning procedure (Type 2)

Write the canopy cleaning procedure for Section 9.

**Research needed:**
- Cleaners safe for acrylic canopies (aviation-specific recommendations)
- Cleaners that must be avoided (solvents that cause crazing)
- Proper technique to avoid scratching
- Anti-static and UV protectant products if applicable
- Check `docs/references/AC43_13/` for relevant guidance on transparent enclosures

**Expected structure:** Overview, Tools and Materials Required, Safety Notes (harmful cleaners), Procedure steps, Post-Procedure Checks.

#### After both pages are written:
- Verify both render correctly in OtterWiki
- Verify the cross-link from canopy page to cleaning page resolves
- Verify `[TOC]` renders if used
- Tom and Claude review together — adjust templates/standards before proceeding

---

## Completed
