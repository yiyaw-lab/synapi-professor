"""One-off generator for the first 10 lab notebooks.

Run once: `python labs/_generate.py`. Each notebook is built to *delight in
Colab*: an emoji hook, a "Run all" nudge, a quiet `pip install` cell so it runs
top-to-bottom with zero setup, a runnable demo, an exercise, and a closing
"🚀 Your move" cell that mirrors that concept's bold move from the curriculum.

Kept in the repo so the labs stay reproducible and reviewable.
"""

import json
import sys
from pathlib import Path

LABS = Path(__file__).parent
sys.path.insert(0, str(LABS.parent))

from curriculum.llm_foundation import LLM_FOUNDATION  # noqa: E402
from curriculum.lesson_metadata import NOTEBOOK_FILES  # noqa: E402

BOLD_MOVE = {lesson.concept: lesson.bold_move for lesson in LLM_FOUNDATION}


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text,
    }


def header(concept, emoji, hook):
    return md(
        f"# {emoji} {concept}\n\n"
        f"{hook}\n\n"
        "> ▶︎ In Colab: **Runtime → Run all** — this notebook runs top to bottom with no setup."
    )


def your_move(concept):
    return md(f"## 🚀 Your move\n\n{BOLD_MOVE[concept]}")


def notebook(*cells):
    return {
        "cells": list(cells),
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.10"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write(filename, nb):
    (LABS / filename).write_text(json.dumps(nb, indent=1) + "\n")


PIP_TIKTOKEN = code("%pip install -q tiktoken")
PIP_ST = code("%pip install -q sentence-transformers")
PIP_TRANSFORMERS = code("%pip install -q transformers torch")
# numpy ships with Colab, but install keeps local runs honest too.
PIP_NUMPY = code("%pip install -q numpy")


NOTEBOOKS = {
    "01_tokens.ipynb": notebook(
        header("Tokens", "🔤", "LLMs read tokens, not words. Let's see the pieces — and what they cost."),
        PIP_TIKTOKEN,
        code(
            "import tiktoken\n\n"
            "enc = tiktoken.get_encoding('cl100k_base')\n"
            "text = 'I love learning.'\n"
            "ids = enc.encode(text)\n"
            "print('Text:', text)\n"
            "print('Token IDs:', ids)\n"
            "print('Pieces:', [enc.decode([t]) for t in ids])"
        ),
        md("## Try it\n\nGuess how each phrase splits, then run it. Then peek at the cost."),
        code(
            "for phrase in ['cat', 'concatenate', 'antidisestablishmentarianism']:\n"
            "    ids = enc.encode(phrase)\n"
            "    print(phrase, '->', [enc.decode([t]) for t in ids])\n\n"
            "# rough cost: GPT-4o input ~ $2.50 / 1M tokens\n"
            "doc = 'token economics ' * 200\n"
            "n = len(enc.encode(doc))\n"
            "print(f'\\n{n} tokens  ~  $' + format(n / 1_000_000 * 2.50, '.6f') + ' to send once')"
        ),
        md("## Takeaway\n\n- A 'word' is often several tokens.\n- Token count *is* the bill and the context limit."),
        your_move("Tokens"),
    ),
    "02_tokenization.ipynb": notebook(
        header("Tokenization", "🔪", "Why words get chopped into sub-word pieces — and who pays for it."),
        PIP_TIKTOKEN,
        code(
            "import tiktoken\n\n"
            "enc = tiktoken.get_encoding('cl100k_base')\n"
            "for word in ['believable', 'unbelievable', 'unbelievably']:\n"
            "    ids = enc.encode(word)\n"
            "    print(f'{word:16s} {len(ids)} tokens -> {[enc.decode([t]) for t in ids]}')"
        ),
        md("## Try it\n\nThe SAME sentence costs more tokens in some languages. Watch the gap."),
        code(
            "pairs = {\n"
            "    'English': 'The cat sleeps on the warm windowsill.',\n"
            "    'Hindi':   'बिल्ली गर्म खिड़की पर सोती है।',\n"
            "    'Thai':    'แมวนอนอยู่บนขอบหน้าต่างที่อบอุ่น',\n"
            "}\n"
            "for lang, s in pairs.items():\n"
            "    print(f'{lang:8s} {len(enc.encode(s)):3d} tokens')"
        ),
        md("## Takeaway\n\n- Common strings get one token; rare ones get many.\n- Tokenizer choices decide whose language is cheap."),
        your_move("Tokenization"),
    ),
    "03_vocabulary.ipynb": notebook(
        header("Vocabulary", "🧱", "Every input is built from a fixed box of token bricks."),
        PIP_TIKTOKEN,
        code(
            "import tiktoken\n\n"
            "enc = tiktoken.get_encoding('cl100k_base')\n"
            "print('Vocabulary size:', enc.n_vocab)"
        ),
        md("## Try it\n\nSee how out-of-the-ordinary input fragments into many pieces."),
        code(
            "for s in ['Zbigniew', 'teh', '🦄', 'def f(x): return x**2']:\n"
            "    ids = enc.encode(s)\n"
            "    print(repr(s), '->', len(ids), 'tokens:', [enc.decode([t]) for t in ids])"
        ),
        md("## Takeaway\n\n- Rare names, typos, emoji, and code cost extra tokens.\n- Nothing is truly 'unknown' — it is spelled out in pieces."),
        your_move("Vocabulary"),
    ),
    "04_embeddings.ipynb": notebook(
        header("Embeddings", "📍", "Tokens become vectors — coordinates on a map of meaning."),
        PIP_ST,
        code(
            "from sentence_transformers import SentenceTransformer\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "vecs = model.encode(['king', 'queen', 'banana'])\n"
            "print('Vector dimension:', vecs.shape[1])\n"
            "print('First 5 dims of king:', vecs[0][:5])"
        ),
        md("## Try it\n\nBuild a tiny semantic search: which sentence is closest to your query?"),
        code(
            "from sentence_transformers import util\n"
            "corpus = ['The cat naps in the sun.', 'Quantum computers use qubits.',\n"
            "          'I love a strong espresso.', 'The dog chased the ball.']\n"
            "q = 'a sleepy kitten'\n"
            "scores = util.cos_sim(model.encode(q), model.encode(corpus))[0]\n"
            "best = int(scores.argmax())\n"
            "print('Query:', q)\n"
            "print('Closest:', corpus[best], f'({float(scores[best]):.3f})')"
        ),
        md("## Takeaway\n\n- Each word/sentence maps to a list of numbers.\n- Those numbers power every RAG and search product."),
        your_move("Embeddings"),
    ),
    "05_semantic_space.ipynb": notebook(
        header("Semantic Space", "🌌", "Meanings live as positions; related ideas orbit close."),
        PIP_ST,
        code(
            "from sentence_transformers import SentenceTransformer, util\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "anchor = 'school'\n"
            "words = ['teacher', 'student', 'exam', 'classroom', 'banana', 'rocket']\n"
            "scores = util.cos_sim(model.encode(anchor), model.encode(words))[0]\n"
            "for w, s in sorted(zip(words, scores), key=lambda x: -x[1]):\n"
            "    print(f'{w:10s} {float(s):.3f}')"
        ),
        md("## Try it\n\nChange the anchor to your own word and re-run. Where does 'banana' land now?"),
        code("anchor = 'ocean'  # <- change me\nwords = ['wave', 'salt', 'whale', 'desert', 'guitar']\n"
             "for w, s in sorted(zip(words, util.cos_sim(model.encode(anchor), model.encode(words))[0]), key=lambda x: -x[1]):\n"
             "    print(f'{w:10s} {float(s):.3f}')"),
        md("## Takeaway\n\n- Distance tracks relatedness.\n- 'banana' and 'rocket' fall far from 'school'."),
        your_move("Semantic Space"),
    ),
    "06_similarity.ipynb": notebook(
        header("Similarity", "🧲", "Models compare vectors to judge how related two things are."),
        PIP_ST,
        code(
            "from sentence_transformers import SentenceTransformer, util\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "pairs = [('doctor', 'hospital'), ('doctor', 'banana'), ('happy', 'joyful')]\n"
            "for a, b in pairs:\n"
            "    s = util.cos_sim(model.encode(a), model.encode(b))[0][0]\n"
            "    print(f'{a:8s} ~ {b:8s} = {float(s):.3f}')"
        ),
        md("## Try it\n\nCan you find a pair that means the OPPOSITE but scores HIGH? (This is the famous trap.)"),
        code(
            "tricky = [('I love this', 'I hate this'), ('hot', 'cold'), ('always', 'never')]\n"
            "for a, b in tricky:\n"
            "    print(f'{a:14s} ~ {b:14s} = {float(util.cos_sim(model.encode(a), model.encode(b))[0][0]):.3f}')"
        ),
        md("## Takeaway\n\n- Cosine similarity: higher = more related.\n- Opposites can score high — similarity is not meaning."),
        your_move("Similarity"),
    ),
    "07_language_as_numbers.ipynb": notebook(
        header("Language as Numbers", "🔢", "A whole sentence collapses into a fixed list of numbers."),
        PIP_ST,
        code(
            "from sentence_transformers import SentenceTransformer\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "v = model.encode('Poetry translated into coordinates.')\n"
            "print('Dimensions:', len(v))\n"
            "print('First 10 numbers:', [round(float(x), 3) for x in v[:10]])"
        ),
        md("## Try it\n\nTwo different sentences, same idea. How close are their numbers?"),
        code(
            "from sentence_transformers import util\n"
            "a = model.encode('The cat sat on the mat.')\n"
            "b = model.encode('A feline rested on the rug.')\n"
            "print('similarity:', round(float(util.cos_sim(a, b)[0][0]), 3))"
        ),
        md("## Takeaway\n\n- Meaning is compressed, not perfectly preserved.\n- Paraphrases land near each other in the space."),
        your_move("Language as Numbers"),
    ),
    "08_next_token_prediction.ipynb": notebook(
        header("Next Token Prediction", "🔮", "The whole game: predict the next token from the ones before."),
        PIP_TRANSFORMERS,
        code(
            "from transformers import pipeline\n\n"
            "gen = pipeline('text-generation', model='distilgpt2')\n"
            "out = gen('The capital of France is', max_new_tokens=5, do_sample=False)\n"
            "print(out[0]['generated_text'])"
        ),
        md("## Try it\n\nPredict each continuation yourself BEFORE running. Score yourself."),
        code(
            "for prompt in ['Once upon a', '2 + 2 =', 'The opposite of hot is']:\n"
            "    print(prompt, '=>', gen(prompt, max_new_tokens=4, do_sample=False)[0]['generated_text'])"
        ),
        md("## Takeaway\n\n- Generation is repeated next-token prediction.\n- A tiny model shows the same mechanism as the giants."),
        your_move("Next Token Prediction"),
    ),
    "09_attention.ipynb": notebook(
        header("Attention", "👁️", "Attention decides which tokens matter for the current one."),
        PIP_NUMPY,
        code(
            "import numpy as np\n\n"
            "def softmax(x):\n"
            "    e = np.exp(x - x.max())\n"
            "    return e / e.sum()\n\n"
            "# toy 'scores' of how much a query token relates to 4 context tokens\n"
            "scores = np.array([2.0, 0.1, 1.0, -1.0])\n"
            "weights = softmax(scores)\n"
            "print('Attention weights:', np.round(weights, 3))\n"
            "print('They sum to:', round(float(weights.sum()), 3))"
        ),
        md("## Try it\n\nChange the scores and watch attention concentrate or spread."),
        code(
            "tokens = ['the', 'animal', 'street', 'tired']\n"
            "for tok, w in zip(tokens, weights):\n"
            "    print(f'{tok:8s} {w:.3f} ' + '#' * int(w * 40))"
        ),
        md("## Takeaway\n\n- Softmax turns raw scores into weights that sum to 1.\n- Attention is a weighted average over context."),
        your_move("Attention"),
    ),
    "10_self_attention.ipynb": notebook(
        header("Self-Attention", "🪞", "Every token attends to every other token and updates its meaning."),
        PIP_NUMPY,
        code(
            "import numpy as np\n\n"
            "def softmax(x):\n"
            "    e = np.exp(x - x.max(axis=-1, keepdims=True))\n"
            "    return e / e.sum(axis=-1, keepdims=True)\n\n"
            "np.random.seed(0)\n"
            "# 4 tokens, each a 3-dim vector\n"
            "X = np.random.randn(4, 3)\n"
            "scores = X @ X.T          # every token scored against every token\n"
            "attn = softmax(scores)    # row i = how token i attends to all tokens\n"
            "out = attn @ X            # updated representations\n"
            "print('Attention matrix:\\n', np.round(attn, 2))\n"
            "print('Updated token 0:', np.round(out[0], 3))"
        ),
        md("## Try it\n\nWhich token does each one attend to most? (Watch the O(n²) comparison happen.)"),
        code(
            "for i, row in enumerate(attn):\n"
            "    print(f'token {i} attends most to token {int(row.argmax())} ({row.max():.2f})')"
        ),
        md("## Takeaway\n\n- Self-attention is a full token-to-token comparison.\n- That n×n cost is the wall every fast-attention method fights."),
        your_move("Self-Attention"),
    ),
}


def main():
    # Sanity: every notebook we emit must be registered in NOTEBOOK_FILES,
    # and every registered file must be produced here. Keeps message links honest.
    produced = set(NOTEBOOKS)
    registered = set(NOTEBOOK_FILES.values())
    assert produced == registered, (
        f"mismatch: only-here={produced - registered}, only-registered={registered - produced}"
    )
    # Remove the superseded original notebook if present.
    old = LABS / "01_tokenization.ipynb"
    if old.exists():
        old.unlink()
    for name, nb in NOTEBOOKS.items():
        write(name, nb)
    print(f"Wrote {len(NOTEBOOKS)} notebooks to {LABS}")


if __name__ == "__main__":
    main()
