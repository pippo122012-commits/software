"""Command-line boundary: parse, read, calculate, record provenance, report."""

import argparse
import hashlib
import json
import logging
import platform
from importlib.metadata import version
from pathlib import Path

import numpy as np

from fieldcheck.core import ndvi, summarize
from fieldcheck.io import read_csv

logger = logging.getLogger(__name__)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Summarize synthetic reflectance CSV")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    if args.input.resolve() == args.output.resolve():
        parser.error("input and output paths must differ")
    try:
        red, nir, quality = read_csv(args.input)
        values = ndvi(red, nir, quality)
        report = summarize(values)
        logger.info(
            "Valid: %d, Excluded: %d",
            report["n_valid"],
            report["n_total"] - report["n_valid"],
        )
        if report["n_valid"] == 0:
            raise ValueError("need at least 1 valid observations")
        report["input_sha256"] = hashlib.sha256(args.input.read_bytes()).hexdigest()
        report["versions"] = {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "fieldcheck": version("fieldcheck-workshop"),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    except (OSError, ValueError) as exc:
        logger.error("%s", exc)
        return 2
    logger.info(
        "Wrote %s (%s/%s valid)", args.output, report["n_valid"], report["n_total"]
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
