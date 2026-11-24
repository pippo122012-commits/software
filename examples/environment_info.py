"""Print reproducibility evidence without treating local paths as portable."""

import hashlib
import json
import platform
import sys
from importlib.metadata import version
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    evidence = {
        "python": platform.python_version(),
        "executable": sys.executable,
        "in_virtual_environment": sys.prefix != sys.base_prefix,
        "packages": {
            name: version(name)
            for name in ("fieldcheck-workshop", "numpy", "pytest", "ruff")
        },
        "sha256": {
            name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in ("pyproject.toml", "uv.lock", "data/tiny.csv")
        },
    }
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()
