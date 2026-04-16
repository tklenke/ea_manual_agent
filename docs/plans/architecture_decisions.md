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

## Section 6: Inspection Structure

**Decision:** Three inspection tiers:
- 6.1 Annual Condition Inspection — single comprehensive checklist page
- 6.2 Post-Cross-Country Check — focused on stress/extended use items
- 6.3 Periodic Check — mid-season, broader than 6.2 but lighter than annual

**Reasoning:** Experimental aircraft under annual condition inspection only. The 6.2 and 6.3 tiers reflect practical maintenance intervals (roughly 10 hours and 50 hours of flying) without implying FAA-mandated tach-time requirements.

**Note:** 6.1 kept as a single page (not broken into sub-pages by system) to preserve its utility as a checklist. If it grows unwieldy, reconsider at next architectural review.

---

## Section 15 Folded into Section 16

**Decision:** Section 15 (Instruments) is eliminated. Instrument content is covered in Section 16 (Avionics).

**Reasoning:** The aircraft has a full glass panel (GDU 460 PFD, G5 backup, GEA 24 EIS). The traditional instruments/avionics boundary assumes steam gauges. On this aircraft, the displays and the avionics generating the data are the same hardware. Splitting them across two sections would force arbitrary decisions about where content belongs and require cross-referencing for every topic.

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

**Decision:** Alternator maintenance procedures live in Section 12 (Power Plant), not Section 14 (Electrical). Section 14 includes a cross-reference pointer to Section 12.

**Reasoning:** Alternators are engine-driven mechanical components. Their maintenance (belt tension, brush inspection, output testing) is physically performed at the engine. The electrical section covers distribution and consumption of power after it is generated, not the generation hardware itself.

---

## Panel and Cover Removal Procedures Live in Section 8

**Decision:** Removal and installation procedures for all panels and covers are in Section 8 (Canopy and Panels). Other sections that reference those panels include a cross-reference pointer rather than duplicating the procedure.

**Reasoning:** Single source of truth for panel procedures. A maintainer working on cabin access or firewall components should not have to reconcile two versions of the same removal steps.

**Examples:**
- Cabin Interior (Section 9) links to Armrests and Firewall Cover Panel in Section 8
- Any section requiring instrument panel access links to IP Access Panel in Section 8

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
- 3.1 General Layout and Configuration
- 3.2 Aircraft Dimensions and Weight
- 3.3 Systems Overview

**Reasoning:** 3.3 added to give a maintainer context before diving into individual systems. A high-level summary with cross-references reduces the chance of someone working on a system without understanding how it fits into the whole.

---

## Section 4: Ground Handling Structure

**Decision:** Four pages:
- 4.1 Towing Procedures
- 4.2 Jacking and Leveling
- 4.3 Tiedown and Parking
- 4.4 Storage

**Reasoning:** Tiedown separated from Jacking (previously misplaced as a sub-page of 4.2). Storage added as a maintenance task in its own right (fuel stabilizer, pitot cover, control locks, etc.).

---

## Section 5: Servicing Index Contents

**Decision:** The following tasks are indexed in Section 5 (each with interval and pointer to home section):

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
