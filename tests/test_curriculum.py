"""Tests for curriculum integrity and the 30/30 lab completeness guarantee."""

import json
from pathlib import Path

import nbformat
import pytest

from curriculum.lesson_metadata import NOTEBOOK_FILES, REFERENCE_LIBRARY
from curriculum.llm_foundation import LLM_FOUNDATION

LABS = Path(__file__).resolve().parent.parent / "labs"
CONCEPTS = [lesson.concept for lesson in LLM_FOUNDATION]


# --- lesson content ------------------------------------------------------


@pytest.mark.parametrize("lesson", LLM_FOUNDATION, ids=CONCEPTS)
def test_every_lesson_has_all_fields_non_empty(lesson):
    for field in ("concept", "plain", "analogy", "frontier", "bold_move"):
        value = getattr(lesson, field)
        assert isinstance(value, str) and value.strip(), f"{lesson.concept}: empty {field}"


def test_concepts_are_unique():
    assert len(CONCEPTS) == len(set(CONCEPTS))


@pytest.mark.parametrize("concept", CONCEPTS)
def test_every_concept_has_at_least_one_reference(concept):
    refs = REFERENCE_LIBRARY.get(concept)
    assert refs, f"{concept} has no references"
    assert all(r.startswith("http") for r in refs)


# --- completeness: every concept has a lab, every lab is registered ------


def test_every_concept_has_a_registered_notebook():
    missing = [c for c in CONCEPTS if c not in NOTEBOOK_FILES]
    assert not missing, f"concepts without a notebook: {missing}"


def test_notebook_files_match_files_on_disk():
    registered = set(NOTEBOOK_FILES.values())
    on_disk = {p.name for p in LABS.glob("*.ipynb")}
    assert registered == on_disk, (
        f"only-registered={registered - on_disk}, only-on-disk={on_disk - registered}"
    )


def test_all_thirty_concepts_are_covered():
    assert len(CONCEPTS) == 30
    assert len(NOTEBOOK_FILES) == 30


# --- notebook structure (cheap validation for every lab) -----------------


@pytest.mark.parametrize("filename", sorted(NOTEBOOK_FILES.values()))
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
    assert light | heavy == set(NOTEBOOK_FILES.values())
