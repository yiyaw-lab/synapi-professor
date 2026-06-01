from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    concept: str
    plain: str
    analogy: str
    exercise: str