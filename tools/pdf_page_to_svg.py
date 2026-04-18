#!/usr/bin/env python3
"""Extract a single PDF page as an editable SVG with real <text> elements.

Optionally strips content outside a page_y window (useful for isolating
diagrams from surrounding headers/body text).

Usage:
    python pdf_page_to_svg.py INPUT.pdf PAGENUM OUTPUT.svg [--keep Y_MIN Y_MAX]

PAGENUM is 1-based. Y_MIN/Y_MAX are page coordinates (0=top, 792=bottom
for US Letter). Text elements outside the window are removed; vector paths
are unaffected.

Requires: pymupdf (pip install pymupdf)

Example — extract Figure 2-1 from G3X Installation Manual p.25:
    python pdf_page_to_svg.py GarminG3XInstallationManual_az.pdf 25 output.svg --keep 200 730
"""
import argparse
import re
import sys

import fitz  # pymupdf

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('pdf')
ap.add_argument('page', type=int, help='1-based page number')
ap.add_argument('out')
ap.add_argument('--keep', nargs=2, type=float, metavar=('Y_MIN', 'Y_MAX'),
                help='Keep only text blocks where Y_MIN <= page_y <= Y_MAX')
args = ap.parse_args()

doc = fitz.open(args.pdf)
page = doc[args.page - 1]
page_h = page.rect.height
svg = page.get_svg_image(text_as_path=False)

if args.keep:
    y_min, y_max = args.keep

    def keep_block(m):
        # PyMuPDF text elements use transform matrix(1 0 0 -1 0 page_h),
        # so SVG y values are negative; convert back to page coordinates.
        ym = re.search(r'\by="(-?[\d.]+)"', m.group(0))
        if not ym:
            return m.group(0)
        page_y = page_h + float(ym.group(1))
        return m.group(0) if y_min <= page_y <= y_max else ''

    svg = re.sub(r'<text[^>]*>.*?</text>', keep_block, svg, flags=re.DOTALL)

with open(args.out, 'w') as f:
    f.write(svg)

print(f'wrote {args.out}', file=sys.stderr)
