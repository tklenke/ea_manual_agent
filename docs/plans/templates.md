# Page Templates

This document defines standard page structures for each type of page in the ea_mxmanual maintenance manual.

**Note to Writer:** Use the appropriate template as a starting point for each new page. Sections marked *[delete if not applicable]* may be removed at Writer's discretion when the section adds no value for that specific page. Do not delete sections just because they are short — a brief Troubleshooting section is better than none if the content is useful.

**Subsection links:** OtterWiki supports links to specific sections within a page using the format `[[Display Text|page-name#section-heading]]`. Use this for cross-references that point to a specific section rather than a whole page.

---

## Procedure Placement Rule

**Short procedures** (no special tools, no safety notes, five steps or fewer) may be written inline on a Component page rather than as a separate Procedure page.

**Complex procedures** (requires tools, has safety notes, or exceeds five steps) must have their own dedicated Type 2 Procedure page. The Component page includes a cross-reference link to it.

> **NOTE:** This is a working rule. If component pages become cluttered with inline procedures, the threshold should be lowered and all procedures moved to their own pages. OtterWiki subsection links mitigate this risk — a cross-reference can point directly to a section within a page, not just the page top.

---

## Type 1a: System Page

Use for pages that describe a system — a functional collection of components working together (e.g., Fuel System overview, Bus Architecture, Autopilot).

```markdown
# [System Name]

::: draft
**DRAFT** — Not yet reviewed.
:::

## Description
What this system does and its role on the aircraft.

## System Components
List of components that make up this system, each linking to its
Component page.

- [[Component Name|component-page-name]] — brief role description
- [[Component Name|component-page-name]] — brief role description

## Operation
How the system works. Focus on what a maintainer needs to understand
to inspect and maintain it — not an engineering deep-dive.

## Inspection
System-level checks: what to verify at the system level, beyond what
is covered on individual component pages.

## Troubleshooting
*[delete if not applicable]*
System-level symptoms and where to look. Cross-reference component
pages or procedure pages rather than duplicating their content.
```

---

## Type 1b: Component Page

Use for pages that describe a specific physical component (e.g., GTR 20 VHF Communication, Batteries, Brake System).

The Component page is a **reference** for the component. Step-by-step procedures belong on Type 2 Procedure pages and are linked from the Procedures section below.

```markdown
# [Component Name]

::: draft
**DRAFT** — Not yet reviewed.
:::

## Description
What it is, what it does, and where it is located on the aircraft.
Include model/part number if known.

## Specifications
*[delete if not applicable]*
Key specifications: model, ratings, capacity, part numbers, or other
reference data a maintainer would need.

## Inspection
What to check, how to check it, and what constitutes a pass or fail.
Include inspection interval if different from the annual condition inspection.

## Procedures
Links to procedure pages for this component. Short procedures (no special
tools, no safety notes, five steps or fewer) may be written inline here
instead of on a separate page.

- **Removal and Installation:** See [[Procedure Name|procedure-page]]
- **[Specific Maintenance Task]:** See [[Procedure Name|procedure-page]]
- **Troubleshooting:** See [[Procedure Name|procedure-page]]

*[If all procedures for this component are simple enough to be inline,
replace the links above with the inline procedures and delete this note.]*
```

---

## Type 2: Procedure Page

Use for step-by-step procedures that are too complex for inline treatment on a Component page, or that are referenced from multiple places (e.g., Wing Removal and Installation, Weighing Procedures, Annual Condition Inspection).

```markdown
# [Procedure Name]

::: draft
**DRAFT** — Not yet reviewed.
:::

## Overview
What this procedure accomplishes and when it should be performed.

## Tools and Materials Required
*[delete if not applicable]*
List of tools, equipment, and consumables needed before starting.

## Safety Notes
Hazards specific to this procedure. Cross-reference Section 2 (Safety
Precautions) for general hazards.

## Prerequisites
Conditions that must be met before starting (e.g., aircraft in specific
configuration, other systems de-energized, prior procedures completed).

## Procedure
Numbered steps. Each step is a single action in imperative mood.

1. Step one.
2. Step two.
3. ...

## Post-Procedure Checks
Verification steps to confirm the procedure was completed correctly and
the aircraft or system is in the expected state.
```

---

## Type 3: Index or Pointer Page

Use for master-list pages that consolidate pointers to procedures elsewhere
(e.g., Servicing, Lubrication).

Each entry follows this format — place the status block at the top of the page, after the H1, before the first entry:

```markdown
# [Index Page Title]

::: draft
**DRAFT** — Not yet reviewed.
:::

## [Task Name]

**Interval:** [interval description]
**Procedure:** See [[Page Title|page-name]] in Section N.
```

No procedures are duplicated on index pages. If a task has no dedicated
procedure page, the interval and brief description may be included inline,
but a home section should be identified for future expansion.

---

## Type 4: Reference or Administrative Page

Use for pages that are informational rather than procedural (e.g., Manual
Standards, Record of Revisions, Systems Overview).

No standard template — structure to suit the content. Apply writing style
and formatting standards from `style.md` and `formatting.md`.
