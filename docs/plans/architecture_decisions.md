# Manual Standards

This document will be published in the manual as the **Manual Standards** page under Section 1 (General Information). It is the authoritative reference for how this manual is organized and why.

## What Belongs Here

This document captures three categories of content:

- **Architecture decisions** — structural choices about the manual: scope boundaries, section organization, where specific topics live, and why. Example: why alternators are in Power Plant rather than Electrical.
- **Content placement rules** — standing rules for where types of content belong. Example: all panel removal procedures live in Section 9 (Canopy and Panels); other sections cross-reference rather than duplicate.
- **Editorial standards** — conventions for how content is written and organized within pages. Example: lists are alphabetical by default.

When in doubt whether something belongs here: if a future Architect or Writer would need to know it to make a consistent decision, it belongs here.

**Note to Architect:** After the TOC audit is complete, create a task for the Writer to migrate this document into the Otterwiki as the Manual Standards page under Section 1. Update `claude/content_development_overview.md` to reference the Otterwiki location.

---

## Manual Scope

**Decision:** This is a maintenance manual only. Fabrication and build content is out of scope.

**Reasoning:** The aircraft is built. The manual is for the owner/maintainer performing ongoing maintenance and inspection. Build procedures are not needed and would create confusion about what applies to a completed aircraft.

**Effect on TOC:**
- Removed `flight-controls-fabrication-notes` (was Section 10)
- Removed `flipping-fuselage` (was Section 5)

---

## Version and Revision Information

**Decision:** Version and revision metadata is NOT embedded in page content. It is provided automatically via OtterWiki print customization.

**Implementation:** OtterWiki's `customBody.html` injects a print-only footer using `@media print` CSS. The footer displays the page's last-edited timestamp (from `page.updated` in the Jinja2 template context) and ideally the short git commit hash, so a printed page can be traced back to an exact version in git.

**Target format:** `Last edited: YYYY-MM-DD HH:MM (short-hash)`

**Reasoning:** Manual timestamps in page content require Writer discipline to maintain and will inevitably drift out of sync. OtterWiki sits on a git backend — the authoritative version information is already there. Automating the footer keeps pages clean, requires no per-edit maintenance, and provides more reliable version tracing than anything manually maintained.

**Setup task:** See architect_todo.md — OtterWiki version footer configuration is a backlog item.

---

## Lubrication Page: Master List with Pointers

**Decision:** The Lubrication page in Section 6 (Servicing) is a comprehensive list of all lubrication points on the aircraft, each with its interval and a pointer to the procedure in the relevant section. It does not contain procedures itself.

**Reasoning:** Same pattern as the overall Section 6 — single place to find everything that requires lubrication, without duplicating procedures that live with the system they belong to.

---

## Section 6: Servicing as Master Index

**Decision:** Section 6 is a master index of all servicing tasks, not a collection of procedures. Each task entry states the service interval and points to the full procedure in its home section.

**Reasoning:** A maintainer planning a service event needs a single place to see everything that requires attention. Duplicating procedures in Section 6 would create maintenance burden and risk of conflicting information.

**Effect:** Procedures like oil change live in Section 14 (Power Plant). Section 6 lists "Oil and Filter" with interval and a pointer to Section 14.

**TOC structure:** Two pages in the TOC:
- `[[servicing|Servicing]]` — master index page; all tasks listed below are `##` sections within this page
- `[[servicing-lubrication|Lubrication]]` — its own page due to volume (comprehensive list of all lubrication points with intervals and pointers)

**Tasks consolidated as sections within `servicing`:**
- Air Filter → Section 14 (Power Plant)
- Avionics Software Updates → Section 17 (Avionics)
- Battery Service → Section 16 (Electrical)
- Brakes → Section 13 (Landing Gear and Brake System)
- Canopy and Door Seals → Section 9 (Canopy and Panels)
- Control Surface Hinges and Linkages → Section 12 (Flight Controls)
- Cooling System → Section 14 (Power Plant)
- Fuel Filters → Section 15 (Fuel System)
- Interior → Section 10 (Cargo and Cabin Systems)
- Lighting → Section 16 (Electrical)
- Oil and Filter → Section 14 (Power Plant)
- Pitot/Static System → Section 17 (Avionics)
- Propeller → Section 14 (Power Plant)
- Spark Plugs → Section 14 (Power Plant)
- Tires and Wheels → Section 13 (Landing Gear and Brake System)
- Wing Removal and Installation → Section 8 (Structures)

**Tasks that may warrant their own page** (Writer to decide based on content volume):
- Exterior Finish — may have enough product notes, cautions, and technique guidance to stand alone
- Fueling — may have enough detail (fuel grades, quantities, anti-contamination steps) to stand alone

