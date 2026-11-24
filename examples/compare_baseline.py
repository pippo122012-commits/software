"""Lab 2 only: check that extraction preserves the original tiny-data summary.

This is a characterization check, not evidence of scientific correctness.
It is expected to fail once Labs 4-5 intentionally repair the calculation.
"""

import json
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from fieldcheck import ndvi, summarize
from fieldcheck.io import read_csv

root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix="fieldcheck-baseline-") as directory:
    temporary = Path(directory)
    shutil.copytree(root / "data", temporary / "data")
    subprocess.run(
        [sys.executable, str(root / "archive/analysis.py")],
        cwd=temporary,
        check=True,
        capture_output=True,
        text=True,
    )
    baseline = json.loads((temporary / "report.json").read_text())
actual = summarize(ndvi(*read_csv(root / "data/tiny.csv")))
assert actual["n_total"] == baseline["n_total"], (actual, baseline)
assert actual["n_valid"] == baseline["n_valid"], (actual, baseline)
assert math.isclose(actual["mean_ndvi"], baseline["mean_ndvi"], abs_tol=1e-12)
print("Original tiny-data behavior preserved: total=8 valid=5 mean=0.183333")
print("This preserves known defects. It does not establish a correct analysis.")
