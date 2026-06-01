from typing import Dict, List

LessonMetadata = Dict[str, List[str]]

REFERENCE_LIBRARY = {
    "Tokens": [
        "https://github.com/openai/tiktoken",
        "https://platform.openai.com/docs/guides/chat/introduction",
        "https://www.freecodecamp.org/news/tokenization-in-natural-language-processing/",
    ],
    "Tokenization": [
        "https://github.com/openai/tiktoken",
        "https://huggingface.co/docs/tokenizers/index",
        "https://jalammar.github.io/illustrated-tokenization/",
    ],
    "Vocabulary": [
        "https://huggingface.co/docs/transformers/main/en/tokenizer_summary",
        "https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/",
    ],
    "Embeddings": [
        "https://www.sbert.net/",
        "https://platform.openai.com/docs/guides/embeddings",
        "https://www.tensorflow.org/text/guide/word_embeddings",
    ],
    "Semantic Space": [
        "https://towardsdatascience.com/semantic-spaces-in-machine-learning-8e9a6aea8db7",
        "https://sebastianraschka.com/blog/2020/semantic-vector-space.html",
    ],
    "Similarity": [
        "https://www.sbert.net/docs/pretrained_models.html",
        "https://towardsdatascience.com/cosine-similarity-explained-2c1f4f7b6d0a",
    ],
    "Next Token Prediction": [
        "https://jalammar.github.io/illustrated-transformer/",
        "https://www.fast.ai/2020/07/09/what-is-a-transformer/",
    ],
    "Attention": [
        "https://www.analyticsvidhya.com/blog/2020/10/illustrated-self-attention/",
        "https://arxiv.org/abs/1706.03762",
    ],
    "Self-Attention": [
        "https://jalammar.github.io/illustrated-transformer/",
        "https://towardsdatascience.com/transformer-self-attention-and-the-residual-connection-44f34527bb1a",
    ],
    "Context Windows": [
        "https://www.eleuther.ai/blog/context-windows/",
        "https://huggingface.co/blog/what-is-context-length",
    ],
    "Transformers": [
        "https://arxiv.org/abs/1706.03762",
        "https://huggingface.co/docs/transformers/index",
    ],
    "Pretraining": [
        "https://www.deeplearningbook.org/",
        "https://openai.com/research/language-models-are-few-shot-learners",
    ],
    "Hallucinations": [
        "https://www.microsoft.com/en-us/research/project/risks/",
        "https://www.fast.ai/2023/07/24/stop-the-system-prompt/",
    ],
    "Retrieval Failures": [
        "https://www.assemblyai.com/blog/rag-retrieval-augmented-generation/",
        "https://www.reddit.com/r/MachineLearning/comments/",
    ],
    "Prompt Engineering": [
        "https://platform.openai.com/docs/guides/chat/completions-api",
        "https://www.promptingguide.ai/",
    ],
    "Alignment": [
        "https://www.alignmentforum.org/",
        "https://www.lesswrong.com/",
    ],
}

NOTEBOOK_LINKS = {
    "Tokenization": "../labs/01_tokenization.ipynb",
    "Embeddings": "../labs/02_embeddings.ipynb",
    "Attention": "../labs/03_attention.ipynb",
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
