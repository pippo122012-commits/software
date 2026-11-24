import pytest

from fieldcheck import ndvi_value


def test_positive_clear_observation():
    assert ndvi_value(0.2, 0.6, 0) == pytest.approx(0.5)
