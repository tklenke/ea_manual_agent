# Writer Todo

## Backlog

### [x] Add connector pinouts to `avionics-arinc-429-adapter` (GAD 29)

Created `avionics-arinc-429-adapter-pinouts` sub-page (J291, J292 tables). Component page updated to link to it; both pages are draft. Needs Reviewer.

**Pattern established:** connector pinouts live on a dedicated `*-pinouts` sub-page, linked from the component page Specifications section. Use this pattern for all avionics component pages.

### [ ] Add connector pinout sub-pages for remaining avionics LRUs (Section 17)

Create a `[component-slug]-pinouts` page for each LRU below, linked from the component page. Input files have been consumed (renamed `_pending`):

- `avionics-primary-flight-display` (GDU 460) — GDU460_conn.md: P4X01 (DE9), P4X02 (DB50), P4X03 (DE9)
- `avionics-engine-data-acquisition` (GEA 24) — GEA24_conn.md: J241 (DE9), J242 (DB25), J243 (DB37), J244 (DB50)
- `avionics-audio-panel` (GMA 245) — GMA245_conn.md: J2401 (DB44), J2402 (DB44)
- `avionics-gps-and-navigation` (GNC 355) — GNC355_conn.md: J3551 (DB62), J3552 (DB44)
- `avionics-autopilot` (GMC 507 + GSA 28) — GSA28_conn.md: J7001/GMC507 (DE15), J281P/J281R/GSA28 (DA15)
- `avionics-adahrs` (GSU 25C) — GSU25_conn.md: J251 (DE9), J252 (15-pin)
- `avionics-backup-instrument` (G5) — GTP59GMU11G5_conn.md: J51 (DE9)
- `avionics-magnetometer` (GMU 11) — GTP59GMU11G5_conn.md: J111 (DE9)
- `avionics-vhf-communication` (GTR 20) — GTR20_conn.md: J2001 (DB37)
- `avionics-transponder-adsb` (GTX 45R) — GTX45R_conn.md: P3251 (DB62), P3252 (DE15)

### [ ] Wire marking convention — `electrical-wiring` and avionics data bus pages

Reference `docs/references/electrical/ea_wire_marking_standard.md` when drafting content that involves wire identification:

- **`electrical-wiring` (Section 16):** Include a section describing the wire marking convention used on N657CZ (label format, system codes, segment letters). This gives a maintainer the vocabulary to interpret wire labels during inspection or repair.
- **Avionics data bus pages (Section 17):** Where CAN bus or ARINC 429 wiring is discussed (e.g., `avionics-adahrs`, `avionics-arinc-429-adapter`), reference the D-code circuit ID ranges (D001–D009 for CAN, D010–D099 for ARINC 429) so wire labels in the harness can be correlated to the documentation.

Wire gauge, insulation type, and endpoints are recorded in the wiring log / schematic notes, not on the label itself — do not present the label alone as a complete wire specification.

### [~] Write `inspection-annual-condition` — Annual Condition Inspection

Checklist content complete; ready for Reviewer. Open `@@TOM:` flags: spark plug gap spec, propeller bolt torque, GPS antenna model, seat heater install, parking brake actuator config, valve cover torque values.
