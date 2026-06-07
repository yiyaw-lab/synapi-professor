"""Foundation per-concept side data, all keyed by ``Lesson.concept``.

Kept separate from ``foundation_llm.py`` so the lesson text stays readable and
the links/tooling can change independently:

    REFERENCE_LIBRARY  concept -> 1-3 canonical URLs ("Go deeper" in the message)
    NOTEBOOK_FILES     concept -> bare lab filename (professor.py builds the URLs)
    TOOLING            library -> (purpose, install command) for running labs locally
    LEARNING_NOTES     a small combined view used by docs/tooling

Invariant (enforced by ``tests/test_curriculum.py``): every concept in
``LLM_FOUNDATION`` has an entry in both ``REFERENCE_LIBRARY`` and
``NOTEBOOK_FILES``, and every notebook filename exists on disk in ``labs/``.
"""

LessonMetadata = dict[str, list[str]]

# One to three canonical resources per lesson for deeper study.
# Preference order: original papers, official docs, then trusted explainers
# (Jay Alammar, Lilian Weng, Hugging Face, distill.pub).
REFERENCE_LIBRARY = {
    "Tokens": [
        "https://tiktokenizer.vercel.app/",
        "https://platform.openai.com/tokenizer",
        "https://github.com/openai/tiktoken",
    ],
    "Tokenization": [
        "https://huggingface.co/docs/transformers/main/en/tokenizer_summary",
        "https://huggingface.co/learn/nlp-course/chapter6/5",
        "https://www.youtube.com/watch?v=zduSFxRajkE",
    ],
    "Vocabulary": [
        "https://huggingface.co/docs/transformers/main/en/tokenizer_summary",
        "https://huggingface.co/docs/tokenizers/index",
    ],
    "Embeddings": [
        "https://jalammar.github.io/illustrated-word2vec/",
        "https://platform.openai.com/docs/guides/embeddings",
        "https://www.sbert.net/",
    ],
    "Semantic Space": [
        "https://jalammar.github.io/illustrated-word2vec/",
        "https://nlp.stanford.edu/projects/glove/",
    ],
    "Similarity": [
        "https://www.sbert.net/docs/usage/semantic_textual_similarity.html",
        "https://en.wikipedia.org/wiki/Cosine_similarity",
    ],
    "Language as Numbers": [
        "https://jalammar.github.io/illustrated-word2vec/",
        "https://distill.pub/2019/activation-atlas/",
    ],
    "Next Token Prediction": [
        "https://jalammar.github.io/how-gpt3-works-visualizations-animations/",
        "https://karpathy.github.io/2015/05/21/rnn-effectiveness/",
    ],
    "Attention": [
        "https://arxiv.org/abs/1706.03762",
        "https://jalammar.github.io/illustrated-transformer/",
        "https://lilianweng.github.io/posts/2018-06-24-attention/",
    ],
    "Self-Attention": [
        "https://jalammar.github.io/illustrated-transformer/",
        "https://nlp.seas.harvard.edu/annotated-transformer/",
    ],
    "Context Windows": [
        "https://huggingface.co/docs/transformers/main/en/llm_tutorial",
        "https://arxiv.org/abs/2307.03172",
    ],
    "Positional Encoding": [
        "https://jalammar.github.io/illustrated-transformer/",
        "https://kazemnejad.com/blog/transformer_architecture_positional_encoding/",
        "https://arxiv.org/abs/2104.09864",
    ],
    "Transformers": [
        "https://arxiv.org/abs/1706.03762",
        "https://jalammar.github.io/illustrated-transformer/",
        "https://huggingface.co/docs/transformers/index",
    ],
    "Information Flow": [
        "https://nlp.seas.harvard.edu/annotated-transformer/",
        "https://transformer-circuits.pub/2021/framework/index.html",
    ],
    "Pretraining": [
        "https://arxiv.org/abs/2005.14165",
        "https://jalammar.github.io/illustrated-bert/",
    ],
    "Loss Functions": [
        "https://www.deeplearningbook.org/contents/ml.html",
        "https://en.wikipedia.org/wiki/Cross-entropy",
    ],
    "Gradient Descent": [
        "https://www.3blue1brown.com/lessons/gradient-descent",
        "https://ruder.io/optimizing-gradient-descent/",
    ],
    "Parameters": [
        "https://jalammar.github.io/how-gpt3-works-visualizations-animations/",
        "https://huggingface.co/blog/large-language-models",
    ],
    "Scaling Laws": [
        "https://arxiv.org/abs/2001.08361",
        "https://arxiv.org/abs/2203.15556",
    ],
    "Emergent Abilities": [
        "https://arxiv.org/abs/2206.07682",
        "https://www.jasonwei.net/blog/emergence",
    ],
    "Learning Review": [
        "https://jalammar.github.io/illustrated-gpt2/",
        "https://huggingface.co/blog/large-language-models",
    ],
    "Hallucinations": [
        "https://arxiv.org/abs/2311.05232",
        "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    ],
    "Context Poisoning": [
        "https://arxiv.org/abs/2302.12173",
        "https://owasp.org/www-project-top-10-for-large-language-model-applications/",
    ],
    "Retrieval Failures": [
        "https://arxiv.org/abs/2005.11401",
        "https://arxiv.org/abs/2307.03172",
    ],
    "Goodhart's Law in AI": [
        "https://en.wikipedia.org/wiki/Goodhart%27s_law",
        "https://arxiv.org/abs/2210.10760",
    ],
    "Distribution Shift": [
        "https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html",
        "https://arxiv.org/abs/2107.03374",
    ],
    "Alignment": [
        "https://arxiv.org/abs/2203.02155",
        "https://openai.com/index/instruction-following/",
        "https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/",
    ],
    "Evaluation": [
        "https://arxiv.org/abs/2009.03300",
        "https://huggingface.co/blog/evaluating-llm-bias",
    ],
    "Prompt Engineering": [
        "https://www.promptingguide.ai/",
        "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview",
        "https://arxiv.org/abs/2201.11903",
    ],
    "Systems Thinking for AI": [
        "https://martinfowler.com/articles/engineering-practices-llm.html",
        "https://huyenchip.com/2023/04/11/llm-engineering.html",
    ],
}

# Notebook filenames (under labs/) that actually exist. Stored as bare
# filenames; professor.py turns them into clickable GitHub + Colab URLs.
# Keep this in sync with the real .ipynb files.
NOTEBOOK_FILES = {
    "Tokens": "01_tokens.ipynb",
    "Tokenization": "02_tokenization.ipynb",
    "Vocabulary": "03_vocabulary.ipynb",
    "Embeddings": "04_embeddings.ipynb",
    "Semantic Space": "05_semantic_space.ipynb",
    "Similarity": "06_similarity.ipynb",
    "Language as Numbers": "07_language_as_numbers.ipynb",
    "Next Token Prediction": "08_next_token_prediction.ipynb",
    "Attention": "09_attention.ipynb",
    "Self-Attention": "10_self_attention.ipynb",
    "Context Windows": "11_context_windows.ipynb",
    "Positional Encoding": "12_positional_encoding.ipynb",
    "Transformers": "13_transformers.ipynb",
    "Information Flow": "14_information_flow.ipynb",
    "Pretraining": "15_pretraining.ipynb",
    "Loss Functions": "16_loss_functions.ipynb",
    "Gradient Descent": "17_gradient_descent.ipynb",
    "Parameters": "18_parameters.ipynb",
    "Scaling Laws": "19_scaling_laws.ipynb",
    "Emergent Abilities": "20_emergent_abilities.ipynb",
    "Learning Review": "21_learning_review.ipynb",
    "Hallucinations": "22_hallucinations.ipynb",
    "Context Poisoning": "23_context_poisoning.ipynb",
    "Retrieval Failures": "24_retrieval_failures.ipynb",
    "Goodhart's Law in AI": "25_goodharts_law.ipynb",
    "Distribution Shift": "26_distribution_shift.ipynb",
    "Alignment": "27_alignment.ipynb",
    "Evaluation": "28_evaluation.ipynb",
    "Prompt Engineering": "29_prompt_engineering.ipynb",
    "Systems Thinking for AI": "30_systems_thinking.ipynb",
}

TOOLING = {
    "tiktoken": [
        "Token and tokenizer experimentation",
        "pip install tiktoken",
    ],
    "transformers": [
        "Model loading, generation, and fine-tuning demos",
        "pip install transformers accelerate",
    ],
    "sentence-transformers": [
        "Embeddings and semantic similarity",
        "pip install sentence-transformers",
    ],
    "faiss-cpu": [
        "Vector retrieval for RAG-style demos",
        "pip install faiss-cpu",
    ],
    "jupyterlab": [
        "Interactive notebook environment",
        "pip install jupyterlab",
    ],
}

LEARNING_NOTES = {
    "Tokens": {
        "references": REFERENCE_LIBRARY["Tokens"],
        "tools": ["tiktoken"],
        "notebook": NOTEBOOK_FILES["Tokens"],
    },
    "Tokenization": {
        "references": REFERENCE_LIBRARY["Tokenization"],
        "tools": ["tiktoken"],
        "notebook": NOTEBOOK_FILES["Tokenization"],
    },
    "Embeddings": {
        "references": REFERENCE_LIBRARY["Embeddings"],
        "tools": ["sentence-transformers", "transformers"],
        "notebook": NOTEBOOK_FILES["Embeddings"],
    },
    "Attention": {
        "references": REFERENCE_LIBRARY["Attention"],
        "tools": ["transformers"],
        "notebook": NOTEBOOK_FILES["Attention"],
    },
}
