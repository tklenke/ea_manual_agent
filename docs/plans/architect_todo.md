# Architect Todo

## In Progress

## Backlog

### [ ] Add page naming standard: no manufacturer names or model numbers in slugs

Page slugs must use functional/descriptive names. Manufacturer names and model numbers belong in the link display text only, not in the slug.

**Examples from Section 17 cleanup (2026-04-18):**
- `avionics-g3x-system` → `avionics-system-overview` ✓
- `avionics-g5-backup-instrument` → `avionics-backup-instrument` ✓
- `avionics-gdu-460-pfd` → `avionics-primary-flight-display` ✓
- Display text retains the model: `[[Primary Flight Display (GDU 460)|avionics-primary-flight-display]]`

**Why:** Slugs are permanent identifiers. If a component is replaced with a different model, a slug like `avionics-gdu-460-pfd` becomes wrong and requires page renames and link updates. A functional slug like `avionics-primary-flight-display` remains valid regardless of which model is installed.

Document this standard in `docs/plans/formatting.md` under Page and Section Naming, and re-publish `manual-standards-formatting` in the WR.

### [ ] Add GAD 29 to Section 17 TOC and create component page plan

GAD 29 (ARINC 429 data concentrator) is confirmed installed and required for the G3X system. It is listed on `avionics-system-overview` linking to `avionics-arinc-429-adapter`. It has been added to `toc_structure.md`. Create a Writer task for the component page.
