# Architect Todo

## In Progress

## Backlog

### [ ] Audit and revise toc_structure.md

The current TOC has significant problems identified on 2026-04-15. Do not begin writing content until this is resolved.

**Problems to address:**

1. **Section 16 (Avionics) is generic commercial-aircraft boilerplate.** The following items almost certainly don't exist on the Cozy Mark IV and should be removed or verified:
   - HF Communication
   - Instrument Landing System (ILS)
   - Fly-by-Wire Technology
   - Terrain Awareness and Warning Systems (TAWS)
   - Ground Proximity Warning Systems (GPWS)
   - Traffic Alert and Collision Avoidance System (TCAS)

2. **Section 14 (Electrical) is also suspiciously generic.** Needs to be audited against what is actually installed on the aircraft.

3. **Wildly inconsistent depth.** Sections 14 and 16 have elaborate sub-page trees; Sections 2, 6, 15, 17, 18 are completely empty. Section 6 (Inspection) should be one of the most developed sections for a maintenance manual — it is currently a skeleton.

4. **Duplicate section number.** Two entries labeled 7.2 in Section 7 (Structures).

5. **Section 1 meta-content.** "Instructions for development of Design and Troubleshooting Documentation" is a guidance doc for Claude/Tom, not content for a maintainer. Remove from the manual TOC.

6. **Missing weight and balance section.** Standard and important for a maintenance manual.

7. **Scope question to resolve with Tom.** Pages like `flight-controls-fabrication-notes` and `flipping-fuselage` — are we writing a maintenance manual, a build manual, or both? This needs an explicit decision before content is written.

**Plan to resolve:**
- Interview Tom: get an inventory of what avionics and electrical systems are actually installed on the aircraft
- Audit Sections 14 and 16 against that inventory — remove or stub pages for systems not present
- Fill in empty section skeletons (especially Section 6 Inspection)
- Fix duplicate 7.2
- Remove meta-content from Section 1
- Add weight and balance section
- Get explicit scope decision from Tom on fabrication content

## Completed
