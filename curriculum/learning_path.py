"""The suggested 5-week study plan over the 30 lessons.

This is guidance for a human following the curriculum, not something the daily
sender reads — ``professor.py`` cycles through ``LLM_FOUNDATION`` by date and
does not consult this file. ``LEARNING_PATH`` groups concepts into weekly themes
(the ``focus`` lists use the same ``concept`` strings as the curriculum) and
``SCHEDULE_NOTES`` records pacing and the recommended per-lesson workflow.
"""

LearningPhase = dict[str, object]

LEARNING_PATH: list[LearningPhase] = [
    {
        "week": 1,
        "theme": "Token and embedding fundamentals",
        "focus": [
            "Tokens",
            "Tokenization",
            "Vocabulary",
            "Embeddings",
            "Semantic Space",
            "Similarity",
        ],
        "deliverables": ["Tokenization notebook", "Token vocabulary exercise"],
    },
    {
        "week": 2,
        "theme": "Core model mechanisms",
        "focus": [
            "Next Token Prediction",
            "Attention",
            "Self-Attention",
            "Context Windows",
            "Positional Encoding",
            "Transformers",
        ],
        "deliverables": ["Transformer attention walkthrough", "Context window exploration"],
    },
    {
        "week": 3,
        "theme": "Training dynamics",
        "focus": [
            "Pretraining",
            "Loss Functions",
            "Gradient Descent",
            "Parameters",
            "Scaling Laws",
            "Emergent Abilities",
        ],
        "deliverables": ["Loss and gradient demo", "Scaling laws reflection"],
    },
    {
        "week": 4,
        "theme": "Reliability and failure modes",
        "focus": [
            "Hallucinations",
            "Context Poisoning",
            "Retrieval Failures",
            "Goodhart's Law in AI",
            "Distribution Shift",
        ],
        "deliverables": ["Failure mode case study", "Retrieval/system evaluation exercise"],
    },
    {
        "week": 5,
        "theme": "Alignment, evaluation, and prompting",
        "focus": ["Alignment", "Evaluation", "Prompt Engineering", "Systems Thinking for AI"],
        "deliverables": ["Prompt design lab", "AI system mapping exercise"],
    },
]

SCHEDULE_NOTES = {
    "duration": "5 weeks",
    "weekly_commitment": "3-5 hours",
    "recommended_workflow": [
        "Read the lesson concept and analogy",
        "Review references for deeper context",
        "Run the associated practical notebook or toolkit exercise",
        "Reflect using the lesson exercise prompt",
    ],
}
