# Labs

One self-contained Jupyter notebook per curriculum concept (30 total). Each opens
in Google Colab and runs top to bottom with **Runtime → Run all** — no local setup.

Every notebook follows the same shape: an emoji header and hook, a quiet
`%pip install` cell, a runnable demo, a **Try it** twist, a **Takeaway**, and a
closing **🚀 Your move** that mirrors that day's bold move from the curriculum.

## ⚠️ These notebooks are generated — do not edit them by hand

`*.ipynb` and `manifest.json` are **build output**. The source of truth is
[`_generate.py`](_generate.py). Hand edits will be overwritten the next time it
runs (and CI regenerates to check they are in sync).

To change a lab, edit `_generate.py`, then regenerate from the repo root:

```bash
python labs/_generate.py
```

The generator also enforces that the notebooks it emits exactly match
`NOTEBOOK_FILES` in [`../curriculum/lesson_metadata.py`](../curriculum/lesson_metadata.py),
and rewrites `manifest.json`.

## Light vs. heavy (`manifest.json`)

The generator tags each notebook by execution cost so CI knows what to run:

- **light** — only `tiktoken` / `numpy`; CI executes these end to end on every push.
- **heavy** — download model weights (`sentence-transformers`, `transformers`,
  `torch`); CI validates their structure but does not execute them.

`manifest.json` is regenerated from `_generate.py`'s `HEAVY` set; the split is
checked in [`../tests/test_curriculum.py`](../tests/test_curriculum.py).

## The notebooks

| # | Notebook | Concept | Tier |
|---|----------|---------|------|
| 01 | `01_tokens.ipynb` | Tokens | light |
| 02 | `02_tokenization.ipynb` | Tokenization | light |
| 03 | `03_vocabulary.ipynb` | Vocabulary | light |
| 04 | `04_embeddings.ipynb` | Embeddings | heavy |
| 05 | `05_semantic_space.ipynb` | Semantic Space | heavy |
| 06 | `06_similarity.ipynb` | Similarity | heavy |
| 07 | `07_language_as_numbers.ipynb` | Language as Numbers | heavy |
| 08 | `08_next_token_prediction.ipynb` | Next Token Prediction | heavy |
| 09 | `09_attention.ipynb` | Attention | light |
| 10 | `10_self_attention.ipynb` | Self-Attention | light |
| 11 | `11_context_windows.ipynb` | Context Windows | light |
| 12 | `12_positional_encoding.ipynb` | Positional Encoding | light |
| 13 | `13_transformers.ipynb` | Transformers | light |
| 14 | `14_information_flow.ipynb` | Information Flow | heavy |
| 15 | `15_pretraining.ipynb` | Pretraining | light |
| 16 | `16_loss_functions.ipynb` | Loss Functions | light |
| 17 | `17_gradient_descent.ipynb` | Gradient Descent | light |
| 18 | `18_parameters.ipynb` | Parameters | light |
| 19 | `19_scaling_laws.ipynb` | Scaling Laws | light |
| 20 | `20_emergent_abilities.ipynb` | Emergent Abilities | light |
| 21 | `21_learning_review.ipynb` | Learning Review | light |
| 22 | `22_hallucinations.ipynb` | Hallucinations | light |
| 23 | `23_context_poisoning.ipynb` | Context Poisoning | light |
| 24 | `24_retrieval_failures.ipynb` | Retrieval Failures | light |
| 25 | `25_goodharts_law.ipynb` | Goodhart's Law in AI | light |
| 26 | `26_distribution_shift.ipynb` | Distribution Shift | light |
| 27 | `27_alignment.ipynb` | Alignment | light |
| 28 | `28_evaluation.ipynb` | Evaluation | light |
| 29 | `29_prompt_engineering.ipynb` | Prompt Engineering | light |
| 30 | `30_systems_thinking.ipynb` | Systems Thinking for AI | light |

The numbering follows the lesson order in
[`../curriculum/llm_foundation.py`](../curriculum/llm_foundation.py).
