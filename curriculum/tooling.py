"""Recommended tools for running the labs locally.

Reference data for humans (and the README), not used by the daily sender. The
labs install what they need at run time via ``%pip`` when opened in Colab, so
this list matters only if you prefer to run the notebooks on your own machine.
``RECOMMENDED_TOOLING`` describes each library; ``RECOMMENDED_COMMANDS`` is a
copy-paste setup sequence.
"""

Tool = dict[str, str]

RECOMMENDED_TOOLING: list[Tool] = [
    {
        "name": "Python 3.10+",
        "purpose": "Runtime for notebooks and examples.",
        "install": "https://www.python.org/downloads/",
    },
    {
        "name": "jupyterlab",
        "purpose": "Interactive notebook environment for labs.",
        "install": "pip install jupyterlab",
    },
    {
        "name": "tiktoken",
        "purpose": "Tokenization experiments and token-counting.",
        "install": "pip install tiktoken",
    },
    {
        "name": "transformers",
        "purpose": "Transformer model loading, generation, and fine-tuning demos.",
        "install": "pip install transformers accelerate",
    },
    {
        "name": "sentence-transformers",
        "purpose": "Embeddings, semantic search, and similarity evaluation.",
        "install": "pip install sentence-transformers",
    },
    {
        "name": "faiss-cpu",
        "purpose": "Vector retrieval for RAG-style retrieval demos.",
        "install": "pip install faiss-cpu",
    },
    {
        "name": "python-dotenv",
        "purpose": "Manage local environment variables for API keys and config.",
        "install": "pip install python-dotenv",
    },
]

RECOMMENDED_COMMANDS = [
    "pip install -r requirements.txt",
    "pip install jupyterlab tiktoken transformers accelerate sentence-transformers faiss-cpu",
    "jupyter lab",
]
