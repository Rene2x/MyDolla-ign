import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

# Google AI SDK (uses API key from Google AI Studio)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

from src.prompt_templates import build_tutor_prompt
from src.rule_engine import RuleEngine, RuleLoadError


DEFAULT_MODEL_NAME = "gemini-2.5-flash"


def _init_genai():
    """Initialize Google AI with API key from environment."""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    
    genai.configure(api_key=api_key)


@dataclass
class TutorResult:
    """
    Strongly-typed view of the tutor output.

    This keeps the shape deterministic and easy to validate in tests.
    """

    status: str
    explanation: str
    quiz: Dict[str, Any]
    tip: Dict[str, Any]
    used_rule_ids: list

    @staticmethod
    def from_dict(raw: Dict[str, Any]) -> "TutorResult":
        # Minimal defensive parsing with defaults for robustness.
        status = str(raw.get("status", "ok"))
        explanation = str(raw.get("explanation", "") or "")
        quiz = raw.get("quiz") or {}
        tip = raw.get("tip") or {}
        used_rule_ids = raw.get("used_rule_ids") or []

        # Enforce required keys when status is ok.
        if status == "ok":
            if not explanation:
                raise ValueError("TutorResult: explanation is required when status='ok'")
            if not isinstance(quiz, dict) or "question" not in quiz:
                raise ValueError("TutorResult: quiz.question is required when status='ok'")
            if not isinstance(tip, dict) or "text" not in tip:
                raise ValueError("TutorResult: tip.text is required when status='ok'")

        return TutorResult(
            status=status,
            explanation=explanation,
            quiz=quiz,
            tip=tip,
            used_rule_ids=list(used_rule_ids),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
            "explanation": self.explanation,
            "quiz": self.quiz,
            "tip": self.tip,
            "used_rule_ids": self.used_rule_ids,
        }


class AITutor:
    """
    Core AI tutor orchestrator using Google AI (Gemini).

    Responsibilities:
    - Validate user financial data.
    - Load and filter financial rules.
    - Build a grounded, strictly constrained prompt.
    - Call Google AI Gemini with deterministic settings.
    - Parse and validate the JSON-only response.
    """

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL_NAME,
        rule_engine: Optional[RuleEngine] = None,
    ) -> None:
        self._model_name = model_name
        self._rule_engine = rule_engine or RuleEngine()
        self._initialized = False

    @staticmethod
    def _has_minimum_data(user_data: Dict[str, Any]) -> bool:
        income = user_data.get("monthly_income")
        expenses = user_data.get("expenses") or {}
        return isinstance(income, (int, float)) and bool(expenses)

    def _ensure_initialized(self):
        """Initialize Google AI on first use."""
        if not self._initialized:
            if not GEMINI_AVAILABLE:
                raise RuntimeError("Google AI SDK is not installed")
            _init_genai()
            self._initialized = True

    def generate_session(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a single tutoring session result.

        Returns a dict matching TutorResult.to_dict().
        Never returns non-JSON content; callers can safely jsonify this.
        """
        # If minimal data missing, short-circuit with deterministic response.
        if not self._has_minimum_data(user_data):
            return TutorResult(
                status="Insufficient data",
                explanation="Key budget information is missing; please provide income and categorized expenses.",
                quiz={
                    "question": "Why is it important to know both income and expenses before building a budget plan?",
                    "answer": "Without both income and expenses, you cannot see whether you are overspending or how much you can safely save.",
                    "rule_ids": [],
                },
                tip={
                    "text": "Start by listing all sources of monthly income and your main expense categories. Once those are clear, a tutor can help you apply budgeting rules.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        try:
            all_rules = self._rule_engine.as_dicts()
            relevant_rules = self._rule_engine.select_relevant_rules(user_data)
        except RuleLoadError as exc:
            return TutorResult(
                status="Insufficient data",
                explanation=f"Financial rules could not be loaded safely ({exc}); tutoring is disabled to avoid unsupported advice.",
                quiz={
                    "question": "What advantage does a financial rule provide when reviewing a budget?",
                    "answer": "Rules give consistent guidelines, such as target savings rates or housing cost ranges, that help interpret the numbers.",
                    "rule_ids": [],
                },
                tip={
                    "text": "Until rules are available, you can still track your spending and ensure expenses do not consistently exceed income.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        if not all_rules:
            return TutorResult(
                status="Insufficient data",
                explanation="No financial rules are available, so the tutor cannot provide grounded guidance.",
                quiz={
                    "question": "Why is grounding in explicit financial rules important for an AI budgeting tutor?",
                    "answer": "It keeps advice consistent with documented principles instead of relying on the model's guesses.",
                    "rule_ids": [],
                },
                tip={
                    "text": "Define at least a few core budgeting rules (such as savings benchmarks or emergency fund targets) before relying on AI-generated tips.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        prompt = build_tutor_prompt(
            user_data=user_data,
            rules=all_rules,
            relevant_rules=relevant_rules,
        )

        try:
            self._ensure_initialized()
            model = genai.GenerativeModel(
                model_name=self._model_name,
                generation_config=genai.GenerationConfig(
                    temperature=0.0,
                    top_p=0.1,
                    max_output_tokens=4096,
                    response_mime_type="application/json",
                ),
            )

            response = model.generate_content(prompt)
        except Exception as exc:
            return TutorResult(
                status="Insufficient data",
                explanation=f"The tutor backend could not reach the language model safely ({exc}).",
                quiz={
                    "question": "What is one thing you can still do without an AI tutor to improve your budget?",
                    "answer": "Review your largest expense categories and decide one small change to reduce or monitor them.",
                    "rule_ids": [],
                },
                tip={
                    "text": "Until the AI tutor is available, focus on tracking your actual spending and comparing it to a simple target like the 50/30/20 guideline.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        raw_text = response.text if hasattr(response, 'text') else None
        if not raw_text:
            return TutorResult(
                status="Insufficient data",
                explanation="The language model returned an empty response when JSON was expected.",
                quiz={
                    "question": "Why should AI outputs be checked for completeness before using them?",
                    "answer": "Incomplete outputs can miss important context or constraints, leading to misleading guidance.",
                    "rule_ids": [],
                },
                tip={
                    "text": "If an AI system returns an empty or invalid result, treat it as a failure and fall back to simple, rule-based checks.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        try:
            parsed = json.loads(raw_text)
        except json.JSONDecodeError as exc:
            return TutorResult(
                status="Insufficient data",
                explanation=f"The language model did not return valid JSON ({exc}).",
                quiz={
                    "question": "Why is strict JSON formatting useful in AI-powered backends?",
                    "answer": "It makes responses easier to validate, test, and consume by other services or frontends.",
                    "rule_ids": [],
                },
                tip={
                    "text": "When designing AI systems, keep outputs structured (like JSON) so they can be checked and safely integrated.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        try:
            result = TutorResult.from_dict(parsed)
        except Exception as exc:
            return TutorResult(
                status="Insufficient data",
                explanation=f"The tutor output did not match the expected JSON structure ({exc}).",
                quiz={
                    "question": "Why is a clear schema important for AI-generated data?",
                    "answer": "A clear schema lets developers validate outputs and prevents silently using incomplete or wrong fields.",
                    "rule_ids": [],
                },
                tip={
                    "text": "Define and document the exact fields your AI outputs must provide so you can write automated tests around them.",
                    "rule_ids": [],
                },
                used_rule_ids=[],
            ).to_dict()

        return result.to_dict()
