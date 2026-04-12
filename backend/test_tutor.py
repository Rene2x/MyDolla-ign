#!/usr/bin/env python3
"""Smoke test: analyze_budget(). Run: python test_tutor.py"""

import sys
from pathlib import Path

_BACKEND_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_BACKEND_DIR))

from dotenv import load_dotenv

load_dotenv(_BACKEND_DIR / ".env")

from app.models.budget import BudgetInput
from app.services.ai_service import analyze_budget


def main() -> None:
    b = BudgetInput(
        monthly_income=4000.0,
        expenses={
            "rent": 1200,
            "food": 500,
            "transportation": 200,
            "utilities": 150,
            "entertainment": 200,
            "savings": 400,
            "other": 150,
        },
        goal="general",
    )
    out = analyze_budget(b)
    assert out.get("quiz_question")
    print("OK — output_source:", out.get("output_source"))


if __name__ == "__main__":
    main()
