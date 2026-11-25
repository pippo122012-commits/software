"""Check a known result using only the Python standard library."""

import json
import math
import sys
from pathlib import Path

report = json.loads(Path(sys.argv[1]).read_text())
if report["n_total"] != 8 or report["n_valid"] != 4:
    raise SystemExit("wrong observation counts")
if not math.isclose(report["mean_ndvi"], 0.25, abs_tol=1e-12):
    raise SystemExit("wrong mean")
print("Installed artifact produced the expected result")
