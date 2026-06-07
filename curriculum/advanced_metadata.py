"""Per-concept side data for the advanced track, keyed by ``Lesson.concept``.

Mirrors ``foundation_metadata.py`` but for ``advanced_llm.ADVANCED_LLM``:

    ADV_REFERENCE_LIBRARY  concept -> 1-3 canonical URLs ("Go deeper")
    ADV_NOTEBOOK_FILES     concept -> bare lab filename (``aNN_*.ipynb``)

Kept separate from the lesson text so the prose stays readable and the
links/notebooks can change independently. The integrity invariant (enforced by
``tests/test_curriculum.py`` across every track) is the same: every concept in
``ADVANCED_LLM`` has an entry in both maps, and every notebook filename exists on
disk in ``labs/``.

Reference preference order matches the foundation track: original papers first,
then official docs/posts, then trusted explainers (Lilian Weng, Hugging Face,
Anthropic interpretability, distill/transformer-circuits).
"""

# One to three canonical resources per advanced lesson.
ADV_REFERENCE_LIBRARY = {
    "Supervised Fine-Tuning": [
        "https://arxiv.org/abs/2203.02155",
        "https://arxiv.org/abs/2305.11206",
        "https://huggingface.co/docs/trl/sft_trainer",
    ],
    "RLHF": [
        "https://arxiv.org/abs/2203.02155",
        "https://huggingface.co/blog/rlhf",
        "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    ],
    "Direct Preference Optimization": [
        "https://arxiv.org/abs/2305.18290",
        "https://huggingface.co/docs/trl/dpo_trainer",
    ],
    "Constitutional AI": [
        "https://arxiv.org/abs/2212.08073",
        "https://www.anthropic.com/news/claudes-constitution",
    ],
    "Reasoning Models": [
        "https://arxiv.org/abs/2501.12948",
        "https://openai.com/index/learning-to-reason-with-llms/",
        "https://lilianweng.github.io/posts/2025-05-01-thinking/",
    ],
    "Reward Hacking": [
        "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
        "https://arxiv.org/abs/2210.10760",
    ],
    "Parameter-Efficient Fine-Tuning": [
        "https://arxiv.org/abs/2106.09685",
        "https://arxiv.org/abs/2305.14314",
        "https://huggingface.co/docs/peft/index",
    ],
    "Quantization": [
        "https://arxiv.org/abs/2210.17323",
        "https://arxiv.org/abs/2306.00978",
        "https://huggingface.co/docs/transformers/main/en/quantization/overview",
    ],
    "Knowledge Distillation": [
        "https://arxiv.org/abs/1503.02531",
        "https://lilianweng.github.io/posts/2023-01-10-inference-optimization/",
    ],
    "Mixture-of-Experts": [
        "https://arxiv.org/abs/2101.03961",
        "https://huggingface.co/blog/moe",
    ],
    "Speculative Decoding": [
        "https://arxiv.org/abs/2211.17192",
        "https://arxiv.org/abs/2401.10774",
    ],
    "KV-Cache and Paged Attention": [
        "https://arxiv.org/abs/2309.06180",
        "https://blog.vllm.ai/2023/06/20/vllm.html",
    ],
    "FlashAttention": [
        "https://arxiv.org/abs/2205.14135",
        "https://arxiv.org/abs/2307.08691",
    ],
    "State-Space Models": [
        "https://arxiv.org/abs/2312.00752",
        "https://srush.github.io/annotated-mamba/hard.html",
    ],
    "Long-Context Methods": [
        "https://arxiv.org/abs/2309.00071",
        "https://arxiv.org/abs/2306.15595",
        "https://arxiv.org/abs/2307.03172",
    ],
    "Multimodal Models": [
        "https://arxiv.org/abs/2103.00020",
        "https://huggingface.co/blog/vlms",
    ],
    "Grouped-Query Attention": [
        "https://arxiv.org/abs/2305.13245",
        "https://arxiv.org/abs/1911.02150",
    ],
    "Synthetic Data": [
        "https://arxiv.org/abs/2305.07759",
        "https://arxiv.org/abs/2305.17493",
    ],
    "Mechanistic Interpretability": [
        "https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html",
        "https://distill.pub/2020/circuits/zoom-in/",
        "https://www.neelnanda.io/mechanistic-interpretability/getting-started",
    ],
    "Sparse Autoencoders": [
        "https://transformer-circuits.pub/2024/scaling-monosemanticity/",
        "https://transformer-circuits.pub/2022/toy_model/index.html",
    ],
    "Activation Steering": [
        "https://arxiv.org/abs/2310.01405",
        "https://arxiv.org/abs/2308.10248",
    ],
    "Model Editing": [
        "https://arxiv.org/abs/2202.05262",
        "https://arxiv.org/abs/2210.07229",
    ],
    "Scaling Laws Revisited": [
        "https://arxiv.org/abs/2203.15556",
        "https://arxiv.org/abs/2001.08361",
    ],
    "Grokking": [
        "https://arxiv.org/abs/2201.02177",
        "https://arxiv.org/abs/2301.05217",
    ],
    "Tool Use": [
        "https://arxiv.org/abs/2302.04761",
        "https://modelcontextprotocol.io/introduction",
        "https://platform.openai.com/docs/guides/function-calling",
    ],
    "Agentic Loops": [
        "https://arxiv.org/abs/2210.03629",
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
    ],
    "Advanced RAG": [
        "https://arxiv.org/abs/2005.11401",
        "https://www.anthropic.com/news/contextual-retrieval",
        "https://arxiv.org/abs/2404.16130",
    ],
    "LLM-as-a-Judge": [
        "https://arxiv.org/abs/2306.05685",
        "https://huggingface.co/learn/cookbook/en/llm_judge",
    ],
    "Structured Outputs": [
        "https://arxiv.org/abs/2307.09702",
        "https://platform.openai.com/docs/guides/structured-outputs",
    ],
    "Inference Economics": [
        "https://arxiv.org/abs/2309.06180",
        "https://lilianweng.github.io/posts/2023-01-10-inference-optimization/",
    ],
}

# Notebook filenames (under labs/) for the advanced track. Prefixed ``a`` so they
# never collide with the foundation track's NN_*.ipynb on disk. professor.py turns
# these into clickable GitHub + Colab URLs.
ADV_NOTEBOOK_FILES = {
    "Supervised Fine-Tuning": "a01_supervised_fine_tuning.ipynb",
    "RLHF": "a02_rlhf.ipynb",
    "Direct Preference Optimization": "a03_dpo.ipynb",
    "Constitutional AI": "a04_constitutional_ai.ipynb",
    "Reasoning Models": "a05_reasoning_models.ipynb",
    "Reward Hacking": "a06_reward_hacking.ipynb",
    "Parameter-Efficient Fine-Tuning": "a07_peft_lora.ipynb",
    "Quantization": "a08_quantization.ipynb",
    "Knowledge Distillation": "a09_distillation.ipynb",
    "Mixture-of-Experts": "a10_mixture_of_experts.ipynb",
    "Speculative Decoding": "a11_speculative_decoding.ipynb",
    "KV-Cache and Paged Attention": "a12_kv_cache.ipynb",
    "FlashAttention": "a13_flash_attention.ipynb",
    "State-Space Models": "a14_state_space_models.ipynb",
    "Long-Context Methods": "a15_long_context.ipynb",
    "Multimodal Models": "a16_multimodal.ipynb",
    "Grouped-Query Attention": "a17_grouped_query_attention.ipynb",
    "Synthetic Data": "a18_synthetic_data.ipynb",
    "Mechanistic Interpretability": "a19_mech_interp.ipynb",
    "Sparse Autoencoders": "a20_sparse_autoencoders.ipynb",
    "Activation Steering": "a21_activation_steering.ipynb",
    "Model Editing": "a22_model_editing.ipynb",
    "Scaling Laws Revisited": "a23_scaling_laws_revisited.ipynb",
    "Grokking": "a24_grokking.ipynb",
    "Tool Use": "a25_tool_use.ipynb",
    "Agentic Loops": "a26_agentic_loops.ipynb",
    "Advanced RAG": "a27_advanced_rag.ipynb",
    "LLM-as-a-Judge": "a28_llm_as_judge.ipynb",
    "Structured Outputs": "a29_structured_outputs.ipynb",
    "Inference Economics": "a30_inference_economics.ipynb",
}
