# Architect Todo

## In Progress

## Backlog

### [ ] Re-publish `manual-standards.md` to WR

`architecture_decisions.md` updated 2026-04-23 with: connector pinout sub-page pattern, electrical schematic sub-pages, wire marking standard as separate page. Writer should sync WR `manual-standards.md`.

**NOTE:** This task was added to writer_todo.md — Architect should verify Writer picks it up.

### [ ] Plan avionics pinout pages: N657CZ-specific connector wiring

Tom has a data schematic (draft) with actual connector pin numbers for N657CZ avionics. When available, use it to plan how N657CZ-specific wiring data is incorporated into the pinout sub-pages. The wire BOM from `docs/references/electrical/wire_bom.csv` has schematic symbol pin numbers only — not physical connector pins — so it cannot be used for this purpose.

### [~] Plan `wb-equipment-list` page (Section 4)

component_bom.csv with coordinates received 2026-04-23. Waiting on Tom to fill in weights in `docs/plans/wb_equipment_weights_input.md`. Once weights are provided, Architect will finalize the page plan and create the Writer task.

**NOTE FROM WRITER (2026-04-21):** During the avionics pinout session, Tom decided that connector pinout tables belong on dedicated sub-pages (`[component-slug]-pinouts`) rather than inline on component pages. The component page links to the pinout page from the Specifications section. Pattern is in use on `avionics-arinc-429-adapter` and `avionics-arinc-429-adapter-pinouts`. Architect should record this decision in `architecture_decisions.md` and publish an updated `manual-standards.md` to the WR.
