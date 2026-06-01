from typing import Dict, List

LessonMetadata = Dict[str, List[str]]

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

# Notebook files that actually exist under labs/. Keep this in sync with the
# real .ipynb files; concepts without an entry fall back to HANDS_ON only.
NOTEBOOK_LINKS = {
    "Tokens": "../labs/01_tokens.ipynb",
    "Tokenization": "../labs/02_tokenization.ipynb",
    "Vocabulary": "../labs/03_vocabulary.ipynb",
    "Embeddings": "../labs/04_embeddings.ipynb",
    "Semantic Space": "../labs/05_semantic_space.ipynb",
    "Similarity": "../labs/06_similarity.ipynb",
    "Language as Numbers": "../labs/07_language_as_numbers.ipynb",
    "Next Token Prediction": "../labs/08_next_token_prediction.ipynb",
    "Attention": "../labs/09_attention.ipynb",
    "Self-Attention": "../labs/10_self_attention.ipynb",
}

# A short, runnable hands-on for every lesson. Each is a self-contained
# snippet or a concrete pen-and-paper prompt so a learner always has
# something to *do*, even when no notebook exists for the concept.
HANDS_ON = {
    "Tokens": (
        "Run: `import tiktoken; enc=tiktoken.get_encoding('cl100k_base'); "
        "print([enc.decode([t]) for t in enc.encode('I love learning.')])` "
        "and see the pieces."
    ),
    "Tokenization": (
        "Tokenize 'unbelievable' vs 'believable' with tiktoken and compare "
        "how many pieces each becomes."
    ),
    "Vocabulary": (
        "Encode a rare name, a typo, and an emoji with tiktoken; count the "
        "tokens each needs and note which fragment the most."
    ),
    "Embeddings": (
        "Use sentence-transformers to embed 'king', 'queen', 'banana' and "
        "print the vector lengths and first few dimensions."
    ),
    "Semantic Space": (
        "Embed five words around a theme (e.g. school, teacher, student, "
        "exam, banana) and rank them by distance from 'school'."
    ),
    "Similarity": (
        "Compute cosine similarity between 'doctor'/'hospital' and "
        "'doctor'/'banana' with sentence-transformers; compare the scores."
    ),
    "Language as Numbers": (
        "Embed one sentence, print its vector, then write one sentence on "
        "what meaning survives the conversion and what is lost."
    ),
    "Next Token Prediction": (
        "Give a model the prompt 'The capital of France is' and predict the "
        "next token yourself before checking; note your confidence."
    ),
    "Attention": (
        "On paper, in 'The trophy didn't fit in the suitcase because it was "
        "too big,' draw an arrow from 'it' to the word it attends to."
    ),
    "Self-Attention": (
        "Repeat the arrow exercise for 'because it was too small' and "
        "explain why the same word 'it' now points elsewhere."
    ),
    "Context Windows": (
        "Count the tokens in a long document with tiktoken; identify what "
        "would be dropped if the window held only the first half."
    ),
    "Positional Encoding": (
        "Write 'dog bites man' and 'man bites dog'; explain in one line why "
        "identical tokens in different positions mean different things."
    ),
    "Transformers": (
        "Sketch the data path of one token through a transformer block: "
        "embed -> attention -> feed-forward -> next layer."
    ),
    "Information Flow": (
        "Pick an ambiguous word and write how its meaning sharpens after "
        "the model reads two more surrounding sentences."
    ),
    "Pretraining": (
        "List five facts you think a model could learn purely from reading "
        "text, and one it could not."
    ),
    "Loss Functions": (
        "By hand, compute cross-entropy loss for a 3-class prediction "
        "[0.7, 0.2, 0.1] when the true class is the second one."
    ),
    "Gradient Descent": (
        "Minimize f(x)=x**2 by hand: start at x=4 and take three steps of "
        "x = x - 0.1*(2x); watch it approach zero."
    ),
    "Parameters": (
        "Estimate parameters in a single linear layer of size 1024x1024 "
        "(weights + biases); compare to a billion-parameter model."
    ),
    "Scaling Laws": (
        "Read the Chinchilla abstract and write the rule of thumb for how "
        "data should grow with model size, in one sentence."
    ),
    "Emergent Abilities": (
        "Name one task small models fail at but large ones suddenly do; "
        "argue whether it is truly 'emergent' or just better measured."
    ),
    "Learning Review": (
        "In one paragraph, explain pretraining, loss, and parameters to a "
        "friend who has never heard of machine learning."
    ),
    "Hallucinations": (
        "Ask a model for a citation on an obscure topic and verify whether "
        "the source actually exists."
    ),
    "Context Poisoning": (
        "Write a short factual prompt, then prepend one false 'fact'; note "
        "how the answer shifts to follow the planted claim."
    ),
    "Retrieval Failures": (
        "Describe a query where the right document exists but keyword search "
        "would miss it; suggest one fix."
    ),
    "Goodhart's Law in AI": (
        "Pick a metric (e.g. answer length) and describe how optimizing it "
        "could make answers worse while the score climbs."
    ),
    "Distribution Shift": (
        "List two inputs unlike normal training text (slang, a new format) "
        "and predict where the model would stumble."
    ),
    "Alignment": (
        "Write one request that is easy to answer helpfully but should be "
        "refused or reframed; explain why helpfulness alone is not enough."
    ),
    "Evaluation": (
        "Design one question whose correct answer cannot be produced by "
        "paraphrasing the prompt, separating recall from understanding."
    ),
    "Prompt Engineering": (
        "Take a vague prompt ('write about dogs') and rewrite it with a "
        "role, goal, constraints, and an output format."
    ),
    "Systems Thinking for AI": (
        "Map one AI product as a system: model, data, user, interface, "
        "feedback loop, and one failure mode for each."
    ),
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
        "notebook": NOTEBOOK_LINKS["Tokenization"],
    },
    "Tokenization": {
        "references": REFERENCE_LIBRARY["Tokenization"],
        "tools": ["tiktoken"],
        "notebook": NOTEBOOK_LINKS["Tokenization"],
    },
    "Embeddings": {
        "references": REFERENCE_LIBRARY["Embeddings"],
        "tools": ["sentence-transformers", "transformers"],
        "notebook": NOTEBOOK_LINKS["Embeddings"],
    },
    "Attention": {
        "references": REFERENCE_LIBRARY["Attention"],
        "tools": ["transformers"],
        "notebook": NOTEBOOK_LINKS["Attention"],
    },
}
