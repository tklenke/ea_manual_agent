# Writer Todo

## Backlog

### [ ] Write avionics-arinc-429-adapter page — Section 17 (2026-04-19)

**Component:** Garmin GAD 29 ARINC 429 data concentrator. Confirmed installed (LRU24 in engineering report). Type 1b Component Page.

**Topics to cover:**
- Description and location on the aircraft
- Role in the G3X system — what ARINC 429 sources it bridges to the G3X (likely GNC 355)
- Inspection: connectors, mounting, indicator lights if any
- Procedures: none anticipated beyond inspection, but verify with Garmin G3X Installation Manual

**Source requirements:**
- Garmin G3X Installation Manual (`docs/references/tds/GarminG3XInstallationManual_az.pdf`) — primary source for GAD 29 specs, wiring, and installation
- Engineering report (`docs/references/electrical/engineering_report.md`) — confirms installation, LRU24
- Flag anything without a source with `@@TOM:`

### [ ] Re-publish formatting standards page — manual-standards-formatting (2026-04-19)

`docs/plans/formatting.md` was updated to add the Page Status Block section. Re-publish by updating `manual-standards-formatting.md` in the WR to match.

### [ ] Re-publish page templates page — manual-standards-page-templates (2026-04-19)

`docs/plans/templates.md` was updated to add `:::draft` status blocks to all four page templates. Re-publish by updating `manual-standards-page-templates.md` in the WR to match.

### [~] Write nose gear actuator page — Section 13 (Landing Gear) (2026-04-18)

**Component:** Wilhelmson EZ Nose Lift electric nose gear actuator. N657CZ has the Marc Zeitlin clamp modification installed.

**Topics to cover (per Tom's notes in `input/writer_todo/nose_gear_actuator_pending.txt`):**
- Description and location
- Limit switch adjustment
- Electrical connections inspection (relays, wiring)
- Actuator function check (on jacks)
- Manual backup functionality testing
- Mechanical inspection (alignment, fasteners, gear teeth)
- Lubrication
- Marc Zeitlin EZ Nose Lift clamp — what it is and why it's installed

**Source requirements:** Tom's notes are background only — no authoritative citations. Research needed:
- Wilhelmson installation/maintenance documentation (ask Tom if available)
- Marc Zeitlin's write-up or SB for the clamp (ask Tom for source)
- AC 43.13 for applicable general maintenance procedures
- Flag anything without a source with `@@TOM:`



### [~] Create avionics-system-overview page and publish G3X diagram — Section 17 (2026-04-18)

**Decision (Architect, 2026-04-18):** The G3X system interconnect diagram belongs on a new Type 1a System Page, `avionics-system-overview` ("G3X System Overview"), added to the top of Section 17 in the TOC. This is the section entry point for the G3X avionics suite.

**Tasks:**
1. Create `avionics-system-overview` in the WR as a Type 1a System Page.
2. Copy the SVG from `docs/references/diagrams/g3x-system-architecture.svg` in the AR to the WR as `assets/diagrams/sec17-g3x-system-interconnect.svg`.
3. Embed the diagram on the page.
4. The page should describe the G3X system, list the installed components (linking to each component's page), and include the interconnect diagram.

**SVG state:** Confirmed finished by Tom (2026-04-18).

