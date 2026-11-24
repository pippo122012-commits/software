"""Minimal input for the guided summary-count debugging demonstration."""

from fieldcheck.core import summarize

print(summarize([0.0, 0.5, float("nan")]))
