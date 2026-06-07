"""The curriculum package: two lesson tracks and their per-concept metadata.

Foundation track (how LLMs work, from tokens up):
- ``foundation_llm``      the 30 ``Lesson`` objects (the content source of truth)
- ``foundation_metadata`` references + notebook filenames, keyed by concept
- ``foundation_path``     the suggested 5-week study plan

Advanced track (post-training, efficiency, interpretability, agents):
- ``advanced_llm``      the 30 advanced ``Lesson`` objects
- ``advanced_metadata`` advanced references + notebook filenames
- ``advanced_path``     the advanced 5-week study plan

Plus ``tooling`` — recommended libraries for running labs locally (shared).

``CURRICULA`` is the single registry of available tracks. Both the daily sender
(``professor.py``) and the integrity tests read from it, so adding a track in one
place wires it everywhere.
"""

from typing import NamedTuple

from lesson_model import Lesson

from .advanced_llm import ADVANCED_LLM
from .advanced_metadata import ADV_NOTEBOOK_FILES, ADV_REFERENCE_LIBRARY
from .foundation_llm import LLM_FOUNDATION
from .foundation_metadata import NOTEBOOK_FILES, REFERENCE_LIBRARY


class Track(NamedTuple):
    """One curriculum track: its lessons plus the metadata maps keyed by concept."""

    lessons: list[Lesson]
    references: dict[str, list[str]]
    notebooks: dict[str, str]


CURRICULA: dict[str, Track] = {
    "foundation": Track(
        lessons=LLM_FOUNDATION,
        references=REFERENCE_LIBRARY,
        notebooks=NOTEBOOK_FILES,
    ),
    "advanced": Track(
        lessons=ADVANCED_LLM,
        references=ADV_REFERENCE_LIBRARY,
        notebooks=ADV_NOTEBOOK_FILES,
    ),
}

DEFAULT_TRACK = "foundation"
