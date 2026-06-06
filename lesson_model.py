"""The ``Lesson`` data model — the single shape every lesson conforms to.

One lesson is the unit the professor sends each day. Keeping it a tiny frozen
dataclass (no behavior) lets the curriculum in ``curriculum/llm_foundation.py``
read as plain data and lets ``professor.build_message`` rely on a fixed set of
fields. Each field maps to one section of the delivered message:

    concept   -> "Today's concept"
    plain     -> "The idea"
    analogy   -> "Picture it"
    frontier  -> "On the frontier"  (ties the concept to current AI work)
    bold_move -> "Bold move today"  (one concrete action: build / provoke / reach out)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    concept: str
    plain: str
    analogy: str
    frontier: str  # one vivid line tying the concept to current AI work
    bold_move: str  # one concrete, ambitious action for the day
