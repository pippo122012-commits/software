"""Build a browsable API reference and landing page using the standard library."""

import os
import pydoc
from pathlib import Path

root = Path(__file__).resolve().parents[1]
output = root / "api-docs"
output.mkdir(exist_ok=True)
os.chdir(output)
pydoc.writedoc("fieldcheck.core")
(output / "index.html").write_text(
    '<!doctype html><html lang="en"><meta charset="utf-8">'
    "<title>Fieldcheck documentation</title><h1>Fieldcheck</h1>"
    "<p>Small synthetic reflectance analysis for the workshop.</p>"
    '<p><a href="fieldcheck.core.html">Calculation API</a></p></html>',
    encoding="utf-8",
)
print("Open api-docs/index.html in a browser")