---

## Section 7: Inspection Structure

**Decision:** Three inspection tiers:
- Annual Condition Inspection — single comprehensive checklist page
- Post-Cross-Country Check — focused on stress/extended use items
- Periodic Check — mid-season, broader than Post-Cross-Country but lighter than annual

**Reasoning:** Experimental aircraft under annual condition inspection only. The Post-Cross-Country and Periodic tiers reflect practical maintenance intervals (roughly 10 hours and 50 hours of flying) without implying FAA-mandated tach-time requirements.

**Note:** The Annual Condition Inspection page is kept as a single page (not broken into sub-pages by system) to preserve its utility as a checklist. If it grows unwieldy, reconsider at next architectural review.

---

## Section 17: G3X System Overview Page at Top of Section

**Decision:** `avionics-system-overview` is added as the first page in Section 17, ahead of the alphabetical component listing. It is a Type 1a System Page and the home for the G3X system interconnect diagram.

**Reasoning:** A system interconnect diagram is section-level content that belongs on a system overview page, not on any individual component page. Placing it first gives a maintainer context before navigating to specific components. This is a justified override of the alphabetical default ordering.

---

## Section 17: Avionics Record Keeping Removed

**Decision:** Removed `avionics-record-keeping` from Section 17 (Avionics).

**Reasoning:** No clear content to put on the page. Software update procedures belong on each component's page, not a separate record keeping page. Wing removal and structural components belong to Section 8. If a genuine need for an avionics record keeping page emerges during writing, it can be added back.

---

## Section 17: Avionics (Instruments Folded In)

**Decision:** Section 15 (Instruments) is eliminated. Instrument content is covered in Section 17 (Avionics).

**Reasoning:** The aircraft has a full glass panel (GDU 460 PFD, G5 backup, GEA 24 EIS). The traditional instruments/avionics boundary assumes steam gauges. On this aircraft, the displays and the avionics generating the data are the same hardware. Splitting them across two sections would force arbitrary decisions about where content belongs and require cross-referencing for every topic.

---

## Page Status Block

**Decision:** Every content page includes a status block immediately after the H1 heading, before the first `##` section. Three states: `:::draft`, `:::pending`, `:::approved`. Each includes a date (except draft, which has no review date yet).

**Reasoning:** Readers need an immediate visual cue about whether a page has been reviewed. A status block in the page content is visible without navigating to any external system, works in OtterWiki's rendered view, and is tracked in git history.

**Implementation:** Custom CSS in `_otterwiki_system/custom/custom.css` defines the three alert types. Block format and rules are in `docs/plans/formatting.md`. All templates include the `:::draft` block.

**Exemptions:** `readme.md` and `home.md` are exempt — they are not content pages.

**Workflow:** Writer adds `:::draft` on page creation (via template). Reviewer changes to `:::approved` or `:::pending` at sign-off. Writer upgrades `:::pending` to `:::approved` when feedback resolves all deferred flags.

---

## Weight and Balance as Standalone Section

**Decision:** Weight and Balance is its own top-level section, not a sub-section of Section 3 (Aircraft General).

**Reasoning:** W&B is a recurring maintenance task with its own procedures, not just background information. It warrants a dedicated section so a maintainer can find it directly.

---

## Section 1: Remove Meta-Content

**Decision:** Removed `Instructions for development of Design and Troubleshooting Documentation` from Section 1.

**Reasoning:** This was guidance for Claude/Tom during manual development, not content for a maintainer. It does not belong in the published manual.

---

## Alternators: Power Plant, Not Electrical

**Decision:** Alternator maintenance procedures live in Section 14 (Power Plant), not Section 16 (Electrical). Section 16 includes a cross-reference pointer to Section 14.

**Reasoning:** Alternators are engine-driven mechanical components. Their maintenance (belt tension, brush inspection, output testing) is physically performed at the engine. The electrical section covers distribution and consumption of power after it is generated, not the generation hardware itself.

---

## Panel and Cover Removal Procedures Live in Section 9

**Decision:** Removal and installation procedures for all panels and covers are in Section 9 (Canopy and Panels). Other sections that reference those panels include a cross-reference pointer rather than duplicating the procedure.

**Reasoning:** Single source of truth for panel procedures. A maintainer working on cabin access or firewall components should not have to reconcile two versions of the same removal steps.

**Examples:**
- Cabin Interior (Section 10) links to Armrests and Firewall Cover Panel in Section 9
- Any section requiring instrument panel access links to IP Access Panel in Section 9

---

## TOC Depth: Component-Specific Procedures Are Not Listed

**Decision:** Type 2 Procedure pages that are specific to a single component are not listed in the TOC. They are accessed through their parent component's Type 1b page.

