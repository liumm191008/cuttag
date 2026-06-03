#!/usr/bin/env python3
"""Compatibility entry point for generating the CUT&Tag HTML report.

This wrapper keeps the report implementation in ``scripts/generate_cuttag_report.py``
while providing a short top-level command requested by users::

    python3 report2.py --input-json input.json --results-dir results --report-dir report
"""

from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from generate_cuttag_report import main  # noqa: E402


if __name__ == "__main__":
    main()
