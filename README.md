# YiyaProfessor

[![CI](https://github.com/yiyaw-lab/YiyaProfessor/actions/workflows/ci.yml/badge.svg)](https://github.com/yiyaw-lab/YiyaProfessor/actions/workflows/ci.yml)

A tiny daily professor for the foundations of large language models.

Every morning it picks one concept from a 30-lesson curriculum and sends it to
Telegram — plain explanation, a vivid analogy, a note from the current frontier,
one bold move to try, a runnable Colab lab, and a couple of curated references to
go deeper. No app to open, no streak to maintain. One idea a day, in your chat.

## What a lesson looks like

```
Good morning, Yiya.

Today’s concept: Tokens

The idea:
LLMs do not read words directly. They read tokens: small chunks of text
that may be words, word parts, punctuation, or spaces.

Picture it:
Like reading a book after every page has been cut into puzzle pieces.

On the frontier:
Token counts are the unit of billing and the hard limit of every model...

⚡ Bold move today:
Build: write a 40-line script that pastes any text, counts its tokens with
tiktoken, and prints what it would cost at GPT-4o and Claude prices.

🧪 Lab (opens in Colab, runs as-is):
https://colab.research.google.com/github/.../labs/01_tokens.ipynb

Go deeper:
https://tiktokenizer.vercel.app/
...
```

## The curriculum

30 lessons that build from text-as-tokens up to thinking about AI systems as a
whole. The suggested pace is a 5-week path (3–5 hours/week):

| Week | Theme |
|------|-------|
| 1 | Token and embedding fundamentals |
| 2 | Core model mechanisms (attention, context, transformers) |
| 3 | Training dynamics (loss, gradients, scaling laws) |
| 4 | Reliability and failure modes |
| 5 | Alignment, evaluation, and prompting |

The full lesson list lives in [curriculum/llm_foundation.py](curriculum/llm_foundation.py);
the week-by-week plan is in [curriculum/learning_path.py](curriculum/learning_path.py).

## Labs

All 30 concepts ship with a self-contained Jupyter notebook in [labs/](labs/) —
one per lesson, from tokens through systems thinking. Each opens in Google Colab
and runs top to bottom with **Runtime → Run all**, no local setup required: an
emoji hook, a quiet `%pip install`, a runnable demo, a "Try it" exercise, and a
closing "🚀 Your move" challenge.

The notebooks are not hand-edited. They are generated from a single source of
truth, [labs/_generate.py](labs/_generate.py), and CI proves they still run (see
[Development](#development)).

## How it works

```
professor.py            entry point: pick the day's lesson, build it, send it
lesson_model.py         the Lesson dataclass
curriculum/
  llm_foundation.py     the 30 lessons (concept, plain, analogy, frontier, bold move)
  lesson_metadata.py    notebook filenames + curated references per concept
  learning_path.py      the 5-week study plan
  tooling.py            recommended tools for the labs
labs/
  _generate.py          source of truth: builds all 30 notebooks
  *.ipynb               generated, Colab-runnable notebooks
  manifest.json         generated: which labs CI executes vs. structure-checks
tests/                  pytest suite (logic + curriculum/lab integrity)
.github/workflows/
  professor.yml         daily scheduled lesson
  ci.yml                lint, type-check, tests, lab execution
```

The day's lesson is chosen deterministically from the date, so everyone subscribed
to the same chat sees the same concept on the same day and the curriculum cycles
through all 30 over time.

The generator enforces an invariant — every concept has exactly one registered
notebook, and every notebook on disk is registered — so the lab links in each
message can never point at a file that does not exist. The test suite re-checks
this, and CI fails if the committed notebooks ever drift from the generator.

## Run it yourself

You'll need a Telegram bot and a chat to send to.

1. **Create a bot** with [@BotFather](https://t.me/BotFather) and copy its token.
2. **Find your chat ID** — message your bot, then visit
   `https://api.telegram.org/bot<TOKEN>/getUpdates` and read the `chat.id`.
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure** a `.env` file (see below) and send a lesson:

   ```bash
   python professor.py
   ```

### Configuration

Set these as environment variables or in a `.env` file:

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `TELEGRAM_BOT_TOKEN` | yes | — | Bot token from BotFather |
| `TELEGRAM_CHAT_ID` | yes | — | Where to send the lesson |
| `RECIPIENT_NAME` | no | `Yiya` | Name in the greeting |
| `TELEGRAM_API_BASE_URL` | no | `https://api.telegram.org` | Override the API host |
| `GITHUB_REPO` | no | `yiyaw-lab/YiyaProfessor` | Repo slug for lab links |
| `GITHUB_BRANCH` | no | `main` | Branch for lab links |

> `.env` is gitignored. Never commit your bot token.

## Daily delivery via GitHub Actions

The included workflow ([.github/workflows/professor.yml](.github/workflows/professor.yml))
runs `professor.py` on a daily cron (and on demand via *Run workflow*). To use it
on your own fork:

1. Go to **Settings → Secrets and variables → Actions**.
2. Add `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` as repository secrets.
3. Enable Actions; the lesson will arrive each day.

## Requirements

- Python 3.10+
- [`requests`](https://pypi.org/project/requests/) and
  [`python-dotenv`](https://pypi.org/project/python-dotenv/) (see
  [requirements.txt](requirements.txt))

The labs use additional libraries (`tiktoken`, `transformers`,
`sentence-transformers`, and more) but install their own dependencies when run in
Colab. See [curriculum/tooling.py](curriculum/tooling.py) for the full list if you
prefer to run them locally.

## Development

[CONTRIBUTING.md](CONTRIBUTING.md) has the architecture diagram, where each file
lives, and how to add a lesson; [labs/README.md](labs/README.md) indexes the
notebooks.

```bash
pip install -r requirements-dev.txt

ruff check . && ruff format --check .   # lint + format
mypy                                    # type-check
pytest                                  # unit tests + curriculum/lab integrity
python labs/_generate.py                # regenerate notebooks from source
python labs/_run_light.py               # execute the lightweight labs end to end
```

CI ([.github/workflows/ci.yml](.github/workflows/ci.yml)) runs all of the above on
every push and pull request. Notebook execution is **tiered**: the lightweight
labs (`numpy`/`tiktoken` only) are executed top to bottom on every push, so a
broken lab fails CI. The six labs that download model weights
(`transformers`/`sentence-transformers`) are validated structurally on every push
and executed on a slower cadence — the split lives in
[labs/manifest.json](labs/manifest.json), written by the generator. If you change a
lab, edit [labs/_generate.py](labs/_generate.py) (not the `.ipynb` files) and
regenerate; CI rejects any drift between the two.

## License

This project is dual-licensed by its nature — code and content are licensed
separately:

- **Code** (Python source, the notebook generator, tests, CI) — Apache License 2.0,
  © 2026 Coaur Inc. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
- **Educational content** (the lessons in [curriculum/](curriculum/) and the docs) —
  [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE-CONTENT), © 2026 Coaur Inc.
  Reuse freely, including commercially; just credit Coaur Inc.
