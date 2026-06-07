# Contributing

Thanks for looking under the hood. This is a small, deliberately simple project;
this guide is the fast path to understanding it and changing it safely.

## Architecture at a glance

One daily job turns a date into a Telegram message:

```
                         ┌─────────────────────────────────────────┐
   .github/workflows/    │ professor.py  (the entry point)          │
   professor.yml  ──────▶│                                          │
   (daily cron)          │  track = CURRICULA[CURRICULUM]            │
                         │  select_daily_lesson(track.lessons)      │
                         │     pick track.lessons[ordinal % 30]     │
                         │  build_message(recipient, lesson)        │
                         │     + lab links (Colab + GitHub)         │
                         │     + references ("Go deeper")           │
                         │  send_telegram_message(...)              │
                         └──────────────┬──────────────────────────┘
                                        │ reads
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
 lesson_model.py            curriculum/foundation_llm.py     curriculum/foundation_metadata.py
 the Lesson dataclass       the 30 lessons (content)         references + notebook filenames
                                        │                               │
                                        │ numbering &                   │ NOTEBOOK_FILES
                                        │ concept keys                  │ keys → labs/*.ipynb
                                        ▼                               ▼
                            curriculum/foundation_path.py          labs/  (generated notebooks)
                            5-week study plan (for humans)         built by labs/_generate.py
```

(The advanced track mirrors this with `advanced_llm.py` / `advanced_metadata.py` /
`advanced_path.py`.) The data flows one way: **content** (`foundation_llm.py`) and
its **metadata** (`foundation_metadata.py`) are plain data keyed by the lesson's
`concept`; everything else reads them. The day's lesson is chosen deterministically
from the date, so nothing is random and the same day always yields the same concept.

### Where things live

| Path | Role |
|------|------|
| `professor.py` | Entry point: select → format → send. The only file that talks to Telegram. |
| `lesson_model.py` | The `Lesson` dataclass — the one shape all lessons share. |
| `curriculum/__init__.py` | The `CURRICULA` track registry — source of truth for which tracks exist. |
| `curriculum/foundation_llm.py` | The 30 foundation lessons. **Content source of truth.** |
| `curriculum/foundation_metadata.py` | Foundation per-concept references + notebook filenames. |
| `curriculum/foundation_path.py` | Foundation 5-week study plan (human-facing). |
| `curriculum/advanced_llm.py` | The 30 advanced lessons. |
| `curriculum/advanced_metadata.py` | Advanced per-concept references + notebook filenames. |
| `curriculum/advanced_path.py` | Advanced 5-week study plan. |
| `curriculum/tooling.py` | Recommended libraries for running labs locally. |
| `labs/_generate.py` | **Generator** for all notebooks + `manifest.json`. |
| `labs/*.ipynb` | Generated labs — do not hand-edit (see below). `NN_…` = foundation, `aNN_…` = advanced. |
| `tests/` | pytest suite covering the sender and per-track curriculum invariants. |

### Curriculum tracks

Two tracks ship today — `foundation` and `advanced` — registered in
`curriculum/__init__.py` as `CURRICULA` (a name → `Track(lessons, references,
notebooks)` map). `professor.py` picks one via the `CURRICULUM` env var
(default `foundation`), and the tests parametrize their invariants over every
track in the registry. Adding a track is: create its three modules, add one entry
to `CURRICULA`, add its labs to the generator — everything else follows.

## Dev setup

```bash
pip install -r requirements-dev.txt   # runtime + test/lint deps
```

## The golden rule: notebooks are generated

`labs/*.ipynb` and `labs/manifest.json` are **build artifacts**. Edit
[`labs/_generate.py`](labs/_generate.py), never the notebooks. Then:

```bash
python labs/_generate.py
```

The generator asserts that the notebooks it emits exactly match the registered
notebook maps (`NOTEBOOK_FILES` in `curriculum/foundation_metadata.py` and
`ADV_NOTEBOOK_FILES` in `curriculum/advanced_metadata.py`), so the message's lab
links can never point at a file that does not exist.

## Adding or changing a lesson

Pick the track's modules — foundation (`foundation_llm.py` / `foundation_metadata.py`)
or advanced (`advanced_llm.py` / `advanced_metadata.py`). The steps are identical:

1. Edit the `Lesson(...)` entry in the track's lessons module (keep all five
   fields non-empty).
2. Add its references under the same `concept` key in the track's metadata module
   (`REFERENCE_LIBRARY` / `ADV_REFERENCE_LIBRARY`).
3. If it should have a lab, add the concept → filename to the track's notebook map
   (`NOTEBOOK_FILES` / `ADV_NOTEBOOK_FILES`; advanced filenames use the `aNN_`
   prefix), add a matching entry in `labs/_generate.py`'s `NOTEBOOKS` /
   `ADVANCED_NOTEBOOKS` (and to `HEAVY` if it downloads model weights), then run
   `python labs/_generate.py`.
4. Run the checks below.

## Checks (what CI runs)

```bash
ruff check .            # lint
mypy                    # type-check the source (config in pyproject.toml)
pytest                  # 100+ tests: selection, formatting, curriculum invariants
python labs/_generate.py && git diff --exit-code labs/   # notebooks in sync
```

The test suite guarantees the **30/30 invariant per track**: every concept has a
reference and a notebook, every registered notebook (across all tracks) exists on
disk, and `manifest.json` partitions all of them. If you add a concept without its
lab/references, tests fail — by design.

## Style

- Python ≥ 3.10, `ruff` line length 100 (config in `pyproject.toml`).
- Keep content as data and behavior in `professor.py`; resist adding logic to the
  curriculum modules.
- Never commit secrets. `.env` is gitignored; the bot token lives only there and
  in GitHub Actions secrets.
