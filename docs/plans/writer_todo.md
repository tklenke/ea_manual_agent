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



### [ ] Publish G3X system interconnect diagram to WR — Section 17 (2026-04-18)

A cleaned-up SVG of the G3X system interconnect diagram (based on Garmin installation manual Figure 2-1, edited for N657CZ) is in the AR at:

`docs/references/diagrams/g3x-system-architecture.svg`

**Task:** Copy it to the WR as `assets/diagrams/sec17-g3x-system-interconnect.svg` and embed it in the appropriate Section 17 page (likely `avionics-antennas` or a new system overview page for Section 17).

**Asset directory structure:** The WR now has `assets/diagrams/`, `assets/schematics/`, and `assets/photos/` directories. See `claude/content_development_overview.md` for naming conventions and the AR/WR asset workflow.

**Note on SVG state:** The diagram has been partially edited (components not installed on N657CZ are struck through). Tom was mid-edit in Inkscape when this task was created — verify the SVG is in its final state before publishing. The Architect's working copy in the AR is the source of truth.

### [ ] Add nose-gear-tipping cross-reference to landing-gear-nose (when written)

When `landing-gear-nose` is written, include a cross-reference to `landing-gear-nose-gear-tipping`.
