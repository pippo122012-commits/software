"""Show the current calculation; compare it with the hand-worked data/README.md."""

import csv
import math
from pathlib import Path

from fieldcheck.core import ndvi_value, summarize


def main():
    print("Current implementation: compare each row with data/README.md")
    values = []
    with Path("data/tiny.csv").open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            value = ndvi_value(
                float(row["red"]), float(row["nir"]), int(row["quality"])
            )
            values.append(value)
            displayed = f"{value:.6f}" if math.isfinite(value) else "NaN (excluded)"
            print(f"{row['id']}: {displayed}")
    report = summarize(values)
    mean = report["mean_ndvi"]
    displayed_mean = "None" if mean is None else f"{mean:.6f}"
    print(f"total={report['n_total']} valid={report['n_valid']} mean={displayed_mean}")


if __name__ == "__main__":
    main()
