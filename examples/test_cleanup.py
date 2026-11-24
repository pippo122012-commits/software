"""Observe fixture setup and teardown with pytest -s."""

import pytest


@pytest.fixture
def opened_file(tmp_path):
    stream = (tmp_path / "sample.txt").open("w+")
    yield stream
    stream.close()
    assert stream.closed


def test_file(opened_file):
    opened_file.write("sample")
    assert not opened_file.closed
