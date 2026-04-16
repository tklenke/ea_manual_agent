# Page Templates

This document defines standard page structures for each type of page in the ea_mxmanual maintenance manual.

**Note to Writer:** Use the appropriate template as a starting point for each new page. Sections marked *[delete if not applicable]* may be removed at Writer's discretion when the section adds no value for that specific page. Do not delete sections just because they are short — a brief Troubleshooting section is better than none if the content is useful.

---

## Type 1: Component or System Page

Use for pages covering a specific component or system (e.g., Brake System, GTR 20 VHF Communication, Batteries).

```markdown
# [Component or System Name]

## Description
What it is, what it does, and where it is located on the aircraft.

## Specifications
*[delete if not applicable]*
Key specifications: model number, ratings, capacity, part numbers, or other
reference data a maintainer would need.

## Inspection
What to check, how to check it, and what constitutes a pass or fail.
Include inspection interval if different from the annual condition inspection.

## Maintenance
Routine maintenance tasks and procedures specific to this component.
For procedures shared with other sections, provide a cross-reference rather
than duplicating steps.

## Removal and Installation
*[delete if not applicable]*
Step-by-step procedure for removing and reinstalling the component.
Include torque values, orientation notes, and any special tools required.

## Troubleshooting
*[delete if not applicable]*
Common failure modes, symptoms, and corrective actions.
```

---

## Type 2: Procedure Page

Use for pages that are primarily step-by-step procedures (e.g., Wing Removal and Installation, Weighing Procedures, Annual Condition Inspection).

```markdown
# [Procedure Name]

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

Each entry follows this format:

```markdown
## [Task Name]

**Interval:** [interval description]
**Procedure:** See [[page-name|Page Title]] in Section N.
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
