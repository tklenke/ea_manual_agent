# Writer Todo

## In Progress

### [~] Section 3 — Aircraft General (2026-04-17)

Three pages to write. Scope agreed with Tom — avoid duplication across pages:

- **aircraft-general-layout** — Configuration and physical orientation. Canard pusher, composite, 4-seat. Where major systems/access points are physically located (canopy, cowling, firewall cover, nose cone, under-seat areas). No specs, no system descriptions.
- **aircraft-dimensions-and-weight** — Already exists with @@TOM flags. Leave flagged for now.
- **aircraft-systems-overview** — Inventory of major systems on N657CZ, one-sentence description each, cross-ref to section. No layout, no specs.

**Session state (2026-04-17):** aircraft-general-layout complete and committed. Next: aircraft-systems-overview (interview Tom to fill gaps). aircraft-dimensions-and-weight exists with @@TOM flags — leave for now.

### [~] Write landing-gear-nose-gear-tipping page (2026-04-17)

Page complete. No open @@TOM flags. Cross-references still needed from ground-handling section and landing-gear-nose (both unwritten). TOC placement pending Architect decision. Pending Reviewer sign-off.

### [~] Write safety-fluids-and-chemicals page — Section 2 (2026-04-17)

Type 4 Reference page in Section 2. Covers AeroShell W100+, MIL-H-5606A, IPA, brake cleaner, Simple Green, Permatex thread sealant, LPS aerosols. No open @@TOM flags. Ready for Reviewer sign-off.

### [~] Write safety-fire-and-fuel page — Section 2 (2026-04-17)

Type 4 Reference page in Section 2 (Safety Precautions). Covers 100LL fire hazards, ignition source elimination, grounding (cross-ref to Section 15), and fuel system work precautions.

**Status:** Draft complete and committed to WR. No open @@TOM flags. Pending Reviewer sign-off.

### [~] Write safety-electrical page — Section 2 (2026-04-17)

Type 4 Reference page in Section 2 (Safety Precautions). Covers electrical hazards: de-energization procedure, short circuit hazards, LiFePO4 battery chemistry, and pre-energization checks.

**Status:** Ready for Reviewer sign-off. All @@TOM flags resolved.

### [~] Write safety-composite-materials page — Section 2 (2026-04-17)

Type 4 Reference page in Section 2 (Safety Precautions). Covers hazards from composite materials encountered during maintenance and inspection of N657CZ.

**Epoxy systems used in construction (@@TOM: confirm details before publishing):**

- **EZ-Poxy** — Resin: EZ 10. Hardeners: EZ 83 (fast), EZ 84 (medium), EZ 87 (slow). EZ 87 noted for fuel resistance (MOGAS applications).
- **Proset** — Made by Gougeon Brothers (same as West System). Hardeners include LAM 125 (medium) and LAM 224 (fast). Suitable for structural aviation applications.
- **MGS** — Resins: MGS 285 and MGS 335. MGS 335 noted for less aggressive skin reactions. Low viscosity; not as fuel resistant as some alternatives.
- **West System** — Resin: West 105. Hardeners: 205 (fast), 206 (slow), 207 (special clear), 209 (extra slow). Favored for sanding and cosmetic finishes.

No TDS available in `docs/references/tds/` for any of these systems. @@TOM: obtain TDS for each system if available.

**Status:** Draft complete and committed to WR. Two @@TOM flags open — confirm epoxy system details and add MSDS sources when available. Pending Reviewer sign-off.

## Backlog

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
