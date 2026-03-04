from typing import Any, Dict, List


def build_tutor_prompt(
    user_data: Dict[str, Any],
    rules: List[Dict[str, Any]],
    relevant_rules: List[Dict[str, Any]],
) -> str:
    """
    Build a strict, grounded prompt for the budgeting tutor.

    The LLM is required to:
    - Use ONLY the numeric values and fields provided in `user_data`.
    - Ground all tips in one or more of the supplied `rules`.
    - Avoid any external assumptions, projections, or products.
    - Refuse politely with status \"Insufficient data\" when required fields are missing.
    - Return a single, valid JSON object with no extra text.
    """

    # Serialize a compact but explicit view of the user data.
    # This function deliberately does not perform calculations; caller is responsible.
    user_profile = {
        "monthly_income": user_data.get("monthly_income"),
        "total_expenses": user_data.get("total_expenses"),
        "remaining": user_data.get("remaining"),
        "goal": user_data.get("goal"),
        "expenses": user_data.get("expenses", {}),
    }

    instructions = """
You are an educational budgeting tutor for a student project.

You are ONLY allowed to use:
- The user financial data under "user_profile" below.
- The financial rules under "financial_rules" below.

You MUST NOT:
- Invent or estimate any numbers that are not present in user_profile.
- Add external financial products, providers, or projections.
- Give personalized investment recommendations.

Grounding requirements:
- Every explanation MUST reference at least one actual numeric value from user_profile.
- Every tip MUST reference at least one rule from financial_rules by its "id".
- The quiz question MUST clearly relate to the user's specific budget breakdown.

If any of the following are missing or null:
- user_profile.monthly_income
- user_profile.expenses (empty or missing)
then you MUST NOT attempt to tutor and MUST respond with a JSON object whose
"status" field is exactly "Insufficient data".

Output format requirements (non‑negotiable):
- Return EXACTLY ONE JSON object.
- The JSON must be syntactically valid (no comments, no trailing commas).
- Do NOT include any explanation, prose, markdown, or text outside the JSON.
- Do NOT include backticks or code fences.

The JSON object MUST have ALL of these top‑level fields:
- "status": either "ok" or "Insufficient data".
- "explanation": string. Short paragraph explaining the user's budget using their real numbers.
- "quiz": object with:
    - "question": string, one question about their budget or rules.
    - "answer": string, the correct answer to the question.
    - "rule_ids": array of rule ids that the quiz is testing (may be empty if purely about their numbers).
- "tip": object with:
    - "text": string, one concrete suggestion grounded in at least one rule.
    - "rule_ids": array of rule ids that justify this tip (MUST contain at least one id when status = "ok").
- "used_rule_ids": array of rule ids you relied on anywhere in the explanation, quiz, or tip.

Additional constraints:
- When status = "Insufficient data", set "explanation" to a short reason,
  return a generic safe quiz and tip, and set both "tip.rule_ids" and "used_rule_ids" to [].
- When status = "ok", you MUST:
  - reference at least one numeric value from user_profile in "explanation",
  - ensure "tip.rule_ids" is non‑empty,
  - ensure every id in "tip.rule_ids" exists in financial_rules.
"""

    return (
        instructions
        + "\n\nUSER DATA (user_profile):\n"
        + repr(user_profile)
        + "\n\nALL FINANCIAL RULES (financial_rules):\n"
        + repr(rules)
        + "\n\nRELEVANT FINANCIAL RULES (relevant_rules):\n"
        + repr(relevant_rules)
        + "\n\nRemember: respond with ONE JSON object only, with the exact required fields."
    )

