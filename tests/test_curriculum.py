"""Tests for curriculum integrity and the 30/30-per-track lab completeness guarantee.

The same invariants are enforced for every track in ``curriculum.CURRICULA``:
every concept has a reference + a registered notebook, every registered notebook
exists on disk, and ``manifest.json`` partitions all notebooks across all tracks.
"""

import json
from pathlib import Path

import nbformat
import pytest

from curriculum import CURRICULA

LABS = Path(__file__).resolve().parent.parent / "labs"

# (track_name, lesson) pairs and (track_name, concept) pairs for parametrization.
ALL_LESSONS = [(name, lesson) for name, t in CURRICULA.items() for lesson in t.lessons]
ALL_CONCEPTS = [(name, lesson.concept) for name, lesson in ALL_LESSONS]
LESSON_IDS = [f"{name}:{lesson.concept}" for name, lesson in ALL_LESSONS]
CONCEPT_IDS = [f"{name}:{concept}" for name, concept in ALL_CONCEPTS]

# Union of every track's registered notebooks.
ALL_NOTEBOOKS = {fn for t in CURRICULA.values() for fn in t.notebooks.values()}


# --- lesson content ------------------------------------------------------


@pytest.mark.parametrize("track,lesson", ALL_LESSONS, ids=LESSON_IDS)
def test_every_lesson_has_all_fields_non_empty(track, lesson):
    for field in ("concept", "plain", "analogy", "frontier", "bold_move"):
        value = getattr(lesson, field)
        assert isinstance(value, str) and value.strip(), f"{lesson.concept}: empty {field}"


@pytest.mark.parametrize("name", list(CURRICULA))
def test_concepts_are_unique_within_each_track(name):
    concepts = [lesson.concept for lesson in CURRICULA[name].lessons]
    assert len(concepts) == len(set(concepts))


def test_concepts_are_unique_across_tracks():
    # Tracks deliberately don't share concept names (and so don't collide on labs).
    all_concepts = [c for _, c in ALL_CONCEPTS]
    assert len(all_concepts) == len(set(all_concepts))


@pytest.mark.parametrize("track,concept", ALL_CONCEPTS, ids=CONCEPT_IDS)
def test_every_concept_has_at_least_one_reference(track, concept):
    refs = CURRICULA[track].references.get(concept)
    assert refs, f"{track}:{concept} has no references"
    assert all(r.startswith("http") for r in refs)


# --- completeness: every concept has a lab, every lab is registered ------


@pytest.mark.parametrize("track,concept", ALL_CONCEPTS, ids=CONCEPT_IDS)
def test_every_concept_has_a_registered_notebook(track, concept):
    assert concept in CURRICULA[track].notebooks, f"{track}:{concept} has no notebook"


def test_notebook_files_match_files_on_disk():
    on_disk = {p.name for p in LABS.glob("*.ipynb")}
    assert ALL_NOTEBOOKS == on_disk, (
        f"only-registered={ALL_NOTEBOOKS - on_disk}, only-on-disk={on_disk - ALL_NOTEBOOKS}"
    )


@pytest.mark.parametrize("name", list(CURRICULA))
def test_each_track_covers_thirty_concepts(name):
    track = CURRICULA[name]
    concepts = [lesson.concept for lesson in track.lessons]
    assert len(concepts) == 30
    assert len(track.notebooks) == 30


# --- notebook structure (cheap validation for every lab) -----------------


@pytest.mark.parametrize("filename", sorted(ALL_NOTEBOOKS))
def test_notebook_is_valid_and_well_formed(filename):
    nb = nbformat.read(LABS / filename, as_version=4)
    nbformat.validate(nb)
    sources = [c.source for c in nb.cells]
    # Each lab opens with a header and ends with the "Your move" call to action.
    assert sources[0].startswith("#")
    assert "🚀 Your move" in sources[-1]
    # Has at least one runnable code cell.
    assert any(c.cell_type == "code" for c in nb.cells)


# --- manifest mirrors the generator's tiering ----------------------------


def test_manifest_partitions_all_notebooks():
    manifest = json.loads((LABS / "manifest.json").read_text())
    light, heavy = set(manifest["light"]), set(manifest["heavy"])
    assert light.isdisjoint(heavy)
    assert light | heavy == ALL_NOTEBOOKS
