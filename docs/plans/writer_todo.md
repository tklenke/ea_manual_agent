# Writer Todo

## Backlog

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



### [~] Create avionics-g3x-system page and publish G3X diagram — Section 17 (2026-04-18)

**Decision (Architect, 2026-04-18):** The G3X system interconnect diagram belongs on a new Type 1a System Page, `avionics-g3x-system` ("G3X System Overview"), added to the top of Section 17 in the TOC. This is the section entry point for the G3X avionics suite.

**Tasks:**
1. Create `avionics-g3x-system` in the WR as a Type 1a System Page.
2. Copy the SVG from `docs/references/diagrams/g3x-system-architecture.svg` in the AR to the WR as `assets/diagrams/sec17-g3x-system-interconnect.svg`.
3. Embed the diagram on the page.
4. The page should describe the G3X system, list the installed components (linking to each component's page), and include the interconnect diagram.

**SVG state:** Confirmed finished by Tom (2026-04-18).

### [x] Add nose-gear-tipping cross-reference to landing-gear-nose (when written)

When `landing-gear-nose` is written, include a cross-reference to `landing-gear-nose-gear-tipping`.
