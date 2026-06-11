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
