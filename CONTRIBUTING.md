# Contributing

Thanks for looking under the hood. This is a small, deliberately simple project;
this guide is the fast path to understanding it and changing it safely.

## Architecture at a glance

One daily job turns a date into a Telegram message:

```
                         ┌─────────────────────────────────────────┐
   .github/workflows/    │ professor.py  (the entry point)          │
   professor.yml  ──────▶│                                          │
   (daily cron)          │  select_daily_lesson(LLM_FOUNDATION)     │
                         │     pick LLM_FOUNDATION[ordinal % 30]    │
                         │  build_message(recipient, lesson)        │
                         │     + lab links (Colab + GitHub)         │
                         │     + references ("Go deeper")           │
                         │  send_telegram_message(...)              │
                         └──────────────┬──────────────────────────┘
                                        │ reads
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
 lesson_model.py            curriculum/llm_foundation.py     curriculum/lesson_metadata.py
 the Lesson dataclass       the 30 lessons (content)         references + notebook filenames
                                        │                               │
                                        │ numbering &                   │ NOTEBOOK_FILES
                                        │ concept keys                  │ keys → labs/*.ipynb
                                        ▼                               ▼
                            curriculum/learning_path.py            labs/  (generated notebooks)
                            5-week study plan (for humans)         built by labs/_generate.py
```

The data flows one way: **content** (`llm_foundation.py`) and its **metadata**
(`lesson_metadata.py`) are plain data keyed by the lesson's `concept`; everything
else reads them. The day's lesson is chosen deterministically from the date, so
nothing is random and the same day always yields the same concept.

### Where things live

| Path | Role |
|------|------|
| `professor.py` | Entry point: select → format → send. The only file that talks to Telegram. |
| `lesson_model.py` | The `Lesson` dataclass — the one shape all lessons share. |
| `curriculum/llm_foundation.py` | The 30 lessons. **Content source of truth.** |
| `curriculum/lesson_metadata.py` | Per-concept references + notebook filenames. |
| `curriculum/learning_path.py` | Suggested 5-week study plan (human-facing). |
| `curriculum/tooling.py` | Recommended libraries for running labs locally. |
| `labs/_generate.py` | **Generator** for the notebooks + `manifest.json`. |
| `labs/*.ipynb` | Generated labs — do not hand-edit (see below). |
| `tests/` | pytest suite covering the sender and curriculum invariants. |

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

The generator asserts that the notebooks it emits exactly match `NOTEBOOK_FILES`
in `curriculum/lesson_metadata.py`, so the message's lab links can never point at
a file that does not exist.

## Adding or changing a lesson

1. Edit the `Lesson(...)` entry in `curriculum/llm_foundation.py` (keep all five
   fields non-empty).
2. Add its references under the same `concept` key in
   `curriculum/lesson_metadata.py` (`REFERENCE_LIBRARY`).
3. If it should have a lab, add the concept → filename to `NOTEBOOK_FILES`, add a
   matching entry in `labs/_generate.py` (and to `HEAVY` if it downloads model
   weights), then run `python labs/_generate.py`.
4. Run the checks below.

## Checks (what CI runs)

```bash
ruff check .            # lint
mypy                    # type-check the source (config in pyproject.toml)
pytest                  # 100+ tests: selection, formatting, curriculum invariants
python labs/_generate.py && git diff --exit-code labs/   # notebooks in sync
```

The test suite guarantees the **30/30 invariant**: every concept has a reference
and a notebook, every registered notebook exists on disk, and `manifest.json`
partitions all of them. If you add a concept without its lab/references, tests
fail — by design.

## Style

- Python ≥ 3.10, `ruff` line length 100 (config in `pyproject.toml`).
- Keep content as data and behavior in `professor.py`; resist adding logic to the
  curriculum modules.
- Never commit secrets. `.env` is gitignored; the bot token lives only there and
  in GitHub Actions secrets.
