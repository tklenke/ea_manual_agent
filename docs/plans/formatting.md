# Formatting

This document defines formatting conventions for the ea_mxmanual maintenance manual. It covers page naming, callout formats, citations, and cross-references.

**Note to Writer:** This document will be published in the Otterwiki alongside Manual Standards and Writing Style.

---

## Page and Section Naming

- Page names use `lowercase-hyphenated` format (e.g., `brake-system-fluid-choice`)
- Wiki links use `[[Display Text|page-name]]` format
- Section headings: Title Case for top-level, sentence case for sub-sections
- Names must describe content, not document history or status
- NEVER use temporal or status terms in names (e.g., "new-procedure", "updated-checklist", "revised-spec")
- Names must be evergreen — valid regardless of when they are read
- NEVER use manufacturer names or model numbers in page slugs — use the functional/descriptive name instead. Model and manufacturer information belongs in the wiki link display text only.

**Examples:**
- `avionics-primary-flight-display` ✓ — not `avionics-gdu-460-pfd` ✗
- `avionics-backup-instrument` ✓ — not `avionics-g5-backup-instrument` ✗
- Link text retains the model: `[[Primary Flight Display (GDU 460)|avionics-primary-flight-display]]`

**Why:** Page slugs are permanent identifiers. A functional slug remains valid if a component is replaced with a different model; a model-based slug becomes wrong and requires page renames and link updates across the manual.

---

## Page Status Block

Every content page includes a status block immediately after the H1 heading. This gives the reader an immediate visual indication of whether the page has been reviewed.

**Placement:** After `# Page Title`, before the first `##` section.

**Three states:**

```markdown
::: draft
**DRAFT** — Not yet reviewed.
:::
```

```markdown
::: pending
**PENDING** — YYYY-MM-DD
:::
```

```markdown
::: approved
**APPROVED** — YYYY-MM-DD
:::
```

**Rules:**
- Writer adds `:::draft` when creating a page (included in all templates).
- Reviewer changes the block at sign-off: `:::approved` if all issues resolved, `:::pending` if flags consciously deferred by Tom. The date is the date of the review session.
- If feedback from `input/feedback/` resolves all pending flags, Writer upgrades `:::pending` to `:::approved` with today's date.
- `readme.md` and `home.md` are exempt — they are not content pages.

---

## NOTE Callouts

### General Note

Use a NOTE to call out important information that does not fit in the main flow of a procedure or description.

```
> **NOTE:** [Text of note here.]
```

**Example:**
> **NOTE:** Torque values apply to dry, unlubricated fasteners unless otherwise specified.

---

### Source Conflict Note

When a manufacturer Technical Data Sheet (TDS) conflicts with AC 43.13 and the TDS is followed, a source conflict NOTE is required.

```
> **NOTE:** This [procedure/specification/value] follows [TDS name] ([tds/filename]) rather
> than AC 43.13 ([ch##_p###]). Where these sources conflict, the manufacturer's Technical
> Data Sheet takes precedence. See both documents for full context.
```

**Fields:**
- `[procedure/specification/value]` — what specifically is affected (e.g., "cure time", "torque specification")
- `[TDS name]` — the common name of the TDS (e.g., "Permatex Thread Sealant TDS")
- `[tds/filename]` — the filename in `docs/references/tds/`
- `[ch##_p###]` — the AC 43.13 chapter and page reference (e.g., `ch01_p001`)

**Example:**
> **NOTE:** This cure time follows the Permatex Thread Sealant TDS (`Permatex_Thread_Sealant_TDS.pdf`) rather than AC 43.13 (ch01_p001). Where these sources conflict, the manufacturer's Technical Data Sheet takes precedence. See both documents for full context.

---

## Citing Sources

All specific values, procedures, and specifications MUST include an inline citation.

- AC 43.13: `(AC 43.13, ch01_p001)`
- TDS: `(Permatex_Thread_Sealant_TDS.pdf)`
- Multiple pages from the same source: `(AC 43.13, ch03_p024, ch03_p040)`

If a value cannot be traced to a source in `docs/references/`, flag it with `@@TOM:` rather than presenting it without attribution.

### Source citations for inspection criteria and general guidance

Where inspection criteria or general maintenance guidance derives from a source, cite it — even when there is no specific numeric value. This is a soft requirement: use judgment, but when you do cite, use the same inline format.

**When to cite:**
- Inspection criteria that specify what to look for and why (e.g., crazing, crack propagation)
- Guidance on repair vs. replacement decisions
- Safety restrictions (e.g., repairs not in pilot's line of vision)
- Any statement where "says who?" is a fair question

**When not required:**
- General descriptive statements with no safety or procedural implication
- Information provided directly by Tom (e.g., operator-specific dimensions, product preferences)

**Format is the same** — parenthetical inline at end of sentence or bullet: `(AC 43.13, ch03_p020)`

Prose form is acceptable when it reads naturally: `per the procedure in AC 43.13, ch03_p040`. Default to parenthetical.

---

## Table of Contents

OtterWiki automatically renders an "On this page" TOC in the sidebar for any page with headings. Do not place `[TOC]` in page content — it renders as literal text, not a table of contents.

---

## Cross-References

When content in one section refers to a procedure or topic covered in another section, use a wiki link rather than duplicating the content.

**Format:** `See [[Page Title|page-name]] in Section N.`

**Example:** `See [[Cowling|panels-cowling]] in Section 9 for removal procedure.`

Do not duplicate procedures. One section owns each procedure; all others point to it.
