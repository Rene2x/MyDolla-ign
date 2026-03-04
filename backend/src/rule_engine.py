import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


DEFAULT_RULES_PATH = os.path.join(
    os.path.dirname(__file__),
    "rules",
    "financial_rules.json",
)


class RuleLoadError(RuntimeError):
    """Raised when financial rules cannot be loaded or parsed."""


@dataclass(frozen=True)
class FinancialRule:
    """
    Immutable representation of a financial rule.

    The JSON file is expected to contain objects with at least:
    - id: stable identifier (e.g. "R_50_30_20")
    - name: human readable label
    - description: high‑level rule description
    - category: e.g. "budget_allocation", "savings", "emergency_fund"
    - reference: optional source string
    - parameters: free‑form dict with thresholds, percentages, etc.
    """

    id: str
    name: str
    description: str
    category: str
    reference: Optional[str]
    parameters: Dict[str, Any]

    @staticmethod
    def from_dict(raw: Dict[str, Any]) -> "FinancialRule":
        try:
            return FinancialRule(
                id=str(raw["id"]),
                name=str(raw["name"]),
                description=str(raw["description"]),
                category=str(raw.get("category", "general")),
                reference=raw.get("reference"),
                parameters=dict(raw.get("parameters", {})),
            )
        except KeyError as exc:
            missing = ", ".join(sorted(k for k in ("id", "name", "description") if k not in raw))
            raise RuleLoadError(f"Rule is missing required field(s): {missing}") from exc


def _load_rules_from_path(path: str) -> List[FinancialRule]:
    if not os.path.exists(path):
        raise RuleLoadError(f"Rules file not found at {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise RuleLoadError(f"Failed to parse rules JSON: {exc}") from exc

    if not isinstance(data, list):
        raise RuleLoadError("Rules file must contain a JSON array of rule objects")

    rules: List[FinancialRule] = []
    for idx, raw in enumerate(data):
        if not isinstance(raw, dict):
            raise RuleLoadError(f"Rule at index {idx} is not an object")
        rules.append(FinancialRule.from_dict(raw))
    return rules


class RuleEngine:
    """
    Lightweight rule loader and selector.

    This class is intentionally simple and deterministic:
    - No network access.
    - No randomness.
    - Pure functions based on provided user data and static rules.
    """

    def __init__(self, rules_path: str = DEFAULT_RULES_PATH) -> None:
        self._rules_path = rules_path
        self._rules: Optional[List[FinancialRule]] = None

    @property
    def rules(self) -> List[FinancialRule]:
        """Load and cache rules on first access."""
        if self._rules is None:
            self._rules = _load_rules_from_path(self._rules_path)
        return self._rules

    def as_dicts(self) -> List[Dict[str, Any]]:
        """Return rules as plain dictionaries (safe to send to an LLM)."""
        result: List[Dict[str, Any]] = []
        for r in self.rules:
            result.append(
                {
                    "id": r.id,
                    "name": r.name,
                    "description": r.description,
                    "category": r.category,
                    "reference": r.reference,
                    "parameters": r.parameters,
                }
            )
        return result

    def select_relevant_rules(self, user_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Select a deterministic subset of rules that are likely relevant.

        This is intentionally conservative and transparent:
        - Uses simple threshold comparisons only.
        - Never infers missing values.
        - Always returns a stable ordering (by rule id).
        """

        income = user_data.get("monthly_income")
        expenses = user_data.get("expenses") or {}
        savings = expenses.get("savings")
        housing = expenses.get("housing") or expenses.get("rent")
        debt_payment = expenses.get("debt_payment")

        relevant: List[FinancialRule] = []

        for rule in self.rules:
            p = rule.parameters
            include = False

            # Very simple, explicit heuristics keyed by category.
            if rule.category == "budget_allocation" and income and isinstance(income, (int, float)):
                include = True
            elif rule.category == "savings" and income and isinstance(income, (int, float)) and isinstance(
                savings, (int, float)
            ):
                include = True
            elif rule.category == "emergency_fund" and income and isinstance(income, (int, float)):
                include = True
            elif rule.category == "overspending" and income and isinstance(income, (int, float)):
                total_expenses = user_data.get("total_expenses")
                if isinstance(total_expenses, (int, float)) and total_expenses > income:
                    include = True
            elif rule.category == "housing_cost" and income and isinstance(income, (int, float)) and isinstance(
                housing, (int, float)
            ):
                include = True
            elif rule.category == "debt_to_income" and income and isinstance(income, (int, float)) and isinstance(
                debt_payment, (int, float)
            ):
                include = True

            # Allow explicit "always_include" parameter in JSON for exceptions.
            if p.get("always_include") is True:
                include = True

            if include:
                relevant.append(rule)

        # Deterministic ordering
        relevant.sort(key=lambda r: r.id)
        return [
            {
                "id": r.id,
                "name": r.name,
                "description": r.description,
                "category": r.category,
                "reference": r.reference,
                "parameters": r.parameters,
            }
            for r in relevant
        ]

