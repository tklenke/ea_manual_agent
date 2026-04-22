# Writer Todo

## Backlog

### [ ] Wire marking convention — `electrical-wiring` and avionics data bus pages

Reference `docs/references/electrical/ea_wire_marking_standard.md` when drafting content that involves wire identification:

- **`electrical-wiring` (Section 16):** Include a section describing the wire marking convention used on N657CZ (label format, system codes, segment letters). This gives a maintainer the vocabulary to interpret wire labels during inspection or repair.
- **Avionics data bus pages (Section 17):** Where CAN bus or ARINC 429 wiring is discussed (e.g., `avionics-adahrs`, `avionics-arinc-429-adapter`), reference the D-code circuit ID ranges (D001–D009 for CAN, D010–D099 for ARINC 429) so wire labels in the harness can be correlated to the documentation.

Wire gauge, insulation type, and endpoints are recorded in the wiring log / schematic notes, not on the label itself — do not present the label alone as a complete wire specification.

### [~] Write `inspection-annual-condition` — Annual Condition Inspection

Checklist content complete; ready for Reviewer. Open `@@TOM:` flags: spark plug gap spec, propeller bolt torque, GPS antenna model, seat heater install, parking brake actuator config, valve cover torque values.
