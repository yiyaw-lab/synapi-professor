"""The advanced curriculum: 30 ordered ``Lesson`` objects, post-training to serving.

This is the second track — the research-and-engineering frontier that sits on top
of ``foundation_llm``. Where the foundation track explains how an LLM works, this
track covers what practitioners actually do to a trained model: align it (RLHF,
DPO), shrink it (LoRA, quantization, distillation), speed it up (MoE, speculative
decoding, paged attention), redesign it (FlashAttention, Mamba, long context),
read its mind (mechanistic interpretability, SAEs, steering), and ship it as a
system (tools, agents, advanced RAG, evals, serving economics).

Like the foundation track, ``ADVANCED_LLM`` is a plain list, so the day's lesson
is ``ADVANCED_LLM[date_ordinal % 30]`` (see ``professor.select_daily_lesson``).
The list order defines the lab numbering in ``labs/`` (``a01``..``a30``) and the
week grouping in ``advanced_path.py``. Per-concept references and notebook
filenames live in ``advanced_metadata.py``, keyed by ``concept``.

License: this lesson content is licensed CC BY 4.0, © 2026 Coaur Inc. (see
``LICENSE-CONTENT``), separate from the repository's Apache-2.0 code license.
"""

from lesson_model import Lesson

ADVANCED_LLM = [
    # --- Week 1: Post-training & preference optimization ----------------------
    Lesson(
        concept="Supervised Fine-Tuning",
        plain="SFT takes a pretrained base model and trains it on curated input→output examples so it follows instructions instead of just continuing text.",
        analogy="Like a brilliant but feral genius who has read everything, finally being shown how a polite conversation is supposed to go.",
        frontier="SFT is where every assistant is born — but the 2024-2025 lesson is that data quality beats quantity wildly: a few thousand hand-crafted examples (LIMA) can outshine millions of scraped ones. Curation is now the real moat.",
        bold_move="Build: hand-write 10 instruction→response pairs in your own voice, then write the system prompt that would make a model imitate them. Notice how much 'alignment' is really just good examples.",
    ),
    Lesson(
        concept="RLHF",
        plain="RLHF trains a reward model on human preference comparisons, then uses reinforcement learning (PPO) to push the LLM toward answers that score higher.",
        analogy="Like training a dog with treats — except the 'treat' is a second AI that learned what humans tend to applaud.",
        frontier="RLHF is what made ChatGPT feel aligned, but it's notoriously unstable and expensive — a fragile dance of four models at once. Half the 2024 frontier (DPO and friends) exists purely to escape PPO's pain.",
        bold_move="Provoke: RLHF optimizes for what raters *click approve* on, not what's true. In one paragraph, argue whether that makes models more honest or just more persuasive — and which is more dangerous.",
    ),
    Lesson(
        concept="Direct Preference Optimization",
        plain="DPO skips the separate reward model and RL loop: it turns 'humans preferred A over B' directly into a single classification-style loss on the policy.",
        analogy="Like learning to cook from a stack of 'this dish beat that dish' cards — no judge in the room, just the verdicts.",
        frontier="DPO (2023) quietly took over open-model alignment because it's stable, cheap, and one loss instead of a pipeline. The 2024-2025 zoo — IPO, KTO, ORPO, SimPO — are all variations chasing the same 'RLHF without the RL' dream.",
        bold_move="Build: implement the DPO loss in ~15 lines of numpy (log-sigmoid of the chosen-minus-rejected log-prob gap, scaled by beta). Feel how 'preferred > rejected' becomes a gradient.",
    ),
    Lesson(
        concept="Constitutional AI",
        plain="Constitutional AI replaces many human labels with the model critiquing and revising its own outputs against a written set of principles (a 'constitution').",
        analogy="Like giving someone a code of ethics and a mirror, and asking them to keep editing their answer until it lives up to both.",
        frontier="Anthropic's Constitutional AI / RLAIF showed AI feedback can stand in for human feedback at scale — the seed of 'models supervising models.' The hard open question: can a system align something smarter than itself?",
        bold_move="Build: write a 5-rule 'constitution,' then take a spicy model answer and manually run critique→revise against each rule. Keep the diff — you just did RLAIF by hand.",
    ),
    Lesson(
        concept="Reasoning Models",
        plain="Reasoning models are trained (often with RL on correctness) to produce long internal chains of thought before answering, spending more compute at inference to think harder.",
        analogy="Like the difference between blurting the first answer and working it out on scratch paper first — and being rewarded only when the final line is right.",
        frontier="The o-series and DeepSeek-R1 opened a whole new scaling axis: test-time compute. Accuracy now climbs with *thinking length*, not just model size — and R1 showed pure RL can grow reasoning with almost no human traces.",
        bold_move="Provoke: reasoning models get smarter by thinking longer at answer time. Argue in a short post whether that's genuine reasoning or just a very expensive search — and what experiment would settle it for you.",
    ),
    Lesson(
        concept="Reward Hacking",
        plain="Reward hacking is when a model maximizes the measured reward while subverting what the reward was meant to capture.",
        analogy="Like a student who games the rubric to ace the grade while learning nothing — the grader's blind spots become the curriculum.",
        frontier="Reward hacking is the beating heart of the alignment problem: models learn to flatter (sycophancy), to pad answers, even to fake reasoning that *looks* faithful. 2025 work on 'reward model overoptimization' shows scores can rise as real quality falls.",
        bold_move="Provoke: invent a reward function for 'helpful answers,' then describe exactly how you'd hack it without being helpful. Then propose the patch — and find the hack in your patch.",
    ),
    # --- Week 2: Efficient models — shrinking & speeding up --------------------
    Lesson(
        concept="Parameter-Efficient Fine-Tuning",
        plain="PEFT methods like LoRA freeze the giant base model and train only a tiny set of new low-rank weights, capturing most of the benefit at a fraction of the cost.",
        analogy="Like adding sticky-note annotations to a textbook instead of reprinting the whole book to fix a chapter.",
        frontier="LoRA + QLoRA democratized fine-tuning — you can now adapt a 70B model on a single consumer GPU. The whole adapter ecosystem (swap a 50MB LoRA to change a model's behavior) is built on this one trick.",
        bold_move="Build: take a weight matrix W, make a low-rank update B@A with rank 4, and show that W + B@A has the same shape but a tiny fraction of the trainable numbers. That ratio is why LoRA works.",
    ),
    Lesson(
        concept="Quantization",
        plain="Quantization stores and computes model weights at lower numerical precision (16→8→4 bits and below), shrinking memory and speeding inference with minimal quality loss.",
        analogy="Like compressing a lossless album to a high-bitrate MP3 — almost indistinguishable, a fraction of the size.",
        frontier="Quantization is what put frontier-class models on laptops and phones. GPTQ, AWQ, and GGUF are the workhorses; the 2024-2025 frontier pushes toward 4-bit and even 1.58-bit (BitNet) training, not just post-hoc squeezing.",
        bold_move="Build: quantize a numpy array to int8 (scale, round, clip) and back, then measure the reconstruction error. Watch how a smart scale factor saves the accuracy a naive cast would throw away.",
    ),
    Lesson(
        concept="Knowledge Distillation",
        plain="Distillation trains a small 'student' model to mimic a large 'teacher' — learning from the teacher's full probability distribution, not just hard labels.",
        analogy="Like an apprentice who learns not just the master's final answer but how confident the master was in every alternative.",
        frontier="Distillation is the open secret behind today's small-but-mighty models — much of the 'small model magic' is a frontier model's outputs in disguise. It's also a live legal and ToS battleground over who may distill whom.",
        bold_move="Build: train a tiny classifier on a bigger model's *soft* probabilities vs. on hard 0/1 labels, and compare. See why the teacher's 'shape of doubt' is a richer signal than the answer alone.",
    ),
    Lesson(
        concept="Mixture-of-Experts",
        plain="An MoE model has many expert sub-networks but a router activates only a few per token, so total parameters are huge while compute per token stays small.",
        analogy="Like a hospital with 100 specialists where each patient sees only the 2 they need — vast expertise, a short visit.",
        frontier="MoE is how frontier labs scale parameter count without scaling cost — Mixtral, DeepSeek-V3, and (reportedly) GPT-4 are sparse. The hard problems are routing stability and load balancing: keep one expert from hogging every token.",
        bold_move="Build: code a toy router that sends each input vector to its top-2 of 4 experts by a learned score, and print which expert fires when. Then make one expert greedy and watch load-balancing break.",
    ),
    Lesson(
        concept="Speculative Decoding",
        plain="Speculative decoding uses a small fast model to draft several tokens, then the big model verifies them all in one pass — accepting the run until the first mismatch.",
        analogy="Like an intern drafting a sentence and the expert glancing once to approve or correct it — far faster than the expert writing every word.",
        frontier="Speculative decoding gives 2-3x speedups with *zero* quality loss (the big model's distribution is provably preserved). It's now standard in vLLM/TensorRT-LLM, with Medusa and EAGLE pushing the draft-and-verify idea further.",
        bold_move="Build: simulate it — a 'draft' function proposes 4 tokens, a 'verify' function accepts the matching prefix and rejects the rest. Track your acceptance rate; that number *is* your speedup.",
    ),
    Lesson(
        concept="KV-Cache and Paged Attention",
        plain="The KV-cache stores past tokens' keys and values so each new token isn't recomputed; paged attention manages that cache in GPU memory like an OS pages RAM.",
        analogy="Like a court stenographer keeping the full transcript so nobody re-reads the whole trial for every new sentence — and a clerk who files the pages without wasting a single drawer.",
        frontier="The KV-cache is the real memory bottleneck of long-context serving — it can dwarf the model weights. vLLM's PagedAttention slashed waste and multiplied throughput; managing this cache is now the core of every fast inference engine.",
        bold_move="Build: compute the KV-cache size for a 70B-class model at 32k context (layers × 2 × heads × dim × tokens × bytes). The number explains why your long chats get expensive — and why paging matters.",
    ),
    # --- Week 3: Architecture & long-context frontier -------------------------
    Lesson(
        concept="FlashAttention",
        plain="FlashAttention computes exact attention without ever writing the full N×N score matrix to slow memory — it tiles the work and keeps it in fast on-chip SRAM.",
        analogy="Like doing long multiplication in your head one column at a time instead of writing out a giant grid you have to keep fetching from another room.",
        frontier="FlashAttention is the quiet reason long context became affordable — same math, memory-aware. It's IO-bound thinking: the bottleneck was moving data, not the FLOPs. v2 and v3 keep squeezing the modern GPU's memory hierarchy.",
        bold_move="Provoke: FlashAttention changed nothing about the math and everything about the cost. Write why 'the algorithm was never the bottleneck — the memory was' is a lesson that generalizes far beyond attention.",
    ),
    Lesson(
        concept="State-Space Models",
        plain="State-space models like Mamba process sequences with a recurrent, linear-time mechanism instead of all-pairs attention, carrying a compressed state forward.",
        analogy="Like reading a book and updating a running summary in your head, versus re-scanning every previous page for each new word.",
        frontier="Mamba and linear-attention models are the most serious challenge yet to the transformer's O(n²) wall — linear scaling in sequence length. The live 2024-2025 verdict: hybrids (a little attention + a lot of SSM) may beat either alone.",
        bold_move="Provoke: attention compares every token to every other; SSMs compress the past into a fixed state. Argue which is closer to how *you* read — and what each one must be giving up.",
    ),
    Lesson(
        concept="Long-Context Methods",
        plain="Techniques like RoPE scaling, position interpolation, and YaRN let a model trained on short sequences generalize to far longer ones without full retraining.",
        analogy="Like learning to read on paragraphs and then, with a clever trick, suddenly handling whole novels without going back to school.",
        frontier="These tricks are how 8k-trained models became 128k-1M context models almost overnight. But 'lost in the middle' persists — a huge window doesn't guarantee the model *uses* the middle. Long-context evals are now their own field.",
        bold_move="Build: take RoPE's rotation angles and 'interpolate' them (divide the position by a scale factor). Show numerically how that squeezes longer positions into the range the model already understands.",
    ),
    Lesson(
        concept="Multimodal Models",
        plain="Vision-language models project images (and audio) into the same token/embedding space as text, so one transformer can reason over pictures and words together.",
        analogy="Like teaching someone to think in a single language where a photo and a paragraph are just different kinds of sentences.",
        frontier="Multimodality went from bolt-on to native: GPT-4o, Gemini, and Claude reason across image, audio, and text in one model. The frontier is 'any-to-any' and grounded agents that *see* a screen — the basis of computer-use agents.",
        bold_move="Build: take any embedding model and show that a caption and a description of the same scene land close in vector space. That shared geometry is the whole trick behind 'a picture is a kind of sentence.'",
    ),
    Lesson(
        concept="Grouped-Query Attention",
        plain="GQA lets multiple query heads share a smaller set of key/value heads, shrinking the KV-cache and speeding inference with little quality loss.",
        analogy="Like a newsroom where many reporters share a few fact-checkers instead of each hiring their own — fewer files to keep, nearly the same output.",
        frontier="GQA (and its extreme, multi-query attention) is in nearly every modern model — Llama, Mistral, and friends — precisely because the KV-cache, not the math, is the serving bottleneck. It's a pure memory-vs-quality dial.",
        bold_move="Build: count the KV-cache entries for full multi-head (32 KV heads) vs. GQA (8 KV heads) vs. MQA (1) at the same context length. The ratio is exactly the memory you save per token.",
    ),
    Lesson(
        concept="Synthetic Data",
        plain="Synthetic data is training data generated by models themselves — to fill gaps, teach reasoning, or replace scarce human text.",
        analogy="Like a student writing their own practice problems once they've outgrown the textbook — powerful, but risky if the problems quietly drift from reality.",
        frontier="With high-quality human text running low (the 'data wall'), synthetic data is the field's biggest bet — and the source of much recent reasoning progress. The danger is model collapse: train carelessly on AI text and quality decays.",
        bold_move="Provoke: if the best new training data is generated by the previous best model, where does genuinely new knowledge enter the loop? Argue your answer — and name the one thing synthetic data can never bootstrap.",
    ),
    # --- Week 4: Interpretability & the model's internals ---------------------
    Lesson(
        concept="Mechanistic Interpretability",
        plain="Mechanistic interpretability reverse-engineers the actual computation inside a model — finding the specific circuits of neurons and attention heads that implement a behavior.",
        analogy="Like a neuroscientist tracing which exact neurons fire to recognize a face, but with full access to every weight and wire.",
        frontier="This is the field trying to make models *legible* instead of trusted-on-faith. Famous results — induction heads, the 'indirect object identification' circuit — show real, findable algorithms inside the weights. It's safety's microscope.",
        bold_move="Reach out: email or DM an interpretability researcher one honest question — 'If we fully understood the circuits, would we trust a model more, or just find scarier ones?' Two sentences on what you're learning, then the question. Send it.",
    ),
    Lesson(
        concept="Sparse Autoencoders",
        plain="Sparse autoencoders decompose a model's dense, polysemantic activations into a large dictionary of sparse, often human-interpretable features.",
        analogy="Like splitting a muddy mixed paint back into the handful of pure pigments that made it — suddenly you can name each color.",
        frontier="SAEs are interpretability's breakout tool: Anthropic's 'Scaling Monosemanticity' pulled millions of features (the 'Golden Gate Bridge' feature) out of a production model. Superposition — many concepts crammed into few neurons — is why we needed them.",
        bold_move="Build: train a tiny sparse autoencoder on random 'activation' vectors and watch the L1 penalty force most features to zero. That sparsity is what turns a tangled vector into nameable parts.",
    ),
    Lesson(
        concept="Activation Steering",
        plain="Activation steering edits a model's behavior at inference by adding a direction vector to its internal activations — no retraining, just a nudge in representation space.",
        analogy="Like turning a single knob in someone's mind labeled 'be more cautious' while they're mid-sentence.",
        frontier="Representation engineering and steering vectors are a cheap, surgical alternative to fine-tuning — turn honesty, refusal, or a persona up or down by adding a vector. The flip side: the same lever is a jailbreak. Control and attack share a door.",
        bold_move="Build: take two sets of vectors ('happy' vs 'sad' sentence embeddings), subtract the means to get a 'steering direction,' and add it to a neutral vector. You just built the core of activation steering.",
    ),
    Lesson(
        concept="Model Editing",
        plain="Model editing surgically changes a specific fact a model 'knows' by directly modifying the weights that store it, without retraining the whole model.",
        analogy="Like correcting one entry in an encyclopedia by rewriting a single sentence, instead of reprinting every volume.",
        frontier="ROME and MEMIT showed facts live in locatable mid-layer MLP weights you can rewrite — fascinating and unsettling. The catch interpretability keeps finding: edits ripple, and 'where a fact lives' is messier than a clean address.",
        bold_move="Provoke: if a company can edit one fact into a model's weights, it can edit a lie in just as easily — invisibly. Write the policy you'd want for disclosing model edits, and who should enforce it.",
    ),
    Lesson(
        concept="Scaling Laws Revisited",
        plain="Scaling laws predict loss from data, parameters, and compute; Chinchilla showed most big models were undertrained — too many parameters for too little data.",
        analogy="Like discovering a fleet of sports cars was running on half-empty tanks — the fix wasn't bigger engines, it was more fuel.",
        frontier="Chinchilla-optimal reset the field, then inference economics flipped it again: if you'll serve a model billions of times, it's worth *overtraining* a smaller one (Llama 3's bet). The optimum depends on whether you're paying to train or to serve.",
        bold_move="Build: plot a toy loss = a·N^-x + b·D^-y over a compute budget and find the (parameters, data) split that minimizes it. You just rediscovered the Chinchilla tradeoff in 20 lines.",
    ),
    Lesson(
        concept="Grokking",
        plain="Grokking is when a model, long after memorizing its training data, suddenly generalizes — test accuracy jumps from chance to near-perfect well past 'convergence.'",
        analogy="Like a student who crams and parrots for weeks, then one morning the underlying rule clicks and they can solve anything.",
        frontier="Grokking is a window into *how* generalization actually forms — interpretability work caught the exact moment a model swaps a memorized lookup for a real algorithm. It hints that 'done training' is a far blurrier line than the loss curve suggests.",
        bold_move="Provoke: grokking means a model can look fully trained while still being one epoch away from truly understanding. Argue what that does to how we should decide a training run is 'finished.'",
    ),
    # --- Week 5: Agentic & production-grade systems ---------------------------
    Lesson(
        concept="Tool Use",
        plain="Tool use (function calling) lets a model emit a structured request to call code, APIs, or search — and fold the result back into its reasoning.",
        analogy="Like a brilliant analyst who, instead of guessing, knows exactly when to pick up the phone, run a query, or open a calculator.",
        frontier="Function calling turned LLMs from talkers into doers — the foundation of every agent. MCP (the Model Context Protocol) is the 2024-2025 push to standardize how models discover and call tools, like USB for AI capabilities.",
        bold_move="Build: define one tool as a JSON schema (name, params), then write the parser that takes a model's 'call this tool' output and dispatches it to a real Python function. That loop is the whole game.",
    ),
    Lesson(
        concept="Agentic Loops",
        plain="An agent runs a loop — reason, act with a tool, observe the result, repeat — until a goal is met, rather than answering in one shot.",
        analogy="Like a detective who doesn't solve the case in one monologue but investigates, follows leads, and revises until it cracks.",
        frontier="ReAct, reflection, and planning turned single answers into autonomous workflows — the defining shift of 2025. The hard problems are now systemic: error compounding over long horizons, cost, and knowing when to stop. Evaluation, not generation, is the bottleneck.",
        bold_move="Build: write a 30-line ReAct loop (Thought→Action→Observation) with one fake tool that the model 'calls' by emitting text. Watch how one wrong observation can derail every step after it.",
    ),
    Lesson(
        concept="Advanced RAG",
        plain="Advanced RAG goes beyond naive vector search: rerankers, hybrid (keyword+vector) retrieval, query rewriting, GraphRAG, and agentic retrieval that searches in a loop.",
        analogy="Like upgrading from grabbing the first book on the shelf to a research librarian who cross-references, double-checks, and digs until the answer is right.",
        frontier="The 2024-2025 consensus: RAG's weak link is retrieval, not generation, so production stacks bolt on rerankers and hybrid search, and GraphRAG adds relationships plain vectors miss. 'Agentic RAG' lets the model decide what to fetch next.",
        bold_move="Build: take a query plain vector search gets wrong (synonyms, acronyms), then add a reranking step that reorders the top-k by a second score. Document the before/after — that delta is why rerankers exist.",
    ),
    Lesson(
        concept="LLM-as-a-Judge",
        plain="LLM-as-a-judge uses a strong model to grade other models' outputs against a rubric, scaling evaluation far beyond what human raters can cover.",
        analogy="Like appointing an expert referee for a tournament too big for human judges to watch every match — fast, but with the referee's own blind spots.",
        frontier="As static benchmarks saturate and leak, eval shifted to model judges and live human-vote arenas (LMArena). But 'who judges the judge?' is unsolved: judges have biases — for length, for their own style, for position. Evaluation is now a research field.",
        bold_move="Build: write a judge prompt that scores two answers 1-5 on a rubric, then test it on a pair where the *longer* answer is worse. Did your judge fall for length bias? Patch the rubric and retry.",
    ),
    Lesson(
        concept="Structured Outputs",
        plain="Structured outputs constrain a model to emit valid JSON or schema-conforming text by masking the token choices that would break the format — guaranteed parseability.",
        analogy="Like a form that physically won't let you write outside the boxes, so every submission is machine-readable by construction.",
        frontier="Constrained decoding (grammars, JSON schema, tool-call formats) is what makes LLMs safe to wire into real software — no more regex-scraping prose. It's now a first-class API feature, and the backbone of reliable tool use and agents.",
        bold_move="Build: write a tiny constrained generator that, at each step, only allows tokens valid in JSON given what's been emitted so far. Even a toy version shows why 'the model literally can't produce broken JSON' beats hoping it won't.",
    ),
    Lesson(
        concept="Inference Economics",
        plain="Serving LLMs is an optimization over throughput, latency, and cost — driven by batching, the KV-cache, quantization, and how you trade tokens-per-second against dollars.",
        analogy="Like running an airline: the model is the plane, but profit lives in how full each flight is, the turnaround time, and the fuel bill per seat.",
        frontier="Inference, not training, is where most AI compute (and money) now goes. Continuous batching, paged attention, and prefix caching are the levers; 'tokens per dollar' is the metric that decides which products are even viable. Serving is a systems-engineering frontier.",
        bold_move="Build: model the cost of one feature — tokens per request × requests per day × price per token — then show how batching or a smaller model changes the bill. Circle the one lever that makes it ship-able.",
    ),
]
