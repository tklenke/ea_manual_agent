# Writer Todo

## In Progress

## Backlog

### [ ] Write panels-turtleback-windows page (flagged by Reviewer 2026-04-17)

Tom has enough information to write this page. It is a Type 1b Component page in Section 9 (Canopy and Panels). Cross-referenced from `panels-canopy-cleaning` — cleaning procedure applies to turtleback windows as well as the canopy.

---

### [x] Publish Manual Standards page (Section 1) (2026-04-16)

Published as a family of `manual-standards-*` pages in the WR:
- `manual-standards` — scope, versioning, TOC depth, list ordering rules; links to all sub-pages
- `manual-standards-section-notes` — section-specific structural decisions
- `manual-standards-writing-style` — voice, tense, language rules
- `manual-standards-formatting` — naming, NOTEs, citations, cross-references
- `manual-standards-page-templates` — standard page structures by type

Also published: `record-of-revisions`, `section-notes` (now `manual-standards-section-notes`).

Processed feedback from `input/feedback/manual-standards.txt` (2026-04-16):
- [TOC] removed from all pages (OtterWiki renders sidebar TOC automatically)
- Section-specific decisions split to `manual-standards-section-notes`
- Manual scope updated to include POH as out of scope
- Writing style, formatting, and page templates published as separate pages
- All manual-standards pages given `manual-standards-` prefix for searchability

---

### [x] Configure OtterWiki print footer and write Record of Revisions page (2026-04-16)

- Print footer implemented via `customBody.html` + `custom.css` in `~/otterwiki_system/custom/`. Uses `document.lastModified` (reliable: OtterWiki sets Last-Modified header from git commit datetime). Shows date only — no git hash.
- `record-of-revisions.md` written and committed to WR. Explains git-based tracking, print footer, page history, and links to `/changelog` built-in view.
- TOC updated: `record-of-revisions` replaces `/changelog` as the TOC link target. `home.md` updated to match.
- Note: changes to volume-mounted custom files require OtterWiki server restart to take effect.

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
