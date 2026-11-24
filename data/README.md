# Synthetic observations

These hand-authored rows are teaching data, not satellite observations.
`red` and `nir` are already-scaled dimensionless reflectances. The workshop's
[0,1] and binary quality rules are an explicit simplification, not a universal
satellite-product specification. Real products need their own scaling, masks,
spatial alignment, and scientific validation.

For `tiny.csv`, valid NDVIs are `[0.5, -0.5, 0, 1]`; the other four rows are
invalid. Expected counts: total 8, valid 4. Expected mean: 0.25. Compare floating
point values with a tolerance; no random inputs or network downloads are needed.

## Work out the answer before running the code

For each row, apply the quality, finite-value, range, and positive-denominator
rules before calculating `(nir - red) / (nir + red)`.

| Row | Red | NIR | Quality | Expected NDVI | Reason |
| --- | --- | --- | --- | --- | --- |
| `a` | `0.2` | `0.6` | `0` | `0.5` | Clear, finite bands within range. |
| `b` | `0.6` | `0.2` | `0` | `-0.5` | A negative result remains a valid measurement. |
| `c` | `0.3` | `0.3` | `0` | `0.0` | Equal nonzero bands; zero must count as valid. |
| `d` | `0.0` | `0.8` | `0` | `1.0` | One zero band is allowed; the sum is positive. |
| `e` | `0.0` | `0.0` | `0` | `NaN` | Both bands zero: the denominator would be zero. |
| `f` | `NaN` | `0.4` | `0` | `NaN` | A band is missing. |
| `g` | `0.2` | `0.8` | `1` | `NaN` | The quality flag excludes an otherwise finite result. |
| `h` | `1.2` | `0.4` | `0` | `NaN` | Red exceeds the workshop's allowed range. |

The four retained values sum to `1.0`; dividing by `4` gives `0.25`.
These hand-computed expectations are the independent reference for the tests.

Run `uv run python examples/inspect_rows.py` from the project root to display
what your current implementation actually computes. Compare row IDs with the
table, including excluded rows. The helper calls your code; its output is an
observation, not proof of correctness. The starter will disagree on rows `g`
and `h` and on the valid count. After Labs 4 and 5 all rows should agree.

## Connect the exercise to your EO work

Before using these checks on a real product, identify its band mapping, scale
and offset, nodata values, quality-mask definition, and spatial/temporal
alignment. Write down which observations the statistic should include. The
binary flag and `[0,1]` rule above are choices for this exercise, not product
metadata. An eight-row test does not establish the scientific suitability of
a real dataset or processing chain.

The [USGS NDVI reference](https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index)
documents the ratio and shows that band mappings and stored index values depend
on the product. Use the documentation for your actual product when transferring
the workflow.
