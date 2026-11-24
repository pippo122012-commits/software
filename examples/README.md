# Worked demonstrations

Run commands from the project root, beside `pyproject.toml`.

- `uv run --locked python examples/environment_info.py`: record interpreter and
  package versions plus metadata, lockfile, and input checksums for Lab 2.
- `uv run python examples/inspect_rows.py`: display each current NDVI and the
  summary. Compare row IDs against the independent table in `data/README.md`;
  the extracted baseline disagrees, and the repaired project should agree after Lab 5.
- `uv run python examples/count.py`: the extracted baseline reports the deliberately wrong
  count 1; after Lab 4, count 2 and mean 0.25.
- `uv run pytest examples/test_tdd_demo.py -q`: intentionally fails initially.
  The slides show a formula, a new excluded-row test, and then a quality guard.
  This is separate from the real `src/fieldcheck/core.py` lab implementation.
- `uv run pytest examples/test_report_demo.py -q`: fails on the extracted baseline;
  passes after the day-one repairs. Lab 7 copies it into `tests/test_report.py`.

Normal `uv run pytest -q` only discovers `tests/`, so these staged demonstrations
cannot accidentally make the ordinary suite red. `ruff` still checks their code.

Additional demonstrations (not extra required labs):

- `uv run python examples/logging_demo.py`: INFO and WARNING in `analysis.log`;
  change INFO to DEBUG to see all three messages. The file appends by default.
- `uv run pytest examples/test_cleanup.py examples/test_mock.py -q`: two passes.
- `uv run pytest examples/test_sorting.py -q`: four passes. Try `sorted(set(values))`
  in a disposable copy; the duplicate case must fail.
- `docstring.txt`: NumPy-style replacement for the scalar function's docstring.

`compare_baseline.py` is for Lab 2 only. It runs the archived ad hoc script in a
temporary directory and compares its summary with the package. It passes for
the package checkpoint and deliberately fails after the numerical repairs.
Do not include it in the normal test suite or CI.
