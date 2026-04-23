# Writer Todo

## Backlog

### [ ] Wire marking convention — `electrical-wiring` and avionics data bus pages

Reference `docs/references/electrical/ea_wire_marking_standard.md` when drafting content that involves wire identification:

- **`electrical-wiring` (Section 16):** Include a section describing the wire marking convention used on N657CZ (label format, system codes, segment letters). This gives a maintainer the vocabulary to interpret wire labels during inspection or repair.
- **Avionics data bus pages (Section 17):** Where CAN bus or ARINC 429 wiring is discussed (e.g., `avionics-adahrs`, `avionics-arinc-429-adapter`), reference the D-code circuit ID ranges (D001–D009 for CAN, D010–D099 for ARINC 429) so wire labels in the harness can be correlated to the documentation.

Wire gauge, insulation type, and endpoints are recorded in the wiring log / schematic notes, not on the label itself — do not present the label alone as a complete wire specification.

### [~] Add citations to avionics pinout sub-pages

Source information provided via `input/writer_todo/pinout_citations.txt`. For each of the 11 pinout pages, resolve the `@@TOM:` flag by:
1. Adding an inline citation to the cited source section
2. Verifying the pinout table data against the cited source

Source map (component → source):
- GAD 29 → G3XInstallationManual_RevAZ.pdf §23.2
- GDU 460 → G3XInstallationManual_RevAZ.pdf §23.3 → `avionics-primary-flight-display-pinouts`
- GEA 24 → G3XInstallationManual_RevAZ.pdf §23.4 → `avionics-engine-data-acquisition-pinouts`
- GMA 245 → GMA245InstallManualRev13.pdf §4.2 → `avionics-audio-panel-pinouts`
- GNC 355 → GNC355_InstallManual_Rev01.pdf Appendix → `avionics-gps-and-navigation-pinouts`
- GMC 507 → G3XInstallationManual_RevAZ.pdf §23.9 → `avionics-autopilot-pinouts`
- GSA 28 → G3XInstallationManual_RevAZ.pdf §23.13 → `avionics-autopilot-pinouts`
- GSU 25 → G3XInstallationManual_RevAZ.pdf §23.14 → `avionics-adahrs-pinouts`
- G5 → G5InstallationManualRev8.pdf Appendix A → `avionics-backup-instrument-pinouts`
- GMU 11 → G3XInstallationManual_RevAZ.pdf §23.10 → `avionics-magnetometer-pinouts`
- GTR 20 → G3XInstallationManual_RevAZ.pdf §23.16 → `avionics-vhf-communication-pinouts`
- GTX 45R → GTX45RInstallManual_Rev03.pdf §5.1 → `avionics-transponder-adsb-pinouts`

Note: `avionics-arinc-429-adapter-pinouts` source TBD — not covered in pinout_citations.txt.

### [~] Write `inspection-annual-condition` — Annual Condition Inspection

Checklist content complete; ready for Reviewer. Open `@@TOM:` flags: spark plug gap spec, propeller bolt torque, GPS antenna model, seat heater install, parking brake actuator config, valve cover torque values.
