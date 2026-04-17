# ABOUTME: Tests for the wiki_check.py CLI — argument parsing and output control.
# ABOUTME: Uses subprocess to exercise the real CLI entry point.

import subprocess
import sys
from pathlib import Path

WR_DIR = Path("/home/tom/projects/N657CZDashTwo")
SCRIPT = Path(__file__).parent.parent / "wiki_check.py"
VENV_PYTHON = Path(__file__).parent.parent / "venv" / "bin" / "python3"


def _run(*args):
    result = subprocess.run(
        [str(VENV_PYTHON), str(SCRIPT)] + list(args),
        capture_output=True, text=True
    )
    return result


def test_basic_output_contains_report_header():
    result = _run()
    assert "Wiki Integrity Report" in result.stdout
    assert result.returncode == 0


def test_basic_output_contains_total_pages():
    result = _run()
    assert "Total WR pages:" in result.stdout


def test_detail_flag_adds_broken_links_section():
    result = _run("--detail")
    assert "Broken links:" in result.stdout
    assert result.returncode == 0


def test_no_detail_flag_omits_detail_sections():
    result = _run()
    # Without --detail, the broken links list section header should not appear
    # (the summary line "Broken links: N" IS there, but not the detail block)
    lines = result.stdout.splitlines()
    # The summary line has a count; the detail block header has no count after it
    detail_headers = [l for l in lines if l.strip() == "Broken links:"]
    assert detail_headers == []


def test_detail_flag_includes_orphan_section():
    result = _run("--detail")
    assert "Orphan pages:" in result.stdout


def test_structural_pages_line_in_normal_output():
    result = _run()
    assert "Structural pages:" in result.stdout


def test_structural_pages_line_in_detail_output():
    result = _run("--detail")
    assert "Structural pages (excluded from orphans):" in result.stdout
