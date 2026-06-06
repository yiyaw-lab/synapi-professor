from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    concept: str
    plain: str
    analogy: str
    frontier: str    # one vivid line tying the concept to current AI work
    bold_move: str   # one concrete, ambitious action for the day
