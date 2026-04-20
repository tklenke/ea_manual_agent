# Writer Todo

## Backlog

### [ ] Write `inspection-annual-condition` — Annual Condition Inspection

**Source:** `docs/references/Canard_CI-PB-Checklist_Template_MZeitlin.csv`

Tom has added an `N657CZ` column. Any row marked `na` in that column is not applicable to this aircraft — skip it. Follow Tom's annotations for equipment-specific alternatives (e.g., where the list offers multiple avionics or ignition options, Tom's column identifies the one installed).

#### Page scope

The ACI page is an inspection checklist only. It does not contain:
- Consumable specifications (oil type, tire size, brake fluid spec, etc.) — those belong on individual component pages in the relevant sections
- Servicing procedures — those live in Section 6 and home sections

The page has two parts:

**Part 1 — Inspection checklist**: Area-by-area items derived from the Zeitlin source, filtered to N657CZ. Preserve the source's area groupings (Canard Area, Nose Area, Top Fuselage, Fuselage Bottom, Front Cockpit, Rear Cockpit, Strake/Wing/Winglet, Engine Compartment, Operations). The Life-Limited items section from the source becomes a table on this page showing each item, its interval/lifetime, and its current due date/hours.

**Part 2 — Annual servicing addendum**: A cross-reference list of servicing tasks that are typically completed at annual inspection time. List the task name, interval, and a link to the home section page. No procedures here — links only. This section exists so a maintainer doing an annual has one place to see what servicing is also due, without duplicating the content.

#### Research tasks

**Life-limited items:** For each item in the Life-Limited section of the source, check `docs/references/AC43_13/` for the applicable interval. Cite AC 43.13 if found. If not found in AC 43.13, flag with `@@TOM:` — do not invent or infer intervals.

**Specific `@@TOM:` flags to pre-place:**
- Spark plug gap spec (source says "gap to XXX")
- Propeller bolt torque value and reference document (source says "torque to XXX ft-lb per XXX")

#### Documents / Placards section

The source includes a Documents/Placards section (AC registration, W&B, logbooks, AD list, etc.). Include this as the first checklist section — it is a standard part of the annual condition inspection.

#### Template

Use the Type 2 Procedure page template. Add the `:::draft` status block immediately after the H1.