**Reasoning:** The TOC reflects the manual's structure at the component/system level. Listing every procedure would make the TOC unwieldy and suggest a flat organization that doesn't exist. A maintainer navigates to the component page first; from there, procedures are one click away.

**What does belong in the TOC:**
- All Type 1a System pages and Type 1b Component pages
- Section-level index pages (e.g., Servicing index, Lubrication index, Annual Condition Inspection)

**What does not belong in the TOC:**
- Component-specific procedures, even substantial ones (e.g., Canopy Cleaning, Wing Removal and Installation, Battery Removal, Brake Fluid Change) — these are accessed through their parent component page in the relevant section

---

## List Ordering: Alphabetical by Default

**Decision:** Lists of pages, items, or components are ordered alphabetically by default. This can be overridden when a different order is clearly better (e.g., procedural sequence, logical grouping), but alphabetical is the starting assumption.

**Reasoning:** Alphabetical ordering is predictable and makes items findable without requiring the reader to understand the author's organizational logic. Arbitrary ordering creates maintenance burden as items are added over time.

---

## Section 2: Safety Precautions Structure

**Decision:** Five pages covering hazards specific to this aircraft:
- Electrical Safety
- Fire and Fuel Hazards
- Composite Material Hazards
- Fluids and Chemicals
- General Shop Safety

**Reasoning:** Kept aircraft-specific. Generic shop safety content excluded. Composite material hazards included because fiberglass dust and epoxy are present in both repair work and routine inspection of this airframe.

---

## Section 3: Aircraft General Structure

**Decision:** Three pages:
- General Layout and Configuration
- Aircraft Dimensions and Weight
- Systems Overview

**Reasoning:** Systems Overview added to give a maintainer context before diving into individual systems. A high-level summary with cross-references reduces the chance of someone working on a system without understanding how it fits into the whole.

---

## Section 5: Ground Handling Structure

**Decision:** Four pages:
- Towing Procedures
- Jacking and Leveling
- Tiedown and Parking
- Storage

**Reasoning:** Tiedown separated from Jacking (previously misplaced as a sub-page of Jacking and Leveling). Storage added as a maintenance task in its own right (fuel stabilizer, pitot cover, control locks, etc.).

---

## Annual Condition Inspection Page Structure

**Decision:** The `inspection-annual-condition` page has two parts: (1) the inspection checklist, and (2) an annual servicing addendum — a cross-reference list of servicing tasks typically completed at annual time, with links to their home section pages.

**Reasoning:** Consumable specifications and servicing procedures belong on their component/section pages (single source of truth). The addendum gives a maintainer doing an annual one place to see what servicing is also due, without duplicating content that is maintained elsewhere.

**Effect:** Consumables list from the Zeitlin source is NOT reproduced on the ACI page. Procedure content is NOT duplicated — only cross-references with task name, interval, and link.

---

## Wire Marking Convention

**Decision:** All wiring on N657CZ uses the EA wire marking standard documented in `docs/references/electrical/ea_wire_marking_standard.md`.

**Label format:** System Code (1 char) + Circuit ID (3–5 chars) + Segment ID (1 optional char). Example: `L105A` = Lighting system, circuit 105, first physical segment.

**System codes** follow MIL-W-5088L Appendix B. Common codes for this aircraft: A (Avionics), D (Data bus), E (Engine Instrument), K (Engine Control), L (Lighting), P (DC Power), R (Radio/Nav), W (Warning/Emergency).

**Data bus wiring** uses system code D with structured circuit ID ranges: D001–D009 for CAN bus, D010–D099 for ARINC 429, D100+ for RS-232/RS-422 and discrete data wires.

**Effect on content:** The `electrical-wiring` page (Section 16) must describe this marking convention. Avionics pages that discuss data bus wiring (Section 17) must reference the D-code ranges for CAN and ARINC 429 connections. Wire labels mentioned anywhere in the manual must follow this format.

**References:** MIL-STD-681E, MIL-W-5088L, AC 43.13-1B Chapter 11.

---

## Section 6: Servicing Index Contents

**Decision:** The following tasks are indexed in Section 6 (each with interval and pointer to home section):

- Fueling
- Oil and Filter
- Spark Plugs
- Air Filter
- Cooling System
- Propeller
- Fuel Filters
- Brakes (fluid and pads)
- Tires and Wheels
- Battery Service (main and brownout)
- Pitot/Static System
- Control Surface Hinges and Linkages
- Canopy and Door Seals
- Exterior Finish
- Lighting
- Interior (seats and seat belts)
- Avionics Software Updates
- Wing Removal and Installation (pointer to Section 8 — no dedicated servicing page)
