# ABOUTME: Formats the wikiCheck summary report for stdout output.
# ABOUTME: Produces exact plain-text layout matching the design spec.

from wikicheck.stats import Stats


def format_report(stats: Stats, today: str, log_last_updated: str) -> str:
    slug_list = ", ".join(stats.structural_pages_found)
    structural_line = (
        f"Structural pages:        {len(stats.structural_pages_found):>2}"
        f"  ({slug_list} — excluded from orphans)"
    )
    lines = [
        f"Wiki Integrity Report — {today}",
        f"Total WR pages:          {stats.total_pages}",
        f"Broken links:            {stats.broken_link_count}  (pages referenced but not yet written)",
        f"System links:            {stats.system_link_count:>2}  (Otterwiki system calls, not checked)",
        f"Orphan pages:            {stats.orphan_count:>2}  (exist in WR, never linked to)",
        structural_line,
        f"Approved pages:          {stats.approved_count}  (of {stats.total_pages} in log)",
        f"Pending pages:           {stats.pending_count:>2}  (reviewed, awaiting resolution)",
        f"Unreviewed pages:        {stats.unreviewed_count:>2}  (in log, never reviewed)",
        f"Pages missing from log:  {stats.missing_from_log_count:>2}  (in WR, not in log)",
        f"Review log last updated: {log_last_updated} ({stats.log_age_days} days ago)",
    ]
    for slug in stats.structural_pages_missing:
        lines.append(f"ERROR: Structural page not in WR: {slug}")
    return "\n".join(lines)


def format_detail(
    broken_links: list,
    pending: list,
    unreviewed: list,
    missing_from_log: list,
    orphan_pages: list,
    structural_pages_found: list,
    structural_pages_missing: list,
    system_links: list,
) -> str:
    def section(title, items):
        lines = [title]
        if items:
            lines.extend(f"  {item}" for item in sorted(items))
        else:
            lines.append("  (none)")
        return "\n".join(lines)

    structural_lines = ["Structural pages (excluded from orphans):"]
    if structural_pages_found:
        structural_lines.extend(f"  {s}" for s in sorted(structural_pages_found))
    else:
        structural_lines.append("  (none)")
    for slug in structural_pages_missing:
        structural_lines.append(f"  ERROR: not in WR: {slug}")
    structural_section = "\n".join(structural_lines)

    parts = [
        section("Broken links:", broken_links),
        section("System links (not checked):", system_links),
        section("Orphan pages:", orphan_pages),
        structural_section,
        section("Pending pages:", pending),
        section("Unreviewed pages:", unreviewed),
        section("Pages missing from log:", missing_from_log),
    ]
    return "\n\n".join(parts)


def format_missing_log_report(
    total_pages: int,
    broken_link_count: int,
    system_link_count: int,
    system_links: list[str],
    structural_pages_found: list[str],
    structural_pages_missing: list[str],
    today: str,
    seed_path: str,
) -> str:
    slug_list = ", ".join(structural_pages_found)
    structural_line = (
        f"Structural pages:        {len(structural_pages_found):>2}"
        f"  ({slug_list} — excluded from orphans)"
    )
    lines = [
        f"Wiki Integrity Report — {today}",
        f"Total WR pages:          {total_pages}",
        f"Broken links:            {broken_link_count}  (pages referenced but not yet written)",
        f"System links:            {system_link_count:>2}  (Otterwiki system calls, not checked)",
        structural_line,
    ]
    for slug in structural_pages_missing:
        lines.append(f"ERROR: Structural page not in WR: {slug}")
    lines.extend([
        f"Review log:              NOT FOUND — seeded template written to",
        f"                         {seed_path}",
        f"                         move to: docs/notes/review_log.md",
    ])
    return "\n".join(lines)
