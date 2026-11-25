"""Run the same checks locally, in GitHub Actions, or in GitLab CI."""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deliver", action="store_true", help="also verify an installed wheel"
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    uv = shutil.which("uv")
    if uv is None:
        parser.error("uv must be installed and available on PATH")
    python = f"{sys.version_info.major}.{sys.version_info.minor}"
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)

    def run(*command, cwd=root):
        print("+ " + " ".join(map(str, command)), flush=True)
        subprocess.run(command, cwd=cwd, env=env, check=True)

    def project(*command):
        run(uv, "run", "--locked", "--python", python, *command)

    try:
        project("ruff", "check", ".")
        project("ruff", "format", "--check", ".")
        project(
            "pytest",
            "--cov=fieldcheck",
            "--cov-report=term-missing",
            "--cov-report=xml:reports/coverage.xml",
            "--junitxml=reports/tests.xml",
        )
        project("python", "scripts/build_docs.py")
        run(uv, "build", "--python", python)
        if args.deliver:
            wheel = root / "dist/fieldcheck_workshop-0.1.0-py3-none-any.whl"
            # The file name is fixed for this workshop. Change it with the project version.
            with tempfile.TemporaryDirectory(
                prefix="fieldcheck-installed-"
            ) as directory:
                temporary = Path(directory)
                source = temporary / "tiny.csv"
                shutil.copy2(root / "data/tiny.csv", source)
                report = temporary / "wheel.json"
                # Outside the source tree: only the installed distribution is importable.
                run(
                    uv,
                    "run",
                    "--isolated",
                    "--no-project",
                    "--python",
                    python,
                    "--with",
                    str(wheel),
                    "fieldcheck",
                    str(source),
                    "--output",
                    str(report),
                    cwd=temporary,
                )
                run(
                    sys.executable,
                    str(root / "scripts/check_report.py"),
                    str(report),
                    cwd=temporary,
                )
                shutil.copy2(report, root / "reports/wheel.json")
        print("CHECKS PASSED" + ("; installed wheel verified" if args.deliver else ""))
    except subprocess.CalledProcessError as exc:
        print(
            f"CHECKS FAILED (exit {exc.returncode}); fix the first failed command.",
            file=sys.stderr,
        )
        return exc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
