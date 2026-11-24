"""Integration example: expected to pass after the day-one repairs.

Run from the project folder: uv run pytest examples/test_report_demo.py -q.
"""

import json

import pytest

from fieldcheck.cli import main


def test_report(tmp_path):
    output = tmp_path / "report.json"
    assert main(["data/tiny.csv", "--output", str(output)]) == 0
    report = json.loads(output.read_text())
    assert report["n_valid"] == 4
    assert report["mean_ndvi"] == pytest.approx(0.25)
    assert len(report["input_sha256"]) == 64
