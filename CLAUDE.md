# YiyaProfessor

@CONTRIBUTING.md

## Non-negotiables

- **`labs/*.ipynb` (and `labs/manifest.json`) are GENERATED build artifacts — never hand-edit.**
  Edit `labs/_generate.py`, then regenerate with `python labs/_generate.py`.
- **CI gate** (run before declaring any change done):
  ```bash
  ruff check . && mypy && pytest && python labs/_generate.py && git diff --exit-code labs/
  ```
- **30-per-track invariant**: each track (`foundation`, `advanced`) has exactly 30 lessons,
  and every concept must have a reference and a notebook (concept ↔ reference ↔ notebook).
  Tests enforce this — adding a lesson without its references/lab fails by design.
- **Content as data**: curriculum modules are plain data; behavior changes go only in
  `professor.py` (the one file that selects, formats, and sends).

## Setup

```bash
pip install -r requirements-dev.txt
```

Local-environment gotcha: `python`/`pytest`/`ruff`/`mypy` resolve to Anaconda
Python 3.9 on this machine while pyproject declares `requires-python = ">=3.10"`.
The full gate passes under 3.9 today (verified 2026-06-11: 268 pytest, ruff clean),
and python3.11 here has no deps installed — but if something fails strangely,
check the version mismatch first.
