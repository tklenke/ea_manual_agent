# ABOUTME: Pytest configuration — adds project root to sys.path so pdfindexer package is importable.
# ABOUTME: Also defines shared fixtures used across test modules.

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
