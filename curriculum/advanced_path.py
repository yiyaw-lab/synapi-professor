"""The suggested 5-week study plan over the 30 advanced lessons.

Like ``foundation_path.py``, this is guidance for a human following the advanced
track, not something the daily sender reads — ``professor.py`` cycles through
``ADVANCED_LLM`` by date and does not consult this file. ``ADVANCED_PATH`` groups
concepts into weekly themes (the ``focus`` lists use the same ``concept`` strings
as the curriculum) and ``ADVANCED_SCHEDULE_NOTES`` records pacing and the
recommended per-lesson workflow.
"""

LearningPhase = dict[str, object]

ADVANCED_PATH: list[LearningPhase] = [
    {
        "week": 1,
        "theme": "Post-training and preference optimization",
        "focus": [
            "Supervised Fine-Tuning",
            "RLHF",
            "Direct Preference Optimization",
            "Constitutional AI",
            "Reasoning Models",
            "Reward Hacking",
        ],
        "deliverables": ["Hand-built DPO loss", "Constitutional critique→revise exercise"],
    },
    {
        "week": 2,
        "theme": "Efficient models: shrinking and speeding up",
        "focus": [
            "Parameter-Efficient Fine-Tuning",
            "Quantization",
            "Knowledge Distillation",
            "Mixture-of-Experts",
            "Speculative Decoding",
            "KV-Cache and Paged Attention",
        ],
        "deliverables": ["LoRA low-rank update demo", "Speculative decoding simulator"],
    },
    {
        "week": 3,
        "theme": "Architecture and the long-context frontier",
        "focus": [
            "FlashAttention",
            "State-Space Models",
            "Long-Context Methods",
            "Multimodal Models",
            "Grouped-Query Attention",
            "Synthetic Data",
        ],
        "deliverables": ["KV-cache size calculation", "RoPE interpolation walkthrough"],
    },
    {
        "week": 4,
        "theme": "Interpretability and the model's internals",
        "focus": [
            "Mechanistic Interpretability",
            "Sparse Autoencoders",
            "Activation Steering",
            "Model Editing",
            "Scaling Laws Revisited",
            "Grokking",
        ],
        "deliverables": ["Tiny sparse autoencoder", "Steering-vector construction"],
    },
    {
        "week": 5,
        "theme": "Agentic and production-grade systems",
        "focus": [
            "Tool Use",
            "Agentic Loops",
            "Advanced RAG",
            "LLM-as-a-Judge",
            "Structured Outputs",
            "Inference Economics",
        ],
        "deliverables": ["ReAct agent loop", "LLM-as-judge rubric + bias test"],
    },
]

ADVANCED_SCHEDULE_NOTES = {
    "duration": "5 weeks",
    "weekly_commitment": "4-6 hours",
    "prerequisite": "The foundation track (or equivalent grounding in how LLMs work).",
    "recommended_workflow": [
        "Read the lesson concept and analogy",
        "Review references — start with the original paper",
        "Run the associated lab and modify one parameter to test your understanding",
        "Reflect using the lesson's bold move",
    ],
}
