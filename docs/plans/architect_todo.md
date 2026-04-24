# Architect Todo

## In Progress

## Backlog

### [x] Document connector pinout sub-page pattern in `architecture_decisions.md`

### [ ] Plan avionics pinout pages: N657CZ-specific connector wiring

Tom has a data schematic (draft) with actual connector pin numbers for N657CZ avionics. When available, use it to plan how N657CZ-specific wiring data is incorporated into the pinout sub-pages. The wire BOM from `docs/references/electrical/wire_bom.csv` has schematic symbol pin numbers only — not physical connector pins — so it cannot be used for this purpose.

### [ ] Plan `wb-equipment-list` page (Section 4)

Waiting on updated `component_bom.csv` from Tom with FS/WL/BL coordinates filled in for all LRUs (30 items currently 0/0/0 — list provided 2026-04-23). Scope: materially significant components only (avionics LRUs, batteries, alternators, starter, major actuators). Exclude diodes, relays, fuses, wire runs.

**NOTE FROM WRITER (2026-04-21):** During the avionics pinout session, Tom decided that connector pinout tables belong on dedicated sub-pages (`[component-slug]-pinouts`) rather than inline on component pages. The component page links to the pinout page from the Specifications section. Pattern is in use on `avionics-arinc-429-adapter` and `avionics-arinc-429-adapter-pinouts`. Architect should record this decision in `architecture_decisions.md` and publish an updated `manual-standards.md` to the WR.
