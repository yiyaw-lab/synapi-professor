from typing import List, Dict

Tool = Dict[str, str]

RECOMMENDED_TOOLING: List[Tool] = [
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
