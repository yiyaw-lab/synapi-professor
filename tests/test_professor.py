"""Tests for the professor entry point: selection, formatting, config, send."""

from datetime import date

import pytest
import requests

import professor
from curriculum.lesson_metadata import NOTEBOOK_FILES, REFERENCE_LIBRARY
from lesson_model import Lesson

SAMPLE = Lesson(
    concept="Tokens",
    plain="LLMs read tokens, not words.",
    analogy="Like puzzle pieces of a page.",
    frontier="Tokens are the unit of billing.",
    bold_move="Count the tokens in a paragraph.",
)


# --- select_daily_lesson -------------------------------------------------


def test_select_daily_lesson_is_deterministic_for_a_date(monkeypatch):
    lessons = [SAMPLE, Lesson("B", "b", "b", "b", "b"), Lesson("C", "c", "c", "c", "c")]

    class FixedDate(date):
        @classmethod
        def today(cls):
            return cls(2026, 6, 6)

    monkeypatch.setattr(professor, "date", FixedDate)
    first = professor.select_daily_lesson(lessons)
    second = professor.select_daily_lesson(lessons)
    assert first is second
    expected = lessons[date(2026, 6, 6).toordinal() % len(lessons)]
    assert first is expected


def test_select_daily_lesson_cycles_the_whole_list(monkeypatch):
    lessons = [Lesson(str(i), "p", "a", "f", "b") for i in range(5)]
    seen = set()
    for day in range(5):
        ordinal = 100 + day

        class D(date):
            _ord = ordinal

            @classmethod
            def today(cls):
                return cls.fromordinal(cls._ord)

        monkeypatch.setattr(professor, "date", D)
        seen.add(professor.select_daily_lesson(lessons).concept)
    assert seen == {str(i) for i in range(5)}


def test_select_daily_lesson_rejects_empty():
    with pytest.raises(ValueError):
        professor.select_daily_lesson([])


# --- build_message -------------------------------------------------------


def test_build_message_includes_all_lesson_fields():
    msg = professor.build_message("Sam", SAMPLE)
    assert "Sam" in msg
    for field in (SAMPLE.concept, SAMPLE.plain, SAMPLE.analogy, SAMPLE.frontier, SAMPLE.bold_move):
        assert field in msg


def test_build_message_greeting_with_name():
    msg = professor.build_message("Sam", SAMPLE, greeting="Good morning")
    assert msg.startswith("Good morning, Sam.")


def test_build_message_greeting_without_name():
    # Empty/whitespace name -> name-less greeting, no dangling comma.
    for empty in ("", "   "):
        msg = professor.build_message(empty, SAMPLE)
        assert msg.startswith("Good morning.")
        assert "Good morning," not in msg


def test_build_message_custom_greeting():
    msg = professor.build_message("Sam", SAMPLE, greeting="Hey")
    assert msg.startswith("Hey, Sam.")


def test_format_greeting_helper():
    assert professor.format_greeting("Good morning", "Sam") == "Good morning, Sam."
    assert professor.format_greeting("Good morning", "") == "Good morning."
    assert professor.format_greeting("Hi", "  Pat  ") == "Hi, Pat."


def test_build_message_includes_lab_and_references_when_present():
    # "Tokens" has both a notebook and references registered.
    assert "Tokens" in NOTEBOOK_FILES
    assert REFERENCE_LIBRARY.get("Tokens")
    msg = professor.build_message("Sam", SAMPLE)
    assert "Lab" in msg
    assert "colab.research.google.com" in msg
    assert "Go deeper:" in msg
    assert REFERENCE_LIBRARY["Tokens"][0] in msg


def test_build_message_omits_lab_block_for_unknown_concept():
    lesson = Lesson("Nonexistent Concept", "p", "a", "f", "b")
    msg = professor.build_message("Sam", lesson)
    assert "Lab" not in msg
    assert "colab" not in msg
    assert "Go deeper:" not in msg


# --- load_config ---------------------------------------------------------


def test_load_config_raises_on_missing_required_vars(monkeypatch):
    monkeypatch.setattr(professor, "TELEGRAM_BOT_TOKEN", None)
    monkeypatch.setattr(professor, "TELEGRAM_CHAT_ID", None)
    with pytest.raises(professor.ConfigurationError) as exc:
        professor.load_config()
    assert "TELEGRAM_BOT_TOKEN" in str(exc.value)
    assert "TELEGRAM_CHAT_ID" in str(exc.value)


def test_load_config_returns_values_when_present(monkeypatch):
    monkeypatch.setattr(professor, "TELEGRAM_BOT_TOKEN", "tok")
    monkeypatch.setattr(professor, "TELEGRAM_CHAT_ID", "123")
    monkeypatch.setattr(professor, "TELEGRAM_API_BASE_URL", "https://example.test")
    monkeypatch.setattr(professor, "RECIPIENT_NAME", "Pat")
    monkeypatch.setattr(professor, "GREETING", "Hey")
    bot, chat, api, recipient, greeting = professor.load_config()
    assert (bot, chat, api, recipient, greeting) == (
        "tok",
        "123",
        "https://example.test",
        "Pat",
        "Hey",
    )


def test_load_config_allows_empty_recipient(monkeypatch):
    # Name is optional for a public user; only the Telegram vars are required.
    monkeypatch.setattr(professor, "TELEGRAM_BOT_TOKEN", "tok")
    monkeypatch.setattr(professor, "TELEGRAM_CHAT_ID", "123")
    monkeypatch.setattr(professor, "RECIPIENT_NAME", "")
    _, _, _, recipient, _ = professor.load_config()
    assert recipient == ""


# --- send_telegram_message ----------------------------------------------


class _FakeResponse:
    def __init__(self, payload, raise_exc=None):
        self._payload = payload
        self._raise_exc = raise_exc

    def raise_for_status(self):
        if self._raise_exc:
            raise self._raise_exc

    def json(self):
        return self._payload


def test_send_telegram_message_success(monkeypatch):
    captured = {}

    def fake_post(url, json, timeout):
        captured["url"] = url
        captured["json"] = json
        return _FakeResponse({"ok": True, "result": {"message_id": 1}})

    monkeypatch.setattr(professor.requests, "post", fake_post)
    data = professor.send_telegram_message("tok", "123", "hello", "https://api.telegram.org")
    assert data["ok"] is True
    assert captured["url"] == "https://api.telegram.org/bottok/sendMessage"
    assert captured["json"] == {"chat_id": "123", "text": "hello"}


def test_send_telegram_message_wraps_request_exception(monkeypatch):
    def fake_post(url, json, timeout):
        raise requests.exceptions.ConnectionError("boom")

    monkeypatch.setattr(professor.requests, "post", fake_post)
    with pytest.raises(professor.TelegramSendError):
        professor.send_telegram_message("tok", "123", "hi", "https://api.telegram.org")


def test_send_telegram_message_raises_on_api_not_ok(monkeypatch):
    def fake_post(url, json, timeout):
        return _FakeResponse({"ok": False, "description": "chat not found"})

    monkeypatch.setattr(professor.requests, "post", fake_post)
    with pytest.raises(professor.TelegramSendError) as exc:
        professor.send_telegram_message("tok", "123", "hi", "https://api.telegram.org")
    assert "chat not found" in str(exc.value)
