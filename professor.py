"""Entry point: pick the day's lesson, format it, and send it to Telegram.

The daily run is a short pipeline:

    select_daily_lesson(LLM_FOUNDATION)   # deterministic from today's date
        -> build_message(recipient, ...)  # plain text with lab + reference links
        -> send_telegram_message(...)     # POST to the Telegram Bot API

Configuration comes from environment variables (or a local ``.env``); see
``load_config`` and the README's Configuration table. Lab links are built from
``GITHUB_REPO``/``GITHUB_BRANCH`` so a fork points at its own notebooks.

Run directly to send today's lesson:  ``python professor.py``
"""

import os
from datetime import date

import requests
from dotenv import load_dotenv

from curriculum.lesson_metadata import NOTEBOOK_FILES, REFERENCE_LIBRARY
from curriculum.llm_foundation import LLM_FOUNDATION
from lesson_model import Lesson

load_dotenv(override=True)

TELEGRAM_API_BASE_URL = os.getenv("TELEGRAM_API_BASE_URL", "https://api.telegram.org")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Personalization. RECIPIENT_NAME is optional: leave it empty for a name-less
# greeting ("Good morning."). GREETING sets the opening line's tone.
RECIPIENT_NAME = os.getenv("RECIPIENT_NAME", "")
GREETING = os.getenv("GREETING", "Good morning")

# Repo slug used to build clickable lab links. The notebooks live on the
# default branch under labs/; GitHub renders them and Colab runs them in-browser.
GITHUB_REPO = os.getenv("GITHUB_REPO", "yiyaw-lab/synapi-professor")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")


def github_lab_url(filename: str) -> str:
    return f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/labs/{filename}"


def colab_lab_url(filename: str) -> str:
    return f"https://colab.research.google.com/github/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/labs/{filename}"


class ConfigurationError(ValueError):
    pass


class TelegramSendError(RuntimeError):
    pass


def load_config() -> tuple[str, str, str, str, str]:
    bot_token = TELEGRAM_BOT_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    api_base = TELEGRAM_API_BASE_URL
    recipient = RECIPIENT_NAME
    greeting = GREETING

    missing = [
        name
        for name, value in (
            ("TELEGRAM_BOT_TOKEN", bot_token),
            ("TELEGRAM_CHAT_ID", chat_id),
        )
        if not value
    ]

    if missing:
        raise ConfigurationError(f"Missing environment variables: {', '.join(missing)}")

    # The missing-check above guarantees these are set; assert narrows the types.
    assert bot_token is not None and chat_id is not None
    return bot_token, chat_id, api_base, recipient, greeting


def select_daily_lesson(lessons: list[Lesson]) -> Lesson:
    if not lessons:
        raise ValueError("Lesson list must contain at least one entry.")
    day_index = date.today().toordinal() % len(lessons)
    return lessons[day_index]


def format_greeting(greeting: str, recipient: str) -> str:
    """The opening line: include the name only when one is configured.

    "Good morning" + "Sam" -> "Good morning, Sam."
    "Good morning" + ""    -> "Good morning."
    """
    name = recipient.strip()
    return f"{greeting}, {name}." if name else f"{greeting}."


def build_message(recipient: str, lesson: Lesson, greeting: str = "Good morning") -> str:
    filename = NOTEBOOK_FILES.get(lesson.concept)
    if filename:
        lab_text = (
            "\n\n🧪 Lab (opens in Colab, runs as-is):\n"
            f"{colab_lab_url(filename)}\n"
            f"{github_lab_url(filename)}"
        )
    else:
        lab_text = ""

    references = REFERENCE_LIBRARY.get(lesson.concept, [])
    references_text = "\n\nGo deeper:\n" + "\n".join(references) if references else ""

    return (
        f"{format_greeting(greeting, recipient)}\n\n"
        f"Today’s concept: {lesson.concept}\n\n"
        "The idea:\n\n"
        f"{lesson.plain}\n\n"
        "Picture it:\n\n"
        f"{lesson.analogy}\n\n"
        "On the frontier:\n\n"
        f"{lesson.frontier}\n\n"
        "⚡ Bold move today:\n\n"
        f"{lesson.bold_move}"
        f"{lab_text}"
        f"{references_text}"
    )


def send_telegram_message(bot_token: str, chat_id: str, text: str, api_base: str) -> dict:
    url = f"{api_base}/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        raise TelegramSendError(f"Telegram request failed: {exc}") from exc

    data = response.json()
    if not data.get("ok"):
        raise TelegramSendError(
            f"Telegram API returned an error: {data.get('description', 'unknown error')}"
        )

    return data


def main() -> int:
    bot_token, chat_id, api_base, recipient, greeting = load_config()
    lesson = select_daily_lesson(LLM_FOUNDATION)
    message = build_message(recipient, lesson, greeting)

    result = send_telegram_message(bot_token, chat_id, message, api_base)
    print("Message sent successfully:", result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
