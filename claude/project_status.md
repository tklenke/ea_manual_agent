## Project Overview

**ea_mxmanual** is a maintenance manual for a Cozy Mark IV experimental aircraft (N657CZ), written as a collection of Markdown files served by Otterwiki. The manual is intended for use by the aircraft owner/builder performing maintenance and inspection.

## Repository Structure

This project uses two git repositories:

- **Agent Repo (AR)** — `/home/tom/projects/ea_mxmanual` — planning documents, standards, role definitions, and reference materials.
- **Wiki Repo (WR)** — `/home/tom/projects/N657CZDashTwo` — all published manual content pages (wiki Markdown files).

The Writer creates all manual content pages in the WR. The AR contains everything else.

## Project Status

Architectural work is complete. The TOC has been fully audited and revised. All planning documents, style standards, and page templates are in place. The project is ready for the Writer to begin content development.

The Writer's first task is defined in `docs/plans/writer_todo.md`: configure the OtterWiki print footer for version tracing, then write the Record of Revisions page.

## Directory Structure

```
ea_mxmanual/
├── claude/                          - Claude guidance files for this project
│   ├── project_status.md            - This file
│   ├── content_development_overview.md - Operational standards for all roles
│   └── roles/
│       ├── architect.md             - Architect role definition
│       ├── writer.md                - Writer role definition
│       └── reviewer.md              - Reviewer role definition
├── docs/
│   ├── acronyms.md                  - Project shorthand terms and acronyms
│   ├── plans/                       - Planning and standards documents
│   │   ├── toc_structure.md         - Manual table of contents (authoritative)
│   │   ├── architecture_decisions.md - Manual Standards: structural decisions
│   │   │                              and content placement rules (will be
│   │   │                              published in Otterwiki, Section 1)
│   │   ├── style.md                 - Writing style: voice, tense, language rules
│   │   ├── formatting.md            - Formatting: naming, NOTEs, citations,
│   │   │                              cross-references
│   │   ├── templates.md             - Standard page structures by page type
│   │   ├── architect_todo.md        - Architect task tracking
│   │   ├── writer_todo.md           - Writer task tracking
│   │   └── poh_items.md             - Content identified for future POH
│   └── references/                  - Source reference materials (READ ONLY)
│       ├── AC43_13/                 - FAA Advisory Circular 43.13 extracted text
│       │                              Files named by chapter and page: ch##_p###.txt
│       │                              Appendices: appendix_1_glossary.txt, etc.
│       ├── electrical/              - Aircraft electrical engineering reports
│       │   └── engineering_report.md - kicad2wireBOM wire harness analysis
│       │                              for N657CZ (component inventory, wire BOM)
│       └── tds/                     - Manufacturer Technical Data Sheets (PDF)
├── input/                           - Drop zone for passing instructions to Claude between sessions
│   ├── architect_todo/              - New architectural tasks for Architect to pick up at session start
│   ├── writer_todo/                 - New writing tasks for Writer to pick up at session start
│   └── feedback/                   - Feedback on published wiki pages for Writer to process
├── otterwiki/                       - Otterwiki instance (not yet configured)
└── tools/                           - Development tools
    ├── CLAUDE.md                    - Claude guidance for tools (Python-optimized)
    ├── claude/                      - Claude role/context files for tools
    ├── PDFindexer/                  - Python tool used to extract AC43_13 text
    └── wikiCheck/                   - Wiki integrity checker (broken links, review log)
        └── plans/spec.md            - Build spec
```

## Key Documents

- **`docs/plans/toc_structure.md`** — The authoritative TOC: 18 sections, all pages defined.
- **`docs/plans/architecture_decisions.md`** — Manual Standards: structural and editorial decisions with rationale. Will be published in the manual under Section 1.
- **`docs/plans/style.md`** — Writing style rules.
- **`docs/plans/formatting.md`** — Formatting conventions: naming, NOTEs, citations, cross-references.
- **`docs/plans/templates.md`** — Standard page structures for the four page types.
- **`docs/plans/writer_todo.md`** — Writer's current task list. Start here.
- **`docs/plans/architect_todo.md`** — Architect's current task list.
- **`docs/plans/poh_items.md`** — Content identified as belonging in the POH, not this manual.
- **`docs/acronyms.md`** — Shorthand terms used between Claude and Tom during development.

## Reference Materials

All files in `docs/references/` are **READ ONLY**. Never modify these files.

- **`docs/references/AC43_13/`** — FAA Advisory Circular 43.13. Text files extracted from the PDF, organized by chapter and page.
- **`docs/references/electrical/engineering_report.md`** — Wire harness engineering report for N657CZ generated from the KiCad schematic. Contains the authoritative component inventory (LRU list), wire BOM, and electrical calculations. Use this as the reference for what avionics and electrical equipment is actually installed on the aircraft.
- **`docs/references/tds/`** — Manufacturer Technical Data Sheets for specific products used on the aircraft.

When AC 43.13 and a TDS conflict, the TDS takes precedence. See `docs/plans/formatting.md` for the Source Conflict NOTE format.

## TOC Summary

18 sections covering: General Information, Safety Precautions, Aircraft General, Weight and Balance, Ground Handling, Servicing, Inspection, Structures, Canopy and Panels, Cargo and Cabin Systems, Emergency Equipment, Flight Controls, Landing Gear and Brake System, Power Plant, Fuel System, Electrical System, Avionics, Heating and Ventilating.

Section 15 (Instruments) was folded into Section 17 (Avionics). Section 18 (Accessories) was removed. See `docs/plans/architecture_decisions.md` for full rationale.
