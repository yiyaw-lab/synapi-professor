"""One-off generator for the first 10 lab notebooks.

Run once: `python labs/_generate.py`. Each notebook mirrors the style of the
original tokenization lab: a title, a runnable demo, an exercise, and a
takeaway. Kept in the repo so the labs are reproducible and reviewable.
"""

import json
from pathlib import Path

LABS = Path(__file__).parent


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


NOTEBOOKS = {
    "01_tokens.ipynb": notebook(
        md("# Lab 1: Tokens\n\nLLMs read tokens, not words. See what the pieces actually look like."),
        code(
            "import tiktoken\n\n"
            "enc = tiktoken.get_encoding('cl100k_base')\n"
            "text = 'I love learning.'\n"
            "ids = enc.encode(text)\n"
            "print('Text:', text)\n"
            "print('Token IDs:', ids)\n"
            "print('Pieces:', [enc.decode([t]) for t in ids])"
        ),
        md("## Exercise\n\nGuess how each phrase splits, then run it."),
        code(
            "for phrase in ['cat', 'concatenate', 'antidisestablishmentarianism']:\n"
            "    ids = enc.encode(phrase)\n"
            "    print(phrase, '->', [enc.decode([t]) for t in ids])"
        ),
        md("## Takeaway\n\n- A 'word' is often several tokens.\n- Token count drives cost and context limits."),
    ),
    "02_tokenization.ipynb": notebook(
        md("# Lab 2: Tokenization\n\nWhy words get chopped into sub-word pieces."),
        code(
            "import tiktoken\n\n"
            "enc = tiktoken.get_encoding('cl100k_base')\n"
            "for word in ['believable', 'unbelievable', 'unbelievably']:\n"
            "    ids = enc.encode(word)\n"
            "    print(f'{word:16s} {len(ids)} tokens -> {[enc.decode([t]) for t in ids]}')"
        ),
        md("## Exercise\n\nFind a long word that is a single token, and a short one that is several."),
        code(
            "tests = ['the', ' the', 'hello', 'GPT', 'asdfqwer', '日本語']\n"
            "for t in tests:\n"
            "    ids = enc.encode(t)\n"
            "    print(repr(t), '->', len(ids), 'tokens')"
        ),
        md("## Takeaway\n\n- Common strings get one token; rare ones get many.\n- Leading spaces and case change the split."),
    ),
    "03_vocabulary.ipynb": notebook(
        md("# Lab 3: Vocabulary\n\nEvery input is built from a fixed box of token pieces."),
        code(
            "import tiktoken\n\n"
            "enc = tiktoken.get_encoding('cl100k_base')\n"
            "print('Vocabulary size:', enc.n_vocab)"
        ),
        md("## Exercise\n\nSee how out-of-the-ordinary input fragments into many pieces."),
        code(
            "for s in ['Zbigniew', 'teh', '🦄', 'supercalifragilistic']:\n"
            "    ids = enc.encode(s)\n"
            "    print(repr(s), '->', len(ids), 'tokens:', [enc.decode([t]) for t in ids])"
        ),
        md("## Takeaway\n\n- Rare names, typos, and emoji cost extra tokens.\n- Nothing is truly 'unknown' — it is just spelled out in pieces."),
    ),
    "04_embeddings.ipynb": notebook(
        md("# Lab 4: Embeddings\n\nTokens become vectors that capture meaning.\n\n_Requires: `pip install sentence-transformers`_"),
        code(
            "from sentence_transformers import SentenceTransformer\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "vecs = model.encode(['king', 'queen', 'banana'])\n"
            "print('Vector dimension:', vecs.shape[1])\n"
            "print('First 5 dims of king:', vecs[0][:5])"
        ),
        md("## Exercise\n\nEmbed words of your choice and inspect the shapes."),
        code(
            "words = ['paris', 'france', 'tokyo', 'sushi']\n"
            "vecs = model.encode(words)\n"
            "for w, v in zip(words, vecs):\n"
            "    print(f'{w:8s} -> dim {len(v)}, norm {float((v**2).sum()**0.5):.3f}')"
        ),
        md("## Takeaway\n\n- Each token/word maps to a list of numbers.\n- Those numbers encode learned patterns of meaning."),
    ),
    "05_semantic_space.ipynb": notebook(
        md("# Lab 5: Semantic Space\n\nMeanings live as positions; related ideas sit closer."),
        code(
            "from sentence_transformers import SentenceTransformer, util\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "anchor = 'school'\n"
            "words = ['teacher', 'student', 'exam', 'classroom', 'banana', 'rocket']\n"
            "av = model.encode(anchor)\n"
            "wv = model.encode(words)\n"
            "scores = util.cos_sim(av, wv)[0]\n"
            "for w, s in sorted(zip(words, scores), key=lambda x: -x[1]):\n"
            "    print(f'{w:10s} {float(s):.3f}')"
        ),
        md("## Exercise\n\nPick your own anchor word and rank a list around it."),
        code("# your turn: change `anchor` and `words` above and re-run"),
        md("## Takeaway\n\n- Distance in the space tracks relatedness.\n- 'banana' and 'rocket' fall far from 'school'."),
    ),
    "06_similarity.ipynb": notebook(
        md("# Lab 6: Similarity\n\nModels compare vectors to judge how related two things are."),
        code(
            "from sentence_transformers import SentenceTransformer, util\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "pairs = [('doctor', 'hospital'), ('doctor', 'banana'), ('happy', 'joyful')]\n"
            "for a, b in pairs:\n"
            "    s = util.cos_sim(model.encode(a), model.encode(b))[0][0]\n"
            "    print(f'{a:8s} ~ {b:8s} = {float(s):.3f}')"
        ),
        md("## Exercise\n\nFind a pair of different words with high similarity, and a similar-looking pair with low similarity."),
        code("# your turn: add pairs to the list above"),
        md("## Takeaway\n\n- Cosine similarity ranges roughly -1..1; higher = more related.\n- Different words can be close in meaning."),
    ),
    "07_language_as_numbers.ipynb": notebook(
        md("# Lab 7: Language as Numbers\n\nA sentence becomes a fixed-length vector of numbers."),
        code(
            "from sentence_transformers import SentenceTransformer\n\n"
            "model = SentenceTransformer('all-MiniLM-L6-v2')\n"
            "v = model.encode('Poetry translated into coordinates.')\n"
            "print('Dimensions:', len(v))\n"
            "print('First 10 numbers:', [round(float(x), 3) for x in v[:10]])"
        ),
        md("## Exercise\n\nEmbed two paraphrases of the same idea and compare their vectors."),
        code(
            "from sentence_transformers import util\n"
            "a = model.encode('The cat sat on the mat.')\n"
            "b = model.encode('A feline rested on the rug.')\n"
            "print('similarity:', float(util.cos_sim(a, b)[0][0]))"
        ),
        md("## Takeaway\n\n- Meaning is compressed, not perfectly preserved.\n- Paraphrases land near each other in the space."),
    ),
    "08_next_token_prediction.ipynb": notebook(
        md("# Lab 8: Next Token Prediction\n\nThe core task: predict the next token from the previous ones.\n\n_Requires: `pip install transformers torch`_"),
        code(
            "from transformers import pipeline\n\n"
            "gen = pipeline('text-generation', model='distilgpt2')\n"
            "out = gen('The capital of France is', max_new_tokens=5, do_sample=False)\n"
            "print(out[0]['generated_text'])"
        ),
        md("## Exercise\n\nBefore running, predict the continuation yourself, then compare."),
        code(
            "for prompt in ['Once upon a', '2 + 2 =', 'The opposite of hot is']:\n"
            "    print(prompt, '=>', gen(prompt, max_new_tokens=4, do_sample=False)[0]['generated_text'])"
        ),
        md("## Takeaway\n\n- Generation is repeated next-token prediction.\n- Small models are weaker but show the same mechanism."),
    ),
    "09_attention.ipynb": notebook(
        md("# Lab 9: Attention\n\nAttention decides which tokens matter for the current one."),
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
        md("## Exercise\n\nChange the scores and watch where attention concentrates."),
        code(
            "tokens = ['the', 'animal', 'street', 'tired']\n"
            "for tok, w in zip(tokens, weights):\n"
            "    print(f'{tok:8s} {w:.3f} ' + '#' * int(w * 40))"
        ),
        md("## Takeaway\n\n- Softmax turns raw scores into weights that sum to 1.\n- Attention is a weighted average over context."),
    ),
    "10_self_attention.ipynb": notebook(
        md("# Lab 10: Self-Attention\n\nEvery token attends to every other token and updates its meaning."),
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
        md("## Exercise\n\nInspect which token each row attends to most."),
        code(
            "for i, row in enumerate(attn):\n"
            "    print(f'token {i} attends most to token {int(row.argmax())} ({row.max():.2f})')"
        ),
        md("## Takeaway\n\n- Self-attention is a full token-to-token comparison.\n- Each output token is a mix of all the others."),
    ),
}


def main():
    # Remove the superseded original notebook if present.
    old = LABS / "01_tokenization.ipynb"
    if old.exists():
        old.unlink()
    for name, nb in NOTEBOOKS.items():
        write(name, nb)
    print(f"Wrote {len(NOTEBOOKS)} notebooks to {LABS}")


if __name__ == "__main__":
    main()
