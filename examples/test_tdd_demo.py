"""Intentionally red first step of the TDD demonstration.

Run explicitly; examples/ is outside the ordinary tests/ discovery directory.
"""

import pytest


def ndvi_value(red, nir, quality):
    return 0.0  # Deliberately unfinished: complete this in the demonstration.


def test_clear():
    assert ndvi_value(0.2, 0.6, 0) == pytest.approx(0.5)
