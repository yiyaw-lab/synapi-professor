# Labs

One self-contained Jupyter notebook per curriculum concept across both tracks
(60 total: 30 foundation `NN_…` + 30 advanced `aNN_…`). Each opens in Google Colab
and runs top to bottom with **Runtime → Run all** — no local setup.

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
`NOTEBOOK_FILES` in [`../curriculum/foundation_metadata.py`](../curriculum/foundation_metadata.py),
and rewrites `manifest.json`.

## Light vs. heavy (`manifest.json`)

The generator tags each notebook by execution cost so CI knows what to run:

- **light** — only `tiktoken` / `numpy`; CI executes these end to end on every push.
- **heavy** — download model weights (`sentence-transformers`, `transformers`,
  `torch`); CI validates their structure but does not execute them.

`manifest.json` is regenerated from `_generate.py`'s `HEAVY` set; the split is
checked in [`../tests/test_curriculum.py`](../tests/test_curriculum.py).

## The notebooks

### Foundation track

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
[`../curriculum/foundation_llm.py`](../curriculum/foundation_llm.py).

### Advanced track

All advanced labs are **light** (pure-numpy simulations), so CI executes them all.

| # | Notebook | Concept |
|---|----------|---------|
| a01 | `a01_supervised_fine_tuning.ipynb` | Supervised Fine-Tuning |
| a02 | `a02_rlhf.ipynb` | RLHF |
| a03 | `a03_dpo.ipynb` | Direct Preference Optimization |
| a04 | `a04_constitutional_ai.ipynb` | Constitutional AI |
| a05 | `a05_reasoning_models.ipynb` | Reasoning Models |
| a06 | `a06_reward_hacking.ipynb` | Reward Hacking |
| a07 | `a07_peft_lora.ipynb` | Parameter-Efficient Fine-Tuning |
| a08 | `a08_quantization.ipynb` | Quantization |
| a09 | `a09_distillation.ipynb` | Knowledge Distillation |
| a10 | `a10_mixture_of_experts.ipynb` | Mixture-of-Experts |
| a11 | `a11_speculative_decoding.ipynb` | Speculative Decoding |
| a12 | `a12_kv_cache.ipynb` | KV-Cache and Paged Attention |
| a13 | `a13_flash_attention.ipynb` | FlashAttention |
| a14 | `a14_state_space_models.ipynb` | State-Space Models |
| a15 | `a15_long_context.ipynb` | Long-Context Methods |
| a16 | `a16_multimodal.ipynb` | Multimodal Models |
| a17 | `a17_grouped_query_attention.ipynb` | Grouped-Query Attention |
| a18 | `a18_synthetic_data.ipynb` | Synthetic Data |
| a19 | `a19_mech_interp.ipynb` | Mechanistic Interpretability |
| a20 | `a20_sparse_autoencoders.ipynb` | Sparse Autoencoders |
| a21 | `a21_activation_steering.ipynb` | Activation Steering |
| a22 | `a22_model_editing.ipynb` | Model Editing |
| a23 | `a23_scaling_laws_revisited.ipynb` | Scaling Laws Revisited |
| a24 | `a24_grokking.ipynb` | Grokking |
| a25 | `a25_tool_use.ipynb` | Tool Use |
| a26 | `a26_agentic_loops.ipynb` | Agentic Loops |
| a27 | `a27_advanced_rag.ipynb` | Advanced RAG |
| a28 | `a28_llm_as_judge.ipynb` | LLM-as-a-Judge |
| a29 | `a29_structured_outputs.ipynb` | Structured Outputs |
| a30 | `a30_inference_economics.ipynb` | Inference Economics |

The numbering follows the lesson order in
[`../curriculum/advanced_llm.py`](../curriculum/advanced_llm.py).
