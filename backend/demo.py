#!/usr/bin/env python3
"""
Terminal demo — same engine as POST /api/analyze (`analyze_budget()`).

Run: python demo.py
Optional: set GEMINI_API_KEY in backend/.env; otherwise deterministic fallback.
Set DEMO_JSON=1 to print full JSON.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_BACKEND_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_BACKEND_DIR))

from dotenv import load_dotenv

load_dotenv(_BACKEND_DIR / ".env")

from app.models.budget import BudgetInput
from app.services.ai_service import analyze_budget


def _f(prompt: str) -> float:
    raw = input(f"{prompt} ($): ").strip().replace(",", "")
    if not raw:
        return 0.0
    try:
        return float(raw.replace("$", ""))
    except ValueError:
        print("  Invalid, using 0.")
        return 0.0


def main() -> None:
    print("\n=== My Dolla $ign — terminal demo (analyze_budget) ===\n")
    income = _f("Monthly income (after tax)")
    expenses = {
        "rent": _f("Rent / housing"),
        "food": _f("Food"),
        "transportation": _f("Transportation"),
        "utilities": _f("Utilities"),
        "entertainment": _f("Entertainment"),
        "savings": _f("Savings"),
        "other": _f("Other"),
    }
    print("\nGoal: 1=general 2=emergency 3=debt 4=big purchase")
    g = input("Choice [1-4]: ").strip() or "1"
    goals = {"1": "general", "2": "emergency_fund", "3": "debt_payoff", "4": "big_purchase"}
    goal = goals.get(g, "general")

    b = BudgetInput(monthly_income=income, expenses=expenses, goal=goal)
    print("\nAnalyzing…\n")
    out = analyze_budget(b)

    print("output_source:", out.get("output_source"))
    print("\n--- financial_advice ---\n", (out.get("financial_advice") or "")[:1200])
    print("\n--- quiz_question ---\n", out.get("quiz_question", ""))
    print("\n--- grounded_tip ---\n", out.get("grounded_tip", ""))

    if os.getenv("DEMO_JSON", "").strip() in ("1", "true", "yes"):
        print("\n", json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
