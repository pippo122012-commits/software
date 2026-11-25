import math

import pytest

from fieldcheck import ndvi_value


def test_positive():
    assert ndvi_value(0.2, 0.6, 0) == pytest.approx(0.5)


def test_negative():
    assert ndvi_value(0.6, 0.2, 0) == pytest.approx(-0.5)


def test_zero():
    assert ndvi_value(0.3, 0.3, 0) == pytest.approx(0.0)


def test_one_zero_band():
    assert ndvi_value(0.0, 0.8, 0) == pytest.approx(1.0)


def test_zero_sum():
    assert math.isnan(ndvi_value(0.0, 0.0, 0))


def test_nonfinite_band():
    assert math.isnan(ndvi_value(float("nan"), 0.4, 0))


def test_quality_excluded():
    assert math.isnan(ndvi_value(0.2, 0.8, 1))


def test_out_of_range():
    assert math.isnan(ndvi_value(1.2, 0.4, 0))


def test_unknown_quality():
    with pytest.raises(ValueError):
        ndvi_value(0.2, 0.6, 99)
