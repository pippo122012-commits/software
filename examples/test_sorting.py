"""A quiz: order alone does not show that all observations were preserved."""

from collections import Counter

import pytest


@pytest.mark.parametrize("values", [[], [1], [2, 1], [1, 2, 1]])
def test_sorting(values):
    result = sorted(values)
    for index in range(1, len(result)):
        assert result[index - 1] <= result[index]
    assert Counter(result) == Counter(values)
