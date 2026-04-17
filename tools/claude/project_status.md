## Project Overview

**PDFindexer** is a Python program that reads the FAA AC 43.13-1B PDF ("Acceptable Methods, Techniques, and Practices - Aircraft Inspection and Repair"), extracts its content by paragraph, and writes a structured text index and paragraph-level text files. The output is consumed by a Claude instance assisting with the ea_mxmanual project.

## Project Status

This repository is in active design. Implementation has not yet started.

### Current Structure

- `pdfindexer/` - Main package (not yet created)
- `tests/` - Test suite (not yet created)
- `docs/plans/` - Design specifications and implementation plans
  - `design.md` - Full architecture and design decisions
  - `required_from_tom.md` - Items needed from Tom before work can proceed
  - `architect_todo.md` - Architect task tracking
  - `programmer_todo.md` - Programmer task tracking
- `docs/acronyms.md` - List of acronyms or terms relevant to this project
- `docs/references/` - Reference materials (READ ONLY)
  - `ac_43.13.pdf` - Source PDF (600+ pages, born-digital, two-column layout)

## Output

The program writes to `data/` within this repo:
- `index.txt` - Master index listing all chapters, sections, and paragraph titles with filenames
- `ch##_p###.txt` - One plain text file per paragraph

Tom copies the contents of `data/` to `../docs/references/FAA43_13/` in the ea_mxmanual
project after a successful run.

## Documentation Management

### Reference Materials
- All files in `docs/references/` are READ ONLY. NEVER modify these files.

## Environment Setup

A Python virtual environment will be configured at `venv/`:

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run specific test file
pytest tests/test_example.py

# Run tests with verbose output
pytest -v

# Run tests and show print statements
pytest -s
```