"""Execute the lightweight lab notebooks headless, top to bottom.

Reads labs/manifest.json (written by _generate.py) and runs every notebook in
the "light" tier with nbclient. A non-zero exit means a lab no longer runs —
the guarantee CI enforces on every push. The model-downloading "heavy" tier is
validated structurally by the test suite, not executed here.

Usage: python labs/_run_light.py
"""

import json
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

LABS = Path(__file__).resolve().parent


def main() -> int:
    manifest = json.loads((LABS / "manifest.json").read_text())
    light = manifest["light"]
    failures = []
    for name in light:
        nb = nbformat.read(LABS / name, as_version=4)
        client = NotebookClient(nb, timeout=120, kernel_name="python3")
        try:
            client.execute()
            print(f"ok   {name}")
        except CellExecutionError as exc:
            failures.append(name)
            print(f"FAIL {name}\n{exc}", file=sys.stderr)

    print(f"\nexecuted {len(light)} light notebooks, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
