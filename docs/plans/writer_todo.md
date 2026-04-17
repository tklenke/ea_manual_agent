# Writer Todo

## In Progress

## Backlog

### [x] Write aircraft-dimensions-and-weight page — Section 3 (from input 2026-04-17)

Type 1b Component page (or Type 4 Reference page) in Section 3 (Aircraft General). Tom provided official Cozy MK IV specifications.

Key specs from input:
- Seats: 4
- Gross Weight: 2050 lbs, Empty Weight: ~1050 lbs
- Max Speed: 220 mph, Min Speed: 64 mph, Range: 1350 mi (w/ 1 hr reserve)
- Wing Span: 28.1 ft, Canard Span: 11.5 ft, Total Wing Area: 101.4 sq. ft.
- Length: 17.0 ft, Height: 7.9 ft
- Cockpit Width Front: 42.0 in, Rear: 38.0 in
- Nose Gear: manual retract
- Engine: Lycoming O-360
- Wing Airfoil: Modified Eppler, Canard Airfoil: Roncz 1145MS
- Plans/support: Aircraft Spruce (Corona, CA); Marc J. Zeitlin (official support, Tehachapi CA)

Source: Cozy MK IV official specs (from input). Verify against plans/builders manual as available.

Input file: `input/writer_todo/COZY MKIV General Information` (renamed to `_pending` after logging)

---

### [x] Write ground-handling-jacking-and-leveling page — Section 5 (from input 2026-04-17)

Type 2 Procedure page in Section 5 (Ground Handling). Tom provided builder community notes on jacking the Cozy MK IV.

Key details from input:
- Jack under center section spar or wing spar — NOT on wing/strake skins
- Further outboard jack placement → more nose weight; prefer end of center spar or just outboard of outboard wing mount bolts
- Use pads (e.g., 4" 2 lb styrofoam, or 12"x12"x3/4" plywood) to distribute load
- Method: extend nose gear → position jacks under center spar → raise aircraft (main gear lift off); or use padded sawhorses
- Do NOT jack on skins — always spar with suitable pad
- No factory-specified jack points; jacking spar with appropriate pads is accepted practice

Source: CozyRAG builder community notes (from input). Cross-reference AC 43.13 for general jacking guidance. Flag any unverified safety specifications.

Input file: `input/writer_todo/Jacking General.md` (renamed to `_pending` after logging)

---

### [ ] Write wb-weighing-procedures page — Section 4 (from input 2026-04-17)

Type 2 Procedure page in Section 4 (Weight and Balance). Tom provided builder's notes on weighing procedures for the Cozy MK IV.

Key details from input:
- Load-cell type scales (stacked on floor jacks) are problematic — jack location can't be verified by plumb bob after placement; inaccurate CG results
- Preferred method: flat scales with wooden ramps; aircraft driven up onto scales; allows re-verification; safer
- Do in closed hangar — wind affects readings
- Use digital level; chalk line on floor to translate plumb bob positions; straight edge for reference
- Wing leading edge FS 113.9 is the datum — set tape to 113.9 on translated wing LE point
- Follow Owners Manual description and examples
- Need at least one helper

Source: Builder community experience (from input). Must reference Cozy MK IV Owners Manual for official procedure. Flag any steps not confirmed by authoritative source. Cross-reference `ground-handling-jacking-and-leveling` for jacking procedures.

Input file: `input/writer_todo/Jacking for weight and balance.md` (renamed to `_pending` after logging)

---

### [x] Write fuel-level-sensors page (from input 2026-04-17)

Type 1b Component page in Section 15 (Fuel System). Tom provided installation notes and product info for the Stewart Warner 385B fuel level sender (SWW-385B from Summit Racing). No PDF/TDS available — product data from Summit Racing listing only. Gasket sealant used: Permatex Form-A-Gasket No. 2. See `input/writer_todo/fuel_level_sensors.txt` (deleted after logging — content preserved in this entry).

Key details from Tom's notes:
- Sender: Stewart Warner 385B, 240Ω empty / 33Ω full, lever style, 6–12 in. depth tank
- Mounts via SAE-5 flange; 5 bolts; max ~2 full turns before bolt exits flange
- Probe bent so tip nearly contacts top and bottom of tank interior — no contact allowed
- Gasket sealant: Permatex Form-A-Gasket No. 2 (thin layer, tighten until gasket just begins to bulge)
- Wires: 3-pin connector (red, black, yellow) to EMS; calibrate empty and full positions
- No TDS available — product data from Summit Racing listing only

---

### [x] Resolve readme.md and home.md Section 1 mismatch (flagged by Reviewer 2026-04-17)

`home.md` links to `[[README|readme]]` under Section 1, but `toc_structure.md` shows that slot as `[[start#disclaimer|Disclaimer]] and [[https://www.gnu.org/licenses/fdl-1.3.html|License]] Information`. The current `readme.md` is a legacy git README — it does not conform to manual style (emojis, asterisk bullets, evaluative language, broken URL). Options:
- Rewrite `readme.md` as a proper Disclaimer/License page and update `home.md` to match the TOC
- Or remove `readme.md` and update `home.md` to point to the Disclaimer/License per the TOC

Discuss with Tom before proceeding. `home.md` is marked pending until resolved.

---

### [x] Write panels-turtleback-windows page (flagged by Reviewer 2026-04-17)

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
