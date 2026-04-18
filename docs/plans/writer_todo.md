# Writer Todo

## In Progress

### [~] Antenna System page — Section 17 (2026-04-18)

New page `avionics-antennas` created. Session state (2026-04-18):
- aircraft-general-layout: pitch trim duplicate removed; antenna cross-ref added.
- aircraft-systems-overview: GA 35 added; GSB 15 (USB power plug) and GPS 20A (GPS source) resolved; G5 corrected to singular; Artex ELT345 added to Emergency Equipment.
- avionics-antennas: external (TED ADS-B → GTX 45R), internal (GA 35 → GPS 20A, G5 GPS antenna, ELT whip dipole → Artex ELT345), and embedded copper foil antennas documented.

Open @@TOM flags on avionics-antennas:
- TED ADS-B model confirmation
- Which stab antenna → GTR 20 vs. GNC 355 comm
- Right wing ~23" VOR/LOC → GNC 355 (confirm)
- Canard ~21": Localizer? (confirm function and LRU)
- Canard ~7" Glideslope → GNC 355 (confirm)
- Fuselage Marker Beacon → GNC 355 (confirm)

Pending Reviewer sign-off.

### [~] Section 3 — Aircraft General (2026-04-17)

Three pages to write. Scope agreed with Tom — avoid duplication across pages:

- **aircraft-general-layout** — Configuration and physical orientation. Canard pusher, composite, 4-seat. Where major systems/access points are physically located (canopy, cowling, firewall cover, nose cone, under-seat areas). No specs, no system descriptions.
- **aircraft-dimensions-and-weight** — Already exists with @@TOM flags. Leave flagged for now.
- **aircraft-systems-overview** — Inventory of major systems on N657CZ, one-sentence description each, cross-ref to section. No layout, no specs.

**Session state (2026-04-17):** aircraft-general-layout and aircraft-systems-overview complete and committed. aircraft-dimensions-and-weight exists with @@TOM flags — leave for now.

**Open @@TOM flags in aircraft-systems-overview:**
- Cooling system description (oil cooler, cowl flap arrangement)
- GSB 15 function
- GPS 20A function/role
- Cabin heat source and controls
- Ventilation arrangement
- Survival equipment (if any)

### [~] Write landing-gear-nose-gear-tipping page (2026-04-17)

Page complete. No open @@TOM flags. Not a TOC-level entry — accessed through `landing-gear-nose` (Architect decision 2026-04-18). Pending Reviewer sign-off.

Cross-reference status:
- `safety-general-shop` — link present
- `ground-handling-jacking-and-leveling` — link missing (see task below)
- `landing-gear-nose` — not yet written; link required when written

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

### [ ] Publish G3X system interconnect diagram to WR — Section 17 (2026-04-18)

A cleaned-up SVG of the G3X system interconnect diagram (based on Garmin installation manual Figure 2-1, edited for N657CZ) is in the AR at:

`docs/references/diagrams/g3x-system-architecture.svg`

**Task:** Copy it to the WR as `assets/diagrams/sec17-g3x-system-interconnect.svg` and embed it in the appropriate Section 17 page (likely `avionics-antennas` or a new system overview page for Section 17).

**Asset directory structure:** The WR now has `assets/diagrams/`, `assets/schematics/`, and `assets/photos/` directories. See `claude/content_development_overview.md` for naming conventions and the AR/WR asset workflow.

**Note on SVG state:** The diagram has been partially edited (components not installed on N657CZ are struck through). Tom was mid-edit in Inkscape when this task was created — verify the SVG is in its final state before publishing. The Architect's working copy in the AR is the source of truth.



### [ ] Add nose-gear-tipping cross-reference to ground-handling-jacking-and-leveling (2026-04-18)

`ground-handling-jacking-and-leveling` exists but does not link to `landing-gear-nose-gear-tipping`. Add a cross-reference — the jacking procedure is a context where the nose gear tipping hazard is directly relevant.

### [~] Write powerplant-cooling-system page — Section 14 (2026-04-18)

Page drafted. Open @@TOM flags:
- Oil cooler model confirmation (expected: AeroClassic 8000216, 17-row drawn cup)
- Cockpit control location for louver cable
- Target oil temperature range for Lycon-upgraded O-360
- Lubrication spec for cable and louver pivots
- Cable adjustment procedure

Pending Reviewer sign-off.

### [ ] Add nose-gear-tipping cross-reference to landing-gear-nose (when written)

When `landing-gear-nose` is written, include a cross-reference to `landing-gear-nose-gear-tipping`.


