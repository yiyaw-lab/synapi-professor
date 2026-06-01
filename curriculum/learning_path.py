from typing import List, Dict

LearningPhase = Dict[str, object]

LEARNING_PATH: List[LearningPhase] = [
    {
        "week": 1,
        "theme": "Token and embedding fundamentals",
        "focus": ["Tokens", "Tokenization", "Vocabulary", "Embeddings", "Semantic Space", "Similarity"],
        "deliverables": ["Tokenization notebook", "Token vocabulary exercise"],
    },
    {
        "week": 2,
        "theme": "Core model mechanisms",
        "focus": ["Next Token Prediction", "Attention", "Self-Attention", "Context Windows", "Positional Encoding", "Transformers"],
        "deliverables": ["Transformer attention walkthrough", "Context window exploration"],
    },
    {
        "week": 3,
        "theme": "Training dynamics",
        "focus": ["Pretraining", "Loss Functions", "Gradient Descent", "Parameters", "Scaling Laws", "Emergent Abilities"],
        "deliverables": ["Loss and gradient demo", "Scaling laws reflection"],
    },
    {
        "week": 4,
        "theme": "Reliability and failure modes",
        "focus": ["Hallucinations", "Context Poisoning", "Retrieval Failures", "Goodhart's Law in AI", "Distribution Shift"],
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
