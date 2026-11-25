import json
from pathlib import Path

from fieldcheck.cli import main


def test_json_report(tmp_path):
    data = Path(__file__).parent.parent / "data" / "tiny.csv"
    output = tmp_path / "report.json"

    status = main([str(data), "--output", str(output)])

    assert status == 0
    result = json.loads(output.read_text())
    assert result["n_total"] == 8
    assert result["n_valid"] == 4
    assert result["mean_ndvi"] == 0.25


def test_rejected_input(tmp_path):
    bad = tmp_path / "bad.csv"
    bad.write_text("red,nir,quality\n0.3,0.5,1\n")
    output = tmp_path / "report.json"

    status = main([str(bad), "--output", str(output)])

    assert status == 2
    assert not output.exists()
