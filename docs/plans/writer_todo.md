# Writer Todo

## In Progress

## Backlog

### [ ] Publish Manual Standards page (Section 1)

Migrate `docs/plans/architecture_decisions.md` into the OtterWiki as the `manual-standards` page under Section 1 (General Information).

**What this is:** `architecture_decisions.md` is already written and complete. This task is a publishing step, not a writing task — convert it to a clean wiki page, not a planning document.

**Steps:**
1. Read `docs/plans/architecture_decisions.md` in full
2. Create `manual-standards.md` in the WR
3. Strip all internal planning notes (e.g., "Note to Architect:", "Note to Writer:") — these are not for the published manual
4. Strip the "What Belongs Here" section — that's guidance for editors, not maintainers
5. Convert all internal cross-references to wiki links using `[[Display Text|page-name]]` format
6. Apply standard formatting (Type 4 Reference page — no fixed template, structure to suit content)
7. Use `[TOC]` — the page has many sections and a TOC will help navigation
8. After publishing, update `claude/content_development_overview.md` to reference the OtterWiki page as the authoritative location (replacing the reference to `docs/plans/architecture_decisions.md`)

**Do NOT delete `docs/plans/architecture_decisions.md`** — it remains the working copy for the Architect to update. The OtterWiki page is a published snapshot; the AR file is the source of truth until a better workflow is established.

---

### [x] Configure OtterWiki print footer and write Record of Revisions page (2026-04-16)

- Print footer implemented via `customBody.html` + `custom.css` in `~/otterwiki_system/custom/`. Uses `document.lastModified` (reliable: OtterWiki sets Last-Modified header from git commit datetime). Shows date only — no git hash.
- `record-of-revisions.md` written and committed to WR. Explains git-based tracking, print footer, page history, and links to `/?do=recent` built-in view.
- TOC updated: `record-of-revisions` replaces `/?do=recent` as the TOC link target. `home.md` updated to match.
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
