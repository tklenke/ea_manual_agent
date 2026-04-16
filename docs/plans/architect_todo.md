# Architect Todo

## In Progress

## Backlog

### [ ] PREREQUISITE: Set up OtterWiki instance on local machine

**Must be done before any Writer tasks can proceed.**

Install and configure a local OtterWiki instance pointed at the `ea_mxmanual` git repository. Writer cannot test the print footer, validate page rendering, or verify link formats without a running instance.

**Steps:**
1. Install OtterWiki (pip or clone from repo)
2. Configure it to use `ea_mxmanual` as its git repository root
3. Start the server and verify pages render
4. Confirm `[[wiki-link]]` format resolves correctly
5. Confirm `[TOC]` tag renders in-page table of contents
6. Confirm Markdown code blocks, blockquotes, and NOTE callout format render as expected

Once running, hand off to Writer for print footer configuration.

---

### [ ] Configure OtterWiki print footer for version tracing

Set up `customBody.html` and `custom.css` to inject a print-only footer showing last-edited timestamp and short git commit hash. Target format: `Last edited: YYYY-MM-DD HH:MM (short-hash)`. Test whether `page.updated` is available in the Jinja2 context for the installed OtterWiki version; if not, use JavaScript against the history endpoint. See architecture_decisions.md for full rationale.

### [ ] OtterWiki navigation sidebar strategy — DECISION TBD (initial: Option C)

Decide how to maintain the OtterWiki navigation sidebar as content is developed. Three options evaluated 2026-04-16:

- **Option A: Hand-maintained `_sidebar.md`** — Writer updates sidebar with each new page commit. Reviewer verifies. Clean hierarchy, manual maintenance burden.
- **Option B: Derived from `toc_structure.md`** — `toc_structure.md` is already in OtterWiki wiki syntax; use it as the source of truth. Less duplication, requires a generation step or direct use as sidebar.
- **Option C: OtterWiki built-in auto-generated index** — Rely on OtterWiki's native page index. No maintenance required, less control over organization.

**Initial decision: Option C.** Let OtterWiki auto-generate navigation. Revisit if organization or findability becomes a problem.

**FINAL DECISION: TBD** — confirm after content development begins and the auto-generated index can be evaluated in practice.

### [ ] Migrate architecture_decisions.md to Otterwiki as Manual Standards page

After TOC audit is complete, create a Writer task to migrate `docs/plans/architecture_decisions.md` into the Otterwiki as the Manual Standards page under Section 1 (General Information). Update `claude/content_development_overview.md` to reference the Otterwiki location instead of the plans file.

### [x] Audit and revise toc_structure.md

Completed 2026-04-16. Full restructure: 18 sections, all pages defined, all content decisions documented in architecture_decisions.md.

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
