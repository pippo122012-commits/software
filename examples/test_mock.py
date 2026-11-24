"""Mock an unavailable input boundary, not the scientific calculation."""

from unittest.mock import MagicMock

from fieldcheck import cli


def test_read_failure(monkeypatch, tmp_path):
    read = MagicMock(side_effect=OSError("unavailable"))
    monkeypatch.setattr(cli, "read_csv", read)
    output = tmp_path / "out.json"
    args = ["input.csv", "--output", str(output)]
    assert cli.main(args) == 2
    read.assert_called_once()
    assert not output.exists()
