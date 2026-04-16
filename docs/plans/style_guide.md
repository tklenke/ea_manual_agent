# Style Guide

This document defines writing and formatting standards for the ea_mxmanual maintenance manual. It is the authoritative reference for how content is written, formatted, and cited.

**Note to Writer:** This document will be published in the Otterwiki. When that migration occurs, update `claude/content_development_overview.md` to reference the Otterwiki location.

---

## Page and Section Naming

- Page names use `lowercase-hyphenated` format (e.g., `brake-system-fluid-choice`)
- Wiki links use `[[page-name|Display Text]]` format
- Section headings: Title Case for top-level, sentence case for sub-sections
- Names must describe content, not document history or status
- NEVER use temporal or status terms in names (e.g., "new-procedure", "updated-checklist", "revised-spec")
- Names must be evergreen — valid regardless of when they are read

---

## Writing Style

- Write in present tense. Content must be evergreen — valid regardless of when it is read.
- NEVER reference the document's own history ("this section was updated to...", "previously...", "as of this revision...")
- NEVER use marketing or evaluative language ("improved", "better", "enhanced")
- Use active voice and imperative mood for procedures (e.g., "Torque the bolt to 25 in-lbs" not "The bolt should be torqued...")
- Define acronyms on first use in each page. Add new terms to `docs/acronyms.md`.
- Be specific. Vague guidance is dangerous in a maintenance manual. If a specific value is unknown, say so explicitly and flag it for research rather than writing around it.

---

## NOTE Format

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
- `[procedure/specification/value]` — what specifically is affected (e.g., "cure time", "application procedure", "torque specification")
- `[TDS name]` — the common name of the TDS (e.g., "Permatex Thread Sealant TDS")
- `[tds/filename]` — the filename in `docs/references/tds/` (e.g., `Permatex_Thread_Sealant_TDS.pdf`)
- `[ch##_p###]` — the AC 43.13 chapter and page reference (e.g., `ch01_p001`)

**Example:**
> **NOTE:** This cure time follows the Permatex Thread Sealant TDS (`Permatex_Thread_Sealant_TDS.pdf`) rather than AC 43.13 (ch01_p001). Where these sources conflict, the manufacturer's Technical Data Sheet takes precedence. See both documents for full context.

---

## Citing Sources

All specific values, procedures, and specifications MUST include a citation. Use these formats inline:

- AC 43.13: `(AC 43.13, ch01_p001)`
- TDS: `(Permatex Thread Sealant TDS)`

If a value cannot be traced to a source in `docs/references/`, flag it with `@@TOM:` rather than presenting it without attribution.

---

## Cross-References

When content in one section refers to a procedure or topic covered in another section, use a wiki link rather than duplicating the content.

**Format:** `See [[page-name|Page Title]] in Section N.`

**Example:** `See [[panels-cowling|Cowling]] in Section 9 for removal procedure.`

Do not duplicate procedures. One section owns each procedure; all others point to it.
