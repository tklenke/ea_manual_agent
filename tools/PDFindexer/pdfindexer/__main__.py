# ABOUTME: Main entry point for PDFindexer — orchestrates TOC parsing, content extraction, and output.
# ABOUTME: Run as: python -m pdfindexer <pdf_path> <output_dir> [--toc-end <page>]

import argparse
import sys
import pdfplumber
from pdfindexer.toc_parser import parse_toc
from pdfindexer.doc_parser import parse_document
from pdfindexer.appendix_extractor import extract_appendix
from pdfindexer.output_writer import write_output


def main():
    parser = argparse.ArgumentParser(
        description="Extract AC 43.13-1B PDF into paragraph text files and index."
    )
    parser.add_argument("pdf_path", help="Path to ac_43.13.pdf")
    parser.add_argument("output_dir", help="Directory to write output files")
    parser.add_argument(
        "--toc-end",
        type=int,
        default=34,
        metavar="PAGE",
        help="Last 1-indexed page number of the TOC (default: 34)",
    )
    args = parser.parse_args()

    print(f"Opening {args.pdf_path} ...")
    with pdfplumber.open(args.pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"  {total_pages} pages total")

        # Phase 1: parse TOC (pages are 0-indexed internally)
        toc_pages = pdf.pages[1 : args.toc_end]  # PDF pages 2..toc_end (0-indexed: 1..toc_end-1)
        print(f"Parsing TOC (PDF pages 2–{args.toc_end}) ...")
        toc = parse_toc(toc_pages)
        chapter_count = len(toc)
        para_count = sum(
            len(sec["paragraphs"])
            for ch in toc
            for sec in ch["sections"]
        )
        print(f"  Found {chapter_count} chapters, {para_count} paragraphs in TOC")

        # Phase 2: extract content (pages after TOC, 0-indexed start = toc_end)
        print(f"Extracting content (PDF pages {args.toc_end + 1}–632) ...")
        paragraphs = parse_document(pdf, toc, content_start_page=args.toc_end)
        print(f"  Extracted {len(paragraphs)} paragraphs")

        # Phase 3: extract appendices
        APPENDIX_DEFS = [
            (633, 641, "Appendix 1: Glossary",                      "appendix_1_glossary.txt"),
            (642, 645, "Appendix 2: Acronyms and Abbreviations",     "appendix_2_acronyms.txt"),
            (646, 646, "Appendix 3: Metric-Based Prefixes and Powers of 10", "appendix_3_metric.txt"),
        ]
        print("Extracting appendices ...")
        appendices = []
        for start, end, title, filename in APPENDIX_DEFS:
            text = extract_appendix(pdf, start, end, title)
            appendices.append({"filename": filename, "title": title, "text": text})
            print(f"  {filename} ({end - start + 1} page(s))")

    # Phase 4: write output
    print(f"Writing output to {args.output_dir} ...")
    write_output(paragraphs, toc, args.output_dir, appendices)
    file_count = len(paragraphs) + len(appendices) + 1  # +1 for index.txt
    print(f"  Wrote {file_count} files ({len(paragraphs)} paragraphs + {len(appendices)} appendices + index.txt)")
    print("Done.")


if __name__ == "__main__":
    main()
