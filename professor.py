import os
from dataclasses import dataclass
from datetime import date
from typing import List, Tuple

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

TELEGRAM_API_BASE_URL = os.getenv("TELEGRAM_API_BASE_URL", "https://api.telegram.org")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
RECIPIENT_NAME = os.getenv("RECIPIENT_NAME", "Yiya")


@dataclass(frozen=True)
class Lesson:
    concept: str
    plain: str
    analogy: str
    exercise: str


LESSONS: List[Lesson] = [
    Lesson(
        concept="Attention",
        plain="Attention lets an LLM decide which parts of the input matter most.",
        analogy="Like knowing which voice to listen to in a crowded room.",
        exercise="Explain attention using a dinner table conversation.",
    ),
    Lesson(
        concept="Tokenization",
        plain="Tokenization breaks text into smaller pieces the model can process.",
        analogy="Like cutting a sentence into puzzle pieces before giving it to the model.",
        exercise="Look at the sentence 'I love language models' and guess how it might be split.",
    ),
    Lesson(
        concept="Embeddings",
        plain="Embeddings turn words or ideas into numbers that capture meaning.",
        analogy="Like giving every concept a coordinate on a giant map of meaning.",
        exercise="Explain why 'king' and 'queen' would be closer than 'king' and 'banana'.",
    ),
]


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
    return (
        f"Good morning, {recipient}.\n\n"
        f"Today’s concept: {lesson.concept}\n\n"
        "Plain idea:\n\n"
        f"{lesson.plain}\n\n"
        "Analogy:\n\n"
        f"{lesson.analogy}\n\n"
        "Tiny exercise:\n\n"
        f"{lesson.exercise}"
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
    lesson = select_daily_lesson(LESSONS)
    message = build_message(recipient, lesson)

    result = send_telegram_message(bot_token, chat_id, message, api_base)
    print("Message sent successfully:", result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
