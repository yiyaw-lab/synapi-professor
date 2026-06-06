import os
from datetime import date
from typing import List, Tuple
from lesson_model import Lesson
from curriculum.llm_foundation import LLM_FOUNDATION
from curriculum.lesson_metadata import NOTEBOOK_FILES, REFERENCE_LIBRARY
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

TELEGRAM_API_BASE_URL = os.getenv("TELEGRAM_API_BASE_URL", "https://api.telegram.org")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
RECIPIENT_NAME = os.getenv("RECIPIENT_NAME", "Yiya")

# Repo slug used to build clickable lab links. The notebooks live on the
# default branch under labs/; GitHub renders them and Colab runs them in-browser.
GITHUB_REPO = os.getenv("GITHUB_REPO", "yiyaw-lab/YiyaProfessor")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")


def github_lab_url(filename: str) -> str:
    return f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/labs/{filename}"


def colab_lab_url(filename: str) -> str:
    return f"https://colab.research.google.com/github/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/labs/{filename}"


class ConfigurationError(ValueError):
    pass


class TelegramSendError(RuntimeError):
    pass


def load_config() -> Tuple[str, str, str, str]:
    bot_token = TELEGRAM_BOT_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    api_base = TELEGRAM_API_BASE_URL
    recipient = RECIPIENT_NAME

    missing = [name for name, value in (
        ("TELEGRAM_BOT_TOKEN", bot_token),
        ("TELEGRAM_CHAT_ID", chat_id),
    ) if not value]

    if missing:
        raise ConfigurationError(
            f"Missing environment variables: {', '.join(missing)}"
        )

    return bot_token, chat_id, api_base, recipient


def select_daily_lesson(lessons: List[Lesson]) -> Lesson:
    if not lessons:
        raise ValueError("Lesson list must contain at least one entry.")
    day_index = date.today().toordinal() % len(lessons)
    return lessons[day_index]


def build_message(recipient: str, lesson: Lesson) -> str:
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
    references_text = (
        "\n\nGo deeper:\n" + "\n".join(references) if references else ""
    )

    return (
        f"Good morning, {recipient}.\n\n"
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
    bot_token, chat_id, api_base, recipient = load_config()
    lesson = select_daily_lesson(LLM_FOUNDATION)
    message = build_message(recipient, lesson)

    result = send_telegram_message(bot_token, chat_id, message, api_base)
    print("Message sent successfully:", result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
