# ABOUTME: Writes paragraph text files and the master index for the AC 43.13-1B knowledge base.
# ABOUTME: Output is plain text optimised for token-efficient reading by a Claude instance.

import os


def write_output(paragraphs, toc, output_dir, appendices=None):
    """Write paragraph files, appendix files, and index.txt to output_dir.

    Args:
        paragraphs: list of paragraph dicts from parse_document()
        toc: chapter/section structure from parse_toc()
        output_dir: directory path to write files into (created if absent)
        appendices: optional list of dicts:
            [{"filename": "appendix_1_glossary.txt",
              "title": "Appendix 1: Glossary",
              "text": "<plain text content>"},
             ...]
    """
    os.makedirs(output_dir, exist_ok=True)

    # Build lookup: paragraph number → output filename
    filename_map = _build_filename_map(paragraphs)

    for para in paragraphs:
        _write_paragraph_file(para, filename_map[para["number"]], output_dir)

    for app in (appendices or []):
        _write_appendix_file(app, output_dir)

    _write_index(toc, filename_map, output_dir, appendices or [])


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _build_filename_map(paragraphs):
    """Map paragraph number → filename (e.g. '1-1' → 'ch01_p001.txt').

    Paragraph numbers are formatted as ch##_p###.txt where the paragraph
    sequence number within the chapter is zero-padded to 3 digits.
    """
    # Group paragraphs by chapter, tracking sequence within chapter
    by_chapter = {}
    for para in paragraphs:
        ch = para["chapter"]
        by_chapter.setdefault(ch, []).append(para["number"])

    filename_map = {}
    for ch, numbers in by_chapter.items():
        for seq, num in enumerate(numbers, start=1):
            # Extract the paragraph number within the chapter (e.g. "1-36" → 36)
            try:
                para_int = int(num.split("-")[1])
            except (IndexError, ValueError):
                para_int = seq
            filename_map[num] = f"ch{ch:02d}_p{para_int:03d}.txt"

    return filename_map


def _write_paragraph_file(para, filename, output_dir):
    """Write a single paragraph text file."""
    if para["section"] == 0:
        # Synthetic section (chapter with no section headers, e.g. Ch.13)
        header = (
            f"AC 43.13-1B  "
            f"Chapter {para['chapter']}: {para['chapter_title']}"
        )
    else:
        header = (
            f"AC 43.13-1B  "
            f"Chapter {para['chapter']}: {para['chapter_title']}  "
            f"Section {para['section']}: {para['section_title']}"
        )
    content = header + "\n\n" + para["text"] + "\n"
    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _write_appendix_file(app, output_dir):
    """Write a single appendix text file."""
    path = os.path.join(output_dir, app["filename"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(app["text"])


def _write_index(toc, filename_map, output_dir, appendices):
    """Write index.txt listing all chapters, sections, paragraphs, and appendices."""
    lines = ["AC 43.13-1B — Acceptable Methods, Techniques, and Practices", ""]

    for ch in toc:
        lines.append(f"CHAPTER {ch['number']}: {ch['title']}")
        lines.append("")
        for sec in ch["sections"]:
            if sec["number"] == 0:
                # Synthetic section (chapter with no section headers, e.g. Ch.13):
                # list paragraphs directly under chapter at 2-space indent
                for para in sec["paragraphs"]:
                    num = para["number"]
                    filename = filename_map.get(num, "")
                    if filename:
                        lines.append(f"  {num}  {para['title']} [{filename}]")
                    else:
                        lines.append(f"  {num}  {para['title']}")
                lines.append("")
            else:
                lines.append(f"  SECTION {sec['number']}: {sec['title']}")
                for para in sec["paragraphs"]:
                    num = para["number"]
                    filename = filename_map.get(num, "")
                    if filename:
                        lines.append(f"    {num}  {para['title']} [{filename}]")
                    else:
                        lines.append(f"    {num}  {para['title']}")
                lines.append("")
        lines.append("")

    if appendices:
        lines.append("APPENDICES")
        lines.append("")
        for app in appendices:
            lines.append(f"  {app['title']} [{app['filename']}]")
        lines.append("")

    path = os.path.join(output_dir, "index.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
